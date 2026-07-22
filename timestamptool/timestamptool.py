#!/usr/bin/env python3

import time


def get_int_timestamp() -> str:
    return f"{time.time():.0f}"


def get_timestamp(decimals: int = 22) -> str:
    return f"{time.time():.{decimals}f}"
