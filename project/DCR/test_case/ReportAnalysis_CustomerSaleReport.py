from project.DCR.page_object.ReportAnalysis_CustomerSaleReport import CustomerSalesReportPage
from libs.common.connect_sql import *
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert
from libs.common.time_ui import sleep
import pytest
import allure


@allure.feature("报表分析-客户销售报表")
class TestQueryCustomerSalesReport:
    @allure.story("查询")
    @allure.title("国包用户查看客户销售报表，统计出库数、退货数与实际销售数")
    @allure.description("国包用户查看客户销售报表，统计出库数、退货数与实际销售数")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        """国包账号登录"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "BD40344201", "dcr123456")
        sleep(6)

        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Report Analysis", "Customer Sales Report")
        sleep(6)

        sales_report = CustomerSalesReportPage(drivers)
        sales_report.input_date("2022-05-01", "2022-06-06")
        sales_report.click_search()

        delivery_total = sales_report.get_delivery_sum_text()
        return_total = sales_report.get_return_sum_text()
        actual_sales = sales_report.get_actual_sales_sum_text()

        #查询国包用户下出库单总数
        user = SQL('DCR', 'test')
        del_result = user.query_db("select count(delivery_code) as sum from t_channel_delivery_ticket  where warehouse_id='62139' and seller_id='1596874516539667' and status=80200001 and delivery_date between '2022-05-01' and '2022-06-06'")
        de_total = del_result[0].get('sum')

        #查询BD40344201国包用户下 已退货的总数
        return_result = user.query_db("select count(delivery_code) as sum from t_channel_delivery_ticket  where warehouse_id = '62139' and seller_id = '1596874516539667' and return_status = 1 and delivery_date between '2022-05-01' and '2022-06-06'")
        re_total = return_result[0].get('sum')

        actualsales = de_total - re_total
        ValueAssert.value_assert_equal(int(delivery_total), de_total)
        ValueAssert.value_assert_equal(int(return_total), re_total)
        ValueAssert.value_assert_equal(int(actual_sales), actualsales)


if __name__ == '__main__':
    pytest.main(['ReportAnalysis_CustomerSaleReport.py'])
