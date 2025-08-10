#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2024 sakito <sakito@sakito.com>
"""
日時関連処理
"""

from datetime import datetime, timedelta, timezone

import dateutil.parser
import pytz
from dateutil.relativedelta import relativedelta


class DatetimeError(RuntimeError):
    """
    datetime_util エラークラス
    """


# デフォルトタイムゾーン
TIMEZONE = 'Asia/Tokyo'


def get_now(str_flag=True, time_zone=None):
    """
    現在時刻取得

    str_flag: 文字列変換フラグ True: 文字列、False: datetime
    """
    now = datetime.now()

    # time zone適用
    date = replace_time_zone(now, time_zone)

    if str_flag:
        return f'{date:%Y%m%d%H%M%S}'

    return date


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


def replace_time_zone(date, time_zone=None):
    """
    time zone の適用

    date: datetime or str
      dateutil で解釈可能な日時文字列
      datetime オブジェクト

    return: datetime time zone適用値
    """
    if not date:
        # None、空の場合はそのまま返す
        return date

    if isinstance(date, str):
        date = dateutil.parser.parse(date)

    date = date.replace(tzinfo=get_tz(time_zone))
    if time_zone:
        date = date.astimezone()

    return date


def add_time(target, month=0, second=0):
    """
    加算

    target datetime: 加算対象

    month int: 加算減算したい「月」(マイナスに対応)
    second int: 加算減算したい「秒」(マイナスに対応)
    """
    return target + relativedelta(months=month, seconds=second)


def to_isoformat(date, time_zone=None) -> str:
    """
    日時関連を ISO 8601 形式「文字列」に変換
    """
    if not date:
        # 空の場合はそのまま返す
        return date

    date = replace_time_zone(date, time_zone)

    return f'{date:%Y-%m-%dT%H:%M:%S.%f%z}'


def format_timedelta(target: timedelta) -> str:
    """
    時刻差分をフォーマット
    """
    total_sec = target.total_seconds()

    hours = total_sec // 3600

    total_sec = total_sec - (hours * 3600)
    minutes = total_sec // 60
    seconds = total_sec - (minutes * 60)

    result = f'{int(hours):02}:{int(minutes):02}:{int(seconds):02}'

    return result


def utcmsec_to_dt(target, jst=False):
    """
    UTC microseconds を datetime に変換

    target: str or float
      0001/1/1 からの経過時刻
    jst: bool
      True: JSTで返す、False: GMTで返す
    """
    if isinstance(target, str):
        # target が str の場合 float に変換
        target = float(target)
    dt = datetime.utcfromtimestamp(target / 1000000.0)
    if jst:
        jst = timezone(timedelta(hours=+9), 'JST')
        dt = dt.replace(tzinfo=timezone.utc).astimezone(tz=jst)

    return dt
