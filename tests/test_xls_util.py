#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2025 sakito <sakito@sakito.com>
import xls_util as t

import config


def test_create():
    """
    create
    """
    output_dir = config.OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / 'test.xlsx'

    out_lst = [[
        'key',
        'val',
    ]]

    for idx in range(10):
        out_lst.append([f'name_{idx}', f'val_{idx}'])

    data_dict = {
        'test': out_lst,
    }

    wb = t.create(data_dict)
    t.save(wb, output_file)
