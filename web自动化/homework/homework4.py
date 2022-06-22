#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/17 19:18

# @Author : Lelsey

# 登录-搜索商品-添加商品属性-加入购物车-校验购物车是否添加成功

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://39.98.138.157/shopxo/index.php")

# 点击登录
driver.find_element("xpath", "//a[text()='登录']").click()
# 输入用户名
driver.find_element("xpath", "//input[@name='accounts']").send_keys("dzce_001")
# 输入密码
driver.find_element("xpath", "//input[@name='pwd']").send_keys("123456")
# 点击登录
driver.find_element("xpath", "//button[text()='登录']").click()
sleep(2)
# 搜索商品
driver.find_element("id", "search-input").send_keys("连衣裙")
# 点击搜索
driver.find_element("id", "ai-topsearch").click()
sleep(2)
# 获取所有句柄
handles = driver.window_handles
print(handles)
# 点击第一个连衣裙
driver.find_element("xpath", "//a[@class='am-block']").click()
sleep(5)
now_handles = driver.window_handles
print(now_handles)
# 切换句柄
driver.switch_to.window(now_handles[1])
sleep(1)
now_handle = driver.current_window_handle
print(now_handle)
# 点击勾选颜色
driver.find_element("xpath", "//li[@data-value='粉色']").click()
# 点击选择尺码
driver.find_element("xpath", "//li[@data-value='S']").click()
# 点击加入购物车
driver.find_element("xpath", "//button[@title='加入购物车']").click()
sleep(1)
# 点击购物车
driver.find_element("xpath", "//span[text()='购物车']/..").click()
sleep(5)
driver.quit()
