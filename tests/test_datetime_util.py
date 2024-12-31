#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2024 sakito <sakito@sakito.com>
import datetime

import datetime_util as t


def test_get_now():
    """
    get_now
    """
    assert isinstance(t.get_now(), str)
    assert isinstance(t.get_now(False), datetime.datetime)

    target = '2024-05-25 17:28:50'
    # +9
    t1 = t.replace_time_zone(target)
    # -6(夏時間実施してないアメリカ地域を指定)
    t2 = t.replace_time_zone(target, time_zone='America/Guatemala')

    assert '-16:39:00' == t.format_timedelta(t1 - t2)
    assert '15:21:00' == t.format_timedelta(t2 - t1)


def test_to_isoformat():
    """
    to_isoformat
    """
    target = '2024-05-25 17:28:50'
    t1 = t.replace_time_zone(target)

    assert '2024-05-25T17:28:50.000000+0919' == t.to_isoformat(t1)
    assert '2024-07-25T17:28:50.000000+0919' == t.to_isoformat(t.add_time(t1, month=2))
