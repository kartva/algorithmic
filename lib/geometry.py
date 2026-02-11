"""Geometry utilities for rainbow smoke algorithm."""
from collections.abc import Iterator


def get_neighbors(x: int, y: int, width: int, height: int) -> Iterator[tuple[int, int]]:
    """Gets valid neighbors for a given coordinate (3 to 8 neighbors)."""
    for dy in range(-1, 2):
        ny = y + dy
        if 0 <= ny < height:
            for dx in range(-1, 2):
                nx = x + dx
                if 0 <= nx < width and (dx != 0 or dy != 0):
                    yield nx, ny


def is_in_heart(x: int, y: int, width: int, height: int) -> bool:
    """
    Check if a pixel is within a heart shape.
    Uses a simple implicit function: x^2 + (y - |x|^0.5)^2 < 1
    """
    # Normalize to [-1, 1] range
    nx = (x / width) * 2 - 1
    ny = (y / height) * 2 - 1
    
    # Heart implicit function (simple and symmetric)
    # Invert y so heart points up
    ny = -ny
    
    # Check if point is inside heart boundary
    xx = nx * nx
    # The |x|^0.5 creates the rounded bumps at the top
    bump_height = abs(nx) ** 0.5
    yy = (ny - bump_height) ** 2
    
    return xx + yy <= 1.0
