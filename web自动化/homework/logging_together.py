#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/18 17:56

# @Author : Lelsey

import logging

# 创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # 默认总开关

logfile = './log.txt'
fh = logging.FileHandler(logfile, mode='a')  # 输出到文件
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()  # 输出到控制台
ch.setLevel(logging.WARNING)

# 定义handle 格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s : %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('这是 debug message')
logger.info('这是 info message')
logger.warning('这是 warning message')
logger.error('这是 error message')
logger.critical('这是 critical message')
