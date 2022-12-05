from libs.common.time_ui import sleep
from project.DCR_INDIA.page_object.Center_Component import LoginPage
from project.DCR_INDIA.page_object.SalesManagement_DeliveryOrder import DeliveryOrderPage
from public.base.assert_ui import ValueAssert
import datetime
import logging
from public.base.basics import Base
import pytest
import allure

@allure.feature("销售管理-出库单")
class TestQueryDeliveryOrder:
    @allure.story("查询出库单")
    @allure.title("出库单页面，查询出库单列表加载数据")
    @allure.description("出库单页面，查询出库单列表加载数据正常，断言查询的出库单数据是否加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        base = Base(drivers)
        base.refresh()
        sleep(3.5)

        """打开销售管理-打开出库单页面"""
        menu = LoginPage(drivers)
        menu.click_gotomenu("Sales Management", "Delivery Order")

        query = DeliveryOrderPage(drivers)
        # 获取日期
        base = Base(drivers)
        today = base.get_datetime_today()
        """根据出库日期筛选列表数据"""
        query.click_unfold()
        query.input_delivery_date("2022-11-01", today)
        query.click_status_input_box()
        query.click_fold()
        query.click_search()
        """根据出库日期筛选结果后，断言列表是否能加载数据"""
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
        query.click_close_delivery_order()


@allure.feature("销售管理-出库单")
class TestExportDeliveryOrder:
    @allure.story("导出出库单")
    @allure.title("出库单页面，导出筛选的出库单记录")
    @allure.description("出库单页面，筛选出库单记录后，导出筛选的出库单记录")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)
        """打开销售管理-打开出库单页面"""
        menu = LoginPage(drivers)
        menu.click_gotomenu("Sales Management", "Delivery Order")
        export = DeliveryOrderPage(drivers)
        # 获取日期
        base = Base(drivers)
        today = base.get_datetime_today()

        export.click_unfold()
        export.input_delivery_date(today, today)
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

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Delivery Order")
        ValueAssert.value_assert_equal(task_id, "testsupervisor")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        export.click_close_export_record()
        export.click_close_delivery_order()


if __name__ == '__main__':
    pytest.main(['SalesManagement_DeliveryOrder.py'])
