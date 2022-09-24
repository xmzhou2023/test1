from project.DCR.page_object.StaffAuthorization_UserShopAssociation import UserShopAssociaPage
import logging
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert
from libs.common.time_ui import sleep
from public.base.basics import Base
import datetime
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_shop_assoc_fixture(drivers):
    yield
    close = UserShopAssociaPage(drivers)
    close.click_close_user_shop_assoc()

@pytest.fixture(scope='function')
def function_export_fixture(drivers):
    yield
    close = UserShopAssociaPage(drivers)
    close.click_close_export_record()
    close.click_close_user_shop_assoc()

@allure.feature("员工授权-用户和门店关系")
class TestSearchUserShopAssociation:
    @allure.story("查询用户和门店关系")
    @allure.title("查询用户和门店关系列表所有数据")
    @allure.description("查询用户和门店关系列表，所有数据加载正常")
    @allure.severity("critical")  #  分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_shop_assoc_fixture')
    def test_001_001(self, drivers):
        """DCR 管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开User And Customer Association菜单页面 """
        user.click_gotomenu("Staff & Authorization", "User and Shop Association")

        """ 查询用户与门店关系列表,所有数据加载正常 """
        user_shop = UserShopAssociaPage(drivers)
        sleep(2)
        userid = user_shop.get_list_user_id()
        username = user_shop.get_list_user_name()
        position = user_shop.get_list_position()
        shop_id = user_shop.get_list_shop_id()
        shop_name = user_shop.get_list_shop_name()
        total = user_shop.get_total_text()

        ValueAssert.value_assert_IsNoneNot(userid)
        ValueAssert.value_assert_IsNoneNot(username)
        ValueAssert.value_assert_IsNoneNot(position)
        ValueAssert.value_assert_IsNoneNot(shop_id)
        ValueAssert.value_assert_IsNoneNot(shop_name)
        """ 断言判读分页总条数，是否能查询到数据且大于1条 """
        user_shop.assert_total(total)
        #user_shop.click_close_user_shop_assoc()


@allure.feature("员工授权-用户和门店关系")
class TestExportUserShopAssociation:
    @allure.story("导出用户和门店关系")
    @allure.title("用户和门店关系列表，筛选User ID：lhmdianzhang关联的门店，并导出筛选的数据")
    @allure.description("用户和门店关系列表，筛选User ID：lhmdianzhang关联的门店，并导出筛选的数据")
    @allure.severity("normal")   #  critical\normal\minor
    @pytest.mark.usefixtures('function_export_fixture')
    def test_002_001(self, drivers):
        """ 根据 Userid：lhmdianzhang，筛选关联的门店，并导出筛选的数据 """
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """打开User And Customer Association菜单页面 """
        user.click_gotomenu("Staff & Authorization", "User and Shop Association")

        export = UserShopAssociaPage(drivers)
        # 获取日期
        base = Base(drivers)
        today = base.get_datetime_today()
        export.input_user_query("lhmdianzhang")
        export.click_search()
        userid = export.get_list_user_id()
        username = export.get_list_user_name()
        position = export.get_list_position()
        shop_id = export.get_list_shop_id()
        shop_name = export.get_list_shop_name()
        total = export.get_total_text()
        ValueAssert.value_assert_equal(userid, "lhmdianzhang")
        ValueAssert.value_assert_equal(username, "lhmdianzhang")
        ValueAssert.value_assert_IsNoneNot(position)
        ValueAssert.value_assert_IsNoneNot(shop_id)
        ValueAssert.value_assert_IsNoneNot(shop_name)
        """ 断言判读分页总条数，是否能查询到数据且大于1条 """
        export.assert_total2(total)

        """点击导出功能"""
        export.click_export()
        export.click_download_more()
        export.input_task_name("Staff Shop Association")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Staff Shop Association")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        #export.click_close_export_record()
        #export.click_close_user_shop_assoc()

if __name__ == '__main__':
    pytest.main(['StaffAuthorization_UserShopAssociation.py'])
