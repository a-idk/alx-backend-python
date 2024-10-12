#!/usr/bin/env python3
"""
Title: Duck typing - first element of a sequence
Author: @a_Idk
"""
from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """ fxn that zooms array """
    zoomed_in: List[int] = [
            item for item in lst
            for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
