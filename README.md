# IBA-Legal

Source for **legal.ibamusic.com** — the public legal-documents subdomain for
**Island Breeze Affiliates Inc.** (d/b/a IBA Music).

This repository exists primarily to satisfy Google OAuth verification for the
IBA Companion iOS app's Google Calendar sync feature. Google requires public,
JavaScript-free Privacy Policy and Terms of Service URLs that specifically
enumerate the OAuth scopes an app uses. Those URLs live on this site.

## Stack

- **[Eleventy 3.x](https://www.11ty.dev)** — static site generator, Markdown source → HTML output
- **[Cloudflare Pages](https://pages.cloudflare.com)** — static hosting at the edge
- **[Wrangler](https://developers.cloudflare.com/workers/wrangler/)** — deploy CLI

No client-side JavaScript. No analytics. No CDN-loaded fonts. No cookies set
by the legal subdomain itself.

## Development

```bash
npm install
npm run dev        # http://localhost:8787
```

Edit Markdown files under `src/`. The base layout lives at
`src/_includes/layouts/base.njk`. Global site data (entity name, URLs, contact
email) lives at `src/_data/site.mjs`.

## Deployment

```bash
npm run deploy
```

This runs `eleventy` to build the `_site/` directory and then
`wrangler pages deploy _site --project-name=iba-legal --branch=main`. Wrangler
must be authenticated (`wrangler login`) against the Cloudflare account that
owns `ibamusic.com`.

There is **no git integration** with Cloudflare Pages. Deploys are explicit,
human-initiated actions from a machine with wrangler credentials.

## "Last updated" dates

The "Last updated" footer on every page is rendered from the git commit time
of that page's Markdown source file, read at build time via
`git log -1 --format=%cI -- <file>`. Editing a page and committing
automatically rolls the date forward — no manual maintenance.

## Pages

| Path | Source | Purpose |
|------|--------|---------|
| `/` | `src/index.md` | Document directory + app home page |
| `/privacy` | `src/privacy.md` | Privacy Policy (includes Google Calendar API disclosure) |
| `/terms` | `src/terms.md` | Terms of Service (Florida governing law) |
| `/cookies` | `src/cookies.md` | Cookie Policy |
| `/security` | `src/security.md` | Security practices + responsible disclosure |
| `/contact` | `src/contact.md` | Privacy / legal / security contact info |

## Headers

`src/_headers` is passed through to Cloudflare Pages to apply a strict
Content-Security-Policy, HSTS, frame-deny, and permissions policy to every
response. No scripts are ever served, so `script-src 'none'` is safe.

## Contact

Privacy, legal, or security questions: **privacy@ibamusic.com**
