import pytest, logging
from public.data.unified_login.unified import *
from public.base.assert_ui import DomAssert, SQLAssert
from public.libs.unified_login.login import Login
from libs.common.read_config import *

pro_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).split('\\')[-1]
pro_env = 'test' # 需要手动配置测试环境
ini = ReadConfig(pro_name, pro_env)

@pytest.fixture(scope='session',autouse=True)
def test_login(drivers):
    """登录用户"""
    logging.info("前置条件：传音统一登录开始")
    user = Login(drivers)
    user.login(drivers, ini.url, account[2]['usernum'], account[2]['passwd'])
    DomAssert(drivers).assert_exact_att('首页')
    logging.info("前置条件：传音统一登录成功")

