from project.DCR.page_object.menu import MenuPage
from project.DCR.page_object.ReportAnalysis_ShopInventoryIMEIQuery import ShopInventoryIMEIQueryPage
import logging
from project.DCR.page_object.login import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert
from libs.common.time_ui import sleep
import datetime
import pytest
import allure


@allure.feature("报表分析-门店库存IMEI查询")
class TestQueryShopInventoryIMEI():
    @allure.story("查询")
    @allure.title("门店库存IMEI页面，查询门店库存IMEI记录列表数据加载")
    @allure.description("门店库存IMEI页面，查询门店库存IMEI记录列表数据加载，断言数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.dcr_login(drivers, "lhmadmin", "dcr123456")
        sleep(5)

        # """刷新页面"""
        # base = Base(drivers)
        # base.refresh()
        # sleep(3.5)

        """报表分析-打开门店库存IMEI查询页面"""
        menu = MenuPage(drivers)
        menu.click_gotomenu("Report Analysis", "Shop Inventory IMEI Query")
        sleep(8)

        """查看Shop Inventory IMEI Query 列表所有数据加载是否正常"""
        shop_inventory = ShopInventoryIMEIQueryPage(drivers)

        #获取列表属性文本内容
        total = shop_inventory.get_total_text()
        total1 = total[6:12]
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

        if int(total1) > 1000:
            logging.info("查看Shop Inventory IMEI Query列表，加载所有数据正常，分页总条数Total：{}".format(total1))
        else:
            logging.info("查看Shop Inventory IMEI Query列表，加载所有数据正常，分页总条数Total：{}".format(total1))
        sleep(2)


    @allure.story("查询")
    @allure.title("门店库存IMEI页面，根据Shop ID查询门店库存IMEI列表记录")
    @allure.description("门店库存IMEI页面，根据Shop ID查询门店库存IMEI列表记录，断言筛选门店库存IMEI数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_002(self, drivers):
        """考勤管理-打开考勤记录页面"""
        """查看Shop Inventory IMEI Query 列表数据加载是否正常"""
        shop_inventory = ShopInventoryIMEIQueryPage(drivers)
        # 筛选前，获取列表属性文本内容
        shop_id_text = shop_inventory.get_shop_id_text()
        shop_name_text = shop_inventory.get_shop_name_text()
        brand_text = shop_inventory.get_brand_text()
        series_text = shop_inventory.get_series_text()
        model_text = shop_inventory.get_model_text()
        #点击Unfold展开筛选按钮
        #shop_inventory.click_unfold()
        shop_inventory.input_shop_id(shop_id_text)
        #shop_inventory.input_inbound_date(today1)
        shop_inventory.click_search()
        #shop_inventory.click_fold()

        #筛选后，获取列表属性文本内容
        total = shop_inventory.get_total_text()
        total1 = total[6:7]
        shop_id = shop_inventory.get_shop_id_text()
        shop_name = shop_inventory.get_shop_name_text()
        brand = shop_inventory.get_brand_text()
        series = shop_inventory.get_series_text()
        model = shop_inventory.get_model_text()

        #断言筛选前获取列表文本内容，然后筛选操作后，断言比较列表文本内容是否一致
        ValueAssert.value_assert_equal(shop_id_text, shop_id)
        ValueAssert.value_assert_equal(shop_name_text, shop_name)
        ValueAssert.value_assert_equal(brand_text, brand)
        ValueAssert.value_assert_equal(series_text, series)
        ValueAssert.value_assert_In(model_text, model)

        if int(total1) >= 1:
            logging.info("查看Shop Inventory IMEI Query列表，加载筛选的数据正常，分页总条数Total：{}".format(total1))
        else:
            logging.info("查看Shop Inventory IMEI Query列表，加载筛选的数据正常，分页总条数Total：{}".format(total1))
        sleep(1)
        shop_inventory.click_reset()
        shop_inventory.click_close_shop_inventory_imei()
        sleep(2)


@allure.feature("报表分析-门店库存IMEI查询")
class TestExportShopInventoryIMEI():
    @allure.story("导出")
    @allure.title("门店库存IMEI页面，根据收货日期查询，门店库存IMEI记录，并导出筛选后的数据")
    @allure.description("门店库存IMEI页面，根据收货日期查询，门店库存IMEI记录，并导出筛选后的门店库存IMEI数据，断言导出数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)

        """报表分析-打开门店库存IMEI查询页面"""
        menu = MenuPage(drivers)
        menu.click_gotomenu("Report Analysis", "Shop Inventory IMEI Query")
        sleep(8)

        export = ShopInventoryIMEIQueryPage(drivers)
        #获取日期
        today = datetime.date.today()
        today1 = str(today)
        # 筛选前，获取列表属性文本内容
        shop_id_text = export.get_shop_id_text()
        export.input_shop_id(shop_id_text)
        export.click_search()

        # 点击导出功能
        export.click_export()
        sleep(3)
        export.click_download_icon()
        export.click_more()
        sleep(5)
        export.click_export_search()

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
        ValueAssert.value_assert_equal(task_name, "Shop Inventory IMEI Query")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date1, today1)
        ValueAssert.value_assert_equal(complete_date1, today1)
        ValueAssert.value_assert_equal(operation, "Download")
        if int(file_size1) > 0:
            logging.info("Shop Inventory IMEI Query导出成功，File Size 导出文件大于1KB:{}".format(file_size1))
        else:
            logging.info("Shop Inventory IMEI Query导出失败，File Size 导出文件小于1KB:{}".format(file_size1))

        if int(export_time1) > 0:
            logging.info("Shop Inventory IMEI Query导出成功，Export Time(s)导出时间大于0s:{}".format(export_time1))
        else:
            logging.info("Shop Inventory IMEI Query导出失败，Export Time(s)导出时间小于0s:{}".format(export_time1))
        #export.click_close_export_record()
        #export.click_close_shop_inventory_imei()
        sleep(1)


if __name__ == '__main__':
    pytest.main(['ReportAnalysis_ShopInventoryIMEIQuery.py'])



