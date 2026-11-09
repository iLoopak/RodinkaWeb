"""Tests for the comparison section: data rules and generated pages.

Run with: python -m unittest discover -s tools -p "test_*.py"
"""

from __future__ import annotations

import re
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import comparisons as cmp  # noqa: E402
import generate_site as site  # noqa: E402

LOCALES = ("cs", "sk", "en")
OFFICIAL_HOSTS = {
    "familia": {"familiaplanner.com"},
    "familywall": {"www.familywall.com", "support.familywall.com"},
    "cozi": {"www.cozi.com"},
}


def all_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from all_strings(item)
    elif isinstance(value, (tuple, list)):
        for item in value:
            yield from all_strings(item)


def shape(value):
    """Structure of a copy tree without its text, to compare locales."""
    if isinstance(value, dict):
        return {key: shape(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [shape(item) for item in value]
    return type(value).__name__


class TableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.rows = 0
        self.in_tbody = False
        self.h1 = 0

    def handle_starttag(self, tag, attrs):
        if tag == "tbody":
            self.in_tbody = True
        if tag == "tr" and self.in_tbody:
            self.rows += 1
        if tag == "h1":
            self.h1 += 1

    def handle_endtag(self, tag):
        if tag == "tbody":
            self.in_tbody = False


class ComparisonDataTest(unittest.TestCase):
    def test_every_row_uses_known_areas_statuses_and_rodinka_facts(self):
        for key, competitor in cmp.COMPETITORS.items():
            areas = [row[0] for row in competitor["rows"]]
            self.assertEqual(len(areas), len(set(areas)), f"{key}: duplicate areas")
            for area, status, note, sources in competitor["rows"]:
                self.assertIn(area, cmp.AREAS)
                self.assertIn(area, cmp.RODINKA, f"{area}: Rodinka side missing")
                self.assertIn(status, cmp.STATUSES)
                self.assertEqual(set(note), set(LOCALES))
                self.assertTrue(sources, f"{key}/{area}: every competitor claim needs a source")
                for source in sources:
                    self.assertIn(source, competitor["sources"], f"{key}/{area}: unknown source {source}")
        for area, (status, note) in cmp.RODINKA.items():
            self.assertIn(status, cmp.STATUSES)
            self.assertEqual(set(note), set(LOCALES))

    def test_sources_are_official_https_pages(self):
        for key, competitor in cmp.COMPETITORS.items():
            for url, _label in competitor["sources"].values():
                parsed = urlparse(url)
                self.assertEqual(parsed.scheme, "https", url)
                self.assertIn(parsed.hostname, OFFICIAL_HOSTS[key], url)

    def test_verification_date_is_iso(self):
        self.assertRegex(cmp.VERIFIED_ON, r"^\d{4}-\d{2}-\d{2}$")
        self.assertEqual(set(cmp.VERIFIED_LABEL), set(LOCALES))

    def test_no_means_the_competitor_said_so(self):
        # "No" is only for an explicit statement on the competitor's own site.
        prefixes = {"cs": "Podle ", "sk": "Podľa ", "en": "According to "}
        for key, competitor in cmp.COMPETITORS.items():
            for area, status, note, _ in competitor["rows"]:
                if status == "no":
                    for locale in LOCALES:
                        self.assertTrue(note[locale].startswith(prefixes[locale]), f"{key}/{area}/{locale}: cite the source of a 'no'")

    def test_unverified_rows_do_not_claim_absence(self):
        forbidden = re.compile(r"nepodporuje|nepodporuje|does not support|not supported|neumí|nevie", re.IGNORECASE)
        for key, competitor in cmp.COMPETITORS.items():
            for area, status, note, _ in competitor["rows"]:
                if status == "unverified":
                    for text in note.values():
                        self.assertIsNone(forbidden.search(text), f"{key}/{area}: '{text}'")

    def test_prices_carry_an_iso_currency(self):
        # Ambiguous "$" amounts and any Rodinka Pro amount must never be published.
        ambiguous = re.compile(r"\d\s*\$|\$\s*\d")
        amount = re.compile(r"\b(\d+(?:[.,]\d+)?)\s*(USD|EUR|CZK|Kč)\b|\b(USD|EUR|CZK)\s*\d")
        for text in all_strings((cmp.COMPETITORS, cmp.COMPARISON_PAGES, cmp.HUB, cmp.GUIDE, cmp.RODINKA)):
            self.assertIsNone(ambiguous.search(text), text)
            if amount.search(text):
                self.assertIn("Cozi", text, f"only the verified Cozi Gold price may be quoted: {text}")

    def test_locales_have_the_same_shape(self):
        for name, tree in (("COMMON", cmp.COMMON), ("HUB", cmp.HUB), ("GUIDE", cmp.GUIDE), *((f"page {key}", page) for key, page in cmp.COMPARISON_PAGES.items())):
            self.assertEqual(set(tree), set(LOCALES), name)
            self.assertEqual(shape(tree["cs"]), shape(tree["sk"]), f"{name}: cs/sk differ")
            self.assertEqual(shape(tree["cs"]), shape(tree["en"]), f"{name}: cs/en differ")

    def test_every_competitor_has_a_page_and_paths(self):
        self.assertEqual(set(cmp.COMPETITOR_ORDER), set(cmp.COMPETITORS))
        self.assertEqual(set(cmp.COMPARISON_PAGES), set(cmp.COMPETITORS))
        for key in cmp.COMPETITOR_ORDER:
            self.assertIn(f"vs_{key}", site.PATHS)
            page = cmp.COMPARISON_PAGES[key]
            for locale in LOCALES:
                self.assertGreaterEqual(len(page[locale]["faq"]), 4)
                self.assertIn(cmp.COMPETITORS[key]["name"], page[locale]["h1"])
                self.assertIn("Rodinka", page[locale]["h1"])

    def test_slovak_copy_has_no_czech_letters(self):
        trees = (cmp.COMMON["sk"], cmp.HUB["sk"], cmp.GUIDE["sk"], *(page["sk"] for page in cmp.COMPARISON_PAGES.values()))
        notes = [note["sk"] for competitor in cmp.COMPETITORS.values() for _, _, note, _ in competitor["rows"]]
        notes += [note["sk"] for _, note in cmp.RODINKA.values()]
        for text in [*all_strings(trees), *notes]:
            self.assertIsNone(re.search(r"[řěů]", text, re.IGNORECASE), text)


class GeneratedComparisonPagesTest(unittest.TestCase):
    def test_rendered_pages_match_the_data(self):
        for key in cmp.COMPETITOR_ORDER:
            for locale in LOCALES:
                html = site.render_comparison(key, locale)
                parser = TableParser()
                parser.feed(html)
                self.assertEqual(parser.h1, 1)
                self.assertEqual(parser.rows, len(cmp.COMPETITORS[key]["rows"]), f"{key}/{locale}: one table row per data row")
                self.assertIn(f'<link rel="canonical" href="{site.canonical(site.PATHS[f"vs_{key}"][locale])}" />', html)
                self.assertIn('"@type":"BreadcrumbList"', html)
                self.assertIn('"@type":"Article"', html)
                self.assertIn(cmp.VERIFIED_ON, html)
                for url, _ in cmp.COMPETITORS[key]["sources"].values():
                    self.assertIn(f'href="{url}"', html, f"{key}/{locale}: source {url} not listed")

    def test_generated_files_are_up_to_date(self):
        renderers = {"compare": site.render_compare_hub, "best": site.render_guide}
        for locale in LOCALES:
            for page_key, render in renderers.items():
                committed = site.output_path(site.PATHS[page_key][locale]).read_text(encoding="utf-8")
                self.assertEqual(committed, render(locale), f"{page_key}/{locale}: run python generate_site.py")
            for key in cmp.COMPETITOR_ORDER:
                committed = site.output_path(site.PATHS[f"vs_{key}"][locale]).read_text(encoding="utf-8")
                self.assertEqual(committed, site.render_comparison(key, locale), f"vs_{key}/{locale}: run python generate_site.py")

    def test_pages_are_in_sitemap_and_linked_from_existing_pages(self):
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        for page_key in site.COMPARE_KEYS:
            for locale in LOCALES:
                self.assertIn(f"<loc>{site.canonical(site.PATHS[page_key][locale])}</loc>", sitemap)
        for locale in LOCALES:
            app_page = site.output_path(site.PATHS["app"][locale]).read_text(encoding="utf-8")
            self.assertIn(f'href="{site.PATHS["compare"][locale]}"', app_page)
            planner_page = site.output_path(site.PATHS["planner"][locale]).read_text(encoding="utf-8")
            self.assertIn(f'href="{site.PATHS["best"][locale]}"', planner_page)


if __name__ == "__main__":
    unittest.main()
