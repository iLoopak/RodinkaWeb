"""Create web-friendly Rodinka product visuals from the store listing exports.

This helper is intentionally outside the production path. The generated WebP
files are committed, so Vercel does not need Pillow or an image build step.

The source is the App Store 6.9" listing folder from the app repository
(`Rodinka/promo/store-listing/app-store-6.9`), which holds one subfolder per
language with exports named by their store order (`01-dnes.png`,
`01-today.png`, ...). Only the numeric prefix is matched, so the localized file
names do not need to be listed here.
"""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError as exc:  # pragma: no cover - maintainer guidance
    raise SystemExit("This optional helper requires Pillow: python -m pip install Pillow") from exc


ROOT = Path(__file__).resolve().parents[1]
# Every product image on the site shares one frame; generate_site.py declares it
# on each <img>. The 1320x2868 store exports are 4 px taller at this width, so
# the bottom edge is trimmed: the phone runs off the canvas there anyway.
SIZE = (900, 1951)
QUALITY = 86
LOCALES = ("cs", "sk", "en")
SOURCES = {
    "01": "rodinka-today-family-overview",
    "02": "rodinka-shared-family-calendar",
    "03": "rodinka-family-memories",
    "04": "rodinka-family-planning",
    "05": "rodinka-family-chores",
    "06": "rodinka-shared-shopping-list",
}


def find_source(locale_dir: Path, prefix: str) -> Path:
    matches = sorted(locale_dir.glob(f"{prefix}-*.png"))
    if len(matches) != 1:
        raise SystemExit(f"Expected one {prefix}-*.png in {locale_dir}, found {len(matches)}")
    return matches[0]


def optimize(source: Path, destination: Path) -> tuple[int, int]:
    with Image.open(source) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGB")
        image = ImageOps.fit(image, SIZE, Image.Resampling.LANCZOS, centering=(0.5, 0.0))
        destination.parent.mkdir(parents=True, exist_ok=True)
        image.save(destination, "WEBP", quality=QUALITY, method=6)
        return image.size


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", type=Path, help="Store listing folder with cs/, sk/ and en/ subfolders")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "assets" / "product",
        help="Destination for committed WebP derivatives",
    )
    args = parser.parse_args()

    for locale in LOCALES:
        for prefix, stem in SOURCES.items():
            source = find_source(args.source_dir / locale, prefix)
            suffix = "" if locale == "cs" else f"-{locale}"
            destination = args.output_dir / f"{stem}{suffix}.webp"
            width, height = optimize(source, destination)
            kib = destination.stat().st_size / 1024
            print(f"{locale}/{source.name} -> {destination.relative_to(ROOT)} ({width}x{height}, {kib:.1f} KiB)")


if __name__ == "__main__":
    main()
