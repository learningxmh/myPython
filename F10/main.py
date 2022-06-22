#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/6/6 21:58

# @Author : xumenghan
'''
    程序主入口：
    1、调用excel读取执行用例
    2、读取指定路径吓得所有excel测试用例
    3、初始化日志和关键类

'''
import os

from F10.common import excel_read
from F10.conf import read_log

if __name__ == '__main__':
    log = read_log.get_conf('conf/log.ini')
    cases = []
    # 获取指定路径下的所有测试用例：用例集中在data/的路径下
    for path, dir, files in os.walk('./data'):
        # 保存获取的所有测试用例文件
        for file in files:
            # 获取文件后缀名
            file_type = os.path.splitext(file)[1]
            if file_type == '.xlsx':
                cases.append(path + '/' + file)
            else:
                log.info('文件类型错误：{}'.format(file))
    #运行测试用例
    for case in cases:
        log.info('正在运行测试用例：{}'.format(case))
        excel_read.read(case, log)
