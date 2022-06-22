#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/26 19:25

# @Author : Lelsey
from selenium import webdriver

from F10.common.utils import BasePage
from F10.conf import read_log


class HkPub(BasePage):
    '''
    港股PC公告
    '''
    url = "https://basic.10jqka.com.cn/HK1810/pub.html"
    # 公告列表
    pub_list = ("id", "data_list_insert_notice")
    # 公告上一页
    pub_sub = ("xpath", "//div[@id='notice']/div/div/a[text()='上一页']")
    # 公告下一页
    pub_next = ("xpath", "//div[@id='notice']/div/div/a[text()='下一页']")
    # 当前页的所有公告日期
    pub_dates = ("xpath", "//div[@id='data_list_insert_notice']/dl/dt/span[@class='date']")
    # 当前页的所有公告标题
    pub_titles = ("xpath", "//div[@id='data_list_insert_notice']/dl/dt/span[@class='title']")

    # 新闻列表
    new_list = ("id", "data_list_insert_mine")
    # 新闻上一页
    new_sub = ("xpath", "//div[@id='mine']/div/div/a[text()='上一页']")
    # 新闻下一页
    new_next = ("xpath", "//div[@id='mine']/div/div/a[text()='下一页']")
    # 当前页的所有新闻标题
    new_titles = ("xpath", "//div[@id='data_list_insert_mine']/dl/dt/span[@class='date']")
    # 当前页的所有新闻日期
    new_dates = ("xpath", "//div[@id='data_list_insert_mine']/dl/dt/span[@class='title']")

    # 页面底部
    footer = ("class name", "footer")

    # 免责声明
    declimaer = ("xpath", "//p[@sc-mode='hide']")



