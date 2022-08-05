import pytest, logging
from public.data.unified_login.unified import *
from public.base.assert_ui import *
from public.libs.unified_login.login import Login
from libs.common.read_config import *
from project.SRM.page_object.login import LoginPage

pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture(scope='session',autouse=True)


def __init__(drivers, env_name):
    """初始化"""

    global pro_env
    pro_env = env_name
    logging.info("【{}】项目【{}】环境- UI自动化开始执行".format(pro_name, pro_env))
    ini = ReadConfig(pro_name, pro_env)
    # url="http://sitsrm.transsion.com/ELSServer_CY/login/login.html"
    # elsAccount ="860000"
    # elsSubAccount = "1001"

    user = LoginPage(drivers)
    user.login(ini.url, "860000", "1001")

    """使用统一登录"""
    # logging.info("前置条件：传音统一登录开始")
    # user = Login(drivers)
    # user.srm_login(drivers,ini.url, account_srm[0]['elAccount'], account_srm[0]['elSubAccount'])
    # # user.srm_login(drivers,url,elsAccount,elsSubAccount)
    # user = DomAssert(drivers)
    # # user.assert_url("{}/dashboard".format(ini.url))
    # user.assert_url("http://sitsrm.transsion.com/ELSServer_CY/default.jsp?account=860000_1001")
    # # user = SQLAssert(pro_name, pro_env)
    # # user.assert_sql(word=account[0]['username'], sql='select name_zh from uc_user where enable_flag=1')
    # logging.info("前置条件：传音统一登录成功")