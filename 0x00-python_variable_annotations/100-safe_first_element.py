#!/usr/bin/env python3
"""
Title: Duck typing - first element of a sequence
Author: @a_Idk
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ function that safely gets first element """
    if lst:
        return lst[0]
    else:
        return None
