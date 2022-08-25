import allure
import pytest
from public.base.assert_ui import *
from project.CRM.page_object.Center_Component import NavPage
from project.CRM.page_object.RepairMgt_WoReportMgt_WoNonSerializedReport import *
import pymysql
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""
@pytest.fixture(scope='module',autouse=True)
def module_setup_fixture(drivers):
    logging.info("前置条件:进入非序列化工单报表页")
    user = NavPage(drivers)
    user.click_gotonav("Repair Mgt", "WO Report Mgt", 'WO NonSerialized Report')
    user = DomAssert(drivers)
    user.assert_url("/maintenanceMgt/workOrderReportMgt/woNoSerializedReport")


@allure.feature("Repair Mgt-WO NonSerialized Report")
class TestWoReportSearch:
    @allure.story("查询非序列化报表所有数据") # 场景名称
    @allure.title("查询非序列化报表所有数据 ")  # 用例名称
    @allure.description("时间查询搜索框中的开始时间清除，再点击search，能查到报表数据")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        num = WONonSerializedReport(drivers)
        num.search_NonwoserlistReport(scope=all)
        record = num.search_stock(stock=all)
        ValueAssert.value_assert_equal(record[0], record[1], )


    @allure.story("查询非序列化报表部分数据")  # 场景名称
    @allure.title("根据国家和时间过滤非序列化报表数据")  # 用例名称
    @allure.description("country字段输入SL，from date输入当月1号，查询SL国家当月的非序列化报表数据")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):
        num = WONonSerializedReport(drivers)
        num.search_NonwoserlistReport(scope='part')
        record = num.search_stock(stock='part')
        ValueAssert.value_assert_equal(record[0], record[1], )

@allure.feature("Repair Mgt-WO NonSerialized Report")
class TestWoReportExport:
    @allure.story("非序列化报表导出成功")  # 场景名称
    @allure.title("导出非序列化报表所有数据")  # 用例名称
    @allure.description("查询到非序列化报表所有数据，可导出成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):
        user = WONonSerializedReport(drivers)
        user.download_report(scope=all)


    @allure.story("非序列化报表导出SL国家数据成功")  # 场景名称
    @allure.title("导出非序列化报表中SL国家数据")  # 用例名称
    @allure.description("查询到SL国家的报表数据，可导出成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):
        user = WONonSerializedReport(drivers)
        user.download_report(scope='part')

# if __name__ == '__main__':
#     pytest.main(['project/DRP/testcase/run_code.py'])
