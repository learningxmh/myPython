#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/17 18:18

# @Author : Lelsey
from selenium import webdriver
from time import sleep

url = "http://39.98.138.157/shopxo/index.php"

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(url)


# 获取当前handle
now_handle = driver.current_window_handle
print(now_handle)
# 点击注册按钮
driver.find_element("xpath", "//a[text()='注册']").click()
# 获取所有handles
handles = driver.window_handles
print(handles)
# 输入用户名
driver.find_element("name", "accounts").send_keys("dzce_001")
# 输入密码
driver.find_element("name", "pwd").send_keys("123456")
# 勾选协议
driver.find_element("xpath", "//input[@name='is_agree_agreement']/../span").click()
# 点击注册
driver.find_element("xpath", "//button[text()='注册']").click()
sleep(5)
driver.quit()
