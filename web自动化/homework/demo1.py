#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/5/19 16:09

# @Author : Lelsey

from time import sleep, ctime


def timefun(func):
    def warp_func():
        print("%s called at %s" % (func.__name__, ctime()))
        func()

    return warp_func


@timefun
def foo():
    print("it over")

foo()
sleep(2)
foo()