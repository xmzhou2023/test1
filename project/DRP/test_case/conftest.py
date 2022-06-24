import os , sys, pytest, logging
from public.data.unified_login.unified import *
from libs.common.assert_ui import DomAssert, SQLAssert
from public.libs.unified_login.login import Login
from libs.common.read_config import ini

@pytest.fixture(scope='session',autouse=True)
def test_login(drivers):
    """登录用户"""
    logging.info("前置条件：传音统一登录开始")
    user = Login(drivers)
    user.login(drivers, account[0]['usernum'], account[0]['passwd'])
    user = DomAssert(drivers)
    user.assert_url("{}/dashboard".format(ini.url))
    user = SQLAssert(drivers)
    user.assert_sql(word=account[0]['username'], sql='select name_zh from uc_user where enable_flag=1')
    logging.info("前置条件：传音统一登录成功")