import allure
import pytest
from project.DRP.page_object.Center_Component import NavPage
from project.CRM.page_object.RC_JSMgt_JSList import JSPage
from public.base.assert_ui import ValueAssert
import random, string
import pytest, logging
from public.base.basics import *
from public.base.assert_ui import *
from public.data.unified_login.unified import *
from project.CRM.page_object.Center_Component import NavPage
from public.libs.unified_login.login import Login
from libs.common.read_config import *
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
    #user = JSPage(drivers)
    #user.GoTo_JS_List()  # 进入JS页面
    result = DomAssert(drivers)
    result.assert_url("/repairCenter/jobSheetMgt/jobSheetList")
    name = "".join(random.sample(num, 10))  # 名称使用随机数，以防重复名称添加失败
    yield name
    logging.info("\n在当前模块完成后执行的teardown")
    user = JSPage(drivers)
    user.Close_Page()  # 关闭页面
    #user.Close_Up_First_Menu("Repair Center")  # 合起菜单




@allure.feature("JSList_pro") # 模块名称
class TestGetJSList:
    @pytest.fixture()
    def class_fixture(self, drivers):
        logging.info("\n这个fixture在每个case前执行一次")
        yield
        logging.info("\n在每个case完成后执行的teardown")
        user = JSPage(drivers)
        user.Clear_Get()  # 恢复查询默认条件

    @allure.story("查询工单")  # 场景名称,中文
    @allure.title("查询工单")  # 用例名称
    @allure.description("JS页面，列表各个字段名称正确")
    @allure.severity("critical")  # 用例等级
   # @pytest.mark.skip  # 跳过不执行

    def test_1750(self, drivers, class_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        user = JSPage(drivers)
        user.Get_List_Header()
        th_num, list_data = user.Get_List_Header()  # 查询成功
        logging.info(th_num)
        logging.info(list_data)
        list_expect_data1 = ['Seq', 'Operate', 'JS No.', 'Document Status', 'Shortage Status', 'Material Code', 'Model', 'Service Type', 'Warranty Status']
       # list_expect_data2 = ['IsEscalate', 'Escalate Status', 'Escalate To','Customer Name', 'Mobile No.', 'Phone No.', 'Country', 'IMEI/SN 1', 'IMEI/SN 2', 'Is Quick Repair', 'Created By', 'Created Date', 'Return On']
        ValueAssert.value_assert_equal(th_num, 22)
        for i in range(0, 9):
            ValueAssert.value_assert_equal(list_data[i], list_expect_data1[i])

        # for j in range(9, 22):
        #     ValueAssert.value_assert_equal(list_data[j], list_expect_data2[j])

    @allure.story("查询工单")  # 场景名称,中文
    @allure.title("查询工单")  # 用例名称
    @allure.description("JS页面，使用工单号精确查询成功")
    @allure.severity("critical")  # 用例等级
    # @pytest.mark.skip  # 跳过不执行

    def test_7958(self, drivers, class_fixture):  # 用例名称取名规范'test+场景编号+用例编号'
        user = JSPage(drivers)
        no = "".join(random.sample(digit_no, 1))  # 使用随机数
        user.JS_Clear_Query_Conditions()
        js_no = user.Get_JS_No(no)
        get_js_no = user.Get_Exact_Word_JS(js_no)
        ValueAssert.value_assert_equal(get_js_no, js_no)  # 判断查出来的js_no与输入的一致
        # user = SQL('CRM', 'test')
        # js_data = user.query_db(
        #     'select job_sheet_no from crm_rc_job_sheet where job_sheet_no="{}"'.format(get_js_no))
        # sql_get_data = js_data[0].get("job_sheet_no")
        # ValueAssert.value_assert_equal(sql_get_data, get_js_no)  # 判断查询出来的js与数据库一致







    @allure.story("查询工单")  # 场景名称,中文
    @allure.title("查询工单")  # 用例名称
    @allure.description("JS页面，遍历Document Status下拉框查询正确")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("status", ["5-Draft", "10-Open", "20-Assigned To Technician", "30-SWAP","35-SWAP Approved", "36-SWAP DisApproved", "40-Checked for SWAP", "45-SWAPPED", "90-Repair Completed", "95-Non Repairable","96-Re-open", "100-Returned", "110-DOA Certificate"])
    @pytest.mark.smoke  # 用例标记
   # @pytest.mark.skip  # 跳过不执行
    def test_1750(self, drivers, class_fixture, status):   # 用例名称取名规范'test+场景编号+用例编号'
        user = JSPage(drivers)
        user.JS_Clear_Query_Conditions()
        get_record = user.Get_Document_Status_JS(status)  # 查询成功
        num = status.split("-", 2)
        logging.info(num[0])
        # user = SQL('CRM', 'test')
        # js_data = user.query_db('select count(status_code) from crm_rc_job_sheet where status_code="{}"'.format(num[0]))
        # sql_get_data = js_data[0].get("count(status_code)")
        # sql_get = str(sql_get_data)
        # logging.info(type(get_record))
        # logging.info(type(sql_get))
        # ValueAssert.value_assert_equal(sql_get, get_record)  # 判断查询出的数据量与数据库一致

    @allure.story("查询工单")  # 场景名称,中文
    @allure.title("查询工单")  # 用例名称
    @allure.description("JS页面，遍历Shortage Status下拉框查询正确")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("status", ["10-Awaiting For Parts", "15-Disapprovaled For Parts", "20-Awaiting for Parts/Processed", "21-Doing", "30-Awaiting for Parts/In transit", "40-Part Available"])
    @pytest.mark.smoke  # 用例标记
   # @pytest.mark.skip  # 跳过不执行
    def test_2395(self, drivers, class_fixture, status):   # 用例名称取名规范'test+场景编号+用例编号'
        user = JSPage(drivers)
        user.JS_Clear_Query_Conditions()
        get_record = user.Get_Shortage_Status_JS(status)  # 查询成功
        num = status.split("-", 2)
        logging.info(num[0])
        # user = SQL('CRM', 'test')
        # js_data = user.query_db('select count(shortage_status) from crm_rc_job_sheet where shortage_status="{}"'.format(num[0]))
        # sql_get_data = js_data[0].get("count(shortage_status)")
        # sql_get = str(sql_get_data)
        # logging.info(type(get_record))
        # logging.info(type(sql_get))
        # ValueAssert.value_assert_equal(sql_get, get_record)  # 判断查询出的数据量与数据库一致

    @allure.story("查询工单")  # 场景名称,中文
    @allure.title("查询工单")  # 用例名称
    @allure.description("JS页面，遍历Service Type下拉框查询正确")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("status", ["Normal", "RWR", "DAP", "OTSR SWAP", "M-SWAP", "SAMPLE", "EOS"])  # DOA、SWAP需要单独判断
    @pytest.mark.smoke  # 用例标记
    # @pytest.mark.skip  # 跳过不执行
    def test_2395(self, drivers, class_fixture, status):   # 用例名称取名规范'test+场景编号+用例编号'
        user = JSPage(drivers)
        user.JS_Clear_Query_Conditions()
        get_record = user.Get_Service_Status_JS(status)  # 查询成功
        # user = SQL('CRM', 'test')
        # js_data = user.query_db('select count(service_type) from crm_rc_job_sheet where service_type="{}"'.format(status))
        # sql_get_data = js_data[0].get("count(service_type)")
        # sql_get = str(sql_get_data)
        # logging.info(type(get_record))
        # logging.info(type(sql_get))
        # ValueAssert.value_assert_equal(sql_get, get_record)  # 判断查询出的数据量与数据库一致

    @allure.story("查询工单")  # 场景名称,中文
    @allure.title("查询工单")  # 用例名称
    @allure.description("JS页面，遍历Quote Status下拉框查询正确")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("status", ["10-Estimation Approval Pending", "15-Estimation Disapproved", "20-Estimation Approved"])
    @pytest.mark.smoke  # 用例标记
  #  @pytest.mark.skip  # 跳过不执行
    def test_2396(self, drivers, class_fixture, status):   # 用例名称取名规范'test+场景编号+用例编号'
        user = JSPage(drivers)
        user.JS_Clear_Query_Conditions()
        get_record = user.Get_Quote_Status_JS(status)  # 查询成功
        num = status.split("-", 2)
        logging.info(num[0])  # 查询出来跟数据库有差异，不适用数据库比较,页面列表也无字段可查看

    @allure.story("查询工单")  # 场景名称,中文
    @allure.title("查询工单")  # 用例名称
    @allure.description("JS页面，Scope下拉框查询正确")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
 #   @pytest.mark.skip  # 跳过不执行
    def test_3319(self, drivers, class_fixture):   # 用例名称取名规范'test+场景编号+用例编号'
        user = JSPage(drivers)
        logging.info("使用Scope中的下拉框Mine查询")
        user.JS_Clear_Query_Conditions()  # 清空其他查询条件
        number, th_num, list1 = user.Get_Scope_JS("Scope", "Mine")  # 查询成功
        # user = SQL('CRM', 'test')
        # js_data = user.query_db('select count(creator) from crm_rc_job_sheet where creator="{}"'.format(account[7]['usernum']))
        # sql_get_data = js_data[0].get("count(creator)")
        # sql_get = str(sql_get_data)
        # ValueAssert.value_assert_equal(sql_get, number)  # 判断查询出的数据量与数据库一致
        # for i in range(0, th_num):
        #     ValueAssert.value_assert_equal(list1[i], account[7]['username'])  # 判断查询出来的JS为登录用户创建的工单

    @allure.story("查询工单")  # 场景名称,中文
    @allure.title("查询工单")  # 用例名称
    @allure.description("JS页面，IsEscatale下拉框查询正确")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("query_status,sql_status", [("Yes", "1"), ("No", "0")])
    @pytest.mark.smoke  # 用例标记
  #  @pytest.mark.skip  # 跳过不执行
    def test_3320(self, drivers, class_fixture, query_status, sql_status):   # 用例名称取名规范'test+场景编号+用例编号'
        user = JSPage(drivers)
        logging.info("步骤1 使用IsEscatale中的下拉框Yes查询")
        user.JS_Clear_Query_Conditions()  # 清空其他查询条件
        number, th_num, list1 = user.Get_IsEcalate_JS(query_status)  # 查询成功
        # user = SQL('CRM', 'test')
        # js_data = user.query_db('select count(is_escalate) from crm_rc_job_sheet where is_escalate="{}"'.format(sql_status))
        # sql_get_data = js_data[0].get("count(is_escalate)")
        # sql_get = str(sql_get_data)
        # ValueAssert.value_assert_equal(sql_get, number)  # 判断查询出的数据量与数据库一致
        for i in range(0, th_num):
            ValueAssert.value_assert_equal(list1[i], query_status)  #判断查询出来的 JS与输入条件一致

    @allure.story("查询工单")  # 场景名称,中文
    @allure.title("查询工单")  # 用例名称
    @allure.description("JS页面，IsQuickRepair下拉框查询正确")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("query_status,sql_status", [("Yes", "1"), ("No", "0")])
    @pytest.mark.smoke  # 用例标记
  #  @pytest.mark.skip  # 跳过不执行
    def test_3321(self, drivers, class_fixture, query_status, sql_status):   # 用例名称取名规范'test+场景编号+用例编号'
        user = JSPage(drivers)
        user.JS_Clear_Query_Conditions()  # 清空其他查询条件
        number, th_num, list1 = user.Get_IsQuickRepair_JS(query_status)  # 查询成功
        # user = SQL('CRM', 'test')
        # js_data = user.query_db('select count(is_quick_repair) from crm_rc_job_sheet where is_quick_repair="{}"'.format(sql_status))
        # sql_get_data = js_data[0].get("count(is_quick_repair)")
        # sql_get = str(sql_get_data)
        # ValueAssert.value_assert_equal(sql_get, number)  # 判断查询出的数据量与数据库一致
        for i in range(0, th_num):
            ValueAssert.value_assert_equal(list1[i], query_status)  # 判断查询出来的 JS与输入条件一致


    @allure.story("查询工单")  # 场景名称,中文
    @allure.title("查询工单")  # 用例名称
    @allure.description("JS页面，遍历Warranty Status下拉框查询正确")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("query_status,sql_status", [("Under Warranty", "underWarranty"), ("Out Warranty","outWarranty")])
    @pytest.mark.smoke  # 用例标记
   # @pytest.mark.skip  # 跳过不执行
    def test_4481(self, drivers, class_fixture, query_status, sql_status):  # 用例名称取名规范'test+场景编号+用例编号'
            user = JSPage(drivers)
            user.JS_Clear_Query_Conditions()
            number, th_num, list1 = user.Get_Warranty_JS(query_status)  # 查询成功
            # user = SQL('CRM', 'test')
            # js_data = user.query_db(
            #     'select count(warranty_status) from crm_rc_job_sheet where warranty_status="{}"'.format(sql_status))
            # logging.info(query_status)
            # sql_get_data = js_data[0].get("count(warranty_status)")
            # sql_get = str(sql_get_data)
            # logging.info(sql_get)
            # ValueAssert.value_assert_equal(sql_get, number)  # 判断查询出的数据量与数据库一致
            for i in range(0, th_num):
                ValueAssert.value_assert_equal(query_status, list1[i])  #


# @allure.feature("JSList")  # 模块名称
# class TestAddJSList:
#     @pytest.fixture()
#     def class_fixture(self, drivers):
#         logging.info("\n这个fixture在每个case前执行一次")
#         yield
#         logging.info("\n在每个case完成后执行的teardown")
#         user = JSPage(drivers)
#         user.Clear_Get()  # 恢复查询默认条件
#
#     @allure.story("新增工单")  # 场景名称,中文
#     @allure.title("新增工单")  # 用例名称
#     @allure.description("JS页面，新增保内工单")
#     @allure.severity("critical")  # 用例等级
#     @pytest.mark.smoke  # 用例标记
#    # @pytest.mark.skip  # 跳过不执行
#     def test_7932(self, drivers, class_fixture):  # 用例名称取名规范'test+场景编号+用例编号'
#         user = JSPage(drivers)
#         mobile_no = "".join(random.sample(digit_no, 9))  # 电话号码使用随机数
#         name = "".join(random.sample(num, 4))  # 名称使用随机数，以防重复名称
#         user.Add_JS_Basic_Info("Carry In", "359051721987485", "Fair", "250001", "122701-显示屏")  # 添加工单的基本信息
#         user.Add_JS_Customer_Info("End User", name, "Andorra", "+376", mobile_no)        # 添加工单的客户信息
#         user.Save_JS()  # 保存工单
#         user.Swith_Original_Window()  # 回到工单页面
#         user.Search_JS()  # 搜索工单
#         imei, customer_name, js_no, warranty_status = user.Get_New_JS()
#         ValueAssert.value_assert_equal(imei, "359051721987485")  # 判断搜索出来的工单IEMI与添加输入的一致
#         ValueAssert.value_assert_equal(customer_name, name)  # 判断搜索出来的工单客户名与添加输入的一致
#         ValueAssert.value_assert_equal(warranty_status, "Under Warranty")  # 判断搜索出来的工单为保内
#         user = SQL('CRM', 'test')
#         js_data = user.query_db(
#             'select job_sheet_no from crm_rc_job_sheet where job_sheet_no="{}"'.format(js_no))
#         sql_get_data = js_data[0].get("job_sheet_no")
#         ValueAssert.value_assert_equal(sql_get_data, js_no)  # 判断数据库搜索出的js no与页面的一致
#         user.query_db(
#             'delete  from crm_rc_job_sheet where job_sheet_no="{}"'.format(js_no))  # 删除JS 工单，恢复环境
#         user.query_db(
#             'delete  from crm_rc_job_sheet_customer where customer_name="{}"'.format(customer_name))  # 删除js客户，恢复环境
#
#


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
