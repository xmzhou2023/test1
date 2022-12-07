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
    @allure.title("sAssetsCode页firstType筛选")  # 用例名称
    @allure.description("对国家查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.parametrize("Firsttype",
                             ["Repair Tools", "Office Equipment", "Publicity Materials", "Warehouse Materials"])
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers, Firsttype):   # 用例名称取名规范'test+场景编号+用例编号'
        user = AssetsMgtPage(drivers)
        user.firsttype_search(Firsttype)
        user = NavPage(drivers)
        total_assets = user.get_total()
        user = AssetsMgtPage(drivers)
        sql_total = user.SQL_search(Firsttype)
        ValueAssert.value_assert_equal(sql_total, int(total_assets))






if __name__ == '__main__':
    pytest.main(['project/CRM/test_case/OperationMgt_PolicyAndProfits_ProfitsTypeMgt.py'])
