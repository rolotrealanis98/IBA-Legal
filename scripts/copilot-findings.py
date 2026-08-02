#!/usr/bin/env python3
"""Every Copilot code-review finding on a PR — inline AND suppressed — as one flat list.

Copilot re-reviews the whole diff on each push and collapses repeats into a
"Suppressed comments" <details> block in the review body, so no single round holds
the full picture. This unions every round and dedupes by file:line (first wins),
then drops threads already marked resolved.

Usage: copilot-findings.py [<pr>] [--repo owner/name] [--include-resolved] [--json]
"""
import argparse, json, re, subprocess, sys

SUP_BLOCK = re.compile(
    r'<details>\s*<summary>\s*(?:Comments s|S)uppressed[^<]*?\(\d+\)\s*</summary>(.*?)</details>',
    re.I | re.S)
SUP_ITEM = re.compile(
    r'\*\*(?P<file>[^*\n]+?):(?P<line>\d+)\*\*\s*\n\*\s*(?P<body>.*?)(?=\n\*\*|\Z)', re.S)
IS_COPILOT = re.compile(r'copilot', re.I)

RESOLVED_Q = """
query($owner:String!,$name:String!,$pr:Int!,$cur:String){
  repository(owner:$owner,name:$name){
    pullRequest(number:$pr){
      reviewThreads(first:100,after:$cur){
        pageInfo{hasNextPage endCursor}
        nodes{
          isResolved
          isOutdated
          comments(first:1){nodes{path line originalLine}}
        }
      }
    }
  }
}
"""

def gh_api(path):
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"gh api {path} failed: {r.stderr.strip()}")
    return json.loads(r.stdout)


def resolved_keys(owner, name, pr):
    """(path, line) of every resolved or outdated review thread."""
    keys, cur = set(), None
    while True:
        cmd = ["gh", "api", "graphql", "-f", f"query={RESOLVED_Q}",
               "-F", f"owner={owner}", "-F", f"name={name}", "-F", f"pr={pr}"]
        if cur:
            cmd += ["-F", f"cur={cur}"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode or '"errors"' in r.stdout:
            print(f"warning: could not read thread resolution state "
                  f"({(r.stderr or r.stdout).strip()[:160]}); showing all findings",
                  file=sys.stderr)
            return set()
        page = json.loads(r.stdout)["data"]["repository"]["pullRequest"]["reviewThreads"]
        for t in page["nodes"]:
            if not (t["isResolved"] or t["isOutdated"]):
                continue
            c = (t["comments"]["nodes"] or [None])[0]
            if c:
                keys.add((c["path"], c["line"] or c["originalLine"]))
        if not page["pageInfo"]["hasNextPage"]:
            return keys
        cur = page["pageInfo"]["endCursor"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pr", nargs="?")
    ap.add_argument("--repo")
    ap.add_argument("--include-resolved", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    sh = lambda c: subprocess.run(c, capture_output=True, text=True).stdout.strip()
    repo = a.repo or sh(["gh", "repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"])
    pr = a.pr or sh(["gh", "pr", "view", "--json", "number", "-q", ".number"])
    if not repo or not pr:
        sys.exit("could not resolve repo/PR — pass them explicitly")
    owner, name = repo.split("/", 1)

    reviews = sorted((r for r in gh_api(f"repos/{repo}/pulls/{pr}/reviews?per_page=100")
                      if IS_COPILOT.search(r["user"]["login"] or "")),
                     key=lambda r: r["submitted_at"] or "")
    if not reviews:
        print(f"No Copilot reviews on {repo}#{pr}.")
        return

    by_review = {}
    for c in gh_api(f"repos/{repo}/pulls/{pr}/comments?per_page=100"):
        if IS_COPILOT.search(c["user"]["login"] or ""):
            by_review.setdefault(c.get("pull_request_review_id"), []).append(c)

    skip = set() if a.include_resolved else resolved_keys(owner, name, int(pr))
    findings, seen = [], set()

    def add(kind, rnd, path, line, body):
        key = (path, line)
        if key in seen or key in skip:
            return
        seen.add(key)
        findings.append({"kind": kind, "round": rnd, "file": path, "line": line,
                         "body": " ".join(body.split())})

    for idx, r in enumerate(reviews, 1):
        for c in by_review.get(r["id"], []):
            add("INLINE", idx, c.get("path"), c.get("line") or c.get("original_line"),
                (c.get("body") or "").strip())
        for block in SUP_BLOCK.findall(r.get("body") or ""):
            for m in SUP_ITEM.finditer(block):
                body = re.sub(r"```.*?```", "", m.group("body"), flags=re.S)
                add("SUPPRESSED", idx, m.group("file").strip(), int(m.group("line")), body)

    if a.json:
        print(json.dumps(findings, indent=2))
        return
    hid = "" if a.include_resolved else f", {len(skip)} resolved/outdated thread(s) hidden"
    print(f"{repo}#{pr} — {len(reviews)} Copilot round(s), "
          f"{len(findings)} open finding(s){hid}\n")
    for f in findings:
        print(f"[{f['kind']:10s}] round {f['round']}  {f['file']}:{f['line']}\n    {f['body']}\n")
    if not findings:
        print("  (nothing open)")


if __name__ == "__main__":
    main()
