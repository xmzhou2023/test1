from project.DCR.page_object.menu import MenuPage
from project.DCR.page_object.SalesManagement_ShopSalesQuery import ShopSaleQueryPage
import logging
from project.DCR.page_object.login import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert
from libs.common.time_ui import sleep
import datetime
import pytest
import allure

@allure.feature("销售管理-门店")
class TestQueryShopSalesQuery():
    @allure.story("查询")
    @allure.title("门店销售查询页面，查询门店销售查询列表数据加载")
    @allure.description("考勤记录页面，查询门店销售查询列表数据加载，断言数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.dcr_login(drivers, "lhmadmin", "dcr123456")
        sleep(5)

        # """刷新页面"""
        # base = Base(drivers)
        # base.refresh()
        # sleep(3.5)
        """打开销售管理-打开门店销售查询页面"""
        menu = MenuPage(drivers)
        menu.click_gotomenu("Sales Management", "Shop Sales Query")
        sleep(4)

        """查看Shop Sales Query门店销量上报 列表数据加载是否正常"""
        shop_sales = ShopSaleQueryPage(drivers)
        shop_sales.input_upload_start_date("2022-06-01")
        shop_sales.click_search()

        shop_id = shop_sales.get_shop_id_text()
        shop_name = shop_sales.get_shop_name_text()
        status = shop_sales.get_status_text()
        sales_date = shop_sales.get_sales_date_text()
        public_id = shop_sales.get_public_id_text()
        total = shop_sales.get_total_text()
        total1 = total[6:12]
        """Shop Sales Query页面，增加断言 对比列表字段与分页总条数是否有数据"""
        ValueAssert.value_assert_IsNoneNot(shop_id)
        ValueAssert.value_assert_IsNoneNot(status)
        ValueAssert.value_assert_IsNoneNot(shop_name)
        ValueAssert.value_assert_IsNoneNot(sales_date)
        ValueAssert.value_assert_IsNoneNot(public_id)
        if int(total1) > 1000:
            logging.info("查看Shop Sales Query列表，加载所有数据正常，分页总条数Total：{}".format(total1))
        else:
            logging.info("查看Shop Sales Query列表，未加载所有数据失败，分页总条数Total：{}".format(total1))
        sleep(2)


    @allure.story("查询")
    @allure.title("门店销售查询页面，按销售开始与结束日期筛选，门店销售查询列表记录数据")
    @allure.description("门店销售查询页面，按销售开始与结束日期筛选，门店销售查询列表记录数据，断言筛选后数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_002(self, drivers):
        shop_sale = ShopSaleQueryPage(drivers)
        """首先按日期筛选门店销量数据"""
        shop_sale.input_upload_start_date("2022-06-01")
        shop_sale.click_search()
        """获取筛选后的列表字段文本"""
        shop_id = shop_sale.get_shop_id_text()
        shop_name = shop_sale.get_shop_name_text()
        status = shop_sale.get_status_text()
        sales_date = shop_sale.get_sales_date_text()
        public_id = shop_sale.get_public_id_text()
        """然后根据Shop ID条件筛选门店销量数据"""
        shop_sale.input_query_shop_id(shop_id)
        shop_sale.click_search()

        """获取按Shop ID条件筛选后的数据进行断言"""
        shopid = shop_sale.get_shop_id_text()
        shop_name2 = shop_sale.get_shop_name_text()
        status2 = shop_sale.get_status_text()
        sales_date2 = shop_sale.get_sales_date_text()
        public_id2 = shop_sale.get_public_id_text()
        total = shop_sale.get_total_text()
        total1 = total[6:7]

        """Shop Sales Query页面，增加断言 对比列表字段与分页总条数是否有数据"""
        ValueAssert.value_assert_equal(shop_id, shopid)
        ValueAssert.value_assert_equal(status, status2)
        ValueAssert.value_assert_equal(shop_name, shop_name2)
        ValueAssert.value_assert_equal(sales_date, sales_date2)
        ValueAssert.value_assert_equal(public_id, public_id2)
        if int(total1) > 0:
            logging.info("Shop Sales Query列表，按Shop ID筛选，加载筛选后的数据正常，分页总条数Total：{}".format(total1))
        else:
            logging.info("查看Shop Sales Query列表，未加载筛选后的数据失败，分页总条数Total：{}".format(total1))
        shop_sale.click_reset()
        shop_sale.click_close_shop_sales_query()
        sleep(1)


@allure.feature("销售管理-门店销售查询")
class TestExportShopSalesQuery():
    @allure.story("导出")
    @allure.title("门店销售查询页面，按销售开始与结束日期查询 门店销售查询记录，并导出筛选后的数据")
    @allure.description("门店销售查询页面，按销售开始与结束日期查询 门店销售查询记录，并导出筛选后的数据")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)

        """打开销售管理-打开门店销售查询页面"""
        menu = MenuPage(drivers)
        menu.click_gotomenu("Sales Management", "Shop Sales Query")
        sleep(4)

        """实例化对象类"""
        export = ShopSaleQueryPage(drivers)
        today = datetime.date.today()
        totay1 = str(today)
        export.input_upload_start_date("2022-06-01")
        export.click_search()
        shop_id = export.get_shop_id_text()
        export.input_query_shop_id(shop_id)
        export.click_search()
        # 筛选销售日期后，点击导出功能
        export.click_export()
        sleep(1.5)

        export.click_download_icon()
        export.click_more()
        sleep(3)
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
        ValueAssert.value_assert_equal(task_name, "Shop Sales Query")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date1, totay1)
        ValueAssert.value_assert_equal(complete_date1, totay1)
        ValueAssert.value_assert_equal(operation, "Download")
        if int(file_size1) > 0:
            logging.info("Shop Sales Query导出成功，File Size 导出文件大于0KB:{}".format(file_size1))
        else:
            logging.info("Shop Sales Query导出成功，File Size 导出文件小于0KB:{}:{}".format(file_size1))

        if int(export_time1) > 0:
            logging.info("Shop Sales Query导出成功，Export Time(s)导出时间大于0s:{}".format(export_time1))
        else:
            logging.info("Shop Sales Query导出失败，Export Time(s)导出时间小于0s:{}".format(export_time1))
        #export.click_close_export_record()
        #export.click_close_shop_sales_query()
        sleep(1)


if __name__ == '__main__':
    pytest.main(['SalesManagement_ShopSalesQuery.py'])
