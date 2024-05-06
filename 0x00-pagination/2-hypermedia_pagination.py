#!/usr/bin/env python3
"""
Implement a method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10.
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Initialization of the server class """
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
        Get dataset from a particular range

        If the input arguments are out of range for the dataset
        an empty list should be returned.
        """
        assert (isinstance(page, int))
        assert (isinstance(page_size, int))
        assert (page > 0) and (page_size > 0)
        start_index, end_index = index_range(page, page_size)
        data_set = self.dataset()
        return data_set[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        returns a dictionary containing the following key-value pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        hyper_dict = {}

        data_set = self.get_page(page, page_size)
        total_pages = (len(self.dataset()))//(page_size)

        hyper_dict["page_size"] = page_size
        hyper_dict["page"] = page
        hyper_dict["data"] = data_set

        next_page = None
        prev_page = None

        if page < total_pages:
            next_page = page + 1

        if page > 1:
            prev_page = page - 1

        hyper_dict["next_page"] = next_page

        hyper_dict["prev_page"] = prev_page

        hyper_dict["total_pages"] = total_pages

        return hyper_dict


def index_range(page: int, page_size: int):
    """
    Arguments:
    - page and
    - page_size

    The function returns a tuple of size two containing s start index
    and an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters

    Page numbers are 1-indexed, i.e. the first page is 1
    """
    return ((page_size * (page - 1)), (page_size * page))
