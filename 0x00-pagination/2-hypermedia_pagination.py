#!/usr/bin/env python3
"""Define 2-hypermedia_pagination module."""
import csv
import math
from typing import List, Optional, Dict, Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculate the start and end index for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start and end index for
                            the specified page.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size - 1
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset.

        Args:
            page (int): The page number (1-indexed). Default is 1.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            List[List]: A list of rows corresponding to the specified
                        page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset_length = len(self.dataset())
        if dataset_length == 0 or (page - 1) * page_size >= dataset_length:
            return []

        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index + 1]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """
        Get a hypermedia representation of a dataset page.

        Args:
            page (int): The page number (1-indexed). Default is 1.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            Dict[str, any]: A dictionary containing hypermedia
                            representation of the dataset page.
        """
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper_data = {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return hyper_data
