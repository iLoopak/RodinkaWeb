"""Dependency-free quality gate for the generated Rodinka marketing site."""

from __future__ import annotations

import json
import re
import struct
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent.parent
SITE = "https://mojerodinka.cz"

FAMILIES = {
    "home": {"cs": "/", "sk": "/sk/", "en": "/en/"},
    "planner": {"cs": "/rodinny-planovac/", "sk": "/sk/rodinny-planovac/", "en": "/en/family-planner/"},
    "calendar": {"cs": "/rodinny-kalendar/", "sk": "/sk/rodinny-kalendar/", "en": "/en/family-calendar/"},
    "shopping": {"cs": "/sdileny-nakupni-seznam/", "sk": "/sk/zdielany-nakupny-zoznam/", "en": "/en/shared-shopping-list/"},
    "chores": {"cs": "/ukoly-pro-rodinu/", "sk": "/sk/ulohy-pre-rodinu/", "en": "/en/family-chores/"},
    "meals": {"cs": "/planovani-jidla/", "sk": "/sk/planovanie-jedal/", "en": "/en/meal-planning/"},
    "app": {"cs": "/aplikace-pro-rodinu/", "sk": "/sk/aplikacia-pre-rodinu/", "en": "/en/family-organizer/"},
}

EXPECTED = {
    path: (family, locale)
    for family, variants in FAMILIES.items()
    for locale, path in variants.items()
}

META_REQUIRED = {
    "description", "robots", "theme-color", "og:title", "og:description",
    "og:type", "og:url", "og:site_name", "og:locale", "og:image",
    "og:image:width", "og:image:height", "og:image:alt", "twitter:card",
    "twitter:title", "twitter:description", "twitter:image", "twitter:image:alt",
}


def file_for_path(path: str) -> Path:
    return ROOT / "index.html" if path == "/" else ROOT / path.strip("/") / "index.html"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_lang = ""
        self.title = ""
        self._in_title = False
        self.h1_count = 0
        self.ids: list[str] = []
        self.meta: dict[str, str] = {}
        self.canonical = ""
        self.alternates: dict[str, str] = {}
        self.hrefs: list[tuple[str, bool]] = []
        self.jsonld: list[str] = []
        self._in_jsonld = False
        self._json_buffer: list[str] = []
        self._switcher_depth = 0
        self._depth = 0

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        attrs = {key: value or "" for key, value in attrs_list}
        self._depth += 1
        classes = set(attrs.get("class", "").split())
        if "language-switcher" in classes:
            self._switcher_depth = self._depth
        if tag == "html":
            self.html_lang = attrs.get("lang", "")
        if tag == "title":
            self._in_title = True
        if tag == "h1":
            self.h1_count += 1
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "meta":
            key = attrs.get("name") or attrs.get("property")
            if key:
                self.meta[key] = attrs.get("content", "")
        if tag == "link":
            rel = set(attrs.get("rel", "").split())
            if "canonical" in rel:
                self.canonical = attrs.get("href", "")
            if "alternate" in rel and attrs.get("hreflang"):
                self.alternates[attrs["hreflang"]] = attrs.get("href", "")
        if tag == "a" and attrs.get("href"):
            self.hrefs.append((attrs["href"], bool(self._switcher_depth)))
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self._in_jsonld = True
            self._json_buffer = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
        if tag == "script" and self._in_jsonld:
            self.jsonld.append("".join(self._json_buffer))
            self._in_jsonld = False
        if self._switcher_depth == self._depth:
            self._switcher_depth = 0
        self._depth -= 1

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data
        if self._in_jsonld:
            self._json_buffer.append(data)


def internal_path(href: str) -> str | None:
    if href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
        return None
    if href.startswith(SITE):
        return urlparse(href).path
    if href.startswith("/") and not href.startswith("//"):
        return urlparse(href).path
    return None


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"Not a PNG file: {path}")
    return struct.unpack(">II", data[16:24])


