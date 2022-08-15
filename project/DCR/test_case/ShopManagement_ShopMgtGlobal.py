from project.DCR.page_object.ShopManagement_ShopMgtGlobal import ShopManagementPage
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import *
from libs.common.connect_sql import *
from libs.common.time_ui import sleep
import pytest
import allure


@allure.feature("门店管理-门店管理(global)")
class TestAddShop:
    @allure.story("新增门店")
    @allure.title("门店管理，新增门店操作")
    @allure.description("门店管理页面，新增门店操作成功后，筛选新增的门店是否加载正常")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "lhmadmin", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        menu = LoginPage(drivers)
        menu.click_gotomenu("Shop Management", "Shop Management(Global)")

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
        """获取列表新建的门店ID与门店名称文本内容"""
        add_shop.input_query_shop_name(shop_name, shop_name)
        add_shop.click_query_search()

        shopid = add_shop.get_shop_id_text()
        shopname = add_shop.get_shop_name_text()
        """断言数据库表中是否存在新建的门店名称"""
        sql_asser = SQLAssert('DCR', 'test')
        sql_asser.assert_sql(shopname,
                             "select shop_name from t_retail_shop_base where creator=99940 order by creation_time desc limit 1")
        """断言门店列表是否存在新建的门店ID与门店名称"""
        ValueAssert.value_assert_In(shopid, shop_id)
        ValueAssert.value_assert_equal(shopname, shop_name)
        add_shop.click_reset()


@allure.feature("门店管理-门店管理(global)")
class TestEditShop:
    @allure.story("扩展门店品牌")
    @allure.title("门店管理页面，对新增的门店进行扩展itel品牌操作")
    @allure.description("门店管理页面，对新增的门店进行扩展品牌操作，扩展itel品牌提交后，列表展示扩展的门店品牌")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_002(self, drivers):
        edit_shop = ShopManagementPage(drivers)
        """从数据库查询最近新建的门店ID"""
        edit_shop.click_first_checkbox()
        edit_shop.click_more_option()
        edit_shop.click_extend_brand()
        edit_shop.select_extend_brand("itel")
        edit_shop.extend_brand_save()

        edit_shop.input_extend_sales_region("Barisal itel")
        edit_shop.click_extend_shop_grade()
        edit_shop.click_extend_shop_type()
        edit_shop.click_extend_image_type()
        edit_shop.extend_retail_customer("SN455338")
        edit_shop.extend_commercial_area()
        edit_shop.click_submit()

        """获取删除成功提示语, 删除成功后显示No Data提示语"""
        #dom = DomAssert(drivers)
        #dom.assert_att("Edited Successfully")
        sleep(2)
        """根据编辑的门店扩展品牌，筛选门店id，进行断言"""
        user = SQL('DCR', 'test')
        shop_data = user.query_db(
            "select public_code,shop_name from  t_retail_shop_base where creator=99940 order by creation_time desc limit 1")
        public_code = shop_data[0].get("public_code")
        shopname = shop_data[0].get("shop_name")

        """增加断言，判断新增的扩展门店品牌，是否保存成功"""
        shop_id = edit_shop.get_extend_shop_id_text()
        shop_name = edit_shop.get_shop_name_text()
        shop_brand = edit_shop.get_shop_brand_text()
        status = edit_shop.get_shop_status_text()
        ValueAssert.value_assert_In(shop_id, public_code)
        ValueAssert.value_assert_equal(shop_name, shopname)
        ValueAssert.value_assert_equal(shop_brand, "itel")
        ValueAssert.value_assert_equal(status, "Enabled")
        sleep(2)


@allure.feature("门店管理-门店管理(global)")
class TestDeleteShop:
    @allure.story("禁用门店")
    @allure.title("门店管理页面，对新增的门店进行禁用操作")
    @allure.description("门店管理页面，对新增的门店进行禁用操作")
    @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_003(self, drivers):
        """实例化ShopManagementPage类，调用页面元素方法"""
        disable = ShopManagementPage(drivers)
        """选中门店进行删除扩展门店"""
        shop_id1 = disable.get_shop_id_text()
        shop_name1 = disable.get_shop_name_text()

        disable.click_first_checkbox()
        disable.click_second_checkbox()
        disable.click_more_option()
        disable.click_disable_confirm()
        """获取删除成功提示语, 删除成功后显示Successfully提示语"""
        dom = DomAssert(drivers)
        dom.assert_att("Successfully")

        """增加断言，获取列表删除前的Shop id、Shop name与删除后的 Shop id、Shop name比较是否不包含此内容"""
        shop_id2 = disable.get_shop_id_text()
        shop_name2 = disable.get_shop_name_text()
        ValueAssert.value_assert_InNot(shop_id1, shop_id2)
        ValueAssert.value_assert_InNot(shop_name1, shop_name2)
        sleep(1)


#暂时无删除功能，用例留着
# @allure.feature("门店管理-门店管理(global)")
# class TestDeleteShop:
#     @allure.story("删除门店")
#     @allure.title("门店管理页面，对新增的扩展品牌门店进行删除操作")
#     @allure.description("门店管理页面，对新增的扩展品牌门店进行删除操作")
#     @allure.severity("blocker")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
#     def test_001_003(self, drivers):
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
    pytest.main(['ShopManagement_ShopMgtGlobal.py'])
