import allure
import pytest

from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.StaffAuthorization_HierarchyManagement import HierarchyManagement
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("用户和授权-上下级关系管理") # 模块名称
class TestHierarchy:
    @allure.story("上下级关系管理") # 场景名称
    @allure.title("页面查询")  # 用例名称
    @allure.description("随机组合查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):
        """变量"""
        query_dict = {
            'User ID': 'wjkTS',
            'User Name': 'wjkTS',
            'Employee Name': 'wjkTS',
            'Country/City': 'Senegal_Kaolack_Kaolack',
            'Staff Status': 'On Service',
            'Gender': 'Female',
            'Have Superior or Not': 'Yes',
            'Have Shop or Not': 'No',
            'Brand': 'TECNO',
            'Position': 'Supervisor',
            'Country': 'Senegal',
            'Staff Type': 'Transsion Staff',
            'Superior': '18650493'
        }
        # user = LoginPage(drivers)
        # user.initialize_login(drivers, "18650493", "xLily6x")
        add = HierarchyManagement(drivers)
        add.click_menu("Staff & Authorization", "Hierarchy Management")
        add.click_unfold()
        add.random_Query_Method(query_dict)

    @allure.story("上下级关系管理") # 场景名称
    @allure.title("关系树查询")  # 用例名称
    @allure.description("关系树查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        add = HierarchyManagement(drivers)
        add.click_menu("Staff & Authorization", "Hierarchy Management")
        """点击Staff Hierarchy"""
        add.click_function_button('Staff Hierarchy')
        """断言：存在上下级关系树"""
        add.assert_Hierarchy_exist('wjkTS001')

    @allure.story("上下级关系管理") # 场景名称
    @allure.title("新增下级关系")  # 用例名称
    @allure.description("新增下级关系")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_003(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        add = HierarchyManagement(drivers)
        add.click_menu("Staff & Authorization", "Hierarchy Management")
        """筛选用户"""
        add.input_search('User ID', 'wjkTS')
        add.click_search()
        """点击复选框"""
        add.click_checkbox('wjkTS')
        """点击Add The Subordinate增加下级关系"""
        add.click_function_button('Add The Subordinate')
        add.click_dialog_unfold()
        add.input_dialog_search('User ID', '1671417004')
        add.click_dialog_search()
        add.click_checkbox('1671417004')
        add.click_dialog_save()
        """断言：增加下级关系成功"""
        add.click_row_function('wjkTS', 'Subordinate')
        add.click_dialog_unfold()
        add.input_dialog_search('User ID', '1671417004')
        add.click_dialog_search()
        add.assert_dialog_Query_result('User ID', '1671417004')

    @allure.story("上下级关系管理") # 场景名称
    @allure.title("删除下级关系")  # 用例名称
    @allure.description("删除下级关系")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_004(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        add = HierarchyManagement(drivers)
        add.click_menu("Staff & Authorization", "Hierarchy Management")
        """筛选用户"""
        add.input_search('User ID', 'wjkTS')
        add.click_search()
        """点击复选框"""
        add.click_checkbox('wjkTS')
        """点击Add The Subordinate 增加下级关系"""
        add.click_function_button('Add The Subordinate')
        add.click_dialog_unfold()
        add.input_dialog_search('User ID', '1671417004')
        add.click_dialog_search()
        add.click_checkbox('1671417004')
        add.click_dialog_save()
        """点击Delete The Subordinate 删除下级关系"""
        add.click_function_button('Delete The Subordinate')
        add.click_dialog_unfold()
        add.input_dialog_search('User ID', '1671417004')
        add.click_dialog_search()
        add.click_checkbox('1671417004')
        add.click_dialog_save('delete')
        DomAssert(drivers).assert_att('Delete success!')
        """断言：删除下级关系成功"""
        add.click_row_function('wjkTS', 'Subordinate')
        add.click_dialog_unfold()
        add.input_dialog_search('User ID', '1671417004')
        add.click_dialog_search()
        add.assert_NoData()

    @allure.story("上下级关系管理") # 场景名称
    @allure.title("设置上级关系")  # 用例名称
    @allure.description("设置上级关系")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_005(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        add = HierarchyManagement(drivers)
        add.click_menu("Staff & Authorization", "Hierarchy Management")
        """筛选用户"""
        add.input_search('User ID', '1671417004')
        add.click_search()
        """点击Set Superior 设置上级关系"""
        add.click_row_function('1671417004', 'Operation')
        add.input_dialog_search('User ID', 'wjkTS001')
        add.click_dialog_search()
        add.click_checkbox('wjkTS001')
        add.click_dialog_save()
        """断言：设置上级关系成功"""
        add.click_search()
        add.assert_Query_result('Superior ID', 'wjkTS001')

    @allure.story("上下级关系管理")
    @allure.title("导出上下级关系")
    @allure.description("导出上下级关系")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_001_006(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """打开User Authorization菜单页面 """
        add = HierarchyManagement(drivers)
        add.click_menu("Staff & Authorization", "Hierarchy Management")
        add.input_search('User ID', "wjkTS")
        add.click_search()
        """导出筛选条件下的门店授权"""
        add.click_function_button('Export')
        """断言：存在导出文件进度条"""
        add.assert_export_success()


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
