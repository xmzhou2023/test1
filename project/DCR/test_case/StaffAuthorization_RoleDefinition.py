from libs.common.time_ui import sleep
from project.DCR.page_object.StaffAuthorization_RoleDefinition import RoleDefinitionPage
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert, DomAssert
import pytest
import allure
import logging


@allure.feature("员工授权-角色定义")
class TestSetRolePermission:
    @allure.story("修改")
    @allure.title("角色定义页面，给“lhmItel店长”角色设置权限")
    @allure.description("角色定义页面，给“lhmItel店长”角色设置菜单权限")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        """DCR 二代账号登录"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "lhmadmin", "dcr123456")

        """打开Staff & Authorization模块下的 Role Definition的菜单"""
        user.click_gotomenu("Staff & Authorization", "Role Definition")

        """Role Definition角色定义页面，筛选“lhmItel店长”角色，然后添加Basic Data Management菜单权限用例"""
        role = RoleDefinitionPage(drivers)
        role.input_role_query("lhmItel店长")
        role.click_search()

        role.click_first_checkbox()
        role.click_permission_setting()
        role.click_check_basic_data_mgt()

        """点击保存"""
        role.click_save()
        """获取保存成功提示语，进行断言是否保存成功"""
        success = role.get_save_successfully()

        dom = DomAssert(drivers)
        dom.assert_exact_att(success)
        role.click_confirm()

        # """设置Basic Data Management模块权限后，检查是否能打开此模块下的菜单 """
        # user = DCRLogin(drivers)
        # user.dcr_login(udrivers, "testlhm0215", "dcr123456")
        # sleep(5)
        #
        # menu = MenuPage(drivers)
        # menu.click_gotomenu("Basic Data Management", "Sales Region Management")
        # sleep(5)
        #
        # sales_region = role.get_sale_region_mgt_text()
        # assert_ui.value_assert_In(sales_region, "Sales Region Management")


if __name__ == '__main__':
    pytest.main(['StaffAuthorization_RoleDefinition.py'])
