---
layout: layouts/base.njk
title: Privacy Policy
description: How IBA Music (Island Breeze Affiliates Inc.) collects, uses, and protects your information, including our use of the Google Calendar API under the calendar.app.created scope.
permalink: /privacy/
---

## 1. Introduction

This Privacy Policy describes how **Island Breeze Affiliates Inc.**,
a Florida corporation doing business as **IBA Music** ("IBA Music",
"we", "us", or "our"), collects, uses, shares, and protects
information in connection with the products and services listed in
section 1.2 below.

IBA Music is the **data controller** for the information described in
this policy. If you have questions or wish to exercise any right
described here, contact us at
**[privacy@ibamusic.com](mailto:privacy@ibamusic.com)**.

### 1.1 Who this policy is written for

IBA Music's apps and web tools are **business tools for our own
operations**. They are used by musicians contracted to perform for
IBA Music, by band leaders, by IBA Music office staff, and by
authorized contractors. They are **not** general-purpose consumer
products. You are most likely reading this policy because you are
one of those people, because you are a regulator or legal reviewer,
or because you are a Google OAuth verification reviewer assessing
IBA Companion's use of the Google Calendar API.

### 1.2 Products covered by this policy

This policy applies to:

- **IBA Companion** — our mobile app for iOS, iPadOS, macOS,
  watchOS, and Android. Musicians use it to view their performance
  schedule, check in at venues, submit invoice receipts, and
  optionally sync their schedule to Apple Calendar (via EventKit) or
  Google Calendar (via the scope described in section 5).
- **IBA Music Admin Dashboard** at admin.ibamusic.com — the internal
  operations tool used by IBA Music staff to manage performances,
  venues, and musician assignments.
- **IBA Music web tools** — availability forms, the invoice portal,
  and band leader schedule tools used by band leaders and musicians.

If IBA Music launches a new product or service in the future, we will
either update this policy to cover it or publish a separate policy
and link to it from the [Legal Center](/).

## 2. Summary

> **Plain language, up front:** IBA Music does not sell your data.
> We do not use analytics or advertising trackers. We do not read
> your Google calendar — the scope we request only lets IBA Companion
> manage calendars it creates itself. We collect the information we
> need to run live-music performances (schedule, check-ins, invoices)
> and nothing more.

The rest of this policy explains each item in detail.

## 3. Information We Collect

### 3.1 Account information

When you sign in to IBA Companion or any IBA Music web tool, we
receive your name, email address, and (for some providers) a unique
identifier from the sign-in provider you choose: **Apple Sign-In**,
**Google Sign-In**, **Microsoft Sign-In**, or an IBA Music-hosted
email and passkey sign-in.

We use this information to create and maintain your account and to
link you to the musician, staff, or contractor record IBA Music
already has for you. We do not receive your sign-in provider password
and we do not store plaintext passwords of our own.

### 3.2 Profile information

Your musician or staff profile may include: legal name, performing
name or nickname, phone number, emergency contact, instrument(s),
preferred bands, uniform sizes, and similar operational details.
This information is supplied by you or by IBA Music staff on your
behalf. You can request corrections at any time.

### 3.3 Location (GPS)

IBA Companion may request your device location **only when you are
actively checking in to a performance** or when a geofence around a
venue automatically triggers a check-in as you arrive. We use
location to confirm that the check-in is consistent with the venue
we booked — it is a fraud-prevention measure, not a movement tracker.

We do **not** track your location in the background, maintain a
location history outside of check-in records, or share location with
any third party except as noted in section 6. Disabling location
permission in your device settings will prevent the check-in feature
from working but will not affect the rest of the app.

### 3.4 Performance and schedule data

We receive your upcoming performance schedule from IBA Music's
internal booking system. This includes the venue, date, start and
end times, dress code, call time, band name, and any notes relevant
to the performance. This is the core data IBA Companion exists to
display to you.

### 3.5 Check-in and attendance records

When you check in at a venue (manually or via geofence), we record
the timestamp, your location at check-in, the performance you
checked in to, and whether the check-in was on time. IBA Music uses
these records for payroll reconciliation, attendance disputes, and
operational reporting.

### 3.6 Invoice receipts

