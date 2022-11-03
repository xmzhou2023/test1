import allure
import pytest

from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.ProcessManage_ProcessConfig import ProcessConfig


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往 DRP流程管理-流程配置 页面")
    user = NavPage(drivers)
    user.click_gotonav("DRP流程管理", "流程配置")
    dom = DomAssert(drivers)
    dom.assert_url("/processManage/processConfig")
    yield
    logging.info("后置条件:关闭 DRP流程管理-流程配置 页面")
    user.close_page()
    dom.assert_url("/dashboard")

@allure.feature("DRP流程管理-流程配置")
class TestSearchProcess:
    @allure.story("查询流程")
    @allure.title("前往指定事业部")
    @allure.description("前往东非地区部")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        process = ProcessConfig(drivers)
        process.goto_BU("东非地区部")
        # 清空查询条件
        process.reset_button()

    @allure.story("查询流程")
    @allure.title("选择流程名称查询")
    @allure.description("前往 战略客户事业部 选择流程名称 战略客户事业部业务拓展一部审批，查询结果正确")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        process = ProcessConfig(drivers)
        process.goto_BU("战略客户事业部")
        process.choice_process("战略客户事业部业务拓展一部审批")
        process.query_button()
        process.assert_process("战略客户事业部业务拓展一部审批")
        # 清空查询条件
        process.reset_button()

@allure.feature("DRP流程管理-流程配置")
class TestAddProcess:
    @allure.story("新建流程")
    @allure.title("新增流程 成功")
    @allure.description("前往东非地区部，新增流程名称Zh = 测试001，新建成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        process = ProcessConfig(drivers)
        process.goto_BU("东非地区部")
        process.add_button()
        process.input_processZh("测试001","测试001")
        process.input_processEn("测试001","test001")
        process.input_processForm("测试001","itel事业部北非区审批")
        process.input_remark("测试001","xxxxx")
        process.save_button("测试001")
        process.assert_process("测试001")
        # 清空测试数据
        process.postposition(drivers,"测试001")

    @allure.story("新建流程")
    @allure.title("[异常] 新增流程名称Zh为空 新增流程 失败")
    @allure.description("前往东非地区部，新增流程名称Zh 为空，新建失败")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_002(self, drivers):
        process = ProcessConfig(drivers)
        process.goto_BU("东非地区部")
        process.add_button()
        process.input_processEn("测试001","test001")
        process.input_processForm("测试001","itel事业部北非区审批")
        process.input_remark("测试001","xxxxx")
        process.save_button("测试001")

    @allure.story("新建流程")
    @allure.title("[异常] 重复新增流程 失败")
    @allure.description("前往东非地区部，重复新增，新建失败")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_003(self, drivers):
        process = ProcessConfig(drivers)
        process.goto_BU("东非地区部")
        process.add_button()
        process.input_processZh("测试001","测试001")
        process.input_processEn("测试001","test001")
        process.input_processForm("测试001","东非地区部审批")
        process.input_remark("测试001","xxxxx")
        process.save_button("测试001")


@allure.feature("DRP流程管理-流程配置")
class TestEditProcess:
    @allure.story("编辑流程")
    @allure.title("编辑流程 成功")
    @allure.description("前往东非地区部，将流程名称Zh 测试001修改为测试002，编辑失败")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_001(self, drivers):
        process = ProcessConfig(drivers)
        process.preposition(drivers)
        process.edit_button("测试001")
        process.input_processZh("测试001","测试002")
        process.save_button("测试002")
        process.assert_process("测试002")
        # 清空测试数据
        process.postposition(drivers,"测试002")

    @allure.story("编辑流程")
    @allure.title("[异常] 修改流程名称重复 编辑失败")
    @allure.description("前往东非地区部，将流程名称Zh 测试001修改为列表已有的名称，编辑失败")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_002(self, drivers):
        process = ProcessConfig(drivers)
        process.preposition(drivers)
        process.edit_button("测试001")
        process.input_processZh("测试001","TECNO事业部备料审批")
        process.save_button("TECNO事业部备料审批")
        process.assert_process("测试001")
        # 清空测试数据
        process.postposition(drivers,"测试001")

    @allure.story("编辑流程")
    @allure.title("[异常] 修改流程 清空必填项 编辑保存失败")
    @allure.description("前往东非地区部，将流程名称En 清空，编辑保存失败")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_003(self, drivers):
        process = ProcessConfig(drivers)
        process.preposition(drivers)
        process.edit_button("测试001")
        process.input_processEn("测试001","")
        process.save_button("测试001")
        process.assert_process("测试001")
        # 清空测试数据
        process.postposition(drivers,"测试001")


@allure.feature("DRP流程管理-流程配置")
class TestDelProcess:
    @allure.story("删除流程成功")
    @allure.title("选择指定流程 删除成功")
    @allure.description("前往东非地区部，将流程测试001删除，删除成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_001(self, drivers):
        process = ProcessConfig(drivers)
        process.preposition(drivers)
        process.del_button("测试001")
        process.del_assert("测试001")


@allure.feature("DRP流程管理-流程配置")
class TestGotoUrl:
    @allure.story("跳转到 配置管理页面")
    @allure.title("点击 管理 跳转到配置管理页面")
    @allure.description("前往东非地区部，点击 管理 跳转到配置管理页面成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_005_001(self, drivers):
        process = ProcessConfig(drivers)
        process.goto_BU("东非地区部")
        process.configuration_button("东非地区部审批")
        dom = DomAssert(drivers)
        dom.assert_url("1371")
        process.close_page("配置管理")

    @allure.story("跳转到 节点配置页面")
    @allure.title("点击 节点配置 跳转到节点配置页面")
    @allure.description("前往东非地区部，点击 节点配置 跳转到节点配置页面成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_005_002(self, drivers):
        process = ProcessConfig(drivers)
        process.goto_BU("东非地区部")
        process.nodeDeployment_button("东非地区部审批")
        dom = DomAssert(drivers)
        dom.assert_url("1371")
        process.close_page("节点配置")


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/ProcessManage_ProcessConfig.py'])
