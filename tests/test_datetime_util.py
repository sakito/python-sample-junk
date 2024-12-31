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

    # +9
    t1 = t.get_now(False)
    # -6
    t2 = t.get_now(False, time_zone='America/Chicago')
