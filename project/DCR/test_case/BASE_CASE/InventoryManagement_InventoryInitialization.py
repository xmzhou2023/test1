from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.InventoryManagement_InventoryInitialization import InventoryInitializationPage
from public.base.assert_ui import ValueAssert, DomAssert
from public.base.basics import Base
import logging
from libs.common.time_ui import sleep
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

@allure.feature("库存管理-库存初始化")
class TestAddInitializationOrder:
    @allure.story("新建IMEI库存初始化")
    @allure.title("库存管理页面，新建IMEI库存初始化，输入仓库不存在的IMEI，IMEI检查通过")
    @allure.description("库存管理页面，新建IMEI库存初始化，输入仓库不存在的IMEI，IMEI检查通过")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        user1 = LoginPage(drivers)
        user1.initialize_login(drivers, 'BD291501', 'dcr123456')
        user1.click_gotomenu('Inventory Management', 'Inventory Initialization')
        add_imei = InventoryInitializationPage(drivers)
        """新建IMEI初始化库存"""
        add_imei.click_add_initialization()
        add_imei.click_add_imei_sn_radio()
        """输入仓库不存在的IMEI，检查成功"""
        add_imei.input_scan_imei_sn('351364951818686')
        add_imei.click_check()
        get_scanned_num = add_imei.get_add_scanned_num()
        ValueAssert.value_assert_equal('1', get_scanned_num)
        DomAssert(drivers).assert_att('Success')
        DomAssert(drivers).assert_att('351364951818686')

        # add.create_initialization_imei_operation('351364951818686')
        # """断言Inventory Initialization列表 ，根本IMEI筛选，是否存在新建的数据"""
        # add.click_unfold_fold('Unfold')
        # add.input_inventory_imei_query('IMEI', '351364951818686')
        # """点击Search查询按钮"""
        # add.click_search()
        # add.assert_Query_result('Customer ID', 'BD2915')
        # add.assert_Query_result('Creator', 'BD291501')
        # add.assert_Query_result('Operation', 'IMEI Detail')
        # get_list_total = add.get_list_total()
        # ValueAssert.value_assert_equal('1', get_list_total)
        # """打开IMEI Detail详情页"""
        # add.click_imei_detail_button()
        # """断言列表是否存在这个IMEI数据"""
        # add.assert_Query_result('IMEI', '351364951818686')
        # get_imei_detail_total = add.get_imei_detail_total()
        # ValueAssert.value_assert_equal('1', get_imei_detail_total)
        # add.click_close_imei_detail()


    @allure.story("新建IMEI库存初始化")
    @allure.title("库存管理页面，新建IMEI库存初始化，输入仓库已存在的IMEI")
    @allure.description("库存管理页面，新建IMEI库存初始化，输入仓库已存在的IMEI，IMEI检查不通过")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_002(self, drivers):
        user2 = LoginPage(drivers)
        user2.initialize_login(drivers, 'BD291501', 'dcr123456')
        user2.click_gotomenu('Inventory Management', 'Inventory Initialization')
        add_imei = InventoryInitializationPage(drivers)
        """新建IMEI初始化库存"""
        add_imei.click_add_initialization()
        """选中IMEI单选按钮，输入已存在的Box ID"""
        add_imei.click_add_imei_sn_radio()
        add_imei.input_scan_imei_sn('43012212030149')
        add_imei.click_check()
        DomAssert(drivers).assert_att('Box has been scaned')

        """选中IMEI/SN单选按钮，输入仓库已存在的IMEI，检查失败"""
        add_imei.input_scan_imei_sn('351364951220222')
        add_imei.click_check()
        get_scanned_num = add_imei.get_add_scanned_num()
        ValueAssert.value_assert_equal('0', get_scanned_num)
        get_no_data = add_imei.get_order_detail_no_data()
        ValueAssert.value_assert_equal('No Data', get_no_data)
        DomAssert(drivers).assert_att('Already in warehouse')
        DomAssert(drivers).assert_att('351364951220222')


    @allure.story("新建Box ID库存初始化")
    @allure.title("库存管理页面，新建Box ID库存初始化，输入仓库已存在的Box ID")
    @allure.description("库存管理页面，新建Box ID库存初始化，输入仓库已存在的Box ID，检查不通过")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_003(self, drivers):
        user3 = LoginPage(drivers)
        user3.initialize_login(drivers, 'BD291501', 'dcr123456')
        user3.click_gotomenu('Inventory Management', 'Inventory Initialization')
        add_box = InventoryInitializationPage(drivers)
        """新建Box ID初始化库存"""
        add_box.click_add_initialization()
        """选中Box ID单选按钮，输入已存在的IMEI"""
        add_box.click_add_box_id_radio()
        add_box.input_scan_box_id('351364951220222')
        add_box.click_check()
        DomAssert(drivers).assert_att('Please enter boxId')

        """输入仓库已存在的Box ID，检查失败"""
        add_box.input_scan_box_id('43012212030149')
        add_box.click_check()
        get_scanned_num = add_box.get_add_scanned_num()
        ValueAssert.value_assert_equal('0', get_scanned_num)
        get_no_data = add_box.get_order_detail_no_data()
        ValueAssert.value_assert_equal('No Data', get_no_data)
        DomAssert(drivers).assert_att('Box has been scaned')
        DomAssert(drivers).assert_att('43012212030149')


