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

- **IBA Companion** — our iOS app for iPhone. Musicians use it to
  view their performance schedule, check in at venues, rehearse
  setlists with multitrack stems (Practice), and optionally sync
  their schedule to Apple Calendar (via EventKit) or Google Calendar
  (via the scope described in section 5).
- **IBA Companion for Android** — the native Android edition of the
  same app, distributed through the Google Play Store. It mirrors the
  iOS feature set: viewing the performance schedule, manual venue
  check-in, rehearsing setlists with multitrack stems (Practice), and
  optional schedule sync to the device's calendar. The Android-specific
  platform disclosures — permissions, push, crash reporting, and the
  Google Play Data Safety mapping — are in section 6A.
- **IBA Music Admin Dashboard** at admin.ibamusic.com — the internal
  operations tool used by IBA Music staff to manage performances,
  venues, and musician assignments.
- **IBA Admin** — our iOS app for iPhone. IBA Music office staff and
  authorized administrators use it to manage events, performer
  assignments, venues, availability, and check-in monitoring. Sign-in
  is restricted to the ibamusic.com Microsoft Entra tenant. The
  iOS-specific platform disclosures for this app — permissions,
  sign-in, push, Wallet, calendar export, and the App Store
  privacy-label mapping — are in section 6B, **not** section 6, which
  covers IBA Companion.
- **IBA Music web tools** — availability forms and band leader
  schedule tools used by band leaders and musicians.

If IBA Music launches a new product or service in the future, we will
either update this policy to cover it or publish a separate policy
and link to it from the [Legal Center](/).

## 2. Summary

> **Plain language, up front:** IBA Music does not sell your data.
> We do not use analytics or advertising trackers. We do not read
> your Google calendar — the scope we request only lets IBA Companion
> manage calendars it creates itself. We collect the information we
> need to run live-music performances (schedule, check-ins) and
> nothing more.

The rest of this policy explains each item in detail.

## 3. Information We Collect

### 3.1 Account information

When you sign in to IBA Companion or any IBA Music web tool, we
receive your name, email address, and (for some providers) a unique
identifier from the sign-in provider you choose: **Apple Sign-In**,
**Google Sign-In**, **Microsoft Sign-In**, or an IBA Music-hosted
email and password sign-in. On Android, the available providers are
**Google Sign-In** and **Microsoft Sign-In** (Apple Sign-In is
offered on Apple platforms only).

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
IBA Music booked you to perform, at the time of check-in. Check-in
is **manual** — you tap **Check In** on your upcoming performance,
IBA Companion requests your current location once, and compares it
against the venue's coordinates. There is no background or automatic
location tracking.

#### iOS location permission we request

IBA Companion declares one Core Location authorization on iOS:

| Permission | Key | Purpose string shown to you |
|---|---|---|
| While Using the App | `NSLocationWhenInUseUsageDescription` | *"IBA Companion checks your location when you tap Check In to confirm you've arrived at the venue. Location is never used in the background."* |

If you deny the prompt, the check-in feature is unavailable but
the rest of the app continues to function normally.

#### Android location permission we request

On Android, IBA Companion declares only **foreground** location
permissions — `ACCESS_FINE_LOCATION` and `ACCESS_COARSE_LOCATION`.
It does **not** declare `ACCESS_BACKGROUND_LOCATION`. When you tap
**Check In**, the app requests a **single, momentary** location fix
through Google Play Services' fused location provider, compares it
against the venue's coordinates, and then stops — there is no
continuous polling and no background location access of any kind.
Android shows its standard runtime location prompt; if you deny it,
check-in is unavailable but the rest of the app works normally.

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
- IBA Companion does **not** declare the `location` background
  mode and does **not** monitor geofences. On iOS,
  `CLLocationManager.allowsBackgroundLocationUpdates` is set to
  `false` at all times. On Android, the same guarantee is structural:
  with no `ACCESS_BACKGROUND_LOCATION` permission declared and no
  continuous location request, the operating system cannot deliver
  location to the app while it is in the background. The app cannot
  read your location while it is in the background on either platform.

#### Sharing

Location data associated with check-ins is stored in IBA Music's
own database on Cloudflare D1 and is used only as described in
section 4. We do **not** transfer location data to any advertising
network, data broker, analytics provider, or third party other
than the sub-processors listed in section 7. We do not sell it.

#### How to turn it off

On iPhone, go to **Settings → Privacy & Security → Location Services
→ IBA Companion**; on Android, go to **Settings → Apps → IBA
Companion → Permissions → Location**. You can change or revoke
permission at any time. Disabling location will prevent the check-in
feature from working but will not affect schedule viewing, calendar
sync, or any other part of the app.

### 3.4 Performance and schedule data

We receive your upcoming performance schedule from IBA Music's
internal booking system. This includes the venue, date, start and
end times, dress code, call time, band name, and any notes relevant
to the performance. This is the core data IBA Companion exists to
display to you.

### 3.5 Check-in and attendance records

