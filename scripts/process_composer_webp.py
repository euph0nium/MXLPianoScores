#!/usr/bin/env python3
"""
Utility script to process composer illustrations into transparent WebP assets.
Supports:
1. Circular artistic avatar: Perfect circular art area with watercolor background and details,
   while everything outside the circle is 100% transparent (with Lanczos 4x subpixel antialiasing).
2. Vignette scene illustration: Soft feathered alpha edge transparency.
"""

import sys
import os
import numpy as np
from PIL import Image, ImageDraw

def make_circular_avatar(input_path: str, output_path: str, circle_radius_ratio: float = 0.443):
    """
    Clips image to a circular art badge where the inside contains the full rich artwork,
    and the outside (the 4 corners) is 100% transparent WebP with smooth antialiasing.
    """
    img = Image.open(input_path).convert('RGBA')
    w, h = img.size

    # 4x supersampling for buttery smooth anti-aliased edge
    scale = 4
    mask_hires = Image.new('L', (w * scale, h * scale), 0)
    draw = ImageDraw.Draw(mask_hires)

    cx = (w * scale) / 2.0
    cy = (h * scale) / 2.0
    radius = (w * scale) * circle_radius_ratio

    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], fill=255)
    mask = mask_hires.resize((w, h), Image.Resampling.LANCZOS)

    img.putalpha(mask)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    img.save(output_path, 'WEBP', quality=95, method=6)
    print(f"✅ Generated circular transparent WebP avatar: {output_path}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 process_composer_webp.py <input_img> <output_webp> [radius_ratio]")
        sys.exit(1)
    ratio = float(sys.argv[3]) if len(sys.argv) > 3 else 0.443
    make_circular_avatar(sys.argv[1], sys.argv[2], ratio)
