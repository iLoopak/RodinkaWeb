"""Validate generated GTM, consent, localization and CTA analytics markup."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

from validate_seo import FAMILIES


ROOT = Path(__file__).resolve().parents[1]
# One page per language per family, taken from the SEO validator so adding a
# topic family cannot silently shrink what this check covers.
EXPECTED_PAGES = sum(len(variants) for variants in FAMILIES.values())
GTM_ID = "GTM-5FM9NJHK"
GA4_ID = "G-LMZQ91Y9NP"
APP_ORIGIN = "https://app.mojerodinka.cz"
ALLOWED_LOCATIONS = {"header", "hero", "video", "content", "footer"}
EXPECTED_COPY = {
    "cs": ("Povolit analytiku", "Odmítnout", "Nastavení cookies"),
    "sk": ("Povoliť analytiku", "Odmietnuť", "Nastavenie cookies"),
    "en": ("Allow analytics", "Reject", "Cookie settings"),
}


class AnalyticsParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.language = ""
        self.app_links: list[dict[str, str]] = []
        self.has_consent_panel = False
        self.has_cookie_settings = False

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        attrs = {key: value or "" for key, value in attrs_list}
        if tag == "html":
            self.language = attrs.get("lang", "")
        elif tag == "section" and "data-cookie-consent" in attrs:
            self.has_consent_panel = True
        elif tag == "button" and "data-cookie-settings" in attrs:
            self.has_cookie_settings = True
        elif tag == "a" and attrs.get("href"):
            destination = urlparse(attrs["href"])
            if f"{destination.scheme}://{destination.netloc}" == APP_ORIGIN:
                self.app_links.append(attrs)


def main() -> int:
    html_files = sorted(ROOT.rglob("*.html"))
    errors: list[str] = []

    if len(html_files) != EXPECTED_PAGES:
        errors.append(f"Expected {EXPECTED_PAGES} generated HTML pages, found {len(html_files)}")

    for path in html_files:
        relative = path.relative_to(ROOT)
        source = path.read_text(encoding="utf-8")
        parser = AnalyticsParser()
        parser.feed(source)

        consent_default = source.find('window.gtag("consent", "default"')
        gtm_bootstrap = source.find("googletagmanager.com/gtm.js")
        if consent_default < 0 or gtm_bootstrap < 0 or consent_default > gtm_bootstrap:
            errors.append(f"{relative}: Consent Mode default is not before GTM")
        if source.count("googletagmanager.com/gtm.js") != 1:
            errors.append(f"{relative}: expected one GTM bootstrap")
        if source.count("googletagmanager.com/ns.html") != 1:
            errors.append(f"{relative}: expected one GTM noscript fallback")
        if not re.search(r"<body>\s*<!-- Google Tag Manager \(noscript\) -->", source):
            errors.append(f"{relative}: GTM noscript is not immediately after <body>")
        if GA4_ID in source or "googletagmanager.com/gtag/js" in source:
            errors.append(f"{relative}: contains a forbidden direct GA4 integration")
        if not parser.has_consent_panel or not parser.has_cookie_settings:
            errors.append(f"{relative}: consent panel or footer settings action is missing")

        expected_copy = EXPECTED_COPY.get(parser.language)
        if expected_copy is None or any(item not in source for item in expected_copy):
            errors.append(f"{relative}: consent localization does not match {parser.language!r}")

        if not parser.app_links:
            errors.append(f"{relative}: no application CTA links found")
        for attrs in parser.app_links:
            location = attrs.get("data-analytics-location", "")
            if location not in ALLOWED_LOCATIONS:
                errors.append(f"{relative}: app CTA has invalid analytics location {location!r}")

    script = (ROOT / "script.js").read_text(encoding="utf-8")
    for token in (
        "cta_app_click",
        "cta_location",
        "cta_text",
        "page_path",
        "page_language",
        "rodinka_analytics_consent",
        "analytics_storage",
    ):
        if token not in script:
            errors.append(f"script.js: missing {token}")
    if GA4_ID in script or "googletagmanager.com/gtag/js" in script:
        errors.append("script.js: contains a forbidden direct GA4 integration")

    if errors:
        print("Analytics validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Analytics validation passed for {len(html_files)} pages: one GTM integration per page, "
        "consent before GTM, localized controls and marked application CTAs."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
