---
layout: layouts/base.njk
title: Open Source Licenses
description: Third-party open source software used by IBA Music products and this legal subdomain, with attribution.
permalink: /licenses/
---

IBA Music and this legal subdomain use open source software. This
page lists the major third-party components and links to their
licenses so you can review the attributions and the terms under
which they are distributed.

Nothing on this page alters your rights as a user of any IBA Music
product — those rights are governed by our [Terms of
Service](/terms) and the [Privacy Policy](/privacy). The open
source licenses below govern only the relationship between IBA
Music and the respective upstream project maintainers.

## IBA Companion (iOS / iPadOS / macOS / watchOS)

The authoritative, up-to-date acknowledgements list for the
IBA Companion iOS app is visible inside the app itself, under
**Settings → About → Acknowledgements**. The list below is a
convenience mirror.

| Project | License | Upstream |
|---|---|---|
| **GoogleSignIn-iOS** | Apache License 2.0 | [github.com/google/GoogleSignIn-iOS](https://github.com/google/GoogleSignIn-iOS) |
| **AppAuth-iOS** *(transitive via GoogleSignIn)* | Apache License 2.0 | [github.com/openid/AppAuth-iOS](https://github.com/openid/AppAuth-iOS) |
| **GTMAppAuth** *(transitive via GoogleSignIn)* | Apache License 2.0 | [github.com/google/GTMAppAuth](https://github.com/google/GTMAppAuth) |
| **GTMSessionFetcher** *(transitive via GoogleSignIn)* | Apache License 2.0 | [github.com/google/gtm-session-fetcher](https://github.com/google/gtm-session-fetcher) |

All other app code is proprietary to IBA Music. The app relies on
first-party Apple frameworks (SwiftUI, EventKit, Core Location,
User Notifications, ASAuthorization, PhotoKit) which are licensed
by Apple under the Apple Developer Program License Agreement.

## IBA Companion (Android)

The in-app acknowledgements screen is the authoritative list. If
you need a written list for compliance purposes, email
[privacy@ibamusic.com](mailto:privacy@ibamusic.com) and we will
send the current manifest.

## IBA Music admin dashboard and satellite web tools

The IBA Music admin dashboard and its satellite web tools
(availability forms, invoice portal, band leader tools) are built
on a hand-rolled stack that includes some open source components.
Notable dependencies include:

- **Alpine.js** — MIT License — [github.com/alpinejs/alpine](https://github.com/alpinejs/alpine)
- **Tailwind CSS** — MIT License — [github.com/tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)
- **Hono** — MIT License — [github.com/honojs/hono](https://github.com/honojs/hono)
- **FullCalendar** — MIT License (core) — [github.com/fullcalendar/fullcalendar](https://github.com/fullcalendar/fullcalendar)
- **Chart.js** — MIT License — [github.com/chartjs/Chart.js](https://github.com/chartjs/Chart.js)
- **Phosphor Icons** — MIT License — [github.com/phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)
- **Lucide** — ISC License — [github.com/lucide-icons/lucide](https://github.com/lucide-icons/lucide)

All of the above MIT- and ISC-licensed projects are used under
their respective license terms, which grant broad permission to
use, copy, modify, and distribute the software subject to the
retention of the license text and copyright notice.

## This legal subdomain (legal.ibamusic.com)

The site you are reading is built from the public
[rolotrealanis98/IBA-Legal](https://github.com/rolotrealanis98/IBA-Legal)
repository using these open source build-time dependencies:

| Project | License | Upstream |
|---|---|---|
| **@11ty/eleventy** | MIT License | [github.com/11ty/eleventy](https://github.com/11ty/eleventy) |
| **wrangler** (Cloudflare) | MIT License | [github.com/cloudflare/workers-sdk](https://github.com/cloudflare/workers-sdk) |

Neither of these dependencies is shipped to the browser — they run
only on the build machine. The HTML, CSS, and Markdown source files
in the repository are the entirety of what the browser receives.

## License text

The full text of the MIT, ISC, and Apache 2.0 licenses referenced
above can be read at:

- **MIT** — [opensource.org/license/mit](https://opensource.org/license/mit)
- **ISC** — [opensource.org/license/isc-license-txt](https://opensource.org/license/isc-license-txt)
- **Apache 2.0** — [apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)

For the exact license text that shipped with each specific version
of a library, visit its upstream repository link above.

## Corrections and attribution requests

If you maintain an open source project IBA Music uses and you would
like to request a correction to the attribution, or if we have
missed a project that belongs on this list, please email
[privacy@ibamusic.com](mailto:privacy@ibamusic.com).
