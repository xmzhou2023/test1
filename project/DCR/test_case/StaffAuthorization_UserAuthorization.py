from project.DCR.page_object.StaffAuthorization_UserAuthorization import UserAuthorizationPage
from project.DCR.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert, DomAssert
from libs.common.time_ui import sleep
from libs.common.logger_ui import log
import pytest
import allure


@allure.feature("员工授权-用户授权")
class TestDeleteBrandAuthorization():
    @allure.story("删除品牌授权")
    @allure.title("用户授权页面，删除Infinix品牌授权")
    @allure.description("用户授权页面，筛选User：NG2061301，删除Infinix品牌授权")
    @allure.severity("normal")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        """DCR 管理员账号登录"""
        user = LoginPage(drivers)
        user.dcr_login(drivers, "lhmadmin", "dcr123456")
        sleep(5)

        """打开User Authorization菜单页面 """
        user.click_gotomenu("Staff & Authorization", "User Authorization")
        sleep(5)

        """如果存在infinix品牌则删除infinix品牌，如果不存在infinix品牌则添加infinix品牌"""
        brand = UserAuthorizationPage(drivers)
        brand.input_dealer_user_query("NG2061301")
        brand.click_search()

        list_infinix = brand.get_list_infinix_text()
        log.info("list_infinix{}".format(list_infinix))

        """如果存在删除Infinix品牌"""
        if "Infinix" == list_infinix:
            """如果存在Infinix品牌，则删除此品牌"""
            brand.click_cancel_association()
            brand.click_delete_brand()
            """断言页面是否存在Successfully成功提示语"""
            domassert = DomAssert(drivers)
            domassert.assert_att("Successfully")
            sleep(2)


@allure.feature("员工授权-用户授权")
class TestAddBrandAuthorization():
    @allure.story("新增品牌授权")
    @allure.title("用户授权页面，新增Infinix品牌授权")
    @allure.description("用户授权页面，筛选User：NG2061301，新增Infinix品牌授权")
    @allure.severity("normal")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        """添如果不存在则添加Infinix品牌"""
        brand = UserAuthorizationPage(drivers)
        brand.click_add_brand()
        get_add_infinix = brand.get_add_infinix_text()
        ValueAssert.value_assert_equal("Infinix", get_add_infinix)
        brand.click_add_brand_checkbox()
        brand.click_save_brand()

        domassert = DomAssert(drivers)
        domassert.assert_att("Successfully")
        list_infinix_text = brand.get_list_infinix_text()
        ValueAssert.value_assert_equal("Infinix", list_infinix_text)
        sleep(2)


@allure.feature("员工授权-用户授权")
class TestDeleteCustAuthorization():
    @allure.story("删除客户授权")
    @allure.title("用户授权页面，删除CN20009客户授权")
    @allure.description("用户授权页面，筛选User：NG2061301，删除CN20009客户授权")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_003_001(self, drivers):
        customer = UserAuthorizationPage(drivers)
        customer.click_customer_tab()
        customer.input_list_customer("CN20009")
        customer.click_customer_search()
        get_cust = customer.get_list_customer_id()
        if get_cust == "CN20009":
            customer.click_list_cust_checkbox()
        customer.click_cust_more_option()
        customer.click_cust_cancel_association()
        customer.click_cust_delete()

        domassert = DomAssert(drivers)
        domassert.assert_att("Successfully")
        customer.click_brand_tab()
        customer.click_customer_tab()


@allure.feature("员工授权-用户授权")
class TestAddCustAuthorization():
    @allure.story("新增客户授权")
    @allure.title("用户授权页面，新增CN20009客户授权")
    @allure.description("用户授权页面，筛选User：NG2061301，新增CN20009客户授权")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_004_001(self, drivers):
        customer = UserAuthorizationPage(drivers)
        customer.click_add_customer()
        customer.click_input_customer("CN20009")
        customer.click_add_customer_search()
        get_customer_id = customer.get_customer_id_text()
        if get_customer_id in "CN20009":
            customer.click_add_customer_checkbox()
            customer.click_cust_authoriz_select()
            domassert = DomAssert(drivers)
            domassert.assert_att("Successfully")
        sleep(2)


