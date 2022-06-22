#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/6/12 20:31

# @Author : xumenghan
import os
import yaml


def read_yaml(key):
    with open(os.getcwd() + '/data.yaml', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


def write_yaml(data):
    with open(os.getcwd() + '/data.yaml', encoding='utf-8', mode='a') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


def clean_yaml():
    with open(os.getcwd() + '/data.yaml', encoding='utf-8', mode='w') as f:
        f.truncate()  # 清空


def read_testcase(yaml_name):
    with open(os.getcwd() + "/" + yaml_name, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value
