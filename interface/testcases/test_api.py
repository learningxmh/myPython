#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/6/12 0:45

# @Author : xumenghan
import json
import requests
import pytest

from interface.common.request_util import RequestUtil
from interface.common.yaml_utils import write_yaml, read_yaml, read_testcase


class TestRequest:
    csrf_token = ""
    php_cookie = ""
    sess = requests.session()

    def test_01_get(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
        url = "https://basic.10jqka.com.cn/basicapi/user/finance/get/"
        data = {"id": "mobile_stock_main_default", "market": "33", "code": "300033", "recommend": "1", "type": "stock"}
        res = RequestUtil().send_request(method="get", url=url, headers=headers, data=data)
        print(res.json())

    @pytest.mark.parametrize("args_name", read_testcase("get_token.yaml"))
    def test_02_get(self, args_name):
        url = args_name['request']['url']
        data = args_name['data']
        method = args_name['request']['method']
        res = RequestUtil().send_request(method=method, url=url, data=data)
        print(res.json())
        if "access_token" in res.text:
            write_yaml({"access_token": res.json()['access_token']})

    # def test_03_post(self):
    #     url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token=" + read_yaml("access_token")
    #     data = {"tag": {"id": 134, "name": "广东人"}}
    #     res = RequestUtil().send_request(method="POST", url=url, data=data)
    #     print(res.json())
    #
    # # 文件上传
    # def test_file_upload(self):
    #     url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=" + TestRequest.access_token
    #     data = {
    #         "media": open(r"G:\myPython\interface\web.png", "rb")
    #     }
    #     res = requests.request("post", url=url, files=data)
    #     print(res.json())
    #
    # # 访问首页接口
    # def test_start(self):
    #     url = "http://47.107.116.139/phpwind/"
    #     res = requests.request(method="get", url=url)
    #     # 正则提取
    #     obj = re.search('name="csrf_token" value="(.*?)"', res.text)
    #     TestRequest.csrf_token = obj.group(1)
    #     print(TestRequest.csrf_token)
    #     TestRequest.php_cookie = res.cookies
    #
    # def test_login(self):
    #     url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
    #     headers = {
    #         "Accept": "application/json,text/javascript,/;q=0.01",
    #         "X-Requested-With": "XMLHttpRequest"
    #     }
    #     data = {
    #         "username": "msxy",
    #         "password": "msxy",
    #         "csrf_token": TestRequest.csrf_token,
    #         "backurl": "http://47.107.116.139/phpwind/",
    #         "invite": ""
    #     }
    #     res = requests.request("post", url=url, data=data, headers=headers, cookies=TestRequest.php_cookie)
    #     print(res.json())


if __name__ == '__main__':
    TestRequest().test_02_get()
    TestRequest().test_03_post()
    # TestRequest().test_file_upload()
    # TestRequest().test_start()
    # TestRequest().test_login()
