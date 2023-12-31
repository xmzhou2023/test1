from libs.common.time_ui import sleep
from project.DCR_INDIA.page_object.Center_Component import LoginPage
from project.DCR_INDIA.page_object.ReportAnalysis_CustomerPSI import CustomerPSIPage
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

@allure.feature("报表分析-客户PSI")
class TestQueryCustomerPSI:
    @allure.story("查询客户PSI")
    @allure.title("Customer PSI页面，查询国包客户PSI列表数据加载")
    @allure.description("Customer PSI页面，查询国包客户PSI列表数据加载，断言数据是否加载正常")
    @pytest.mark.smoke  # 用例标记
    @allure.severity("blocker")  # 分别为3种类型等级：blocker\critical\normal
    def test_001_001(self, drivers):
        """筛选国包客户PSI列表数据，是否加载正常"""
        #user.dcr_login(drivers, "testsupervisor", "dcr123456")
        user = LoginPage(drivers)
        """报表分析-打开客户PSI页面"""
        user.click_gotomenu("Report Analysis", "Customer PSI")
        psi = CustomerPSIPage(drivers)
        region_text_2 = psi.get_sale_regiona_text()
        region_text_3 = psi.get_sale_regionb_text()
        brand_text = psi.get_brand_text()
        total = psi.get_total_text()
        """根据日期筛选Distributor Customer PSI数据后，断言是否查询到数据"""
        ValueAssert.value_assert_IsNoneNot(region_text_2)
        ValueAssert.value_assert_IsNoneNot(region_text_3)
        ValueAssert.value_assert_IsNoneNot(brand_text)
        psi.assert_total(total)


    @allure.story("查询客户PSI")
    @allure.title("Customer PSI页面，导出按日期查询国包客户PSI列表数据")
    @allure.description("Customer PSI页面，按日期查询国包客户PSI列表数据，并导出")
    @allure.severity("blocker")  # 分别为3种类型等级：blocker\critical\normal
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_export_fixture')
    def test_001_002(self, drivers):
        """筛选国包客户PSI列表数据，导出数据是否正常"""
        export = CustomerPSIPage(drivers)
        # 获取日期
        today = Base(drivers).get_datetime_today()
        last_date = export.get_last_day(2)
        """按日期筛选当天日期前一天的数据，然后进行导出"""
        export.customer_psi_start_date_query(last_date)
        export.click_search()
        # 默认选中查询国包PSI数据
        #点击导出功能
        export.click_export()
        export.click_download_more()
        """进入导出记录页面，根据任务名称与创建日期条件筛选导出的任务记录"""
        export.input_task_name('Customer PSI')
        export.export_record_create_date_query(today)
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
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
        ValueAssert.value_assert_equal(task_id, "testsupervisor")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        # export.click_close_customerPSI()


    @allure.story("查询客户PSI")
    @allure.title("Customer PSI页面，按日期查询二代客户PSI列表数据加载")
    @allure.description("Customer PSI页面，按日期查询二代客户PSI列表数据加载，断言数据是否加载正常")
    @pytest.mark.smoke  # 用例标记
    @allure.severity("blocker")  # 分别为3种类型等级：blocker\critical\normal
    def test_001_003(self, drivers):
        """根据日期筛选二代客户PSI列表数据，是否加载正常"""
        """考勤管理-打开考勤记录页面"""
        menu = LoginPage(drivers)
        menu.click_gotomenu("Report Analysis", "Customer PSI")
        psi = CustomerPSIPage(drivers)
        """点击Sub-dealer按钮筛选二代数据"""
        psi.click_sub_dealer()
        psi.click_search()
        region2_text = psi.get_sale_regiona_text()
        region3_text = psi.get_sale_regionb_text()
        brand_text = psi.get_brand_text()
        total = psi.get_total_text()
        """根据日期筛选Distributor Customer PSI数据后，断言是否查询到数据"""
        ValueAssert.value_assert_IsNoneNot(region2_text)
        ValueAssert.value_assert_IsNoneNot(region3_text)
        ValueAssert.value_assert_IsNoneNot(brand_text)
        psi.assert_total(total)


    @allure.story("查询客户PSI")
    @allure.title("Customer PSI页面，导出按日期查询二代客户PSI列表数据")
    @allure.description("Customer PSI页面，按日期查询二代客户PSI列表数据，并导出。断言导出数据是否正常")
    @allure.severity("blocker")  # 分别为3种类型等级：blocker\critical\normal
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_export_fixture')
    def test_001_004(self, drivers):
        """根据日期筛选二代客户PSI列表数据，导出数据是否正常"""
        export = CustomerPSIPage(drivers)
        # 获取日期
        today = Base(drivers).get_datetime_today()
        last_date = export.get_last_day(2)
        export.customer_psi_start_date_query(last_date)
        # 查询二代PSI数据
        export.click_sub_dealer()
        export.click_search()
        # 筛选出库单后，点击导出功能
        export.click_export()
        export.click_download_more()
        """进入导出记录页面，根据任务名称与创建日期条件筛选导出的任务记录"""
        export.input_task_name('Customer PSI')
        export.export_record_create_date_query(today)
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = export.click_export_search()
        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        user_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()
        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Customer PSI")
        ValueAssert.value_assert_equal(user_id, "testsupervisor")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        # export.click_close_export_record()
        # export.click_close_customerPSI()


if __name__ == '__main__':
    pytest.main(['ReportAnalysis_CustomerPSI.py'])