# @allure.feature("库存管理-库存初始化")
# class TestExportInitializationOrder:
#     @allure.story("查询库存初始化数据")
#     @allure.title("库存管理页面，查询每个筛选条件")
#     @allure.description("库存管理页面，查询每个筛选条件，查询结果与条件一致")
#     @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
#     @pytest.mark.smoke  # 用例标记
#     @pytest.mark.usefixtures('function_export_fixture')
#     def test_002_001(self, drivers):
#         login = LoginPage(drivers)
#         login.initialize_login(drivers, 'BD291501', 'dcr123456')
#         login.click_gotomenu('Inventory Management', 'Inventory Initialization')
#         select = InventoryInitializationPage(drivers)


    # @allure.story("查询库存初始化数据")
    # @allure.title("库存管理页面，查询查看一条数据的IMEI Detail详情")
    # @allure.description("库存管理页面，查看一条数据的IMEI Detail详情列表信息")
    # @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    # @pytest.mark.smoke  # 用例标记
    # @pytest.mark.usefixtures('function_export_fixture')
    # def test_002_002(self, drivers):
    #     login = LoginPage(drivers)
    #     login.initialize_login(drivers, 'BD291501', 'dcr123456')
    #     login.click_gotomenu('Inventory Management', 'Inventory Initialization')
    #     select = InventoryInitializationPage(drivers)



@allure.feature("库存管理-库存初始化")
class TestExportInitializationOrder:
    @allure.story("导出库存初始化数据")
    @allure.title("库存管理页面，导出库存初始化列表数据")
    @allure.description("库存管理页面，导出库存初始化列表数据")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_export_fixture')
    def test_003_001(self, drivers):
        login = LoginPage(drivers)
        login.initialize_login(drivers, 'BD291501', 'dcr123456')
        login.click_gotomenu('Inventory Management', 'Inventory Initialization')
        export = InventoryInitializationPage(drivers)
        """获取当天日期"""
        today = Base(drivers).get_datetime_today()
        """点击导出按钮"""
        export.click_initial_list_export()
        login.click_download_more()
        login.input_task_name('Inventory Initialization')
        login.export_record_create_start_date(today)
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = login.click_export_search()
        file_size = login.get_file_size_text()
        export_time = login.get_export_time_text()
        login.assert_file_time_size(file_size, export_time)
        export.assert_Query_result('Download Status', down_status)
        export.assert_Query_result('Task Name', 'Inventory Initialization')
        export.assert_Query_result('Create Date', today)
        export.assert_Query_result('Completed Date', today)
        export.assert_Query_result('Operation', 'Download')


    # @allure.story("导出库存初始化数据")
    # @allure.title("库存管理页面，导出IMEI Detail详情列表信息")
    # @allure.description("库存管理页面，导出IMEI Detail详情列表信息")
    # @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    # @pytest.mark.smoke  # 用例标记
    # @pytest.mark.usefixtures('function_export_fixture')
    # def test_003_002(self, drivers):
    #     login = LoginPage(drivers)
    #     login.initialize_login(drivers, 'BD291501', 'dcr123456')
    #     login.click_gotomenu('Inventory Management', 'Inventory Initialization')
    #     export_detail = InventoryInitializationPage(drivers)
    #
    #     """筛选某条IMEI数据，查看IMEI详情，导出IMEI Detail详情信息"""
    #     export_detail.click_unfold_fold('Unfold')
    #     export_detail.input_inventory_imei_query('IMEI', '351364951818686')


if __name__ == '__main__':
    pytest.main(['InventoryManagement_InventoryInitialization.py'])

