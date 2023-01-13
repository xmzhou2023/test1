from project.DCR.page_object.ReportAnalysis_ShopInventoryIMEIQuery import ShopInventoryIMEIQueryPage
import logging
from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert
from libs.common.time_ui import sleep
import datetime
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_query_fixture(drivers):
    yield
    close = ShopInventoryIMEIQueryPage(drivers)
    close.click_close_shop_inventory_imei()

@pytest.fixture(scope='function')
def function_report_fixture(drivers):
    yield
    close = ShopInventoryIMEIQueryPage(drivers)
    close.click_close_export_record()
    close.click_close_shop_inventory_imei()


@allure.feature("报表分析-门店库存IMEI查询")
class TestQueryShopInventoryIMEI:
    @allure.story("查询门店库存IMEI")
    @allure.title("门店库存IMEI页面，查询门店库存IMEI记录列表数据加载")
    @allure.description("门店库存IMEI页面，查询门店库存IMEI记录列表数据加载，断言数据加载正常")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_query_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """报表分析-打开门店库存IMEI查询页面"""
        user.click_gotomenu("Report Analysis", "Shop Inventory IMEI Query")
        """查看Shop Inventory IMEI Query 列表所有数据加载是否正常"""
        shop_inventory = ShopInventoryIMEIQueryPage(drivers)
        #获取列表属性文本内容
        total = shop_inventory.get_total_text()
        shop_id = shop_inventory.get_shop_id_text()
        shop_name = shop_inventory.get_shop_name_text()
        brand = shop_inventory.get_brand_text()
        series = shop_inventory.get_series_text()
        model = shop_inventory.get_model_text()
        #断言筛选前获取列表文本内容，然后筛选操作后，断言比较列表文本内容是否一致
        ValueAssert.value_assert_IsNoneNot(shop_id)
        ValueAssert.value_assert_IsNoneNot(shop_name)
        ValueAssert.value_assert_IsNoneNot(brand)
        ValueAssert.value_assert_IsNoneNot(series)
        ValueAssert.value_assert_IsNoneNot(model)
        shop_inventory.assert_total(total)
        #shop_inventory.click_close_shop_inventory_imei()


@allure.feature("报表分析-门店库存IMEI查询")
class TestExportShopInventoryIMEI:
    @allure.story("导出门店库存IMEI")
    @allure.title("门店库存IMEI页面，根据收货日期查询，门店库存IMEI记录，并导出筛选后的数据")
    @allure.description("门店库存IMEI页面，根据收货日期查询，门店库存IMEI记录，并导出筛选后的门店库存IMEI数据，断言导出数据加载正常")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_report_fixture')
    def test_002_001(self, drivers):
        """查看Shop Inventory IMEI Query 列表数据加载是否正常"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """报表分析-打开门店库存IMEI查询页面"""
        user.click_gotomenu("Report Analysis", "Shop Inventory IMEI Query")
        export = ShopInventoryIMEIQueryPage(drivers)
        # 获取日期
        today = Base(drivers).get_datetime_today()
        """获取当天日期之前13天的日期"""
        last_date = Base(drivers).get_last_day(13)
        #点击Unfold展开筛选按钮
        export.click_unfold()
        export.input_inbound_date(last_date)
        export.click_fold()
        export.click_search()
        #筛选后，获取列表属性文本内容
        total = export.get_total_text()
        export.assert_total2(total)

        # 点击导出功能
        export.click_export()
        export.click_download_more()
        """进入导出记录页面，根据任务名称与创建日期条件筛选导出的任务记录"""
        export.input_task_name("Shop Inventory IMEI Query")
        export.export_record_create_date_query(today)
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = export.click_export_search()
        #task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        #task_id = export.get_task_user_id_text()
        #create_date = export.get_create_date_text()
        #complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        # operation = export.get_export_operation_text()
        # ValueAssert.value_assert_equal(down_status, "COMPLETE")
        # ValueAssert.value_assert_equal(task_name, "Shop Inventory IMEI Query")
        # ValueAssert.value_assert_equal(task_id, "lhmadmin")
        # ValueAssert.value_assert_equal(create_date, today)
        # ValueAssert.value_assert_equal(complete_date, today)
        # ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        export.assert_shop_inventory_imei_field('Download Status', down_status)
        export.assert_shop_inventory_imei_field('Task Name', 'Shop Inventory IMEI Query')
        export.assert_shop_inventory_imei_field('User ID', 'lhmadmin')
        export.assert_shop_inventory_imei_field('Create Date', today)
        export.assert_shop_inventory_imei_field('Completed Date', today)
        export.assert_shop_inventory_imei_field('Operation', 'Download')
        # export.click_close_export_record()
        # export.click_close_shop_inventory_imei()


if __name__ == '__main__':
    pytest.main(['ReportAnalysis_ShopInventoryIMEIQuery.py'])



