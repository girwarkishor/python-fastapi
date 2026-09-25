#!/usr/bin/env python3

import asyncio

import fire
from mylib import logics

if __name__ == '__main__':
    asyncio.set_event_loop(asyncio.new_event_loop())
    fire.Fire(logics)