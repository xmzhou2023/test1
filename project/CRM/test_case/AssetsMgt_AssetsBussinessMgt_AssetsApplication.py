import allure
import pytest
from project.CRM.page_object.OperationMgt_PolicyAndProfits_ProfitsTypeMgt import *
from project.CRM.page_object.Center_Component import *
from public.base.assert_ui import *
import logging
from project.CRM.page_object.AssetsMgt_AssetsBussinessMgt_AssetsApplication import *


"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@pytest.fixture(scope='module' , autouse=True) # 模块名称
def module_fixture(drivers):
    logging.info("模块前置条件，前往AssetsMgt页面")
    user = NavPage(drivers)
    user.refresh_page()
    user.click_gotonav_CRM("AssetsMgt", "AssetsBuessinessMgt", "AssetsApplication")  # 点击菜单
    user= DomAssert(drivers)
    sleep(1)
    user.assert_url("assetsMgt/assetsBusinessMgt/assetsApplication")
    yield
    logging.info("后置条件：收起菜单")
    user = NavPage(drivers)
    user.click_gotonav("AssetsMgt")


@allure.feature("AssetsBussinessMgt") # 模块名称
class TestAssetsApplication:
    @allure.story("AssetsBussiness_AssetsApplication") # 场景名称
    @allure.title("AssetsApplication页whetherReturn筛选")  # 用例名称
    @allure.description("对whetherReturn查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.parametrize("status, code",
                             [("Yes", "1"), ("No", "0")])
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers, status, code):   # 用例名称取名规范'test+场景编号+用例编号'
        user = AssetsMgtPage(drivers)
        user.Get_search(status, choice="whetherReturn")
        user.assets_search()
        user = NavPage(drivers)
        get_total = user.get_total()
        user = SQL("CRM", "test")
        s_ser = user.query_db("SELECT COUNT(*) FROM crm_wms_assets_application aa WHERE aa.whether_return = {} AND aa.is_deleted = 0;".format(code))
        sql_qty = s_ser[0].get("COUNT(*)")
        ValueAssert.value_assert_equal(sql_qty, int(get_total))

    @allure.feature("AssetsBussinessMgt")  # 模块名称
    class TestAssetsApplication:
        @allure.story("AssetsBussiness_AssetsApplication")  # 场景名称
        @allure.title("AssetsApplication页whetherReturn筛选")  # 用例名称
        @allure.description("对whetherReturn查询")
        @allure.severity("normal")  # 用例等级
        @pytest.mark.parametrize("status, code",
                                 [("Draft", "0"), ("Submitted", "1"), ("In Approval", "2"), ("Approved", "3"), ("Failed", "4")])
        @pytest.mark.smoke  # 用例标记
        def test_001_002(self, drivers, status, code):  # 用例名称取名规范'test+场景编号+用例编号'
            user = AssetsMgtPage(drivers)
            user.Get_search(status, choice="approveStatus")
            user.assets_search()
            user = NavPage(drivers)
            get_total = user.get_total()
            user = SQL("CRM", "test")
            s_ser = user.query_db(
                "SELECT COUNT(*) FROM crm_wms_assets_application aa WHERE aa.approve_status = {} AND aa.is_deleted = 0".format(
                    code))
            sql_qty = s_ser[0].get("COUNT(*)")
            ValueAssert.value_assert_equal(sql_qty, int(get_total))

if __name__ == '__main__':
    pytest.main(['project/CRM/test_case/OperationMgt_PolicyAndProfits_ProfitsTypeMgt.py'])
