import logging
from project.DCR.page_object.ShopManagement_ShopManagement import ShopManagementPage
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import *
from libs.common.connect_sql import *
from libs.common.time_ui import sleep
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

@pytest.fixture(scope='function')
def function_view_fixture(drivers):
    yield
    close = ShopManagementPage(drivers)
    close.click_close_shop_view()
    close.click_close_shop_management()

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

@allure.feature("门店管理-门店管理(global)")
class TestAddShop:
    @allure.story("新增门店")
    @allure.title("门店管理，新增门店操作")
    @allure.description("门店管理页面，新增门店操作成功后，筛选新增的门店是否加载正常")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_001_001(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Shop Management", "Shop Management(Global)")

        """新建 TECNO品牌的门店"""
        add_shop = ShopManagementPage(drivers)
        add_shop.click_add()
        """门店名称后面增加随机数字"""
        num = add_shop.shop_random()
        add_shop.input_shop_name("smartShop" + num)
        add_shop.input_contact_name("testlhm" + num)
        add_shop.input_contact_no("138730985" + num)
        add_shop.input_country_city("Barisal")
        add_shop.input_address("深圳市 南山区深圳湾生态园9B5")
        add_shop.click_brand()
        add_shop.input_sales_region("Barisal itel")
        add_shop.click_shop_grade()
        add_shop.click_shop_type()
        add_shop.click_image_type()
        add_shop.click_upload_mode()
        add_shop.input_retailer_account("SN455338")
        add_shop.click_commercial_area_tag()
        add_shop.click_submit()
        add_shop.click_query_search()

        """从数据库查询最近新建的门店ID"""
        user = SQL('DCR', 'test')
        shop_data = user.query_db(
            "select public_code,shop_name from  t_retail_shop_base where creator=99940 order by creation_time desc limit 1")
        shop_id = shop_data[0].get("public_code")
        shop_name = shop_data[0].get("shop_name")
        shop_id1 = shop_id[1:]
        logging.info("从数据库查询Shop ID：{}".format(shop_id1))

        """筛选新建的门店ID与门店名称文本内容"""
        add_shop.input_query_shop_name(shop_id1)
        add_shop.click_query_search()

        shopid = add_shop.get_shop_id_text()
        shopname = add_shop.get_shop_name_text()
        """断言数据库表中是否存在新建的门店名称"""
        sql_asser = SQLAssert('DCR', 'test')
        sql_asser.assert_sql(shopname,
                             "select shop_name from t_retail_shop_base where creator=99940 order by creation_time desc limit 1")
        """断言门店列表是否存在新建的门店ID与门店名称"""
        ValueAssert.value_assert_In(shopid, shop_id1)
        ValueAssert.value_assert_equal(shopname, shop_name)
        #add_shop.click_close_shop_management()


@allure.feature("门店管理-门店管理(global)")
class TestExpandBrandShop:
    @allure.story("扩展门店品牌")
    @allure.title("门店管理页面，对新增的门店进行扩展itel品牌操作")
    @allure.description("门店管理页面，对新增的门店进行扩展品牌操作，扩展itel品牌提交后，列表展示扩展的门店品牌")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_002_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Shop Management", "Shop Management(Global)")

        expand_brand = ShopManagementPage(drivers)
        """从数据库查询最近新建的门店ID"""
        user = SQL('DCR', 'test')
        shop_data = user.query_db(
            "select public_code,shop_name from  t_retail_shop_base where creator=99940 order by creation_time desc limit 1")
        shop_code = shop_data[0].get("public_code")
        shop_code1 = shop_code[1:]
        logging.info("从数据库查询Shop ID：{}".format(shop_code1))

        """筛选新建的门店ID与门店名称文本内容"""
        expand_brand.input_query_shop_name(shop_code1)
        expand_brand.click_query_search()

        expand_brand.click_first_checkbox()
        expand_brand.click_more_option()
        expand_brand.click_extend_brand()
        expand_brand.select_extend_brand("itel")
        expand_brand.extend_brand_save()

        expand_brand.input_extend_sales_region("Barisal itel")
        expand_brand.click_extend_shop_grade()
        expand_brand.click_extend_shop_type()
        expand_brand.click_extend_image_type()
        expand_brand.extend_retail_customer("SN455338")
        expand_brand.extend_commercial_area()
        expand_brand.click_submit()

        """获取编辑成功提示语"""
        # dom = DomAssert(drivers)
        # dom.assert_att("Edited Successfully")
        # sleep(2)
        """根据编辑的门店扩展品牌，筛选门店id，进行断言"""
        user = SQL('DCR', 'test')
        shop_data = user.query_db(
            "select public_code,shop_name from  t_retail_shop_base where creator=99940 order by creation_time desc limit 1")
        public_code = shop_data[0].get("public_code")
        public_code1 = public_code[1:]
        shopname = shop_data[0].get("shop_name")

        """增加断言，判断新增的扩展门店品牌，是否保存成功"""
        expand_brand.click_reset()
        get_public = expand_brand.get_shop_public()
        get_shop_name = expand_brand.get_shop_name_text()
        get_shop_brand = expand_brand.get_shop_brand_text()
        get_status = expand_brand.get_shop_status_text()

        ValueAssert.value_assert_In(get_public, public_code1)
        ValueAssert.value_assert_equal(get_shop_name, shopname)
        ValueAssert.value_assert_IsNoneNot(get_shop_brand)
        ValueAssert.value_assert_equal(get_status, "Enabled")
        #expand_brand.click_close_shop_management()


@allure.feature("门店管理-门店管理(global)")
class TestDisableShop:
    @allure.story("禁用门店")
    @allure.title("门店管理页面，对新增的门店进行禁用操作")
    @allure.description("门店管理页面，对新增的门店进行禁用操作")
    @allure.severity("minor")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_003_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Shop Management", "Shop Management(Global)")

        """实例化ShopManagementPage类，调用页面元素方法"""
        disable = ShopManagementPage(drivers)
        """选中门店进行禁用扩展门店"""
        shop_id1 = disable.get_shop_id_text()
        shop_name1 = disable.get_shop_name_text()

        disable.click_first_checkbox()
        disable.click_second_checkbox()
        disable.click_more_option()
        disable.click_disable_confirm()
        """获取删除成功提示语, 删除成功后显示Successfully提示语"""
        dom = DomAssert(drivers)
        dom.assert_att("Successfully")

        """增加断言，获取列表禁用前的Shop id、Shop name与删除后的 Shop id、Shop name比较是否不包含此内容"""
        shop_id2 = disable.get_shop_id_text()
        shop_name2 = disable.get_shop_name_text()
        ValueAssert.value_assert_InNot(shop_id1, shop_id2)
        ValueAssert.value_assert_InNot(shop_name1, shop_name2)
        #disable.click_close_shop_management()


@allure.feature("门店管理-门店管理(global)")
class TestEditShop:
    @allure.story("编辑门店信息")
    @allure.title("门店管理页面，Edit编辑门店信息")
    @allure.description("门店管理页面，Edit编辑门店信息，提交后，返回列表显示编辑后的门店信息")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_004_001(self, drivers):
        user5 = LoginPage(drivers)
        user5.initialize_login(drivers, "lhmadmin", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        user5.click_gotomenu("Shop Management", "Shop Management(Global)")
        """实例化ShopManagementPage类，调用页面元素方法"""
        edit = ShopManagementPage(drivers)
        # """从数据库查询最近新建的门店ID"""
        # user = SQL('DCR', 'test')
        # shop_data = user.query_db(
        #     "select public_code, shop_name from t_retail_shop_base where creator=99940 order by creation_time desc limit 1")
        # shop_id = shop_data[0].get("public_code")
        # shop_name = shop_data[0].get("shop_name")
        # logging.info("从数据库表查询最近新建的Shop ID{}".format(shop_id))
        # logging.info("从数据库表查询最近新建的Shop ID{}".format(shop_name))
        """筛选新建的门店ID记录"""
        edit.input_query_shop_name("BD026498")
        edit.click_status_filter("Disabled")
        edit.click_status_attribute()
        edit.click_query_search()

        """点击Edit按钮"""
        edit.click_edit_shop()
        """门店名称后面增加随机数字"""
        num = edit.shop_random()
        edit.input_shop_name("test_shop"+num)
        edit_shop_name = "test_shop"+num
        logging.info("获取编辑后的shop name：{}".format(edit_shop_name))

        """点击提交按钮"""
        edit.click_submit()
        DomAssert(drivers).assert_att("Edited Successfully")
        sleep(2)
        #edit.click_close_shop_management()


@allure.feature("门店管理-门店管理(global)")
class TestEnableShop:
    @allure.story("启用门店")
    @allure.title("门店管理页面，对禁用的门店，进行启用操作")
    @allure.description("门店管理页面，对禁用的门店，进行启用操作")
    @allure.severity("minor")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_005_001(self, drivers):
        user6 = LoginPage(drivers)
        user6.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例  BD026498"""
        user6.click_gotomenu("Shop Management", "Shop Management(Global)")
        """实例化ShopManagementPage类，调用页面元素方法"""
        enable = ShopManagementPage(drivers)

        """筛选门店，然后启用门店操作"""
        enable.input_query_shop_name("BD026498")
        enable.click_status_filter("Disabled")
        enable.click_status_attribute()
        enable.click_query_search()
        """获取列表最新的门店状态"""
        get_status1 = enable.get_shop_status_text()
        if "Enabled" == get_status1:
            enable.click_first_checkbox()
            enable.click_more_option()
            enable.click_disable_confirm()
            DomAssert(drivers).assert_att("Successfully")
            sleep(5)
            """获取列表最新的门店状态"""
            get_status2 = enable.get_shop_status_text()
            ValueAssert.value_assert_equal("Disabled", get_status2)
        else:
            enable.click_first_checkbox()
            enable.click_more_option()
            enable.click_enable_confirm()
            DomAssert(drivers).assert_att("Successfully")
            sleep(5)
            get_status3 = enable.get_shop_status_text()
            """断言启用操作后，门店列表是否更新为Enabled状态 """
            ValueAssert.value_assert_equal("Enabled", get_status3)
        #enable.click_close_shop_management()


@allure.feature("门店管理-门店管理(global)")
class TestExportShop:
    @allure.story("导出门店")
    @allure.title("门店管理页面，根据门店创建日期筛选门店后，进行导出操作")
    @allure.description("门店管理页面，根据门店创建日期筛选门店后，进行导出操作")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_export_fixture')
    def test_006_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例  BD026498"""
        user.click_gotomenu("Shop Management", "Shop Management(Global)")
        """实例化ShopManagementPage类，调用页面元素方法"""
        export = ShopManagementPage(drivers)

        today = Base(drivers).get_datetime_today()
        logging.info("打印当前日期：{}".format(today))

        export.click_unfold()
        """门店列表，按日期筛选门店记录"""
        export.input_create_date("2022-10-01", today)
        export.click_status_attribute()
        """点击查询按钮"""
        export.click_query_search()
        export.click_fold()

        """点击导出"""
        export.click_export()
        export.click_download_more()
        export.input_task_name("Shop Manager List")
        """循环点击查询按钮，直到获取到Download Status字段的状态更新为COMPLETE"""
        down_status = export.click_export_search()

        task_name = export.get_task_name_text()
        file_size = export.get_file_size_text()

        task_id = export.get_task_user_id_text()
        create_date = export.get_create_date_text()
        complete_date = export.get_complete_date_text()
        export_time = export.get_export_time_text()
        operation = export.get_operation_text()

        ValueAssert.value_assert_equal(down_status, "COMPLETE")
        ValueAssert.value_assert_equal(task_name, "Shop Manager List")
        ValueAssert.value_assert_equal(task_id, "lhmadmin")
        ValueAssert.value_assert_equal(create_date, today)
        ValueAssert.value_assert_equal(complete_date, today)
        ValueAssert.value_assert_equal(operation, "Download")
        export.assert_file_time_size(file_size, export_time)
        #export.click_close_export_record()
        #export.click_close_shop_management()


@allure.feature("门店管理-门店管理(global)")
class TestQueryGlobalShop:
    @allure.story("查询全球门店")
    @allure.title("门店管理页面，按门店ID与状态条件筛选全球门店列表数据加载是否正常")
    @allure.description("门店管理页面，按门店ID与状态条件筛选全球门店列表数据加载是否正常")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_menu_fixture')
    def test_007_001(self, drivers):
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Shop Management", "Shop Management(Global)")

        """实例化ShopManagementPage类，调用页面元素方法"""
        query = ShopManagementPage(drivers)
        today = Base(drivers).get_datetime_today()
        logging.info("打印当前日期：{}".format(today))

        query.click_unfold()
        """门店列表，按日期筛选门店记录"""
        query.input_create_date("2022-08-20", today)
        query.click_status_attribute()
        """点击查询按钮"""
        query.click_query_search()
        query.click_fold()

        """断言筛选后列表是否存在门店记录，分页总数是否有记录"""
        get_list_shop_id = query.get_list_shop_id_text()
        get_list_shop_name = query.get_list_shop_name_text()
        get_list_brand = query.get_list_brand_text()
        get_public_id = query.get_list_public_id_text()

        ValueAssert.value_assert_IsNoneNot(get_list_shop_id)
        ValueAssert.value_assert_IsNoneNot(get_list_shop_name)
        ValueAssert.value_assert_IsNoneNot(get_list_brand)
        ValueAssert.value_assert_IsNoneNot(get_public_id)
        total = query.get_total_text()
        query.assert_total(total)


    @allure.story("查询全球门店")
    @allure.title("门店管理页面，查看View门店详情信息是否正确")
    @allure.description("门店管理页面，查看View门店详情信息是否正确")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.usefixtures('function_view_fixture')
    def test_007_002(self, drivers):
        user4 = LoginPage(drivers)
        user4.initialize_login(drivers, "lhmadmin", "dcr123456")
        """销售管理菜单-出库单-筛选出库单用例"""
        user4.click_gotomenu("Shop Management", "Shop Management(Global)")
        """实例化ShopManagementPage类，调用页面元素方法"""
        view = ShopManagementPage(drivers)
        # """从数据库查询最近新建的门店ID"""
        # user = SQL('DCR', 'test')
        # shop_data = user.query_db(
        #     "select public_code, shop_name from t_retail_shop_base where creator=99940 order by creation_time desc limit 1")
        # shop_id = shop_data[0].get("public_code")
        # shop_name = shop_data[0].get("shop_name")
        # logging.info("从数据库表查询最近新建的Shop ID{}".format(shop_id))
        # logging.info("从数据库表查询最近新建的Shop ID{}".format(shop_name))

        """筛选新建的门店ID记录"""
        view.input_query_shop_name("BD026498")
        view.click_status_filter("Disabled")
        view.click_status_attribute()
        view.click_query_search()

        list_shop_name = view.get_list_shop_name_text()
        list_public_id = view.get_list_public_id_text()
        list_contact_name = view.get_list_contact_name_text()
        list_contact_no = view.get_list_contact_no_text()

        """点击view打开门店详情页"""
        view.click_view_shop()
        view_shop_name = view.get_view_shop_name_text()
        view_contact_name = view.get_view_contact_name_text()
        view_contact_no = view.get_view_contact_no_text()
        view_public_id = view.get_view_public_id_text()

        """断言获取列表的门店基本信息与 查看view详情页面的信息是否一致"""
        ValueAssert.value_assert_equal(list_shop_name, view_shop_name)
        ValueAssert.value_assert_equal(list_contact_name, view_contact_name)
        ValueAssert.value_assert_equal(list_contact_no, view_contact_no)
        ValueAssert.value_assert_equal(list_public_id, view_public_id)
        """点击关闭view页面"""
        #view.click_close_shop_view()
        #view.click_close_shop_management()


# #暂时无删除功能，用例留着
# @allure.feature("门店管理-门店管理(global)")
# class TestDeleteShop:
#     @allure.story("删除门店")
#     @allure.title("门店管理页面，对新增的扩展品牌门店进行删除操作")
#     @allure.description("门店管理页面，对新增的扩展品牌门店进行删除操作")
#     @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
#     def test_008_001(self, drivers):
#         """实例化ShopManagementPage类，调用页面元素方法"""
#         del_shop = ShopManagementPage(drivers)
#         """选中门店进行删除扩展门店"""
#         shop_id1 = del_shop.get_shop_id_text()
#         shop_name1 = del_shop.get_shop_name_text()
#         del_shop.click_first_checkbox()
#         del_shop.click_second_checkbox()
#         del_shop.click_more_option()
#         del_shop.click_delete()
#         del_shop.click_confirm_delete()
#         """获取删除成功提示语, 删除成功后显示Successfully提示语"""
#         dom = DomAssert(drivers)
#         dom.assert_att("Successfully")
#
#         """增加断言，获取列表删除前的Shop id、Shop name与删除后的 Shop id、Shop name比较是否不包含此内容"""
#         del_shop.click_query_search()
#         shop_id2 = del_shop.get_shop_id_text()
#         shop_name2 = del_shop.get_shop_name_text()
#         ValueAssert.value_assert_InNot(shop_id1, shop_id2)
#         ValueAssert.value_assert_InNot(shop_name1, shop_name2)
#         sleep(1)


if __name__ == '__main__':
    pytest.main(['ShopManagement_ShopManagement.py'])
