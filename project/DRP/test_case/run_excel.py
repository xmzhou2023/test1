import pytest

from libs.common import read_excel
from libs.common.action import KeyWord
from libs.common.logger_ui import log
from libs.config.conf import TESTCASE_PATH

class TestLogin:
    def test_run_excel(self,drivers):

        key_word = KeyWord(drivers)
        for step in read_excel.excel(TESTCASE_PATH):
            if step['步骤名'] is None:
                continue
            else:
                步骤名 = step['步骤名'] # 变量名可以是unicode,包括中文
                关键字 = step['关键字']
                参数 = step['参数']
                # print(f"{步骤名}...", end='') # 取消换行
                f = getattr(key_word, f"key_{关键字}") # 关键字变为python函数
                f(*参数) # 解包参数，函数运行
                log.info(step)
if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_excel.py'])