When you check in at a venue, we record the timestamp, your
location at check-in, the performance you checked in to, and
whether the check-in was on time. IBA Music uses these records for
payroll reconciliation, attendance disputes, and operational
reporting.

### 3.6 Device and technical information

- **Push notification tokens.** If you grant notification permission,
  IBA Companion registers for remote notifications and hands us the
  device token your device reports — the **Apple Push Notification
  service (APNs)** token on iOS, or the **Firebase Cloud Messaging
  (FCM)** registration token on Android (see section 6A.3). We store
  that token so IBA Music's backend can deliver operational push
  notifications — schedule changes, check-in reminders, payroll
  updates. We do **not** send marketing or advertising push
  notifications.
- **Background delivery modes.** IBA Companion declares the iOS
  background modes listed below, each tied to a specific,
  user-visible feature. It does **not** declare `voip`,
  `external-accessory`, `bluetooth-central`, or any other background
  mode beyond those listed here.

    | Background mode | Feature | Purpose |
    |---|---|---|
    | `remote-notification` | Push notifications (§6.3) | Silent push payloads wake the app to refresh your schedule or update an active Live Activity in the background. |
    | `fetch` | Calendar sync v2 | Periodic `BGAppRefreshTask` with identifier `com.rolotrealanis.IBA-Companion.calendarsync.refresh` reconciles your opted-in calendar with your performance schedule while the app is in the background. |
    | `audio` | Practice (multitrack rehearsal, §3.9) | Allows Practice audio you started to continue playing when the screen is locked or the app is backgrounded — identical behavior to any music or podcast app. |

    IBA Companion does **not** use the `audio` background mode to
    record audio, capture microphone input, run speech recognition,
    or do anything other than continue user-initiated rehearsal
    playback. The microphone is never accessed —
    `NSMicrophoneUsageDescription` is not declared and
    `AVAudioSession` is configured for `.playback` (output only),
    never `.record` or `.playAndRecord`.
- **Crash and diagnostic logs.** This differs by platform:
    - *On iOS*, IBA Companion integrates **no** third-party
      crash-reporting SDK (no Firebase Crashlytics, Sentry, or
      Bugsnag). Platform-level crash reports are collected by Apple on
      IBA Music's behalf only when you opt in through Apple's "Share
      With App Developers" setting, delivered through the App Store
      Connect console, and used only to find and fix bugs.
    - *On Android*, IBA Companion uses **Firebase Crashlytics** (a
      Google service) to collect crash reports and basic diagnostic
      data — stack traces, device model, OS version, and the app state
      at the time of a crash — so we can find and fix defects. Before a
      crash report leaves the device, it passes through an on-device
      redaction step that strips personal identifiers (such as names,
      emails, and tokens) from log messages. Crashlytics data is
      processed by Google as a sub-processor (section 7), is used only
      for stability and debugging, and is never used for advertising or
      sold. The Android app does **not** use Firebase Analytics,
      Performance Monitoring, Remote Config, or App Check.

    IBA Music does not operate a custom diagnostic telemetry pipeline of
    its own on either platform, and does not knowingly include personal
    data in crash reports.

### 3.7 Calendar integration data

Calendar sync is **optional**. Your choices are:

- **Google Calendar** — see section 5 for the exact OAuth scope,
  calendar names created, and Google-specific Limited Use
  commitments.
- **Apple Calendar (EventKit)** — see section 6.1 for the EventKit
  permission we request and how we handle on-device calendar data.
- **Android device calendar (Calendar Provider)** — on Android,
  schedule sync writes to your device's native calendar through the
  Android Calendar Provider, which requires the `READ_CALENDAR` and
  `WRITE_CALENDAR` permissions. See section 6A.5. IBA Companion
  writes and maintains only the IBA Music calendar entries it creates
  and never reads or modifies your other calendar events.

You can use one, both, or neither. Choosing neither does not
disable any other feature of IBA Companion.

### 3.8 Biometric identifiers (NOT collected)

IBA Music does **not** collect, store, transmit, or process
biometric identifiers of any kind. Specifically, IBA Music does
not receive, record, or retain:

- Face geometry, facial scans, or FaceID template data
- Fingerprint templates, TouchID data, or any other friction-ridge
  data
- Voiceprints or voice characteristics
- Retina or iris scans
- Hand or palm geometry
- Gait or behavioral-biometric signatures

When you sign in to IBA Companion using Face ID or Touch ID via
your device's standard auto-fill or sign-in provider flow, the
biometric check happens **entirely on your device**, inside Apple's
Secure Enclave. The biometric data never leaves your device and is
never visible to IBA Music or our servers. We receive only the
OAuth assertion the device produces after it has locally verified
your biometric — an opaque cryptographic token that contains no
biometric information.

This policy addresses the Illinois Biometric Information Privacy
Act (BIPA), Texas Capture or Use of Biometric Identifier Act
(CUBI), and similar biometric-specific statutes: because IBA Music
does not collect biometric identifiers, the notice, consent,
retention, and destruction requirements of those statutes do not
apply to us. If that ever changes — for example, if a future
feature required biometric processing on our servers — we would
update this policy, obtain express written consent before
collecting any biometric data, and comply with all applicable
biometric-privacy laws.

