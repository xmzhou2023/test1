from datetime import datetime

import allure
import pytest

from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.StaffAuthorization_UserAndCustomerAssociation import UserAndCustomerAssociation
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("用户和授权-员工与客户关系") # 模块名称
class TestCustomerAssociation:
    @allure.story("员工与客户关系")  # 场景名称
    @allure.title("页面查询")  # 用例名称
    @allure.description("随机组合查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):
        """变量"""
        query_dict = {
            'User': 'SN200000',
            'Sales Region': 'West Africa IV_Senegal_Kaolack Dept',
            'Customer Type': 'Retailer',
            'Customer Categroy': '',
            'Brand': 'Infinix',
            'Customer': 'SN400001',
            'Country': 'Senegal'
        }
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        add = UserAndCustomerAssociation(drivers)
        add.click_menu("Staff & Authorization", "User And Customer Association")
        add.click_unfold()
        add.random_Query_Method(query_dict)

    @allure.story("员工与客户关系")
    @allure.title("导入用户与客户关系")
    @allure.description("导入用户与客户关系")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_001_002(self, drivers):
        login = LoginPage(drivers)
        login.initialize_login(drivers, "18650493", "xLily6x")
        """打开User Authorization菜单页面 """
        user = UserAndCustomerAssociation(drivers)
        user.click_menu("Staff & Authorization", "User And Customer Association")
        user.click_unfold()
        user.input_search('User', "wjkTS")
        user.input_search('Customer', "SN400001")
        user.click_search()
        """移除所有授权"""
        user.reset_Association('wjkTS')
        """导入文件授权"""
        user.click_function_button('Import')
        user.import_file('用户与客户关系.xlsx')
        user.click_save()
        user.click_confirm()
        user.assert_Record_result('Import Record', '用户与客户关系.xlsx', 'Status', 'Upload Successfully')
        """断言ImportRecord页面结果"""
        today = datetime.now().strftime('%Y-%m-%d')
        user.assert_Record_result('Import Record', '用户与客户关系.xlsx', 'Status', 'Upload Successfully')
        user.assert_Record_result('Import Record', '用户与客户关系.xlsx', 'Total', '1')
        user.assert_Record_result('Import Record', '用户与客户关系.xlsx', 'Success', '1')
        user.assert_Record_result('Import Record', '用户与客户关系.xlsx', 'Import Date', today)
        """断言：用户与客户关系授权成功"""
        user.click_menu("Staff & Authorization", "User And Customer Association")
        user.click_unfold()
        user.input_search('User', "wjkTS")
        user.input_search('Customer', "SN400001")
        user.click_search()
        user.assert_Query_result('Customer ID', 'SN400001')
        """移除客户关系授权"""
        user.click_CheckBox('wjkTS')
        user.click_function_button('Delete')
        user.click_Delete()
        DomAssert(drivers).assert_att('Successfully')
        user.assert_NoData()


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
