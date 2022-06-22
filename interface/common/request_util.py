#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/6/12 21:13

# @Author : xumenghan
import json

import requests


class RequestUtil:
    # 全局变量，通过类名调用
    sess = requests.session()

    def send_request(self, method, url, data=None, **kwargs):
        method = str(method).lower()
        if method == "get":
            res = RequestUtil.sess.request(method=method, url=url, params=data, **kwargs)

        elif method == "post":
            if data:
                data = json.dumps(data)
            res = RequestUtil.sess.request(method=method, url=url, data=data, **kwargs)
        else:
            pass
        return res
