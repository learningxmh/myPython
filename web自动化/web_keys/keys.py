#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/21 22:47

# @Author : Lelsey


from selenium import webdriver


# 不同浏览器生成
def open_brower(type_):
    # 基于反射机制
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class Key:
    def __init__(self, type_):
        self.driver = open_brower(type_)
        self.driver.implicitly_wait(10)
