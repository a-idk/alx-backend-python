#!/usr/bin/env python3
"""
Title: Tasks 2
Author: @a_idk
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ fxn that retuens an asyncio task """

    tasks = [task_wait_random(max_delay) for i in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]
