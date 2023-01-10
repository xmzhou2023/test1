from project.DCR.page_object.StaffAuthorization_UserAndShopAssociation import UserShopAssociaPage
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
        """打开User And Shop Association菜单页面 """
        user.click_gotomenu("Staff & Authorization", "User and Shop Association")
        """ 查询用户与门店关系列表,所有数据加载正常 """
        user_shop = UserShopAssociaPage(drivers)
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


    # @allure.story("查询用户和门店关系")
    # @allure.title("组合条件筛选用户和门店关系数据")
    # @allure.description("组合条件筛选用户和门店关系数据，断言列表加载筛选的数据正确")
    # @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    # @pytest.mark.usefixtures('function_shop_assoc_fixture')
    # def test_001_002(self, drivers):
    #     """DCR 管理员账号登录"""
    #     user = LoginPage(drivers)
    #     user.initialize_login(drivers, "lhmadmin", "dcr123456")
    #     """变量"""
    #     query_dict = {
    #         'User': 'lhmdianzhang',
    #         'Sales Region': '',
    #         'Brand': 'TECNO',
    #         'Shop Type': '',
    #         'Position': '',
    #         'Manpower Type': '',
    #         'Shop': '',
    #         'Country': ''
    #     }
    #     query = UserShopAssociaPage(drivers)
    #     """打开User And Shop Association菜单页面 """
    #     user.click_gotomenu("Staff & Authorization", "User and Shop Association")
    #     query.click_unfold_or_fold('Unfold')
    #     query.random_Query_Method(query_dict)


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
        """打开User And Shop Association菜单页面 """
        user.click_gotomenu("Staff & Authorization", "User and Shop Association")
        export = UserShopAssociaPage(drivers)
        sleep(5)
        # 获取日期
        today = Base(drivers).get_datetime_today()
        export.input_user_or_shop_query("lhmdianzhang", 'User')
        export.click_search()
        export.assert_contains_user_and_shop_assoc_field('User ID', 'lhmdianzhang')
        export.assert_contains_user_and_shop_assoc_field('User Name', 'lhmdianzhang')
        export.assert_contains_user_and_shop_assoc_field('Position', 'lhm店长')
        export.assert_contains_user_and_shop_assoc_field('Shop ID', 'EG000706')
        export.assert_contains_user_and_shop_assoc_field('Shop Name', 'EG000706')
        """ 断言判读分页总条数，是否能查询到数据且大于1条 """
        total = export.get_total_text()
        export.assert_total2(total)
        """点击导出功能"""
        export.click_export()
        export.click_download_more()
        export.input_task_name("Staff And Shop Association")
        down_status = export.click_export_search()
        export.assert_contains_user_and_shop_assoc_field('Download Status', down_status)
        export.assert_contains_user_and_shop_assoc_field('Task Name', 'Staff And Shop Association')
        export.assert_contains_user_and_shop_assoc_field('User ID', 'lhmadmin')
        export.assert_contains_user_and_shop_assoc_field('Create Date	', today)
        export.assert_contains_user_and_shop_assoc_field('Completed Date	', today)
        export.assert_contains_user_and_shop_assoc_field('Operation', 'Download')
        export_time = export.get_export_time_text()
        file_size = export.get_file_size_text()
        export.assert_file_time_size(file_size, export_time)
        #export.click_close_export_record()
        #export.click_close_user_shop_assoc()


