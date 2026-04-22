---
layout: layouts/base.njk
title: Security
description: IBA Music's security practices and responsible disclosure policy for security researchers.
permalink: /security/
---

IBA Music takes the security of its systems and the data entrusted
to it seriously. This page describes the high-level security
measures we use and how to report a suspected vulnerability.

## Our security practices

### Transport security

All traffic between users and IBA Music services is encrypted with
**TLS 1.2 or higher** using modern cipher suites. Plaintext HTTP
requests are redirected to HTTPS. HTTP Strict Transport Security
(HSTS) is applied to the legal subdomain and our primary production
hosts.

### Authentication

- **No plaintext passwords.** IBA Music does not store plaintext
  passwords for any account.
- **OAuth 2.0.** Users sign in via Apple Sign-In, Google Sign-In, or
  Microsoft Sign-In (Azure Active Directory).
- **Passkeys (WebAuthn).** Where supported, we prefer passkey
  authentication backed by the device's secure enclave or hardware
  security module.
- **Session tokens** expire on a rolling basis and are bound to the
  device that requested them where possible.
- **Rate limiting** is applied to authentication endpoints to slow
  credential-guessing and enumeration attempts.

### Data at rest

- Primary relational data is stored in **Cloudflare D1** and is
  encrypted at rest by Cloudflare.
- File uploads (invoice receipts, profile photos) and IBA Music's
  multitrack audio stems used by the Practice feature are stored
  in **Cloudflare R2** and are encrypted at rest by Cloudflare.
- OAuth refresh tokens and other secrets on mobile devices are
  stored in the **iOS Keychain** or **Android Keystore** with
  hardware-backed protection where the device supports it.

### Infrastructure

- The Service runs on **Cloudflare's global edge network** under
  IBA Music's own Cloudflare account. Workers and Pages projects
  are deployed with least-privilege service bindings.
- Access to the IBA Music admin dashboard is gated by sign-in and
  role-based access control; sensitive actions require elevated
  authorization.
- Source code is maintained in private GitHub repositories. This
  legal subdomain's repository (github.com/rolotrealanis98/IBA-Legal)
  is public to allow Google OAuth verification reviewers and
  regulators to inspect the source of the policies they read here.

### Privacy by design

We keep the minimum data necessary to run the Service. We do not
use third-party analytics or advertising trackers on any IBA Music
product. See our [Privacy Policy](/privacy) for the full
description.

## Reporting a vulnerability

If you believe you have found a security vulnerability in any
IBA Music product or web property, **please email us before
disclosing it publicly**:

**[privacy@ibamusic.com](mailto:privacy@ibamusic.com)**
(Subject line: "Security — {brief description}")

Include, to the extent you can:

- A clear description of the vulnerability and the affected
  product, URL, or API endpoint.
- Steps to reproduce, or a small proof-of-concept.
- Your name (or handle, if you prefer) and a way to reach you for
  follow-up questions.
- Whether you would like public credit if we choose to publish a
  fix advisory, and how you would like to be credited.
- Any recommendations you have for remediation.

We commit to:

- **Acknowledge** your report within **5 business days**.
- **Investigate** in good faith and keep you reasonably informed of
  our progress.
- **Not pursue legal action** against researchers who act in good
  faith, who do not exfiltrate data beyond what is necessary to
  demonstrate the issue, who do not disrupt the Service, and who
  give us a reasonable window to remediate before public
  disclosure.
- **Provide a remediation timeline** or, if we decide not to fix an
  issue, an explanation of our reasoning.

## Scope

In scope for responsible disclosure:

- admin.ibamusic.com and other IBA Music-owned production web
  tools.
- IBA Companion mobile apps (iOS / iPadOS / macOS / watchOS /
  Android) — as published on the App Store and Google Play.
- API endpoints owned by IBA Music at companion.ibamusic.com and
  related subdomains.
- This legal subdomain (legal.ibamusic.com).

Out of scope:

- **Denial-of-service** or volumetric attacks.
- **Social engineering** of IBA Music staff, musicians, or
  contractors.
- **Physical attacks** against IBA Music offices, venues, or
  equipment.
- Findings from **automated scanners** that have not been
  manually validated to demonstrate real impact.
- Issues that require a compromised victim device (root / jailbreak
  / malware already installed).
- Issues in third-party services (Apple, Google, Microsoft,
  Cloudflare, etc.) where IBA Music is not the operator — please
  report those to the vendor directly.

## Public credit

With your permission, we maintain an acknowledgements list for
researchers who have reported valid vulnerabilities and helped us
improve. We do not currently operate a paid bug bounty program.

## Questions

Email [privacy@ibamusic.com](mailto:privacy@ibamusic.com). Thank you
for helping keep IBA Music's musicians and data safe.
