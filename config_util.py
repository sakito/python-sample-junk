#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2024 sakito <sakito@sakito.com>
"""
設定ファイル処理

設定はtomlファイル前提
"""

from pathlib import Path


def get_prj_root():
    """
    プロジェクトルートディレクトリ取得

    return: str ディレクトリパス
    """
    prj_dir = (Path(__file__).parent / '..' / '..').absolute().resolve()

    return prj_dir


def get_conf_file(file_path='conf.toml', base_dir='conf'):
    """
    設定ファイルパス取得

    file_path: str or Path ファイル名
    base_dir: str 基準ディレクトリ名

    return: Path ディレクトリパス
    """
    conf_file_path = get_prj_root() / base_dir / file_path

    return conf_file_path