### 3.9 Practice (multitrack rehearsal)

IBA Companion includes a **Practice** tab that lets you rehearse
the songs on your IBA Music setlist with separated instrument
stems (vocals, drums, bass, keys, guitar, etc.). All practice data
belongs either to IBA Music's backend or to your device — it is
not shared with any third party outside the sub-processors listed
in section 7.

#### What we collect for Practice

- **Song catalog metadata** — title, artist, key, tempo, section
  markers, cover art. This metadata is stored in IBA Music's own
  database on Cloudflare D1 and is delivered to your device via
  our Companion API when you open the Practice tab.
- **Audio stems** — individual instrument recordings that belong
  to IBA Music's internal multitrack library, stored in IBA
  Music's own Cloudflare R2 bucket. When you choose to practice a
  song, IBA Companion downloads those stems to your device for
  offline playback using a standard iOS background `URLSession`.
- **On-device usage signals** — your per-song mixer preset (mute,
  solo, volume per stem), the last position you played to, and a
  "recently practiced" list. These are stored on your device only
  and are not transmitted to IBA Music unless you are signed in
  and IBA Companion synchronizes preferences across your own
  devices in a future release.

#### On-device storage, limits, and deletion

- Downloaded stems are cached in IBA Companion's sandboxed
  Documents directory (`Documents/Songs/{songId}/`). They are
  **not** indexed by iOS Spotlight, **not** shared to the Files
  app unless you explicitly export, and **not** visible to other
  apps.
- IBA Companion enforces a **storage cap** (10 downloaded songs
  by default, configurable between 5 and 20) and a **time-to-live
  (TTL) auto-delete** (7 days by default, configurable between 3
  and 30). Stems you have not practiced in a while are
  automatically removed to keep device storage in check. You can
  review usage and delete downloads manually from
  **Settings → Practice → Storage**.
- Uninstalling IBA Companion removes every stem file.

#### Lock screen, CarPlay, and Bluetooth transport controls

When you are practicing, IBA Companion publishes **Now Playing**
metadata (song title, artist, cover art, playback position) via
`MPNowPlayingInfoCenter` so iOS can display it on your lock
screen and in Control Center. It also registers for the standard
**remote command center** (play, pause, next, previous, and
scrub) so the transport buttons on Bluetooth headphones, CarPlay,
and your lock screen control the Practice player. This is
identical to how any music or podcast app integrates with iOS.

IBA Companion does **not**:

- Access Apple Music, the Music app's library, or any audio file
  outside its own downloaded stems.
- Record audio or use the microphone —
  `NSMicrophoneUsageDescription` is not declared and
  `AVAudioSession` is configured for `.playback` (output only).
- Share what you are practicing with other musicians, bandleaders,
  or IBA Music staff. Practice playback happens locally and is
  not reported back to our servers.
- Apply any copy protection or DRM beyond the standard iOS
  sandbox — the stems are IBA Music's intellectual property (see
  [Terms of Service](/terms) §4.5) and your right to use them
  ends when your engagement with IBA Music ends, at which point
  your access to the Companion API is revoked and any local
  downloads become orphaned and age out via TTL.

### 3.10 Photos and camera (not collected)

IBA Companion does **not** declare `NSCameraUsageDescription` or
`NSPhotoLibraryUsageDescription`. It does not access the device
camera or photo library.

### 3.12 Maps and external apps (canOpenURL only)

IBA Companion declares three URL schemes in
`LSApplicationQueriesSchemes` so that it can render
"open in…" options if you have those apps installed:

| Scheme | App | Where it's offered |
|---|---|---|
| `comgooglemaps` | Google Maps | Venue address routing (alongside Apple Maps) |
| `waze` | Waze | Venue address routing |
| `weather` | Apple Weather | Venue weather glance |

Each check is an **on-device-only** existence query using Apple's
`canOpenURL` API — no information about your installed apps, your
device, your location, or your account is transmitted to IBA Music
or any third party. IBA Companion does not enumerate any other app
schemes and does not use these queries for analytics,
fingerprinting, or any purpose other than rendering the optional
"open in…" buttons.

## 4. How We Use Information

We use the information described in section 3 to:

- **Provide the service** — show you your performance schedule,
  route push notifications, accept check-ins, and (if you opt in)
  keep your calendar in sync.
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
IBA Companion app on iPhone.

