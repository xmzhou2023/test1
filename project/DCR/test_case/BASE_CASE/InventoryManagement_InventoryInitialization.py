from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.InventoryManagement_InventoryInitialization import InventoryInitializationPage
from public.base.assert_ui import ValueAssert, DomAssert
from public.base.basics import Base
from libs.common.connect_sql import *
import logging
from libs.common.time_ui import sleep
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
        # add.input_initial_imei_query('IMEI', '351364951818686')
        # """点击Search查询按钮"""
        # add.click_search_reset('Search')
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


    @allure.story("新建IMEI库存初始化")
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


@allure.feature("库存管理-库存初始化")
class TestQueryInitializationOrder:
    @allure.story("查询库存初始化数据")
    @allure.title("库存管理页面，查询每个筛选条件")
    @allure.description("库存管理页面，查询每个筛选条件，查询结果与条件一致")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        login = LoginPage(drivers)
        login.initialize_login(drivers, 'lhmadmin', 'dcr123456')
        login.click_gotomenu('Inventory Management', 'Inventory Initialization')
        select = InventoryInitializationPage(drivers)
        select.click_unfold_fold('Unfold')
        """按Initial ID条件筛选初始化id数据"""
        select.input_initial_id_query('Initial ID', '05HK2301300001')
        select.click_search_reset('Search')
        select.assert_Query_result('Initial ID', '05HK2301300001')
        select.assert_Query_result('Operation', 'IMEI Detail')
        select.assert_Query_result('Customer ID', 'BD2915')
        select.click_search_reset('Reset')

        """按Customer条件筛选初始化数据"""
        select.input_initial_customer_query('Customer', 'BD2915', 'BD2915 lhmSubdealer001')
        select.click_search_reset('Search')
        select.assert_Query_result('Customer ID', 'BD2915')
        select.assert_Query_result('Customer Name', 'lhmSubdealer001')
        select.click_search_reset('Reset')

        """按Customer Type条件筛选初始化数据"""
        select.input_initial_customer_type_query('Customer Type', 'Distributor')
        select.click_search_reset('Search')
        select.assert_Query_result('Customer Type', '1')
        select.click_search_reset('Reset')

        """按Warehouse条件筛选初始化数据"""
        select.input_initial_warehouse_query('Warehouse', 'WBD291502')
        select.click_search_reset('Search')
        select.assert_Query_result('Warehouse ID', 'WBD291502')
        select.click_search_reset('Reset')

        """按Model条件筛选初始化数据"""
        select.input_initial_model_query('Model', 'X665B')
        select.click_search_reset('Search')
        select.assert_Query_result('Model', 'X665B')
        select.click_search_reset('Reset')

        """按Brand条件筛选初始化数据"""
        select.input_initial_brand_query('Brand', 'Infinix')
        select.click_search_reset('Search')
        select.assert_Query_result('Brand', 'Infinix')
        select.click_search_reset('Reset')

        """按Market Name条件筛选初始化数据"""
        select.input_initial_market_name_query('Market Name', 'HOT 12i')
        select.click_search_reset('Search')
        select.assert_Query_result('Market Name', 'HOT 12i')
        select.click_search_reset('Reset')

        """按IMEI条件筛选初始化数据"""
        select.input_initial_imei_query('IMEI', '357274166980524')
        select.click_search_reset('Search')
        """点击IMEI Detail按钮，打开详情页"""
        select.click_imei_detail_button()
        """断言IMEI Detail详情页是否存在 筛选的IMEI"""
        get_detail_total = select.get_imei_detail_total()
        ValueAssert.value_assert_equal('1', get_detail_total)
        select.assert_Query_result('IMEI', '357274166980524')
        select.click_close_imei_detail()
        select.click_search_reset('Reset')

        """按Country条件筛选初始化数据"""
        select.input_initial_country_query('Country', 'Bangladesh')
        select.click_search_reset('Search')
        select.assert_Query_result('Country', 'Bangladesh')
        select.click_search_reset('Reset')


    @allure.story("查询库存初始化数据")
    @allure.title("库存管理页面，查询查看一条数据的IMEI Detail详情")
    @allure.description("库存管理页面，查看一条数据的IMEI Detail详情列表信息")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_export_fixture')
    def test_002_002(self, drivers):
        login = LoginPage(drivers)
        login.initialize_login(drivers, 'BD291501', 'dcr123456')
        login.click_gotomenu('Inventory Management', 'Inventory Initialization')
        select = InventoryInitializationPage(drivers)

        """筛选某条IMEI数据，查看IMEI详情，导出IMEI Detail详情信息"""
        select.click_unfold_fold('Unfold')
        select.input_initial_imei_query('IMEI', '351364951220222')
        select.click_search_reset('Search')

        """断言 分页总条数，是否筛选到满足条件的一条数据"""
        get_list_total = select.get_list_total()
        ValueAssert.value_assert_equal('1', get_list_total)
        """点击IMEI Detail按钮，打开详情页"""
        select.click_imei_detail_button()
        get_detail_total = select.get_imei_detail_total()
        ValueAssert.value_assert_equal('1', get_detail_total)
        select.assert_Query_result('IMEI', '351364951220222')
        select.assert_Query_result('Brand', 'TECNO')
        select.click_close_imei_detail()


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


    @allure.story("导出库存初始化数据")
    @allure.title("库存管理页面，导出IMEI Detail详情列表信息")
    @allure.description("库存管理页面，导出IMEI Detail详情列表信息")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_002(self, drivers):
        login = LoginPage(drivers)
        login.initialize_login(drivers, 'BD291501', 'dcr123456')
        login.click_gotomenu('Inventory Management', 'Inventory Initialization')
        export_detail = InventoryInitializationPage(drivers)
        """筛选某条IMEI数据，查看IMEI详情，导出IMEI Detail详情信息"""
        export_detail.click_unfold_fold('Unfold')
        export_detail.input_initial_imei_query('IMEI', '351364951220222')
        export_detail.click_search_reset('Search')

        """断言 分页总条数，是否筛选到满足条件的一条数据"""
        get_list_total = export_detail.get_list_total()
        ValueAssert.value_assert_equal('1', get_list_total)
        """点击IMEI Detail按钮，打开详情页"""
        export_detail.click_imei_detail_button()
        """断言IMEI Detail详情页 分页总数是否为有1条数据"""
        get_detail_total = export_detail.get_imei_detail_total()
        ValueAssert.value_assert_equal('1', get_detail_total)
        export_detail.assert_Query_result('IMEI', '351364951220222')

        """点击IMEI Detail 详情页的导出按钮, 断言导出进度条是否100%"""
        logging.info('the total in test case is %s' % get_detail_total)
        if int(get_detail_total) > 0:
            export_detail.click_imei_detail_export()
            sleep(3)
            complete_value = export_detail.get_download_value()
            ValueAssert.value_assert_equal(complete_value, 100)
        else:
            logging.info('the total is empty')
        export_detail.click_close_imei_detail()


