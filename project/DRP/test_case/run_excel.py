import importlib

import pytest

from libs.common import read_excel
from libs.common.logger_ui import log
from libs.config.conf import TESTCASE_PATH
from public.libs.unified_login.login import Login
from libs.common.assert_ui import DomAssert
# from project.DRP.page_object.nav import NavPage
# from project.DRP.page_object.user import UserPage

class TestLogin:
    def test_run_excel(self,drivers):
        log.info("Excel驱动自动化用例：开始")
        for step in read_excel.excel(TESTCASE_PATH):
            if step['步骤名'] is None:
                continue
            else:
                步骤名 = step['步骤名']
                模块名 = step['模块名']
                类名 = step['类名']
                关键字 = step['关键字']
                参数 = step['参数']
                log.info(参数)
                if len(参数) != 0:
                    parm = 参数[0].split(',')
                else:
                    parm = 参数

                if 类名 is None:
                    key_word = Login(drivers)
                    f = getattr(key_word, f"{关键字}")  # 关键字变为python函数
                    f(drivers, *parm)  # 解包参数，函数运行
                else:
                    excelmodule = importlib.import_module(f"{模块名}")
                    f = getattr(excelmodule, f"{类名}")
                    key_word = f(drivers)
                    f = getattr(key_word, f"{关键字}")  # 关键字变为python函数
                    f(*parm)  # 解包参数，函数运行

        log.info("Excel驱动自动化用例解析结束：结束")

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_excel.py'])