If you submit an invoice receipt through IBA Companion or the
invoice portal, we store the image you upload (using your device's
standard photo picker — we do **not** scan your photo gallery), the
performance date it relates to, and any metadata you enter (amount,
category, notes). Receipts are retained for the period required by
Florida tax and labor-records law, which is typically seven years.

### 3.7 Device and technical information

- **Push notification tokens.** To send you push notifications about
  schedule changes, check-in reminders, and payroll updates, we
  store the Apple Push Notification service (APNs) device token or
  Firebase Cloud Messaging (FCM) token your device reports.
- **Crash and diagnostic logs.** If the app crashes we may receive a
  minimal diagnostic report (OS version, app version, stack trace)
  to help us fix bugs. We do not knowingly include personal data in
  these reports.

### 3.8 Google Calendar integration data

See section 5 — **Google Calendar Integration** — for a detailed
account of the Google OAuth scope we request, what we do with it,
and what we never access.

## 4. How We Use Information

We use the information described in section 3 to:

- **Provide the service** — show you your performance schedule,
  route push notifications, accept check-ins, process invoice
  uploads, and (if you opt in) keep your calendar in sync.
- **Run internal operations** — payroll, attendance reconciliation,
  performance reporting, customer-service responses to musicians
  who write to us with questions about their schedule.
- **Security and fraud prevention** — detect abusive sign-in
  attempts, investigate suspected fake check-ins, and protect the
  integrity of payroll data.
- **Legal compliance** — respond to lawful subpoenas and court
  orders, comply with tax and labor-law record-keeping, and meet
  other statutory obligations.

We do **not**:

- Sell, rent, or lease your information to anyone for any purpose.
- Use your information to serve advertisements.
- Build behavioral advertising profiles.
- Use your information to train generalized machine-learning models.

## 5. Google Calendar Integration

When you choose to sync your IBA Music performance schedule to
Google Calendar, IBA Companion uses the Google OAuth 2.0
authorization flow to request a single, narrow scope:

**`https://www.googleapis.com/auth/calendar.app.created`**

This scope permits IBA Companion to **create and manage only the
calendars IBA Companion itself creates** in your Google account. It
does not grant access to any calendar you created manually, any
calendar shared with you by another person, or any other Google
service.

### 5.1 What IBA Companion creates

On first sync, IBA Companion creates:

- One primary calendar named **IBA Music** in your Google account.
- Optionally, one sub-calendar per band you perform with, named
  **IBA — {Band Name}** (for example, *IBA — Beach Boys Tribute*).

All events written to those calendars come directly from your
IBA Music performance schedule and contain only: event title, venue
name and address, start and end time, notes (call time, dress code,
parking), and the IBA Music event identifier used to look up the
event on subsequent syncs. We do not write events containing any
information you did not provide to IBA Music in the first place.

### 5.2 What IBA Companion never accesses

IBA Companion **never**:

- Reads any calendar you created manually in Google Calendar.
- Reads any calendar another person has shared with you.
- Accesses event details, attendees, attachments, or descriptions
  from any calendar IBA Companion did not itself create.
- Accesses any other Google service (Gmail, Drive, Contacts, Photos,
  Maps, YouTube, Tasks, Keep, or any other).

The `calendar.app.created` scope is **technically incapable** of
reading user-created or shared calendars — the Google Calendar API
refuses such requests at the server. IBA Companion requests no other
Google scope, so there is no other API path by which we could reach
your data.

### 5.3 Google API Services User Data Policy — Limited Use

