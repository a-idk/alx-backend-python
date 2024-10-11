#!/usr/bin/env python3
"""
Title: duck type an iterable object
Author: @a_Idk
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ function that return values with the appropriate types """
    return [(i, len(i)) for i in lst]
