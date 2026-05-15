---
layout: layouts/base.njk
title: Account deletion
description: How to delete your IBA Companion account, what data is removed, and what we retain for tax and labor-records compliance.
permalink: /account-deletion/
---

This page describes how to delete your **IBA Companion** account on
iOS or Android, what information is removed when you do so, and the
records IBA Music must retain for tax, payroll, and labor-law
purposes. It exists so that the deletion path is discoverable
without first installing the app, as required by Google Play and
the Apple App Store.

If you have only used IBA Companion to view your schedule and have
not yet been booked on any event, you can delete your account
entirely in the app. If you have ever been paid by IBA Music — even
once — some records must be retained by law; see *What we retain*
below.

## In-app deletion (recommended)

The fastest path is from inside the app. The in-app flow asks you
to re-authenticate with the same provider you sign in with, then
calls our deletion endpoint and wipes the app's on-device data.

**iOS:**

1. Open **IBA Companion**.
2. Tap the **Settings** tab.
3. Scroll to the bottom of the screen and tap **Delete Account**.
4. Read the disclosure and tap **Continue**.
5. Re-authenticate with Apple, Google, Microsoft, or your email
   password (whichever you originally used).
6. Confirm the final prompt. The app signs you out, wipes its
   on-device data, and shows a success screen.

**Android:**

1. Open **IBA Companion**.
2. Tap the **Settings** tab.
3. Scroll to **Delete Account** and tap it.
4. Read the disclosure and tap **Continue**.
5. Re-authenticate with Google or Microsoft (whichever you
   originally used).
6. Confirm the final prompt. The app signs you out and wipes its
   on-device data.

Both platforms send the same request to our server, and the result
is identical regardless of which device you use.

## Alternative — email request

If you cannot access the app (for example, you no longer have the
device, or you signed in with a Microsoft account you can no longer
access), you can request deletion by email.

Send a message to
**[privacy@ibamusic.com](mailto:privacy@ibamusic.com)** from the
email address on file with your account, with the subject line
"**Account deletion request**". Include:

- The full name on your account.
- The email address used to sign in.
- Any band(s) you have worked with, if you remember them — this
  helps us verify your identity.

We will reply within five (5) business days to confirm the request
and within thirty (30) days to confirm that deletion has been
completed.

## What happens when you delete

Account deletion in IBA Companion is implemented as a
**deactivation**. Concretely:

- Your account is marked inactive on our servers immediately. You
  can no longer sign in to the iOS or Android apps, the admin
  dashboard, or any other IBA Music product with the credentials
  attached to that account.
- An audit row is written recording the deletion event (timestamp,
  account identifier, requesting platform). This row contains no
  personal information beyond the account identifier.
- The on-device app data — cached schedule, downloaded practice
  stems, secure tokens, push-notification registration, and local
  preferences — is wiped from the device that initiated the
  deletion.
- Push-notification tokens for your account are invalidated. You
  will not receive any further notifications from IBA Music after
  the deletion completes.
- The Microsoft / Google Calendar integration is unlinked from your
  account. Events previously written to your calendar remain in
  your calendar (we never delete events from your personal calendar
  on your behalf — you may delete them manually from Google
  Calendar or Outlook if you wish).

## What we retain and why

IBA Music is a Florida limited liability company that contracts
professional musicians. United States federal and Florida state
law require us to retain certain records about people we have
paid, even after they have stopped working with us:

| Category | Retention period | Reason |
|---|---|---|
| Performance and attendance records | 7 years | Florida tax and labor records retention. |
| Invoices, 1099s, and payment records | 7 years | IRS and state tax compliance. |
| Location check-in records associated with paid attendance | 7 years (alongside the attendance record) | Cannot be unlinked without invalidating the attendance record. |
| Profile information necessary to identify those records (name, payee email, phone, instrument) | 7 years | Required so that the retained records remain meaningful and auditable. |
| Push-notification token | Removed immediately on deletion | Not legally required to retain. |
| Crash and diagnostic logs (Apple / Google platform-level) | Controlled by Apple / Google | We do not retain copies on our own infrastructure. |
| Google Calendar / Microsoft Calendar event content | None retained | We never stored a mirror; events live in your own calendar account. |

The retention periods above are the same as those listed in our
[Privacy Policy §8](/privacy/#data-retention).

## Can I re-activate?

No. Deletion is final. If at a later date you wish to work with
IBA Music again, you will need to submit a fresh musician
application at the appropriate IBA Music recruiting channel; a new
account will be created at that point and is treated as a separate
account from the deleted one.

## Questions

For any question about the deletion process, or to escalate a
request that has not been resolved within the timeframes above,
contact **[privacy@ibamusic.com](mailto:privacy@ibamusic.com)**.
