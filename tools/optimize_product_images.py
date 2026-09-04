"""Create web-friendly Rodinka product visuals from the supplied PNG exports.

This helper is intentionally outside the production path. The generated WebP
files are committed, so Vercel does not need Pillow or an image build step.
"""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError as exc:  # pragma: no cover - maintainer guidance
    raise SystemExit("This optional helper requires Pillow: python -m pip install Pillow") from exc


ROOT = Path(__file__).resolve().parents[1]
MAX_WIDTH = 900
QUALITY = 86
SOURCES = {
    "01-dnes.png": "rodinka-today-family-overview.webp",
    "02-kalendar.png": "rodinka-shared-family-calendar.webp",
    "03-planovat.png": "rodinka-family-planning.webp",
    "04-aktivity.png": "rodinka-family-activities.webp",
    "05-nakup.png": "rodinka-shared-shopping-list.webp",
    "06-vzpominky.png": "rodinka-family-memories.webp",
    "07-mimco.png": "rodinka-expected-child.webp",
}


def optimize(source: Path, destination: Path) -> tuple[int, int]:
    with Image.open(source) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGB")
        if image.width > MAX_WIDTH:
            height = round(image.height * MAX_WIDTH / image.width)
            image = image.resize((MAX_WIDTH, height), Image.Resampling.LANCZOS)
        destination.parent.mkdir(parents=True, exist_ok=True)
        image.save(destination, "WEBP", quality=QUALITY, method=6, optimize=True)
        return image.size


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", type=Path, help="Directory containing the original PNG exports")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "assets" / "product",
        help="Destination for committed WebP derivatives",
    )
    args = parser.parse_args()

    for source_name, output_name in SOURCES.items():
        source = args.source_dir / source_name
        if not source.is_file():
            raise SystemExit(f"Missing source image: {source}")
        destination = args.output_dir / output_name
        width, height = optimize(source, destination)
        kib = destination.stat().st_size / 1024
        print(f"{source.name} -> {destination.relative_to(ROOT)} ({width}x{height}, {kib:.1f} KiB)")


if __name__ == "__main__":
    main()
