from libs.common.time_ui import sleep
from project.DCR_GLOBAL.page_object.login import LoginPage
from project.DCR_GLOBAL.page_object.ReportAnalysis_CustomerPSI import CustomerPSIPage
from project.DCR_GLOBAL.page_object.menu import MenuPage
from public.base.assert_ui import ValueAssert
import datetime
import logging
from public.base.basics import Base
import pytest
import allure


@allure.feature("报表分析-客户PSI")
class TestQueryDistiCustomerPSI():
    @allure.story("查询客户PSI")
    @allure.title("Customer PSI页面，按日期查询国包客户PSI列表数据加载")
    @allure.description("Customer PSI页面，按日期查询国包客户PSI列表数据加载，断言数据是否加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        """筛选国包客户PSI列表数据，是否加载正常"""
        # user = LoginPage(drivers)
        # user.dcr_login(drivers, "testsupervisor", "dcr123456")
        # sleep(6)

        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)
        """报表分析-打开客户PSI页面"""
        menu = MenuPage(drivers)
        menu.click_gotomenu("Report Analysis", "Customer PSI")
        sleep(9)

        psi = CustomerPSIPage(drivers)
        region2_text = psi.get_sales_region2_text()
        region3_text = psi.get_sales_region3_text()
        brand_text = psi.get_brand_text()
        total = psi.get_total_text()
        total1 = total[6:8]

        """根据日期筛选Distributor Customer PSI数据后，断言是否查询到数据"""
        ValueAssert.value_assert_IsNoneNot(region2_text)
        ValueAssert.value_assert_IsNoneNot(region3_text)
        ValueAssert.value_assert_IsNoneNot(brand_text)

        if int(total1) >= 1:
            logging.info("按日期筛选Distributor Customer PSI后，能正常加载数据，Total{}".format(total1))
        else:
            logging.info("按日期筛选Distributor Customer PSI后，未筛选到满足条件的数据，Total1{}".format(total1))
        sleep(2)


    @allure.story("查询客户PSI")
    @allure.title("Customer PSI页面，按日期查询二代客户PSI列表数据加载")
    @allure.description("Customer PSI页面，按日期查询二代客户PSI列表数据加载，断言数据是否加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_002(self, drivers):
        """根据日期筛选二代客户PSI列表数据，是否加载正常"""
        psi = CustomerPSIPage(drivers)
        #点击Sub-dealer按钮筛选二代数据
        psi.click_sub_dealer()
        psi.click_search()
        sleep(8)

        region2_text = psi.get_sales_region2_text()
        region3_text = psi.get_sales_region3_text()
        brand_text = psi.get_brand_text()
        total = psi.get_total_text()
        total1 = total[6:8]
        """根据日期筛选Distributor Customer PSI数据后，断言是否查询到数据"""
        ValueAssert.value_assert_IsNoneNot(region2_text)
        ValueAssert.value_assert_IsNoneNot(region3_text)
        ValueAssert.value_assert_IsNoneNot(brand_text)

        if int(total1) >= 1:
            logging.info("按日期筛选Distributor Customer PSI后，能正常加载数据，Total{}".format(total1))
        else:
            logging.info("按日期筛选Distributor Customer PSI后，未筛选到满足条件的数据，Total1{}".format(total1))
        psi.click_close_customerPSI()
        sleep(1.5)


@allure.feature("报表分析-客户PSI")
class TestExportDistiCustomerPSI():
    @allure.story("导出客户PSI")
    @allure.title("Customer PSI页面，导出按日期查询国包客户PSI列表数据")
    @allure.description("Customer PSI页面，按日期查询国包客户PSI列表数据，并导出")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)

        """报表分析-打开客户PSI页面"""
        menu = MenuPage(drivers)
        menu.click_gotomenu("Report Analysis", "Customer PSI")
        sleep(9)

        """筛选国包客户PSI列表数据，导出数据是否正常"""
        export = CustomerPSIPage(drivers)
        # 获取日期
        today = datetime.date.today()
        today1 = str(today)

        # 点击导出功能
        export.click_export()
        sleep(3)
        export.click_download_icon()
        export.click_more()
        sleep(8)
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
        ValueAssert.value_assert_equal(task_name, "Customer Psi")
        ValueAssert.value_assert_equal(task_id, "testsupervisor")
        ValueAssert.value_assert_equal(create_date1, today1)
        ValueAssert.value_assert_equal(complete_date1, today1)
        ValueAssert.value_assert_equal(operation, "Download")
        if int(file_size1) > 0:
            logging.info("Customer PSI导出成功，File Size 导出文件大于1KB:{}".format(file_size1))
        else:
            logging.info("Customer PSI导出失败，File Size 导出文件小于1KB:{}".format(file_size1))

        if int(export_time1) > 0:
            logging.info("Customer PSI导出成功，Export Time(s)导出时间大于0s:{}".format(export_time1))
        else:
            logging.info("Customer PSI导出失败，Export Time(s)导出时间小于0s:{}".format(export_time1))
        export.click_close_customerPSI()
        sleep(2)


    @allure.story("导出客户PSI")
    @allure.title("Customer PSI页面，导出按日期查询二代客户PSI列表数据")
    @allure.description("Customer PSI页面，按日期查询二代客户PSI列表数据，并导出。断言导出数据是否正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_002(self, drivers):
        """根据日期筛选二代客户PSI列表数据，导出数据是否正常"""
        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)
        """考勤管理-打开考勤记录页面"""
        menu = MenuPage(drivers)
        menu.click_gotomenu("Report Analysis", "Customer PSI")
        sleep(9)

        export = CustomerPSIPage(drivers)
        # 获取日期
        today = datetime.date.today()
        today1 = str(today)

        # 查询二代PSI数据
        export.click_sub_dealer()
        sleep(9)

        #点击导出功能
        export.click_export()
        sleep(2)
        export.click_download_icon()
        export.click_more()
        sleep(5)
        export.click_export_search()
        sleep(5)
        down_status = export.get_download_status_text()
        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        file_size1 = file_size[0:1]
        user_id = export.get_task_user_id_text()
        sleep(1)
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
        ValueAssert.value_assert_equal(create_date1, today1)
        ValueAssert.value_assert_equal(complete_date1, today1)
        ValueAssert.value_assert_equal(operation, "Download")
        if int(file_size1) > 0:
            logging.info("Customer PSI导出成功，File Size 导出文件大于1KB:{}".format(file_size1))
        else:
            logging.info("Customer PSI导出失败，File Size 导出文件小于1KB:{}".format(file_size1))

        if int(export_time1) > 0:
            logging.info("Customer PSI导出成功，Export Time(s)导出时间大于0s:{}".format(export_time1))
        else:
            logging.info("Customer PSI导出失败，Export Time(s)导出时间小于0s:{}".format(export_time1))
        export.click_close_export_record()
        export.click_close_customerPSI()
        sleep(1)


if __name__ == '__main__':
    pytest.main(['ReportAnalysis_CustomerPSI.py'])
