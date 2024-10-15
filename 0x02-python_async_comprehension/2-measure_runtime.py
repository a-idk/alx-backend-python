#!/usr/bin/env python3

"""
Title: Parallel Comprehension Runtime
Author: @a_idk
"""

import asyncio
from time import perf_counter
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ coroutine that execute async_comp 4x in parallel """

    start_counter = perf_counter()

    para_out = [asyncio.create_task(async_comprehension()) for x in range(4)]
    await asyncio.gather(*para_out)

    return perf_counter() - start_counter
