"""Composite a localized marketing header over an original product visual.

Only the headline/pill region is taken from the localized draft. The Rodinka
logo, phone mockup and every in-app pixel come from the original web asset.
This helper is outside the production path; generated WebP files are committed.
"""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from PIL import Image, ImageFilter
except ImportError as exc:  # pragma: no cover - maintainer guidance
    raise SystemExit("This optional helper requires Pillow: python -m pip install Pillow") from exc


HEADER_BOX = (18, 112, 882, 365)
FEATHER_RADIUS = 18
QUALITY = 86


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=Path, help="Original 900 px Rodinka WebP asset")
    parser.add_argument("localized_draft", type=Path, help="Localized header draft")
    parser.add_argument("output", type=Path, help="Final localized WebP path")
    args = parser.parse_args()

    with Image.open(args.base) as opened_base, Image.open(args.localized_draft) as opened_draft:
        base = opened_base.convert("RGB")
        draft = opened_draft.convert("RGB")
        target_height = round(draft.height * base.width / draft.width)
        draft = draft.resize((base.width, target_height), Image.Resampling.LANCZOS)

        if draft.height < HEADER_BOX[3] or base.height < HEADER_BOX[3]:
            raise SystemExit("Input is too short for the maintained header region")

        mask = Image.new("L", base.size, 0)
        solid = Image.new("L", base.size, 0)
        solid.paste(255, HEADER_BOX)
        mask = solid.filter(ImageFilter.GaussianBlur(FEATHER_RADIUS))
        draft_canvas = Image.new("RGB", base.size)
        visible_height = min(base.height, draft.height)
        draft_canvas.paste(draft.crop((0, 0, base.width, visible_height)), (0, 0))
        base.paste(draft_canvas, (0, 0), mask)

        args.output.parent.mkdir(parents=True, exist_ok=True)
        base.save(args.output, "WEBP", quality=QUALITY, method=6, optimize=True)
        print(f"Created {args.output} ({base.width}x{base.height}, {args.output.stat().st_size / 1024:.1f} KiB)")


if __name__ == "__main__":
    main()
