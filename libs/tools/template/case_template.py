import os, sys
import allure
import pytest
from public.data.unified_login.unified import *
from libs.common.assert_ui import DomAssert, SQLAssert, ValueAssert
from libs.common.logger_ui import log

@allure.feature("一级标题") # 模块名称
class TestUtil:
    @allure.story("二级标题") # 场景名称
    @allure.title("三级标题")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级，blocker\critical\normal\minor\trivial
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers): # 用例名称取名规范'test+场景编号+用例编号'
        pass

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
