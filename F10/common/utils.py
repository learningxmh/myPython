#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/26 19:08

# @Author : Lelsey
import HTMLTestRunner
import os
import time
from selenium import webdriver
from time import sleep
from F10.conf.chrome_options import Options


def open_browser(type_):
    '''
    :param
    :param type_: 浏览器类型，如Chrome
    :return: driver
    '''
    if type_ == 'Chrome':
        driver = webdriver.Chrome(options=Options().brow_options())
    else:
        try:
            driver = getattr(webdriver, type_)()
        except Exception as e:
            driver = webdriver.Chrome()
    return driver


class BasePage:
    def __init__(self, type_, log):
        self.driver = open_browser(type_)
        self.driver.implicitly_wait(10)
        self.log = log

    def find(self, by, value):
        '''
        :param by: 查找单个元素，输入后面小写的
        ID ：id
        NAME：name
        CLASS_NAME：class name
        LINK_TEXT：link text
        PATRIAL_LINK_TEXT：patrial link text
        TAG_NAME：tag name
        CSS_SELECTOR：css selector
        XPATH：xpath
        :param value: 定位元素
        :return:
        '''
        try:
            return self.driver.find_element(by, value)
        except Exception:
            return None

    def finds(self, by, value):
        '''
        :param by: 查找多个元素，输入后面小写的
        ID ：id
        NAME：name
        CLASS_NAME：class name
        LINK_TEXT：link text
        PATRIAL_LINK_TEXT：patrial link text
        TAG_NAME：tag name
        CSS_SELECTOR：css selector
        XPATH：xpath
        :param value: 定位元素
        :return:
        '''
        try:
            return self.driver.find_elements(by, value)
        except Exception:
            return None

    def open(self, url):
        '''

        :param url: 访问url地址
        :return:
        '''
        self.driver.get(url)

    def click(self, by, value):
        '''
        点击操作
        :param by:
        :param value:
        :return:
        '''
        self.find(by, value).click()

    def wait(self, time):
        '''
        强制等待
        :param time:
        :return:
        '''
        sleep(time)

    def input(self, by, value, txt):
        '''
        输入框输入文本
        :param by:
        :param value:
        :param txt: 要输入的文本内容
        :return:
        '''
        self.find(by, value).send_keys(txt)

    def quit(self):
        '''
        退出浏览器
        :return:
        '''
        self.driver.quit()

    def scrollto(self, by, value):
        '''
        使得查找到的元素显示在视图中，适用于有滚动条的页面
        :param by:
        :param value:
        :return:
        '''
        el = self.find(by, value)
        js = "arguments[0].scrollIntoView()"
        self.driver.execute_script(js, el)

    def assume_text(self, by, value):
        self.log.info("当前正在执行校验文本是否有异常字符")
        try:
            text = self.find(by, value).text
            error_text = ('NaN', 'INF', 'null', 'undefined', 'false')
            if text is not None:
                assert (text not in error_text)
                return True
            else:
                self.log.info("当前文本为空")
                return False
        except Exception as e:
            self.log.exception('出现异常，断言失败'.format(e))
            return False

    def switch_handle(self, status=1):
        # 句柄的切换：为了满足有些场景下不需要close，需要考虑逻辑的处理
        handles = self.driver.window_handles
        if status == 1:
            self.driver.close()
        self.driver.switch_to.window(handles[1])

    def assert_almost_equal(self, by, value, excepted):
        try:
            reality = self.find(by, value).text
            assert excepted in reality, '{0}不在{1}的范围内'.format(excepted, reality)
            return True
        except Exception as e:
            self.log.exception('出现异常，断言失败，实际结果与预期不符合：{}'.format(e))
            return False

    def assert_equal(self, by, value, excepted):
        try:
            reality = self.find(by, value).text
            assert excepted == reality, '{0}与{1}不相等'.format(excepted, reality)
            return True
        except Exception as e:
            self.log.exception('出现异常，断言失败，实际结果与预期不符合：{}'.format(e))
            return False

    def time_strft(self):
        return time.strftime("%Y-%m-%d", time.localtime())


