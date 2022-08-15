from project.DCR.page_object.StaffAuthorization_UserCustAssociation import UserCustomerAssociaPage
import logging
from libs.common.time_ui import sleep
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert
from public.base.basics import Base
import pytest
import allure


@allure.feature("员工授权-用户和客户关系")
class TestSearchUserCustAssocia:
    @allure.story("查询用户和客户关系")
    @allure.title("查询用户和客户关系列表所有数据")
    @allure.description("查询用户和客户关系列表，所有数据加载正常")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        """DCR 管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开User And Customer Association菜单页面 """
        user.click_gotomenu("Staff & Authorization", "User and Customer Association")

        """ 查询用户与客户关系列表,所有数据加载正常 """
        user_cust = UserCustomerAssociaPage(drivers)
        sleep(40)
        userid = user_cust.get_list_user_id()
        username = user_cust.get_list_user_name()
        position = user_cust.get_list_position()
        customer_id = user_cust.get_list_customer_id()
        customer_name = user_cust.get_list_customer_name()
        total = user_cust.get_total_text()

        ValueAssert.value_assert_IsNoneNot(userid)
        ValueAssert.value_assert_IsNoneNot(username)
        ValueAssert.value_assert_IsNoneNot(position)
        ValueAssert.value_assert_IsNoneNot(customer_id)
        ValueAssert.value_assert_IsNoneNot(customer_name)
        """ 断言判读分页总条数，是否能查询到数据且大于1条 """
        user_cust.assert_total(total)
        user_cust.click_close_user_cust_assoc()


@allure.feature("员工授权-用户和客户关系")
class TestExportUserCustAssocia:
    @allure.story("导出用户和客户关系")
    @allure.title("用户和客户关系列表，筛选User ID：NG2061301关联的客户，并导出筛选的数据")
    @allure.description("用户和客户关系列表，筛选User ID：NG2061301关联的客户，并导出筛选的数据")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开User And Customer Association菜单页面 """
        user.click_gotomenu("Staff & Authorization", "User and Customer Association")

        export = UserCustomerAssociaPage(drivers)
        # 获取日期
        base = Base(drivers)
        today = base.get_datetime_today()

        export.input_user_query("NG2061301")
        export.click_search()
        userid = export.get_list_user_id()
        username = export.get_list_user_name()
        position = export.get_list_position()
        customer_id = export.get_list_customer_id()
        customer_name = export.get_list_customer_name()
        total = export.get_total_text()

        ValueAssert.value_assert_equal("NG2061301", userid)
        ValueAssert.value_assert_equal("xinyanli", username)
        ValueAssert.value_assert_IsNoneNot(position)
        ValueAssert.value_assert_IsNoneNot(customer_id)
        ValueAssert.value_assert_IsNoneNot(customer_name)
        """ 断言判读分页总条数，是否能查询到数据且大于1条 """
        export.assert_total1(total)

        """点击导出功能"""
        export.click_export()
        export.click_download_more()
        export.input_task_name("Staff Customer Association")

        down_status = export.click_export_search()
        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Staff Customer Association")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        export.click_close_export_record()
        export.click_close_user_cust_assoc()

if __name__ == '__main__':
    pytest.main(['StaffAuthorization_UserCustAssociation.py'])

