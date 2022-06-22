#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/30 21:14

# @Author : Lelsey

import openpyxl
from F10.common.utils import BasePage

from F10.conf import read_log, excel_conf


def arguments(value):
    '''
    解析测试用例中单元格的参数，并转换为字典的形态
    :param value:
    :return: 字典
    '''
    data = dict()
    if value:
        # 字符串内容切割，先切割分号，区分多组参数
        str_temp = value.split(";")
        for temp in str_temp:
            temp = temp.split("=", 1)  # 只分割一次
            data[temp[0]] = temp[1]
    else:
        pass
    return data


def read(file,log):
    # 读取excel
    excel = openpyxl.load_workbook(file)
    try:
        # 获取sheet页
        sheets = excel.sheetnames
        # 循环每个sheet页
        for sheet in sheets:
            # 循环每一行
            for value in excel[sheet].values:
                # 判断第一个单元格是不是数字编号，是则执行步骤
                if type(value[0]) is int:
                    # 参数不为空
                    data = arguments(value[2])
                    # 运行期间的日志生成
                    log.info('当前正在执行:{}'.format(value[3]))
                    # 操作行为的执行
                    if value[1] == 'open_browser':
                        key = BasePage(data['type_'], log)
                    # 断言行为：基于断言的返回结果判定测试的成功失败，并进行写入操作
                    elif 'assert' in value[1]:
                        status = getattr(key, value[1])(excepted=value[4], **data)  # value[4]就是预期结果填的内容
                        if status:
                            excel_conf.write_result(excel[sheet].cell, row=value[0] + 2, column=6)
                        else:
                            excel_conf.write_result(excel[sheet].cell, row=value[0] + 2, column=6, status=2)
                        # 保存excel
                        excel.save(file)
                    else:
                        getattr(key, value[1])(**data)
    except Exception as e:
        log.exception('运行异常：{}'.format(e))
    finally:
        excel.close()
