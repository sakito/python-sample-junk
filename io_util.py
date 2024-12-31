#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2024 sakito <sakito@sakito.com>
"""
io 関連
"""

import hashlib


def read_file_bin(file_path, mode='rb') -> str:
    """
    指定ファイル全データ読み込み

    file_path: str or Path ファイルパス

    return: str ファイル内容文字列
    """
    data = ''
    with open(file_path, mode, encoding='utf-8') as f:
        data = f.read()

    return data


def read_file(file_path) -> str:
    """
    テキストファイル読み込み

    file_path: str or Path ファイルパス
    """
    return read_file_bin(file_path, mode='r')


def write_file_bin(file_path, data, mode='mode'):
    """
    指定ファイル出力

    file_path: str or Path ファイルパス
    data: str or bin 出力データ
    """
    with open(file_path, mode, encoding='utf-8') as f:
        f.write(data)


def write_file(file_path, data):
    """
    テキストファイル出力

    file_path: str or Path ファイルパス
    data: str 出力データ
    """
    write_file_bin(file_path, data, mode='w')


def itr_file_read(f, size=64 * 1024):
    """
    巨大ファイル順次読み込み

    利用例:
    with open(file_path, 'r') as f:
        for chunk in itr_file_read(f):
            chunk処理
    """
    while True:
        block = f.read(size)
        if not block:
            break
        yield block


def get_sha256(file_path):
    """
    sha256のhash値生成
    巨大ファイル対応
    """
    hash_obj = hashlib.sha256()

    with open(file_path, 'rb') as f:
        for block in itr_file_read(f):
            hash_obj.update(block)

    digest = hash_obj.hexdigest()

    return digest