**It does not apply to IBA Admin**, our separate iPhone app for office
staff and administrators. IBA Admin's iOS disclosures — including its
own App Store privacy-label mapping — are in section 6B.

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
- Payroll status updates
- **Stage Alerts** — time-sensitive on-stage messages sent by IBA
  Music staff during a performance. You can acknowledge or reply
  from the notification by choosing one of four predefined
  responses (OK, On my way, Need 5 min, Can't right now). Replies
  are posted only to IBA Music's Companion API — no free-text
  input is accepted and no third party sees them.
- Critical service announcements from IBA Music operations

We do **not** send advertising notifications, marketing offers,
third-party promotions, or behavioral re-engagement nudges. You
can disable notifications at any time in **Settings →
Notifications → IBA Companion**.

### 6.4 Live Activities (Set Tracker) and WeatherKit

IBA Companion declares `NSSupportsLiveActivities` so that during a
live performance it can optionally display a **Set Tracker** Live
Activity on your lock screen and in the Dynamic Island. The Live
Activity shows set-by-set timing — current set, remaining time,
countdown to the next break — drawn entirely from the performance
schedule IBA Music already holds on its servers. No new categories
of personal data are collected by the Live Activity: it is a
presentation-layer feature over schedule data already described
elsewhere in this policy.

The Live Activity may also show an optional **hourly
precipitation timeline** for the venue using **Apple WeatherKit**.
When the Live Activity has venue coordinates from the performance
schedule, IBA Companion asks WeatherKit for a short-range forecast
at those coordinates. WeatherKit is an Apple service: the forecast
query uses the venue's coordinates (not your device's location)
and is subject to Apple's own WeatherKit privacy terms. IBA Music
does not receive any additional personal data back from Apple in
this flow — only a forecast — and the forecast is rendered
locally on your device. IBA Companion does not query WeatherKit
for your current location and does not log or transmit the
forecast data elsewhere.

Live Activities are managed by iOS and follow Apple's timing
rules: they appear while the performance is active, update via
ActivityKit, and are dismissed automatically (or on your manual
swipe) when the performance ends. You can disable Live Activities
for IBA Companion at any time in **Settings → IBA Companion →
Live Activities** (or globally via **Settings → Face ID &
Passcode → Allow Access When Locked → Live Activities**).

### 6.5 App Tracking Transparency (ATT) and the IDFA

IBA Companion does **not** track you across apps and websites
owned by other companies, and does **not** show the App Tracking
Transparency prompt, because there is nothing to ask permission
for:

- IBA Companion does **not** read, request, or store the
  Identifier for Advertisers (IDFA / `advertisingIdentifier`).
- IBA Companion includes **no advertising SDKs** of any kind —
  no Google Ads Mobile SDK, no Meta Audience Network SDK, no
  AppLovin, no Unity Ads, no Chartboost, no IronSource, none.
- The **iOS** build of IBA Companion includes **no analytics SDKs** —
  no Firebase Analytics, no Amplitude, no Mixpanel, no Segment, no
  Hotjar, no Sentry, no Crashlytics, none. (The Android build uses
  Firebase Cloud Messaging for push and Firebase Crashlytics for crash
  reporting only — both operational, neither for advertising — as
  disclosed in section 6A; it likewise includes no analytics or
  advertising SDKs.)
- IBA Companion does **not** share any data with third parties
  for cross-app or cross-site advertising. It does not share data
  with data brokers.

Consistent with this, IBA Companion declares in its App Store
privacy report that it does **not** use data to track users and
does **not** perform any of Apple's defined tracking activities.

### 6.6 Account deletion

You can close your IBA Music account at any time.

**In-app option (recommended).** Open IBA Companion, go to
**Settings → Account → Delete Account**, and follow the prompts.
The flow discloses what happens to your data, asks you to
re-authenticate to prove you own the account, and closes your
account once you confirm. You do not need to email us or leave the
app to complete this. This satisfies Apple App Store Review
Guideline 5.1.1(v).

**Email option.** If you cannot reach the in-app control for any
reason — for example, you no longer have the app installed or
cannot sign in — email
[privacy@ibamusic.com](mailto:privacy@ibamusic.com) from the email
address on your account. We verify your identity and close your
account on the same terms.

**What happens when you close your account.** We immediately
deactivate your IBA Music account so you can no longer sign in to
IBA Companion or to the web tools through any sign-in provider
(Apple, Google, Microsoft, or email). You are signed out on every
device you were using. Push notifications to those devices stop.
In-app closures take effect immediately; email closures take effect
within 30 days of receipt.

**What we retain, and why.** Florida labor and tax recordkeeping
law requires IBA Music to retain records of the performances you
worked, the payroll artifacts tied to them, and the minimum
personal identifiers — your name, contact information, instruments,
and the performance history itself — needed to keep those records
meaningful to a tax auditor or labor regulator. IBA Music retains
this information for **seven (7) years** from the date of the
underlying record.

During the retention period IBA Music uses the retained information
**only** for tax, labor, audit, and legal-process purposes, and only
when specifically required by law or by a legitimate business
continuity need. The retained information is **not** made available
to any active feature of the Service — it is not used for scheduling,
messaging, push notifications, marketing, automated processing,
feature enrichment, model training, analytics, or any operational
function of IBA Companion after your account is closed. You are not
contacted about events, schedules, availability, or any other
operational matter after closure.

After the seven-year retention window elapses, IBA Music reviews the
retained information and removes it from the live system unless a
pending audit, legal hold, or ongoing dispute requires continued
retention.