@allure.feature("库存管理-库存初始化")
class TestImportInitializationOrder:
    @allure.story("导入库存初始化数据")
    @allure.title("库存管理页面，导入库存初始化数据成功")
    @allure.description("库存管理页面，导入库存初始化数据成功")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_001(self, drivers):
        login = LoginPage(drivers)
        login.initialize_login(drivers, 'BD291501', 'dcr123456')
        login.click_gotomenu('Inventory Management', 'Inventory Initialization')
        add_upload = InventoryInitializationPage(drivers)
        today = Base(drivers).get_datetime_today()
        """需要导入的IMEI参数"""
        imei = '359037470982967'
        add_upload.click_initial_import('Import')
        add_upload.upload_true_file('Inventory+Initiali+Template_Success.xlsx')
        """根据导入日期筛选当前导入的数据"""
        login.input_batch_import_date_query(today)
        """进入Import Record页面，点击Search按钮 """
        add_upload.click_search_reset('Search')

        """Import Record 导入记录页面，断言是否新增一条导入成功的记录"""
        add_upload.assert_Query_result('File Name', 'Inventory+Initiali+Template_Success.xlsx')
        add_upload.assert_Query_result('Status', 'Upload Successfully')
        add_upload.assert_Query_result('Total', '1')
        add_upload.assert_Query_result('Success', '1')
        add_upload.assert_Query_result('Failed', '0')
        add_upload.assert_Query_result('Import Date', today)
        add_upload.assert_Query_result('User ID', 'BD291501')
        """关闭当前打开的菜单"""
        login.click_close_open_menu()

        """根据导入的库存初始化数据，筛选导入的数据，进行断言列表是否存在导入的数据"""
        add_upload.click_unfold_fold('Unfold')
        add_upload.input_initial_imei_query('IMEI', imei)
        add_upload.click_search_reset('Search')
        """断言Inventory Initialization页面，是否加载导入成的数据"""
        get_list_total = add_upload.get_list_total()
        logging.info("获取Inventory Initialization页面，分页总条数:{}".format(get_list_total))
        ValueAssert.value_assert_equal('1', get_list_total)
        initial_id = add_upload.get_initial_id_text()
        logging.info("获取Inventory Initialization页面列表，Initial ID字段内容:{}".format(initial_id))
        add_upload.assert_Query_result('Brand', 'itel')
        """点击IMEI Detail按钮，打开详情页"""
        add_upload.click_imei_detail_button()
        get_detail_total = add_upload.get_imei_detail_total()
        ValueAssert.value_assert_equal('1', get_detail_total)
        add_upload.assert_Query_result('IMEI', imei)
        add_upload.assert_Query_result('Brand', 'itel')
        add_upload.click_close_imei_detail()
        """通过数据库脚本删除导入的初始化数据"""
        add_upload.delete_import_initial_data(initial_id, imei)



    @allure.story("导入库存初始化数据")
    @allure.title("库存管理页面，导入库存初始化列表已存在的IMEI，导入失败")
    @allure.description("库存管理页面，导入库存初始化列表已存在的IMEI，导入失败")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    @pytest.mark.usefixtures('function_export_fixture')
    def test_004_002(self, drivers):
        login = LoginPage(drivers)
        login.initialize_login(drivers, 'BD291501', 'dcr123456')
        login.click_gotomenu('Inventory Management', 'Inventory Initialization')
        add_upload = InventoryInitializationPage(drivers)
        today = Base(drivers).get_datetime_today()

        add_upload.click_initial_import('Import')
        add_upload.upload_true_file('Inventory+Initiali+Template_Failed.xlsx')
        """根据导入日期筛选当前导入的数据"""
        login.input_batch_import_date_query(today)
        """进入Batch Import页面，点击Search按钮 """
        add_upload.click_search_reset('Search')

        """Import Record 导入记录页面，断言是否新增一条导入失败的记录"""
        add_upload.assert_Query_result('File Name', 'Inventory+Initiali+Template_Failed.xlsx')
        add_upload.assert_Query_result('Status', 'Upload Successfully')
        add_upload.assert_Query_result('Total', '1')
        add_upload.assert_Query_result('Success', '0')
        add_upload.assert_Query_result('Failed', '1')
        add_upload.assert_Query_result('Fail Data', 'Download Failed')
        add_upload.assert_Query_result('Import Date', today)
        add_upload.assert_Query_result('User ID', 'BD291501')



if __name__ == '__main__':
    pytest.main(['InventoryManagement_InventoryInitialization.py'])