# @allure.feature("员工授权-用户和门店关系")
# class TestDeleteUserShopAssociation:
#     @allure.story("删除用户和门店关系")
#     @allure.title("用户和门店关系列表，筛选User ID：lhmdianzhang关联的门店，并导出筛选的数据")
#     @allure.description("用户和门店关系列表，筛选User ID：lhmdianzhang关联的门店，并导出筛选的数据")
#     @allure.severity("normal")   #  critical\normal\minor
#     @pytest.mark.usefixtures('function_shop_assoc_fixture')
#     def test_003_001(self, drivers):
#         """ 根据 Userid：lhmdianzhang，筛选关联的门店，并导出筛选的数据 """
#         user = LoginPage(drivers)
#         user.initialize_login(drivers, "lhmadmin", "dcr123456")
#         """打开User And Shop Association菜单页面 """
#         user.click_gotomenu("Staff & Authorization", "User and Shop Association")
#         delete = UserShopAssociaPage(drivers)
#         sleep(5)
#         """ 根据User ID与 Shop ID条件进行搜索待删除的数据 """
#         delete.user_and_shop_query('Unfold')
#         """ 在列表中，进行删除导入的用户和门店关系数据 """
#         delete.click_delete_operation('Fold')
#         get_list_total = delete.get_total_text()
#         ValueAssert.value_assert_equal('0', get_list_total)
#
#
# @allure.feature("员工授权-用户和门店关系")
# class TestImportUserShopAssociation:
#     @allure.story("导入用户和门店关系")
#     @allure.title("用户和门店关系列表，导入用户和门店关系数据")
#     @allure.description("用户和门店关系列表，导入用户和门店关系数据，断言导入是否成功")
#     @allure.severity("normal")   #  critical\normal\minor
#     @pytest.mark.usefixtures('function_shop_assoc_fixture')
#     def test_004_001(self, drivers):
#         """ 根据 Userid：lhmdianzhang，筛选关联的门店，并导出筛选的数据 """
#         menu = LoginPage(drivers)
#         menu.initialize_login(drivers, "lhmadmin", "dcr123456")
#         """打开User And Shop Association菜单页面 """
#         menu.click_gotomenu("Staff & Authorization", "User and Shop Association")
#         upload = UserShopAssociaPage(drivers)
#         sleep(5)
#         upload.click_import()
#         upload.click_upload_save('Employee+Shop+Association+Template.xlsx')
#         """获取当天日期"""
#         today = Base(drivers).get_datetime_today()
#         """根据Import Date条件筛选当天导入的数据"""
#         upload.import_record_import_date_query(today)
#         """循环点击查询，直到获取到导入记录状态为Upload Successfully"""
#         upload.click_import_status_search()
#         """Import Record 导入记录页面，断言是否新增一条导入成功的记录"""
#         upload.assert_contains_user_and_shop_assoc_field('File Name', 'Employee+Shop+Association+Template.xlsx')
#         upload.assert_contains_user_and_shop_assoc_field('Status', 'Upload Successfully')
#         upload.assert_contains_user_and_shop_assoc_field('Total', '1')
#         upload.assert_contains_user_and_shop_assoc_field('Success', '1')
#         upload.assert_contains_user_and_shop_assoc_field('Failed', '0')
#         upload.assert_contains_user_and_shop_assoc_field('Import Date', today)
#         """关闭当前打开的导入记录菜单"""
#         menu.click_close_open_menu()
#         """根据导入的客户ID，筛选导入的数据，然后进行删除操作"""
#         upload.click_search()
#         upload.input_user_or_shop_query('lhmdianzhang', 'User')
#         upload.click_search()
#         """断言User Salary Management 页面，是否加载导入成的数据"""
#         upload.assert_user_and_shop_assoc_field('User ID', 'lhmdianzhang')
#         upload.assert_user_and_shop_assoc_field('User Name', 'lhmdianzhang')
#         upload.assert_user_and_shop_assoc_field('Position', 'EG000706')
#         upload.assert_user_and_shop_assoc_field('Shop ID', 'EG000706')
#         """删除导入的数据"""
#         """ 根据User ID与 Shop ID条件进行搜索待删除的数据 """
#         upload.user_and_shop_query('Unfold')
#         """ 在列表中，进行删除导入的用户和门店关系数据 """
#         upload.click_delete_operation('Fold')
#         get_list_total = upload.get_total_text()
#         ValueAssert.value_assert_equal('0', get_list_total)


if __name__ == '__main__':
    pytest.main(['StaffAuthorization_UserAndShopAssociation.py'])
