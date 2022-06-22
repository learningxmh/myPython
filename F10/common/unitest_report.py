#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/6/11 21:40

# @Author : xumenghan
import os
import time
from HTMLTestRunner import HTMLTestRunner


class Report:
    def unnittest_report_runner(self):
        nowtime = time.strftime("%Y-%m-%d", time.localtime())
        name = open(os.getcwd()+'/report/' + nowtime + "_report.html", "wb")
        runner = HTMLTestRunner(stream=name, verbosity=2, title="自动化测试报告", description="报告详情如下")
        return runner
