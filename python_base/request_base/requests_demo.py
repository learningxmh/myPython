#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/4/16 14:29

# @Author : Lelsey

import requests
import re

url = 'https://movie.douban.com/chart'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

r = requests.get(url=url, headers=header)
# r.text，以字符串返回页面源码
# r.content，以字节返回页面源码
# r.json()，以json格式返回服务端的响应
page = r.text
print(page)