IBA Music's use of information received from Google APIs adheres to
the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy),
including the [Limited Use](https://developers.google.com/terms/api-services-user-data-policy#additional_requirements_for_specific_api_scopes)
requirements. In plain English:

- **No advertising.** We do not use Google user data — including the
  contents of any calendar IBA Companion creates on your behalf — to
  serve ads of any kind.
- **No selling.** We do not transfer Google user data to third
  parties for money or any other consideration.
- **No AI or ML training.** We do not use Google user data to
  develop, improve, or train generalized machine-learning models.
- **No human reading.** IBA Music personnel do not read the contents
  of calendars created through the Google Calendar integration
  except (a) with your explicit consent, typically for a support
  request you opened; (b) for a narrow security investigation where
  doing so is necessary to protect you or IBA Music; or (c) where
  required by law.

### 5.4 Revoking access

You can revoke IBA Companion's Google Calendar access at any time:

- **Inside IBA Companion:** open Settings → Calendar Sync → and
  choose **Disconnect Google**.
- **In your Google account:** visit
  [myaccount.google.com/permissions](https://myaccount.google.com/permissions)
  and remove IBA Companion.

Either action immediately stops IBA Companion from reading or writing
any Google Calendar data.

### 5.5 What happens to the calendars after revocation

The **IBA Music** calendar and any **IBA — {Band Name}**
sub-calendars IBA Companion created remain in your Google account
under **your sole control** after revocation. IBA Companion can no
longer add, edit, or remove events in them. You can delete these
calendars entirely from [calendar.google.com](https://calendar.google.com)
at any time. IBA Music does not retain an independent copy of Google
user data on our servers — your performance schedule is stored in
our own database and is the source we push to Google Calendar, not
the other way around.

## 6. Information We Share

We share information only with the sub-processors we need in order
to operate the service. We never sell personal information, share it
for cross-context behavioral advertising, or permit any third party
to use your information for its own marketing purposes.

| Sub-processor | Purpose |
|---|---|
| **Apple Inc.** | Apple Push Notification service (APNs), Apple Sign-In, and EventKit for optional Apple Calendar sync on iOS/iPadOS/macOS/watchOS. |
| **Google LLC** | Google Calendar API via the `calendar.app.created` scope (opt-in calendar sync), Google Sign-In for authentication, Firebase Cloud Messaging (FCM) for Android push. |
| **Microsoft Corporation** | Microsoft Sign-In (Azure Active Directory) and Microsoft Graph — used on the IBA Music admin side to sync performance bookings with Microsoft 365 calendars belonging to IBA Music staff. Not used for musician-facing features. |
| **Cloudflare, Inc.** | Edge hosting for admin.ibamusic.com and related tools, database storage (Cloudflare D1), object storage for receipt images (Cloudflare R2), and hosting for this legal subdomain itself. Cloudflare processes data on IBA Music's behalf; its own use of the data is governed by its contractual role as a processor. |

We also disclose information when we reasonably believe disclosure
is necessary to comply with a lawful subpoena, court order, or
similar legal process; to investigate fraud, security incidents, or
violations of our [Terms of Service](/terms); or to protect the
rights, property, or safety of IBA Music, our musicians, or the
public. We will contest overbroad legal demands where we believe
doing so is proper and practical.

## 7. Data Retention

| Category | Retention |
|---|---|
| Account profile | Until you close your account, plus up to 30 days to complete deletion. |
| Performance and attendance records | Seven (7) years, consistent with Florida tax and labor-records requirements. |
| Invoice receipts | Seven (7) years. |
| Location records (check-ins) | Seven (7) years alongside the associated attendance record. We do not maintain location history outside of check-in transactions. |
| Push notification tokens | Until the token is invalidated by your device or you sign out. |
| Crash and diagnostic logs | Up to 90 days. |
| Google Calendar data | Not stored on IBA Music servers. Events live in your Google account; we write to them but do not keep a mirror. |

## 8. Your Rights

Regardless of where you live, you may request:

- **Access** — a copy of the personal information we hold about you.
- **Correction** — a fix for inaccurate or incomplete information.
- **Deletion** — removal of your information, subject to our
  retention obligations under section 7.
- **Portability** — a machine-readable export.
- **Objection and withdrawal of consent** — an end to processing
  based on your consent, where consent is the lawful basis.

Send requests to
**[privacy@ibamusic.com](mailto:privacy@ibamusic.com)** from the
email address on file with your account, or use another method
reasonable to verify your identity. We respond within the time
frames required by applicable law.

## 9. European Economic Area, United Kingdom, and Switzerland (GDPR)

If you are located in the European Economic Area, the United Kingdom,
or Switzerland, the following additional information applies.

- **Data controller:** Island Breeze Affiliates Inc., Florida, USA.
- **Lawful bases for processing:**
    - *Contract performance* — operating IBA Companion and admin
      tools so you can do the work you were hired to do.
    - *Legitimate interests* — running IBA Music's business safely,
      preventing fraud, investigating security incidents, and
      meeting tax and labor-law record-keeping.
    - *Consent* — specifically for the optional Google Calendar
      integration and any future marketing communications.
    - *Legal obligation* — meeting requirements of Florida and US
      federal tax, labor, and civil law.
- **International transfer:** IBA Music is based in the United
  States and uses US-based and globally-distributed sub-processors.
  Transfers of EEA/UK/Swiss personal data to the United States are
  made in reliance on the Standard Contractual Clauses published by
  the European Commission and (where applicable) the EU–US Data
  Privacy Framework.
- **Right to complain:** you may lodge a complaint with your local
  supervisory authority. In the UK that is the ICO
  (ico.org.uk). We prefer that you contact us first so we have a
  chance to resolve the concern directly.

We do not currently maintain an EU representative because IBA Music's
operations are focused on Florida, USA. We will appoint one if our
processing reaches the thresholds that require it under Article 27
GDPR.

## 10. California (CCPA / CPRA)

If you are a California resident, the following additional
information applies.

- **Categories of personal information we collect:** identifiers
  (name, email, account ID), contact information (phone, address),
  employment-related information (performances, check-ins, invoices),
  geolocation (precise, only at check-in), internet activity
  (technical logs), and inferences drawn from the foregoing for
  the limited purpose of running the service.
- **Categories sold or shared for cross-context behavioral
  advertising:** **None.** IBA Music does not sell personal
  information and does not share it for cross-context behavioral
  advertising.
- **Sources:** you, IBA Music staff acting on your behalf, and the
  devices you use to interact with the service.
- **Retention:** see section 7.
- **Your rights:** you may request to know, delete, correct, and
  limit use of sensitive personal information (which, for our
  purposes, means your precise geolocation at check-in). Contact
  us at [privacy@ibamusic.com](mailto:privacy@ibamusic.com) to
  exercise any right. We do not discriminate against users who
  exercise rights under the CCPA.

## 11. Children's Privacy

IBA Music's apps and services are **not directed to children under
13 years of age**, and we do not knowingly collect personal
information from anyone under 13. IBA Music contracts musicians who
are adults; users of our apps are expected to be at least 18.

If you believe a child under 13 has provided personal information to
us, please contact
[privacy@ibamusic.com](mailto:privacy@ibamusic.com) and we will
delete the information promptly.

## 12. Security

We take reasonable measures to protect information against
unauthorized access, use, disclosure, alteration, and destruction:

- All traffic between your device and our servers is encrypted with
  **TLS 1.2 or higher**.
- Data at rest in Cloudflare D1 and R2 is encrypted by Cloudflare
  using industry-standard algorithms.
- OAuth tokens on mobile devices are stored in the **iOS Keychain**
  or **Android Keystore**, protected by the operating system's
  hardware-backed security.
- Authentication uses OAuth 2.0 (Apple, Google, Microsoft) or
  **WebAuthn passkeys**. We do not store plaintext passwords for
  any account.
- Access to the IBA Music admin dashboard requires sign-in and is
  limited to authorized IBA Music personnel.

No security measure is perfect, and we cannot guarantee the
security of information transmitted over the internet. If you
believe your account has been compromised or you have identified a
vulnerability in our services, please email
[privacy@ibamusic.com](mailto:privacy@ibamusic.com) — see the
[Security](/security) page for our responsible disclosure policy.

## 13. Changes to This Policy

We may update this Privacy Policy from time to time. When we do, we
will update the "Last updated" date at the top of the page. For
material changes — changes that expand the categories of data we
collect, change how we share it, or meaningfully reduce your rights —
we will notify registered users by email or in-app notice at least
30 days before the change takes effect where practical. Your
continued use of the service after the effective date means you
accept the updated policy.

## 14. Contact

For any question about this Privacy Policy or to exercise any right
described here, contact:

**Island Breeze Affiliates Inc.** (d/b/a IBA Music)
Privacy inquiries:
[privacy@ibamusic.com](mailto:privacy@ibamusic.com)
Jurisdiction: Florida, USA

A physical mailing address will be provided on request to
[privacy@ibamusic.com](mailto:privacy@ibamusic.com) or on this page
at a later date.
