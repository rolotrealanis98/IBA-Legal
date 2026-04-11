// Eleventy 3.x configuration for legal.ibamusic.com
// Ships pure static HTML — no client-side JS, no tracking, no CDN assets.

import { gitCommitDate } from "./lib/git-commit-date.mjs";

export default function (eleventyConfig) {
  // Copy stylesheets and CF Pages control files into the build output verbatim.
  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });
  eleventyConfig.addPassthroughCopy({ "src/_headers": "_headers" });
  eleventyConfig.addPassthroughCopy({ "src/robots.txt": "robots.txt" });
  // RFC 9116 security.txt lives under the well-known URI prefix so
  // security researchers and automated scanners can discover it.
  eleventyConfig.addPassthroughCopy({ "src/.well-known": ".well-known" });

  // Filter: `{{ page.inputPath | gitCommitIso }}` → ISO-8601 string for
  // the `<time datetime="...">` attribute. Reads the git log of the
  // page's source file — no hardcoded dates anywhere.
  eleventyConfig.addFilter("gitCommitIso", (inputPath) => {
    return gitCommitDate(inputPath).iso;
  });

  // Filter: `{{ page.inputPath | gitCommitHuman }}` → "April 11, 2026"
  // for the visible "Last updated" footer text.
  eleventyConfig.addFilter("gitCommitHuman", (inputPath) => {
    return gitCommitDate(inputPath).human;
  });

  return {
    dir: {
      input: "src",
      includes: "_includes",
      data: "_data",
      output: "_site",
    },
    templateFormats: ["md", "njk", "html"],
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    pathPrefix: "/",
  };
}
