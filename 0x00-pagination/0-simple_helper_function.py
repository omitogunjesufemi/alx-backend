#!/usr/bin/env python3
"""
The function returns a tuple of size two containing s start index
and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters

Page numbers are 1-indexed, i.e. the first page is 1
"""


def index_range(page, page_size):
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
