import allure
import pytest
from public.base.assert_ui import *
from project.CRM.page_object.Center_Component import NavPage
from project.CRM.page_object.RepairMgt_WoReportMgt_WoNonSerializedReport import WONonSerializedReport
import pymysql
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""
@pytest.fixture(scope='session',autouse=True)
def goto_center_component(drivers):
    logging.info("前置条件:进入非序列化工单报表页")
    user = NavPage(drivers)
    user.click_gotonav("Repair Mgt", "WO Report Mgt", 'WO NonSerialized Report')
    user = DomAssert(drivers)
    user.assert_url("/maintenanceMgt/workOrderReportMgt/woNoSerializedReport")


@allure.feature("Repair Mgt-WO NonSerialized Report")
class TestWoReportSearch:
    @allure.story("查询非序列化报表") # 场景名称
    @allure.title("查询非序列化报表所有数据 ")  # 用例名称
    @allure.description("时间查询搜索框中的开始时间清除，再点击search，能查到报表数据")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = WONonSerializedReport(drivers)
        user.Stop_date()
        user.clear_date()
        user.search_report()
        num1 = user.get_total()
        num1 = ''.join(filter(str.isdigit, num1))
        # user= WONonSerializedReport(drivers)
        user = SQL('CRM', 'test')
        total_records = user.query_db('SELECT count(*) FROM crm_rc_deserialize_work_order dwo LEFT JOIN crm_rc_deserialize_repair_result drr ON dwo.id = drr.work_order_id AND drr.is_deleted = 0 LEFT JOIN crm_rc_deserialize_repair_result_detail drrd ON drr.id = drrd.result_id AND drrd.is_deleted = 0 WHERE dwo.is_deleted = 0')
        for item in total_records:
            for key in item:
                print(item[key])
        ValueAssert.value_assert_equal(item[key], int(num1))
        user.input_date()
        user.search_report()

    @allure.story("查询非序列化报表")  # 场景名称
    @allure.title("根据国家过滤非序列化报表数据")  # 用例名称
    @allure.description("country字段输入SL，查询SL国家的非序列化报表数据")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):
        user = WONonSerializedReport(drivers)
        user.input_date()
        user.Stop_date()
        user.clear_date()
        user.input_country()
        user.search_report()
        num1 = user.get_total()
        num1 = ''.join(filter(str.isdigit, num1))
        user = SQL('CRM', 'test')
        total_records = user.query_db("SELECT count(*) FROM crm_rc_deserialize_work_order dwo LEFT JOIN crm_rc_deserialize_repair_result drr ON dwo.id = drr.work_order_id AND drr.is_deleted = 0 LEFT JOIN crm_rc_deserialize_repair_result_detail drrd ON drr.id = drrd.result_id AND drrd.is_deleted = 0 WHERE dwo.is_deleted = 0 and warehouse_country_code='SL'")
        for item in total_records:
            for key in item:
                print(item[key])
        ValueAssert.value_assert_equal(item[key], int(num1))
        user.input_country()
        user.search_report()

@allure.feature("Repair Mgt-WO NonSerialized Report")
class TestWoReportExport:
    @allure.story("非序列化报表导出")  # 场景名称
    @allure.title("导出非序列化报表所有数据")  # 用例名称
    @allure.description("查询到非序列化报表所有数据，可导出成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):
        user = WONonSerializedReport(drivers)
        user.input_date()
        user.search_report()
        user.Stop_date()
        user.clear_date()
        user.Stop_country()
        user.clear_country()
        user.input_country()
        user.search_report()
        user.download_report()


    @allure.story("非序列化报表导出SL国家数据")  # 场景名称
    @allure.title("导出非序列化报表中SL国家数据")  # 用例名称
    @allure.description("查询到SL国家的报表数据，可导出成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):

        user = WONonSerializedReport(drivers)
        user.input_date()
        user.search_report()
        user.Stop_date()
        user.clear_date()
        user.search_report()
        user.download_report()

# if __name__ == '__main__':
#     pytest.main(['project/DRP/testcase/run_code.py'])
