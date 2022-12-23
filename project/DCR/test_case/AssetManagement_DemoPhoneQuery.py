from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.AssetManagement_DemoPhoneQuery import DemoPhoneQueryPage
from public.base.assert_ui import ValueAssert, DomAssert
import logging
from libs.common.time_ui import sleep
from public.base.basics import Base
import datetime
import pytest
import allure

@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@allure.feature("资产管理-门店资产")
class TestQueryDemoPhoneQuery:
    @allure.story("查询门店资产")
    @allure.title("门店资产页面，随机组合条件查询门店资产")
    @allure.description("门店资产页面，随机组合条件查询门店资产")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    @pytest.mark.UT
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        """变量"""
        query_dict = {
            'Shop': 'BD017762',
            'Sales Region': 'Barisal-测试',
            'IMEI': '355790111294440',
            'Brand': 'TECNO',
            'Type': 'Common owner',
            'Status': 'Retired',
            'Manpower Type': 'Manned-Flexi',
            'Market Name': 'CAMON 15 Premier',
            'Model': 'CD8j',
            'Series': 'CAMON'
        }
        query = DemoPhoneQueryPage(drivers)
        user.click_gotomenu("Asset Management", "Demo Phone Query")
        query.click_unfold_fold('Unfold')
        query.random_Query_Method(query_dict)


if __name__ == '__main__':
    pytest.main(['AssetManagement_DemoPhoneQuery.py'])

