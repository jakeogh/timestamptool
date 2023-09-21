#!/usr/bin/env python3
# -*- coding: utf8 -*-
# tab-width:4

from __future__ import annotations

import time


def get_int_timestamp() -> str:
    stamp = f"{time.time():.0f}"
    return stamp


def get_timestamp() -> str:
    stamp = f"{time.time():.22f}"
    return stamp
