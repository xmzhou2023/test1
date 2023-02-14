import allure
import pytest
from project.CRM.page_object.RC_JSMgt_JSList import JSPage
from project.CRM.page_object.RC_JSMgt_AssignTechnician import AssignPage
from public.base.assert_ui import ValueAssert
import random, string
import pytest, logging
from public.base.basics import *
from public.base.assert_ui import *
from public.data.unified_login.unified import *
from project.CRM.page_object.Center_Component import NavPage
from public.libs.unified_login.login import Login
from libs.common.read_config import *
from public.base.assert_ui import *
from datetime import *
from datetime import timedelta
import math
pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import logging
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""
num = string.ascii_letters + string.digits
digit_no = string.digits
@pytest.fixture(scope='module',autouse=True)
def module_fixture(drivers):
    logging.info("前往RC中的JS Mgt的JS List")
    user = JSPage(drivers)
    user.Clear_Get()
    user = NavPage(drivers)
    user.list_search(content='JS List')
    result = DomAssert(drivers)
    result.assert_url("/repairCenter/jobSheetMgt/jobSheetList")
    name = "".join(random.sample(num, 10))  # 名称使用随机数，以防重复名称添加失败
    user = SQL('CRM', 'test')
    user.query_db(
        'delete  from crm_rc_job_sheet where imei_sn_1="{}"'.format("359051721987485"))
    user = JSPage(drivers)
    mobile_no = "".join(random.sample(digit_no, 9))  # 电话号码使用随机数
    name = "".join(random.sample(num, 4))  # 名称使用随机数，以防重复名称
    user.Add_JS_Basic_Info("Carry In", "359051721987485", "Fair", "250001", "122701-显示屏")  # 添加工单的基本信息
    user.Add_JS_Customer_Info("End User", name, "Andorra", "+376", mobile_no)  # 添加工单的客户信息
    user.Add_JS_Change_Tab("Quote")
    user.Qte_20_Status(material="1227", qty="1", symptom="12278201", fault="12278202")  # 填写各项报价信息
    user.Save_JS()  # 在前置条件中添加一个工单
    user.Swith_Original_Window()  # 回到工单页面
    user.Get_Exact_Word_JS("359051721987485")
    imei, customer_name, js_no, warranty_status = user.Get_New_JS()
    yield js_no
    logging.info("\n在当前模块完成后执行的teardown")
    user = NavPage(drivers)
    user.list_search(content='JS List')
    user = JSPage(drivers)
    user.Get_Exact_Word_JS("359051721987485")
    imei, customer_name, js_no, warranty_status = user.Get_New_JS()
    user = SQL('CRM', 'test')
    sql_get = user.query_db('select id from crm_rc_job_sheet where job_sheet_no="{}"'.format(js_no))
    sql_get_id = sql_get[0].get("id")
    user.query_db('delete from crm_rc_assign_technician WHERE document_id="{}"'.format(sql_get_id))  # 删除指派技术员表里数据
    user.query_db(
        'delete  from crm_rc_job_sheet where job_sheet_no="{}"'.format(js_no))  # 删除JS 工单，恢复环境
    user.query_db(
        'delete  from crm_rc_job_sheet_customer where customer_name="{}"'.format(customer_name))  # 删除js客户，恢复环境
    user = AssignPage(drivers)
    user.Close_Page()  # 关闭页面
    user.Clear_Get()  # 刷新页面

@allure.feature("AssignTechincian")  # 模块名称
class TestAssignTechincian:
    @pytest.fixture()
    def class_fixture(self, drivers):
        logging.info("\n这个fixture在每个case前执行一次")
        user = AssignPage(drivers)
        user.Close_Page()  # 关闭页面
        user.Clear_Get()  # 刷新页面
        user = NavPage(drivers)
        user.list_search(content='Assign Technician Mgt')
        result = DomAssert(drivers)
        result.assert_url("/repairCenter/jobSheetMgt/assignTechnicianMgt")  #进入派料页面
        yield
        logging.info("\n在每个case完成后执行的teardown")
        user = AssignPage(drivers)
        user.Clear_Get()  # 恢复查询默认条件


    @allure.story("工单指派技术员")  # 场景名称,中文
    @allure.title("对JS工单指派技术员后，工单状态变为20")  # 用例名称
    @allure.description("对JS工单指派技术员后，工单状态变为20")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
   # @pytest.mark.skip  # 跳过不执行
    def test_27432(self, drivers, module_fixture, class_fixture):  # 用例名称取名规范'test+场景编号+用例编号'
        js_no = module_fixture.js_no
        user = AssignPage(drivers)
        user.Get_Exact_Word_JS(js_no)
        user.Assign_Select_JS(account="18645342")  # 指派技术员
        user.Close_Page()  # 关闭页面
        user.Clear_Get()  # 刷新页面
        user = NavPage(drivers)
        user.list_search(content='JS List')
        user = AssignPage(drivers)
        user.Get_Exact_Word_JS(js_no)
        document_status, serivice_type = user.Get_JS_Status_Type()
        ValueAssert.value_assert_equal(document_status, "20-Assigned To Technician")  # 判断搜索出来的工单状态为20



    @allure.story("工单指派技术员")  # 场景名称,中文
    @allure.title("工单指派技术员页面使用保修状态查询工单")  # 用例名称
    @allure.description("工单指派技术员页面，遍历Warranty Status下拉框查询正确")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("query_status,sql_status", [("Under Warranty", "underWarranty"), ("Out Warranty","outWarranty")])
    @pytest.mark.smoke  # 用例标记
    #@pytest.mark.skip  # 跳过不执行
    def test_4481(self, drivers, class_fixture, query_status, sql_status):  # 用例名称取名规范'test+场景编号+用例编号'
        user = AssignPage(drivers)
        number, th_num, list1 = user.Get_Warranty_JS(query_status)  # 查询成功
        for i in range(0, th_num):
            ValueAssert.value_assert_equal(query_status, list1[i])  # 判断查询出来的 JS与输入条件一致

    @allure.story("工单指派技术员")  # 场景名称,中文
    @allure.title("工单指派技术员页面，遍历Service Type下拉框查询正确")  # 用例名称
    @allure.description("工单指派技术员页面，遍历Service Type下拉框查询正确")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("status", ["Normal", "RWR", "DAP", "OTSR SWAP", "M-SWAP", "SAMPLE", "EOS", "DOA", "SWAP"]) # DOA、SWAP需要单独判断
    @pytest.mark.smoke  # 用例标记
   # @pytest.mark.skip  # 跳过不执行
    def test_10140(self, drivers, class_fixture, status):   # 用例名称取名规范'test+场景编号+用例编号'
        user = AssignPage(drivers)
        get_record = user.Get_Service_Status_JS(status)  # 查询成功
        # user = SQL('CRM', 'test')
        # js_data = user.query_db('select count(service_type) from crm_rc_job_sheet where service_type="{}"'.format(status))
        # sql_get_data = js_data[0].get("count(service_type)")
        # sql_get = int(sql_get_data)
        # logging.info(type(get_record))
        # logging.info(type(sql_get))
        # ValueAssert.value_assert_equal(sql_get, get_record)  # 判断查询出的数据量与数据库一致

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
