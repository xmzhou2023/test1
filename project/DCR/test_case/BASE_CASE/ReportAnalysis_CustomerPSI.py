from project.DCR.page_object.ReportAnalysis_CustomerPSI import CustomerPSIPage
import logging
from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert
from libs.common.time_ui import sleep
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_cust_psi_fixture(drivers):
    yield
    close = CustomerPSIPage(drivers)
    close.click_close_customerPSI()

@pytest.fixture(scope='function')
def function_export_psi_fixture(drivers):
    yield
    close = CustomerPSIPage(drivers)
    close.click_close_export_record()
    close.click_close_customerPSI()


@allure.feature("报表分析-客户PSI")
class TestQueryDistiCustomerPSI:
    @allure.story("查询客户PSI")
    @allure.title("Customer PSI页面，按日期查询国包客户PSI列表数据加载")
    @allure.description("Customer PSI页面，按日期查询国包客户PSI列表数据加载，断言数据是否加载正常")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_cust_psi_fixture')
    def test_001_001(self, drivers):
        """筛选国包客户PSI列表数据，是否加载正常"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """报表分析-打开客户PSI页面"""
        user.click_gotomenu("Report Analysis", "Customer PSI")
        query_psi = CustomerPSIPage(drivers)
        #默认筛选国包数据
        region2_text = query_psi.get_sales_region2_text()
        region3_text = query_psi.get_sales_region3_text()
        brand_text = query_psi.get_brand_text()
        total = query_psi.get_total_text()
        """根据日期筛选Distributor Customer PSI数据后，断言是否查询到数据"""
        ValueAssert.value_assert_IsNoneNot(region2_text)
        ValueAssert.value_assert_IsNoneNot(region3_text)
        ValueAssert.value_assert_IsNoneNot(brand_text)
        query_psi.assert_total(total)
        #query_psi.click_close_customerPSI()


    @allure.story("查询客户PSI")
    @allure.title("Customer PSI页面，按日期查询二代客户PSI列表数据加载")
    @allure.description("Customer PSI页面，按日期查询二代客户PSI列表数据加载，断言数据是否加载正常")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_cust_psi_fixture')
    def test_001_002(self, drivers):
        """根据日期筛选二代客户PSI列表数据，是否加载正常"""
        user2 = LoginPage(drivers)
        user2.initialize_login(drivers, "lhmadmin", "dcr123456")
        """报表分析-打开客户PSI页面"""
        user2.click_gotomenu("Report Analysis", "Customer PSI")
        psi = CustomerPSIPage(drivers)
        #点击Sub-dealer按钮筛选二代数据
        psi.click_sub_dealer()
        psi.click_search()
        region2_text = psi.get_sales_region2_text()
        region3_text = psi.get_sales_region3_text()
        brand_text = psi.get_brand_text()
        total = psi.get_total_text()
        """根据日期筛选Distributor Customer PSI数据后，断言是否查询到数据"""
        ValueAssert.value_assert_IsNoneNot(region2_text)
        ValueAssert.value_assert_IsNoneNot(region3_text)
        ValueAssert.value_assert_IsNoneNot(brand_text)
        psi.assert_total(total)
        #psi.click_close_customerPSI()


@allure.feature("报表分析-客户PSI")
class TestExportSubCustomerPSI:
    @allure.feature("报表分析-客户PSI")
    class TestExportDistiCustomerPSI:
        @allure.story("导出客户PSI")
        @allure.title("Customer PSI页面，导出按日期查询国包客户PSI列表数据")
        @allure.description("Customer PSI页面，按日期查询国包客户PSI列表数据，并导出")
        @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
        @pytest.mark.smoke  # 用例标记
        @pytest.mark.usefixtures('function_export_psi_fixture')
        def test_002_001(self, drivers):
            """筛选国包客户PSI列表数据，导出数据是否正常"""
            user1 = LoginPage(drivers)
            user1.initialize_login(drivers, "lhmadmin", "dcr123456")
            """报表分析-打开客户PSI页面"""
            user1.click_gotomenu("Report Analysis", "Customer PSI")
            export = CustomerPSIPage(drivers)
            # 获取日期
            today = Base(drivers).get_datetime_today()
            last_date = export.get_last_day(2)
            export.customer_psi_start_date_query(last_date)
            export.click_search()
            # 系统默认选中查询国包PSI数据
            # 点击导出功能
            export.click_export()
            export.click_download_more()
            """进入导出记录页面，根据任务名称与创建日期条件筛选导出的任务记录"""
            export.input_task_name("Customer PSI")
            export.export_record_create_date_query(today)
            """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
            down_status = export.click_export_search()
            file_size = export.get_file_size_text()
            export_time = export.get_export_time_text()
            export.assert_file_time_size(file_size, export_time)
            export.assert_customer_psi_field('Download Status', down_status)
            export.assert_customer_psi_field('Task Name', 'Customer PSI')
            export.assert_customer_psi_field('User ID', 'lhmadmin')
            export.assert_customer_psi_field('Create Date', today)
            export.assert_customer_psi_field('Completed Date', today)
            export.assert_customer_psi_field('Operation', 'Download')
            # export.click_close_export_record()
            # export.click_close_customerPSI()


    @allure.story("导出二代客户PSI")
    @allure.title("Customer PSI页面，导出按日期查询二代客户PSI列表数据")
    @allure.description("Customer PSI页面，按日期查询二代客户PSI列表数据，并导出。断言导出数据是否正常")
    @allure.severity("normal")  # 分别为5种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_export_psi_fixture')
    def test_002_002(self, drivers):
        """根据日期筛选二代客户PSI列表数据，导出数据是否正常"""
        user3 = LoginPage(drivers)
        user3.initialize_login(drivers, "lhmadmin", "dcr123456")
        """报表分析-打开客户PSI页面"""
        user3.click_gotomenu("Report Analysis", "Customer PSI")
        export = CustomerPSIPage(drivers)
        # 获取日期
        today = Base(drivers).get_datetime_today()
        last_date = export.get_last_day(2)
        export.customer_psi_start_date_query(last_date)
        # 查询二代PSI数据
        export.click_sub_dealer()
        export.click_search()
        #点击导出功能
        export.click_export()
        export.click_download_more()
        """进入导出记录页面，根据任务名称与创建日期条件筛选导出的任务记录"""
        export.input_task_name("Customer PSI")
        export.export_record_create_date_query(today)
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = export.click_export_search()
        file_size = export.get_file_size_text()
        export_time = export.get_export_time_text()
        export.assert_file_time_size(file_size, export_time)
        export.assert_customer_psi_field('Download Status', down_status)
        export.assert_customer_psi_field('Task Name', 'Customer PSI')
        export.assert_customer_psi_field('User ID', 'lhmadmin')
        export.assert_customer_psi_field('Create Date', today)
        export.assert_customer_psi_field('Completed Date', today)
        export.assert_customer_psi_field('Operation', 'Download')
        #export.click_close_export_record()
        #export.click_close_customerPSI()


if __name__ == '__main__':
    pytest.main(['ReportAnalysis_CustomerPSI.py'])
