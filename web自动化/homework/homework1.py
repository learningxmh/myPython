#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/16 22:14

# @Author : Lelsey

from selenium import webdriver

from time import sleep

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://39.98.138.157/shopxo/index.php")

driver.implicitly_wait(5)

driver.find_element("xpath", "//a[text()='登录']").click()

sleep(3)

username = driver.find_element("xpath", "//input[@name='accounts']")
username.send_keys("666666")
password = driver.find_element("xpath", "//input[@name='pwd']")
password.send_keys("111111")
sleep(2)
login_button = driver.find_element("xpath", "//button[text()='登录']")

login_button.click()
sleep(3)
driver.quit()
