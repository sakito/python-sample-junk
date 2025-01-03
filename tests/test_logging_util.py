#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2024 sakito <sakito@sakito.com>
import logging_util as t


def test_logger():
    """
    logger
    """
    logger = t.LoggingUtil().get_logger('debug')
    logger.debug('DEBUG テスト')
    logger.info('INFO テスト')
    logger.warning('WARNING テスト')
    logger.error('ERROR テスト')
    logger.critical('CRITICAL テスト')
