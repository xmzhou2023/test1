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
        """获取当天日期之前7天的日期"""
        last_date = Base(drivers).get_last_day(7)
        visit_task.input_submit_start_date(last_date)
        visit_task.click_shop_self_inspection('Visit task')
        visit_task.click_search()
        shop_id = visit_task.get_shop_id_text()
        logging.info("获取Visit task的巡店记录列表Shop ID字段文本{}".format(shop_id))
        visit_task.input_shop_id_query(shop_id)
        """点击查询按钮"""
        visit_task.click_search()
        visit_date = visit_task.get_visit_date_text()
        total = visit_task.get_total_text()
        visit_task.assert_visit_record_field('Shop ID', shop_id)
        visit_task.assert_visit_record_field('Visit Date', visit_date)
        visit_task.assert_visit_record_field('Operation', 'View')
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
        """获取当天日期之前50天的日期"""
        last_date = Base(drivers).get_last_day(50)
        visit.input_submit_start_date(last_date)
        visit.click_shop_self_inspection('Shop self-inspection')
        visit.click_search()
        shop_id = visit.get_shop_id_text()
        logging.info("获取Shop self-inspection的巡店记录列表Shop ID字段文本{}".format(shop_id))
        visit.input_shop_id_query(shop_id)
        visit.click_search()
        visit_date = visit.get_visit_date_text()
        total = visit.get_total_text()
        visit.assert_visit_record_field('Shop ID', shop_id)
        visit.assert_visit_record_field('Visit Date', visit_date)
        visit.assert_visit_record_field('Operation', 'View')
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
        export = VisitRecordPage(drivers)
        """获取当天日期"""
        today = Base(drivers).get_datetime_today()
        """获取当天日期之前7天的日期"""
        last_date = Base(drivers).get_last_day(7)
        export.input_submit_start_date(last_date)
        export.click_shop_self_inspection('Visit task')
        """点击查询按钮"""
        export.click_search()

        """点击导出"""
        export.click_export()
        export.click_download_more()
        """进入导出记录页面，根据任务名称与创建日期条件筛选导出的任务记录"""
        export.input_task_name('Visit Record')
        export.export_record_create_date_query(today)
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = export.click_export_search()
        file_size = export.get_file_size_text()
        export_time = export.get_export_time_text()
        export.assert_file_time_size(file_size, export_time)
        export.assert_visit_record_field('Download Status', down_status)
        export.assert_visit_record_field('Task Name', 'Visit Record')
        export.assert_visit_record_field('User ID', 'lhmadmin')
        export.assert_visit_record_field('Create Date', today)
        export.assert_visit_record_field('Completed Date', today)
        export.assert_visit_record_field('Operation', 'Download')



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
        today = Base(drivers).get_datetime_today()
        """获取当天日期之前7天的日期"""
        last_date = Base(drivers).get_last_day(7)
        export2 = VisitRecordPage(drivers)
        export2.input_submit_start_date(last_date)
        export2.click_shop_self_inspection('Visit task')
        export2.click_search()

        export2.click_export_detail()
        export2.click_download_more()
        """进入导出记录页面，根据任务名称与创建日期条件筛选导出的任务记录"""
        export2.input_task_name("Visit Record Details List")
        export2.export_record_create_date_query(today)
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = export2.click_export_search()
        file_size = export2.get_file_size_text()
        export_time = export2.get_export_time_text()
        export2.assert_file_time_size(file_size, export_time)
        export2.assert_visit_record_field('Download Status', down_status)
        export2.assert_visit_record_field('Task Name', 'Visit Record Details List')
        export2.assert_visit_record_field('User ID', 'lhmadmin')
        export2.assert_visit_record_field('Create Date', today)
        export2.assert_visit_record_field('Completed Date', today)
        export2.assert_visit_record_field('Operation', 'Download')


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
        today = Base(drivers).get_datetime_today()
        """获取当天日期之前50天的日期"""
        last_date = Base(drivers).get_last_day(50)
        export = VisitRecordPage(drivers)
        export.input_submit_start_date(last_date)
        export.click_shop_self_inspection('Shop self-inspection')
        export.click_search()
        export.click_export()
        export.click_download_more()
        """进入导出记录页面，根据任务名称与创建日期条件筛选导出的任务记录"""
        export.input_task_name('Visit Record')
        export.export_record_create_date_query(today)
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = export.click_export_search()
        file_size = export.get_file_size_text()
        export_time = export.get_export_time_text()
        export.assert_file_time_size(file_size, export_time)
        export.assert_visit_record_field('Download Status', down_status)
        export.assert_visit_record_field('Task Name', 'Visit Record')
        export.assert_visit_record_field('User ID', 'lhmadmin')
        export.assert_visit_record_field('Create Date', today)
        export.assert_visit_record_field('Completed Date', today)
        export.assert_visit_record_field('Operation', 'Download')


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
        today = Base(drivers).get_datetime_today()
        """获取当天日期之前50天的日期"""
        last_date = Base(drivers).get_last_day(50)
        export = VisitRecordPage(drivers)
        export.input_submit_start_date(last_date)
        export.click_shop_self_inspection('Shop self-inspection')
        export.click_search()

        export.click_export_detail()
        export.click_download_more()
        """进入导出记录页面，根据任务名称与创建日期条件筛选导出的任务记录"""
        export.input_task_name("Visit Record Details List")
        export.export_record_create_date_query(today)
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = export.click_export_search()
        file_size = export.get_file_size_text()
        export_time = export.get_export_time_text()
        export.assert_file_time_size(file_size, export_time)
        export.assert_visit_record_field('Download Status', down_status)
        export.assert_visit_record_field('Task Name', 'Visit Record Details List')
        export.assert_visit_record_field('User ID', 'lhmadmin')
        export.assert_visit_record_field('Create Date', today)
        export.assert_visit_record_field('Completed Date', today)
        export.assert_visit_record_field('Operation', 'Download')


if __name__ == '__main__':
    pytest.main(['AttendanceVisiting_VisitRecord.py'])
