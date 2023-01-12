import allure
import pytest
from public.data.unified_login.unified import *
from public.base.assert_ui import *
from project.TranDesk.page_object.Center_Component import UserPage
from project.TranDesk.page_object.场景管理 import UserPage


@pytest.fixture(scope='module', autouse=True)
def module_setup_fixture(drivers):
    logging.info("模块前置条件：前往 系统管理-用户管理 页面")
    # user = NavPage(drivers)
    # user.click_gotonav("系统管理", "用户管理")
    # dom = DomAssert(drivers)
    # dom.assert_url("/systemManage/userManage")
    yield
    logging.info("后置条件:关闭 系统管理-用户管理 页面")
    # user.close_page()
    # dom.assert_url("/dashboard")

@allure.feature("自动化管理_场景管理")
class Test_4079: # Test+(增，删，改，查，导入（上传），导出（下载）)

    @allure.story("用例管理迭代需求CRM试验")
    @allure.title("TranTest自动化测试用例1")
    @allure.description("1.步骤内容;2.步骤内容;3.步骤内容;")
    @allure.severity("minor")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_28234(self, drivers):
        user = UserPage(drivers)
        # user.search_user(jobnum=account[4]['usernum'])

    @allure.story("用例管理迭代需求CRM试验")
    @allure.title("传测自动化测试用例2")
    @allure.description("1.程序执行步骤一;2.程序执行步骤二;3.程序执行步骤三;")
    @allure.severity("minor")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_28235(self, drivers):
        user = UserPage(drivers)
        # user.search_user(jobnum=account[4]['usernum'])