**What happens to your calendars.** Closing your IBA Music account
does **not** automatically delete calendars IBA Companion previously
created in your Google Calendar or Apple Calendar. Those calendars
belong to you and remain in your account under your sole control.
See sections 5.5 and 6.1 for how to remove them if you wish.

**Your state-law privacy rights are unchanged.** Nothing in this
section limits any right you have under the California Consumer
Privacy Act or any other applicable privacy law to request access,
correction, deletion, or limitation of use with respect to specific
categories of personal information. See section 11 for details and
the contact path for exercising those rights. Requests are honored
subject to the retention carve-outs described above, which reflect
legal obligations IBA Music is required to meet.

### 6.7 App Store privacy labels — data mapping

Below is how the data described elsewhere in this policy maps to
Apple's App Store privacy-label categories **for IBA Companion**. This
exists so App Store reviewers can cross-check the policy against the
privacy nutrition label displayed on IBA Companion's App Store page.
The equivalent mapping for the Android app's Google Play **Data
Safety** form is in section 6A.8 — note that, unlike iOS, the Android
app does collect crash/diagnostic data via Firebase Crashlytics.

**Reviewing IBA Admin instead?** Use the table in section 6B.9. This
one is IBA Companion's and includes categories, such as Location and
Phone Number, that IBA Admin does not collect.

| Apple category | Items collected | Linked to user? | Used to track? | Purpose |
|---|---|---|---|---|
| **Contact Info** — Name, Email, Phone | Section 3.1, 3.2 | Yes | No | App Functionality |
| **Location** — Precise Location | Section 3.3 | Yes | No | App Functionality |
| **Identifiers** — User ID (from sign-in provider) | Section 3.1 | Yes | No | App Functionality |
| **Usage Data** | *Not collected* | — | — | — |
| **Diagnostics** | *Not collected by IBA Music.* Apple's platform-level crash reports remain available to us via App Store Connect only when you opt in via your device's "Share With App Developers" setting; see §3.6. | — | — | — |
| **User Content** | *Not collected* — see §3.9 (Practice audio is delivered to device, not collected) and §3.10 (camera / photos not used) | — | — | — |
| **Sensitive Info** | *Not collected* | — | — | — |
| **Financial Info** | *Not collected* | — | — | — |
| **Health & Fitness** | *Not collected* | — | — | — |
| **Contacts** | *Not collected* | — | — | — |
| **Browsing History** | *Not collected* | — | — | — |
| **Search History** | *Not collected* | — | — | — |

"Used to track?" is **No for every category** because IBA Companion
does not perform any of Apple's defined tracking activities (see
section 6.5).

Practice stem audio (§3.9) is delivered **to** your device from
IBA Music's own servers — it is not user-provided content and is
not "collected" in the App Store privacy-label sense. The
User Content row above is "Not collected" for exactly this
reason: Practice does not upload audio and does not link that
audio to your user identity, and the camera / photo library are
never accessed (§3.10).

### 6.8 Supported operating systems and upgrade path

IBA Companion supports the current major version of iOS plus the
immediately previous major version where practical. Security fixes
target the current version first. If your iPhone cannot run a
supported version, some features — notably calendar sync and
modern privacy prompts — may not be available. IBA Music does not
intentionally limit functionality on older devices as long as they
remain supported by Apple.

## 6A. Google Play / Android Platform Disclosures

This section covers the platform-specific disclosures that Google
Play and Android conventions expect for **IBA Companion for
Android**. It is the Android counterpart to the Apple disclosures in
section 6. Where a feature behaves identically to iOS, the rest of
this policy already applies; the items below describe the
Android-specific mechanisms.

### 6A.1 Distribution and sign-in

IBA Companion for Android is distributed through the **Google Play
Store**. Sign-in is offered through **Google Sign-In** (via Android
Credential Manager) and **Microsoft Sign-In**; Sign in with Apple is
not offered on Android. As on iOS, any biometric unlock used during
sign-in is performed entirely on-device by the Android operating
system — IBA Music never receives biometric data (see section 3.8).

### 6A.2 Location permission

IBA Companion for Android declares only foreground location
permissions — `ACCESS_FINE_LOCATION` and `ACCESS_COARSE_LOCATION` —
and does **not** declare `ACCESS_BACKGROUND_LOCATION`. Location is
read as a **single momentary fix** at the moment you tap **Check
In**, using Google Play Services' fused location provider, and is
used only to confirm you are at the venue (section 3.3). The app
performs no continuous tracking and cannot access location in the
background.

### 6A.3 Push notifications (Firebase Cloud Messaging)

Android push notifications are delivered through **Firebase Cloud
Messaging (FCM)**, a Google service. With your permission (the
Android 13+ `POST_NOTIFICATIONS` runtime prompt) the app registers
with FCM and sends the resulting device registration token to IBA
Music's backend so we can deliver the same operational notifications
described in section 6.3 — schedule changes, check-in reminders,
payroll updates, stage alerts, and critical service announcements. We
send no advertising or marketing notifications. FCM is operated by
Google as a sub-processor (section 7).

