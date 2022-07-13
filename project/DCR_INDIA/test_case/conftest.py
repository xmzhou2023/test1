import pytest, logging
from public.data.unified_login.unified import *
from public.base.assert_ui import DomAssert, SQLAssert
from public.libs.unified_login.login import Login
from libs.common.read_config import *

pro_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).split('\\')[-1]
pro_env = 'prod' # 需要手动配置测试环境

logging.info(pro_name)
