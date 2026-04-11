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

IBA Companion uses your device's precise location for **one purpose
only**: to verify that you are physically present at the venue where
IBA Music booked you to perform, at the time of check-in. There are
two ways a check-in can trigger:

1. **Manual check-in** — you tap **Check In** on your upcoming
   performance. IBA Companion requests your current location once
   and compares it against the venue's coordinates.
2. **Automatic geofence check-in** *(optional)* — you can enable
   geofence auto-checkin, which asks iOS to notify IBA Companion
   when you enter a small region centered on the venue for your
   upcoming performance. When iOS fires that region-enter event,
   IBA Companion records your arrival automatically so you don't
   have to remember to tap Check In.

#### iOS location permissions we request

On iOS, iPadOS, and watchOS, IBA Companion asks you to grant one or
both of the standard Core Location authorizations:

| Permission | Key | Why we request it | Purpose string shown to you |
|---|---|---|---|
| When-In-Use | `NSLocationWhenInUseUsageDescription` | Manual check-in (tap Check In while the app is open) | *"IBA Companion needs your location to verify you've arrived at the venue for GPS check-in."* |
| Always | `NSLocationAlwaysAndWhenInUseUsageDescription` | Geofence auto-checkin — required because iOS only delivers region-enter events to an authorized app when the app is in the background | *"IBA Companion uses your location to notify you when you arrive at a venue, so you can check in quickly."* |

You can grant **When-In-Use only** (manual check-in works; auto
check-in does not), grant **Always** (both work), or deny both
(neither location feature works, but the rest of the app continues
to function normally).

On the IBA Companion **Apple Watch app**, IBA Companion requests
When-In-Use only, to confirm your arrival from your watch without
unlocking your phone. On **macOS**, IBA Companion does not use
location services at all — the Mac app is read-only for schedule
viewing.

#### What we do with location data

- We request **precise location**
  (`kCLLocationAccuracyBest`) because venue-matching accuracy of
  tens of meters is necessary — adjacent Disney-resort venues can
  be within 100 meters of one another. We do not collect
  reduced-accuracy location and do not currently expose a
  reduced-accuracy toggle.
- Location fixes are taken **only during a check-in transaction**
  — IBA Companion does not log a continuous location history, does
  not track your movement between venues, and does not retain
  location points outside of check-in records.
- Geofence regions are created for your upcoming performances only,
  up to the iOS system limit of 20 simultaneously monitored
  regions. They are removed as soon as the performance ends.
- The `location` background mode is declared in IBA Companion's
  `Info.plist` so iOS can deliver region-enter events while the app
  is in the background. IBA Companion does **not** use that
  background mode to poll your location, build a movement profile,
  or share live location with anyone. It is used only to complete
  check-in bookkeeping when iOS wakes the app on arrival.

#### Sharing

Location data associated with check-ins is stored in IBA Music's
own database on Cloudflare D1 and is used only as described in
section 4. We do **not** transfer location data to any advertising
network, data broker, analytics provider, or third party other
than the sub-processors listed in section 7. We do not sell it.

#### How to turn it off

Go to **Settings → Privacy & Security → Location Services → IBA
Companion** on your iOS or iPadOS device to change or revoke
permission at any time. Disabling location will prevent the
check-in feature from working but will not affect schedule viewing,
calendar sync, invoice submission, or any other part of the app.

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

### 3.6 Invoice receipts (camera and photo library)

If you have an IBA Music role that submits expense receipts
(typically administrators and band leaders), IBA Companion includes
a receipt-capture flow. You can:

