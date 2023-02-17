from project.DCR_INDIA.page_object.SalesManagement_ReturnOrder import ReturnOrderPage
from project.DCR_INDIA.page_object.Center_Component import LoginPage
from libs.common.time_ui import sleep
from public.base.basics import Base
from libs.common.connect_sql import *
from libs.config.conf import DOWNLOAD_PATH
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
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
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        """变量"""
        query_dict = {
            'Return Order ID': 'RDIN202301044532',
            'Delivery/DN Order ID': '02IN2212160011396',
            'Brand': 'itel',
            #'Return Date': '2023-01-02',
            'Status': 'Agree',
            'Return Type': 'Return To Seller',
            'Seller': 'IN400599I',
            'Buyer': '1400019850',
            'Seller Warehouse Region': 'India District',
            'Buyer Warehouse Region': 'India District',
            'Model': 'A511LQ',
            'Market Name': 'A511LQ',
            'Seller Country': 'India',
            'IMEI': '355168718751205'
        }
        query = ReturnOrderPage(drivers)
        user.click_menu("Sales Management", "Return Order")
        query.click_unfold()
        query.return_order_return_date_query('Return Date', '2023-01-04')
        query.random_Query_Method(query_dict)


if __name__ == '__main__':
    pytest.main(['SalesManagement_ReturnOrder.py'])
