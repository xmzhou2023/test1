from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.GTMManagement_MonitoringTemplate import MonitoringTemplatePage
from public.base.assert_ui import ValueAssert, DomAssert
import logging
from libs.common.connect_sql import *
from libs.common.time_ui import sleep
from public.base.basics import Base
import datetime
import pytest
import allure

"""后置关闭菜单方法  pytest.fixture(scope='作用域' function函数级别  """
@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()


@allure.feature("GTM管理-预警模板")
class TestAddMonitorTemplate:
    @allure.story("新增预警模板")
    @allure.title("预警模板页面，新增预警模板,选择Inventory Monitor类型的预警模板")
    @allure.description("预警模板页面，新增预警模板操作，断言列表是否加载新增的预警模板")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("GTM Management", "Monitoring Template")

        add = MonitoringTemplatePage(drivers)
        """随机生成title后面的编号"""
        num = add.asset_random()
        title_name = "InventoryMonitor"+num
        """点击新增预警模板按钮"""
        add.click_add_monitoring()
        add.add_basic_information(title_name, 'itel', 'Bangladesh', 'Inventory Monitor', '8', 'it2191', '2022-11-01', '2022-11-30', 'CHIN', 'Zone Shop', 'Unmanned', 'By 3 Days', 'lhm二代')

        """点击提交按钮"""
        add.click_add_submit()
        DomAssert(drivers).assert_att('SUCCESS')
        """根据Title 条件查询预警"""
        add.query_title(title_name)
        """点击查询按钮"""
        add.click_search()
        """断言列表是否加载新增的预警模板"""
        get_title = add.get_list_field_content("Get list Title")
        get_brand = add.get_list_field_content("Get list Brand")
        get_country = add.get_list_field_content("Get list Country")
        get_monitor_type = add.get_list_field_content("Get list Monitor Type")
        get_shop_type = add.get_list_field_content("Get list Shop Type")
        get_frequency = add.get_list_field_content('Get list Frequency')
        get_status = add.get_list_field_content('Get list Status')
        ValueAssert.value_assert_equal(title_name, get_title)
        ValueAssert.value_assert_equal('itel', get_brand)
        ValueAssert.value_assert_equal('Bangladesh', get_country)
        ValueAssert.value_assert_equal('Inventory Monitor', get_monitor_type)
        ValueAssert.value_assert_equal('CHIN', get_shop_type)
        ValueAssert.value_assert_equal('By 3 Days', get_frequency)
        ValueAssert.value_assert_In('Enabled', get_status)

        add.query_title(title_name)
        """点击查询按钮"""
        add.click_search()
        """勾选筛选后预警模板"""
        add.click_check_box()
        """点击Disable按钮"""
        add.click_disable_button()
        """断言查询该预警记录是否更新为 Disable状态"""
        add.query_title_status(get_title, 'Disabled')
        add.click_search()
        get_title = add.get_list_field_content("Get list Title")
        get_status = add.get_list_field_content('Get list Status')
        ValueAssert.value_assert_equal(get_title, get_title)
        ValueAssert.value_assert_In('Disabled', get_status)


    @allure.story("新增预警模板")
    @allure.title("预警模板页面，新增预警模板，选择Sale Monitor类型的预警模板")
    @allure.description("预警模板页面，新增预警模板操作，断言列表是否加载新增的预警模板")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("GTM Management", "Monitoring Template")

        add = MonitoringTemplatePage(drivers)
        """随机生成title后面的编号"""
        num = add.asset_random()
        title_name = "SaleMonitor"+num
        """点击新增预警模板按钮"""
        add.click_add_monitoring()
        add.add_basic_information(title_name, 'TECNO', 'Pakistan', 'Sale Monitor', '7', 'BB4j 32+2', '2022-11-01', '2022-11-30', 'GRT', 'Zone Shop', 'Manned', 'Weekly', 'Distributor')

        """点击提交按钮"""
        add.click_add_submit()
        DomAssert(drivers).assert_att('SUCCESS')
        """根据Title 条件查询预警"""
        add.query_title(title_name)
        """点击查询按钮"""
        add.click_search()
        """断言列表是否加载新增的预警模板"""
        get_title = add.get_list_field_content("Get list Title")
        get_brand = add.get_list_field_content("Get list Brand")
        get_country = add.get_list_field_content("Get list Country")
        get_monitor_type = add.get_list_field_content("Get list Monitor Type")
        get_shop_type = add.get_list_field_content("Get list Shop Type")
        get_frequency = add.get_list_field_content('Get list Frequency')
        get_status = add.get_list_field_content('Get list Status')
        ValueAssert.value_assert_equal(title_name, get_title)
        ValueAssert.value_assert_equal('TECNO', get_brand)
        ValueAssert.value_assert_equal('Pakistan', get_country)
        ValueAssert.value_assert_equal('Sale Monitor', get_monitor_type)
        ValueAssert.value_assert_equal('GRT', get_shop_type)
        ValueAssert.value_assert_equal('Weekly', get_frequency)
        ValueAssert.value_assert_In('Enabled', get_status)


