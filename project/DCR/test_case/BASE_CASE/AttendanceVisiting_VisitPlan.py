from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.AttendanceVisiting_VisitPlan import VisitPlan
from public.base.assert_ui import ValueAssert
import logging
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

@allure.feature("考勤&巡店-巡店计划")
class TestVisitPlan:
    @allure.story("查询巡店计划")
    @allure.title("查询巡店计划页面，根据Shop查询巡店计划信息，列表数据加载")
    @allure.description("巡店计划页面，根据Shop查询巡店计划列表数据加载，断言数据加载正常")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Visit Plan")

        query = VisitPlan(drivers)
        shop_id = query.get_list_shop_id()
        logging.info("获取列表Shop ID：{}".format(shop_id))
        query.click_unfold()
        """获取列表Shop ID，然后根据门店ID进行筛选巡店计划数据"""
        query.input_shop_query_search(shop_id)
        query.click_fold()

        get_plan_no = query.get_plan_no()
        get_shop_name = query.get_list_shop_name()
        get_shop_id = query.get_list_shop_id()
        get_status = query.get_list_status()
        get_upload_user = query.get_list_upload_user()
        get_user_name = query.get_list_user_name()
        get_position = query.get_list_position()
        get_total = query.get_total_text()
        ValueAssert.value_assert_IsNoneNot(get_plan_no)
        ValueAssert.value_assert_IsNoneNot(get_shop_name)
        ValueAssert.value_assert_equal(shop_id, get_shop_id)
        ValueAssert.value_assert_IsNoneNot(get_status)
        ValueAssert.value_assert_IsNoneNot(get_upload_user)
        ValueAssert.value_assert_IsNoneNot(get_user_name)
        ValueAssert.value_assert_IsNoneNot(get_position)
        query.assert_total(get_total)


if __name__ == '__main__':
    pytest.main(['AttendanceVisiting_VisitPlan.py'])
