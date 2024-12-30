#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2024 sakito <sakito@sakito.com>
"""
tomlファイル処理

python 3.11 以上では tomllib 標準

それ以下の場合 完全互換ライブラリである tomli を利用
pip install tomli
"""
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


def read_toml(file_path):
    """
    file_path: str or Path

    return: dict
    """
    data = None
    with open(file_path, mode='rb') as f:
        data = tomllib.load(f)

    return data
