#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/16 23:55

# @Author : Lelsey

from selenium import webdriver
from time import sleep

url = "http://music.163.com"
driver = webdriver.Chrome()
driver.maximize_window()
# 访问网易云音乐
driver.get(url)
driver.implicitly_wait(5)
# 切换入iframe
driver.switch_to.frame("g_iframe")
# 点击登录
driver.find_element("id", "index-enter-default").click()
sleep(2)
# 切换到最外层框架
driver.switch_to.default_content()
# 点击选择其他登录模式
driver.find_element("xpath", "//a[text()='选择其他登录模式']").click()
sleep(1)
# 勾选协议
driver.find_element("id", "j-official-terms").click()
# 点击QQ登录
driver.find_element("link text", "QQ登录").click()
sleep(5)
# 获取所有句柄
handles = driver.window_handles
# 切换句柄
driver.switch_to.window(handles[1])
sleep(3)
driver.switch_to.frame("ptlogin_iframe")
# 点击qq头像
driver.find_element("id", "img_out_1132600697").click()
sleep(5)
driver.quit()
