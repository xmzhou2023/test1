import pytest, logging
from public.data.unified_login.unified import *
from public.base.assert_ui import *
from public.libs.unified_login.login import Login
from libs.common.read_config import *

pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture(scope='session',autouse=True)
def __init__(drivers, env_name):
    """初始化"""
    global pro_env
    pro_env = env_name
    logging.info("【{}】项目【{}】环境- UI自动化开始执行".format(pro_name, pro_env))
    ini = ReadConfig(pro_name, pro_env)

    """使用统一登录"""
    logging.info("前置条件：传音统一登录开始")
    user = Login(drivers)
    user.login(drivers, ini.url, account[2]['usernum'], account[2]['passwd'])
    DomAssert(drivers).assert_exact_att('首页')
    logging.info("前置条件：传音统一登录成功")

