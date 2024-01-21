#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """coroutine that call wait_random n times"""
    random_delay_list: List[float] = []

    for i in range(n):
        random_delay_list.append(await task_wait_random(max_delay))

    return sorted(random_delay_list)
