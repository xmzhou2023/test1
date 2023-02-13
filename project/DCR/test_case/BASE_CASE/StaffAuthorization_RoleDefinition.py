from datetime import datetime

from libs.common.time_ui import sleep
from project.DCR.page_object.StaffAuthorization_RoleDefinition import RoleDefinitionPage
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert, DomAssert
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_set_role_fixture(drivers):
    yield
    close = RoleDefinitionPage(drivers)
    close.click_close_role_definition()

@allure.feature("用户和授权-角色管理")
class TestSetRolePermission:
    @allure.story("角色管理")
    @allure.title("角色定义页面，给“lhmItel店长”角色设置权限")
    @allure.description("角色定义页面，给“lhmItel店长”角色设置菜单权限")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_set_role_fixture')
    def test_001_001(self, drivers):
        """DCR 二代账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开Staff & Authorization模块下的 Role Definition的菜单"""
        user.click_gotomenu("Staff & Authorization", "Role Definition")
        """Role Definition角色定义页面，筛选“lhmItel店长”角色，然后添加Basic Data Management菜单权限用例"""
        role = RoleDefinitionPage(drivers)
        role.input_role_query("lhmItel店长")
        role.click_search()

        role.click_first_checkbox()
        role.click_permission_setting()
        role.click_check_basic_data_mgt()
        """点击保存"""
        role.click_save()
        """断言是否弹出保存成功提示"""
        DomAssert(drivers).assert_att('Save Successfully')
        role.click_confirm()
        #role.click_close_role_definition()
        # """设置Basic Data Management模块权限后，检查是否能打开此模块下的菜单 """
        # user = DCRLogin(drivers)
        # user.dcr_login(udrivers, "testlhm0215", "dcr123456")
        # sleep(5)
        # menu = MenuPage(drivers)
        # menu.click_gotomenu("Basic Data Management", "Sales Region Management")
        # sleep(5)
        # sales_region = role.get_sale_region_mgt_text()
        # assert_ui.value_assert_In(sales_region, "Sales Region Management")

    @allure.story("角色管理") # 场景名称
    @allure.title("组合查询成功")  # 用例名称
    @allure.description("组合查询成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):
        """变量"""
        query_dict = {
            'Role': 'wjkedit',
            # 'Web Menu': 'wjkTS',
            # 'App Menu': 'wjkTS',
            'Enable or Not': 'Enable',
            # 'Menu Type': 'Web Menu',
            'Creator': 'pakadmin',
            'Updater': 'pakadmin'
        }
        add = RoleDefinitionPage(drivers)
        add.click_menu("Staff & Authorization", "Role Definition")
        add.click_unfold()
        add.All_Query_Method(query_dict)


    @allure.story("角色管理") # 场景名称
    @allure.title("单一条件随机查询成功")  # 用例名称
    @allure.description("单一条件随机查询成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):
        """变量"""
        query_dict = {
            'Role': 'wjkedit',
            # 'Web Menu': 'wjkTS',
            # 'App Menu': 'wjkTS',
            'Enable or Not': 'Enable',
            # 'Menu Type': 'Web Menu',
            'Creator': 'pakadmin',
            'Updater': 'pakadmin'
        }
        add = RoleDefinitionPage(drivers)
        add.click_menu("Staff & Authorization", "Role Definition")
        add.click_unfold()
        add.random_Query_Method(query_dict)

    @allure.story("角色管理")
    @allure.title("新增角色成功")
    @allure.description("新增角色成功")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):
        """账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击角色管理菜单"""
        add = RoleDefinitionPage(drivers)
        add.click_menu("Staff & Authorization", "Role Definition")
        """新增角色"""
        Role = 'Role名称自动生成{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        add.click_function_button('Add')
        add.input_role_content('Role Code', Role)
        add.input_role_content('Role', Role)
        add.click_AddSave()
        """断言：角色新增成功"""
        DomAssert(drivers).assert_att("Successfully")
        add.refresh()
        add.input_search('Role', Role)
        add.click_search()
        add.assert_Query_result('Role', Role)
        add.assert_Query_result('Enable or Not', 'Yes')
        """删除角色"""
        add.click_checkbox(Role)
        add.click_function_button('Delete')
        DomAssert(drivers).assert_att("Successfully")

    @allure.story("角色管理")
    @allure.title("编辑角色成功")
    @allure.description("编辑角色成功")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):
        """账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击角色管理菜单"""
        add = RoleDefinitionPage(drivers)
        add.click_menu("Staff & Authorization", "Role Definition")
        """新增角色"""
        Role = 'Role名称自动生成{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        add.click_function_button('Add')
        add.input_role_content('Role Code', Role)
        add.input_role_content('Role', Role)
        add.click_AddSave()
        """编辑角色"""
        Role2 = 'Role名称自动生成{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        Remark = '自动化编辑备注自动生成{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        add.click_edit(Role)
        add.input_role_content('Role', Role2)
        add.input_role_content('Remark', Remark)
        add.click_AddSave()
        """断言：角色编辑成功"""
        DomAssert(drivers).assert_att("Successfully")
        add.refresh()
        add.input_search('Role', Role2)
        add.click_search()
        add.assert_Query_result('Role', Role2)
        add.assert_Query_result('Remark', Remark)
        """删除角色"""
        add.click_checkbox(Role2)
        add.click_function_button('Delete')
        DomAssert(drivers).assert_att("Successfully")

    @allure.story("角色管理")
    @allure.title("删除角色成功")
    @allure.description("删除角色成功")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    def test_001_006(self, drivers):
        """账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击角色管理菜单"""
        add = RoleDefinitionPage(drivers)
        add.click_menu("Staff & Authorization", "Role Definition")
        """新增角色"""
        Role = 'Role名称自动生成{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        add.click_function_button('Add')
        add.input_role_content('Role Code', Role)
        add.input_role_content('Role', Role)
        add.click_AddSave()
        DomAssert(drivers).assert_att("Successfully")
        add.refresh()
        """删除角色"""
        add.input_search('Role', Role)
        add.click_search()
        add.click_checkbox(Role)
        add.click_function_button('Delete')
        """断言：角色删除成功"""
        DomAssert(drivers).assert_att("Successfully")
        add.click_search()
        add.assert_NoData()

    @allure.story("角色管理")
    @allure.title("导出角色管理明细成功")
    @allure.description("导出角色管理明细成功")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_001_007(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击角色管理菜单"""
        add = RoleDefinitionPage(drivers)
        add.click_menu("Staff & Authorization", "Role Definition")
        add.click_unfold()
        add.input_search('Role', "wjkedit")
        add.input_search('Menu Type', "App Menu")
        add.click_search()
        """导出筛选条件下的角色管理明细"""
        add.click_checkbox('wjkedit')
        add.click_function_button('Export Permission')
        """断言：存在导出文件进度条"""
        add.assert_export_success()

    @allure.story("角色管理")
    @allure.title("角色权限设置成功")
    @allure.description("角色权限设置成功")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_001_008(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """点击角色管理菜单"""
        add = RoleDefinitionPage(drivers)
        add.click_menu("Staff & Authorization", "Role Definition")
        """新增角色"""
        Role = 'Role名称自动生成{}'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        add.click_function_button('Add')
        add.input_role_content('Role Code', Role)
        add.input_role_content('Role', Role)
        add.click_AddSave()
        DomAssert(drivers).assert_att("Successfully")
        add.refresh()
        """角色授权设置"""
        add.input_search('Role', Role)
        add.click_search()
        add.click_checkbox(Role)
        add.click_function_button('Permission Setting')
        add.click_menu_checkbox('Home Page')
        add.click_menu_checkbox('Basic Data Management')
        add.click_menu_management('app')
        add.click_menu_checkbox('Main Menu')
        add.click_permissionSave()
        """断言：角色授权设置成功"""
        DomAssert(drivers).assert_att('Save Successfully')
        add.click_dialog_Confirm()
        """删除角色"""
        add.click_checkbox(Role)
        add.click_function_button('Delete')
        DomAssert(drivers).assert_att("Successfully")


if __name__ == '__main__':
    pytest.main(['StaffAuthorization_RoleDefinition.py'])
