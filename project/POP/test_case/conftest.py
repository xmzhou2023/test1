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
    if pro_env == "test":
        """使用统一登录"""
        logging.info("前置条件：传音体专店登录开始")
        user = Login(drivers)
        user.pop_login(drivers,ini.url,account[10]['usernum'],account[10]['passwd'])
        user = DomAssert(drivers)
        user.assert_url(ini.url)
        user = SQLAssert(pro_name, pro_env)
        user.assert_sql(word=account[10]['username'],sql='SELECT user_name from `user` where id="28";')
        logging.info("前置条件：传音体专店登录成功")
    else:
        logging.info("前置条件：传音体专店登录开始")
        user = Login(drivers)
        user.pop_login(drivers, ini.url, account[10]['usernum'], account[10]['passwd'])
        user = DomAssert(drivers)
        user.assert_url(ini.url)
        user = SQLAssert(pro_name, pro_env)
        user.assert_sql(word=account[10]['username'], sql='SELECT user_name from `user` where id="28";')
        logging.info("前置条件：传音体专店登录成功")
