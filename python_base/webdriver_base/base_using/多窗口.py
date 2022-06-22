#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/10 12:49

# @Author : Lelsey

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
driver.implicitly_wait(10)
print(driver.title)
now_handle = driver.current_window_handle
driver.find_element('link text', 'hao123').click()
handles = driver.window_handles
for i in handles:
    if i != now_handle:
        driver.switch_to.window(i)
        print(driver.title)

driver.close()
driver.switch_to.window(now_handle)
print(driver.title)
