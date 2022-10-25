import time

import allure
import pytest

from project.SRM.page_object.Srm_Approval import ApprovalPage
from public.base.assert_ui import *
from libs.common.connect_sql import *
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""


@pytest.fixture(scope="module", autouse=True)
def approval_module_fixture(drivers):
    user = ApprovalPage(drivers)
    user.enter_approval()
    # page_title = user.get_page_title()
    # assert '审批列表' in page_title, '未进入到审批列表'
    yield
    user = ApprovalPage(drivers)
    user.close_approval()
    print("审批测试结束")

@allure.feature("审批") # 模块名称
class TestApproval:

    @allure.story("审批列表")  # 场景名称
    @allure.title("按任务名称搜索")  # 用例名称
    @allure.description("输入任务名称进行搜索")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_approval_name(self, drivers):
        user = ApprovalPage(drivers)
        user.approval_search_name("采购执行主管")
        sql1 = SQL("SRM", "test")
        sql_val1 = "select count(node_name_) from uflo_task where assignee_ ='860000_1001' and node_name_ ='采购执行主管' "
        result = sql1.query_db(sql_val1)
        # print(type(result))
        # for i in result:
        #     sql_val = i["count(node_name_)"]
        #     print(sql_val)
        # a = result[0]
        # b = a["count(node_name_)"]
        # print(b)
        # search_val = user.serch_value()
        # print(search_val)
        # ValueAssert.value_assert_In(str(b), search_val)
        user.Clear_input()


    @allure.story("审批列表")  # 场景名称
    @allure.title("按主题名称搜索")  # 用例名称
    @allure.description("输入主题名称进行搜索")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_approval_task(self, drivers):
        user = ApprovalPage(drivers)
        user.approval_search_task("20220628000011")
        # subject_title = user.get_subject_title()
        # assert '20220628000011' in subject_title, '搜索结果中没有此主题数据'



    @allure.story("审批列表")  # 场景名称
    @allure.title("按发起人搜索")  # 用例名称
    @allure.description("输入发起人进行搜索")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_approval_initiator(self, drivers):
        user = ApprovalPage(drivers)
        user.approval_search_initiator("管理员")


    @allure.story("审批列表")  # 场景名称
    @allure.title("按主题和任务名称组合搜索")  # 用例名称
    @allure.description("输入发起人，任务名称进行搜索")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_approval_comination(self, drivers):
        user = ApprovalPage(drivers)
        user.combination_search2("GL202203240001", "采购执行主管")


    @allure.story("审批列表")  # 场景名称
    @allure.title("按主题和任务名称组合搜索")  # 用例名称
    @allure.description("输入发起人，任务名称进行搜索")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_approval_comination2(self, drivers):
        user = ApprovalPage(drivers)
        user.combination_search3("GL202203240001", "采购执行主管", "管理员")


    @allure.story("审批列表")  # 场景名称
    @allure.title("审批历史")  # 用例名称
    @allure.description("查看审批历史数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_approval_history(self, drivers):
        user = ApprovalPage(drivers)
        user.approval_history()
        history = user.get_history_title()
        assert '审批历史' in history, '未进入到审批历史界面'
        user.close_history()

    # 10月23日
    @allure.story("审批列表")  # 场景名称
    @allure.title("审批历史--主题查询")  # 用例名称
    @allure.description("审批历史，按照主题查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_history_subject(self, drivers):
        user = ApprovalPage(drivers)
        user.approval_history()
        history = user.get_history_title()
        assert '审批历史' in history, '未进入到审批历史界面'
        user.history_subject("供应商审厂申请")
        user.Clear_input_subject()
        user.close_history()


    @allure.story("审批列表")  # 场景名称
    @allure.title("审批历史--任务查询")  # 用例名称
    @allure.description("审批历史，按照任务名称查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_history_task(self, drivers):
        user = ApprovalPage(drivers)
        user.approval_history()
        user.history_task("开始")
        user.Clear_input_task()
        user.close_history()





    # def test_approval_pass(self,drivers):
    #     user = ApprovalPage(drivers)
    #     user.approval_pass()



if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
