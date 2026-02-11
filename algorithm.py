import random
from collections.abc import Callable
import numpy as np
import numpy.typing as npt

from lib.geometry import get_neighbors
from lib.colors import color_diff, MAX_DIFF

# Sig: (iteration, total, pixels_array) -> None
ProgressCallback = Callable[[int, int, npt.NDArray[np.int32]], None]


def run_algorithm(
    colors_list: list[tuple[int, int, int]],
    width: int,
    height: int,
    on_progress: ProgressCallback | None = None,
    progress_interval: int = 1000,
) -> npt.NDArray[np.int32]:
    """
    Run the rainbow smoke algorithm.

    Args:
        colors_list: List of RGB color tuples to place (should be exactly width*height)
        width: Canvas width
        height: Canvas height
        on_progress: Callback called every progress_interval steps with (iteration, total, pixels)
        progress_interval: How often to call the progress callback (default: 1000)

    Returns:
        Numpy array of shape (height, width, 3) with int32 RGB values
    """
    start_x = width // 2
    start_y = height // 2

    # Shuffle colors
    random.shuffle(colors_list)
    total_colors = len(colors_list)

    # Canvas state
    pixels: npt.NDArray[np.int32] = np.zeros((height, width, 3), dtype=np.int32)
    placed: npt.NDArray[np.bool_] = np.zeros((height, width), dtype=np.bool_)
    available: set[tuple[int, int]] = {(start_x, start_y)}

    # Place all colors
    for i, color in enumerate(colors_list):
        if on_progress is not None and i % progress_interval == 0:
            on_progress(i, total_colors, pixels)

        # Find best position by evaluating all available positions
        best_x, best_y = -1, -1
        best_diff = MAX_DIFF

        for ax, ay in available:
            # Calculate minimum color difference to placed neighbors
            min_diff = MAX_DIFF
            for nx, ny in get_neighbors(ax, ay, width, height):
                if placed[ny, nx]:
                    diff = color_diff(pixels[ny, nx], color)
                    if diff < min_diff:
                        min_diff = diff

            if min_diff <= best_diff:
                best_diff = min_diff
                best_x, best_y = ax, ay

        # Place the pixel
        pixels[best_y, best_x] = color
        placed[best_y, best_x] = True

        # Update available set
        available.discard((best_x, best_y))

        # Add empty neighbors to available set
        for nx, ny in get_neighbors(best_x, best_y, width, height):
            if not placed[ny, nx]:
                available.add((nx, ny))

    # Final progress callback
    if on_progress is not None:
        on_progress(total_colors, total_colors, pixels)

    return pixels
