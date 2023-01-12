import allure
import pytest

from project.DCR_INDIA.page_object.CustomerManagement_CustomerManagement import CustomerManagementPage

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("客户管理-客户管理") # 模块名称
class TestSearch:
    @allure.story("查询客户")
    @allure.title("随机条件组合查询")
    @allure.description("客户管理页面，随机组合查询条件查询客户成功")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_001_001(self, drivers):
        """变量"""
        query_dict = {
            'Customer': 'IN407454V',
            'Contact Name': 'sandeep wadhwani',
            'Sales Region': 'India District_India-itel-HA_GUJ-MH',
            'Country/City': 'India_Maharashtra_Yavatmal',
            'Customer Type': 'Distributor',
            'Customer Grade': 'A',
            'SAP Customer ID': '407454',
            'Whether use DCR system': 'Yes',
            'Customer Category': '',
            'Brand': 'itel appliances',
            'Status': 'Enable',
            'Channel Sales Manager': '',
            'User': 'IN407454V',
            'Warehouse': 'WIN407454V'
        }
        add = CustomerManagementPage(drivers)
        add.click_menu("Customer Management", "Customer Management")
        add.click_unfold()
        add.random_Query_Method(query_dict)


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
