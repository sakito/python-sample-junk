#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2024 sakito <sakito@sakito.com>

import io_util as t
import config


def test_read_file():
    """
    read_file
    """
    file_path = config.INPUT_DIR / 'file_sample.txt'
    data = t.read_file(file_path)

    assert 'a\n' == data
