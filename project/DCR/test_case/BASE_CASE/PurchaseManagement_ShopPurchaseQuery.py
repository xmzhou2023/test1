import datetime
import time

import allure
import pytest

from project.DCR.page_object.Center_Component import LoginPage
from project.DCR.page_object.PurchaseManagement_ShopPurchaseQuery import ShopPurchaseQuery
from project.DCR.page_object.SalesManagement_ShopSalesQuery import ShopSaleQueryPage
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("采购管理-门店采购查询") # 模块名称
class TestShopPurchaseQuery:
    @allure.story("门店采购查询")
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
            'Shop': 'CN000132',
            'Sales Region': 'New Market_Pakistan-itel_North-itel',
            'IMEI': '354082547473884',
            'Brand': 'itel',
            'First Category': 'Mobile',
            'Model': 'it2173',
            'Item': 'it2173',
            'Creator': 'lxjcxyyd111',
            'Create Date': '2023-01-01To2023-01-31',
            'Status': 'Committed',
            'Manpower Type': 'Unmanned',
            'SP/FP': 'Feature',
            'Market Name': 'it2173',
            'Retailer': 'IN405556',
            'Public ID': 'PCN000130',
            'Country': 'Pakistan',
            'Source': 'App Scan',
            'Inbound Date': '2023-01-01To2023-01-31',
            'Activation Status': 'Activated',
            'Activated Date': '2021-09-01To2023-01-31',
            'Activation Country': 'Nigeria',
            'Delivery Country': 'Nigeria',
            'Belong MD': '',
            'Supplier': 'IN402932'
        }
        add = ShopPurchaseQuery(drivers)
        add.click_menu("Purchase Management", "Shop Purchase Query")
        add.click_unfold()
        add.random_Query_Method(query_dict)


    @allure.story("门店采购查询")
    @allure.title("逻辑冲突的查询条件查询结果为空：是否激活&激活时间")
    @allure.description("逻辑冲突的查询条件查询结果为空：是否激活&激活时间")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_001_002(self, drivers):
        """ lhmadmin管理员账号登录"""
        user = LoginPage(drivers)
        user.initialize_login(drivers, "lhmadmin", "dcr123456")
        add = ShopPurchaseQuery(drivers)
        add.click_menu("Purchase Management", "Shop Purchase Query")
        add.click_unfold()
        add.input_search('Activation Status', 'Not Activated')
        add.input_search('Create Date', '2021-01-01To2023-01-31')
        add.input_search('Activated Date', '2021-01-01To2023-01-31')
        add.click_search()
        add.assert_NoData()

    @allure.story("门店采购查询")
    @allure.title("撤回门店入库单成功")
    @allure.description("取消撤回门店入库单：Commited状态的可取消")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SenegalwjkPromoterInfinix", "xLily6x")
        """前置：重置导入数据"""
        IMEI = '356209114086694'
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        user = ShopPurchaseQuery(drivers)
        user.reset_ShopPurchaseQuery_import(IMEI)
        """库存上报"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_import()
        user.import_file('撤回门店入库单成功.xlsx')
        user.assert_import_success()
        user.click_save()
        DomAssert(drivers).assert_att('The file has been uploaded successfully. Data is being imported, please wait for a few minutes and go to the Import Record page to check the results.')
        user.click_confirm()
        """断言ImportRecord页面结果"""
        user.assert_Record_result('Import Record', '撤回门店入库单成功.xlsx', 'Status', 'Upload Successfully')
        user.assert_Record_result('Import Record', '撤回门店入库单成功.xlsx', 'Total', '1')
        user.assert_Record_result('Import Record', '撤回门店入库单成功.xlsx', 'Success', '1')
        user.assert_Record_result('Import Record', '撤回门店入库单成功.xlsx', 'Import Date', today)
        """Shop Purchase Query页面点击指定imei复选框，取消"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_search('IMEI', IMEI)
        user.input_search('Status', 'Committed')
        user.click_search()
        user.click_checkbox(IMEI)
        user.click_cancel()
        DomAssert(drivers).assert_att('Cancel success')


    @allure.story("门店采购查询")
    @allure.title("撤回门店入库单失败")
    @allure.description("取消撤回门店入库单：Canceled状态的不可取消")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SenegalwjkPromoterInfinix", "xLily6x")
        """筛选IMEI"""
        IMEI = '356514117190074'
        user = ShopPurchaseQuery(drivers)
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_search('IMEI', IMEI)
        user.input_search('Status', 'Canceled')
        user.click_search()
        """Shop Purchase Query页面点击指定imei复选框，取消"""
        user.click_checkbox(IMEI)
        user.click_cancel()
        DomAssert(drivers).assert_att('The IMEI has been cancelled.')


    @allure.story("门店采购查询")
    @allure.title("导出查询记录成功")
    @allure.description("导出Shop Purchase Query查询记录")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SenegalwjkPromoterInfinix", "xLily6x")
        """筛选IMEI"""
        IMEI = '356514117190074'
        user = ShopPurchaseQuery(drivers)
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_search('IMEI', IMEI)
        user.input_search('Status', 'Canceled')
        user.click_search()
        """导出查询结果"""
        user.click_export()
        DomAssert(drivers).assert_att('Create successful , will auto downloaded , please wait')
        user.click_menu("Basic Data Management", "Export Record")
        user.assert_Record_result('Export Record', 'Shop Purchase Query', 'Download Status', 'COMPLETE')
        user.assert_Record_result('Export Record', 'Shop Purchase Query', 'File Size')


    @allure.story("门店采购查询")
    @allure.title("批量导入门店库存成功，配置项：Whether Transfer Stock To Shop，配置1")
    @allure.description("批量导入门店库存，配置项：Whether Transfer Stock To Shop，配置1，门店手动上报库存减零售商库存")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    @pytest.mark.smoke  # 用例标记
    def test_001_006(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SenegalwjkPromoterInfinix", "xLily6x")
        """前置：重置导入数据"""
        IMEI1 = '356514118470111'
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        user = ShopPurchaseQuery(drivers)
        user.reset_ShopPurchaseQuery_import(IMEI1)
        """库存上报"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_import()
        user.import_file('批量导入门店库存成功.xlsx')
        user.assert_import_success()
        user.click_save()
        DomAssert(drivers).assert_att('The file has been uploaded successfully. Data is being imported, please wait for a few minutes and go to the Import Record page to check the results.')
        user.click_confirm()
        """断言ImportRecord页面结果"""
        user.assert_Record_result('Import Record', '批量导入门店库存成功.xlsx', 'Status', 'Upload Successfully')
        user.assert_Record_result('Import Record', '批量导入门店库存成功.xlsx', 'Total', '1')
        user.assert_Record_result('Import Record', '批量导入门店库存成功.xlsx', 'Success', '1')
        user.assert_Record_result('Import Record', '批量导入门店库存成功.xlsx', 'Import Date', today)
        """断言ShopPurchaseQuery页面结果"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_search('IMEI', IMEI1)
        user.input_search('Status', 'Committed')
        user.click_search()
        user.assert_Query_result('IMEI', IMEI1)
        """断言Report Analysis/IMEI Inventory Query页面结果"""
        user.click_menu("Report Analysis", "IMEI Inventory Query")
        user.click_unfold()
        user.input_search('IMEI', IMEI1)
        user.click_search()
        user.assert_NoData()
        """Shop Purchase Query页面点击指定imei复选框，取消"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_search('IMEI', IMEI1)
        user.input_search('Status', 'Committed')
        user.click_search()
        user.click_checkbox(IMEI1)
        user.click_cancel()
        DomAssert(drivers).assert_att('Cancel success')
        """断言Report Analysis/IMEI Inventory Query页面结果：取消库存上报后，零售商库存还原"""
        user.click_menu("Report Analysis", "IMEI Inventory Query")
        user.click_unfold()
        user.input_search('IMEI', IMEI1)
        user.click_search()
        user.assert_InventoryQuery_result('IMEI/SN', IMEI1)

    @allure.story("门店采购查询")
    @allure.title("批量导入门店库存成功，配置项：Whether Transfer Stock To Shop，配置0")
    @allure.description("批量导入门店库存，配置项：Whether Transfer Stock To Shop，配置0，门店手动上报库存不减零售商库存")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    def test_001_007(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SenegalwjkPromoterTECNO", "xLily6x")
        """前置：重置导入数据"""
        IMEI1 = '358870660332002'
        IMEI2 = '358870660818026'
        IMEI_List = '358870660332002,358870660818026'
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        user = ShopPurchaseQuery(drivers)
        salesReset = ShopSaleQueryPage(drivers)
        salesReset.reset_ShopSalesQuery_import(IMEI1)
        salesReset.reset_ShopSalesQuery_import(IMEI2)
        user.reset_ShopPurchaseQuery_import(IMEI1)
        user.reset_ShopPurchaseQuery_import(IMEI2)
        """库存上报"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_import()
        user.import_file('批量导入门店库存成功不扣减零售商库存.xlsx')
        user.assert_import_success()
        user.click_save()
        DomAssert(drivers).assert_att('The file has been uploaded successfully. Data is being imported, please wait for a few minutes and go to the Import Record page to check the results.')
        user.click_confirm()
        """断言ImportRecord页面结果"""
        user.assert_Record_result('Import Record', '批量导入门店库存成功不扣减零售商库存.xlsx', 'Status', 'Upload Successfully')
        user.assert_Record_result('Import Record', '批量导入门店库存成功不扣减零售商库存.xlsx', 'Total', '2')
        user.assert_Record_result('Import Record', '批量导入门店库存成功不扣减零售商库存.xlsx', 'Success', '2')
        user.assert_Record_result('Import Record', '批量导入门店库存成功不扣减零售商库存.xlsx', 'Import Date', today)
        """断言ShopPurchaseQuery页面结果"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_search('IMEI', IMEI_List)
        user.input_search('Status', 'Committed')
        user.click_search()
        user.assert_Query_result('IMEI', IMEI1)
        user.assert_Query_result('IMEI', IMEI2)
        """断言Report Analysis/IMEI Inventory Query页面结果：门店手动上报库存不减零售商库存"""
        user.click_menu("Report Analysis", "IMEI Inventory Query")
        user.click_unfold()
        user.input_search('IMEI', IMEI_List)
        user.click_search()
        user.assert_InventoryQuery_result('IMEI/SN', IMEI1)
        user.assert_InventoryQuery_result('IMEI/SN', IMEI2)
        # """Shop Sales Query页面点击指定imei复选框，删除"""
        # salesReset.click_menu("Sales Management", "Shop Sales Query")
        # salesReset.click_unfold()
        # salesReset.input_ShopSalesQuery_query('IMEI/SN', IMEI_List)
        # salesReset.click_search()
        # salesReset.click_checkbox(IMEI1)
        # salesReset.click_checkbox(IMEI2)
        # salesReset.click_delete()
        # DomAssert(drivers).assert_att('Deleted Successfully')
        """Shop Purchase Query页面点击指定imei复选框，取消"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_search('IMEI', IMEI_List)
        user.input_search('Status', 'Committed')
        user.click_search()
        user.click_checkbox(IMEI1)
        user.click_checkbox(IMEI2)
        user.click_cancel()
        DomAssert(drivers).assert_att('Cancel success')

    @allure.story("门店采购查询")
    @allure.title("配置项：stock activation date limit，配置1，门店手动上报激活时间超过1天的imei失败")
    @allure.description("配置项：stock activation date limit，配置1，门店手动上报激活时间超过1天的imei失败")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    def test_001_008(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SenegalwjkPromoterInfinix3", "xLily6x")
        """前置：重置导入数据"""
        IMEI = '356209114086694'
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        user = ShopPurchaseQuery(drivers)
        user.reset_ShopPurchaseQuery_import(IMEI)
        """库存上报"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_import()
        user.import_file('批量导入门店库存成功1失败1_激活日期.xlsx')
        user.assert_import_success()
        user.click_save()
        DomAssert(drivers).assert_att('The file has been uploaded successfully. Data is being imported, please wait for a few minutes and go to the Import Record page to check the results.')
        user.click_confirm()
        """断言ImportRecord页面结果"""
        user.assert_Record_result('Import Record', '批量导入门店库存成功1失败1_激活日期.xlsx', 'Status', 'Upload Successfully')
        user.assert_Record_result('Import Record', '批量导入门店库存成功1失败1_激活日期.xlsx', 'Total', '2')
        user.assert_Record_result('Import Record', '批量导入门店库存成功1失败1_激活日期.xlsx', 'Success', '1')
        user.assert_Record_result('Import Record', '批量导入门店库存成功1失败1_激活日期.xlsx', 'Failed', '1')
        user.assert_Record_result('Import Record', '批量导入门店库存成功1失败1_激活日期.xlsx', 'Import Date', today)
        """断言ShopPurchaseQuery页面结果"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_search('IMEI', IMEI)
        user.input_search('Status', 'Committed')
        user.click_search()
        user.assert_Query_result('IMEI', IMEI)
        """Shop Purchase Query页面点击指定imei复选框，取消"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_search('IMEI', IMEI)
        user.input_search('Status', 'Committed')
        user.click_search()
        user.click_checkbox(IMEI)
        user.click_cancel()
        DomAssert(drivers).assert_att('Cancel success')

    @allure.story("门店采购查询")
    @allure.title("配置项：verifing imei country when upload inventory，配置1，门店手动上报不同国家失败")
    @allure.description("配置项：verifing imei country when upload inventory，配置1，门店手动上报不同国家失败")
    @allure.severity("normal")  # 分别为3种类型等级：critical\normal\minor
    def test_001_009(self, drivers):
        menu = LoginPage(drivers)
        menu.initialize_login(drivers, "SenegalwjkPromoterInfinix3", "xLily6x")
        """前置：重置导入数据"""
        IMEI = '356209114086694'
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        user = ShopPurchaseQuery(drivers)
        user.reset_ShopPurchaseQuery_import(IMEI)
        """库存上报"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_import()
        user.import_file('批量导入门店库存成功1失败1_校验国家.xlsx')
        user.assert_import_success()
        user.click_save()
        DomAssert(drivers).assert_att('The file has been uploaded successfully. Data is being imported, please wait for a few minutes and go to the Import Record page to check the results.')
        user.click_confirm()
        """断言ImportRecord页面结果"""
        user.assert_Record_result('Import Record', '批量导入门店库存成功1失败1_校验国家.xlsx', 'Status', 'Upload Successfully')
        user.assert_Record_result('Import Record', '批量导入门店库存成功1失败1_校验国家.xlsx', 'Total', '2')
        user.assert_Record_result('Import Record', '批量导入门店库存成功1失败1_校验国家.xlsx', 'Success', '1')
        user.assert_Record_result('Import Record', '批量导入门店库存成功1失败1_校验国家.xlsx', 'Failed', '1')
        user.assert_Record_result('Import Record', '批量导入门店库存成功1失败1_校验国家.xlsx', 'Import Date', today)
        """断言ShopPurchaseQuery页面结果"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_search('IMEI', IMEI)
        user.input_search('Status', 'Committed')
        user.click_search()
        user.assert_Query_result('IMEI', IMEI)
        """Shop Purchase Query页面点击指定imei复选框，取消"""
        user.click_menu("Purchase Management", "Shop Purchase Query")
        user.click_unfold()
        user.input_search('IMEI', IMEI)
        user.input_search('Status', 'Committed')
        user.click_search()
        user.click_checkbox(IMEI)
        user.click_cancel()
        DomAssert(drivers).assert_att('Cancel success')


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
