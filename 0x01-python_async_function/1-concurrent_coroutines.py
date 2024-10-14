#!/usr/bin/env python3
"""
Title: Executing Multiple Coroutines
Author: @a_idk
"""

import asyncio
import random
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    async fxn that imports wait_random 4m previous file & return lst of delays
    """
    delay_lst = []
    for x in range(n):
        delay_lst.append(asyncio.create_task(wait_random(max_delay)))
    return sorted(await asyncio.gather(*delay_lst))
