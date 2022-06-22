#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/10 16:30

# @Author : Lelsey
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://music.163.com/#/discover/toplist")
driver.implicitly_wait(10)

f = driver.find_element('id', 'g_iframe')
driver.switch_to.frame(f)
music = driver.find_elements('xpath','//div[@class="tt"]/span')
driver.execute_script('arguments[0].scrollIntoView();',music[70])
sleep(1)
music[70].click()