#!/usr/bin/env python

# coding: utf-8

# @Time : 2022/5/30 20:34

# @Author : Lelsey
import os
import unittest
from F10.conf import read_log
from F10.page.F10_hk.F10_hk_pub import HkPub
from F10.common import excel_read


class PcHkPub(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.log = read_log.get_conf(os.getcwd() + '/conf/log.ini')
        cls.hp = HkPub('Chrome', cls.log)
        cls.hp.open(cls.hp.url)

    def test_01_pub_list(self):
        excel_read.read(os.getcwd() + '/data/pc_hk_pub.xlsx', self.log)
        # self.hp.assume_text(*self.hp.pub_list)
        # self.hp.assert_almost_equal(*self.hp.pub_list, "报表")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.hp.quit()
