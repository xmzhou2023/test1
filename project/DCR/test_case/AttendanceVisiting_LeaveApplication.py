from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.AttendanceVisiting_LeaveApplication import LeaveApplicationRecords
from public.base.assert_ui import ValueAssert
import logging
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

@allure.feature("考勤&巡店-休假申请记录")
class TestLeaveApplicationRecords:
    @allure.story("查询休假申请记录")
    @allure.title("休假申请记录页面，根据user查询休假申请记录列表数据加载")
    @allure.description("休假申请记录页面，根据user查询休假申请记录列表数据加载，断言数据加载正常")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Leave Application Records")

        query = LeaveApplicationRecords(drivers)

        user_id = query.get_list_user_id()
        logging.info("打印列表获取的User ID：{}".format(user_id))
        """根据user 或Position 条件筛选考勤统计信息"""
        query.query_leave_application_records('2022-07-01', user_id)

        get_leave_type = query.get_list_leave_type()
        get_leave_reason = query.get_list_leave_reason()
        get_start_date = query.get_list_start_date()
        get_start_time = query.get_list_start_time()
        get_end_date = query.get_list_end_date()
        get_end_time = query.get_list_end_time()
        get_duration = query.get_list_duration()
        get_status = query.get_list_status()
        get_user_id = query.get_list_user_id()
        get_total = query.get_total_text()

        ValueAssert.value_assert_IsNoneNot(get_leave_type)
        ValueAssert.value_assert_IsNoneNot(get_leave_reason)
        ValueAssert.value_assert_IsNoneNot(get_start_date)
        ValueAssert.value_assert_IsNoneNot(get_start_time)
        ValueAssert.value_assert_IsNoneNot(get_end_date)
        ValueAssert.value_assert_IsNoneNot(get_end_time)
        ValueAssert.value_assert_IsNoneNot(get_duration)
        ValueAssert.value_assert_IsNoneNot(get_status)
        ValueAssert.value_assert_equal(user_id, get_user_id)
        query.assert_total(get_total)


if __name__ == '__main__':
    pytest.main(['AttendanceVisiting_LeaveApplication.py'])
