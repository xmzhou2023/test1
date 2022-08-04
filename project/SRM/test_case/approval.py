import allure
import pytest

from project.SRM.page_object.approval import ApprovalPage
from project.SRM.page_object.login import LoginPage
from project.SRM.test_case.login import  TestLogin
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
    def test_approval_name(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = ApprovalPage(drivers)
        user.approval_search_name("周本林")


    # def test_approval_task(self,drivers):
    #     user = TestLogin(drivers)
    #     user.test_approval_task("")



    # def test_approval_001(self,drivers):
    #     user = ApprovalPage(drivers)
    #     user.approval_pass()
    #
    # @allure.description("任务名称进行搜素")
    # def test_approval_002(self, drivers):
    #     user = ApprovalPage(drivers)
    #     user.approval_search_name("周本林")






if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
