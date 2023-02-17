from project.DCR_GLOBAL.page_object.Center_Component import DCRLoginPage
from project.DCR_GLOBAL.page_object.AssetManagement_ShopAsset import ShopAssetPage
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


@allure.feature("资产管理-门店资产")
class TestQueryShopAsset:
    @allure.story("查询门店资产")
    @allure.title("门店资产页面，随机组合条件查询门店资产")
    @allure.description("门店资产页面，随机组合条件查询门店资产")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_002(self, drivers):
        user = DCRLoginPage(drivers)
        """变量"""
        #权限变动，数据修改下
        query_dict = {
            'Country': 'Pakistan',
            'Brand': 'TECNO',
            'Create Date': '2021-09-09',
            'Category': 'Shop Construction Props',
            'Status': 'Available',
            'Shop': 'PKCL3466',
            'Asset Name': '收银台2021',
            'Has ASN': 'Yes',
            'Sales Region': 'Pakistan-TECNO',
            'Design By': 'Local',
            'Manpower Type': 'Unmanned'
        }
        query = ShopAssetPage(drivers)
        user.click_gotomenu("Asset Management", "Shop Asset")
        query.click_unfold_fold('Unfold')
        query.random_Query_Method(query_dict)


if __name__ == '__main__':
    pytest.main(['AssetManagement_ShopAsset.py'])