- **Take a new photo** with the device camera — iOS shows the
  standard camera permission prompt
  (`NSCameraUsageDescription`: *"Camera required for Admins,
  Receipt upload feature."*). The camera is invoked only when you
  explicitly choose **Take photo**.
- **Pick an existing photo** from your photo library using the
  standard iOS photo picker (`PHPickerViewController` / SwiftUI
  `PhotosPicker`). The photo picker is a system component that
  runs outside IBA Companion's sandbox — IBA Companion receives
  only the image you select and **never scans, lists, or sees the
  rest of your photo library**. Because of this, IBA Companion
  does **not** request `NSPhotoLibraryUsageDescription` and iOS
  does not show a library-access prompt.

We store the receipt image you provide, the expense line it is
associated with, and any metadata you enter (amount, category,
notes). Receipts are retained for the period required by Florida
tax and labor-records law, which is typically seven years.

Invoice receipts are **user-generated content** under IBA Music's
[Terms of Service](/terms). They are visible only to you and to
authorized IBA Music staff — they are never published, shared with
other musicians, or used for any purpose other than expense
reconciliation, payroll, and tax records.

### 3.7 Device and technical information

- **Push notification tokens.** If you grant notification permission
  (the standard iOS prompt) IBA Companion registers for remote
  notifications with Apple and hands us the Apple Push Notification
  service (APNs) device token your device reports. We store that
  token so IBA Music's backend can deliver operational push
  notifications — schedule changes, check-in reminders, payroll
  updates. We do **not** send marketing or advertising push
  notifications. On Android, the equivalent token is a Firebase
  Cloud Messaging (FCM) token; the purpose and handling are
  identical.
- **Background delivery modes.** IBA Companion declares the
  `remote-notification` background mode so push payloads can wake
  the app to refresh your schedule silently. IBA Companion does
  **not** declare `audio`, `voip`, `external-accessory`,
  `bluetooth-central`, or any other background mode that would
  allow long-running background execution beyond what is required
  for push refresh and geofence arrival events (section 3.3).
- **Crash and diagnostic logs.** IBA Companion does not integrate
  Firebase Crashlytics, Sentry, Bugsnag, or any other third-party
  crash-reporting SDK. Crash reports are the ones Apple and Google
  collect on IBA Music's behalf when you opt in to sharing with
  developers through your device settings (Apple's "Share With App
  Developers" toggle, Google Play's "Usage & diagnostics"). Those
  reports are delivered to IBA Music through Apple's App Store
  Connect console and Google Play Console, and are used only to
  find and fix bugs. We do not knowingly include personal data in
  these reports.

### 3.8 Calendar integration data

Calendar sync is **optional** on every platform. Your choices are:

- **Google Calendar** — see section 5 for the exact OAuth scope,
  calendar names created, and Google-specific Limited Use
  commitments.
- **Apple Calendar (EventKit)** — see section 6.1 for the EventKit
  permission we request and how we handle on-device calendar data.

You can use one, both, or neither. Choosing neither does not
disable any other feature of IBA Companion.

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

## 6. Apple Platform Disclosures

This section covers the additional disclosures that Apple App Store
reviewers, App Tracking Transparency rules, and iOS platform
conventions expect IBA Companion to make. It applies to the
IBA Companion app on iPhone, iPad, Mac (Apple Silicon), and Apple
Watch.

### 6.1 Apple Calendar integration (EventKit)

IBA Companion can also sync your performance schedule to your
device's **Apple Calendar** using Apple's EventKit framework. This
is an **on-device, local** integration — the calendar and its events
live in your device's own calendar database (and in iCloud if you
have Apple Calendar iCloud sync enabled through your Apple ID), not
on IBA Music's servers.

When you enable Apple Calendar sync, IBA Companion asks you for
calendar permission. iOS shows the standard prompt with the string
`NSCalendarsFullAccessUsageDescription` —
*"IBA Companion adds your performance schedule directly to your
device calendar so it stays up to date even when the app is
closed."*

We request **full calendar access** (rather than the more limited
"write-only access" introduced in iOS 17) because IBA Companion
needs to **read back** the events it previously wrote so it can
update or delete them when your schedule changes without
duplicating them. IBA Companion reads only the events it itself
created for IBA Music — it identifies them by a stable IBA Music
event identifier stored on each EventKit `EKEvent`. It does **not**
read, modify, delete, or transmit events that belong to any
other calendar source or that were created by any other app.

You can revoke calendar access at any time in **Settings → Privacy
& Security → Calendars → IBA Companion**. Revocation immediately
stops IBA Companion from touching your Apple Calendar. The IBA
Music calendar and any events IBA Companion previously wrote remain
under your sole control — you can delete them from Apple Calendar
whenever you like. IBA Music does not retain a mirror of your
device calendar on our servers.

The EventKit integration runs on iOS, iPadOS, and watchOS.
On **macOS** (Mac Catalyst / Apple Silicon), IBA Companion does not
currently enable the calendar sync feature.

### 6.2 Sign in with Apple

IBA Companion offers **Sign in with Apple** as a first-class
authentication option alongside Google Sign-In, consistent with
App Store Review Guideline 4.8. If you sign in with Apple:

- You may choose to share your real Apple ID email or to use
  **Private Relay** (Apple's email-masking service). Either way,
  IBA Companion treats the address as your account email and sends
  operational email to it.
- If Apple provides a display name to us during the first-time
  sign-in, we store it as your profile name. You can change this
  at any time in the IBA Music admin dashboard or by emailing
  [privacy@ibamusic.com](mailto:privacy@ibamusic.com).
- Apple assigns IBA Music a stable "user identifier" that is
  unique to your Apple ID and the IBA Companion app. IBA Music
  stores this identifier to recognize your account on future
  sign-ins. It cannot be used to look you up in any other Apple
  service.

### 6.3 Push notifications (APNs)

Push notifications are **optional**. iOS asks you for permission
the first time IBA Companion tries to register. If you grant it,
IBA Companion registers for remote notifications and hands the
APNs device token to IBA Music's backend so we can deliver
operational notifications to you.

IBA Music uses push notifications **only** for:

- Schedule changes (a performance moved, added, or cancelled)
- Check-in reminders before a performance
- Payroll and invoice status updates
- Critical service announcements from IBA Music operations

We do **not** send advertising notifications, marketing offers,
third-party promotions, or behavioral re-engagement nudges. You
can disable notifications at any time in **Settings →
Notifications → IBA Companion**.

### 6.4 App Tracking Transparency (ATT) and the IDFA

IBA Companion does **not** track you across apps and websites
owned by other companies, and does **not** show the App Tracking
Transparency prompt, because there is nothing to ask permission
for:

- IBA Companion does **not** read, request, or store the
  Identifier for Advertisers (IDFA / `advertisingIdentifier`).
- IBA Companion includes **no advertising SDKs** of any kind —
  no Google Ads Mobile SDK, no Meta Audience Network SDK, no
  AppLovin, no Unity Ads, no Chartboost, no IronSource, none.
- IBA Companion includes **no analytics SDKs** — no Firebase
  Analytics, no Amplitude, no Mixpanel, no Segment, no Hotjar, no
  Sentry, no Crashlytics, none.
- IBA Companion does **not** share any data with third parties
  for cross-app or cross-site advertising. It does not share data
  with data brokers.

Consistent with this, IBA Companion declares in its App Store
privacy report that it does **not** use data to track users and
does **not** perform any of Apple's defined tracking activities.

### 6.5 Account deletion

We treat your right to delete your account seriously and recognize
that the Apple App Store Review Guidelines require apps that
support account creation to also support account deletion.

**How to delete your account today:** email
[privacy@ibamusic.com](mailto:privacy@ibamusic.com) from the email
address on your account and request deletion. We confirm the
request, delete your personal profile, credentials, push tokens,
location records (except where Florida tax and labor law requires
retention — see section 8), and any other personal data not
covered by those retention rules, and send you a confirmation.
We complete deletions within 30 days.

**In-app deletion:** a dedicated "Delete Account" action inside
IBA Companion — tapping it initiates the same deletion flow without
needing to email us — is scheduled to ship in an upcoming release.
Until that release is live, the email path above is the supported
deletion method.

### 6.6 App Store privacy labels — data mapping

Below is how the data described elsewhere in this policy maps to
Apple's App Store privacy-label categories. This exists so App
Store reviewers can cross-check the policy against the privacy
nutrition label displayed on IBA Companion's App Store page.

| Apple category | Items collected | Linked to user? | Used to track? | Purpose |
|---|---|---|---|---|
| **Contact Info** — Name, Email, Phone | Section 3.1, 3.2 | Yes | No | App Functionality |
| **Location** — Precise Location | Section 3.3 | Yes | No | App Functionality |
| **User Content** — Photos (receipts) | Section 3.6 | Yes | No | App Functionality |
| **Identifiers** — User ID (from sign-in provider) | Section 3.1 | Yes | No | App Functionality |
| **Usage Data** | *Not collected* | — | — | — |
| **Diagnostics** — Crash Data, Performance Data | Section 3.7 | No | No | App Functionality |
| **Sensitive Info** | *Not collected* | — | — | — |
| **Financial Info** | *Not collected* | — | — | — |
| **Health & Fitness** | *Not collected* | — | — | — |
| **Contacts** | *Not collected* | — | — | — |
| **Browsing History** | *Not collected* | — | — | — |
| **Search History** | *Not collected* | — | — | — |

"Used to track?" is **No for every category** because IBA Companion
does not perform any of Apple's defined tracking activities (see
section 6.4).

### 6.7 Supported operating systems and upgrade path

IBA Companion supports current major versions of iOS, iPadOS,
watchOS, and macOS, plus the immediately previous major version
where practical. Security fixes target the current version first.
If your device cannot run a supported version, some features —
notably calendar sync, passkeys, and modern privacy prompts — may
not be available. IBA Music does not intentionally limit
functionality on older devices as long as they remain supported by
Apple.

## 7. Information We Share

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

## 8. Data Retention

| Category | Retention |
|---|---|
| Account profile | Until you close your account, plus up to 30 days to complete deletion. |
| Performance and attendance records | Seven (7) years, consistent with Florida tax and labor-records requirements. |
| Invoice receipts | Seven (7) years. |
| Location records (check-ins) | Seven (7) years alongside the associated attendance record. We do not maintain location history outside of check-in transactions. |
| Push notification tokens | Until the token is invalidated by your device or you sign out. |
| Crash and diagnostic logs | Up to 90 days. |
| Google Calendar data | Not stored on IBA Music servers. Events live in your Google account; we write to them but do not keep a mirror. |

## 9. Your Rights

Regardless of where you live, you may request:

- **Access** — a copy of the personal information we hold about you.
- **Correction** — a fix for inaccurate or incomplete information.
- **Deletion** — removal of your information, subject to our
  retention obligations under section 8.
- **Portability** — a machine-readable export.
- **Objection and withdrawal of consent** — an end to processing
  based on your consent, where consent is the lawful basis.

Send requests to
**[privacy@ibamusic.com](mailto:privacy@ibamusic.com)** from the
email address on file with your account, or use another method
reasonable to verify your identity. We respond within the time
frames required by applicable law.

## 10. European Economic Area, United Kingdom, and Switzerland (GDPR)

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

## 11. California (CCPA / CPRA)

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
- **Retention:** see section 8.
- **Your rights:** you may request to know, delete, correct, and
  limit use of sensitive personal information (which, for our
  purposes, means your precise geolocation at check-in). Contact
  us at [privacy@ibamusic.com](mailto:privacy@ibamusic.com) to
  exercise any right. We do not discriminate against users who
  exercise rights under the CCPA.

## 12. Children's Privacy

IBA Music's apps and services are **not directed to children under
13 years of age**, and we do not knowingly collect personal
information from anyone under 13. IBA Music contracts musicians who
are adults; users of our apps are expected to be at least 18.

If you believe a child under 13 has provided personal information to
us, please contact
[privacy@ibamusic.com](mailto:privacy@ibamusic.com) and we will
delete the information promptly.

## 13. Security

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

## 14. Changes to This Policy

We may update this Privacy Policy from time to time. When we do, we
will update the "Last updated" date at the top of the page. For
material changes — changes that expand the categories of data we
collect, change how we share it, or meaningfully reduce your rights —
we will notify registered users by email or in-app notice at least
30 days before the change takes effect where practical. Your
continued use of the service after the effective date means you
accept the updated policy.

## 15. Contact

For any question about this Privacy Policy or to exercise any right
described here, contact:

**Island Breeze Affiliates Inc.** (d/b/a IBA Music)
Privacy inquiries:
[privacy@ibamusic.com](mailto:privacy@ibamusic.com)
Jurisdiction: Florida, USA

A physical mailing address will be provided on request to
[privacy@ibamusic.com](mailto:privacy@ibamusic.com) or on this page
at a later date.
