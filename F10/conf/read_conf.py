#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/6/15 15:01

# @Author : xumenghan

import configparser


# 读取配置文件中的内容

def ReadConf(path, section, option):
    conf = configparser.ConfigParser()
    conf.read(path)
    value = conf.get(section, option)
    return value


if __name__ == '__main__':
    value = ReadConf('./config.ini', "TEST_SERVER", "url")
    print(value)
