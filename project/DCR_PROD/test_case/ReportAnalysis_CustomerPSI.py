from libs.common.time_ui import sleep
from project.DCR_PROD.page_object.Center_Component import DCRLoginPage
from project.DCR_PROD.page_object.ReportAnalysis_CustomerPSI import CustomerPSIPage
from public.base.assert_ui import ValueAssert
from public.base.basics import Base
import pytest
import allure


@allure.feature("报表分析-客户PSI")
class TestQueryDistiCustomerPSI:
    @allure.story("查询国包客户PSI")
    @allure.title("Customer PSI页面，查询国包客户PSI列表数据加载")
    @allure.description("Customer PSI页面，查询国包客户PSI列表数据加载，断言数据是否加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        """筛选国包客户PSI列表数据，是否加载正常"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)

        menu = DCRLoginPage(drivers)
        #user.dcr_login(drivers, "testsupervisor", "dcr123456")

        """报表分析-打开客户PSI页面"""
        menu.click_gotomenu("Report Analysis", "Customer PSI")

        psi = CustomerPSIPage(drivers)
        region_texta = psi.get_sale_regiona_text()
        region_textb = psi.get_sale_regionb_text3()
        brand_text = psi.get_brand_text()
        total = psi.get_total_text()

        """根据日期筛选Distributor Customer PSI数据后，断言是否查询到数据"""
        ValueAssert.value_assert_IsNoneNot(region_texta)
        ValueAssert.value_assert_IsNoneNot(region_textb)
        ValueAssert.value_assert_IsNoneNot(brand_text)
        psi.assert_total(total)
        sleep(1)


@allure.feature("报表分析-客户PSI")
class TestExportDistiCustomerPSI:
    @allure.story("导出国包客户PSI")
    @allure.title("Customer PSI页面，导出按日期查询国包客户PSI列表数据")
    @allure.description("Customer PSI页面，按日期查询国包客户PSI列表数据，并导出")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        """筛选国包客户PSI列表数据，导出数据是否正常"""
        export = CustomerPSIPage(drivers)
        # 获取日期
        base = Base(drivers)
        today = base.get_datetime_today()

        #点击导出功能
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
        ValueAssert.value_assert_equal(task_name, "Customer Psi")
        ValueAssert.value_assert_equal(task_id, "testsupervisor")
        ValueAssert.value_assert_equal(create_date1, today)
        ValueAssert.value_assert_equal(complete_date1, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size1, export_time1)
        export.click_close_customerPSI()
        sleep(1)


@allure.feature("报表分析-客户PSI")
class TestQuerSubCustomerPSI:
    @allure.story("查询二代客户PSI")
    @allure.title("Customer PSI页面，按日期查询二代客户PSI列表数据加载")
    @allure.description("Customer PSI页面，按日期查询二代客户PSI列表数据加载，断言数据是否加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_003_001(self, drivers):
        """根据日期筛选二代客户PSI列表数据，是否加载正常"""
        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)
        """考勤管理-打开考勤记录页面"""
        menu = DCRLoginPage(drivers)
        menu.click_gotomenu("Report Analysis", "Customer PSI")

        psi = CustomerPSIPage(drivers)
        # 点击Sub-dealer按钮筛选二代数据
        psi.click_sub_dealer()
        psi.click_search()

        region2_text = psi.get_sale_regiona_text()
        region3_text = psi.get_sale_regionb_text3()
        brand_text = psi.get_brand_text()
        total = psi.get_total_text()

        """根据日期筛选Distributor Customer PSI数据后，断言是否查询到数据"""
        ValueAssert.value_assert_IsNoneNot(region2_text)
        ValueAssert.value_assert_IsNoneNot(region3_text)
        ValueAssert.value_assert_IsNoneNot(brand_text)
        psi.assert_total(total)


@allure.feature("报表分析-客户PSI")
class TestExportSubCustomerPSI:
    @allure.story("导出二代客户PSI")
    @allure.title("Customer PSI页面，导出按日期查询二代客户PSI列表数据")
    @allure.description("Customer PSI页面，按日期查询二代客户PSI列表数据，并导出。断言导出数据是否正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_004_001(self, drivers):
        """根据日期筛选二代客户PSI列表数据，导出数据是否正常"""
        export = CustomerPSIPage(drivers)
        # 获取日期
        base = Base(drivers)
        today = base.get_datetime_today()
        # 查询二代PSI数据
        export.click_sub_dealer()

        # 筛选出库单后，点击导出功能
        export.click_export()
        export.click_download_more()
        export.click_export_search()

        down_status = export.get_download_status_text()
        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        file_size1 = file_size[0:1]
        user_id = export.get_task_user_id_text()

        create_date = export.get_create_date_text()
        create_date1 = create_date[0:10]
        complete_date = export.get_complete_date_text()
        complete_date1 = complete_date[0:10]
        export_time = export.get_export_time_text()
        export_time1 = export_time[0:1]
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Customer Psi")
        ValueAssert.value_assert_equal(user_id, "testsupervisor")
        ValueAssert.value_assert_equal(create_date1, today)
        ValueAssert.value_assert_equal(complete_date1, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size1, export_time1)

        export.click_close_export_record()
        export.click_close_customerPSI()



if __name__ == '__main__':
    pytest.main(['ReportAnalysis_CustomerPSI.py'])
