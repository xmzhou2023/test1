from project.DCR.page_object.ReportAnalysis_CustomerSaleReport import CustomerSalesReportPage
from libs.common.connect_sql import *
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert
from libs.common.time_ui import sleep
from public.base.basics import Base
import pytest
import allure
import logging


@allure.feature("报表分析-客户销售报表")
class TestQueryCustomerSalesReport:
    @allure.story("国包用户查看客户销售报表")
    @allure.title("国包用户查看客户销售报表，统计出库数、退货数与实际销售数")
    @allure.description("国包用户查看客户销售报表，统计出库数、退货数与实际销售数")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        """国包账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "BD40344201", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Report Analysis", "Customer Sales Report")

        sales_report = CustomerSalesReportPage(drivers)
        sales_report.input_date("2022-07-15", "2022-07-26")
        sales_report.click_search()

        delivery_total = sales_report.get_delivery_sum_text()
        return_total = sales_report.get_return_sum_text()
        actual_sales = sales_report.get_actual_sales_sum_text()

        #查询国包用户下出库单总数
        user = SQL('DCR', 'test')
        del_result = user.query_db("select count(delivery_code) as sum from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and status=80200001 and delivery_date between '2022-07-15' and '2022-07-26'")
        del_total = del_result[0].get('sum')
        logging.info("打印del_total{}".format(del_total))
        sleep(1)
        #查询BD40344201国包用户下 已退货的总数
        return_result = user.query_db("select count(delivery_code) as sum from t_channel_delivery_ticket  where warehouse_id = '62139' and seller_id = '1596874516539667' and return_status = 1 and delivery_date between '2022-07-15' and '2022-07-26'")
        ret_total = return_result[0].get('sum')
        logging.info("打印ret_total{}".format(ret_total))
        sleep(1)
        #出库单-退货单=实际销售总数
        actualsales = del_total - ret_total
        actualsales1 = int(actualsales)
        ValueAssert.value_assert_equal(delivery_total, del_total)
        ValueAssert.value_assert_equal(return_total, ret_total)
        ValueAssert.value_assert_equal(actual_sales, actualsales1)
        sales_report.click_close_cust_sale_report()


if __name__ == '__main__':
    pytest.main(['ReportAnalysis_CustomerSaleReport.py'])
