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


@allure.feature("报表分析-客户PSI")
class TestExportDistiCustomerPSI:
    @allure.story("导出客户PSI")
    @allure.title("Customer PSI页面，导出按日期查询国包客户PSI列表数据")
    @allure.description("Customer PSI页面，按日期查询国包客户PSI列表数据，并导出")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_export_psi_fixture')
    def test_002_001(self, drivers):
        """筛选国包客户PSI列表数据，导出数据是否正常"""
        user1 = LoginPage(drivers)
        user1.initialize_login(drivers, "lhmadmin", "dcr123456")

        """报表分析-打开客户PSI页面"""
        user1.click_gotomenu("Report Analysis", "Customer PSI")

        export = CustomerPSIPage(drivers)
        # 获取日期
        base = Base(drivers)
        today = base.get_datetime_today()

        # 系统默认选中查询国包PSI数据
        # 点击导出功能
        export.click_export()
        export.click_download_more()
        export.input_task_name("Customer PSI")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()

        operation = export.get_export_operation_text()
        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Customer PSI")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        export.assert_file_time_size(file_size, export_time)
        #export.click_close_export_record()
        #export.click_close_customerPSI()


@allure.feature("报表分析-客户PSI")
class TestQuerSubCustomerPSI:
    @allure.story("查询二代客户PSI")
    @allure.title("Customer PSI页面，按日期查询二代客户PSI列表数据加载")
    @allure.description("Customer PSI页面，按日期查询二代客户PSI列表数据加载，断言数据是否加载正常")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_cust_psi_fixture')
    def test_003_001(self, drivers):
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
    @allure.story("导出二代客户PSI")
    @allure.title("Customer PSI页面，导出按日期查询二代客户PSI列表数据")
    @allure.description("Customer PSI页面，按日期查询二代客户PSI列表数据，并导出。断言导出数据是否正常")
    @allure.severity("normal")  # 分别为5种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_export_psi_fixture')
    def test_004_001(self, drivers):
        """根据日期筛选二代客户PSI列表数据，导出数据是否正常"""
        user3 = LoginPage(drivers)
        user3.initialize_login(drivers, "lhmadmin", "dcr123456")

        """报表分析-打开客户PSI页面"""
        user3.click_gotomenu("Report Analysis", "Customer PSI")

        export = CustomerPSIPage(drivers)
        # 获取日期
        base = Base(drivers)
        today = base.get_datetime_today()
        # 查询二代PSI数据
        export.click_sub_dealer()

        #点击导出功能
        export.click_export()
        export.click_download_more()
        export.input_task_name("Customer PSI")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()

        user_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        create_date1 = create_date[0:10]
        complete_date = export.get_complete_date_text()
        complete_date1 = complete_date[0:10]
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Customer PSI")
        ValueAssert.value_assert_equal(user_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date1, today)
        ValueAssert.value_assert_equal(complete_date1, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        #export.click_close_export_record()
        #export.click_close_customerPSI()


if __name__ == '__main__':
    pytest.main(['ReportAnalysis_CustomerPSI.py'])
