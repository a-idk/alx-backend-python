#!/usr/bin/env python3
"""
Title: Measure Runtime
Author: @a_idk
"""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ fcn that measures the total executtion time & returns total time/n """

    begin = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    out = (end - begin) / n

    return out
