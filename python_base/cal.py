#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/4/14 13:06

# @Author : Lelsey

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}*{i}={i*j:2}', end=' ')
    print('')
