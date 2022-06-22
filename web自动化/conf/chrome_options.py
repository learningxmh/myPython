#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/4/12 17:04

# @Author : Lelsey
from selenium import webdriver


# Chrome_options常规操作
# 1.如何在调用浏览器时候就是最大化窗体？
# 2.自动化启动时，如何驱动浏览器警告条
# 3.浏览器在启动时，如何有缓存
# 4.浏览器如何在隐身模式与常规模式切换

'''
Chrome浏览器的配置项
'''
class Options:
    def brow_options(self):
        # 创建options对象：配置浏览器的设置
        options = webdriver.ChromeOptions()
        # 页面加载策略
        options.page_load_strategy = 'eager'
        # 去掉浏览器提示自动化黄条:没什么用处，只是为了好看而已。(附加去掉控制台多余日志信息)
        options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable- logging'])
        # 窗体最大化
        # windows系统写法
        options.add_argument('start_maximized')
        # mac系统写法
        #options.add_argument('--start-fullscreen')
        # 1加载本地缓存地址
        '''
        1.windows,打开浏览器通过指令：chrome//:version查找缓存地址
        2.mac系统缓存地址：/Users/xxx/Library/Caches/Google/Chrome/Default/Cache  xxx为用户名
        3.通过传入本地缓存来实现缓存获取，参数：--user-data-dir
        4.调用本地缓存时需要关闭所有正在应用的浏览器窗体
        5。因为需要加载本地缓存，启动浏览器之后运行脚本的第一条指令会非常缓慢，如果要提速，手动输入一个请求url即可
        6.一般不推荐使用，需要绕过验证码操作的时候可以添加
        '''
        # options.add_argument(r'--user-data-dir=/Users/xxx/Library/Caches/Google/Chrome/Default/Cache')
        # 指定用户客户端-模拟手机浏览
        # options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36')
        # 添加配置去掉密码管理弹窗
        prefs = dict()
        prefs["credentials_enable_services"] = False
        prefs["profiles.password_manager_enabled"] = False
        options.add_experimental_option('prefs', prefs)
        # 无头模式：不在桌面实现浏览器的运行，作为后台静默运行，虽然看不到，但是一切照旧。
        # 偶尔场景会有异常， 但很少
        # selenium设置了headless，就会导致cmd控制台不断输出CONSOLE信息
        # options.add_argument('--headless')
        # 设置日志打印级别，小于3则不打印
        # options.add_argument('--log-level=3')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--ignore-certificate-errors')
        # 隐身模式
        # 隐身模式下无法调用selenium中的switch_to.new_window()函数
        # options.add_argument('incognito')
        # 指定窗口大小
        # options.add_argument('-windows-size=1360,920')
        # return这一步很重要。因为需要有options对象进行返回才可以对webdriver生效
        return options


if __name__ == "__main__":
    # 生成浏览器配置
    options = Options().brow_options()
    # 配置webdriver，新版本写法（python3以上）
    # 老版本写法：driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome(options=options)
    driver.get('http://baidu.com')
