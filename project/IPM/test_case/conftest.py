import pytest, logging

from public.data.unified_login.unified import *
from public.base.assert_ui import *
from public.libs.unified_login.login import Login
from libs.common.read_config import *
from project.IPM.page_object.Center_Component import *

pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
username=account[15]['usernum']
pwd=account[15]['passwd']
@pytest.fixture(scope='session', autouse=True)
def __init__(drivers, env_name):
    """初始化"""
    global pro_env
    pro_env = env_name
    logging.info("【{}】项目【{}】环境- UI自动化开始执行".format(pro_name, pro_env))
    ini = ReadConfig(pro_name, pro_env)

    """使用统一登录"""
    logging.info("前置条件：传音统一登录开始")
    user = Login(drivers)
    user.IPM_login(drivers, ini.url,username , pwd)
    logging.info("前置条件：传音统一登录成功")


def current_url_ipm(driver,configure,env_name):
    """登录页存在多个"""
    kt_fixture=CenterComponent(driver)
    url =kt_fixture.current_url_ipm()
    if configure in url:
        logging.info('当前页面的地址匹配成功')
    else:
        logging.info('当前地址不匹配，重新跳转登录页')
        kt_ini = ReadConfig(pro_name, env_name)
        kt_fixture.get_url(kt_ini._get('HOST', 'url_kt5'))
        kt_fixture.ipm_input_account_KT5(username
                                         )
        kt_fixture.ipm_input_passwd_KT5(pwd)
        kt_fixture.ipm_click_login_KT5()