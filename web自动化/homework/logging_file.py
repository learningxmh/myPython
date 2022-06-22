#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/18 16:31

# @Author : Lelsey

import logging

logging.basicConfig(level=logging.WARNING,
                    filename='./log.txt',
                    filemode='a',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logging.debug('这是 debug message')
logging.info('这是 info message')
logging.warning('这是 warning message')
logging.error('这是 error message')
logging.critical('这是 critical message')
