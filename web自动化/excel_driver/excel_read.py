#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/21 23:56

# @Author : Lelsey

import openpyxl


def read(file, log):
    excel = openpyxl.load_workbook(file)
    sheets = excel.sheetnames
    for sheet in sheets:
        # 循环每个sheet页
        for values in excel[sheet].values:
            # 判断第一个单元格不是数字编号
            if values[2] is not None:
                data = {}
                # 字符串内容的切割，先切割分号，区分多组参数
                str_temp = values[2].split(';')
                for temp in str_temp:
                    temp = temp.split('=', 1)
                    data[temp[0]] = temp[1]
            else:
                data = None
