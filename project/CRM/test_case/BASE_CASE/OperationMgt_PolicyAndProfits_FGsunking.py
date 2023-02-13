import allure
import pytest
from project.CRM.page_object.OperationMgt_PolicyAndProfits_ProfitsTypeMgt import *
from project.CRM.page_object.Center_Component import *
from public.base.assert_ui import *
import logging
from project.CRM.page_object.OperationMgt_PolicyAndProfits_WarrantyDurationMgt import *
from project.CRM.page_object.OperationMgt_PolicyAndProfits_PolicyMgt import *
from project.CRM.page_object.OperationMgt_PolicyAndProfits_FGsunking import *

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
    user.click_gotonav_CRM("OperationMgt", "PolicyandProfits", "FGPolicyForsunking")  # 点击菜单
    user= DomAssert(drivers)
    sleep(1)
    user.assert_url("policyAndProfits/FGPolicyForSunking")
    yield
    logging.info("后置条件：收起菜单")
    user = NavPage(drivers)
    user.click_gotonav("OperationMgt")


@allure.feature("Operation_FGsunking") # 模块名称
class TestFGsunking:
    @allure.story("PolicyMgt_sunking") # 场景名称
    @allure.title("sungking页国家筛选")  # 用例名称
    @allure.description("对国家查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = PolicyPage(drivers)
        user.search_policy(countrycode="SL")
        number = user.get_total()
        sql_qty = user.sql_search(countrycode="SL")
        ValueAssert.value_assert_equal(sql_qty, int(number))  # 校验获取的sql值与获取的total值相等

    @allure.story("PolicyMgt_sunking") # 场景名称
    @allure.title("sungking页禁用数据筛选")  # 用例名称
    @allure.description("对禁用数据查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_002(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = PolicyPage(drivers)
        user.search_policy(status="0")
        number = user.get_total()
        sql_qty = user.sql_search(status="0")
        ValueAssert.value_assert_equal(sql_qty, int(number))  # 校验获取的sql值与获取的total值相等

    @allure.story("PolicyMgt_sunking") # 场景名称
    @allure.title("sungking页country+material条件组合筛选")  # 用例名称
    @allure.description("对country+material条件组合查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_003(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = FGsunking(drivers)
        keyword = user.get_columnValue(choice="4")[2]
        user = PolicyPage(drivers)
        user.search_policy(countrycode="SL", keyword=keyword)
        sleep(2)
        number = user.get_total()
        sql_qty = user.sql_search(keyword=keyword)
        ValueAssert.value_assert_equal(sql_qty, int(number))  # 校验获取的sql值与获取的total值相等

    @allure.story("PolicyMgt_sunking") # 场景名称
    @allure.title("新增重复数据")  # 用例名称
    @allure.description("输入重复的batch数据进行校验")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_004(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = FGsunking(drivers)
        repeatbatch = user.get_columnValue(choice="3")[2]
        user.sunkingadd(batch=repeatbatch, country="EG", code="71", startdate="2019-9-5", enddate="2021-9-11")
        user = DomAssert(drivers)
        user.assert_exact_att("the BatchNo cannot be repeated")
        user = FGsunking(drivers)
        user.click_cancel()

    @allure.story("PolicyMgt_sunking") # 场景名称
    @allure.title("新增异常校验")  # 用例名称
    @allure.description("输入开始日期大于结束日期")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_005(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        number = user.get_Numbersletters()
        user = FGsunking(drivers)
        end = user.get_date()[0]
        user.sunkingadd(batch=number, country="EG", code="71", startdate=end, enddate="2019-9-11")
        user = DomAssert(drivers)
        user.assert_exact_att("Start time is greater than the end time")  # 验证页面上有错误提示
        user = FGsunking(drivers)
        user.click_cancel()

    @allure.story("PolicyMgt_sunking") # 场景名称
    @allure.title("新增正确数据")  # 用例名称
    @allure.description("新增一条正确的数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_006(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        number = user.get_Numbersletters()
        user = FGsunking(drivers)
        user.sunkingadd(batch=number, country="EG", code="71", startdate="2019-9-5", enddate="2021-9-11")
        user = SQL("CRM", "test")  # 链接数据库
        sql = user.query_db('SELECT batch_no FROM crm_mdm_sunking_policy WHERE batch_no = "{}"'.format(number))
        sql_batch = sql[0].get("batch_no")
        ValueAssert.value_assert_equal(sql_batch, number)  # 校验新增数据存在与数据库中
        user = FGsunking(drivers)
        user.disable()
        user = DomAssert(drivers)
        user.assert_exact_att("Disabled Successfully!")


    @allure.story("PolicyMgt_sunking") # 场景名称
    @allure.title("新增batch长度超过限制")  # 用例名称
    @allure.description("新增数据输入batch长度超过限制")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_007(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = FGsunking(drivers)
        number = user.get_Numbersletters()  # 获取11位数的文本
        user.sunkingadd(batch=number, country="EG", code="71", startdate="2019-9-5", enddate="2021-9-11")  # 输入11位文本只取10位
        user = DomAssert(drivers)
        user.assert_exact_att("Success")
        user = FGsunking(drivers)
        user.disable()
        user = DomAssert(drivers)
        user.assert_exact_att("Disabled Successfully!")

    @allure.story("PolicyMgt_sunking") # 场景名称
    @allure.title("编辑sunking数据的BatchNo")  # 用例名称
    @allure.description("新增一条数据后，编辑数据修改BatchNo")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_008(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        number = user.get_Numbersletters()
        user = FGsunking(drivers)
        user.sunkingadd(batch=number,country="EG",code="71",startdate="2019-9-5",enddate="2021-9-11")  # 新增一条数据
        user = SQL("CRM", "test")  # 链接数据库
        sql = user.query_db('SELECT batch_no FROM crm_mdm_sunking_policy WHERE batch_no = "{}"'.format(number))
        sql_batch = sql[0].get("batch_no")
        ValueAssert.value_assert_equal(sql_batch, number)  # 校验新增数据存在与数据库中
        user = OperationPage(drivers)
        numberedit = user.get_Numbersletters()
        user = FGsunking(drivers)
        user.sunkingedit(batch=numberedit, startdate="2019-9-5", enddate="2021-9-11")  # 编辑数据
        user = SQL("CRM", "test")  # 链接数据库
        sql = user.query_db('SELECT batch_no FROM crm_mdm_sunking_policy WHERE batch_no = "{}"'.format(numberedit))
        sql_batch = sql[0].get("batch_no")
        ValueAssert.value_assert_equal(sql_batch, numberedit)  # 校验新增数据存在与数据库中
        user = FGsunking(drivers)
        user.disable()

    @allure.story("PolicyMgt_sunking") # 场景名称
    @allure.title("编辑sunking数据的BatchNo")  # 用例名称
    @allure.description("新增一条数据后，编辑日期开始日期大于结束")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_009(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = OperationPage(drivers)
        number = user.get_Numbersletters()
        user = FGsunking(drivers)
        end = user.get_date()[0]
        logging.info("获取的endedit值是{}".format(end))
        user.sunkingedit(batch=number, startdate=end, enddate="2018-9-11")
        user = DomAssert(drivers)
        user.assert_exact_att("Start time is greater than the end time")  # 验证页面上有错误提示
        user = FGsunking(drivers)
        user.click_cancel()

@allure.feature("Operation_FGsunking") # 模块名称
class TestFGsunking_Download:
    @allure.story("PolicyMgt_sunking_Download") # 场景名称
    @allure.title("sunking数据导出")  # 用例名称
    @allure.description("对所有数据点击导出")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.skip  # 跳过不执行
    def test_002_001(self,drivers):
        user = FGsunking(drivers)
        user.FG_export(country= None)
        user = NavPage(drivers)
        user.click_gotonav("Report Center", "Asynchronous Report Mgt", 'Task List')
        user = DomAssert(drivers)
        user.assert_url("/reportCenter/asReportMgt/taskList")
        user = FGsunking(drivers)
        user.task_download("king", "Sunking_Policy")
        user = NavPage(drivers)
        user.click_gotonav_CRM("OperationMgt", "PolicyandProfits", "FGPolicyForsunking")

    @allure.story("PolicyMgt_sunking_Download") # 场景名称
    @allure.title("sunking数据导出")  # 用例名称
    @allure.description("对指定国家数据点击导出")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.skip  # 跳过不执行
    def test_002_002(self,drivers):
        user = FGsunking(drivers)
        user.FG_export(country="EG")
        user = NavPage(drivers)
        user.click_gotonav("Report Center", "Asynchronous Report Mgt", 'Task List')
        user = DomAssert(drivers)
        user.assert_url("/reportCenter/asReportMgt/taskList")
        user = FGsunking(drivers)
        user.task_download("king", "Sunking_Policy")
        user = NavPage(drivers)
        user.click_gotonav_CRM("OperationMgt", "PolicyandProfits", "FGPolicyForsunking")



if __name__ == '__main__':
    pytest.main(['project/CRM/test_case/OperationMgt_PolicyAndProfits_ProfitsTypeMgt.py'])
