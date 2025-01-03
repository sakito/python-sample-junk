#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>
"""
test json_util
"""
import pytest

import json_util as t


@pytest.fixture
def dict_data():
    """
    データ設定
    """
    return {
        'a': 10,
        'b': {
            'c': 20,
        }
    }



def test_load_json(dict_data):
    """
    load_json
    """
    str_data = '{"a": 10, "b": {"c": 20}}'

    actual = t.load_json(str_data)

    assert dict_data == actual


def test_dupm_json(dict_data):
    """
    dump_json
    """
    ret = t.dump_json(dict_data)

    assert '{"a": 10, "b": {"c": 20}}' == ret


def test_pretty_json(dict_data):
    """
    pretty_json
    """
    ret = t.pretty_json(dict_data)

    expected = """{
  "a": 10,
  "b": {
    "c": 20
  }
}"""

    assert expected == ret


def test_flatten(dict_data):
    """
    flatten
    """
    assert {'a': 10, 'b.c': 20} == t.flatten(dict_data)
    assert {'parent.a': 10, 'parent.b.c': 20} == t.flatten(dict_data, 'parent')
    assert {'a': 10, 'b_c': 20} == t.flatten(dict_data, separator='_')
