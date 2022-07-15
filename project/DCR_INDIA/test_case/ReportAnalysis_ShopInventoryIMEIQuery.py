from libs.common.time_ui import sleep
from project.DCR_INDIA.page_object.Center_Component import LoginPage
from project.DCR_INDIA.page_object.ReportAnalysis_ShopInventoryIMEIQuery import ShopInventoryIMEIQueryPage
from public.base.assert_ui import ValueAssert
import datetime
import logging
from public.base.basics import Base
import pytest
import allure

@allure.feature("报表分析-门店库存IMEI查询")
class TestQueryShopInventoryIMEI:
    @allure.story("查询门店库存IMEI")
    @allure.title("门店库存IMEI页面，查询门店库存IMEI记录列表数据加载")
    @allure.description("门店库存IMEI页面，查询门店库存IMEI记录列表数据加载，断言数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        #user.dcr_login(drivers, "testsupervisor", "dcr123456")
        #get_home_page = user.get_home_page_text()
        #ValueAssert.value_assert_equal("Home Page-Customer", get_home_page)
        base = Base(drivers)
        base.refresh()
        sleep(3.5)
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
        shop_inventory.click_close_shop_inventory_imei()


@allure.feature("报表分析-门店库存IMEI查询")
class TestExportShopInventoryIMEI:
    @allure.story("导出门店库存IMEI")
    @allure.title("门店库存IMEI页面，根据收货日期查询，门店库存IMEI记录，并导出筛选后的数据")
    @allure.description("门店库存IMEI页面，根据收货日期查询，门店库存IMEI记录，并导出筛选后的门店库存IMEI数据，断言导出数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        base = Base(drivers)
        base.refresh()
        sleep(3.5)

        """报表分析-打开门店库存IMEI查询页面"""
        user = LoginPage(drivers)
        user.click_gotomenu("Report Analysis", "Shop Inventory IMEI Query")

        export = ShopInventoryIMEIQueryPage(drivers)
        #获取日期
        base = Base(drivers)
        today = base.get_datetime_today()

        # 点击Unfold展开筛选按钮
        export.click_unfold()
        export.input_inbound_date(today)
        export.click_fold()
        export.click_search()

        #shop_id = export.get_shop_id_text()
        total = export.get_total_text()

        export.assert_total(total)

        # 点击导出功能
        export.click_export()
        export.click_download_more()
        down_status = export.click_export_search()

        #down_status = export.get_download_status_text()
        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        create_date1 = create_date[0:10]
        complete_date = export.get_complete_date_text()
        complete_date1 = complete_date[0:10]
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Shop Inventory IMEI Query")
        ValueAssert.value_assert_equal(task_id, "testsupervisor")
        ValueAssert.value_assert_equal(create_date1, today)
        ValueAssert.value_assert_equal(complete_date1, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        export.click_close_export_record()
        export.click_close_shop_inventory_imei()


if __name__ == '__main__':
    pytest.main(['ReportAnalysis_ShopInventoryIMEIQuery.py'])



