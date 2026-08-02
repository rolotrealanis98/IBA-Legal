#!/usr/bin/env python3
"""Every Copilot code-review finding on a PR — inline AND suppressed — as one flat list.

This repo re-reviews on every push (`review_on_push`), so Copilot re-reads the whole
diff each time and collapses repeats into a "Suppressed comments" <details> block in
the review *body*. Those are not inline comments: the PR page, `gh pr view`, and
`gh api .../pulls/N/comments` all miss them. No single round holds the full picture.

This unions every round, merges inline + suppressed, dedupes (first occurrence wins),
and hides only threads a human explicitly **resolved**. Threads GitHub marks *outdated*
are still shown, tagged `moved` — outdated means the line shifted, NOT that the issue
was fixed, and across many pushes that distinction is the difference between a clean
list and a silently dropped finding.

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


def thread_state(owner, name, pr):
    """(path, line) -> {"resolved": bool, "outdated": bool} for every review thread."""
    state, cur = {}, None
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
            return {}
        page = json.loads(r.stdout)["data"]["repository"]["pullRequest"]["reviewThreads"]
        for t in page["nodes"]:
            c = (t["comments"]["nodes"] or [None])[0]
            if c:
                state[(c["path"], c["line"] or c["originalLine"])] = {
                    "resolved": t["isResolved"], "outdated": t["isOutdated"]}
        if not page["pageInfo"]["hasNextPage"]:
            return state
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

    state = thread_state(owner, name, int(pr))
    findings, seen, resolved_hidden = [], set(), 0

    def add(kind, rnd, path, line, body):
        nonlocal resolved_hidden
        body = " ".join(body.split())
        st = state.get((path, line), {})
        # Dedupe on position AND on wording: re-review restates findings at shifted
        # line numbers, so position alone lets the same defect through twice.
        keys = {(path, line), (path, body[:160])}
        if seen & keys:
            return
        if st.get("resolved") and not a.include_resolved:
            resolved_hidden += 1
            return
        seen.update(keys)
        findings.append({"kind": kind, "round": rnd, "file": path, "line": line,
                         "moved": bool(st.get("outdated")), "body": body})

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
    hid = "" if a.include_resolved else f", {resolved_hidden} resolved thread(s) hidden"
    print(f"{repo}#{pr} — {len(reviews)} Copilot round(s), "
          f"{len(findings)} open finding(s){hid}\n")
    for f in findings:
        tag = "  [line moved since review]" if f["moved"] else ""
        print(f"[{f['kind']:10s}] round {f['round']}  {f['file']}:{f['line']}{tag}\n"
              f"    {f['body']}\n")
    if not findings:
        print("  (nothing open)")


if __name__ == "__main__":
    main()
