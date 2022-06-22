#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/6/11 21:45

# @Author : xumenghan
import os

from F10.common.unitest_report import Report
import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    testcases = unittest.defaultTestLoader.discover(start_dir=os.getcwd()+'/case', pattern='test*.py')
    suite.addTests(testcases)
    Report().unnittest_report_runner().run(suite)