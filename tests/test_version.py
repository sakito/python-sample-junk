#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>
import version as t


def test_get_version():
    """
    get_version
    """
    actual = t.get_version()

    print(actual)
