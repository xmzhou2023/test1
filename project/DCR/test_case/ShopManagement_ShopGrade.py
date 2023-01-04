import allure
import pytest

from libs.common.time_ui import sleep
from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.ShopManagement_ShopGrade import ShopGrade
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("门店管理-门店等级") # 模块名称
class TestSearch:
    @allure.story("门店等级") # 场景名称
    @allure.title("查询门店等级")  # 用例名称
    @allure.description("查询门店等级")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        """变量"""
        query_dict = {
            'Brand': 'Infinix',
            'Country': 'Senegal',
        }
        add = ShopGrade(drivers)
        add.click_menu("Shop Management", "Shop Grade")
        add.random_Query_Method(query_dict)

    @allure.story("门店等级") # 场景名称
    @allure.title("新增门店等级")  # 用例名称
    @allure.description("新增门店等级")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_002(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        grade = ShopGrade(drivers)
        grade.click_menu("Shop Management", "Shop Grade")
        grade.click_add()
        grade.input_add_info('Brand', 'oraimo')
        grade.input_add_info('Country', 'Senegal')
        # grade.input_add_info('Statistical Dimension', 'Quarter')
        grade.input_ShopGrade('S', '10-20')
        grade.click_save()
        DomAssert(drivers).assert_att('Set Up Successfully')
        grade.input_search('Brand', 'oraimo')
        grade.input_search('Country', 'Senegal')
        grade.click_search()
        grade.assert_Query_result('Brand', 'oraimo')
        grade.assert_Query_result('Grade Name', 'S')
        grade.assert_Query_result('Sales Range', '10-20')
        grade.click_checkbox('oraimo')
        grade.click_delete()
        DomAssert(drivers).assert_att('Deleted Successfully')

    @allure.story("门店等级") # 场景名称
    @allure.title("编辑门店等级")  # 用例名称
    @allure.description("编辑门店等级")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_003(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        grade = ShopGrade(drivers)
        grade.click_menu("Shop Management", "Shop Grade")
        grade.click_add()
        grade.input_add_info('Brand', 'oraimo')
        grade.input_add_info('Country', 'Senegal')
        # grade.input_add_info('Statistical Dimension', 'Quarter')
        grade.input_ShopGrade('S', '10-20')
        grade.click_save()
        DomAssert(drivers).assert_att('Set Up Successfully')
        grade.input_search('Brand', 'oraimo')
        grade.input_search('Country', 'Senegal')
        grade.click_search()
        grade.click_edit('oraimo')
        grade.input_ShopGrade('A', '21-30', 'edit')
        grade.click_save()
        DomAssert(drivers).assert_att('Set Up Successfully')
        grade.click_search()
        grade.assert_Query_result('Brand', 'oraimo')
        grade.assert_Query_result('Grade Name', 'A')
        grade.assert_Query_result('Sales Range', '21-30')
        grade.click_checkbox('oraimo')
        grade.click_delete()
        DomAssert(drivers).assert_att('Deleted Successfully')

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
