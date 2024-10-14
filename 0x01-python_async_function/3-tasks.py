#!/usr/bin/env python3
"""
Title: Tasks
Author: @a_idk
"""

import asyncio
import time

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ fxn that takes an int and returns a asyncio task """

    return asyncio.create_task(wait_random(max_delay))
