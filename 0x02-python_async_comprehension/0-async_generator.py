#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random


async def async_generator():
    """ Function that loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10"""
    for _ in range(10):
        random_number: float = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield random_number
