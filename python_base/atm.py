#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/4/15 15:49

# @Author : Lelsey
import os


def get_dirstory(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            return os.listdir(path)
        else:
            print(f'{path}不是目录')
    else:
        print(f'{path}不存在')
    return False


def read_file(path, encoding='utf8'):
    if os.path.exists(path) and os.path.isfile(path):
        with open(file=path, mode='r', encoding=encoding) as f:
            return f.readlines()
    else:
        print(f'{path}不存在')
    return False


def is_continue():
    return True


def login(userinfo, path):
    flag1, flag2 = True, True
    while flag1:
        username = input("请输入用户名")
        if username in userinfo:
            error = 0
            file_path = f'{path}/{username}'
            info = read_file(file_path)
            while flag2:
                password = input("请输入密码")
                if password == info[0].strip():
                    print("登录成功")
                else:
                    error += 1
                    if error >= 3:
                        print("密码错误超过3次,结束")
                        flag1, flag2 = False, False
                    else:
                        print("密码错误，请重新输入")
                        flag2 = is_continue()
                        flag1 = flag2

        else:
            print("用户名不存在")


def register():
    username = input("请输入用户名")
    password = input("请输入密码")


if __name__ == '__main__':
    path = './user'
    users = get_dirstory(path)
    print(users)
