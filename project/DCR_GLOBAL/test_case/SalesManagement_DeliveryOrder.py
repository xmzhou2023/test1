from libs.common.time_ui import sleep
from project.DCR_GLOBAL.page_object.Center_Component import DCRLoginPage
from project.DCR_GLOBAL.page_object.SalesManagement_DeliveryOrder import DeliveryOrderPage
from public.base.assert_ui import ValueAssert
import datetime
import logging
from public.base.basics import Base
import pytest
import allure

@pytest.fixture(scope='function')
def function_export_fixture(drivers):
    yield
    menu = DCRLoginPage(drivers)
    for i in range(2):
        get_menu_class = menu.get_open_menu_class()
        class_value = "tags-view-item router-link-exact-active router-link-active active"
        if class_value == str(get_menu_class):
            menu.click_close_open_menu()
            sleep(1)

@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = DCRLoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@allure.feature("销售管理-出库单")
class TestQueryDeliveryOrder:
    @allure.story("查询出库单")
    @allure.title("出库单页面，查询出库单列表加载数据")
    @allure.description("出库单页面，查询出库单列表加载数据正常，断言查询的出库单数据是否加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        menu = DCRLoginPage(drivers)
        #user.dcr_login(drivers, "testsupervisor", "dcr123456")
        base = Base(drivers)
        base.refresh()
        sleep(3.5)
        """打开销售管理-打开出库单页面"""
        menu.click_gotomenu("Sales Management", "Delivery Order")
        query = DeliveryOrderPage(drivers)
        sale_order = query.get_sales_order_text()
        deli_order = query.get_delivery_order_text()
        deli_date = query.get_delivery_date_text()
        status = query.get_status_text()
        total = query.get_total_text()
        ValueAssert.value_assert_IsNoneNot(sale_order)
        ValueAssert.value_assert_IsNoneNot(deli_order)
        ValueAssert.value_assert_IsNoneNot(deli_date)
        ValueAssert.value_assert_IsNoneNot(status)
        query.assert_total(total)


@allure.feature("销售管理-出库单")
class TestExportDeliveryOrder:
    @allure.story("导出出库单")
    @allure.title("出库单页面，导出筛选的出库单记录")
    @allure.description("出库单页面，筛选出库单记录后，导出筛选的出库单记录")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    @pytest.mark.usefixtures('function_export_fixture')
    def test_002_001(self, drivers):
        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)
        """打开销售管理-打开出库单页面"""
        menu = DCRLoginPage(drivers)
        menu.click_gotomenu("Sales Management", "Delivery Order")
        export = DeliveryOrderPage(drivers)
        # 获取日期
        base = Base(drivers)
        today = base.get_datetime_today()
        last_date = export.get_last_day(1)
        export.click_unfold()
        export.input_delivery_date(last_date, today)
        export.click_status_input_box()
        export.click_fold()
        export.click_search()
        # 筛选出库单后，点击导出功能
        export.click_export()
        export.click_download_more()
        down_status = export.click_export_search()
        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()
        """断言导出记录列表，字段内容是否正确"""
        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Delivery Order")
        ValueAssert.value_assert_equal(task_id, "testsupervisor")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)


if __name__ == '__main__':
    pytest.main(['SalesManagement_DeliveryOrder.py'])
