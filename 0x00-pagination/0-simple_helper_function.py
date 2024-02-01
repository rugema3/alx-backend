#!/usr/bin/env python3
"""0-simple_heleper_function module."""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Takes two integer arguments page and page_size.
    Returns a tuple of size two containing a start index and an end index.
    """
    opening, closing = 0, 0
    for i in range(page):
        opening = closing
        closing += page_size

    return (opening, closing)
