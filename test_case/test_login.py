#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import time

import pytest
from tools.loggerUI import log
from common.readconfig import ini
from page_object.searchpage import SearchPage
from page_object.loginpage import LoginPage
from page_object.nav import NavPage
from page_object.user import UserPage
from time import sleep


class TestLogin:


    def test_001(self, drivers):
        """前往菜单"""
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "用户管理")
        sleep(3)
        # user = UserPage(drivers)
        user.input_account('18650617')

# class TestSearch:
#     @pytest.fixture(scope='function', autouse=True)
#     def login(self, drivers):
#         """打开百度"""
#         search = SearchPage(drivers)
#         search.get_url(ini.url)
#         search.click_search()

# def test_001(self, drivers):
#     """搜索"""
#     search = SearchPage(drivers)
#     search.input_search("selenium")
#     search.click_search()
#     result = re.search(r'selenium', search.get_source)
#     log.info(result)
#     assert result
#
# def test_002(self, drivers):
#     """测试搜索候选"""
#     search = SearchPage(drivers)
#     search.input_search("selenium")
#     log.info(list(search.imagine))
#     assert all(["selenium" in i for i in search.imagine])


if __name__ == '__main__':
    pytest.main(['test_case/test_search.py'])
