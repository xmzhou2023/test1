from project.DCR_GLOBAL.page_object.Center_Component import DCRLoginPage
from project.DCR_GLOBAL.page_object.AssetManagement_DemoPhoneQuery import DemoPhoneQueryPage
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
    menu = DCRLoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@allure.feature("资产管理-样机查询")
class TestQueryDemoPhoneQuery:
    @allure.story("样机查询")
    @allure.title("门店资产页面，随机组合条件查询样机")
    @allure.description("门店资产页面，随机组合条件查询样机")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    @pytest.mark.UT
    def test_001_001(self, drivers):
        user = DCRLoginPage(drivers)
        """变量"""
        query_dict = {
            #'Shop': 'BD017762',
            'Sales Region': 'Bangladesh District',
            'IMEI': '350677680044626',
            'Brand': 'TECNO',
            'Type': 'Shop owner demo device',
            'Status': 'Publish',
            'Manpower Type': 'Manned',
            'Market Name': 'POVA 4',
            'Model': 'LG7n',
            'Series': 'POVA'
        }
        query = DemoPhoneQueryPage(drivers)
        user.click_gotomenu("Asset Management", "Demo Phone Query")
        query.click_unfold_fold('Unfold')
        query.random_Query_Method(query_dict)


if __name__ == '__main__':
    pytest.main(['AssetManagement_DemoPhoneQuery.py'])

