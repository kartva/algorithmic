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

    pixels: npt.NDArray[np.int32] = np.zeros((height, width, 3), dtype=np.int32)

    # do stuff to the pixels


    return pixels
