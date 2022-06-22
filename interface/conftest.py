#!/usr/bin/env python

# coding: utf-8 

# @Time : 2022/6/12 20:51

# @Author : xumenghan

import pytest

from interface.common.yaml_utils import clean_yaml


@pytest.fixture(scope='session',autouse=True)
def clear_token():
    clean_yaml()