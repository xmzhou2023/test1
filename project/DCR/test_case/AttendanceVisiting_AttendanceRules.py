from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.AttendanceVisiting_AttendanceRules import AttendanceRulesPage
from public.base.assert_ui import ValueAssert, DomAssert
import logging
from libs.common.time_ui import sleep
from public.base.basics import Base
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

@allure.feature("考勤&巡店-考勤排班")
class TestQueryAttendanceRules:
    @allure.story("查询考勤排班")
    @allure.title("考勤排班页面，筛选查询考勤排班记录")
    @allure.description("考勤排班页面，筛选查询开始月份的考勤排班记录")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Attendance Rules")

        query = AttendanceRulesPage(drivers)
        query.input_start_month_query('2022-10')
        query.click_start_month_label()
        query.click_search()
        """断言考勤排班列表，是否展示筛选后的数据，及分页总条数是否有数据"""
        get_start_month = query.get_list_start_month()
        get_country = query.get_list_country()
        get_total = query.get_total()
        logging.info("打印Total 分页总条数：{}".format(get_total))
        ValueAssert.value_assert_equal('2022-10', get_start_month)
        ValueAssert.value_assert_IsNoneNot(get_country)
        query.assert_total(get_total)


    @allure.story("查询考勤排班")
    @allure.title("随机条件组合查询考勤排班")
    @allure.description("考勤排班页面，查询考勤排班的随机条件组合查询")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_002(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """变量"""
        query_dict = {
            'Brand': 'TECNO',
            'Country': 'China',
            'Start Month': '2022-12'
        }
        add = AttendanceRulesPage(drivers)
        user.click_gotomenu("Attendance & Visiting", "Attendance Rules")
        add.random_Query_Method(query_dict)


@allure.feature("考勤&巡店-考勤排班")
class TestAddDeleteAttendanceRules:
    @allure.story("新增、删除考勤排班")
    @allure.title("考勤排班页面，新增、删除考勤排班操作")
    @allure.description("考勤排班页面，新增、删除考勤排班保存后，断言列表是否显示新增的考勤排班记录")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Attendance Rules")

        add_rules = AttendanceRulesPage(drivers)
        """点击Add 新增考勤规则操作"""
        add_rules.click_add()
        add_rules.click_add_cancel()
        """点击Cancel取消新增操作"""
        add_rules.click_add()
        add_rules.click_add_brand3('Infinix', 'TECNO', 'itel')
        add_rules.input_add_country('Bangladesh')
        add_rules.input_add_position('lhm二代')
        """点击position label释放光标"""
        add_rules.click_position_label()
        add_rules.input_remark('新增10月份考勤规则')
        add_rules.click_start_month('2022-10')
        """点击on work time label释放光标"""
        add_rules.click_on_work_time_label()
        add_rules.input_on_work_time('09:00')
        add_rules.input_off_work_time('18:00')
        """"Add考勤规则页面，检验工时"""
        add_rules.click_check_working_hours()
        add_rules.click_save()
        DomAssert(drivers).assert_att('Set Up Successfully')
        sleep(1.5)

        """根据开始日期筛选考勤规则记录"""
        add_rules.input_country_query('Bangladesh')
        add_rules.input_start_month_query('2022-10')
        add_rules.click_start_month_label()
        add_rules.click_search()

        """断言列表是否展示新增的考勤记录"""
        get_start_month = add_rules.get_list_start_month()
        get_country = add_rules.get_list_country()
        get_on_work_time = add_rules.get_list_on_work_time()
        get_off_work_time = add_rules.get_list_off_work_time()
        get_position = add_rules.get_list_position()
        ValueAssert.value_assert_equal('2022-10', get_start_month)
        ValueAssert.value_assert_equal('Bangladesh', get_country)
        ValueAssert.value_assert_equal('09:00', get_on_work_time)
        ValueAssert.value_assert_equal('18:00', get_off_work_time)
        ValueAssert.value_assert_equal('lhm二代', get_position)

        """删除考勤规则记录 """
        add_rules.click_first_checkbox()
        add_rules.click_delete_confirm()
        DomAssert(drivers).assert_att('Deleted Successfully')


    @allure.story("新增考勤排班")
    @allure.title("考勤排班页面，不支持新增已存在的考勤排班")
    @allure.description("考勤排班页面，新增已存在的考勤排班操作，提示：同一国家的品牌位置不允许重复")
    @allure.severity("minor")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Attendance Rules")

        add_rules = AttendanceRulesPage(drivers)
        """点击Add 新增考勤规则操作"""
        add_rules.click_add()
        add_rules.click_add_brand2('TECNO', 'itel')
        add_rules.input_add_country('China')
        add_rules.input_add_position('lhm二代')
        """点击position label释放光标"""
        add_rules.click_position_label()
        add_rules.input_remark('新增10月份考勤规则')
        add_rules.click_start_month('2022-10')
        """点击on work time label释放光标"""
        add_rules.click_on_work_time_label()
        add_rules.input_on_work_time('09:00')
        add_rules.input_off_work_time('18:00')
        add_rules.click_check_working_hours()
        add_rules.click_save()
        DomAssert(drivers).assert_att('The same country brand position is not allowed to repeat')
        sleep(1)
        add_rules.click_cancel()


@allure.feature("考勤&巡店-考勤排班")
class TestEditAttendanceRules:
    @allure.story("编辑考勤排班")
    @allure.title("考勤排班页面，编辑考勤排班操作")
    @allure.description("考勤排班页面，编辑考勤排班保存后，断言列表是否显示编辑后的排班信息")
    @allure.severity("blocker")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Attendance & Visiting", "Attendance Rules")

        edit = AttendanceRulesPage(drivers)
        edit.input_country_query('China')
        edit.input_start_month_query('2022-10')
        """点击start month label释放光标位置"""
        edit.click_start_month_label()
        edit.click_search()

        edit.click_edit()
        """点击on work time label释放光标"""
        edit.click_add_brand1('Infinix')
        edit.click_on_work_time_label()
        edit.input_on_work_time('09:00')
        edit.input_off_work_time('18:00')
        edit.click_save()
        DomAssert(drivers).assert_att('Set Up Successfully')

        """断言列表是否更新修改后字段内容，获取列表字段内容与修改后的字段进行比较是否一致"""
        get_start_month = edit.get_list_start_month()
        get_country = edit.get_list_country()
        get_on_work_time = edit.get_list_on_work_time()
        get_off_work_time = edit.get_list_off_work_time()
        ValueAssert.value_assert_equal('China', get_country)
        ValueAssert.value_assert_equal('2022-10', get_start_month)
        ValueAssert.value_assert_equal('09:00', get_on_work_time)
        ValueAssert.value_assert_equal('18:00', get_off_work_time)


if __name__ == '__main__':
    pytest.main(['AttendanceVisiting_AttendanceRules.py'])
