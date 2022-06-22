#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/9 20:18

# @Author : Lelsey

from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.maximize_window()  #浏览器最大化

driver.get("https://www.baidu.com")
time.sleep(5)