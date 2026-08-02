#!/usr/bin/env python3
"""Every Copilot code-review finding on a PR — inline AND suppressed — as one flat list.

This repo re-reviews on every push (`review_on_push`), so Copilot re-reads the whole
diff each time and collapses repeats into a "Suppressed comments" <details> block in
the review *body*. Those are not inline comments: the PR page, `gh pr view`, and
`gh api .../pulls/N/comments` all miss them. No single round holds the full picture —
measured on one PR, the final round listed 0 of 45 accumulated findings.

This unions every round, merges inline + suppressed, dedupes (first occurrence wins),
and hides only threads a human explicitly **resolved**. Threads GitHub marks *outdated*
are still shown, tagged `line moved since review` — outdated means the line shifted,
NOT that the issue was fixed.

Suppressed findings have no review thread, so there is nothing to resolve and they
would sit on the list forever even once fixed. `--promote` re-posts them as real review
comments so the whole loop is uniform: fix it, resolve the thread, it drops off.

Usage: copilot-findings.py [<pr>] [--repo owner/name] [--include-resolved] [--json]
                           [--promote]
"""
import argparse, json, re, subprocess, sys

SUP_BLOCK = re.compile(
    r'<details>\s*<summary>\s*(?:Comments s|S)uppressed[^<]*?\(\d+\)\s*</summary>(.*?)</details>',
    re.I | re.S)
# Terminate an item only on the next real "**path:line**" header — a bare "**Impact:**"
# inside a body must not truncate the finding.
ITEM_HEAD = r'\*\*[^*\n]+?:\d+\*\*'
SUP_ITEM = re.compile(r'\*\*(?P<file>[^*\n]+?):(?P<line>\d+)\*\*'
                      r'\s*\n\*\s*(?P<body>.*?)(?=\n' + ITEM_HEAD + r'|\Z)', re.S)

# GitHub reports Copilot under three different logins depending on the surface:
# REST reviews "copilot-pull-request-reviewer[bot]", REST comments "Copilot",
# GraphQL authors "copilot-pull-request-reviewer". Match all three exactly — a
# substring test also swallows unrelated humans like "copilot-helper".
COPILOT_LOGINS = {"copilot-pull-request-reviewer[bot]",
                  "copilot-pull-request-reviewer", "copilot"}
MARK = "<!-- promoted-copilot-finding -->"

THREADS_Q = """
query($owner:String!,$name:String!,$pr:Int!,$cur:String){
  repository(owner:$owner,name:$name){
    pullRequest(number:$pr){
      reviewThreads(first:100,after:$cur){
        pageInfo{hasNextPage endCursor}
        nodes{
          isResolved
          isOutdated
          comments(first:1){nodes{path line originalLine body author{login}}}
        }
      }
    }
  }
}
"""


def is_copilot(login):
    return (login or "").lower() in COPILOT_LOGINS


def gh_list(path):
    """GET a paginated list endpoint and flatten every page."""
    r = subprocess.run(["gh", "api", "--paginate", "--slurp", path],
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"gh api {path} failed: {r.stderr.strip()}")
    return [item for page in json.loads(r.stdout) for item in page]


def thread_state(owner, name, pr):
    """(path, line) -> {resolved, outdated} for Copilot-authored review threads.

    Restricted to Copilot's own threads: a resolved *human* thread at the same
    path:line would otherwise hide an unrelated open Copilot finding.
    """
    state, cur = {}, None
    while True:
        cmd = ["gh", "api", "graphql", "-f", f"query={THREADS_Q}",
               "-F", f"owner={owner}", "-F", f"name={name}", "-F", f"pr={pr}"]
        if cur:
            cmd += ["-F", f"cur={cur}"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode or '"errors"' in r.stdout:
            print(f"warning: could not read thread state "
                  f"({(r.stderr or r.stdout).strip()[:160]}); showing all findings",
                  file=sys.stderr)
            return {}
        page = json.loads(r.stdout)["data"]["repository"]["pullRequest"]["reviewThreads"]
        for t in page["nodes"]:
            c = (t["comments"]["nodes"] or [None])[0]
            if not c:
                continue
            # Promoted threads are authored by us but stand in for a Copilot finding.
            if not (is_copilot((c.get("author") or {}).get("login"))
                    or MARK in (c.get("body") or "")):
                continue
            state[(c["path"], c["line"] or c["originalLine"])] = {
                "resolved": t["isResolved"], "outdated": t["isOutdated"]}
        if not page["pageInfo"]["hasNextPage"]:
            return state
        cur = page["pageInfo"]["endCursor"]


def promote(repo, pr, suppressed):
    """Re-post suppressed findings as review comments so they gain resolvable threads."""
    if not suppressed:
        print("Nothing to promote — no open suppressed findings.")
        return
    head = json.loads(subprocess.run(["gh", "api", f"repos/{repo}/pulls/{pr}"],
                                     capture_output=True, text=True).stdout)["head"]["sha"]
    ok = skipped = 0
    for f in suppressed:
        payload = {"commit_id": head, "path": f["file"], "line": f["line"], "side": "RIGHT",
                   "body": f"{MARK}\n**Copilot (suppressed, round {f['round']}):** {f['body']}"}
        r = subprocess.run(["gh", "api", "-X", "POST", f"repos/{repo}/pulls/{pr}/comments",
                            "--input", "-"], input=json.dumps(payload),
                           capture_output=True, text=True)
        if r.returncode:
            print(f"  skip   {f['file']}:{f['line']} — not anchorable in the current diff")
            skipped += 1
        else:
            print(f"  posted {f['file']}:{f['line']}")
            ok += 1
    print(f"\nPromoted {ok} finding(s) to resolvable threads"
          + (f", {skipped} not anchorable." if skipped else "."))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pr", nargs="?")
    ap.add_argument("--repo")
    ap.add_argument("--include-resolved", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--promote", action="store_true",
                    help="post each open suppressed finding as a review comment so it "
                         "becomes a resolvable thread")
    a = ap.parse_args()

    sh = lambda c: subprocess.run(c, capture_output=True, text=True).stdout.strip()
    repo = a.repo or sh(["gh", "repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"])
    pr = a.pr or sh(["gh", "pr", "view", "--json", "number", "-q", ".number"])
    if not repo or not pr:
        sys.exit("could not resolve repo/PR — pass them explicitly")
    owner, name = repo.split("/", 1)

    reviews = sorted((r for r in gh_list(f"repos/{repo}/pulls/{pr}/reviews?per_page=100")
                      if is_copilot(r["user"]["login"])),
                     key=lambda r: r["submitted_at"] or "")
    if not reviews:
        print("[]" if a.json else f"No Copilot reviews on {repo}#{pr}.")
        return

    by_review = {}
    for c in gh_list(f"repos/{repo}/pulls/{pr}/comments?per_page=100"):
        if is_copilot(c["user"]["login"]):
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

    if a.promote:
        promote(repo, pr, [f for f in findings if f["kind"] == "SUPPRESSED"])
        return
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
