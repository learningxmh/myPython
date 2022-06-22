#!/usr/bin/env python

# -*- coding: utf-8 -*-

# @Time : 2022/4/11 15:04

# @Author : Lelsey
import unittest
from ddt import ddt, file_data


@ddt
class Case(unittest.TestCase):
    @file_data('../data/data.yaml')
    def test_01(self, **kwargs):
        common = kwargs['common']

