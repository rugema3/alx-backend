#!/usr/bin/env python3
"""0-simple_heleper_function module."""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Takes two integer arguments page and page_size.
    Returns a tuple of size two containing a start index and an end index.
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
