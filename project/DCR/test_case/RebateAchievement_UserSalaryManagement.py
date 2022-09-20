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

# @allure.feature("返利模块-员工工资管理")
# class TestQueryUserSalaryMgt:
#     @allure.story("查询员工工资单")
#     @allure.title("工资管理页面，根据国家筛选员工工资单，列表数据加载")
#     @allure.description("工资管理页面，根据国家筛选员工工资单，断言列表是否能查询到数据")
#     @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
#     @pytest.mark.usefixtures('function_menu_fixture')
#     def test_001_001(self, drivers):
#         user = LoginPage(drivers)
#         user.initialize_login(drivers, "lhmadmin", "dcr123456")
#         """打开考勤与巡店管理-打开巡店记录页面"""
#         user.click_gotomenu("Rebate & Achievement", "User Salary Management")
#
#         query = UserSalaryManagement(drivers)
#         """根据User ID，筛选导入的数据，然后进行删除操作"""
#         query.input_country_query_search('China')
#
#         get_total = query.get_list_total()
#         logging.info("获取User Salary Management页面Total分页总条数：{}".format(get_total))
#         query.assert_total(get_total)
#         get_user_id = query.get_list_user_id()
#         get_yyyy_mm = query.get_list_yyyy_mm()
#         get_position = query.get_list_position()
#         get_basic_salary = query.get_list_basic_salary()
#         get_bonus = query.get_list_bonus_incentive()
#         get_country = query.get_list_country()
#         ValueAssert.value_assert_IsNoneNot(get_user_id)
#         ValueAssert.value_assert_IsNoneNot(get_yyyy_mm)
#         ValueAssert.value_assert_IsNoneNot(get_position)
#         ValueAssert.value_assert_IsNoneNot(get_basic_salary)
#         ValueAssert.value_assert_IsNoneNot(get_bonus)
#         ValueAssert.value_assert_equal('China', get_country)
#
#
# @allure.feature("返利模块-员工工资管理")
# class TestEditUserSalaryMgt:
#     @allure.story("编辑员工工资")
#     @allure.title("员工工资管理页面，编辑员工基本工资操作")
#     @allure.description("员工工资管理页面，编辑员工基本工资操作，断言列表是否显示编辑后的基本工资")
#     @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
#     @pytest.mark.usefixtures('function_menu_fixture')
#     def test_002_001(self, drivers):
#         user = LoginPage(drivers)
#         user.initialize_login(drivers, "lhmadmin", "dcr123456")
#         """打开考勤与巡店管理-打开巡店记录页面"""
#         user.click_gotomenu("Rebate & Achievement", "User Salary Management")
#
#         edit = UserSalaryManagement(drivers)
#         """根据User ID，筛选导入的数据，然后进行删除操作"""
#         edit.input_user_query_search('lhmdianzhang')
#         edit.click_edit()
#         edit.input_edit_basic_salary('5588', '6050')
#         edit.click_edit()
#         DomAssert(drivers).assert_att('Edited Successfully')


