import pytest
import logging
from public.base.assert_ui import *
#from project.DCR_INDIA.page_object.Center_Component import LoginPageDCR
from libs.common.read_config import *
from public.libs.unified_login.login import Login
from public.data.unified_login.unified import *

pro_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).split('\\')[-1]
pro_env = 'prod' # 需要手动配置测试环境
ini = ReadConfig(pro_name, pro_env)


@pytest.fixture(scope='session',autouse=True)
def test_login(drivers):
    """登录用户"""
    logging.info("前置条件：传音统一登录开始")
    #user = LoginPageDCR(drivers)
    #user.dcr_login(drivers, ini.url, "testsupervisor", "dcr123456")

    user = Login(drivers)
    user.dcr_login(drivers, ini.url, account[3]['usernum'], account[3]['passwd'])
    DomAssert(drivers).assert_att("testsupervisor")
    logging.info("前置条件：传音统一登录成功")


pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture(scope='session',autouse=True)
def __init__(drivers, env_name):
    """初始化"""
    global pro_env
    pro_env = "prod"
    logging.info("【{}】项目【{}】环境- UI自动化开始执行".format(pro_name, pro_env))
    ini = ReadConfig(pro_name, pro_env)

