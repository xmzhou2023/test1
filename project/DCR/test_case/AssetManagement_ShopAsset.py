from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.AssetManagement_ShopAsset import ShopAssetPage
from public.base.assert_ui import ValueAssert, DomAssert
import logging
from libs.common.time_ui import sleep
from public.base.basics import Base
import datetime
import pytest
import allure

@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@allure.feature("资产管理-门店资产")
class TestImportShopAsset:
    @allure.story("导入门店资产")
    @allure.title("门店资产页面，导入门店资产数据")
    @allure.description("门店资产页面，导入门店资产操作")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("Asset Management", "Shop Asset")

        upload = ShopAssetPage(drivers)
        """导入门店资产数据"""
        upload.click_import()
        upload.click_import_save()
        DomAssert(drivers).assert_att('Please upload first.')
        sleep(1)

        upload.upload_true_file('ShopAssetTemplate.xlsx')
        """循环点击查询，直到获取到导入记录状态为Upload Successfully"""
        upload.click_import_status_search()

        today = Base(drivers).get_datetime_today()
        """Import Record 导入记录页面，断言是否新增一条导入成功的记录"""
        get_file_name = upload.get_import_file_name()
        get_status = upload.get_import_status()
        get_total = upload.get_import_total()
        get_success = upload.get_import_success()
        get_failed = upload.get_import_failed()
        get_import_date = upload.get_import_import_date()
        ValueAssert.value_assert_equal('ShopAssetTemplate.xlsx', get_file_name)
        ValueAssert.value_assert_equal('Upload Successfully', get_status)
        ValueAssert.value_assert_equal('1', get_total)
        ValueAssert.value_assert_equal('0', get_success)
        ValueAssert.value_assert_equal('1', get_failed)
        ValueAssert.value_assert_equal(today, get_import_date)
        """关闭当前打开的导入记录菜单"""
        menu = LoginPage(drivers)
        menu.click_close_open_menu()


@allure.feature("资产管理-门店资产")
class TestDeleteShopAsset:
    @allure.story("删除门店资产")
    @allure.title("删除有效状态的门店资产")
    @allure.description("门店资产页面，有效状态的门店资产不支持删除")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("Asset Management", "Shop Asset")

        delete = ShopAssetPage(drivers)
        """筛选Available状态的门店资产数据，进行删除操作"""
        delete.click_unfold_fold('Unfold')
        delete.input_create_date_query('2022-11-14', '2022-11-14')
        delete.click_status_query('Available')
        delete.click_unfold_fold('Fold')
        delete.click_search()
        """断言获取列表字段内容比较是否一致"""
        get_status = delete.get_list_field_content('Get list Status')
        get_picture = delete.get_list_field_content('Get list Picture')
        get_create_date = delete.get_list_field_content('Get list Create Date')
        ValueAssert.value_assert_equal('Available', get_status)
        ValueAssert.value_assert_equal('Picture', get_picture)
        ValueAssert.value_assert_In('2022-11-14', get_create_date)
        """勾选门店资产记录，进行删除操作"""
        delete.click_checkbox()
        delete.click_delete()
        DomAssert(drivers).assert_att('Please retire the asset in the app first')


if __name__ == '__main__':
    pytest.main(['AssetManagement_ShopAsset.py'])
