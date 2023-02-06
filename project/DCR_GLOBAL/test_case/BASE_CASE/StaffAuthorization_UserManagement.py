from project.DCR_GLOBAL.page_object.StaffAuthorization_UserManagement import UserManagementPage
import allure
import pytest

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""


@allure.feature("员工授权-用户管理") # 模块名称
class TestSearch:
    @allure.story("查询用户")
    @allure.title("随机条件组合查询")
    @allure.description("用户管理页面，查询用户列表所有用户数据加载")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):
        """变量"""
        query_dict = {
            'User ID': 'PK2021301',
            'User Name': 'Ahmed Mobile+Okara',
            'Superior': '',
            'Sales Region': 'Okara',
            'Staff Status': 'On Service',
            'Have Superior or Not': 'No',
            'Have Shop or Not': 'No',
            'Staff Type': 'Dealer Staff',
            'Belong To Customer': 'PK20213',
            'Country/City': 'Okara',
            'Brand': 'TECNO',
            'Position': 'Sub_dealer Sales Manager',
            'Role': 'Sub_dealer Sales Manager'
        }
        add = UserManagementPage(drivers)
        add.click_menu("Staff & Authorization", "User Management")
        add.click_unfold()
        add.random_Query_Method(query_dict)


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
