#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/22 0:02

# @Author : Lelsey

"""程序主入口
    1、调用excel读取执行测试用例
    2、读取指定路径下所有的excel测试用例
    3、初始化日志器和关键类


"""
import os

from web自动化.conf import log_conf
from web自动化.excel_driver import excel_read

if __name__ == '__main__':
    log = log_conf.get_log('conf/log.ini')
    # 定义测试用例list
    cases = []
    # 获取指定路径下的所有测试用例：用例集中在test_data目录下
    for path, dir, files in os.walk('./test_data'):
        # 保存获取的所有测试用例文件：其实就是后缀名为.xlsx
        for file in files:
            # 获取文件后缀名
            file_type = os.path.splitext(file)[1]
            # 判断文件是否为excel
            if file_type == '.xlsx':
                cases.append(path + '/' + file)
            else:
                log.info('文件类型错误：{}'.format(file))
    # 调用excel_driver中的run函数，运行测试用例
    for case in cases:
        excel_read.run(case, log)
