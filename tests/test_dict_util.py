#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>
import dict_util as t


def test_to_box():
    """
    to_box
    """
    test_data = {
        'a': 10,
        'b': {
            'c': 20,
        }
    }

    ret = t.to_box(test_data)

    assert 10 == ret.a
    assert {'c': 20} == ret.b
    assert 20 == ret.b.c


def test_is_box():
    """
    is_box
    """
    test_data = 10
    assert not t.is_box(test_data)

    test_data = {
        'a': 10
    }
    assert not t.is_box(test_data)

    assert t.is_box(t.to_box(test_data))
