from project.DCR.page_object.Center_Component import LoginPage
from project.DCR_GLOBAL.page_object.NewProductBooking_ShopBookingStatistics import ShopBookingStatisticsPage
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

@allure.feature("新品预定-门店预订统计")
class TestQueryShopBookingStatistics:
    @allure.story("新品预定")
    @allure.title("新品预定页面，随机组合条件查询门店预订统计")
    @allure.description("新品预定页面，随机组合条件查询门店预订统计")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    @pytest.mark.UT
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        """变量"""
        query_dict = {
            #'Enable Date': '2022-12-26',
            'Shop': 'PK48922',
            'Model': 'X672',
            'Brand': 'Infinix',
            'Market Name': 'NOTE 12 VIP',
            'Manpower Type': 'Unmanned',
            'City': 'Lahore',
            'Sales Region': 'Pakistan-Infinix',
            'Template': 'TEM2206300001'
        }
        query = ShopBookingStatisticsPage(drivers)
        user.click_gotomenu("New Product Booking", "Shop Booking Statistics")
        query.click_unfold_fold('Unfold')
        query.random_Query_Method(query_dict)


if __name__ == '__main__':
    pytest.main(['NewProductBooking_ShopBookingStatistics.py'])

