import allure
import pytest
from project.CRM.page_object.OperationMgt_PolicyAndProfits_ProfitsTypeMgt import *
from project.CRM.page_object.Center_Component import *
from public.base.assert_ui import *
import logging
from project.CRM.page_object.AssetsMgt_AssetsBasicInfoMgt_AssetsCodeMgt import *


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
    user.click_gotonav_CRM("AssetsMgt", "AssetsBasicInfoMgt", "AssetsCodeMgt")  # 点击菜单
    user= DomAssert(drivers)
    sleep(1)
    user.assert_url("assetsMgt/assetsBasicInfoMgt/assetsCodeMgt")
    yield
    logging.info("后置条件：收起菜单")
    user = NavPage(drivers)
    user.click_gotonav("AssetsMgt")


@allure.feature("AssetsBasicInfoMgt") # 模块名称
class TestAssetsCode:
    @allure.story("AssetsBasicInfoMgt_AssetsCode") # 场景名称
    @allure.title("AssetsCode页firstType筛选")  # 用例名称
    @allure.description("对国家查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.parametrize("status, FT",
                             [("Repair Tools", "FT002"), ("Office Equipment", "FT001"), ("Publicity Materials", "FT003"), ("Warehouse Materials", "FT004")])
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers, status, FT):   # 用例名称取名规范'test+场景编号+用例编号'
        user = AssetsMgtPage(drivers)
        user.Get_search(status, choice="firstType")
        user = NavPage(drivers)
        total_assets = user.get_total()
        user = SQL("CRM", "test")
        s_ser = user.query_db('SELECT COUNT(*) FROM crm_wms_assets_code_application WHERE first_type = "{}"'.format(FT))
        sql_total = s_ser[0].get("COUNT(*)")
        ValueAssert.value_assert_equal(sql_total, int(total_assets))

    @allure.story("AssetsBasicInfoMgt_AssetsCode") # 场景名称
    @allure.title("AssetsCode页approved status筛选")  # 用例名称
    @allure.description("对国家查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.parametrize("status, code",
                             [("Draft", 0), ("Submitted", 1), ("In Approval", 2), ("Approved", 3), ("Failed", 4)])
    @pytest.mark.smoke # 用例标记
    def test_001_002(self, drivers, status, code):   # 用例名称取名规范'test+场景编号+用例编号'
        user = AssetsMgtPage(drivers)
        user.Get_search(status, choice="approveStatus")
        user = NavPage(drivers)
        get_total = user.get_total()
        user = SQL("CRM", "test")
        s_ser = user.query_db('SELECT COUNT(*) FROM crm_wms_assets_code_application WHERE approve_status = "{}" AND is_deleted = 0'.format(code))
        logging.info("获取到sql数据：".format(s_ser))
        sql_qty = s_ser[0].get("COUNT(*)")
        ValueAssert.value_assert_equal(sql_qty, int(get_total))





if __name__ == '__main__':
    pytest.main(['project/CRM/test_case/OperationMgt_PolicyAndProfits_ProfitsTypeMgt.py'])
