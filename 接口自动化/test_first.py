#!/usr/bin/env python

# coding: utf-8 

# @Time : 2023/10/9 22:57

# @Author : xumenghan

import pytest

def test_1():
    print("测试")
    print("测试github修改内容后上传")

if __name__ == '__main__':
    pytest.main(["-s", "test_first.py"])
