---
layout: layouts/base.njk
title: IBA Companion — by Island Breeze Affiliates Inc. (IBA Music)
description: IBA Companion is the private companion app for musicians contracted to IBA Music. Musicians use it to view their performance schedule, check in at venues, submit invoice receipts, and optionally sync their schedule to Google Calendar or Apple Calendar. This page is the app home page and legal document directory.
permalink: /
---

**IBA Companion** is the private companion mobile app operated by
**Island Breeze Affiliates Inc.** (d/b/a **IBA Music**), a Florida
live-music performance company. This page is IBA Companion's
official home page and the directory for every legal document that
covers the app.

**Quick links to required policies:**
[Privacy Policy](https://legal.ibamusic.com/privacy/) ·
[Terms of Service](https://legal.ibamusic.com/terms/) ·
[Contact](https://legal.ibamusic.com/contact/)

## What IBA Companion is

IBA Companion is a **private-use app for musicians contracted to
IBA Music**. It is not a general-purpose consumer product and is
not distributed to the public at large — it is only used by people
who already have an active performance, staff, or contractor
relationship with IBA Music.

The app is published for **iPhone, iPad, Mac (Apple Silicon),
Apple Watch, and Android**. Across all of those platforms it
provides the same core feature set.

## What IBA Companion does

IBA Companion lets an IBA Music musician:

- **View the performance schedule** that IBA Music has booked for
  them — venue, date, start and end time, call time, dress code,
  parking notes, and the band they are performing with.
- **Check in at the venue** when they arrive, either by tapping a
  **Check In** button or by opting in to a geofence that records
  their arrival automatically. Check-ins are used for attendance
  verification and payroll reconciliation, not for tracking.
- **Submit invoice receipts** (admin and band-leader roles only)
  by taking a photo with the device camera or picking an image
  from the device's photo library. Receipts are attached to
  expense lines for payroll processing.
- **Receive operational push notifications** — schedule changes,
  check-in reminders, and payroll updates. Push is optional and
  can be disabled in device settings. IBA Music does not send
  advertising notifications.
- **Optionally sync the schedule to a calendar** — either to the
  device's native **Apple Calendar** through Apple's EventKit
  framework, or to **Google Calendar** through a narrowly-scoped
  Google OAuth integration described in the next section.
- **Rehearse setlists in the Practice tab** with separated
  multitrack audio stems provided by IBA Music. Downloads are
  cached on-device only, auto-delete on a TTL, and are never
  uploaded anywhere by the musician.
- **See a Set Tracker Live Activity during a performance** with
  set-by-set timing on the lock screen and in the Dynamic Island.

## How IBA Companion uses Google API data

The Google Calendar sync feature is **opt-in**. When a musician
chooses to enable it, IBA Companion uses the Google OAuth 2.0
authorization flow to request a single, narrow scope:

**`https://www.googleapis.com/auth/calendar.app.created`**

This scope lets IBA Companion create and manage **only the
calendars IBA Companion itself creates** in the user's Google
account. It does **not** allow reading, writing, or deleting any
calendar the user created manually or that was shared with them
by another person. IBA Companion creates:

- One primary calendar named **IBA Music** in the user's Google
  account, and
- Optionally, one sub-calendar per band, named
  **IBA — {Band Name}** (for example, *IBA — Beach Boys Tribute*).

Events written to those calendars are drawn from the user's own
IBA Music performance schedule. IBA Companion **never**:

- Reads any calendar the user created manually
- Reads any calendar shared with the user by another person
- Accesses Gmail, Drive, Contacts, Photos, Maps, YouTube, or any
  other Google service

IBA Music's use of information received from Google APIs adheres
to the
[Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy),
including the [Limited Use requirements](https://developers.google.com/terms/api-services-user-data-policy#additional_requirements_for_specific_api_scopes).
No Google user data is sold, shared with third parties for
advertising, or used to train generalized machine-learning models.

The full disclosure of the Google Calendar integration — including
what can be done with it, how to revoke it, and what happens to
calendars after revocation — is in
[Privacy Policy §5 — Google Calendar Integration](https://legal.ibamusic.com/privacy/).

## Legal documents for IBA Companion

All legal documents that apply to IBA Companion, the IBA Music
admin dashboard, and IBA Music's other web tools are published on
this subdomain:

- **[Privacy Policy](https://legal.ibamusic.com/privacy/)** — What
  data IBA Companion collects, how we use it, how we share it,
  and how the Google Calendar scope (`calendar.app.created`) is
  used.
- **[Terms of Service](https://legal.ibamusic.com/terms/)** —
  Rules for using IBA Companion and IBA Music web tools. Governed
  by Florida law. Includes a binding arbitration clause with a
  30-day opt-out for new users.
- **[Cookie Policy](https://legal.ibamusic.com/cookies/)** — How
  (and whether) cookies are used. This legal subdomain sets no
  cookies at all; the admin dashboard uses session cookies only.
- **[Sub-processors](https://legal.ibamusic.com/subprocessors/)** —
  The third-party providers (Apple, Google, Microsoft, Cloudflare)
  that process personal data on IBA Music's behalf.
- **[Open Source Licenses](https://legal.ibamusic.com/licenses/)** —
  Attribution for the open source software used by IBA Companion.
- **[Security](https://legal.ibamusic.com/security/)** — Security
  practices and the responsible-disclosure process. A
  machine-readable contact is also published at
  [/.well-known/security.txt](https://legal.ibamusic.com/.well-known/security.txt)
  per RFC 9116.
- **[Contact](https://legal.ibamusic.com/contact/)** — How to reach
  IBA Music for privacy, legal, or security matters.

## About IBA Music (the operator)

The app is built and operated by **Island Breeze Affiliates Inc.**
(d/b/a IBA Music), a corporation organized under the laws of the
State of **Florida, USA**. IBA Music books and manages live-music
performances at venues including theme parks, resorts, private
events, and concert venues. IBA Companion is an internal tool for
the musicians, band leaders, and office staff who deliver those
performances.

## Contact

Privacy, legal, and security inquiries:
**[privacy@ibamusic.com](mailto:privacy@ibamusic.com)**

If you believe you have reached this site in error — IBA Companion
is not a general-purpose consumer app and is not available through
the public App Store listings without a valid IBA Music
invitation — you can safely close this tab.

---

*This page serves as both the IBA Companion application home page
(as referenced in the Google Cloud Console OAuth consent screen)
and as the directory for every legal document that governs the app.
It is published as part of Google's OAuth verification requirements
for sensitive-scope applications.*
