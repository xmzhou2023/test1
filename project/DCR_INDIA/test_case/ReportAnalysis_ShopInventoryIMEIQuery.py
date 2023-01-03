from libs.common.time_ui import sleep
from project.DCR_INDIA.page_object.Center_Component import LoginPage
from project.DCR_INDIA.page_object.ReportAnalysis_ShopInventoryIMEIQuery import ShopInventoryIMEIQueryPage
from public.base.assert_ui import ValueAssert
import datetime
import logging
from public.base.basics import Base
import pytest
import allure

@pytest.fixture(scope='function')
def function_export_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    for i in range(2):
        get_menu_class = menu.get_open_menu_class()
        class_value = "tags-view-item router-link-exact-active router-link-active active"
        if class_value == str(get_menu_class):
            menu.click_close_open_menu()
            sleep(1)

@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@allure.feature("报表分析-门店库存IMEI查询")
class TestQueryShopInventoryIMEI:
    @allure.story("查询门店库存IMEI")
    @allure.title("门店库存IMEI页面，查询门店库存IMEI记录列表数据加载")
    @allure.description("门店库存IMEI页面，查询门店库存IMEI记录列表数据加载，断言数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        #user.dcr_login(drivers, "testsupervisor", "dcr123456")
        Base(drivers).refresh()
        sleep(2)
        user = LoginPage(drivers)
        """报表分析-打开门店库存IMEI查询页面"""
        user.click_gotomenu("Report Analysis", "Shop Inventory IMEI Query")
        """查看Shop Inventory IMEI Query 列表所有数据加载是否正常"""
        shop_inventory = ShopInventoryIMEIQueryPage(drivers)
        #获取列表属性文本内容
        shop_id = shop_inventory.get_shop_id_text()
        shop_name = shop_inventory.get_shop_name_text()
        brand = shop_inventory.get_brand_text()
        series = shop_inventory.get_series_text()
        model = shop_inventory.get_model_text()
        total = shop_inventory.get_total_text()
        #断言筛选前获取列表文本内容，然后筛选操作后，断言比较列表文本内容是否一致
        ValueAssert.value_assert_IsNoneNot(shop_id)
        ValueAssert.value_assert_IsNoneNot(shop_name)
        ValueAssert.value_assert_IsNoneNot(brand)
        ValueAssert.value_assert_IsNoneNot(series)
        ValueAssert.value_assert_IsNoneNot(model)
        shop_inventory.assert_total(total)


@allure.feature("报表分析-门店库存IMEI查询")
class TestExportShopInventoryIMEI:
    @allure.story("导出门店库存IMEI")
    @allure.title("门店库存IMEI页面，根据收货日期查询，门店库存IMEI记录，并导出筛选后的数据")
    @allure.description("门店库存IMEI页面，根据收货日期查询，门店库存IMEI记录，并导出筛选后的门店库存IMEI数据，断言导出数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal
    @pytest.mark.usefixtures('function_export_fixture')
    def test_002_001(self, drivers):
        Base(drivers).refresh()
        sleep(2)
        """报表分析-打开门店库存IMEI查询页面"""
        user = LoginPage(drivers)
        user.click_gotomenu("Report Analysis", "Shop Inventory IMEI Query")
        export = ShopInventoryIMEIQueryPage(drivers)
        #获取日期
        base = Base(drivers)
        today = base.get_datetime_today()
        last_date = export.get_last_day(1)
        # 点击Unfold展开筛选按钮
        export.click_unfold()
        export.input_inbound_date(last_date)
        export.click_fold()
        export.click_search()
        total = export.get_total_text()
        export.assert_total(total)
        # 点击导出功能
        export.click_export()
        export.click_download_more()
        export.input_task_name('Shop Inventory IMEI Query')
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = export.click_export_search()
        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()
        """断言导出记录列表字段内容是否正确"""
        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Shop Inventory IMEI Query")
        ValueAssert.value_assert_equal(task_id, "testsupervisor")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)


if __name__ == '__main__':
    pytest.main(['ReportAnalysis_ShopInventoryIMEIQuery.py'])



