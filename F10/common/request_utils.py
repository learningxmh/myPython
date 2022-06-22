#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/6/16 16:58

# @Author : xumenghan
import json

import requests


class RequestUtils:
    sess = requests.session()

    def send_request(self, method, url, data=None, **kwargs):
        method = str(method).lower()
        if method == 'get':
            res = RequestUtils.sess.request(method=method, url=url, params=data, **kwargs)
        elif method == 'post':
            if data:  # 如果数据不为空，将字典格式数据转换成json格式
                data = json.dumps(data)
            res = RequestUtils.sess.request(method=method, url=url, data=data, **kwargs)
        else:
            pass
        return res

    def vilivated_assert(self, excepted, reality):
        try:
            assert excepted == reality, '{0}与{1}不相等'.format(excepted, reality)
            return True
        except Exception as e:
            print('出现异常，断言失败，预期与实际结果不符合：{}'.format(e))
            return False
