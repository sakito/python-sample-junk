#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>
"""
json関連
"""
import json
import uuid
import datetime
import collections

def _support_default(value):
    """
    JSON変換できない型が来た場合の処理
    """
    if isinstance(value, uuid.UUID):
        return str(value)

    elif isinstance(value, datetime.datetime):
        return f'{value:%Y-%m-%dT%H:%M:%s.%f%z}'

    elif isinstance(value, set):
        return sorted(list(value))

    raise TypeError('value is not JSON serializable')


def write_json(data_dict, file_path):
    """
    JSON出力
    """
    data_dict = None
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            data_dict = json.load(f)

    except UnicodeDecodeError as e:
        raise TypeError('file encoding is not UTF-8.') from e

    return data_dict


def load_json(value):
    """
    JSON相当strをdict変換

    value: str or dict
      JSON相当文字列
      dictの場合は変換しない
    """
    if isinstance(value, (str, bytes)):
        try:
            value = json.loads(value)
        except json.decoder.JSONDecodeError as e:
            raise e

    return value


def dump_json(value):
    """
    JSON相当 obj を str 変換

    value: str or dict or list
      JSON相当文字列
      str の場合は変換しない
    """
    if isinstance(value, (dict, list)):
        value = json.dumps(
            value,
            ensure_ascii=False,
            default=_support_default
        )

    return value


def pretty_json(dict_data):
    """
    JSON表示

    dict_data: dict
      JSON表示dict
    """
    return json.dumps(
        dict_data,
        indent=2,
        ensure_ascii=False,
        sort_keys=True,
        separators=(',', ': '),
        default=_support_default,
    )


def flatten(dict_data, parent_key=None, separator='.') -> dict:
    """
    dict の flat 化

    :param dict_data dict: flat対象dict
    :param parent_key str: flat化する時に親キーを付与するか
    :param separator str: flat化時利用するseparator文字
    :return dict: flat化dict
    """
    items = []

    for key, value in dict_data.items():
        new_key = str(parent_key) + separator + key if parent_key else key

        if isinstance(value, collections.abc.MutableMapping):
            items.extend(flatten(value, new_key, separator).items())

        elif isinstance(value, list):
            items.append((new_key, '#  LIST'))
            for k, v in enumerate(value):
                items.extend(flatten({str(k): v}, new_key).items())
        else:
            items.append((new_key, value))

    return dict(items)
