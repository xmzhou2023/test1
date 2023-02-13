import allure
import pytest

from project.DCR_GLOBAL.page_object.ShopManagement_ShopManagement import ShopManagementPage

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("门店管理-门店管理(global)") # 模块名称
class TestShopManagementSearch:
    @allure.story("查询全球门店") # 场景名称
    @allure.title("随机条件组合查询")  # 用例名称
    @allure.description("门店管理页面，随机条件组合查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        """变量"""
        query_dict = {
            'Shop': 'PK4999705',
            'Sales Region': 'New Market_Pakistan-Infinix_North',
            'Brand': 'Infinix',
            'Shop Type': 'IR',
            'Create Date': '2022-07-17To2022-07-19',
            'Country/City': 'Pakistan_Punjab_Wah Cantt',
            'Shop Grade': 'C',
            'Manpower Type': 'Unmanned',
            'Image Type': 'Sales Point',
            'Retail Customer': 'PK4999705',
            'Public ID': 'PPK4999705',
            'City Tier': '',
            'Carlcare Shop Code': 'No',
            'POS ID': 'No'
        }
        add = ShopManagementPage(drivers)
        add.click_menu("Shop Management", "Shop Management")
        add.click_unfold()
        add.random_Query_Method(query_dict)


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
