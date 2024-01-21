#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """coroutine that takes an int and return random number"""
    random_delay: float = random.uniform(0, max_delay)

    await asyncio.sleep(random_delay)

    return random_delay
