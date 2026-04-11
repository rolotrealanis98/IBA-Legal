// Resolve the ISO timestamp and human-readable date for the most recent
// git commit that touched a given file path. Used by eleventy.config.mjs
// to inject "Last updated" footers into every rendered page from git
// history — no hardcoded dates, no manual maintenance.
//
// Falls back to `new Date()` if git is unavailable or the file is
// untracked. Returns an object { iso, human } where:
//   - iso    = strict ISO-8601 for the <time datetime="..."> attribute
//   - human  = human-friendly "April 11, 2026" for visible footer text

import { execFileSync } from "node:child_process";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, "..");

// Cache results so repeated template renders don't re-shell to git.
const cache = new Map();

/**
 * @param {string} inputPath - Eleventy `page.inputPath`, e.g. "./src/privacy.md"
 * @returns {{iso: string, human: string}}
 */
export function gitCommitDate(inputPath) {
  if (!inputPath) return fallback();

  // Eleventy passes "./src/privacy.md". Normalize to an absolute-ish
  // path relative to the repo root so git can locate it.
  const relative = inputPath.replace(/^\.\//, "");

  if (cache.has(relative)) return cache.get(relative);

  let result;
  try {
    const iso = execFileSync(
      "git",
      ["log", "-1", "--format=%cI", "--", relative],
      { cwd: REPO_ROOT, encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] },
    ).trim();

    if (iso) {
      result = formatBoth(new Date(iso));
    } else {
      // File exists in the working tree but has never been committed —
      // happens during first commit. Use current time.
      result = fallback();
    }
  } catch {
    // git is not installed, not in a repo, or shelling out failed.
    result = fallback();
  }

  cache.set(relative, result);
  return result;
}

function fallback() {
  return formatBoth(new Date());
}

function formatBoth(date) {
  return {
    iso: date.toISOString(),
    human: date.toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
      timeZone: "America/New_York",
    }),
  };
}
