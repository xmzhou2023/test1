from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.NewProductBooking_ShopBookingStatistics import ShopBookingStatisticsPage
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

@allure.feature("新产品预订-门店预订统计")
class TestQueryShopBookingStatistics:
    @allure.story("样机查询")
    @allure.title("新产品预订页面，随机组合条件查询门店预订统计")
    @allure.description("门店资产页面，随机组合条件查询门店预订统计")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    @pytest.mark.UT
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """变量"""
        query_dict = {
            #'Enable Date': '2022-12-26',
            'Shop': 'NG003867',
            'Model': 'X608',
            'Brand': 'Infinix',
            'Market Name': 'HOT 6',
            'Manpower Type': 'Unmanned',
            'City': 'Aba',
            'Sales Region': 'Barisal-测试',
            'Template': 'TEM2212190002'
        }
        query = ShopBookingStatisticsPage(drivers)
        user.click_gotomenu("New Product Booking", "Shop Booking Statistics")
        query.click_unfold_fold('Unfold')
        query.random_Query_Method(query_dict)

if __name__ == '__main__':
    pytest.main(['NewProductBooking_ShopBookingStatistics.py'])