### 6A.4 Crash and diagnostic reporting (Firebase Crashlytics)

The Android app uses **Firebase Crashlytics** to collect crash
reports and basic diagnostics (stack traces, device model, OS
version, app state at the time of a crash) so we can fix defects.
Crash payloads pass through an on-device redaction step that removes
personal identifiers before transmission. This data is processed by
Google as a sub-processor (section 7), is used only for stability and
debugging, and is never used for advertising or sold. The Android app
does **not** include Firebase Analytics, Performance Monitoring,
Remote Config, App Check, or any other analytics SDK.

### 6A.5 Calendar integration (Android Calendar Provider)

Optional schedule sync on Android writes to your device's native
calendar through the **Android Calendar Provider**, which requires
the `READ_CALENDAR` and `WRITE_CALENDAR` permissions. IBA Companion
creates and maintains only the IBA Music calendar entries it writes —
identified by a stable IBA Music event identifier — and reads back
only those entries so it can update or remove them when your schedule
changes. It does not read, modify, or transmit any other event in
your calendar. This is an on-device integration; if your device
calendar is itself backed by a Google or Microsoft account, those
entries sync through that account under that provider's terms. You can
revoke calendar access at any time in **Settings → Apps → IBA
Companion → Permissions → Calendar**.

### 6A.6 No advertising, no tracking, no ad identifier

IBA Companion for Android contains **no advertising SDKs** and **no
analytics SDKs**, does not request the Android Advertising ID (AAID),
and does not track you across other apps or websites. The only
third-party data flows are the operational sub-processors listed in
section 7.

### 6A.7 Account deletion

The Android app provides in-app account deletion at **Settings →
Delete Account**, with re-authentication, on the same terms described
in section 6.6 and on the public
[Account deletion](/account-deletion/) page. This satisfies Google
Play's in-app data-deletion requirement.

### 6A.8 Google Play Data Safety — data mapping

This table maps the data described elsewhere in this policy to
Google Play's Data Safety categories, so Play reviewers can
cross-check it against the Data Safety form on IBA Companion's Play
listing. No data type is used for tracking, and none is shared for
advertising. Data processed by Google as a service provider (FCM,
Crashlytics) is "collected" but not "shared" in the Data Safety
sense.

| Play Data Safety type | Collected | Shared | Purpose |
|---|---|---|---|
| **Personal info** — Name, Email address, Phone number | Yes (§3.1, §3.2) | No | App functionality; Account management |
| **Location** — Approximate & precise location | Yes (§3.3) — momentary, at check-in only | No | App functionality |
| **App info & performance** — Crash logs, Diagnostics | Yes (§6A.4) | No | App functionality — stability & debugging (processed by Google / Firebase Crashlytics; PII redacted) |
| **Device or other IDs** — FCM registration token | Yes (§6A.3) | No | App functionality — push delivery (processed by Google / Firebase Cloud Messaging) |
| **App activity / Financial info / Health & fitness / Photos & videos / Audio / Contacts / Messages / Web browsing** | Not collected | — | — |

The Practice feature downloads IBA Music's own audio stems **to** your
device; it does not collect or upload audio from you. The Android app
does not access the camera or photo library.

## 6B. IBA Admin (iOS) Platform Disclosures

This section covers the **IBA Admin** iPhone app described in section
1.2. It is a separate app from IBA Companion with a different audience,
a different sign-in method, and a materially smaller data footprint.
Sections 6 and 6A describe IBA Companion and do **not** apply to
IBA Admin.

IBA Admin is distributed only to IBA Music office staff and authorized
administrators. It is not usable without an IBA Music administrator
account.

### 6B.1 Sign-in and account information

Sign-in is through **Microsoft Entra ID**, restricted to the
ibamusic.com tenant. The app rejects any address that is not
`@ibamusic.com`. On successful sign-in IBA Music receives the
administrator's **name**, **email address**, and **user ID**, together
with the role and page grants that determine which tools that account
can see.

This is the entire set of personal information IBA Admin collects. It
is used solely to authenticate the administrator and to decide what
they are permitted to view — never for analytics, personalization, or
advertising.

After the first sign-in the app can create a **passkey** (WebAuthn) for
subsequent sign-ins. The passkey is bound to that specific device and
its private key is generated and held in the device's Secure Enclave.
It never leaves the device and IBA Music never receives it. Because
passkeys are device-bound, the button for one appears only on a device
where a passkey has already been enrolled.

### 6B.2 Face ID

IBA Admin declares `NSFaceIDUsageDescription` and uses Face ID (or the
device passcode as a fallback) to re-protect the admin session. Apple's
biometric system performs the match entirely on-device and returns only
a success or failure result. **IBA Music never receives, stores, or
transmits any biometric data**, and no biometric identifier is
collected. This mirrors section 3.8.

### 6B.3 Location — not collected

**IBA Admin does not collect location of any kind.** It declares no
`NSLocationWhenInUseUsageDescription`, no
`NSLocationAlwaysAndWhenInUseUsageDescription`, and it never requests
location authorization or displays the device's own position.

