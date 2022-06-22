#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/6/16 16:54

# @Author : xumenghan
import os

import pytest

from F10.common.request_utils import RequestUtils
from F10.common.yaml_util import read_yaml


class TestStockMainDefault:

    @pytest.mark.parametrize("args_name", read_yaml("stock_id.yaml"))
    def test_01_stock_id(self, args_name):
        res = RequestUtils().send_request(method=args_name['request']['method'], url=args_name['request']['url'],
                                          headers=args_name['request']['headers'], data=args_name['data'])
        RequestUtils().vilivated_assert(args_name['vilacited']['status_code'], res.json()['status_code'])

    @pytest.mark.parametrize("args_name", read_yaml("stock_code.yaml"))
    def test_02_stock_code(self, args_name):
        res = RequestUtils().send_request(method=args_name['request']['method'], url=args_name['request']['url'],
                                          headers=args_name['request']['headers'], data=args_name['data'])
        RequestUtils().vilivated_assert(args_name['vilacited']['status_code'], res.json()['status_code'])

    @pytest.mark.parametrize("args_name", read_yaml("stock_market.yaml"))
    def test_03_stock_market(self, args_name):
        res = RequestUtils().send_request(method=args_name['request']['method'], url=args_name['request']['url'],
                                          headers=args_name['request']['headers'], data=args_name['data'])
        RequestUtils().vilivated_assert(args_name['vilacited']['status_code'], res.json()['status_code'])

    @pytest.mark.parametrize("args_name", read_yaml("stock_recommend.yaml"))
    def test_04_stock_recommend(self, args_name):
        res = RequestUtils().send_request(method=args_name['request']['method'], url=args_name['request']['url'],
                                          headers=args_name['request']['headers'], data=args_name['data'])
        RequestUtils().vilivated_assert(args_name['vilacited']['status_code'], res.json()['status_code'])

    @pytest.mark.parametrize("args_name", read_yaml("stock_type.yaml"))
    def test_05_stock_type(self, args_name):
        res = RequestUtils().send_request(method=args_name['request']['method'], url=args_name['request']['url'],
                                          headers=args_name['request']['headers'], data=args_name['data'])
        RequestUtils().vilivated_assert(args_name['vilacited']['status_code'], res.json()['status_code'])
