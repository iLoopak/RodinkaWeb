"""Build the self-hosted WOFF2 webfonts in assets/fonts/ (optional helper).

The generated files are committed, so the production site never needs this script.
Run it only to refresh the fonts after changing the upstream version or the
character set below:

    pip install fonttools brotli
    python tools/build_fonts.py

Why the build looks the way it does
-----------------------------------
The site previously loaded DM Sans and Manrope from fonts.googleapis.com. To keep
the typography byte-for-byte identical after self-hosting, this script reproduces
exactly what the Google Fonts CSS API used to serve:

* Same upstream releases: DM Sans 4.004 and Manrope 4.504.
* DM Sans is a two-axis font (opsz 9-40, wght 100-1000). The Google Fonts API
  pinned the optical size at 14 for the `css2?family=DM+Sans:wght@...` query the
  site used, so this script pins opsz=14 too. Using the upstream default (opsz=9)
  would render visibly different letterforms.
* Manrope ships a single wght axis and was served unmodified.

Two deliberate reductions keep the payload small without touching appearance:

* The weight axis is clipped to the range the stylesheet actually asks for
  (DM Sans 400-700, Manrope 700-800). Rendering inside that range is unchanged;
  clipping just drops delta data the site can never reach. This is what makes
  the variable fonts smaller than static instances would be.
* The character set is Latin-1 plus the Central European letters, so Czech and
  Slovak diacritics render from the webfont. See CHARACTER_SET below.
"""

from __future__ import annotations

import sys
import urllib.request
from pathlib import Path

try:
    from fontTools import subset
    from fontTools.ttLib import TTFont
    from fontTools.varLib.instancer import instantiateVariableFont
except ModuleNotFoundError:  # pragma: no cover - helper script, not a build dependency
    sys.exit("This helper needs fontTools and brotli: pip install fonttools brotli")


ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "assets" / "fonts"
UPSTREAM = "https://raw.githubusercontent.com/google/fonts/main/ofl"

# Latin-1 covers English plus the acute/diaeresis/circumflex vowels shared by Czech
# and Slovak. The explicit list adds the Latin Extended-A letters those two
# languages need (caron, ring, l-acute, l-caron, r-acute) and leaves room for
# Polish and Hungarian without pulling in the whole 128-codepoint block.
CENTRAL_EUROPEAN = (
    "ĀāĂăĄąĆćČčĎďĐđĒēĖėĘęĚěĞğĪīĮįİıĹĺĽľŁłŃńŇňŐőŒœŔŕŘřŚśŞşŠšŢţŤťŮůŰűŲųŸŹźŻżŽžĲĳ"
)
# Typographic punctuation the site uses (quotes, dashes, ellipsis) plus the
# currency and math signs Google's "latin" subset included.
PUNCTUATION = (
    "–—‘’‚“”„†…‰‹›"
    "⁄€™↑↓−ˆ˜˙˛˝"
)
# NOTE: U+2192 (the "→" in call-to-action links) is deliberately absent. Google's
# "latin" subset did not include it either, so it has always rendered from the
# system font. Adding it here would change how those arrows look.
CHARACTER_SET = (
    set(range(0x20, 0x7F))
    | set(range(0xA0, 0x100))
    | {ord(c) for c in CENTRAL_EUROPEAN}
    | {ord(c) for c in PUNCTUATION}
)

FONTS = (
    {
        "name": "DM Sans",
        "source": f"{UPSTREAM}/dmsans/DMSans%5Bopsz%2Cwght%5D.ttf",
        "license": f"{UPSTREAM}/dmsans/OFL.txt",
        "version": "Version 4.004",
        # opsz 14 reproduces the instance the Google Fonts API served.
        "location": {"opsz": 14, "wght": (400, 700)},
        "output": "dm-sans-latin-ext-400-700.woff2",
        "license_output": "OFL-DMSans.txt",
    },
    {
        "name": "Manrope",
        "source": f"{UPSTREAM}/manrope/Manrope%5Bwght%5D.ttf",
        "license": f"{UPSTREAM}/manrope/OFL.txt",
        "version": "Version 4.504",
        "location": {"wght": (700, 800)},
        "output": "manrope-latin-ext-700-800.woff2",
        "license_output": "OFL-Manrope.txt",
    },
)


def fetch(url: str, cache: Path) -> bytes:
    if cache.exists():
        return cache.read_bytes()
    with urllib.request.urlopen(url) as response:  # noqa: S310 - pinned Google Fonts URL
        payload = response.read()
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_bytes(payload)
    return payload


def build(spec: dict, cache_dir: Path) -> None:
    source = cache_dir / f"{spec['output']}.source.ttf"
    fetch(spec["source"], source)
    font = TTFont(source)
    # Keep the upstream head.modified stamp so repeated builds are byte-identical.
    font.recalcTimestamp = False

    released = font["name"].getDebugName(5) or ""
    if not released.startswith(spec["version"]):
        raise SystemExit(
            f"{spec['name']}: upstream is {released!r}, expected {spec['version']!r}. "
            "Re-check the rendering before bumping the pinned version."
        )

    covered = CHARACTER_SET & {c for c in font.getBestCmap() if c >= 0x20}
    options = subset.Options()
    options.flavor = "woff2"
    options.notdef_outline = False
    options.name_IDs = ["*"]
    options.name_legacy = True
    options.name_languages = ["*"]
    subsetter = subset.Subsetter(options=options)
    subsetter.populate(unicodes=covered)
    # Subset before instancing: clipping an axis first can strip the variation data
    # the subsetter expects to still be present for blank glyphs such as U+00A0.
    subsetter.subset(font)
    instantiateVariableFont(font, spec["location"], inplace=True, updateFontNames=False)

    font.flavor = "woff2"
    destination = OUT_DIR / spec["output"]
    font.save(destination)

    (OUT_DIR / spec["license_output"]).write_bytes(fetch(spec["license"], cache_dir / spec["license_output"]))

    axes = ", ".join(f"{a.axisTag} {a.minValue:g}-{a.maxValue:g}" for a in font["fvar"].axes)
    print(f"{destination.relative_to(ROOT)}: {destination.stat().st_size:,} B, {len(covered)} glyphs, axes {axes}")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cache_dir = Path(__file__).resolve().parent / ".font-cache"
    for spec in FONTS:
        build(spec, cache_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
