#!/usr/bin/env python3
"""
Title: Duck typing - first element of a sequence
Author: @a_Idk
"""
from typing import Any, Union, Mapping, TypeVar


# Assigning variable to get a shorter length char length
T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """ function that safely retrieves value from a dict using a given key """
    if key in dct:
        return dct[key]
    else:
        return default
