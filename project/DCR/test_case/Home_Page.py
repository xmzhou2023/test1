from project.DCR.page_object.Center_Component import LoginPage
from public.base.basics import Base
from public.base.assert_ui import ValueAssert
from project.DCR.page_object.Home_Page import HomePagePage
import logging
from libs.common.time_ui import sleep
import datetime
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_user_fixture(drivers):
    yield
    close = HomePagePage(drivers)
    close.click_close_export_record()
    close.click_close_user_management()

@pytest.fixture(scope='function')
def function_customer_fixture(drivers):
    yield
    close = HomePagePage(drivers)
    close.click_close_export_record()
    close.click_close_customer_mgt()

@pytest.fixture(scope='function')
def function_shop_fixture(drivers):
    yield
    close = HomePagePage(drivers)
    close.click_close_export_record()
    close.click_close_shop_mgt()

@pytest.fixture(scope='function')
def function_export_fixture(drivers):
    yield
    close = HomePagePage(drivers)
    close.click_close_export_record()

@allure.feature("首页")
class TestQueryAllIndicatorsOnTheHomepage:
    @allure.story("查询User Management& Authorization卡片")
    @allure.title("查看Homepage首页，User Management& Authorization卡片维度数据加载")
    @allure.description("查看Homepage首页，User Management& Authorization卡片的各维度数据")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_001_001(self, drivers):
        """DCR 管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Home Page")

        page_user_mgt = HomePagePage(drivers)
        page_user_mgt.click_time_period()
        page_user_mgt.click_search()
        user_mgt_card = page_user_mgt.get_user_mgt_authorization()
        ValueAssert.value_assert_equal(user_mgt_card, "User Management & Authorization")

        page_user_mgt.get_no_auth_cust_wh_shop()
        page_user_mgt.get_country_and_above_authority()
        page_user_mgt.get_trans_days_no_login()
        page_user_mgt.get_no_menu()
        page_user_mgt.get_no_auth_cust_wh()
        page_user_mgt.get_cust_days_no_login()
        sleep(1)


    @allure.story("查询Abnormal Data卡片")
    @allure.title("Homepage首页，查询Abnormal Data卡片维度数据加载")
    @allure.description("Homepage首页，查询Abnormal Data卡片的各维度数据")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_001_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        # """销售管理菜单-出库单-筛选出库单用例"""
        # user.click_gotomenu("Home Page")

        abnormal = HomePagePage(drivers)
        abnormal.click_time_period()
        abnormal.click_search()

        abnormal_text = abnormal.get_abnormal_data_text()
        infiltration_sale_text = abnormal.get_infiltration_sales_text()

        ValueAssert.value_assert_equal("Abnormal Data", abnormal_text)
        ValueAssert.value_assert_In("Infiltration Sales", infiltration_sale_text)

        abnormal.get_dist_deli_date()
        abnormal.get_sub_deal_deli_date()
        abnormal.get_factory_deli_date()
        abnormal.get_shop_sales_date()
        abnormal.get_infiltration_sales_pcs()
        sleep(1)


    @allure.story("查询Sub-dealer Management卡片")
    @allure.title("Homepage首页，查询Sub-dealer Management卡片维度数据加载")
    @allure.description("Homepage首页，查询Sub-dealer Management卡片的各维度数据")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_001_003(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        # """销售管理菜单-出库单-筛选出库单用例"""
        # user.click_gotomenu("Home Page")

        query = HomePagePage(drivers)
        query.click_time_period()
        query.click_search()

        sub_dealer_text = query.get_sub_dealer_management()
        ValueAssert.value_assert_equal("Sub-dealer Management", sub_dealer_text)

        query.get_total_sub_dealer_value()
        query.get_number_of_rebated_user()
        query.get_days_no_stock_in_out()
        query.get_no_permission_seller_buyer()
        sleep(1)


    @allure.story("查询Distributor Management卡片")
    @allure.title("Homepage首页，查询Distributor Management卡片维度数据加载")
    @allure.description("Homepage首页，查询Distributor Management卡片的各维度数据")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_001_004(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        # """销售管理菜单-出库单-筛选出库单用例"""
        # user.click_gotomenu("Home Page")

        query_dist = HomePagePage(drivers)
        query_dist.click_time_period()
        query_dist.click_search()

        dist_management = query_dist.get_distributor_management()
        ValueAssert.value_assert_equal("Distributor Management", dist_management)

        query_dist.get_total_distributor()
        query_dist.get_dist_number_of_rebated_user()
        query_dist.get_dist_days_no_stock_in_out()
        query_dist.get_dist_no_permission_buyer()
        sleep(1)


    @allure.story("查询Shop Management卡片")
    @allure.title("Homepage首页，查询Shop Management卡片维度数据加载")
    @allure.description("Homepage首页，查询Shop Management卡片的各维度数据")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_001_005(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        # """销售管理菜单-出库单-筛选出库单用例"""
        # user.click_gotomenu("Home Page")

        query_shop = HomePagePage(drivers)
        query_shop.click_time_period()
        query_shop.click_search()

        get_shop_mgt = query_shop.get_shop_management_text()
        ValueAssert.value_assert_equal("Shop Management", get_shop_mgt)

        query_shop.get_total_shop()
        #query_shop.get_shop_number_of_rebated_user()
        query_shop.get_shop_days_no_upload_sales()
        sleep(1)


@allure.feature("首页")
class TestExportAllIndicatorsOnTheHomepage:
    @allure.story("导出User Management & Authorization卡片")
    @allure.title("Homepage首页，导出User Management & Authorization卡片维度数据")
    @allure.description("Homepage首页的，导出User Management& Authorization卡片的各维度数据")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_user_fixture')
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        # """销售管理菜单-出库单-筛选出库单用例"""
        # user.click_gotomenu("Home Page")

        export = HomePagePage(drivers)
        export.click_time_period()
        export.click_search()

        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()

        export.click_time_period()
        export.click_search()
        export.click_user_mgt_export()
        export.click_download_more()
        sleep(48)
        export.input_task_name("User management")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()

        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "User management")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        # export.click_close_export_record()
        # export.click_close_user_management()


    @allure.story("导出Abnormal Data卡片")
    @allure.title("Homepage首页，导出Abnormal Data卡片维度数据")
    @allure.description("Homepage首页，导出Abnormal Data卡片的各维度数据")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_export_fixture')
    def test_002_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        # """销售管理菜单-出库单-筛选出库单用例"""
        # user.click_gotomenu("Home Page")

        export = HomePagePage(drivers)
        export.click_time_period()
        export.click_search()

        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()

        export.click_time_period()
        export.click_search()
        export.click_export_abnormal_data()
        export.click_download_more()
        export.input_task_name("Activation Abnormal Data")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text("Activation Abnormal Data")
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Activation Abnormal Data")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        #export.click_close_export_record()
        sleep(1)


    @allure.story("导出Sub-dealer Management卡片")
    @allure.title("Homepage首页，导出Sub-dealer Management卡片维度数据")
    @allure.description("Homepage首页，导出Sub-dealer Management卡片的各维度数据")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_customer_fixture')
    def test_002_003(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        # """销售管理菜单-出库单-筛选出库单用例"""
        # user.click_gotomenu("Home Page")

        export = HomePagePage(drivers)
        export.click_time_period()
        export.click_search()
        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()

        export.click_time_period()
        export.click_search()

        export.click_sub_dealer_export()
        export.click_download_more()
        export.input_task_name("Customer management")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text("Customer management")
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Customer management")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        # export.click_close_export_record()
        # export.click_close_customer_mgt()


    @allure.story("导出Distributor Management卡片")
    @allure.title("Homepage首页，导出Distributor Management卡片维度数据")
    @allure.description("Homepage首页，导出Distributor Management卡片的各维度数据")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_customer_fixture')
    def test_002_004(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        # """销售管理菜单-出库单-筛选出库单用例"""
        # user.click_gotomenu("Home Page")

        export = HomePagePage(drivers)
        export.click_time_period()
        export.click_search()
        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()

        export.click_distributor_export()
        export.click_download_more()
        export.input_task_name("Customer management")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text("Customer management")
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Customer management")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        # export.click_close_export_record()
        # export.click_close_customer_mgt()


    @allure.story("导出Shop Management卡片")
    @allure.title("Homepage首页，导出Shop Management卡片维度数据")
    @allure.description("Homepage首页，导出Shop Management卡片的各维度数据")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_shop_fixture')
    def test_002_005(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        # """销售管理菜单-出库单-筛选出库单用例"""
        # user.click_gotomenu("Home Page")

        export = HomePagePage(drivers)
        export.click_time_period()
        export.click_search()

        """获取当天日期"""
        base = Base(drivers)
        today = base.get_datetime_today()

        export.click_shop_export()
        export.click_download_more()
        sleep(42)
        export.input_task_name("Shop Manager List")
        down_status = export.click_export_search()

        task_name = export.get_task_name_text("Shop Manager List")
        file_size = export.get_file_size_text()
        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_export_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Shop Manager List")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        # export.click_close_export_record()
        # export.click_close_shop_mgt()


if __name__ == '__main__':
    pytest.main(['Home_Page.py'])