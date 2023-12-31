from libs.common.time_ui import sleep
from project.DCR_INDIA.page_object.Center_Component import LoginPage
from project.DCR_INDIA.page_object.SalesManagement_ShopSalesQuery import ShopSaleQueryPage
from public.base.assert_ui import ValueAssert, DomAssert
import datetime
import logging
from public.base.basics import Base
import pytest
import allure

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


@allure.feature("销售管理-门店销量查询")
class TestShopSalesQuery:
    @allure.story("门店销量查询")
    @allure.title("门店销售查询页面，查询门店销售查询列表数据加载")
    @allure.description("考勤记录页面，查询门店销售查询列表数据加载，断言数据加载正常")
    @allure.severity("blocker")  # 分别为3种类型等级：blocker\critical\normal
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        #user.dcr_login(drivers, "testsupervisor", "dcr123456")
        """打开销售管理-打开门店销售查询页面"""
        user.click_gotomenu("Sales Management", "Shop Sales Query")
        """查看Shop Sales Query门店销量上报 列表数据加载是否正常"""
        shop_sales = ShopSaleQueryPage(drivers)
        total = shop_sales.get_total_text()
        if int(total) > 0:
            shop_id = shop_sales.get_shop_id_text()
            shop_name = shop_sales.get_shop_name_text()
            status = shop_sales.get_status_text()
            sales_date = shop_sales.get_sales_date_text()
            public_id = shop_sales.get_public_id_text()
            """Shop Sales Query页面，增加断言 对比列表字段与分页总条数是否有数据"""
            ValueAssert.value_assert_IsNoneNot(shop_id)
            ValueAssert.value_assert_IsNoneNot(status)
            ValueAssert.value_assert_IsNoneNot(shop_name)
            ValueAssert.value_assert_IsNoneNot(sales_date)
            ValueAssert.value_assert_IsNoneNot(public_id)
            shop_sales.assert_total(total)
        else:
            shop_sales.assert_total(total)


    @allure.story("门店销量查询")
    @allure.title("门店销售查询页面，按销售开始与结束日期查询 门店销售查询记录，并导出筛选后的数据")
    @allure.description("门店销售查询页面，按销售开始与结束日期查询 门店销售查询记录，并导出筛选后的数据")
    @allure.severity("blocker")  # 分别为3种类型等级：blocker\critical\normal
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_export_fixture')
    def test_001_002(self, drivers):
        #"""刷新页面"""
        #Base(drivers).refresh()
        """打开销售管理-打开门店销售查询页面"""
        menu = LoginPage(drivers)
        menu.click_menu("Sales Management", "Shop Sales Query")
        """实例化对象类"""
        export = ShopSaleQueryPage(drivers)
        today = Base(drivers).get_datetime_today()
        last_date = export.get_last_day(1)
        """根据销售日期筛选门店销售数据"""
        export.click_unfold()
        export.shop_sales_query_sales_date_query(last_date, today)
        export.click_search()
        get_shop_id = export.get_shop_id_text()
        """获取列表Shop ID，进行筛选"""
        export.shop_sales_query_shop_query(get_shop_id)
        export.click_fold()
        """点击Search按钮"""
        export.click_search()
        total = export.get_total_text()
        """Shop Sales Query页面，增加断言 对比列表字段与分页总条数是否有数据"""
        export.assert_total(total)
        #筛选销售日期后，点击导出功能
        export.click_export()
        DomAssert(drivers).assert_att("Create successful , will auto downloaded , please wait")
        export.click_menu("Basic Data Management", "Export Record")
        export.input_task_name('Shop Sales Query')
        export.export_record_create_date_query(today)
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = export.click_export_search()
        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()
        """断言导出记录列表，字段内容是否正确"""
        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Shop Sales Query")
        ValueAssert.value_assert_equal(task_id, "testsupervisor")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)


    @allure.story("门店销量查询")
    @allure.title("逻辑冲突的查询条件查询结果为空：是否激活&激活时间")
    @allure.description("逻辑冲突的查询条件查询结果为空：是否激活&激活时间")
    @pytest.mark.smoke  # 用例标记
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_001_003(self, drivers):
        user = ShopSaleQueryPage(drivers)
        user.click_menu("Sales Management", "Shop Sales Query")
        user.click_unfold()
        user.input_search('Activation Status', 'Not Activated')
        user.input_search('Activation Date', '2019-01-01To2023-12-31')
        user.input_search('Upload Date', '2019-01-01To2023-12-31')
        user.click_search()
        user.assert_NoData()


if __name__ == '__main__':
    pytest.main(['SalesManagement_ShopSalesQuery.py'])
