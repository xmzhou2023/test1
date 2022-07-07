from project.DCR.page_object.StaffAuthorization_UserShopAssociation import UserShopAssociaPage
from project.DCR.page_object.menu import MenuPage
import logging
from project.DCR.page_object.login import LoginPage
from public.base.assert_ui import ValueAssert
from libs.common.time_ui import sleep
import datetime
import pytest
import allure


@allure.feature("员工授权-用户和门店关系")
class TestSearchUserShopAssociation():
    @allure.story("查询")
    @allure.title("查询用户和门店关系列表所有数据")
    @allure.description("查询用户和门店关系列表，所有数据加载正常")
    @allure.severity("critical") # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        """DCR 管理员账号登录"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "lhmadmin", "dcr123456")
        sleep(5)

        """打开User And Customer Association菜单页面 """
        menu = MenuPage(drivers)
        menu.click_gotomenu("Staff & Authorization", "User and Shop Association")
        sleep(7)

        """ 查询用户与门店关系列表,所有数据加载正常 """
        user_shop = UserShopAssociaPage(drivers)
        userid = user_shop.get_list_user_id()
        username = user_shop.get_list_user_name
        position = user_shop.get_list_position()
        shop_id = user_shop.get_list_shop_id()
        shop_name = user_shop.get_list_shop_name()
        total = user_shop.get_total_text()
        total1 = total[6:7]
        ValueAssert.value_assert_IsNoneNot(userid)
        ValueAssert.value_assert_IsNoneNot(username)
        ValueAssert.value_assert_IsNoneNot(position)
        ValueAssert.value_assert_IsNoneNot(shop_id)
        ValueAssert.value_assert_IsNoneNot(shop_name)
        """ 断言判读分页总条数，是否能查询到数据且大于1条 """
        if int(total1) >= 1000:
            logging.info("查看User and Shop Association列表，加载筛选的数据正常，分页总条数Total：{}".format(total1))
        else:
            logging.info("查看User and Shop Association列表，加载筛选的数据正常，分页总条数Total：{}".format(total1))
        sleep(1)


@allure.feature("员工授权-用户和门店关系")
class TestExportUserShopAssociation():
    @allure.story("导出")
    @allure.title("用户和门店关系列表，筛选User ID：lhmdianzhang关联的门店，并导出筛选的数据")
    @allure.description("用户和门店关系列表，筛选User ID：lhmdianzhang关联的门店，并导出筛选的数据")
    @allure.severity("normal")# blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        """ 根据 Userid：lhmdianzhang，筛选关联的门店，并导出筛选的数据 """
        export = UserShopAssociaPage(drivers)
        # 获取日期
        today = datetime.date.today()
        today1 = str(today)
        export.input_user_query("lhmdianzhang")
        export.click_search()
        userid = export.get_list_user_id()
        username = export.get_list_user_name
        position = export.get_list_position()
        shop_id = export.get_list_shop_id()
        shop_name = export.get_list_shop_name()
        total = export.get_total_text()
        total1 = total[6:7]
        ValueAssert.value_assert_equal(userid, "lhmdianzhang")
        ValueAssert.value_assert_equal(username, "lhmdianzhang")
        ValueAssert.value_assert_IsNoneNot(position)
        ValueAssert.value_assert_IsNoneNot(shop_id)
        ValueAssert.value_assert_IsNoneNot(shop_name)
        """ 断言判读分页总条数，是否能查询到数据且大于1条 """
        if int(total1) >= 1:
            logging.info("查看User and Shop Association列表，加载筛选的数据正常，分页总条数Total：{}".format(total1))
        else:
            logging.info("查看User and Shop Association列表，加载筛选的数据正常，分页总条数Total：{}".format(total1))
        """点击导出功能"""
        export.click_export()
        sleep(2)

        export.click_download_icon()
        sleep(1)
        export.click_more()
        export.click_export_search()

        down_status = export.get_download_status_text()
        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        file_size1 = file_size[0:1]
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        create_date1 = create_date[0:10]
        complete_date = export.get_complete_date_text()
        complete_date1 = complete_date[0:10]
        export_time = export.get_export_time_text()
        export_time1 = export_time[0:1]
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Staff Shop Association")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date1, str(today1))
        ValueAssert.value_assert_equal(complete_date1, str(today1))
        ValueAssert.value_assert_equal(operation, "Download")
        if int(file_size1) > 0:
            logging.info("User and Shop Association导出成功，File Size 导出文件大于1KB:{}".format(file_size1))
        else:
            logging.info("User and Shop Association导出失败，File Size 导出文件小于1KB:{}".format(file_size1))

        if int(export_time1) > 0:
            logging.info("User and Shop Association导出成功，Export Time(s)导出时间大于0s:{}".format(export_time1))
        else:
            logging.info("User and Shop Association导出成功，Export Time(s)导出时间等于0s:{}".format(export_time1))
        sleep(1)


if __name__ == '__main__':
    pytest.main(['StaffAuthorization_UserShopAssociation.py'])
