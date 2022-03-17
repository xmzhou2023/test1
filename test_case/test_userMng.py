#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:huangqin
# @time:2022/3/16 14:51
import re
import time

import pytest
from tools.loggerUI import log
from common.readconfig import ini
# from page_object.searchpage import SearchPage
from page_object.loginpage import LoginPage
from page_base.webpage import WebPage
from page_object.userManage import UserMngPage
class TestLogin():
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

        user.get_url('http://10.250.112.166:9000/#/systemManage/userManage')
        time.sleep(10)

    def test_001(self, drivers):
        log.info('1111')
        # pass
        userMng = UserMngPage(drivers)
        userMng.input_account('18650617')
        userMng.click_query()
        #
        time.sleep(10)


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
    pytest.main(['test_case/test_.py'])
