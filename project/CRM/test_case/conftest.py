import pytest, logging
from public.data.unified_login.unified import *
from public.base.assert_ui import *
from public.libs.unified_login.login import Login
from libs.common.read_config import *
from selenium.webdriver.common.by import By
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
    if pro_env == 'test':
        user.crm_login(drivers,ini.url, account[7]['usernum'], account[7]['passwd'])
    else:
        user.crm_pro_login(drivers, ini.url, account[7]['usernum'], account[13]['passwd'])
    user = DomAssert(drivers)
    user.assert_url("{}".format(ini.url))
    logging.info("前置条件：传音统一登录成功")

    # elif pro_env == "pro_9s":
    #     logging.info("前置条件：传音统一登录开始")
    #     user = Login(drivers)
    #     user.crm_pro_9s_login(drivers, ini.url, account[7]['usernum'], account[13]['passwd'])
    #     user = DomAssert(drivers)
    #     user.assert_url("{}".format(ini.url))
    #     logging.info("前置条件：传音统一登录成功")
    #
    # else:
    #     logging.info("前置条件：传音统一登录开始")
    #     user = Login(drivers)
    #     user.crm_pro_login(drivers, ini.url, account[7]['usernum'], account[13]['passwd'])
    #     user = DomAssert(drivers)
    #     user.assert_url("{}".format(ini.url))
    #     # user.assert_exact_att('18646156')
    #     logging.info("前置条件：传音统一登录成功")
    return pro_env