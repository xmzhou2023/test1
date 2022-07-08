from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.AttendanceVisiting_AttendanceRecords import AttendanceRecordPage
from public.base.assert_ui import ValueAssert
import logging
from libs.common.time_ui import sleep
import datetime
import pytest
import allure


@allure.feature("考勤&巡店-考勤记录")
class TestQueryAttendanceRecord():
    @allure.story("查询考勤记录")
    @allure.title("考勤记录页面，查询考勤记录列表数据加载")
    @allure.description("考勤记录页面，查询考勤记录列表数据加载，断言数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.dcr_login(drivers, "lhmadmin", "dcr123456")
        sleep(5)
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Attendance Records")
        sleep(10)

        """查询考勤记录列表，是否存在当天考勤记录用例"""
        query_all = AttendanceRecordPage(drivers)
        picture = query_all.get_photo_text()
        date = query_all.get_date_text()

        total = query_all.get_total_text()
        total1 = total[6:11]
        today = datetime.date.today()
        today1 = str(today)
        """断言查询的列表数据是否存在，分页下面的总条数是否有数据"""
        ValueAssert.value_assert_equal(picture, "Picture")
        ValueAssert.value_assert_equal(today1, date)
        if int(total1) > 1000:
            logging.info("查看考勤记录列表，分页总条数大于1000，能查询到考勤记录Total：{}".format(total1))
        else:
            logging.info("查看考勤记录列表，分页总条数为1000，未查询到考勤记录Total：{}".format(total1))
        sleep(1.5)


    @allure.story("查询考勤记录")
    @allure.title("考勤记录页面，查询某个用户的，当天考勤记录")
    @allure.description("考勤记录页面，查询某个用户的，当天考勤记录，断言查询后的数据加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_002(self, drivers):
        """查询某个用户的，当天考勤记录用例"""
        query_user = AttendanceRecordPage(drivers)
        sleep(1)
        today = datetime.date.today()
        today1 = str(today)

        query_user.input_query_date(today1)
        query_user.click_search()
        sleep(7)

        user_id = query_user.get_user_id_text()
        query_user.input_user_id_query(user_id, user_id)
        query_user.click_search()
        sleep(7)

        picture = query_user.get_photo_text()
        date = query_user.get_date_text()
        date1 = str(date)
        userid = query_user.get_user_id_text()
        total = query_user.get_total_text()
        total1 = total[6]

        """断言查询的列表数据是否存在，分页下面的总条数是否有数据"""
        ValueAssert.value_assert_In(picture, "Picture")
        ValueAssert.value_assert_equal(user_id, userid)
        ValueAssert.value_assert_equal(today1, date1)
        if int(total1) > 0:
            logging.info("筛选考勤记录列表，分页总条数大于0，能查询到考勤记录数Total:{}".format(total1))
        else:
            logging.info("筛选考勤记录列表，分页总条数为0，未查询到考勤记录数Total:{}:".format(total1))
        query_user.click_reset()
        sleep(1)


@allure.feature("考勤&巡店-考勤记录")
class TestExportAttendanceRecord():
    @allure.story("导出考勤记录")
    @allure.title("考勤记录页面，导出筛选用户的当天考勤记录")
    @allure.description("考勤记录页面，查询某个用户的，当天考勤记录，然后导出筛选的考勤记录")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_export_record(self, drivers):
        export = AttendanceRecordPage(drivers)
        """获取当天日期"""
        today = datetime.date.today()
        totay1 = str(today)
        export.input_query_date(totay1)
        export.click_search()
        export.click_export()
        sleep(3)
        export.click_download_icon()
        export.click_more()
        sleep(11)
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
        operation = export.get_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "attendance record")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date1, totay1)
        ValueAssert.value_assert_equal(complete_date1, totay1)
        ValueAssert.value_assert_equal(operation, "Download")
        if int(file_size1) > 0:
            logging.info("Attendance Records导出成功，File Size导出文件大于M:{}".format(file_size1))
        else:
            logging.info("Attendance Records导出失败，File Size导出文件小于M:{}".format(file_size1))

        if int(export_time1) > 0:
            logging.info("Attendance Records导出成功，Export Time(s)导出时间大于0s:{}".format(export_time1))
        else:
            logging.info("Attendance Records导出失败，Export Time(s)导出时间小于0s:{}".format(export_time1))
        #export.click_close_export_record()
        #export.click_close_atten_record()
        sleep(1)

if __name__ == '__main__':
    pytest.main(['AttendanceVisiting_AttendanceRecords.py'])
