"""Color palette generation and utilities."""
import sys
from typing import cast
from PIL import Image
import numpy as np
import numpy.typing as npt

MAX_DIFF = 255 * 255 * 3 + 1

def color_diff(c1: npt.NDArray[np.int32], c2: npt.NDArray[np.int32]) -> int:
    """
    Args:
        c1: First color as (R, G, B) array
        c2: Second color as (R, G, B) array

    Returns:
        Squared Euclidean distance between the colors
    """
    diff = c1 - c2
    return int(np.sum(diff * diff))


def generate_rgb_colors(width: int, height: int) -> list[tuple[int, int, int]]:
    """
    Generate a uniform list of RGB colors sized to fit the canvas.
    """
    total_pixels = width * height

    # Find the cube dimension: solve n^3 >= total_pixels for n
    num_colors = 1
    while num_colors ** 3 < total_pixels:
        num_colors += 1

    colors_list: list[tuple[int, int, int]] = []

    # Generate the full cube across color space, then take what we need
    for r in range(num_colors):
        for g in range(num_colors):
            for b in range(num_colors):
                colors_list.append((
                    int(r * 255 / (num_colors - 1)) if num_colors > 1 else 0,
                    int(g * 255 / (num_colors - 1)) if num_colors > 1 else 0,
                    int(b * 255 / (num_colors - 1)) if num_colors > 1 else 0,
                ))

    # Return exactly the number of colors needed to fill the canvas
    return colors_list[:total_pixels]


def load_image_colors(
    image_path: str,
    target_width: int = 256,
    target_height: int = 128,
) -> tuple[list[tuple[int, int, int]], int, int]:
    """
    Load colors from an image file, downscaling to target dimensions.
    """
    try:
        img = Image.open(image_path).convert("RGB")
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)

    w, h = img.size

    print(f"Resizing image from {w}x{h} to {target_width}x{target_height}")
    img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    w, h = target_width, target_height

    colors_data = img.getdata()
    colors_list = list(cast(list[tuple[int, int, int]], colors_data))
    print(f"Loaded {len(colors_list)} pixels from {image_path} ({w}x{h})")

    return colors_list, w, h
