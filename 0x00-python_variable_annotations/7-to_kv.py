#!/usr/bin/env python3
"""
Title: Complex types - string and int/float to tuple
Author: @a_Idk
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ 
    function that takes a string and an int OR float as arguments and
    returns a tuple. The first element of the tuple is the string. 
    The second element is the square of the int/float and should be
    annotated as a float
    """
    return (k, float(v**2))
