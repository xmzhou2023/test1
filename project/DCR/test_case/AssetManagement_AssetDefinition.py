from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.AssetManagement_AssetDefinition import AssetDefinitionPage
from public.base.assert_ui import ValueAssert, DomAssert
import logging
from libs.common.time_ui import sleep
from public.base.basics import Base
import datetime
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_export_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    for i in range(2):
        get_menu_class = menu.get_open_menu_class()
        class_value = "tags-view-item router-link-exact-active router-link-active active"
        if class_value == str(get_menu_class):
            menu.click_close_open_menu()
            sleep(1)

@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()


@allure.feature("考勤&巡店-考勤记录")
class TestAddAsset:
    @allure.story("新增资产")
    @allure.title("资产管理页面，新增资产")
    @allure.description("资产管理页面，新增资产操作，断言资产管理列表是否加载新增的资产信息")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """考勤管理-打开考勤记录页面"""
        user.click_gotomenu("Asset Management", "Asset Definition")

        add = AssetDefinitionPage(drivers)
        #点击add新增按钮
        add.click_add_asset()
        #新增资产
        add.add_asset('TECNO', 'Headquarters', 'Shop Construction Props', 'TECNO Smart Phone', 'TECNO智能手机', 'V123')
        add.click_upload_picture('20211207_110302.png')
        DomAssert(drivers).assert_att("Success")
        add.click_add_submit()

        #查询新建的资产信息
        # """获取当天日期"""
        # base = Base(drivers)
        # today = base.get_datetime_today()
        # add.query_create_date('2022-09-02')
        # add.query_category('POSM')
        # add.click_search()
        # #返回Asset Definition列表，查询是否加载新增的资产信息
        # brand = add.get_list_field_content('Get list Brand')
        # design_by = add.get_list_field_content('Get list Design By')
        # category = add.get_list_field_content('Get list Category')
        # version = add.get_list_field_content('Get list Version')
        # asset_name_cn = add.get_list_field_content('Get list Asset Name CN')
        # asset_name_en = add.get_list_field_content('Get list Asset Name EN')
        # create_date = add.get_list_field_content('Get list Create Date')
        # #断言相等比较列表字段内容是否一致
        # ValueAssert.value_assert_equal(brand, 'TECNO')
        # ValueAssert.value_assert_equal(design_by, 'Headquarters')
        # ValueAssert.value_assert_equal(category, 'POSM')
        # ValueAssert.value_assert_equal(version, 'V1.0')
        # ValueAssert.value_assert_equal(asset_name_cn, 'CJP20220902(CN)')
        # ValueAssert.value_assert_equal(asset_name_en, 'CJP20220902(EN)')
        # ValueAssert.value_assert_In('2022-09-02', create_date)



if __name__ == '__main__':
    pytest.main(['AssetManagement_AssetDefinition.py'])
