import allure
import pytest

from project.SRM.page_object.login import LoginPage
from project.SRM.page_object.Performance_appraisal import Performance
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("脚本名称") # 模块名称
class TestUtil:
    @allure.story("二级标题") # 场景名称
    @allure.title("三级标题")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_login(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        driver = drivers
        driver.get("http://sitsrm.transsion.com/ELSServer_CY/login/login.html")
        user = LoginPage(drivers)
        user.login("860000", "1001")

    def test_approval_001(self, drivers):
        user = Performance(drivers)
        user.PerformanceAppraisal()

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])