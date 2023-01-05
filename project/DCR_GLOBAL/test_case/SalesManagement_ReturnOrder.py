from project.DCR_GLOBAL.page_object.SalesManagement_ReturnOrder import ReturnOrderPage
from project.DCR_GLOBAL.page_object.Center_Component import DCRLoginPage
from libs.common.time_ui import sleep
from libs.common.connect_sql import *
from libs.config.conf import DOWNLOAD_PATH
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = DCRLoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()


@allure.feature("销售管理-退货单")
class TestReturnOrder:
    @allure.story("查询退货单")
    @allure.title("随机条件组合查询退货单")
    @allure.description("退货单页面，查询退货单的随机条件组合查询")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = DCRLoginPage(drivers)
        """变量"""
        query_dict = {
            'Return Order ID': 'RDHK202301020121',
            'Delivery/DN Order ID': '02HK2210070001307',
            'Brand': 'TECNO',
            #'Return Date': '2023-01-03',
            'Status': 'Agree',
            'Return Type': 'Return To Seller',
            'Seller': 'BD406678',
            'Buyer': 'BD4031266',
            'Seller Warehouse Region': 'Bangladesh District',
            'Buyer Warehouse Region': 'Bangladesh District',
            'Model': 'LG6n',
            'Market Name': 'POVA Neo 2',
            'Seller Country': 'Bangladesh',
            'IMEI': '351357690181424'
        }
        query = ReturnOrderPage(drivers)
        user.click_gotomenu("Sales Management", "Return Order")
        query.click_unfold()
        query.return_order_return_date_query('Return Date', '2023-01-03')
        query.random_Query_Method(query_dict)


if __name__ == '__main__':
    pytest.main(['SalesManagement_ReturnOrder.py'])
