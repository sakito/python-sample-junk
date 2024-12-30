#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2024 sakito <sakito@sakito.com>
import logging_util as t


def test_logger():
    """
    logger
    """
    t.logger.debug('DEBUG テスト')
    t.logger.info('INFO テスト')
    t.logger.warning('WAARNING テスト')
    t.logger.error('ERROR テスト')
    t.logger.critical('CRITICAL テスト')
