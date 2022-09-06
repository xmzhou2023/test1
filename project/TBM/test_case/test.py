import allure
import pytest

from project.TBM.page_object.test import BOM
from public.base.assert_ui import DomAssert
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("脚本名称") # 模块名称
class TestUtil:
    @allure.story("二级标题") # 场景名称
    @allure.title("三级标题")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = BOM(drivers)
        # user.click_menu()
        # user.click_add()
        # user.click_type()
        # user.click_brand()
        # user.click_mach()
        # user.click_stage()
        # user.click_market()
        # user.click_addBom()
        # user.click_Bomtype()
        # user.click_Bomstatus()
        # user.click_edit()
        # user.click_code()
        # user.click_sum()
        # user.click_comfirm()
        # user.click_audit_mpm()
        # user.click_audit_nps()
        # user.click_submit()
        # DomAssert(drivers).assert_att('创建流程成功')
        # user.click_search()
        # code = user.get_code()# 目前没用到传参
        user.click_todo()
        user.click_app()
        user.click_recall()
        user.click_menu()
        user.click_delete()
        DomAssert(drivers).assert_att('删除成功')

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
