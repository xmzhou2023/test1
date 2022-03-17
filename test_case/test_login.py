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


class TestLogin:
    @pytest.fixture(scope='function', autouse=True)
    def login(self, drivers):
        """打开登录页"""
        user = LoginPage(drivers)
        user.get_url(ini.url)
        user.click_accountlogin()
        user.input_account('18650617')
        user.input_passwd('jf3249JFL')
        if user.check_box() == False:
            user.click_checkbox()
        user.click_loginsubmit()
        user.click_loginsubmit()

    def test_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "用户管理")
        user.click_gotonav("系统管理", "区域管理")
        user.click_gotonav("系统管理", "维度管理")
        # time.sleep(10)
        # menu = drivers.find_element('xpath', '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span')
        # hidden_submenu = drivers.find_element('xpath', '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span')
        # log.info(menu)
        # log.info(hidden_submenu)
        #
        # actions = ActionChains(drivers)
        # actions.move_to_element(menu).perform()
        # drivers.find_element('xpath', '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div/span')
        # sleep(10)

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
