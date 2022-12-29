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
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = DCRLoginPage(drivers)
        """变量"""
        query_dict = {
            'Return Order ID': 'RDHK202212250025',
            'Delivery/DN Order ID': '02HK2211160001591',
            'Brand': 'TECNO',
            'Return Date': '2022-12-25',
            'Status': 'Agree',
            'Return Type': 'Return To Seller',
            'Seller': 'PK20106',
            'Buyer': 'PK411448',
            'Seller Warehouse Region': 'New Market',
            'Buyer Warehouse Region': 'New Market',
            'Model': 'CH6i',
            'Market Name': 'CAMON 19 Neo',
            'Seller Country': 'Pakistan',
            'IMEI': '352525754569663'
        }
        query = ReturnOrderPage(drivers)
        user.click_gotomenu("Sales Management", "Return Order")
        query.click_unfold()
        query.random_Query_Method(query_dict)


if __name__ == '__main__':
    pytest.main(['SalesManagement_ReturnOrder.py'])
