import logging
from datetime import datetime

from project.DCR.page_object.StaffAuthorization_UserAuthorization import UserAuthorizationPage
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.time_ui import sleep
from libs.common.logger_ui import log
import pytest
import allure

"""后置关闭菜单方法"""
@pytest.fixture(scope='function')
def function_menu_fixture(drivers):
    yield
    menu = LoginPage(drivers)
    get_menu_class = menu.get_open_menu_class()
    class_value = "tags-view-item router-link-exact-active router-link-active active"
    if class_value == str(get_menu_class):
        menu.click_close_open_menu()

@allure.feature("员工授权-用户授权")
class TestDeleteBrandAuthorization:
    @allure.story("删除、新增品牌授权")
    @allure.title("用户授权页面，删除、新增Infinix品牌授权")
    @allure.description("用户授权页面，筛选User：NG2061301，删除、新增Infinix品牌授权")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        """DCR 管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开User Authorization菜单页面 """
        user.click_gotomenu("Staff & Authorization", "User Authorization")
        """如果存在infinix品牌则删除infinix品牌，如果不存在infinix品牌则添加infinix品牌"""
        brand = UserAuthorizationPage(drivers)
        brand.input_dealer_user_query("NG2061301")
        """点击查询按钮"""
        brand.click_search()
        list_infinix = brand.get_list_infinix_text()
        """如果存在删除Infinix品牌"""
        if "Infinix" == list_infinix:
            """如果存在Infinix品牌，则删除此品牌"""
            brand.click_cancel_association()
            brand.click_delete_brand()
            """断言页面是否存在Successfully成功提示语"""
            DomAssert(drivers).assert_att("Successfully")

        """用户授权页面，新增Infinix品牌授权"""
        brand.click_add_brand()
        get_add_infinix = brand.get_add_infinix_text()
        ValueAssert.value_assert_equal("Infinix", get_add_infinix)
        brand.click_add_brand_checkbox()
        brand.click_save_brand()

        DomAssert(drivers).assert_att("Successfully")
        list_infinix_text = brand.get_list_infinix_text()
        ValueAssert.value_assert_equal("Infinix", list_infinix_text)