The app does draw maps — a map of the day's event locations, and a
venue geofence editor. Both plot **venue** coordinates supplied by
IBA Music's own servers. Those are business records about a place, not
information about the person using the app.

This is a deliberate difference from IBA Companion, which does collect
a momentary GPS reading at check-in (section 3.3). **That disclosure
does not apply to IBA Admin.**

### 6B.4 Apple Calendar integration (EventKit)

IBA Admin declares `NSCalendarsFullAccessUsageDescription` and can
export the administrator's schedule into their **Apple Calendar**. The
integration is **outbound and on-device**: events flow from IBA Music
into the local calendar, and nothing from the calendar is ever
transmitted to IBA Music's servers or to any third party.

The app **does read from the local calendar store**, and we want to be
precise about why: when a sync runs it looks up the entries it created
previously so it can update the ones that changed and remove the ones
that no longer apply, instead of creating duplicates every time. Those
reads happen entirely on the device, are limited to reconciling
IBA Admin's own entries, and their results are never uploaded, logged
off-device, or shared.

Calendar access is optional. Declining it disables schedule export and
affects nothing else in the app. It can be revoked at any time in
iOS Settings → Privacy & Security → Calendars.

### 6B.5 Background refresh

IBA Admin registers one background task identifier,
`com.ibamusic.admin.calendar-sync`, and declares the `fetch` and
`remote-notification` background modes. These let a scheduled calendar
export and incoming notifications be processed while the app is not in
the foreground. No location is gathered in the background, and no
additional personal data is collected by these tasks.

### 6B.6 Push notifications (APNs)

IBA Admin uses **Apple Push Notification service** to deliver schedule
and change-request alerts. Apple issues a device token that IBA Music
stores in order to address notifications to that device. The token
identifies a device installation, not a person, and is not used for
advertising or tracking. Notifications are optional and can be turned
off in iOS Settings → Notifications.

### 6B.7 Apple Wallet passes

IBA Admin can add passes — including venue parking passes — to
**Apple Wallet** using Apple's PassKit framework. Passes are issued by
IBA Music and added to the local Wallet at the administrator's request.
The app reads no payment card, no payment instrument, and no
transaction history from Wallet, and it processes no payments.

### 6B.8 No tracking, no third-party SDKs, no advertising

IBA Admin performs none of Apple's defined tracking activities. It does
not use the advertising identifier and presents no App Tracking
Transparency prompt because it has nothing to ask for.

The app contains **no third-party SDKs at all** — no analytics, no
crash reporter, no advertising library. Its only dependencies are
first-party Apple frameworks. Note that this differs from the Android
edition of IBA Companion, which does use Firebase Crashlytics
(section 6A.4); **no equivalent exists in IBA Admin**.

The app also does not access the camera or the photo library, and
declares no camera permission.

### 6B.9 App Store privacy labels — data mapping for IBA Admin

This is the mapping for **IBA Admin**. The table in section 6.7 is for
IBA Companion and lists categories — notably Location and Phone — that
IBA Admin does **not** collect. App Store reviewers cross-checking
IBA Admin's privacy label should use this table.

| Apple category | Items collected | Linked to user? | Used to track? | Purpose |
|---|---|---|---|---|
| **Contact Info** — Name | Section 6B.1 | Yes | No | App Functionality |
| **Contact Info** — Email Address | Section 6B.1 | Yes | No | App Functionality |
| **Identifiers** — User ID | Section 6B.1 | Yes | No | App Functionality |
| **Contact Info** — Phone Number | *Not collected* | — | — | — |
| **Location** — Precise or Coarse | *Not collected* — see §6B.3 | — | — | — |
| **Financial Info** | *Not collected* — see §6B.10 | — | — | — |
| **Contacts** | *Not collected* — calendar export (§6B.4) is not contacts access | — | — | — |
| **Usage Data** | *Not collected* — no analytics SDK | — | — | — |
| **Diagnostics** | *Not collected* — no crash reporter | — | — | — |
| **User Content** | *Not collected* | — | — | — |
| **Sensitive Info** | *Not collected* | — | — | — |
| **Health & Fitness** | *Not collected* | — | — | — |
| **Browsing History** | *Not collected* | — | — | — |
| **Search History** | *Not collected* | — | — | — |
| **Purchases** | *Not collected* | — | — | — |
| **Photos or Videos / Audio Data** | *Not collected* — no camera or photo access | — | — | — |

"Used to track?" is **No for every category**, for the reasons in
section 6B.8.

### 6B.10 Financial information — not collected

IBA Admin displays monetary figures in one place: the late-arrival
**penalty tier** configuration, where an administrator sets the
company's own policy thresholds — for example, a flat deduction that
applies past a certain lateness.

These are company policy settings, and where a figure relates to a
person, that person is a contracted performer whose schedule the
administrator manages — not the user of the app. Apple's "Financial
Info" category covers the **app user's own** payment information,
credit information, or other financial information, and IBA Admin
collects none of that. It handles no payment instrument, no card or
bank details, and no credit information, and it processes no
transactions.

