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
    "IBA Companion (iOS, iPadOS, macOS, watchOS)",
    "IBA Companion for Android",
    "IBA Music Admin Dashboard (admin.ibamusic.com)",
    "IBA Music web tools (availability, invoice portal, band leader)",
  ],

  // Google OAuth scope disclosed on the Privacy Policy
  googleScope: "https://www.googleapis.com/auth/calendar.app.created",

  // Copyright year — computed once per build
  currentYear: new Date().getFullYear(),
};
