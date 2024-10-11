#!/usr/bin/env python3
"""
Title: Complex types - mixed list
Author: @a_Idk
"""
from typing import List, Union


def sum_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Fxn takes a list of int & floats & returns their sum """
    return float(sum(mxd_lst))
