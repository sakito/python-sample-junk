#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2024 sakito <sakito@sakito.com>
"""
toml_util.py テスト
"""
import toml_util as t
import config


def test_read_toml():
    """
    read_toml
    """
    file_path = config.INPUT_DIR / 'toml_sample.toml'
    data = t.read_toml(file_path)

    expect = {'test': {'a': 10}}

    assert expect == data
