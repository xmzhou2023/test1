import pytest

from project.TBM.api.api import APIRequest
from public.data.unified_login.unified import *
from public.base.assert_ui import *
from public.libs.unified_login.login import Login
from libs.common.read_config import *

pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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
    user.login(drivers, ini.url, account[2]['usernum'], account[2]['passwd'])
    DomAssert(drivers).assert_exact_att('首页')
    logging.info("前置条件：传音统一登录成功")


@pytest.fixture(scope='function', autouse=False)
def BarePhone_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_BarePhone_Add()
    yield api_response
    logging.info('开始后置操作')
    user.API_BarePhone_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def BarePhone_Factory_API():
    logging.info('开始前置操作-新建流程-补充工厂审批同意')
    user = APIRequest()
    api_response = user.API_BarePhone_Add()
    user.API_BarePhone_Factory(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_BarePhone_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def BarePhone_StructureEnginner_API():
    logging.info('开始前置操作-新建流程-结构工程师审批同意')
    user = APIRequest()
    api_response = user.API_BarePhone_Add()
    user.API_BarePhone_StructureEnginner(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_BarePhone_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def BarePhone_Approval_API():
    logging.info('开始前置操作-新建流程-业务审核审批同意')
    user = APIRequest()
    api_response = user.API_BarePhone_Add()
    user.API_BarePhone_Approval(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_BarePhone_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def BarePhone_Approval_Fail_API():
    logging.info('开始前置操作-新建流程-业务审核审批同意')
    user = APIRequest()
    api_response = user.API_BarePhone_Fail_Add()
    user.API_BarePhone_Approval(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_BarePhone_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Machine_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_Machine_Add()
    yield api_response
    logging.info('开始后置操作')
    user.API_Machine_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Machine_Factory_API():
    logging.info('开始前置操作-新建流程-补充工厂审批同意')
    user = APIRequest()
    api_response = user.API_Machine_Add()
    user.API_Machine_Factory(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Machine_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Machine_bomEnginner_API():
    logging.info('开始前置操作-新建流程-BOM工程师审批审批同意')
    user = APIRequest()
    api_response = user.API_Machine_Add()
    user.API_Machine_bomEnginner(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Machine_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Machine_Approval_API():
    logging.info('开始前置操作-新建流程-业务审核审批同意')
    user = APIRequest()
    api_response = user.API_Machine_Add()
    user.API_Machine_Approval(api_response[0], api_response[1], api_response[2])
    yield api_response
    logging.info('开始后置操作')
    user.API_Machine_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def Component_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_Components_Add()
    yield api_response
    logging.info('开始后置操作')
    user.API_Components_Delete(api_response[1], api_response[2])


@pytest.fixture(scope='function', autouse=False)
def Shipping_API():
    logging.info('开始前置操作')
    user = APIRequest()
    api_response = user.API_Shipping_Add()
    yield api_response
    logging.info('开始后置操作')
    user.API_Shipping_Delete(api_response[1], api_response[2])

@pytest.fixture(scope='function', autouse=False)
def KeyComponents_SQL():
    a = SQL('TBM', 'test')
    a.change_db(
        "UPDATE kd_flow_main SET is_deleted = 1 WHERE device_bid IN ( SELECT bid FROM kd_device_info WHERE model "
        "= '50A1S')"
    )
    logging.info('开始：调用sql脚本修改数据库数据')
    yield
    a.change_db(
        "UPDATE kd_flow_main SET is_deleted = 1 WHERE device_bid IN ( SELECT bid FROM kd_device_info WHERE model "
        "= '50A1S')"
    )
    logging.info('结束：调用sql脚本修改数据库数据')