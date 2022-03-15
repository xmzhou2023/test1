#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:huangqin
# @time:2022/3/10 15:24

import pytest
from selenium import webdriver
from base_object.login_page import TestLoginPage
from base_object.index_page import TestIndexPage
from ddt import ddt, file_data

@ddt
class TestCase():
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

        # cls.driver = TestLoginPage.initial_driver()
        cls.lp = TestLoginPage()
        # cls.ip = TestIndexPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @file_data('../data/DRP/user.yaml')
    def test_1_login(self, username, passwd, ttt):
        tet = self.lp.login(username, passwd)
        assert tet == ttt

    # @pytest.mark.parametrize('txt', ('衣服', '手机'))
    # def test_2_login(self, txt):
    #     self.ip.search(txt)

if __name__ == '__main__':
    pytest.main(['test_case/testcase_for_search.py'])

