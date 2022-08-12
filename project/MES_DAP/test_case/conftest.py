import pytest, logging
from project.MES_DAP.page_object.Center_Component import *
from public.base.assert_ui import *
from libs.common.read_config import *
from project.MES_DAP.data.login import *

pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(scope='session', autouse=True)
def __init__(drivers, env_name):
    """初始化"""
    global pro_env
    pro_env = env_name
    logging.info("【{}】项目【{}】环境- UI自动化开始执行".format(pro_name, pro_env))
    ini = ReadConfig(pro_name, pro_env)

    logging.info("前置条件：MES_DAP登录开始")
    user = Login(drivers)
    user.mes_dap_login(drivers, ini.url, mes_account[0]['usernum'], mes_account[0]['passwd'])
    login_result = DomAssert(drivers)
    login_result.assert_url("{}/demos/overview".format(ini.url))
    logging.info("前置条件：MES_DAP登录成功")