def main() -> int:
    errors: list[str] = []
    pages: dict[str, PageParser] = {}
    titles: list[str] = []
    descriptions: list[str] = []
    linked_pages: set[str] = set()

    for path, (family, locale) in EXPECTED.items():
        file_path = file_for_path(path)
        if not file_path.is_file():
            errors.append(f"Missing HTML for {path}: {file_path}")
            continue
        text = file_path.read_text(encoding="utf-8")
        parser = PageParser()
        try:
            parser.feed(text)
        except Exception as exc:
            errors.append(f"HTML parse failed for {path}: {exc}")
            continue
        pages[path] = parser

        if parser.html_lang != locale:
            errors.append(f"{path}: html lang is {parser.html_lang!r}, expected {locale!r}")
        if parser.h1_count != 1:
            errors.append(f"{path}: expected one H1, found {parser.h1_count}")
        duplicate_ids = [key for key, count in Counter(parser.ids).items() if count > 1]
        if duplicate_ids:
            errors.append(f"{path}: duplicate IDs: {duplicate_ids}")
        if not parser.title.strip():
            errors.append(f"{path}: missing title")
        titles.append(parser.title.strip())
        descriptions.append(parser.meta.get("description", ""))

        expected_canonical = f"{SITE}{path}"
        if parser.canonical != expected_canonical:
            errors.append(f"{path}: canonical {parser.canonical!r} != {expected_canonical!r}")
        missing_meta = sorted(META_REQUIRED - parser.meta.keys())
        if missing_meta:
            errors.append(f"{path}: missing metadata {missing_meta}")
        if parser.meta.get("og:url") != expected_canonical:
            errors.append(f"{path}: og:url does not match canonical")
        expected_og_locale = {"cs": "cs_CZ", "sk": "sk_SK", "en": "en_US"}[locale]
        if parser.meta.get("og:locale") != expected_og_locale:
            errors.append(f"{path}: incorrect og:locale")
        expected_og_image = f"{SITE}/" + {"cs": "og-image.png", "sk": "og-image-sk.png", "en": "og-image-en.png"}[locale]
        if parser.meta.get("og:image") != expected_og_image or parser.meta.get("twitter:image") != expected_og_image:
            errors.append(f"{path}: social image is not localized for {locale}")
        image_file = ROOT / urlparse(expected_og_image).path.lstrip("/")
        if image_file.is_file():
            width, height = png_dimensions(image_file)
            if parser.meta.get("og:image:width") != str(width) or parser.meta.get("og:image:height") != str(height):
                errors.append(f"{path}: social image dimensions do not match the PNG")

        expected_alternates = {code: f"{SITE}{href}" for code, href in FAMILIES[family].items()}
        expected_alternates["x-default"] = f"{SITE}{FAMILIES[family]['cs']}"
        if parser.alternates != expected_alternates:
            errors.append(f"{path}: hreflang set is not complete and reciprocal")

        if len(parser.jsonld) != 1:
            errors.append(f"{path}: expected one JSON-LD block, found {len(parser.jsonld)}")
        else:
            try:
                payload = json.loads(parser.jsonld[0])
                graph = payload.get("@graph", [])
                types = {item.get("@type") for item in graph}
                if not {"WebSite", "WebApplication", "WebPage"}.issubset(types):
                    errors.append(f"{path}: JSON-LD graph lacks required entities")
                webapps = [item for item in graph if item.get("@type") == "WebApplication"]
                if not webapps or webapps[0].get("@id") != f"{SITE}/#webapp":
                    errors.append(f"{path}: unstable WebApplication @id")
                webpages = [item for item in graph if item.get("@type") == "WebPage"]
                if not webpages or webpages[0].get("inLanguage") != locale:
                    errors.append(f"{path}: JSON-LD WebPage language mismatch")
            except json.JSONDecodeError as exc:
                errors.append(f"{path}: invalid JSON-LD: {exc}")

        if "lorem ipsum" in text.lower() or "example.com" in text.lower():
            errors.append(f"{path}: placeholder content found")
        if "https://app.mojerodinka.cz" not in text:
            errors.append(f"{path}: missing CTA link to the web application")
        if locale == "sk" and re.search(r"[řěů]", text, re.IGNORECASE):
            errors.append(f"{path}: likely Czech text leaked into Slovak HTML")

        for href, in_switcher in parser.hrefs:
            target = internal_path(href)
            if target is None or target in {"/styles.css", "/script.js"}:
                continue
            if target in EXPECTED:
                linked_pages.add(target)
                target_locale = EXPECTED[target][1]
                if not in_switcher and target_locale != locale:
                    errors.append(f"{path}: content link crosses from {locale} to {target_locale}: {href}")
            elif not Path(ROOT / target.lstrip("/")).is_file():
                errors.append(f"{path}: broken internal link {href}")

    title_duplicates = [value for value, count in Counter(titles).items() if value and count > 1]
    description_duplicates = [value for value, count in Counter(descriptions).items() if value and count > 1]
    if title_duplicates:
        errors.append(f"Duplicate titles: {title_duplicates}")
    if description_duplicates:
        errors.append(f"Duplicate descriptions: {description_duplicates}")

    orphaned = set(EXPECTED) - linked_pages
    if orphaned:
        errors.append(f"Pages not reached by normal HTML links: {sorted(orphaned)}")

    try:
        sitemap_root = ET.parse(ROOT / "sitemap.xml").getroot()
        namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        sitemap_urls = {url.text or "" for url in sitemap_root.findall("s:url/s:loc", namespace)}
        expected_urls = {f"{SITE}{path}" for path in EXPECTED}
        if sitemap_urls != expected_urls:
            errors.append("sitemap.xml does not exactly match canonical page URLs")
    except (ET.ParseError, OSError) as exc:
        errors.append(f"Invalid sitemap.xml: {exc}")

    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    if "User-agent: *" not in robots or "Allow: /" not in robots or f"Sitemap: {SITE}/sitemap.xml" not in robots:
        errors.append("robots.txt is incomplete")

    try:
        json.loads((ROOT / "vercel.json").read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        errors.append(f"Invalid vercel.json: {exc}")

    for asset in ("styles.css", "script.js", "favicon.svg", "favicon-96.png", "apple-touch-icon.png", "og-image.png", "og-image-sk.png", "og-image-en.png"):
        if not (ROOT / asset).is_file():
            errors.append(f"Missing shared asset: {asset}")

    if errors:
        print(f"SEO validation failed with {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"SEO validation passed for {len(pages)} pages in 3 languages.")
    print("Titles, descriptions, H1s, canonicals, hreflang, JSON-LD, sitemap and internal links are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
