import time

import allure
import pytest

from project.SRM.page_object.Approval import ApprovalPage
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

@allure.feature("审批") # 模块名称
class TestApproval:


    @allure.story("审批列表") # 场景名称
    @allure.title("按任务名称搜索")  # 用例名称
    @allure.description("输入任务名称进行搜索")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_enter_approval(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ApprovalPage(drivers)
        user.enter_approval()
        page_title = user.get_page_title()
        assert '审批列表' in page_title, '未进入到审批列表'

    def test_approval_name(self, drivers):
        user = ApprovalPage(drivers)
        user.approval_search_name("周本林")
        name_title = user.get_name_title()
        assert '周本林' in name_title, '搜索结果中没有此主题名数据'



    @allure.story("审批列表")  # 场景名称
    @allure.title("按主题名称搜索")  # 用例名称
    @allure.description("输入主题名称进行搜索")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_approval_task(self,drivers):
        user = ApprovalPage(drivers)
        user.approval_search_task("20220628000011")
        subject_title = user.get_subject_title()
        assert '20220628000011'  in subject_title, '搜索结果中没有此主题数据'


    @allure.story("审批列表")  # 场景名称
    @allure.title("按发起人搜索")  # 用例名称
    @allure.description("输入发起人进行搜索")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_approval_initiator(self, drivers):
        user = ApprovalPage(drivers)
        user.approval_search_initiator("管理员")

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


    #
    # def test_approval_pass(self,drivers):
    #     user = ApprovalPage(drivers)
    #     user.approval_pass()





if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
