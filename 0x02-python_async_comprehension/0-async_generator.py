#!/usr/bin/env python3

"""
TItle: Async Generator
Author: @a_idk
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ coroutine that loops 10 times """

    for t in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