### 6B.11 Data retention and your rights

Retention (section 8), your rights (section 9), GDPR (section 10), and
CCPA/CPRA (section 11) apply to IBA Admin exactly as written. Because
IBA Admin accounts are issued by IBA Music to its own staff and
contractors, account creation and removal are handled through IBA Music
internal administration; requests can also be made to
[privacy@ibamusic.com](mailto:privacy@ibamusic.com).

## 7. Information We Share

We share information only with the sub-processors we need in order
to operate the service. We never sell personal information, share it
for cross-context behavioral advertising, or permit any third party
to use your information for its own marketing purposes. A
stand-alone, always-current list of sub-processors is published at
[legal.ibamusic.com/subprocessors](/subprocessors/) — the table
below is a summary.

| Sub-processor | Purpose |
|---|---|
| **Apple Inc.** | Apple Push Notification service (APNs), Apple Sign-In, EventKit for optional Apple Calendar sync, ActivityKit for the Set Tracker Live Activity (§6.4), and Apple WeatherKit for the optional venue precipitation forecast shown inside the Live Activity (queries use venue coordinates, not your device location). |
| **Google LLC** | Google Calendar API via the `calendar.app.created` scope (opt-in calendar sync on iOS); Google Sign-In for authentication; and, on Android, **Firebase Cloud Messaging** (operational push-notification delivery) and **Firebase Crashlytics** (crash and diagnostic reporting, with on-device PII redaction). |
| **Microsoft Corporation** | Microsoft Sign-In (Azure Active Directory) — IBA Companion offers Microsoft 365 sign-in to musicians whose IBA Music account is linked to a Microsoft identity, alongside Apple Sign-In and Google Sign-In. Microsoft Graph is also used on the IBA Music admin side to sync performance bookings with IBA Music staff Outlook calendars; that admin use is not part of the IBA Companion app. |
| **Cloudflare, Inc.** | Edge hosting for admin.ibamusic.com and related tools, database storage (Cloudflare D1 — performance schedule, check-ins, song metadata), object storage (Cloudflare R2 — IBA Music's multitrack audio stems used by the Practice feature, §3.9), and Cloudflare Pages hosting for this legal subdomain itself. Cloudflare processes data on IBA Music's behalf; its own use of the data is governed by its contractual role as a processor. |

We also disclose information when we reasonably believe disclosure
is necessary to comply with a lawful subpoena, court order, or
similar legal process; to investigate fraud, security incidents, or
violations of our [Terms of Service](/terms); or to protect the
rights, property, or safety of IBA Music, our musicians, or the
public. We will contest overbroad legal demands where we believe
doing so is proper and practical.

<a name="data-retention"></a>

## 8. Data Retention

| Category | Retention |
|---|---|
| Account profile | Until you close your account, plus up to 30 days to complete deletion. |
| Performance and attendance records | Seven (7) years, consistent with Florida tax and labor-records requirements. |
| Location records (check-ins) | Seven (7) years alongside the associated attendance record. We do not maintain location history outside of check-in transactions. |
| Push notification tokens | Until the token is invalidated by your device or you sign out. |
| Crash and diagnostic logs (platform-level, via Apple/Google) | Controlled by Apple/Google. We do not retain copies on our own infrastructure. |
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

For step-by-step instructions on deleting your IBA Companion
account from inside the iOS or Android app, see the dedicated
[Account deletion](/account-deletion/) page.

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
  employment-related information (performances, check-ins),
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
- OAuth tokens on the device are stored in the **iOS Keychain**,
  protected by the operating system's hardware-backed security.
- Authentication uses OAuth 2.0 (Apple, Google, Microsoft) for
  third-party sign-in. IBA Music-hosted email-and-password sign-in
  uses an industry-standard salted, slow-hash password store (we do
  not store plaintext passwords). The IBA Music admin dashboard
  additionally supports **WebAuthn passkeys** for staff sign-in.
- Access to the IBA Music admin dashboard requires sign-in and is
  limited to authorized IBA Music personnel.

No security measure is perfect, and we cannot guarantee the
security of information transmitted over the internet. If you
believe your account has been compromised or you have identified a
vulnerability in our services, please email
[privacy@ibamusic.com](mailto:privacy@ibamusic.com) — see the
[Security](/security) page for our responsible disclosure policy.

**Breach notification.** If we determine that a security incident
has resulted in unauthorized access to your personal data, we will
notify you **without undue delay** and, where required by law,
within the timeframes set by applicable breach-notification
statutes — including 72 hours of becoming aware of a personal data
breach for notifications to supervisory authorities under Article
33 of the EU GDPR and the equivalent UK GDPR provision, and the
timeframes required by Florida Statute §501.171 (Florida
Information Protection Act of 2014) for affected Florida residents.
Our notice will describe the nature of the breach, the categories
of data affected, the steps we are taking in response, and the
steps you can take to protect yourself.

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
