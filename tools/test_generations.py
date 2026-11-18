"""Tests for the family-across-generations content (homepage section and the
circle page): every language carries it, it keeps the store-first CTA, and the
copy never leaks internal wave names or outdated availability claims.

Run with: python -m unittest discover -s tools -p "test_*.py"
"""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import generate_site as site  # noqa: E402

LOCALES = ("cs", "sk", "en", "de", "pl")


def page(path: str) -> str:
    return (ROOT / path.lstrip("/") / "index.html").read_text(encoding="utf-8")


def visible_text(html: str) -> str:
    html = re.sub(r"<(script|style)\b.*?</\1>", " ", html, flags=re.S)
    return re.sub(r"<[^>]+>", " ", html)


def shape(value):
    if isinstance(value, dict):
        return {key: shape(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return tuple(shape(item) for item in value)
    return type(value).__name__


class GenerationsCopyTest(unittest.TestCase):
    def test_every_language_has_the_same_structures(self):
        for name in ("HOME_CIRCLE", "ESCORT_MOCK", "INVITE_MOCK"):
            data = getattr(site, name)
            for locale in LOCALES:
                self.assertEqual(shape(data[locale]), shape(data["cs"]), f"{name}[{locale}]")
        for locale in LOCALES:
            self.assertEqual(shape(site.TOPICS[locale]["circle"]), shape(site.TOPICS["cs"]["circle"]), locale)

    def test_homepage_section_offers_two_to_four_scenarios(self):
        for locale in LOCALES:
            self.assertTrue(2 <= len(site.HOME_CIRCLE[locale]["cards"]) <= 4, locale)


class GeneratedPagesTest(unittest.TestCase):
    def test_circle_page_explains_both_ways_to_help(self):
        for locale in LOCALES:
            html = page(site.PATHS["circle"][locale])
            self.assertIn('class="app-mock escort-mock"', html, locale)
            self.assertIn('class="app-mock invite-mock"', html, locale)
            self.assertEqual(html.count("<h1"), 1, locale)
            # The mocks are drawings; the same facts must be in visible text.
            self.assertEqual(html.count('aria-hidden="true"><p class="escort-screen">'), 1, locale)

    def test_store_first_cta_on_new_content(self):
        for locale in LOCALES:
            for path in (site.PATHS["circle"][locale], site.PATHS["home"][locale]):
                html = page(path)
                self.assertIn(site.STORE_URLS["ios"], html, path)
                self.assertIn(site.STORE_URLS["android"], html, path)
                self.assertIn('class="web-app-link"', html, path)

    def test_homepage_section_links_to_the_circle_page(self):
        for locale in LOCALES:
            html = page(site.PATHS["home"][locale])
            section = html[html.index('id="sirsi-rodina"'):]
            section = section[:section.index("</section>")]
            self.assertIn('class="app-mock escort-mock"', section, locale)
            self.assertIn(f'href="{site.PATHS["circle"][locale]}"', section, locale)

    def test_no_internal_wave_names_in_marketing_text(self):
        pattern = re.compile(r"\bG[0-9](?:\.[0-9])?[ab]?\b")
        for path in ROOT.rglob("index.html"):
            text = visible_text(path.read_text(encoding="utf-8"))
            self.assertIsNone(pattern.search(text), f"{path}: {pattern.search(text)}")

    def test_no_outdated_browser_only_availability(self):
        outdated = (
            "Otevře se Rodinka v prohlížeči", "Otvorí sa Rodinka v prehliadači", "Rodinka opens in your browser",
            "Rodinka öffnet sich im Browser", "Rodinka otworzy się w przeglądarce", "není nutná instalace",
            "inštalácia nie je potrebná", "installation is optional", "Installation ist optional",
            "instalacja jest opcjonalna", "Nothing to install", "nothing to install", "na plochu ji přidáte jako aplikaci",
        )
        for path in ROOT.rglob("index.html"):
            text = path.read_text(encoding="utf-8")
            for phrase in outdated:
                self.assertNotIn(phrase, text, f"{path}: {phrase!r}")


if __name__ == "__main__":
    unittest.main()
