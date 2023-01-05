from project.DCR.page_object.StaffAuthorization_PositionManagement import PositionManagementPage
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert, DomAssert
from public.base.basics import Base
from libs.common.time_ui import sleep
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

@allure.feature("员工授权-新增职位")
class TestAddPosition:
    @allure.story("新增职位")
    @allure.title("员工授权，新增启用状态的职位")
    @allure.description("职位管理页面，新增启用状态的职位")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.UT
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Staff & Authorization", "Position Management")
        """新建启用状态的职位"""
        add_position = PositionManagementPage(drivers)
        """获取当天日期"""
        today = Base(drivers).get_datetime_today()
        add_position.click_operation_button('Add')
        get_num = add_position.get_number()
        position_name = 'lhm_transsion'+get_num
        add_position.add_input_position_name(position_name)
        add_position.add_select_enabled_yes()
        add_position.add_position_type_promoter_yes('Promoter Group')
        add_position.add_input_default_roles2('Transsion Administrator', 'Transsion Sales Manager', 'Default Roles')
        add_position.add_input_position_remark('传音促销员职位')
        add_position.add_position_save_button()
        """新增职位成功后，弹出成功提示语"""
        DomAssert(drivers).assert_att('Set Up Successfully')
        """刷新页面，才能搜索到新增的职位"""
        Base(drivers).refresh()
        """按 Position条件筛选，新增的职位，点击查询按钮"""
        add_position.input_position_query(position_name, 'Position')
        add_position.click_operation_button('Search')
        """断言查询的结果是否与新增的角色内容一致"""
        add_position.assert_user_management_field('Position', position_name)
        add_position.assert_contains_user_management_field('Default Roles', 'Transsion Administrator')
        add_position.assert_user_management_field('Position Type', 'Promoter Group')
        add_position.assert_user_management_field('Enabled or Not', 'Enabled')
        add_position.assert_user_management_field('Remark', '传音促销员职位')
        add_position.assert_contains_user_management_field('Create Date', today)


    @allure.story("新增职位")
    @allure.title("员工授权，新增禁用状态的职位")
    @allure.description("职位管理页面，新增禁用状态的职位")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.UT
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Staff & Authorization", "Position Management")
        """新建启用状态的职位"""
        add_position = PositionManagementPage(drivers)
        """获取当天日期"""
        today = Base(drivers).get_datetime_today()
        add_position.click_operation_button('Add')
        get_num = add_position.get_number()
        position_name = 'lhm_transsion'+get_num
        add_position.add_input_position_name(position_name)
        add_position.add_select_enabled_no()
        add_position.add_position_type_supervisor('Supervisor Group')
        add_position.add_input_default_roles1('Transsion Administrator', 'Default Roles')
        add_position.add_input_position_remark('传音督导职位')
        add_position.add_position_save_button()
        """新增职位成功后，弹出成功提示语"""
        DomAssert(drivers).assert_att('Set Up Successfully')
        """刷新页面，才能搜索到新增的职位"""
        Base(drivers).refresh()
        """按 Position条件筛选，新增的职位，点击查询按钮"""
        add_position.input_position_query(position_name, 'Position')
        add_position.click_operation_button('Search')
        """断言查询的结果是否与新增的角色内容一致"""
        add_position.assert_user_management_field('Position', position_name)
        add_position.assert_user_management_field('Default Roles', 'Transsion Administrator')
        add_position.assert_user_management_field('Position Type', 'Supervisor Group')
        add_position.assert_user_management_field('Enabled or Not', 'Disabled')
        add_position.assert_user_management_field('Remark', '传音督导职位')
        add_position.assert_contains_user_management_field('Create Date', today)


    @allure.story("编辑职位")
    @allure.title("员工授权，编辑新增的职位")
    @allure.description("职位管理页面，编辑新增的职位")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.UT
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_003(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Staff & Authorization", "Position Management")
        """新建启用状态的职位"""
        edit_position = PositionManagementPage(drivers)
        """获取当天日期"""
        today = Base(drivers).get_datetime_today()
        """获取列表新增待编辑的职位"""
        get_list_add_position = edit_position.get_list_position('lhm_transsion')

        if get_list_add_position is not None:
            """按 Position条件筛选职位，点击查询按钮"""
            edit_position.input_position_query(get_list_add_position, 'Position')
            edit_position.click_operation_button('Search')
            """断言是否筛选到一条满足条件的数据"""
            get_total = edit_position.get_list_total()
            ValueAssert.value_assert_equal('1', get_total)
            """选中筛选的新增职位，点击Edit编辑职位操作"""
            edit_position.click_edit_position_button()
            """编辑常用的职位字段"""
            edit_position.add_position_type_promoter_no('Promoter Group')
            edit_position.add_input_default_roles2('System Administrator', 'Transsion Administrator', 'Default Roles')
            edit_position.add_input_position_remark('编辑系统管理员角色')
            edit_position.add_position_save_button()
            """编辑职位成功后，弹出成功提示语"""
            DomAssert(drivers).assert_att('Set Up Successfully')
            """断言列表字段内容，是否显示编辑后的内容"""
            edit_position.assert_user_management_field('Position', get_list_add_position)
            edit_position.assert_contains_user_management_field('Default Roles', 'System Administrator')
            edit_position.assert_contains_user_management_field('Position Type', 'Promoter Group')
            edit_position.assert_user_management_field('Remark', '编辑系统管理员角色')
            edit_position.assert_contains_user_management_field('Update Date', today)
            """断言列表，分页总条数是否为1"""
            get_total = edit_position.get_list_total()
            ValueAssert.value_assert_equal('1', get_total)
        else:
            pass


    @allure.story("删除职位")
    @allure.title("员工授权，删除新增的职位")
    @allure.description("职位管理页面，删除新增的职位")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.UT
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_004(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Staff & Authorization", "Position Management")
        """新建启用状态的职位"""
        delete_position = PositionManagementPage(drivers)
        """获取列表新增待删除的职位"""
        get_list_add_position = delete_position.get_list_position('lhm_transsion')
        if get_list_add_position is not None:
            """按 Position条件筛选职位，点击查询按钮"""
            delete_position.input_position_query(get_list_add_position, 'Position')
            delete_position.click_operation_button('Search')
            """选中筛选的新增职位，点击Delete删除职位操作"""
            delete_position.click_delete_position('Delete')
            """删除职位成功后，弹出成功提示语"""
            DomAssert(drivers).assert_att('Successfully')
            """断言删除职位成功后，分页总条数是否为0"""
            get_total = delete_position.get_list_total()
            ValueAssert.value_assert_equal('0', get_total)
        else:
            pass


if __name__ == '__main__':
    pytest.main(['StaffAuthorization_PositionManagement.py'])
