from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.RebateAchievement_UserSalaryManagement import UserSalaryManagement
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.time_ui import sleep
from public.base.basics import Base
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

@allure.feature("返利模块-员工工资管理")
class TestUserSalaryManagement:
    @allure.story("导入、删除员工工资")
    @allure.title("员工工资管理页面，导入、删除员工工资操作")
    @allure.description("员工工资管理页面，导入、删除员工工资操作，断言列表是否显示导入的员工工资数据")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Rebate & Achievement", "User Salary Management")

        upload = UserSalaryManagement(drivers)
        upload.click_import()
        upload.click_import_save()
        DomAssert(drivers).assert_att('Please upload first.')
        sleep(1)
        upload.upload_true_file()

        upload.click_search()
        today = Base(drivers).get_datetime_today()
        """Import Record 导入记录页面，断言是否新增一条导入成功的记录"""
        get_file_name = upload.get_import_file_name()
        get_status = upload.get_import_status()
        get_total = upload.get_import_total()
        get_success = upload.get_import_success()
        get_failed = upload.get_import_failed()
        get_import_date = upload.get_import_import_date()
        ValueAssert.value_assert_In('StaffSalaryTemplate', get_file_name)
        ValueAssert.value_assert_equal('Upload Successfully', get_status)
        ValueAssert.value_assert_equal('2', get_total)
        ValueAssert.value_assert_equal('2', get_success)
        ValueAssert.value_assert_equal('0', get_failed)
        ValueAssert.value_assert_equal(today, get_import_date)

        """关闭当前打开的菜单"""
        menu = LoginPage(drivers)
        menu.click_close_open_menu()
        sleep(1)
        """根据导入的员工ID，筛选导入的数据，然后进行删除操作"""
        upload.input_user_query_search('lhmdianzhang')
        """删除导入的员工工资数据"""
        upload.click_first_checkbox()
        upload.click_delete()
        DomAssert(drivers).assert_att('Deleted Successfully')


    @allure.story("导入错误的文件")
    @allure.title("员工工资管理页面，导入错误的文件，导入失败")
    @allure.description("员工工资管理页面，导入错误的员工工资操作，断言导入记录页面，导入状态失败")
    @allure.severity("minor")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Rebate & Achievement", "User Salary Management")

        upload = UserSalaryManagement(drivers)
        upload.click_import()
        upload.click_import_save()
        DomAssert(drivers).assert_att('Please upload first.')
        sleep(1)
        upload.upload_wrong_file()

        today = Base(drivers).get_datetime_today()
        """Import Record 导入记录页面，断言是否新增一条导入成功的记录"""
        get_file_name = upload.get_import_file_name()
        get_status = upload.get_import_status()
        get_total = upload.get_import_total()
        get_success = upload.get_import_success()
        get_failed = upload.get_import_failed()
        get_fail_data = upload.get_import_fail_data()
        get_import_date = upload.get_import_import_date()
        ValueAssert.value_assert_In('CustomerTemplate', get_file_name)
        ValueAssert.value_assert_equal('Upload Successfully', get_status)
        ValueAssert.value_assert_equal('1', get_total)
        ValueAssert.value_assert_equal('0', get_success)
        ValueAssert.value_assert_equal('1', get_failed)
        ValueAssert.value_assert_In('Download Failed', get_fail_data)
        ValueAssert.value_assert_equal(today, get_import_date)
        """关闭当前打开的菜单"""
        menu = LoginPage(drivers)
        menu.click_close_open_menu()


if __name__ == '__main__':
    pytest.main(['RebateAchievement_UserSalaryManagement.py'])
