#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2024 sakito <sakito@sakito.com>
"""
日時関連処理
"""
from datetime import datetime, timezone, timedelta

import pytz
import dateutil.parser
from dateutil.relativedelta import relativedelta


class DatetimeError(RuntimeError):
    """
    datetime_util エラークラス
    """


# デフォルトタイムゾーン
TIMEZONE = 'Asia/Tokyo'

# 日時フォーマット
FORMAT = {
    'ymdThms': '%y-%m-%d%%H:%M:%S',
    'ymdhms': '%Y%m%d%H%M%S',
    'iso': '%Y-%m-%dT%H:%M:%S.%f',
}

def get_now(str_flag=True, time_zone=None):
    """
    現在時刻取得

    str_flag: 文字列変換フラグ True: 文字列、False: datetime
    """
    now = datetime.now()

    return to_ymdhms(now, str_flag, time_zone)


def get_tz(time_zone=None):
    """
    タイムゾーン取得

    time_zone: str タイムゾーン文字列
    """
    if time_zone is None or time_zone == '':
        # 空の場合
        time_zone = TIMEZONE

    tz = pytz.timezone(time_zone)

    return tz

def to_ymdhms(date, str_flag=True, time_zone=None):
    """
    datetime or str -> str(yyyymmddhhMMss)

    date: datetime or str
      dateutil で解釈可能な日時文字列
      datetime オブジェクト

    return: str or datetime フォーマットを変換した文字列
    """
    if not date:
        # None、空の場合はそのまま返す
        return date

    if isinstance(date, str):
        date = dateutil.parser.parse(date)

    date = date.replace(tzinfo=get_tz(time_zone))
    date = date.astimezone()

    if str_flag:
        return f'{date:%Y%m%d%H%M%S}'

    return date