@allure.feature("返利模块-员工工资管理")
class TestImportDeleteSalaryMgt:
    @allure.story("导入、删除员工工资单")
    @allure.title("员工工资管理页面，导入、删除员工工资操作")
    @allure.description("员工工资管理页面，导入、删除员工工资操作，断言列表是否显示导入的员工工资数据")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开考勤与巡店管理-打开巡店记录页面"""
        user.click_gotomenu("Rebate & Achievement", "User Salary Management")
        upload = UserSalaryManagement(drivers)

        """根据导入的员工ID，筛选导入的数据，然后进行删除操作"""
        upload.input_user_query_search('lhmdianzhang')
        total1 = self.get_list_total()
        """" User Salary Management页面，导入前获取列表总条数，如果大于2条以上记录，先删除重复的工资单 """
        upload.delete_repetitive_salary(total1)

        upload.click_import()
        upload.click_import_save()
        DomAssert(drivers).assert_att('Please upload first.')
        sleep(1)
        upload.upload_true_file('StaffSalaryTemplate.xlsx')

        upload.click_import_record_search()
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

        """根据导入的员工ID，筛选导入的数据，然后进行删除操作"""
        upload.input_user_query_search('lhmdianzhang')
        """断言User Salary Management 页面，是否加载导入成的数据"""
        get_user_id = upload.get_list_user_id()
        get_yyyy_mm = upload.get_list_yyyy_mm()
        get_position = upload.get_list_position()
        get_basic_salary = upload.get_list_basic_salary()
        get_incentive = upload.get_list_bonus_incentive()
        logging.info("打印获取列表User ID字段内容：{}".format(get_user_id))
        logging.info("打印获取列表yyyy mm段内容：{}".format(get_yyyy_mm))
        logging.info("打印获取列表position 字段内容：{}".format(get_position))
        logging.info("打印获取列表basic salary字段内容：{}".format(get_basic_salary))
        logging.info("打印获取列表bonus incentive 字段内容：{}".format(get_incentive))
        ValueAssert.value_assert_equal('lhmdianzhang', get_user_id)
        ValueAssert.value_assert_IsNoneNot(get_yyyy_mm)
        ValueAssert.value_assert_IsNoneNot(get_position)
        ValueAssert.value_assert_equal('5100.00', get_basic_salary)
        ValueAssert.value_assert_IsNoneNot(get_incentive)

        """删除导入的员工工资数据"""
        upload.click_first_checkbox2()
        upload.click_delete()
        DomAssert(drivers).assert_att('Deleted Successfully')


    # @allure.story("Import导入错误的文件")
    # @allure.title("员工工资管理页面，Import导入错误的文件，导入失败")
    # @allure.description("员工工资管理页面，Import导入错误的员工工资操作，断言导入记录页面，导入状态失败")
    # @allure.severity("minor")  # 分别为3种类型等级：critical\normal\minor
    # @pytest.mark.usefixtures('function_menu_fixture')
    # def test_003_002(self, drivers):
    #     user = LoginPage(drivers)
    #     user.initialize_login(drivers, "lhmadmin", "dcr123456")
    #
    #     """打开考勤与巡店管理-打开巡店记录页面"""
    #     user.click_gotomenu("Rebate & Achievement", "User Salary Management")
    #
    #     upload = UserSalaryManagement(drivers)
    #     upload.click_import()
    #     upload.upload_wrong_file('CustomerTemplate1.xlsx')
    #
    #     upload.click_import_record_search()
    #     today = Base(drivers).get_datetime_today()
    #     """Import Record 导入记录页面，断言是否新增一条导入成功的记录"""
    #     get_file_name = upload.get_import_file_name()
    #     get_status = upload.get_import_status()
    #     get_total = upload.get_import_total()
    #     get_success = upload.get_import_success()
    #     get_failed = upload.get_import_failed()
    #     get_fail_data = upload.get_import_fail_data()
    #     get_import_date = upload.get_import_import_date()
    #     ValueAssert.value_assert_In('CustomerTemplate1', get_file_name)
    #     ValueAssert.value_assert_equal('Upload Successfully', get_status)
    #     ValueAssert.value_assert_equal('1', get_total)
    #     ValueAssert.value_assert_equal('0', get_success)
    #     ValueAssert.value_assert_equal('1', get_failed)
    #     ValueAssert.value_assert_In('Download Failed', get_fail_data)
    #     ValueAssert.value_assert_equal(today, get_import_date)
    #     """关闭当前打开的菜单"""
    #     menu = LoginPage(drivers)
    #     menu.click_close_open_menu()


    # @allure.story("导入、删除工资明细单")
    # @allure.title("员工工资管理页面，导入、删除工资明细单操作")
    # @allure.description("员工工资管理页面，导入、删除工资明细单，断言列表是否显示导入的员工工资明细单数据")
    # @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    # @pytest.mark.usefixtures('function_menu_fixture')
    # def test_003_003(self, drivers):
    #     user = LoginPage(drivers)
    #     user.initialize_login(drivers, "lhmadmin", "dcr123456")
    #     """打开考勤与巡店管理-打开巡店记录页面"""
    #     user.click_gotomenu("Rebate & Achievement", "User Salary Management")
    #     upload2 = UserSalaryManagement(drivers)
    #
    #     """根据导入的员工ID，筛选导入的数据，然后进行删除操作"""
    #     upload2.input_user_query_search('lhmdianzhang')
    #     total2 = self.get_list_total()
    #     """" User Salary Management页面，导入前获取列表总条数，如果大于2条以上记录，先删除重复的工资单 """
    #     upload2.delete_repetitive_salary(total2)
    #
    #     upload2.click_import_payslip()
    #     upload2.click_import_save()
    #     DomAssert(drivers).assert_att('Please upload first.')
    #     sleep(1)
    #     upload2.upload_true_file('PaySlipTemplate.xlsx')
    #
    #     upload2.click_import_record_search()
    #     today = Base(drivers).get_datetime_today()
    #     """Import Record 导入记录页面，断言是否新增一条导入成功的记录"""
    #     get_file_name = upload2.get_import_file_name()
    #     get_status = upload2.get_import_status()
    #     get_total = upload2.get_import_total()
    #     get_success = upload2.get_import_success()
    #     get_failed = upload2.get_import_failed()
    #     get_import_date = upload2.get_import_import_date()
    #     ValueAssert.value_assert_equal('PaySlipTemplate.xlsx', get_file_name)
    #     ValueAssert.value_assert_equal('Upload Successfully', get_status)
    #     ValueAssert.value_assert_equal('1', get_total)
    #     ValueAssert.value_assert_equal('1', get_success)
    #     ValueAssert.value_assert_equal('0', get_failed)
    #     ValueAssert.value_assert_equal(today, get_import_date)
    #     """关闭当前打开的菜单"""
    #     menu = LoginPage(drivers)
    #     menu.click_close_open_menu()
    #
    #     """根据导入的员工ID，筛选导入的数据，然后进行删除操作"""
    #     upload2.input_user_query_search('lhmdianzhang')
    #     """断言User Salary Management 页面，是否加载导入成的数据"""
    #     get_user_id = upload2.get_list_user_id()
    #     get_yyyy_mm = upload2.get_list_yyyy_mm()
    #     get_position = upload2.get_list_position()
    #     get_basic_salary = upload2.get_list_basic_salary()
    #     get_incentive = upload2.get_list_bonus_incentive()
    #     logging.info("打印获取列表User ID字段内容：{}".format(get_user_id))
    #     logging.info("打印获取列表yyyy mm段内容：{}".format(get_yyyy_mm))
    #     logging.info("打印获取列表position 字段内容：{}".format(get_position))
    #     logging.info("打印获取列表basic salary字段内容：{}".format(get_basic_salary))
    #     logging.info("打印获取列表bonus incentive 字段内容：{}".format(get_incentive))
    #     ValueAssert.value_assert_equal('lhmdianzhang', get_user_id)
    #     ValueAssert.value_assert_equal('2022-09', get_yyyy_mm)
    #     ValueAssert.value_assert_IsNoneNot(get_position)
    #     ValueAssert.value_assert_equal('5880.00', get_basic_salary)
    #     ValueAssert.value_assert_equal('656.00', get_incentive)
    #
    #     """删除导入的员工工资数据"""
    #     upload2.click_first_checkbox1()
    #     upload2.click_delete()
    #     DomAssert(drivers).assert_att('Deleted Successfully')
    #

    # @allure.story("Import Payslip 导入错误的文件")
    # @allure.title("员工工资管理页面，Import Payslip 导入错误的文件，导入失败")
    # @allure.description("员工工资管理页面，Import Payslip 导入错误的员工工资操作，断言导入记录页面，导入状态失败")
    # @allure.severity("minor")  # 分别为3种类型等级：critical\normal\minor
    # @pytest.mark.usefixtures('function_menu_fixture')
    # def test_003_004(self, drivers):
    #     user = LoginPage(drivers)
    #     user.initialize_login(drivers, "lhmadmin", "dcr123456")
    #
    #     """打开考勤与巡店管理-打开巡店记录页面"""
    #     user.click_gotomenu("Rebate & Achievement", "User Salary Management")
    #
    #     upload = UserSalaryManagement(drivers)
    #     upload.click_import_payslip()
    #     upload.upload_wrong_file('CustomerTemplate2.xlsx')
    #
    #     upload.click_import_record_search()
    #     today = Base(drivers).get_datetime_today()
    #     """Import Record 导入记录页面，断言是否新增一条导入成功的记录"""
    #     get_file_name = upload.get_import_file_name()
    #     get_status = upload.get_import_status()
    #     get_total = upload.get_import_total()
    #     get_success = upload.get_import_success()
    #     get_failed = upload.get_import_failed()
    #     get_fail_data = upload.get_import_fail_data()
    #     get_import_date = upload.get_import_import_date()
    #     ValueAssert.value_assert_In('CustomerTemplate2', get_file_name)
    #     ValueAssert.value_assert_equal('Upload Successfully', get_status)
    #     ValueAssert.value_assert_equal('1', get_total)
    #     ValueAssert.value_assert_equal('0', get_success)
    #     ValueAssert.value_assert_equal('1', get_failed)
    #     ValueAssert.value_assert_In('Download Failed', get_fail_data)
    #     ValueAssert.value_assert_equal(today, get_import_date)
    #     """关闭当前打开的菜单"""
    #     menu = LoginPage(drivers)
    #     menu.click_close_open_menu()


if __name__ == '__main__':
    pytest.main(['RebateAchievement_UserSalaryManagement.py'])
