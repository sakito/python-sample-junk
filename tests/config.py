#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2024 sakito <sakito@sakito.com>

from pathlib import Path

from logging_util import LoggingUtil

PRJ_DIR = (Path(__file__).parent / '..').absolute()

INPUT_DIR = PRJ_DIR / 'tests' / 'input'

DEBUG = True
logger = LoggingUtil().get_logger('debug' if DEBUG else 'all')