@allure.feature("员工授权-用户授权")
class TestDeleteWareAuthorization():
    @allure.story("删除仓库授权")
    @allure.title("用户授权页面，删除WNG2061304仓库授权")
    @allure.description("用户授权页面，筛选User：NG2061301，删除WNG2061304 仓库授权")
    @allure.severity("normal")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_005_001(self, drivers):
        ware = UserAuthorizationPage(drivers)
        ware.click_warehouse_tab()
        ware.input_list_query_ware("WNG2061304")
        ware.click_warehouse_list_search()
        get_list_ware = ware.get_list_warehouseID_text()
        if get_list_ware == "WNG2061304":
            ware.click_list_ware_checkbox()
        ware.click_ware_more_option()
        ware.click_ware_cancel_association()
        ware.click_ware_delete()

        domassert = DomAssert(drivers)
        domassert.assert_att("Successfully")
        sleep(1)
        get_no_data = ware.get_ware_dele_no_data()
        ValueAssert.value_assert_In(get_no_data, "No Data")
        sleep(2)

@allure.feature("员工授权-用户授权")
class TestAddWareAuthorization():
    @allure.story("新增仓库授权")
    @allure.title("用户授权页面，新增WNG2061304仓库授权")
    @allure.description("用户授权页面，筛选User：NG2061301，新增WNG2061304 仓库授权")
    @allure.severity("normal")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_006_001(self, drivers):
        ware = UserAuthorizationPage(drivers)
        ware.click_add_association_ware()
        ware.input_add_query_ware("WNG2061304")
        ware.click_add_ware_search()
        get_add_ware = ware.get_add_warehouseid_text()
        if get_add_ware == "WNG2061304":
            ware.click_add_ware_checkbox()
        ware.click_add_ware_save()

        domassert = DomAssert(drivers)
        domassert.assert_att("Successfully")
        get_list_ware2 = ware.get_list_warehouseID_text()
        ValueAssert.value_assert_equal(get_add_ware, get_list_ware2)
        sleep(2)


@allure.feature("员工授权-用户授权")
class TestAddRegionAuthorization():
    @allure.story("新增销售区域")
    @allure.title("用户授权页面，新增销售区域授权")
    @allure.description("用户授权页面，筛选User：testlhm0215，新增销售区域授权")
    @allure.severity("normal")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_007_001(self, drivers):
        sale_region = UserAuthorizationPage(drivers)
        sale_region.input_trans_user_query("testlhm0215")
        sale_region.click_search()
        sale_region.click_sales_region_tab()
        sale_region.click_east_africa_checkbox()
        sale_region.click_score_user_checkbox()
        sale_region.click_save_sales_region()

        domassert = DomAssert(drivers)
        domassert.assert_att("Successfully")
        sleep(2)


@allure.feature("员工授权-用户授权")
class TestDeleteShopAuthorization():
    @allure.story("删除门店授权")
    @allure.title("用户授权页面，删除EG000378门店授权")
    @allure.description("用户授权页面，筛选User：testlhm0215，删除Shop ID:EG000378授权")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_008_001(self, drivers):
        shop = UserAuthorizationPage(drivers)
        shop.click_shop_tab()
        shop.input_list_query_shop("EG000378")
        shop.click_shop_list_search()
        get_list_shop = shop.get_list_shop_text()
        if get_list_shop == "EG000378":
            shop.click_list_shop_checkbox()
        shop.click_shop_more_option()
        shop.click_shop_cancel_association()
        shop.click_shop_delete()

        domassert = DomAssert(drivers)
        domassert.assert_att("Successfully")
        get_shop_no_data = shop.get_shop_delete_no_data()
        ValueAssert.value_assert_In(get_shop_no_data, "No Data")
        sleep(2)


@allure.feature("员工授权-用户授权")
class TestAddShopAuthorization():
    @allure.story("新增门店授权")
    @allure.title("用户授权页面，新增EG000378门店授权")
    @allure.description("用户授权页面，筛选User：testlhm0215，新增Shop ID:EG000378授权")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_009_001(self, drivers):
        shop = UserAuthorizationPage(drivers)
        shop.click_add_association_shop()
        shop.input_add_query_shop("EG000378")
        shop.click_add_shop_search()
        get_add_shop_id = shop.get_add_shop_id_text()
        if get_add_shop_id == "EG000378":
            shop.click_add_shop_checkbox()
        shop.click_add_shop_author_select()

        domassert = DomAssert(drivers)
        domassert.assert_att("Successfully")
        get_list_shop_id = shop.get_list_shop_id_text()
        ValueAssert.value_assert_equal(get_list_shop_id, "EG000378")


if __name__ == '__main__':
    pytest.main(['StaffAuthorization_UserAuthorization.py'])
