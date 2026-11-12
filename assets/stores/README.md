# Official store badges

Downloaded 2026-11-12, without modifying artwork. Locales: cs, sk, en, de, pl.

Apple SVG source: `https://toolbox.marketingtools.apple.com/api/v2/badges/download-on-the-app-store/black/{locale}-{country}?releaseDate=1464739200`
Locale/country pairs: cs-cz, sk-sk, en-us, de-de, pl-pl.
Guidelines: https://developer.apple.com/app-store/marketing/guidelines/

Google PNG source: `https://play.google.com/intl/en_us/badges/static/images/badges/{locale}_badge_web_generic.png`
Guidelines: https://partnermarketinghub.withgoogle.com/brands/google-play/google-play/lockups-icons-badges/

Preserve intrinsic proportions and the Google artwork's built-in clear space. Apple is first; both black badges have comparable visible heights. Store destinations are centralized in `generate_site.py: STORE_URLS`; the verified Czech Apple URL is retained for every locale rather than guessing country storefronts.
