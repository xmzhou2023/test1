from libs.common.time_ui import sleep
from project.DCR_GLOBAL.page_object.Center_Component import DCRLoginPage
from project.DCR_GLOBAL.page_object.SalesManagement_ShopSalesQuery import ShopSaleQueryPage
from public.base.assert_ui import ValueAssert
import datetime
import logging
from public.base.basics import Base
import pytest
import allure

@allure.feature("销售管理-门店销售查询")
class TestQueryShopSalesQuery:
    @allure.story("查询门店销量")
    @allure.title("门店销售查询页面，查询门店销售查询列表数据加载")
    @allure.description("考勤记录页面，查询门店销售查询列表数据加载，断言数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        base = Base(drivers)
        base.refresh()
        sleep(3.5)

        user = DCRLoginPage(drivers)
        #user.dcr_login(drivers, "testsupervisor", "dcr123456")

        """打开销售管理-打开门店销售查询页面"""
        user.click_gotomenu("Sales Management", "Shop Sales Query")

        """查看Shop Sales Query门店销量上报 列表数据加载是否正常"""
        shop_sales = ShopSaleQueryPage(drivers)

        shop_id = shop_sales.get_shop_id_text()
        shop_name = shop_sales.get_shop_name_text()
        status = shop_sales.get_status_text()
        sales_date = shop_sales.get_sales_date_text()
        public_id = shop_sales.get_public_id_text()
        total = shop_sales.get_total_text()
        total1 = total[6:]
        """Shop Sales Query页面，增加断言 对比列表字段与分页总条数是否有数据"""
        ValueAssert.value_assert_IsNoneNot(shop_id)
        ValueAssert.value_assert_IsNoneNot(status)
        ValueAssert.value_assert_IsNoneNot(shop_name)
        ValueAssert.value_assert_IsNoneNot(sales_date)
        ValueAssert.value_assert_IsNoneNot(public_id)
        shop_sales.assert_total2(total1)
        #shop_sales.click_close_shop_sales_query()


@allure.feature("销售管理-门店销售查询")
class TestExportShopSalesQuery:
    @allure.story("导出查询门店销量")
    @allure.title("门店销售查询页面，按销售开始与结束日期查询 门店销售查询记录，并导出筛选后的数据")
    @allure.description("门店销售查询页面，按销售开始与结束日期查询 门店销售查询记录，并导出筛选后的数据")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        # """刷新页面"""
        # base = Base(drivers)
        # base.refresh()
        # sleep(3.5)
        #
        # """打开销售管理-打开门店销售查询页面"""
        # menu = DCRLoginPage(drivers)
        # menu.click_gotomenu("Sales Management", "Shop Sales Query")

        """实例化对象类"""
        export = ShopSaleQueryPage(drivers)
        base = Base(drivers)
        today = base.get_datetime_today()

        export.click_unfold()
        export.input_sales_date_date(today, today)
        export.click_fold()
        export.click_search()

        total = export.get_total_text()
        total1 = total[6:]
        """Shop Sales Query页面，增加断言 对比列表字段与分页总条数是否有数据"""
        export.assert_total(total1)

        #筛选销售日期后，点击导出功能
        export.click_export()
        export.click_download_more()
        down_status = export.click_export_search()

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
        ValueAssert.value_assert_equal(task_name, "Shop Sales Query")
        ValueAssert.value_assert_equal(task_id, "testsupervisor")
        ValueAssert.value_assert_equal(create_date1, today)
        ValueAssert.value_assert_equal(complete_date1, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size1, export_time1)

        export.click_close_export_record()
        export.click_close_shop_sales_query()


if __name__ == '__main__':
    pytest.main(['SalesManagement_ShopSalesQuery.py'])
