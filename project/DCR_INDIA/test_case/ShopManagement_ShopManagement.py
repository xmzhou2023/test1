import allure
import pytest

from project.DCR_INDIA.page_object.ShopManagement_ShopManagement import ShopManagementPage

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("门店管理-门店管理") # 模块名称
class TestSearch:
    @allure.story("查询全球门店") # 场景名称
    @allure.title("随机条件组合查询")  # 用例名称
    @allure.description("门店管理页面，随机条件组合查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        """变量"""
        query_dict = {
            'Shop': 'IN114578',
            'Sales Region': 'India District_India-itel-SG_WB-NESA-OR',
            'Brand': 'itel accessories',
            # 'Shop Type': 'IR',
            'Create Date': '2022-11-12To2022-11-14',
            'Country/City': 'India_West Bengal_Murshidabad',
            # 'Shop Grade': 'C',
            'Manpower Type': 'Unmanned',
            'Image Type': 'Sales Point',
            'Retail Customer': 'IN114578',
            'Public ID': 'PIN114578',
            'City Tier': 'T4',
            'Carlcare Shop Code': 'No',
            'POS ID': 'No'
        }
        add = ShopManagementPage(drivers)
        add.click_menu("Shop Management", "Shop Management")
        add.click_unfold()
        add.random_Query_Method(query_dict)

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
