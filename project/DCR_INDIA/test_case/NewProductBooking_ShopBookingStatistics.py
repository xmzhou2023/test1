from project.DCR_INDIA.page_object.Center_Component import LoginPage
from project.DCR_INDIA.page_object.NewProductBooking_ShopBookingStatistics import ShopBookingStatisticsPage
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
    @pytest.mark.UT
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        """变量"""
        query_dict = {
            #'Enable Date': '2022-12-26',
            'Shop': '1400435304',
            'Model': 'AD9',
            'Brand': 'TECNO',
            'Market Name': 'PHANTOM X2 Pro',
            'Manpower Type': 'Unmanned',
            'Country': 'India',
            'Sales Region': 'India-TECNO',
            'Template': 'TEM2212200003'
        }
        query = ShopBookingStatisticsPage(drivers)
        user.click_gotomenu("New Product Booking", "Shop Booking Statistics")
        query.click_unfold_fold('Unfold')
        query.shop_book_statistics_enable_date_query('Enable Date', '2022-12-26')
        query.random_Query_Method(query_dict)


if __name__ == '__main__':
    pytest.main(['NewProductBooking_ShopBookingStatistics.py'])