@allure.feature("GTM管理-预警模板")
class TestEditMonitorTemplate:
    @allure.story("编辑预警模板")
    @allure.title("预警模板页面，编辑预警模板")
    @allure.description("预警模板页面，编辑预警模板操作，断言列表是否加载新增的预警模板")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("GTM Management", "Monitoring Template")

        edit = MonitoringTemplatePage(drivers)
        """根据Title 条件查询预警"""
        get_title = edit.get_list_field_content("Get list Title")
        edit.query_title(get_title)
        """点击查询按钮"""
        edit.click_search()

        """点击编辑按钮"""
        edit.click_edit()
        """随机生成title后面的编号"""
        num = edit.asset_random()
        title_name = "SaleMonitor"+num
        """编辑预警模板基本信息"""
        edit.edit_basic_information(title_name, 'SIS', 'Exclusive Shop', 'Manned-Flexi')
        """点击提交按钮"""
        edit.click_add_submit()

        """根据修改后的title 条件查询预警"""
        edit.query_title(title_name)
        """点击查询按钮"""
        edit.click_search()
        """断言列表是否展示更新后的字段内容"""
        get_title = edit.get_list_field_content("Get list Title")
        get_shop_type = edit.get_list_field_content("Get list Shop Type")
        get_status = edit.get_list_field_content('Get list Status')
        ValueAssert.value_assert_equal(title_name, get_title)
        ValueAssert.value_assert_In('SIS', get_shop_type)
        ValueAssert.value_assert_In('Enabled', get_status)


@allure.feature("GTM管理-预警模板")
class TestDisableMonitorTemplate:
    @allure.story("失效预警模板")
    @allure.title("预警模板页面，将新增的预警模板失效")
    @allure.description("预警模板页面，将新增的预警模板失效操作,断言列表该记录是否更新为Disabled状态")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("GTM Management", "Monitoring Template")

        disable = MonitoringTemplatePage(drivers)
        """根据Title 条件查询预警"""
        get_title = disable.get_list_field_content("Get list Title")
        disable.query_title(get_title)
        """点击查询按钮"""
        disable.click_search()

        """勾选筛选后预警模板"""
        disable.click_check_box()
        """点击Disable按钮"""
        disable.click_disable_button()

        """断言查询该预警记录是否更新为 Disable状态"""
        disable.query_title_status(get_title, 'Disabled')
        disable.click_search()
        get_title = disable.get_list_field_content("Get list Title")
        get_status = disable.get_list_field_content('Get list Status')
        ValueAssert.value_assert_equal(get_title, get_title)
        ValueAssert.value_assert_In('Disabled', get_status)


if __name__ == '__main__':
    pytest.main(['GTMManagement_MonitoringTemplate.py'])
