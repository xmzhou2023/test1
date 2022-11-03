import allure
import pytest
from project.CRM.page_object.OperationMgt_PolicyAndProfits_ProfitsTypeMgt import *
from project.CRM.page_object.Center_Component import *
from public.base.assert_ui import *
import logging
from project.CRM.page_object.OperationMgt_PolicyAndProfits_WarrantyDurationMgt import *
from project.CRM.page_object.OperationMgt_PolicyAndProfits_PolicyMgt import *
from project.CRM.page_object.OperationMgt_PolicyAndProfits_FGsunking import *
from project.CRM.page_object.OperationMgt_PolicyAndProfits_ProfitsMgt import *

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
    logging.info("模块前置条件，前往operation页面")
    user = NavPage(drivers)
    user.refresh_page()
    user.click_gotonav_CRM("OperationMgt", "PolicyandProfits", "ProfitsMgt")  # 点击菜单
    user= DomAssert(drivers)
    sleep(1)
    user.assert_url("policyAndProfits/profitsMgt")
    yield
    logging.info("后置条件：收起菜单")
    user = NavPage(drivers)
    user.click_gotonav("OperationMgt")


@allure.feature("Operation_ProfitsMgt") # 模块名称
class TestProfits:
    @allure.story("PolicyMgt_Profits") # 场景名称
    @allure.title("profits权益页查询")  # 用例名称
    @allure.description("对keyword+profitsMget进行查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.parametrize("profitstype", ["Accessories  Warranty", "OW Spare Warranty", "DOA", "DAP","Spare Warranty", "Finished Goods Warranty", "Retail Accessories"])
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers, profitstype):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ProfitsPage(drivers)
        user.profits_search(profitstype, keyword="356847092768864")
        user = PolicyPage(drivers)
        total = user.get_total()
        user = SQL("CRM", "test")
        sql_serach = user.query_db('SELECT COUNT(*) FROM crm_mdm_profits pr LEFT JOIN crm_mdm_profits_type ty ON ty.id = pr.profits_type_id WHERE ty.profits_name = "{}" AND pr.unique_code = "356847092768864"'.format(profitstype))
        sql_total = sql_serach[0].get("COUNT(*)")
        ValueAssert.value_assert_equal(sql_total, int(total))







if __name__ == '__main__':
    pytest.main(['project/CRM/test_case/OperationMgt_PolicyAndProfits_ProfitsTypeMgt.py'])
