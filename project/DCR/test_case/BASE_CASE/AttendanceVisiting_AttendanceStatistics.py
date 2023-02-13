from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.AttendanceVisiting_AttendanceStatistics import AttendanceStatistics
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

@allure.feature("考勤&巡店-考勤统计")
class TestAttendanceStatistics:
    @allure.story("查询考勤统计")
    @allure.title("考勤统计页面，根据user或position查询考勤统计记录列表数据加载")
    @allure.description("考勤统计页面，根据user或position查询考勤统计记录列表数据加载，断言数据加载正常")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Attendance Statistics")

        query = AttendanceStatistics(drivers)
        """根据user 或Position 条件筛选考勤统计信息"""
        query.query_attendance_statistics('Dengdd121', 'DengDD1督导121')

        get_brand = query.get_list_brand()
        get_user_id = query.get_list_user_id()
        get_user_name = query.get_list_user_name()
        get_position = query.get_list_position()
        get_normal = query.get_list_normal()
        get_absence = query.get_list_absence()
        get_late = query.get_list_late()
        get_early = query.get_list_leave_early()
        get_total = query.get_total_text()
        query.assert_total(get_total)
        ValueAssert.value_assert_equal('Dengdd121', get_user_id)
        ValueAssert.value_assert_IsNoneNot(get_brand)
        ValueAssert.value_assert_IsNoneNot(get_user_name)
        ValueAssert.value_assert_IsNoneNot(get_position)
        ValueAssert.value_assert_IsNoneNot(get_normal)
        ValueAssert.value_assert_IsNoneNot(get_absence)
        ValueAssert.value_assert_IsNoneNot(get_late)
        ValueAssert.value_assert_IsNoneNot(get_early)



if __name__ == '__main__':
    pytest.main(['AttendanceVisiting_AttendanceStatistics.py'])