@allure.feature("员工授权-用户授权")
class TestDeleteCustAuthorization:
    @allure.story("删除、新增客户授权")
    @allure.title("用户授权页面，删除、新增CN20009客户授权")
    @allure.description("用户授权页面，筛选User：NG2061301，删除、新增CN20009客户授权")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开User Authorization菜单页面 """
        user.click_gotomenu("Staff & Authorization", "User Authorization")
        customer = UserAuthorizationPage(drivers)
        customer.input_dealer_user_query("NG2061301")
        """点击查询按钮"""
        customer.click_search()

        customer.click_customer_tab()
        customer.input_list_customer("CN20009")

        customer.click_customer_search()
        get_cust = customer.get_list_customer_id("CN20009")
        if get_cust == "CN20009":
            customer.click_list_cust_checkbox()
            customer.click_cust_more_option()
            customer.click_cust_cancel_association()
            customer.click_cust_delete()
            DomAssert(drivers).assert_att("Successfully")

        """新增CN20009客户授权"""
        customer.click_add_customer()
        customer.click_input_customer("CN20009")
        customer.click_add_customer_search()

        get_customer_id = customer.get_customer_id_text()
        if get_customer_id in "CN20009":
            customer.click_add_customer_checkbox()
            customer.click_cust_authoriz_select()
            DomAssert(drivers).assert_att("Successfully")


    @allure.story("授权客户")
    @allure.title("传音员工授权客户，批量取消")
    @allure.description("传音员工授权客户，批量取消客户授权Batch Cancel Association")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")

        """打开User Authorization菜单页面 """
        customer = UserAuthorizationPage(drivers)
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS")
        customer.click_search()
        """点击Customer标签页"""
        customer.click_tab('Customer')
        """移除所有授权"""
        customer.reset_Association()
        """添加授权组合方法"""
        customer.Association_Method('SN400001')
        customer.Association_Method('SN400002')
        """断言：添加客户授权成功"""
        customer.assert_Query_containsresult('Customer ID', 'SN400002')
        customer.assert_Query_containsresult('Customer ID', 'SN400001')
        """移除客户授权"""
        customer.click_CheckBox('SN400002')
        customer.click_CheckBox('SN400001')
        customer.click_function_button('Batch Cancel Association')
        customer.click_Delete()
        """断言：移除客户授权成功"""
        DomAssert(drivers).assert_att('Successfully')
        customer.assert_NoData()

    @allure.story("授权客户")
    @allure.title("传音员工授权客户，一键清空")
    @allure.description("传音员工授权客户，一键清空客户授权 Empty All Association")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_003(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")

        """打开User Authorization菜单页面 """
        customer = UserAuthorizationPage(drivers)
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS")
        customer.click_search()
        """点击Customer标签页"""
        customer.click_tab('Customer')
        """移除所有授权"""
        customer.reset_Association()
        """添加授权组合方法"""
        customer.Association_Method('SN400001')
        customer.Association_Method('SN400002')
        """断言：添加客户授权成功"""
        customer.assert_Query_containsresult('Customer ID', 'SN400002')
        customer.assert_Query_containsresult('Customer ID', 'SN400001')
        """移除客户授权"""
        customer.click_function_button('Empty All Association')
        customer.click_Delete()
        DomAssert(drivers).assert_att('Successfully')
        customer.assert_NoData()

    @allure.story("授权客户")
    @allure.title("批量授权客户")
    @allure.description("批量授权客户")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_004(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "xLily6x")
        """打开User Authorization菜单页面 """
        customer = UserAuthorizationPage(drivers)
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS")
        customer.click_search()
        """点击Customer标签页"""
        customer.click_tab('Customer')
        """移除所有授权"""
        customer.reset_Association()
        """导入文件授权"""
        customer.click_function_button('Import')
        customer.import_file('批量导入客户授权.xlsx')
        customer.click_save()
        customer.click_confirm()
        customer.assert_Record_result('Import Record', '批量导入客户授权.xlsx', 'Status', 'Upload Successfully')
        """断言ImportRecord页面结果"""
        today = datetime.now().strftime('%Y-%m-%d')
        customer.assert_Record_result('Import Record', '批量导入客户授权.xlsx', 'Status', 'Upload Successfully')
        customer.assert_Record_result('Import Record', '批量导入客户授权.xlsx', 'Total', '2')
        customer.assert_Record_result('Import Record', '批量导入客户授权.xlsx', 'Success', '2')
        customer.assert_Record_result('Import Record', '批量导入客户授权.xlsx', 'Import Date', today)
        """断言：添加客户授权成功"""
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS")
        customer.click_search()
        customer.click_tab('Customer')
        customer.assert_Query_containsresult('Customer ID', 'SN400002')
        customer.assert_Query_containsresult('Customer ID', 'SN400001')
        """移除客户授权"""
        customer.click_function_button('Empty All Association')
        customer.click_Delete()
        DomAssert(drivers).assert_att('Successfully')
        customer.assert_NoData()

    @allure.story("门店授权")
    @allure.title("导出筛选条件下的门店授权")
    @allure.description("导出筛选条件下的门店授权")
    @allure.severity("normal")
    @pytest.mark.smoke
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_005(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """打开User Authorization菜单页面 """
        customer = UserAuthorizationPage(drivers)
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS")
        customer.click_search()
        """点击Customer标签页"""
        customer.click_tab('Customer')
        """导出筛选条件下的门店授权"""
        customer.click_function_button('Export Filtered')
        """断言：存在导出文件进度条"""
        customer.assert_export_success()


@allure.feature("员工授权-用户授权")
class TestDeleteWareAuthorization:
    @allure.story("仓库授权")
    @allure.title("用户授权页面，删除、新增WNG2061304仓库授权")
    @allure.description("用户授权页面，筛选User：NG2061301，删除、新增WNG2061304 仓库授权")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开User Authorization菜单页面 """
        user.click_gotomenu("Staff & Authorization", "User Authorization")
        ware = UserAuthorizationPage(drivers)
        ware.input_dealer_user_query("NG2061301")
        ware.click_search()
        """点击Warehouse 页签"""
        ware.click_warehouse_tab()
        ware.input_list_query_ware("WNG2061304")
        ware.click_warehouse_list_search()
        get_list_ware = ware.get_list_warehouseID_text()
        if get_list_ware == "WNG2061304":
            ware.click_list_ware_checkbox()
            ware.click_ware_more_option()
            ware.click_ware_cancel_association()
            ware.click_ware_delete()
        DomAssert(drivers).assert_att("Successfully")
        get_no_data = ware.get_ware_dele_no_data()
        ValueAssert.value_assert_In(get_no_data, "No Data")

        """ 新增WNG2061304仓库授权 """
        ware.click_add_association_ware()
        ware.input_add_query_ware("WNG2061304")
        ware.click_add_ware_search()
        get_add_ware = ware.get_add_warehouseid_text()
        if get_add_ware == "WNG2061304":
            ware.click_add_ware_checkbox()
            ware.click_add_ware_save()
        DomAssert(drivers).assert_att("Successfully")
        get_list_ware2 = ware.get_list_warehouseID_text()
        ValueAssert.value_assert_equal(get_add_ware, get_list_ware2)


    @allure.story("仓库授权")
    @allure.title("传音员工授权仓库，批量取消")
    @allure.description("传音员工授权仓库，批量取消仓库授权Batch Cancel Association")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")

        """打开User Authorization菜单页面 """
        customer = UserAuthorizationPage(drivers)
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS002")
        customer.click_search()
        """点击Warehouse标签页"""
        customer.click_tab('Warehouse')
        """移除所有授权"""
        customer.reset_Association()
        """添加授权组合方法"""
        customer.Association_Method('SN400004')
        customer.Association_Method('SN400005')
        """断言：添加仓库授权成功"""
        customer.assert_Query_containsresult('Customer ID', 'SN400004')
        customer.assert_Query_containsresult('Customer ID', 'SN400005')
        """批量取消仓库授权"""
        customer.click_CheckBox('SN400004')
        customer.click_CheckBox('SN400005')
        customer.click_function_button('Batch Cancel Association')
        customer.click_Delete()
        """断言：移除仓库授权成功"""
        DomAssert(drivers).assert_att('Successfully')
        customer.assert_NoData()

    @allure.story("仓库授权")
    @allure.title("传音员工授权仓库，一键清空")
    @allure.description("传音员工授权仓库，一键清空仓库授权 Empty All Association")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_003(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")

        """打开User Authorization菜单页面 """
        customer = UserAuthorizationPage(drivers)
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS002")
        customer.click_search()
        """点击Warehouse标签页"""
        customer.click_tab('Warehouse')
        """移除所有授权"""
        customer.reset_Association()
        """添加授权组合方法"""
        customer.Association_Method('SN400004')
        customer.Association_Method('SN400005')
        """断言：添加仓库授权成功"""
        customer.assert_Query_containsresult('Customer ID', 'SN400004')
        customer.assert_Query_containsresult('Customer ID', 'SN400005')
        """一键清空仓库授权"""
        customer.click_function_button('Empty All Association')
        customer.click_Delete()
        """断言：移除仓库授权成功"""
        DomAssert(drivers).assert_att('Successfully')
        customer.assert_NoData()

    @allure.story("仓库授权")
    @allure.title("批量授权仓库")
    @allure.description("批量授权仓库")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_004(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "xLily6x")
        """打开User Authorization菜单页面 """
        customer = UserAuthorizationPage(drivers)
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS002")
        customer.click_search()
        """点击Warehouse标签页"""
        customer.click_tab('Warehouse')
        """移除所有授权"""
        customer.reset_Association()
        """导入文件授权"""
        customer.click_function_button('Import')
        customer.import_file('批量导入仓库授权.xlsx')
        customer.click_save()
        customer.click_confirm()
        customer.assert_Record_result('Import Record', '批量导入仓库授权.xlsx', 'Status', 'Upload Successfully')
        """断言ImportRecord页面结果"""
        today = datetime.now().strftime('%Y-%m-%d')
        customer.assert_Record_result('Import Record', '批量导入仓库授权.xlsx', 'Status', 'Upload Successfully')
        customer.assert_Record_result('Import Record', '批量导入仓库授权.xlsx', 'Total', '2')
        customer.assert_Record_result('Import Record', '批量导入仓库授权.xlsx', 'Success', '2')
        customer.assert_Record_result('Import Record', '批量导入仓库授权.xlsx', 'Import Date', today)
        """断言：添加仓库授权成功"""
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS002")
        customer.click_search()
        customer.click_tab('Warehouse')
        customer.assert_Query_containsresult('Customer ID', 'SN400004')
        customer.assert_Query_containsresult('Customer ID', 'SN400005')
        """移除仓库授权"""
        customer.click_function_button('Empty All Association')
        customer.click_Delete()
        DomAssert(drivers).assert_att('Successfully')
        customer.assert_NoData()

    @allure.story("仓库授权")
    @allure.title("导出筛选条件下的仓库授权")
    @allure.description("导出筛选条件下的仓库授权")
    @allure.severity("normal")
    @pytest.mark.smoke
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_005(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """打开User Authorization菜单页面 """
        customer = UserAuthorizationPage(drivers)
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS002")
        customer.click_search()
        """点击Warehouse标签页"""
        customer.click_tab('Warehouse')
        """导出筛选条件下的仓库授权"""
        customer.click_function_button('Export Filtered')
        """断言：存在导出文件进度条"""
        customer.assert_export_success()


@allure.feature("员工授权-用户授权")
class TestAddRegionAuthorization:
    @allure.story("销售区域授权")
    @allure.title("用户授权页面，给筛选的传音用户授权部分销售区域")
    @allure.description("用户授权页面，筛选User：testlhm0215，授权部分销售区域")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开User Authorization菜单页面 """
        user.click_gotomenu("Staff & Authorization", "User Authorization")
        sale_region = UserAuthorizationPage(drivers)
        sale_region.input_trans_user_query("testlhm0215")
        sale_region.click_search()
        """切换Sales Region销售区域页签"""
        sale_region.click_sales_region_tab()
        sale_region.click_east_africa_checkbox()
        sale_region.click_score_user_checkbox()
        sale_region.click_save_sales_region()
        DomAssert(drivers).assert_att("Successfully")


    @allure.story("销售区域授权")
    @allure.title("授权销售区域下面的所有客户，店铺")
    @allure.description("授权销售区域下面的所有客户，店铺")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_002(self, drivers):
        login = LoginPage(drivers)
        login.initialize_login(drivers, "18650493", "xLily6x")

        """打开User Authorization菜单页面 """
        user = UserAuthorizationPage(drivers)
        user.click_menu("Staff & Authorization", "User Authorization")
        user.input_search('User ID', "1671417004")
        user.click_search()
        """点击Sales Region标签页"""
        user.click_tab('Sales Region')
        """移除所有授权"""
        user.reset_Association('Sales Region')
        """销售区域授权"""
        user.select_SalesRegion('Senegal')
        user.select_ScopeOfAutorization('All Customer')
        user.select_ScopeOfAutorization('Shop')
        user.click_SalesRegion_save()
        """断言：添加销售区域授权成功"""
        DomAssert(drivers).assert_att('Successfully')
        user.assert_SalesRegionAutorization_success('Senegal', 'All Customer', 'Distributor', 'Sub-dealer', 'Shop')
        """移除销售区域授权"""
        user.select_SalesRegion('Senegal')
        user.click_SalesRegion_save()
        """断言：移除销售区域成功"""
        DomAssert(drivers).assert_att('Successfully')
        user.assert_NoData()


    @allure.story("销售区域授权")
    @allure.title("授权销售区域下面的所有国包，用户")
    @allure.description("授权销售区域下面的所有国包，用户")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_003(self, drivers):
        login = LoginPage(drivers)
        login.initialize_login(drivers, "18650493", "xLily6x")

        """打开User Authorization菜单页面 """
        user = UserAuthorizationPage(drivers)
        user.click_menu("Staff & Authorization", "User Authorization")
        user.input_search('User ID', "1671417004")
        user.click_search()
        """点击Sales Region标签页"""
        user.click_tab('Sales Region')
        """移除所有授权"""
        user.reset_Association('Sales Region')
        """销售区域授权"""
        user.select_SalesRegion('Senegal')
        user.select_ScopeOfAutorization('Distributor')
        user.select_ScopeOfAutorization('User')
        user.click_SalesRegion_save()
        """断言：添加销售区域授权成功"""
        DomAssert(drivers).assert_att('Successfully')
        user.assert_SalesRegionAutorization_success('Senegal', 'Distributor', 'User')
        """移除销售区域授权"""
        user.select_SalesRegion('Senegal')
        user.click_SalesRegion_save()
        """断言：移除销售区域成功"""
        DomAssert(drivers).assert_att('Successfully')
        user.assert_NoData()

    @allure.story("销售区域授权")
    @allure.title("销售销售区域下面的所二级经销商， 用户")
    @allure.description("销售销售区域下面的所二级经销商， 用户")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_004(self, drivers):
        login = LoginPage(drivers)
        login.initialize_login(drivers, "18650493", "xLily6x")

        """打开User Authorization菜单页面 """
        user = UserAuthorizationPage(drivers)
        user.click_menu("Staff & Authorization", "User Authorization")
        user.input_search('User ID', "1671417004")
        user.click_search()
        """点击Sales Region标签页"""
        user.click_tab('Sales Region')
        """移除所有授权"""
        user.reset_Association('Sales Region')
        """销售区域授权"""
        user.select_SalesRegion('Senegal')
        user.select_ScopeOfAutorization('Sub-dealer')
        user.select_ScopeOfAutorization('User')
        user.click_SalesRegion_save()
        """断言：添加销售区域授权成功"""
        DomAssert(drivers).assert_att('Successfully')
        user.assert_SalesRegionAutorization_success('Senegal')
        user.assert_SalesRegionAutorization_success('Senegal', 'Sub-dealer', 'User')
        """移除销售区域授权"""
        user.select_SalesRegion('Senegal')
        user.click_SalesRegion_save()
        """断言：移除销售区域成功"""
        DomAssert(drivers).assert_att('Successfully')
        user.assert_NoData()


@allure.feature("员工授权-用户授权")
class TestDeleteShopAuthorization:
    @allure.story("门店授权")
    @allure.title("用户授权页面，删除、新增SN002331门店授权")
    @allure.description("用户授权页面，筛选User：testlhm0215，删除、新增Shop ID:SN002331授权")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_005_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """打开User Authorization菜单页面 """
        user.click_gotomenu("Staff & Authorization", "User Authorization")
        shop = UserAuthorizationPage(drivers)
        shop.input_trans_user_query("lhmyingxiao001")
        shop.click_search()
        """切换Shop页签"""
        shop.click_shop_tab()
        shop.input_list_query_shop("SN002331")
        shop.click_shop_list_search()

        get_list_shop = shop.get_list_shop_text("SN002331")
        if get_list_shop == "SN002331":
            shop.click_list_shop_checkbox()
            shop.click_shop_more_option()
            shop.click_shop_cancel_association()
            shop.click_shop_delete()
        DomAssert(drivers).assert_att("Successfully")
        get_shop_no_data = shop.get_shop_delete_no_data()
        ValueAssert.value_assert_In(get_shop_no_data, "No Data")

        """ 新增SN002331门店授权 """
        shop.click_add_association_shop()
        shop.input_add_query_shop("SN002331")
        shop.click_add_shop_search()
        get_add_shop_id = shop.get_add_shop_id_text("SN002331")
        logging.info("新增门店页面，获取列表的门店ID{}".format(get_add_shop_id))
        sleep(1)
        if "SN002331" == get_add_shop_id:
            shop.click_add_shop_checkbox()
            shop.click_add_shop_author_select()

        DomAssert(drivers).assert_att("Successfully")
        get_list_shop_id = shop.get_list_shop_id_text("SN002331")
        ValueAssert.value_assert_equal(get_list_shop_id, "SN002331")


    @allure.story("门店授权")
    @allure.title("传音员工门店授权，批量取消")
    @allure.description("传音员工门店授权，批量取消授权Batch Cancel Association")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_005_002(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")

        """打开User Authorization菜单页面 """
        customer = UserAuthorizationPage(drivers)
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS")
        customer.click_search()
        """点击Shop标签页"""
        customer.click_tab('Shop')
        """移除所有授权"""
        customer.reset_Association()
        """添加授权组合方法"""
        customer.Association_Method('SN002424', header='Shop')
        customer.Association_Method('SN002425', header='Shop')
        """断言：添加门店授权成功"""
        customer.assert_Query_containsresult('Shop ID', 'SN002424')
        customer.assert_Query_containsresult('Shop ID', 'SN002425')
        """移除门店授权"""
        customer.click_CheckBox('SN002424')
        customer.click_CheckBox('SN002425')
        customer.click_function_button('Batch Cancel Association')
        customer.click_Delete()
        """断言：移除门店授权成功"""
        DomAssert(drivers).assert_att('Successfully')
        customer.assert_NoData()

    @allure.story("门店授权")
    @allure.title("传音员工门店授权，一键清空")
    @allure.description("传音员工门店授权，一键清空授权 Empty All Association")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_005_003(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")

        """打开User Authorization菜单页面 """
        customer = UserAuthorizationPage(drivers)
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS")
        customer.click_search()
        """点击Shop标签页"""
        customer.click_tab('Shop')
        """移除所有授权"""
        customer.reset_Association()
        """添加授权组合方法"""
        customer.Association_Method('SN002424', header='Shop')
        customer.Association_Method('SN002425', header='Shop')
        """断言：添加门店授权成功"""
        customer.assert_Query_containsresult('Shop ID', 'SN002424')
        customer.assert_Query_containsresult('Shop ID', 'SN002425')
        """移除门店授权"""
        customer.click_function_button('Empty All Association')
        customer.click_Delete()
        DomAssert(drivers).assert_att('Successfully')
        customer.assert_NoData()

    @allure.story("门店授权")
    @allure.title("批量门店授权")
    @allure.description("批量门店授权")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_005_004(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """打开User Authorization菜单页面 """
        customer = UserAuthorizationPage(drivers)
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS")
        customer.click_search()
        """点击Shop标签页"""
        customer.click_tab('Shop')
        """移除所有授权"""
        customer.reset_Association()
        """导入文件授权"""
        customer.click_function_button('Import')
        customer.import_file('批量导入门店授权.xlsx')
        customer.click_save()
        customer.click_confirm()
        customer.assert_Record_result('Import Record', '批量导入门店授权.xlsx', 'Status', 'Upload Successfully')
        """断言ImportRecord页面结果"""
        today = datetime.now().strftime('%Y-%m-%d')
        customer.assert_Record_result('Import Record', '批量导入门店授权.xlsx', 'Status', 'Upload Successfully')
        customer.assert_Record_result('Import Record', '批量导入门店授权.xlsx', 'Total', '2')
        customer.assert_Record_result('Import Record', '批量导入门店授权.xlsx', 'Success', '2')
        customer.assert_Record_result('Import Record', '批量导入门店授权.xlsx', 'Import Date', today)
        """断言：添加门店授权成功"""
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS")
        customer.click_search()
        customer.click_tab('Shop')
        customer.assert_Query_containsresult('Shop ID', 'SN002424')
        customer.assert_Query_containsresult('Shop ID', 'SN002425')
        """移除门店授权"""
        customer.click_function_button('Empty All Association')
        customer.click_Delete()
        DomAssert(drivers).assert_att('Successfully')
        customer.assert_NoData()

    @allure.story("门店授权")
    @allure.title("导出筛选条件下的门店授权")
    @allure.description("导出筛选条件下的门店授权")
    @allure.severity("normal")
    @pytest.mark.smoke
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_005_005(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "18650493", "xLily6x")
        """打开User Authorization菜单页面 """
        customer = UserAuthorizationPage(drivers)
        customer.click_menu("Staff & Authorization", "User Authorization")
        customer.input_search('User ID', "wjkTS")
        customer.click_search()
        """点击Shop标签页"""
        customer.click_tab('Shop')
        """导出筛选条件下的门店授权"""
        customer.click_function_button('Export Filtered')
        """断言：存在导出文件进度条"""
        customer.assert_export_success()


if __name__ == '__main__':
    pytest.main(['StaffAuthorization_UserAuthorization.py'])
