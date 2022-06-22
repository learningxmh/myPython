#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/6/16 16:47

# @Author : xumenghan
import os

import yaml


def read_yaml(path):
    with open(os.getcwd()+"/data/"+path, mode='r', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value


def write_yaml(path, data):
    with open(os.getcwd()+"/data/"+path, mode='a', encoding='utf-8') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


def clean_yaml(path):
    with open(os.getcwd()+"/data/"+path, mode="w", encoding='utf-8') as f:
        f.truncate()


