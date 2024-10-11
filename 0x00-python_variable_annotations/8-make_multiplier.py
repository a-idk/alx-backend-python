#!/usr/bin/env python3
"""
Title: Complex types - functions
Author: @a_Idk
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that takes a float argument & returns a fxn multiplied by a float
    """
    return lamda x: x * multiplier
