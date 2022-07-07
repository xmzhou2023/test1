from project.DCR.page_object.SalesManagement_DeliveryOrder import DeliveryOrderPage
from project.DCR.page_object.menu import MenuPage
import logging
from project.DCR.page_object.login import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert
from libs.common.time_ui import sleep
import datetime
import pytest
import allure


@allure.feature("销售管理-出库单")
class TestQueryDeliveryOrder():
    @allure.story("查询")
    @allure.title("出库单页面，查询出库单列表加载数据")
    @allure.description("出库单页面，查询出库单列表加载数据正常，断言查询的出库单数据是否加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.dcr_login(drivers, "lhmadmin", "dcr123456")
        sleep(5)

        # """刷新页面"""
        # base = Base(drivers)
        # base.refresh()
        # sleep(3.5)
        """打开销售管理-打开出库单页面"""
        menu = MenuPage(drivers)
        menu.click_gotomenu("Sales Management", "Delivery Order")
        sleep(9)

        list = DeliveryOrderPage(drivers)
        sale_order = list.text_sales_order
        deli_order = list.text_delivery_order()
        deli_date = list.get_delivery_date_text()
        status = list.text_delivery_Status()

        total = list.get_total_text()
        total1 = total[6:8]
        ValueAssert.value_assert_IsNoneNot(sale_order)
        ValueAssert.value_assert_IsNoneNot(deli_order)
        ValueAssert.value_assert_IsNoneNot(deli_date)
        ValueAssert.value_assert_IsNoneNot(status)
        if int(total1) > 1:
            logging.info("查看Delivery Order列表，加载数据正常，分页总记录数：{}".format(total1))
        else:
            logging.info("查看Delivery Order列表，加载数据失败，分页总记录数：{}".format(total1))
        list.click_close_delivery_order()
        sleep(1)


@allure.feature("销售管理-出库单")
class TestExportDeliveryOrder():
    @allure.story("导出")
    @allure.title("出库单页面，导出筛选的出库单记录")
    @allure.description("出库单页面，筛选出库单记录后，导出筛选的出库单记录")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)
        """打开销售管理-打开出库单页面"""
        menu = MenuPage(drivers)
        menu.click_gotomenu("Sales Management", "Delivery Order")
        sleep(10)

        export = DeliveryOrderPage(drivers)
        # 获取日期
        today = datetime.date.today()
        today1 = str(today)

        export.click_unfold()
        export.input_delivery_date(today1, today1)
        export.click_status_input_box()
        export.click_fold()
        export.click_search()
        #筛选出库单后，点击导出功能
        export.click_export()
        sleep(2)
        export.click_download_icon()
        export.click_more()
        sleep(5)
        export.click_export_search()
        sleep(3)

        down_status = export.get_download_status_text()
        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        file_size1 = file_size[0:1]
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        create_date1 = create_date[0:10]
        complete_date = export.get_complete_date_text()
        complete_date1 = complete_date[0:10]
        export_time = export.get_export_time_text()
        export_time1 = export_time[0:1]
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Delivery Order")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date1, today1)
        ValueAssert.value_assert_equal(complete_date1, today1)
        ValueAssert.value_assert_equal(operation, "Download")
        if int(file_size1) > 0:
            logging.info("Delivery Order导出成功，File Size 导出文件大于1KB:{}".format(file_size1))
        else:
            logging.info("Delivery Order导出失败，File Size 导出文件小于1KB:{}".format(file_size1))

        if int(export_time1) > 0:
            logging.info("Delivery Order导出成功，Export Time(s)导出时间大于0s:{}".format(export_time1))
        else:
            logging.info("Delivery Order导出失败，Export Time(s)导出时间小于0s:{}".format(export_time1))
        #export.click_close_export_record()
        #export.click_close_delivery_order()
        sleep(1)


if __name__ == '__main__':
    pytest.main(['SalesManagement_DeliveryOrder.py'])
