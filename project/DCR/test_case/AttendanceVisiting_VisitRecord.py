from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.AttendanceVisiting_VisitRecord import VisitRecordPage
from public.base.assert_ui import ValueAssert
import logging
from public.base.basics import Base
from libs.common.time_ui import sleep
import datetime
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

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

@allure.feature("考勤&巡店-巡店记录")
class TestQueryVisitRecord:
    @allure.story("查询巡店记录")
    @allure.title("巡店记录页面，根据门店ID查询类型为Visit task的巡店记录，能正常加载筛选的巡店记录")
    @allure.description("巡店记录页面，根据门店ID查询类型为Visit task的巡店记录，列表数据加载，断言数据加载正常")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Visit Record")

        visit_task = VisitRecordPage(drivers)
        visit_task.input_submit_start_date("2022-11-01")
        visit_task.click_submit_date()
        visit_task.click_shop_self_inspection('Visit task')
        visit_task.click_search()
        shop_id = visit_task.get_shop_id_text()
        logging.info("获取Visit task的巡店记录列表Shop ID字段文本{}".format(shop_id))
        visit_task.click_unfold()
        visit_task.input_shop_id_query(shop_id)
        visit_task.click_fold()
        visit_task.click_search()
        sleep(2)
        shop_id2 = visit_task.get_shop_id_text()
        submit_date = visit_task.get_submit_date_text()
        visit_date = visit_task.get_visit_date_text()
        operation = visit_task.get_view_operation_text()
        total = visit_task.get_total_text()

        ValueAssert.value_assert_equal(shop_id, shop_id2)
        ValueAssert.value_assert_IsNoneNot(submit_date)
        ValueAssert.value_assert_IsNoneNot(visit_date)
        ValueAssert.value_assert_In(operation, "View")
        visit_task.assert_total(total)


    @allure.story("查询巡店记录")
    @allure.title("巡店记录页面，根据门店ID查询类型为Shop self-inspection的巡店记录，能正常加载筛选的巡店记录")
    @allure.description("巡店记录页面，根据门店ID查询类型为Shop self-inspection的巡店记录，列表数据加载，断言数据加载正常")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Visit Record")

        visit = VisitRecordPage(drivers)
        visit.input_submit_start_date("2022-09-01")
        visit.click_shop_self_inspection('Shop self-inspection')
        visit.click_search()
        sleep(2)
        shop_id = visit.get_shop_id_text()
        logging.info("获取Shop self-inspection的巡店记录列表Shop ID字段文本{}".format(shop_id))
        visit.click_unfold()
        visit.input_shop_id_query(shop_id)
        visit.click_fold()
        visit.click_search()
        sleep(2)
        shop_id2 = visit.get_shop_id_text()
        submit_date = visit.get_submit_date_text()
        visit_date = visit.get_visit_date_text()
        operation = visit.get_view_operation_text()
        total = visit.get_total_text()

        ValueAssert.value_assert_equal(shop_id, shop_id2)
        ValueAssert.value_assert_IsNoneNot(submit_date)
        ValueAssert.value_assert_IsNoneNot(visit_date)
        ValueAssert.value_assert_In(operation, "View")
        visit.assert_total(total)


@allure.feature("考勤&巡店-巡店记录")
class TestExportVisitRecord:
    @allure.story("导出巡店记录")
    @allure.title("巡店记录页面，切换Visit task页签，按Submit Date条件筛选，导出筛选后的巡店记录")
    @allure.description("巡店记录页面，切换Visit task页签，按Submit Date条件筛选，导出筛选后的巡店记录，断言导出数据是否正常")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_export_fixture')
    def test_002_001(self, drivers):
        """打开考勤与巡店管理-打开巡店记录页面"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Visit Record")
        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()

        export = VisitRecordPage(drivers)
        export.input_submit_start_date("2022-09-01")
        export.click_submit_date()
        export.click_search()

        export.click_export()
        export.click_download_more()
        export.input_task_name("History List")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()

        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()
        logging.info("获取导出记录列表的operation字段内容{}".format(operation))

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "History List")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)


    @allure.story("导出巡店记录")
    @allure.title("巡店记录页面，切换Visit task页签，按Submit Date条件筛选，导出筛选后的巡店记录详情数据")
    @allure.description("巡店记录页面，切换Visit task页签，按Submit Date条件筛选，导出筛选后的巡店记录详情数据，断言导出数据是否正常")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_export_fixture')
    def test_002_002(self, drivers):
        """打开考勤与巡店管理-打开巡店记录页面"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Visit Record")
        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()
        export2 = VisitRecordPage(drivers)

        export2.input_submit_start_date("2022-09-01")
        export2.click_submit_date()
        export2.click_search()

        export2.click_export_detail()
        export2.click_download_more()
        export2.input_task_name("VisitingRecordDetails List")
        down_status = export2.click_export_search()

        task_name = export2.get_task_name_text()
        file_size = export2.get_file_size_text()

        task_id = export2.get_task_user_id_text()
        create_date = export2.get_create_date_text()
        complete_date = export2.get_complete_date_text()
        export_time = export2.get_export_time_text()
        operation = export2.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "VisitingRecordDetails List")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export2.assert_file_time_size(file_size, export_time)


    @allure.story("导出巡店记录")
    @allure.title("巡店记录页面，切换Shop self-inspection页签，按Submit Date条件筛选，导出筛选后的巡店记录")
    @allure.description("巡店记录页面，切换Shop self-inspection页签，按Submit Date条件筛选，导出筛选后的巡店记录，断言导出数据是否正常")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_export_fixture')
    def test_002_003(self, drivers):
        """打开考勤与巡店管理-打开巡店记录页面"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Visit Record")
        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()

        export = VisitRecordPage(drivers)
        export.input_submit_start_date("2022-08-22")
        export.click_submit_date()
        export.click_shop_self_inspection()
        export.click_search()

        export.click_export()
        export.click_download_more()
        export.input_task_name("History List")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()

        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "History List")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)


    @allure.story("导出巡店记录")
    @allure.title("巡店记录页面，切换Shop self-inspection页签，按Submit Date条件筛选，导出筛选后的巡店详情记录")
    @allure.description("巡店记录页面，切换Shop self-inspection页签，按Submit Date条件筛选，导出筛选后的巡店详情记录，断言导出数据是否正常")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_export_fixture')
    def test_002_004(self, drivers):
        """打开考勤与巡店管理-打开巡店记录页面"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Visit Record")
        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()

        export = VisitRecordPage(drivers)
        export.input_submit_start_date("2022-08-22")
        export.click_submit_date()
        export.click_shop_self_inspection()
        export.click_search()

        export.click_export_detail()
        export.click_download_more()
        export.input_task_name("VisitingRecordDetails List")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()

        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "VisitingRecordDetails List")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)


if __name__ == '__main__':
    pytest.main(['AttendanceVisiting_VisitRecord.py'])
