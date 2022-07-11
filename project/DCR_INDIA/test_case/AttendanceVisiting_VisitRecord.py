from libs.common.time_ui import sleep
from project.DCR_INDIA.page_object.login import LoginPage
from project.DCR_INDIA.page_object.AttendanceVisiting_VisitRecord import VisitRecordPage
from project.DCR_INDIA.page_object.menu import MenuPage
from public.base.assert_ui import ValueAssert
import datetime
import logging
from public.base.basics import Base
import pytest
import allure


@allure.feature("考勤&巡店-巡店记录")
class TestQueryVisitRecord():
    @allure.story("查询巡店记录")
    @allure.title("巡店记录页面，查询巡店记录列表数据加载")
    @allure.description("巡店记录页面，查询巡店记录列表数据加载，校验数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        # user = LoginPage(drivers)
        # user.dcr_login(drivers, "testsupervisor", "dcr123456")
        # sleep(6)

        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)
        """打开考勤与巡店管理-打开巡店记录页面"""
        menu = MenuPage(drivers)
        menu.click_gotomenu("Attendance & Visiting", "Visit Record")
        sleep(8)

        all_visit = VisitRecordPage(drivers)
        shop_id = all_visit.get_shop_id_text()
        submit_date = all_visit.get_submit_date_text()
        visit_date = all_visit.get_visit_date_text()
        operation = all_visit.get_view_operation_text()
        total = all_visit.get_total_text()
        total1 = total[6:11]

        ValueAssert.value_assert_IsNoneNot(shop_id)
        ValueAssert.value_assert_IsNoneNot(submit_date)
        ValueAssert.value_assert_IsNoneNot(visit_date)
        ValueAssert.value_assert_In(operation, "View")
        if int(total1) > 1000:
            logging.info("查看巡店记录列表，加载所有数据正常，分页总条数Total:{}".format(total1))
        else:
            logging.info("查看巡店记录列表，未加载所有数据，分页总条数Total:{}".format(total1))
        sleep(2)


    @allure.story("查询巡店记录")
    @allure.title("巡店记录页面，按Shop ID条件筛选，查询门店巡店记录数据加载")
    @allure.description("巡店记录页面，按Shop ID条件筛选，查询门店巡店记录，校验数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_002(self, drivers):
        """获取当天日期"""
        today = datetime.date.today()
        today1 = str(today)
        visit = VisitRecordPage(drivers)
        visit.click_unfold()

        shop_id = visit.get_shop_id_text()
        visit.input_shop_id_query(shop_id)
        visit.click_search()
        visit.click_fold()

        shopid = visit.get_shop_id_text()
        submit_date = visit.get_submit_date_text()
        visit_date = visit.get_visit_date_text()
        operation = visit.get_view_operation_text()
        total = visit.get_total_text()
        total1 = total[6]

        ValueAssert.value_assert_equal(shop_id, shopid)
        ValueAssert.value_assert_equal(submit_date, today1)
        ValueAssert.value_assert_equal(visit_date, today1)
        ValueAssert.value_assert_In(operation, "View")
        if int(total1) > 0:
            logging.info("根据门店ID筛选，巡店记录列表中，加载筛选的数据正常，分页总条数Total:{}".format(total1))
        else:
            logging.info("根据门店ID筛选，巡店记录列表中，未加载筛选的数据，分页总条数Total:{}".format(total1))
        visit.click_reset()
        visit.click_close_visit_record()
        sleep(1.5)


@allure.feature("考勤&巡店-巡店记录")
class TestExportVisitRecord():
    @allure.story("导出巡店记录")
    @allure.title("巡店记录页面，按Shop ID条件筛选，导出筛选后的巡店记录")
    @allure.description("巡店记录页面，按Shop ID条件筛选，导出筛选后的巡店记录，断言导出数据是否正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        """刷新页面"""
        base = Base(drivers)
        base.refresh()
        sleep(3.5)

        """打开考勤与巡店管理-打开巡店记录页面"""
        menu = MenuPage(drivers)
        menu.click_gotomenu("Attendance & Visiting", "Visit Record")
        sleep(8)

        """获取当天日期"""
        today = datetime.date.today()
        today1 = str(today)
        export = VisitRecordPage(drivers)
        export.input_submit_start_date(today1)
        export.click_sales_region()
        export.click_search()

        export.click_export()
        sleep(3)
        export.click_download_icon()
        export.click_more()
        sleep(18)
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
        ValueAssert.value_assert_equal(task_name, "History List")
        ValueAssert.value_assert_equal(task_id, "testsupervisor")
        ValueAssert.value_assert_equal(create_date1, today1)
        ValueAssert.value_assert_equal(complete_date1, today1)
        ValueAssert.value_assert_equal(operation, "Download")
        if int(file_size1) > 0:
            logging.info("Visit Record导出成功，File Size 导出文件大于0M:{}".format(file_size1))
        else:
            logging.info("Visit Record导出失败，File Size 导出文件小于0M:{}".format(file_size1))

        if int(export_time1) > 0:
            logging.info("Visit Record导出成功，Export Time(s)导出时间大于0s:{}".format(export_time1))
        else:
            logging.info("Visit Record导出失败，Export Time(s)导出时间小于0s:{}".format(export_time1))
        export.click_close_export_record()
        export.click_close_visit_record()
        sleep(1)


if __name__ == '__main__':
    pytest.main(['AttendanceVisiting_VisitRecord.py'])
