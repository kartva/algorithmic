"""Command-line interface for the rainbow smoke algorithm."""
import os
import argparse
from PIL import Image

from algorithm import run_algorithm
from lib.colors import generate_rgb_colors, load_image_colors


def cli_progress(iteration: int, total: int, pixels) -> None:
    print(f"Progress: {iteration/total:.1%}", end='\r')


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rainbow Smoke Algorithm - Visualize color spaces",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m cli --rgb
  python -m cli --image ../in/photo.png
  python -m cli --rgb -o result.png
"""
    )

    # Input mode: either --rgb or --image
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "--rgb",
        action="store_true",
        help="Generate RGB color cube (256×128)"
    )
    input_group.add_argument(
        "--image",
        type=str,
        metavar="PATH",
        help="Load colors from image file"
    )

    # Output options
    parser.add_argument(
        "-o", "--output",
        default="output.png",
        help="Output filename (default: output.png)"
    )

    args = parser.parse_args()

    # Get colors
    if args.rgb:
        width, height = 256, 128
        colors_list = generate_rgb_colors(width, height)
        print(f"Generated {len(colors_list)} RGB colors for {width}×{height} canvas")
    else:
        colors_list, width, height = load_image_colors(args.image)
        print(f"Loaded {len(colors_list)} colors from image ({width}×{height})")

    # Create output directory
    os.makedirs("out", exist_ok=True)
    output_path = os.path.join("out", args.output)

    print("Starting generation...")
    result = run_algorithm(colors_list, width, height, on_progress=cli_progress)

    # Save result
    print(f"\nFinished! Saving to {output_path}")
    final_img: Image.Image = Image.fromarray(result.astype("uint8"))
    final_img.save(output_path)


if __name__ == "__main__":
    main()
