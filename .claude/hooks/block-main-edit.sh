#!/bin/bash
# PreToolUse guard: forbid Edit/Write on this repo's default branch (main/master).
#
# Why: when several local agents share one default-branch working tree they stomp each
# other's uncommitted files — multi-agent confusion and overlapping PRs. Each agent/task
# must work in its own git worktree on a feature branch (worktrees are on feature branches,
# so they pass this guard).
#
# Default branch is auto-detected (origin/HEAD → else main/master). Exceptions: plans/, docs/.
# One-off bypass for a deliberate default-branch edit: IBA_ALLOW_MAIN_EDIT=1.
set -uo pipefail

[ "${IBA_ALLOW_MAIN_EDIT:-}" = "1" ] && exit 0

input="$(cat)"
file_path="$(printf '%s' "$input" | jq -r '.tool_input.file_path // .tool_input.notebook_path // empty' 2>/dev/null || true)"
[ -z "$file_path" ] && exit 0

dir="$file_path"
while [ ! -d "$dir" ] && [ "$dir" != "/" ] && [ "$dir" != "." ]; do dir="$(dirname "$dir")"; done

toplevel="$(git -C "$dir" rev-parse --show-toplevel 2>/dev/null || true)"
[ -z "$toplevel" ] && exit 0

cur="$(git -C "$dir" rev-parse --abbrev-ref HEAD 2>/dev/null || true)"
proto="$(git -C "$dir" symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#^origin/##' || true)"
if [ -n "$proto" ]; then
  [ "$cur" = "$proto" ] || exit 0
  protected="$proto"
else
  case "$cur" in main|master) protected="$cur" ;; *) exit 0 ;; esac
fi

rel="${file_path#"$toplevel"/}"
case "$rel" in plans/*|docs/*) exit 0 ;; esac

repo="$(basename "$toplevel")"
cat >&2 <<EOF
BLOCKED: editing '$repo' on its default branch ('$protected') is not allowed.

Concurrent agents collide in the shared default-branch working tree. Work in an isolated
worktree on a feature branch instead:

  git worktree add ../${repo}-wt-<slug> -b <branch> ${protected}
  cd ../${repo}-wt-<slug>
  # re-run your edit here, then open a PR to merge back into '${protected}'.

One-off edit on '${protected}' (docs/config): re-run with IBA_ALLOW_MAIN_EDIT=1 set.
EOF
exit 2
