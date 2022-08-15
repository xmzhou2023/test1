from project.DCR_INDIA.page_object.PurchaseManagement_InboundReceipt import InboundReceiptPage
from project.DCR_INDIA.page_object.Center_Component import LoginPage
from public.base.assert_ui import ValueAssert
from libs.common.time_ui import sleep
import pytest
import allure


@allure.feature("采购管理-二代零售商收货")
class TestQueryInboundReceipt:
    @allure.story("查询二代零售商收货")
    @allure.title("二代用户进入Inbound Receipt页面，按日期筛选收货列表数据加载是否正常")
    @allure.description("二代用户进入Inbound Receipt页面，按日期筛选收货列表数据加载是否正常")
    @allure.severity("critical")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_001_001(self, drivers):
        user = LoginPage(drivers)
        #user.dcr_login(drivers, "BD291501", "dcr123456")

        """销售管理菜单-出库单-筛选出库单用例"""
        user.click_gotomenu("Purchase Management", "Inbound Receipt")

        query = InboundReceiptPage(drivers)
        query.click_unfold()
        query.input_delivery_date("2022-07-12")
        query.click_deliver_Order()
        query.click_select_brand()
        query.click_deliver_Order()
        query.click_search()
        query.click_fold()

        saleo_order = query.text_salesOrder()
        delivery_order = query.text_deliveryOrder()
        delivery_date = query.get_delivery_date_text()
        status = query.get_status_text()
        product = query.get_product_text()
        total = query.get_total_text()

        ValueAssert.value_assert_IsNoneNot(saleo_order)
        ValueAssert.value_assert_IsNoneNot(delivery_order)
        ValueAssert.value_assert_IsNoneNot(delivery_date)
        ValueAssert.value_assert_IsNoneNot(status)
        ValueAssert.value_assert_IsNoneNot(product)
        query.assert_total(total)
        query.click_reset()


@allure.feature("采购管理-二代零售商收货")
class TestQueryIMEIDetail:
    @allure.story("查询IMEI详情信息")
    @allure.title("二代用户进入Inbound Receipt页面，查看收货列表第一条IMEI详情信息加载是否正常")
    @allure.description("二代用户进入Inbound Receipt页面，查看收货列表第一条IMEI详情信息加载是否正常")
    @allure.severity("normal")  # 分别为5种类型等级：blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        query = InboundReceiptPage(drivers)
        query.click_unfold()
        query.click_select_brand()
        query.click_deliver_Order()
        query.click_search()
        query.click_fold()

        #获取Inbound Receipt列表字段文本
        list_brand = query.get_brand_text()
        #点击IMEI Detai功能按钮
        query.click_imei_detail()
        select_record = query.get_please_select_record()
        ValueAssert.value_assert_equal("Please select a record", select_record)
        #勾选第一条记录前的复选框
        query.select_checkbox()
        query.click_imei_detail()

        detail_material = query.get_imei_detail_material_id()
        detail_product = query.get_imei_detail_product()
        detail_itel = query.get_imei_detail_itel()
        detail_brand = query.get_imei_detail_brand()
        detail_imei = query.get_imei_detail_imei()
        detail_export = query.get_imei_detail_export()
        total = query.get_imei_detail_total()
        query.assert_total_imei_detail(total)

        ValueAssert.value_assert_IsNoneNot(detail_product)
        ValueAssert.value_assert_IsNoneNot(detail_itel)
        ValueAssert.value_assert_equal(list_brand, detail_brand)
        ValueAssert.value_assert_IsNoneNot(detail_material)
        ValueAssert.value_assert_IsNoneNot(detail_imei)
        ValueAssert.value_assert_equal("Export", detail_export)
        query.click_close_inbound_imei_detail()
        query.click_close_inbound_receipt()


if __name__ == '__main__':
    pytest.main(['PurchaseManagement_InboundReceipt.py'])
