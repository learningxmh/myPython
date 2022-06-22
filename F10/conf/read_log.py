#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/26 19:04

# @Author : Lelsey
import logging
import logging.config


def get_conf(path):
    # 日志生成器
    logging.config.fileConfig(path)
    return logging.getLogger()
