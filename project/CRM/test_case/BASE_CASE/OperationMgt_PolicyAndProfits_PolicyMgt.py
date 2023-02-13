import allure
import pytest
from project.CRM.page_object.OperationMgt_PolicyAndProfits_ProfitsTypeMgt import *
from project.CRM.page_object.Center_Component import *
from public.base.assert_ui import *
import logging
from project.CRM.page_object.OperationMgt_PolicyAndProfits_WarrantyDurationMgt import *
from project.CRM.page_object.OperationMgt_PolicyAndProfits_PolicyMgt import *

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
    user.click_gotonav("OperationMgt", "PolicyandProfits", "PolicyMgt")  # 点击菜单
    user= DomAssert(drivers)
    user.assert_url("policyAndProfits/policyMgt")
    yield
    logging.info("后置条件：收起菜单")
    user = NavPage(drivers)
    user.click_gotonav("OperationMgt")

@allure.feature("Operation_PolicyMgt") # 模块名称
class TestPolicyMgt:
    @allure.story("PolicyMgt_政策") # 场景名称
    @allure.title("政策页国家和品类筛选")  # 用例名称
    @allure.description("对国家和品类筛选组合查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = PolicyPage(drivers)
        user.search_policy(country="EG",brand="TECNO-SP")
        number = user.get_total()
        user = SQL("CRM", "test")  # 链接数据库
        tatal = user.query_db(
            'SELECT COUNT(*) FROM crm_mdm_policy p WHERE p.country_code LIKE "%EG%" AND p.brand_category_id LIKE "%cb9400ceef01cb7f2be358457d6918e3%" AND p.is_enable = 1')
        sql_tatal = tatal[0].get("COUNT(*)")  # 执行sql后获取返回值的第一个值
        ValueAssert.value_assert_equal(sql_tatal, int(number))  # 校验获取的sql值与获取的total值相等

    @allure.story("PolicyMgt_政策") # 场景名称
    @allure.title("政策页国家筛选")  # 用例名称
    @allure.description("对国家进行查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_002(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = PolicyPage(drivers)
        user.search_policy(country="EG")
        number = user.get_total()
        user = SQL("CRM", "test")  # 链接数据库
        tatal = user.query_db(
                'SELECT COUNT(*) FROM crm_mdm_policy p WHERE p.country_code LIKE "%EG%" AND p.is_enable = 1')
        sql_tatal = tatal[0].get("COUNT(*)")  # 执行sql后获取返回值的第一个值
        ValueAssert.value_assert_equal(sql_tatal, int(number))  # 校验获取的sql值与获取的total值相等

    @allure.story("PolicyMgt_政策") # 场景名称
    @allure.title("政策页国家+品牌+keyword筛选")  # 用例名称
    @allure.description("对国家+品牌+keyword组合进行查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_003(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ProfitsType(drivers)
        keyword_txt = user.get_columnValue()[2]
        user = PolicyPage(drivers)
        user.search_policy(country="EG",brand="TECNO-SP",keyword=keyword_txt)
        number = user.get_total()

        user = SQL("CRM", "test")  # 链接数据库
        tatal = user.query_db(
                'SELECT COUNT(*) FROM crm_mdm_policy p WHERE p.country_code LIKE "%EG%" AND p.brand_category_id LIKE "%cb9400ceef01cb7f2be358457d6918e3%" AND p.is_enable = 1 AND p.policy_no = "{}"'.format(keyword_txt))
        sql_tatal = tatal[0].get("COUNT(*)")  # 执行sql后获取返回值的第一个值
        ValueAssert.value_assert_equal(sql_tatal, int(number))  # 校验获取的sql值与获取的total值相等

    @allure.story("PolicyMgt_政策") # 场景名称
    @allure.title("禁用数据筛选")  # 用例名称
    @allure.description("对禁用数据查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_004(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = PolicyPage(drivers)
        user.search_policy(status="0")
        number = user.get_total()
        user = SQL("CRM", "test")  # 链接数据库
        tatal = user.query_db(
                'SELECT COUNT(*) FROM crm_mdm_policy p WHERE p.is_enable = "0"')
        sql_tatal = tatal[0].get("COUNT(*)")  # 执行sql后获取返回值的第一个值
        ValueAssert.value_assert_equal(sql_tatal, int(number))  # 校验获取的sql值与获取的total值相等

if __name__ == '__main__':
    pytest.main(['project/CRM/test_case/OperationMgt_PolicyAndProfits_ProfitsTypeMgt.py'])
