#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2024 sakito <sakito@sakito.com>
"""
ログ関連
"""

import logging.config
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


class LoggingUtil:
    """
    ログ設定クラス
    """

    def __init__(self):
        """
        設定ファイル読み込み
        """
        pwd = (Path(__file__).parent).absolute()
        LOGGING_CONF = pwd / 'logging.config.toml'

        with open(LOGGING_CONF, mode='rb') as f:
            conf = tomllib.load(f)

        # ログ出力位置を絶対パスに変換
        for key in conf['handlers'].keys():
            if 'filename' in conf['handlers'][key]:
                conf['handlers'][key]['filename'] = pwd / conf['handlers'][key]['filename']

        logging.config.dictConfig(conf)

    def get_logger(self, name='tool'):
        """
        logger オブジェクト取得

        name: str ログ名

        return: logging ログオブジェクト
        """
        return logging.getLogger(name)


logger = LoggingUtil().get_logger()
