import allure
import pytest
from public.data.unified_login.unified import *
from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.SystemMgmt_UserMgmt import UserPage


@pytest.fixture(scope='module', autouse=True)
def module_setup_fixture(drivers):
    logging.info("模块前置条件：前往 系统管理-用户管理 页面")
    user = NavPage(drivers)
    user.click_gotonav("系统管理", "用户管理")
    dom = DomAssert(drivers)
    dom.assert_url("/systemManage/userManage")
    yield
    logging.info("后置条件:关闭 系统管理-用户管理 页面")
    user.close_page()
    dom.assert_url("/dashboard")

@allure.feature("37自动化管理_259场景管理")
class Test_11908: # Test+(增，删，改，查，导入（上传），导出（下载）)

    @allure.story("录制操作测试")
    @allure.title("根据姓名查询用户")
    @allure.description("在输入框输入用户工号18650617,进行查询")
    @allure.severity("minor")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        user = UserPage(drivers)
        user.search_user(jobnum=account[4]['usernum'])

@allure.feature("37自动化管理_259场景管理")
class Test_11907:
    @allure.story("录制操作可行性调试")
    @allure.title("根据姓名查询用户并添加456")
    @allure.description("查询工号为18650893，并添加该用户到系统")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.skip
    def test_1(self, drivers):
        """用户管理-新建用户"""
        user = UserPage(drivers)
        user.append_account("18649572")

@allure.feature("37自动化管理_259场景管理")
class Test_11904:
    @allure.story("替换需求自测与联调")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_2(self, drivers):
        pass

@allure.feature("37自动化管理_259场景管理")
class Test_11903:
    @allure.story("替换实现")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_3(self, drivers):
        pass

@allure.feature("37自动化管理_259场景管理")
class Test_11902:
    @allure.story("录制操作可用性探索")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_4(self, drivers):
        pass

@allure.feature("37自动化管理_259场景管理")
class Test_11900:
    @allure.story("层级结构对齐自测与联调")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_5(self, drivers):
        pass

@allure.feature("37自动化管理_259场景管理")
class Test_11899:
    @allure.story("界面迭代，需求，用例层级结构顺序对齐脚手架")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_6(self, drivers):
        pass

@allure.feature("37自动化管理_259场景管理")
class Test_11897:
    @allure.story("用例管理迭代需求自测与联调")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_7(self, drivers):
        pass

@allure.feature("37自动化管理_259场景管理")
class Test_11896:
    @allure.story("用例管理迭代需求方案实现")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_8(self, drivers):
        pass

@allure.feature("37自动化管理_259场景管理")
class Test_11893:
    @allure.story("多任务并发自测与联调")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_9(self, drivers):
        pass

@allure.feature("37自动化管理_259场景管理")
class Test_11892:
    @allure.story("多任务并发方案实施")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_10(self, drivers):
        pass

@allure.feature("37自动化管理_259场景管理")
class Test_11906:
    @allure.story("录制操作可行性实践")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_11(self, drivers):
        pass

@allure.feature("37自动化管理_259场景管理")
class Test_11895:
    @allure.story("用例管理迭代需求评审与修改")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_12(self, drivers):
        pass

@allure.feature("37自动化管理_259场景管理")
class Test_11891:
    @allure.story("多任务并发方案评审与修改")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_13(self, drivers):
        pass

@allure.feature("37自动化管理_259场景管理")
class Test_11894:
    @allure.story("用例管理迭代需求CRM试验")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_14(self, drivers):
        pass

@allure.feature("37自动化管理_259场景管理")
class Test_11890:
    @allure.story("多任务并发需求概要设计")
    @allure.title("查找到指定用户并配置菜单权限")
    @allure.description("更新工号为18650893的用户添加组织权限为‘itel事业部’和‘东非地区部‘")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    @pytest.mark.RT
    def test_003_15(self, drivers):
        pass