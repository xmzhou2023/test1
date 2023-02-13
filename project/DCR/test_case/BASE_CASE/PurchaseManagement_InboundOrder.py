import datetime

import allure
import pytest

from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.PurchaseManagement_InboundOrder import InboundOrder
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("采购管理-入库单") # 模块名称
class TestInboundOrder:
    @allure.story("入库单")
    @allure.title("页面随机组合查询")
    @allure.description("随机组合查询")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        """变量"""
        query_dict = {
            'Buyer': 'BD2915',
            'Seller': 'BD403442',
            'Inbound Date': '2023-01-01To2023-01-31',
            'Delivery Date': '2023-01-01To2023-01-31',
            'Inbound ID': '01HK2301300002335',
            'Order ID': '02HK2301300000004',
            'Delivery Order ID': '02HK2301300000004',
            'Warehouse': 'WBD291502',
            'Type': 'Secondary',
            'Material ID': '10304168',
            'Brand': 'TECNO',
            'Buyer Category': '',
            'Model': 'A2 se',
            'Market Name': 'A2 se',
            'Seller Region': 'North Africa_Egypt_Cairo',
            'Buyer Region': 'North Africa_Egypt_Cairo',
            'Buyer Country': 'Bangladesh',
            'Seller Country': 'Bangladesh',
            'Buyer Type': 'Sub-dealer',
            'Seller Type': 'Distributor',
            'Upload Type': 'WEB SYNC'
        }
        add = InboundOrder(drivers)
        add.click_menu("Purchase Management", "Inbound Order")
        add.click_unfold()
        add.random_Query_Method(query_dict)


    @allure.story("入库单")
    @allure.title("导出查询记录成功")
    @allure.description("导出Inbound Order查询记录")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "lhmadmin", "xLily6x")
        """筛选IMEI"""
        InboundID = '01IN2301310004242'
        user = InboundOrder(drivers)
        user.click_menu("Purchase Management", "Inbound Order")
        user.click_unfold()
        user.input_search('Inbound ID', InboundID)
        user.click_search()
        """导出查询结果"""
        user.click_export()
        DomAssert(drivers).assert_att('Create successful , will auto downloaded , please wait')
        user.click_menu("Basic Data Management", "Export Record")
        user.assert_Record_result('Export Record', 'Inbound Order', 'Download Status', 'COMPLETE')
        user.assert_Record_result('Export Record', 'Inbound Order', 'File Size')


    @allure.story("入库单")
    @allure.title("导出详情记录成功")
    @allure.description("导出Inbound Order Detail查询记录")
    @pytest.mark.smoke  # 用例标记
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    def test_001_003(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "lhmadmin", "xLily6x")
        """筛选IMEI"""
        InboundID = '01IN2301310004242'
        user = InboundOrder(drivers)
        user.click_menu("Purchase Management", "Inbound Order")
        user.click_unfold()
        user.input_search('Inbound ID', InboundID)
        user.click_search()
        """导出查询结果"""
        user.click_export_Details()
        DomAssert(drivers).assert_att('Create successful , will auto downloaded , please wait')
        user.click_menu("Basic Data Management", "Export Record")
        user.assert_Record_result('Export Record', 'Inbound Order Detail', 'Download Status', 'COMPLETE')
        user.assert_Record_result('Export Record', 'Inbound Order Detail', 'File Size')

    @allure.story("入库单")
    @allure.title("Order IMEI功能正常")
    @allure.description("点击Order IMEI，检查订单imei数量正常，导出按钮正常")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "lhmadmin", "xLily6x")
        """打开Inbound Order"""
        user = InboundOrder(drivers)
        user.click_menu("Purchase Management", "Inbound Order")
        """获取第一个订单数量"""
        num = user.get_FirstRow_info('Order Quantity')
        user.get_FirstRow_checkbox()
        user.click_Order_IMEI()
        user.assert_Order_IMEI_result(num)
        """导出查询结果"""
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        user.click_DialogExport()
        DomAssert(drivers).assert_att('Create successful , will auto downloaded , please wait')
        user.click_menu("Basic Data Management", "Export Record")
        user.assert_Record_result('Export Record', 'Inbound Imei Detail', 'Download Status', 'COMPLETE')
        user.assert_Record_result('Export Record', 'Inbound Imei Detail', 'File Size')
        user.assert_Record_result('Export Record', 'Inbound Imei Detail', 'Create Date', today)

    @allure.story("入库单")
    @allure.title("Scaned IMEI功能正常")
    @allure.description("点击Scaned IMEI，检查订单imei数量正常，导出按钮正常")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "lhmadmin", "xLily6x")
        """打开Inbound Order"""
        user = InboundOrder(drivers)
        user.click_menu("Purchase Management", "Inbound Order")
        """获取第一个订单数量"""
        num = user.get_FirstRow_info('Order Quantity')
        user.click_First_ScanedIMEI()
        user.assert_Order_IMEI_result(num)
        """导出查询结果"""
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        user.click_DialogExport()
        DomAssert(drivers).assert_att('Create successful , will auto downloaded , please wait')
        user.click_menu("Basic Data Management", "Export Record")
        user.assert_Record_result('Export Record', 'Inbound Imei Detail', 'Download Status', 'COMPLETE')
        user.assert_Record_result('Export Record', 'Inbound Imei Detail', 'File Size')
        user.assert_Record_result('Export Record', 'Inbound Imei Detail', 'Create Date', today)


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
