from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.AssetManagement_DemoPhoneQuery import DemoPhoneQueryPage
from public.base.assert_ui import ValueAssert, DomAssert
import logging
from libs.common.time_ui import sleep
from public.base.basics import Base
import datetime
import pytest
import allure


@allure.feature("资产管理-门店资产")
class TestQueryShopAsset:
    @allure.story("查询门店资产")
    @allure.title("门店资产页面，随机组合条件查询门店资产")
    @allure.description("门店资产页面，随机组合条件查询门店资产")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    @pytest.mark.UT
    def test_001_003(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        """变量"""
        query_dict = {
            'Shop': 'Bangladesh',
            'Sales Region': 'TECNO',
            'IMEI': '2022-12-21',
            'Brand': 'Shop Construction Props',
            'Type': 'Available',
            'Publish Time': 'BD026690',
            'Status': 'TECNO_门店建筑道具',
            'Retire Time': 'No',
            'Sales Region': 'Barisal-测试',
            'Design By': 'Headquarters',
            'Manpower Type': 'Manned'
        }
        query = DemoPhoneQueryPage(drivers)
        user.click_gotomenu("Asset Management", "Demo Phone Query")
        query.click_unfold_fold('Unfold')
        query.random_Query_Method(query_dict)


if __name__ == '__main__':
    pytest.main(['AssetManagement_DemoPhoneQuery.py'])

