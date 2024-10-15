#!/usr/bin/env python3

"""
Title: Async Comprehensions
Author: @a_Idk
"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ fxn that collects 10 random numbers using async comprehension """

    return [x async for x in async_generator()]
