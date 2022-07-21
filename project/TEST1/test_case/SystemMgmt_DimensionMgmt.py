import time

import allure
import pytest

from project.DRP.page_object.Center_Component import NavPage
from project.TEST1.page_object.SystemMgmt_DimensionMgmt import DimenPage
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

# @allure.feature("脚本名称") # 模块名称
class TestUtil:
    # @allure.story("二级标题") # 场景名称
    # @allure.title("三级标题")  # 用例名称
    # @allure.description("用例描述")
    # @allure.severity("normal")  # 用例等级
    # @pytest.mark.smoke # 用例标记
    # def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
    #     pass

    @allure.title("点击角色管理")  # 用例名称
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user =NavPage(drivers)
        user.click_gotonav("系统管理","维度管理")
        user = DomAssert(drivers)
        time.sleep(3)
        user.assert_url("/systemManage/dimensionManage")
        user = DimenPage(drivers)
        user.click_role()


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
