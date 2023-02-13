from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.GTMManagement_InventoryShortageReport import InventoryShortagePage
from public.base.assert_ui import ValueAssert, DomAssert
import logging
import pytest
import allure

"""后置关闭菜单方法  pytest.fixture(scope='作用域' function函数级别  """
@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()


@allure.feature("GTM管理-库存不足报告")
class TestQueryInventoryShortage:
    @allure.story("查询库存不足报告")
    @allure.title("库存不足报告页面，根据品牌、国家、时间查询库存不足报告数据")
    @allure.description("库存不足报告页面，根据品牌、国家、时间查询库存不足报告数据")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.UT
    @pytest.mark.usefixtures('function_menu_f  @pytest.mark.UTixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("GTM Management", "Inventory Shortage Report")

        query = InventoryShortagePage(drivers)
        query.query_inventory_shortage_report('TECNO', 'DB3', '2022-06-01', '2022-11-16')
        """点击查询按钮"""
        query.click_search()

        """断言获取列表数据，与筛选条件比较是否一致"""
        get_total = query.get_total()
        query.assert_total(get_total)
        get_shop_id = query.get_list_field_content('Get list Shop ID')
        get_shop_name = query.get_list_field_content('Get list Shop Name')
        get_quantity = query.get_list_field_content('Get list Inventory Quantity')
        get_frequency = query.get_list_field_content('Get list Frequency')
        get_brand = query.get_list_field_content('Get list Brand')
        get_country = query.get_list_field_content('Get list Country')
        ValueAssert.value_assert_IsNoneNot(get_shop_id)
        ValueAssert.value_assert_IsNoneNot(get_shop_name)
        ValueAssert.value_assert_IsNoneNot(get_quantity)
        ValueAssert.value_assert_IsNoneNot(get_frequency)
        ValueAssert.value_assert_equal('TECNO', get_brand)
        ValueAssert.value_assert_equal('DB3', get_country)


if __name__ == '__main__':
    pytest.main(['GTMManagement_InventoryShortageReport.py'])
