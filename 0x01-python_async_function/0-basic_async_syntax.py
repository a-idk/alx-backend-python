#!/usr/bin/env python3
"""
Title: The basics of async
Author: @a_idk
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ coroutine that takes in int arg that waits for rand delay & returns"""
    d = random.uniform(0, max_delay)
    await asyncio.sleep(d)
    return d
