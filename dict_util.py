#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>
"""
辞書操作
"""
import json

from box import Box
from config import logger


class DictUtilException(Exception):
    """
    例外
    """
    def __init__(self, error_code, message):
        """
        コンストラクタ

        error_code: str
        message: str
          内部処理でのエラーハンドリング用に必要な文字列
        """
        super().__init__()
        self.error_code = error_code
        self.message = message

    def __str__(self):
        return f'{self.error_code}: {self.message}'

    def get_message(self, message=None):
        """
        メッセージ取得
        """
        if message is None:
            message = self.message

        return {
            'error_code': self.error_code,
            'message': message,
        }


def to_box(dict_data, default_box=False):
    """
    dict を Box に変換

    dict_data: dict or str(json.loads可能形式)
      変換対象辞書

    return: Box
      変換したオブジェクト
    """
    try:
        if isinstance(dict_data, str):
            dict_data = json.loads(dict_data)

        if default_box:
            ret = Box(dict_data, default_box=default_box)
        else:
            ret = Box(dict_data)

    except Exception as e:
        msg = f'Boxオブジェクトへの変換に失敗しました: {dict_data}'
        logger.exception(msg)
        raise DictUtilException(
            'to_box error',
            f'{msg}: {dict_data}',
        ) from e

    return ret


def is_box(value):
    """
    Box型か判定

    value: obj
      判定したいオブジェクト

    return: bool
      True: Box型、False： それ以外の方
    """
    return isinstance(value, Box)
