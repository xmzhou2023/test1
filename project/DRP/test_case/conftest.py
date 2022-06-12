#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:huangqin
# @time:2022/5/31 19:17
import pytest, sys
from public.data.unified_login.unified import *
from libs.common.assert_ui import DomAssert, SQLAssert
from public.libs.unified_login.login import Login
from project.DRP.page_object.nav import NavPage
from project.DRP.page_object.user import UserPage
from libs.common.read_config import ini
from libs.common.logger_ui import log

@pytest.fixture(scope='session', autouse=True)
def test_login(drivers):
    """登录用户"""
    print('所有用例执行只执行一遍')
    user = Login(drivers)
    user.login(drivers, account[0]['usernum'], account[0]['passwd'])
    user = DomAssert(drivers)
    user.assert_url("{}/dashboard".format(ini.url))
    user = SQLAssert(drivers)
    user.assert_sql(word=account[0]['username'], sql='select name_zh from uc_user where enable_flag=1')
    print('登录成功')

# @pytest.fixture(scope='function', autouse=True)
# def dec_name(f):
#     name = f.__name__
#     def new_f(*a, **ka):
#         return f(*a, __name__=name, **ka)
#     log.info("{} is start".format(name))
#     return new_f
# @dec_name
# def fun_name(x, __name__):
#     print(__name__)
# z = fun_name
# z(1)
if __name__ == '__main__':
    pytest.main()
