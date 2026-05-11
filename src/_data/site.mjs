// Site-wide data — single source of truth for entity, URLs, and contact info.
// All templates read this via Eleventy's data cascade as `site.*`.

export default {
  // Organization / data controller
  entity: {
    legalName: "Island Breeze Affiliates Inc.",
    dba: "IBA Music",
    fullName: "Island Breeze Affiliates Inc. d/b/a IBA Music",
    jurisdiction: "Florida, USA",
    // Physical mailing address intentionally omitted until confirmed
    // with the operator. CCPA allows contact via email alone for
    // data-subject requests, and we prefer not to publish a home
    // address publicly. See plan phase 05 for follow-up.
  },

  // Contact
  contact: {
    privacyEmail: "privacy@ibamusic.com",
    supportEmail: "support@ibamusic.com",
  },

  // Canonical URLs
  url: "https://legal.ibamusic.com",
  urls: {
    home: "https://legal.ibamusic.com/",
    privacy: "https://legal.ibamusic.com/privacy",
    terms: "https://legal.ibamusic.com/terms",
    cookies: "https://legal.ibamusic.com/cookies",
    security: "https://legal.ibamusic.com/security",
    contact: "https://legal.ibamusic.com/contact",
  },

  // Products covered by these legal documents
  productsCovered: [
    "IBA Companion for iOS (iPhone)",
    "IBA Companion for Android",
    "IBA Music Admin Dashboard (admin.ibamusic.com)",
    "IBA Music web tools (availability, band leader)",
  ],

  // Google OAuth scope disclosed on the Privacy Policy
  googleScope: "https://www.googleapis.com/auth/calendar.app.created",

  // Effective date for the current published version of these
  // documents. Bump when material changes are made. App version is
  // the IBA Companion iOS build these documents apply to.
  effectiveDate: "2026-04-30",
  appVersion: "1.2",

  // Copyright year — computed once per build
  currentYear: new Date().getFullYear(),
};
