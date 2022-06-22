#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/4/16 16:31

# @Author : Lelsey
import requests
import re

url = 'https://movie.douban.com/chart'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

r = requests.get(url=url, headers=header)
page = r.text
imgs = re.findall(r'data-original="(.*?)"', page)
print(f'开始下图片,总共{len(imgs)}张')
for i, j in enumerate(imgs):
    print(f'正在下载第{i+1}张图片')
    with open(f'./imgs/{i+1}.jpeg', 'wb') as f:
        r = requests.get(url=j, headers=header)
        f.write(r.content)
else:
    print("下载完成")
