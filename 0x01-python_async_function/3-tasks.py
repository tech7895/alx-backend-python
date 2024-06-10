#!/usr/bin/env python3
'''This script contains 3's module.
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.This script contains:
    '''Creates an asynchronous task for wait_random.
    '''
    return asyncio.create_task(wait_random(max_delay))
