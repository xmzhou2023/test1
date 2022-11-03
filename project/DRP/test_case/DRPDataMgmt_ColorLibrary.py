import allure
import pytest

from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.DRPDataMgmt_ColorLibrary import ColorLibrary


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往 DRP数据管理-颜色库 页面")
    user = NavPage(drivers)
    user.click_gotonav("DRP数据管理", "颜色库")
    dom = DomAssert(drivers)
    dom.assert_url("/dataManage/colorLibrary")
    yield
    logging.info("后置条件:关闭 DRP数据管理-颜色库 页面")
    user.close_page()
    dom.assert_url("/dashboard")

@allure.feature("DRP数据管理-颜色库")
class TestSearchColor:
    @allure.story("查询颜色")
    @allure.title("按照颜色条件（颜色名称Zh）过滤颜色库信息")
    @allure.description("输入颜色名称Zh，查询 颜色=123 的颜色库信息")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        color = ColorLibrary(drivers)
        color.input_color("半透黑")
        color.query_button()
        color.screen_assert("颜色名称Zh", "半透黑")
        color.reset_button()

    @allure.story("查询颜色")
    @allure.title("按照颜色条件（颜色名称En）过滤颜色库信息")
    @allure.description("输入颜色名称En，查询 颜色=ABC 的颜色库信息")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        color = ColorLibrary(drivers)
        color.input_color("Aegean Blue")
        color.query_button()
        color.screen_assert("颜色名称En", "Aegean Blue")
        color.reset_button()

    @allure.story("查询颜色")
    @allure.title("按照颜色条件（颜色编码）过滤颜色库信息")
    @allure.description("输入颜色编码，查询 颜色编码=# 的颜色库信息")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_003(self, drivers):
        color = ColorLibrary(drivers)
        color.input_color("#")
        color.query_button()
        color.screen_assert("颜色编码", "#")
        color.reset_button()

    @allure.story("查询可用状态")
    @allure.title("按照可用状态条件过滤颜色库信息")
    @allure.description("选择可用状态 为禁用的颜色库信息")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_004(self, drivers):
        color = ColorLibrary(drivers)
        color.choice_state("禁用")
        color.query_button()
        color.screen_assert("可用状态", "禁用")
        color.reset_button()

    @allure.story("组合查询颜色库（颜色、可用状态）")
    @allure.title("按照可用状态条件过滤颜色库信息")
    @allure.description("选择可用状态 为禁用的颜色库信息")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_005(self, drivers):
        color = ColorLibrary(drivers)
        color.input_color("#")
        color.choice_state("启用")
        color.query_button()
        color.screen_assert("颜色编码", "#")
        color.screen_assert("可用状态", "启用")
        color.reset_button()

    @allure.story("查询条件重置")
    @allure.title("点击重置按钮，查询条件清空，列表数据恢复")
    @allure.description("先通过条件过滤， 点击重置按钮，查询条件清空，列表数据恢复")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_006(self, drivers):
        color = ColorLibrary(drivers)
        color.input_color("#")
        color.choice_state("启用")
        color.query_button()
        beforeNum = color.listnum_assert()
        color.reset_button()
        afterNum = color.listnum_assert()
        ValueAssert.value_assert_Notequal(beforeNum, afterNum)


@allure.feature("DRP数据管理-颜色库")
class TestExportColorLibrary:
    @allure.story("导出Excel")
    @allure.title("点击导出按钮，导出Excel")
    @allure.description("点击导出按钮，导出Excel")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        color = ColorLibrary(drivers)
        color.export_button("drp_color_export")


@allure.feature("DRP数据管理-颜色库")
class TestAppendColor:
    @allure.story("新增颜色库数据")
    @allure.title("点击新增按钮，维护颜色信息 保存")
    @allure.description("点击新增按钮，维护颜色信息 颜色名称Zh=123,颜色名称Eh=ABC,备注=123，保存成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_001(self, drivers):
        color = ColorLibrary(drivers)
        color.append_button()
        color.input_colorinf({"颜色名称Zh": "123","颜色名称En": "ABC","备注": "123"})
        color.save_button()
        color.list_assert("AB", {"2":"ABC","3": "123"})  # 页面列表数据断言
        color.clear_testdata("123", "ABC", "123", "隆江")

    @allure.story("新增颜色库数据")
    @allure.title("[异常]未维护必填项,保存失败")
    @allure.description("点击新增按钮，维护颜色信息 颜色名称Zh=123,不维护颜色名称En，保存失败")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_002(self, drivers):
        color = ColorLibrary(drivers)
        color.reset_button()
        beforlistNum = color.listnum_assert()
        color.append_button()
        color.input_colorinf({"颜色名称Zh": "123"})  # 颜色名称Zh,颜色名称En 为必填项
        color.save_button()
        color.reset_button()
        afterlistNum = color.listnum_assert()
        ValueAssert.value_assert_equal(beforlistNum,afterlistNum)

    @allure.story("新增颜色库数据")
    @allure.title("[异常]输入文本超过32位,保存失败")
    @allure.description("点击新增按钮，维护颜色信息 颜色名称Zh 输入超32位文本，保存失败")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_003(self, drivers):
        color = ColorLibrary(drivers)
        beforlistNum = color.listnum_assert()
        color.append_button()
        num = color.build_testData(33)
        color.input_colorinf({"颜色名称Zh": num})  # 颜色名称Zh 输入超32位字符
        color.save_button()
        color.reset_button()
        afterlistNum = color.listnum_assert()
        ValueAssert.value_assert_equal(beforlistNum,afterlistNum)

    @allure.story("新增颜色库数据")
    @allure.title("[异常]颜色名称En 输入非字符型文本,保存失败")
    @allure.description("点击新增按钮，维护颜色信息 颜色名称En 输入非字符型文本，保存失败")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_004(self, drivers):
        color = ColorLibrary(drivers)
        beforlistNum = color.listnum_assert()
        color.append_button()
        color.input_colorinf({"颜色名称Zh": "abc","颜色名称En": "123"})  # 颜色名称En 输入非字符型文本
        color.save_button()
        color.reset_button()
        afterlistNum = color.listnum_assert()
        ValueAssert.value_assert_equal(beforlistNum,afterlistNum)



@allure.feature("DRP数据管理-颜色库")
class TestEditColor:
    @allure.story("修改颜色库数据")
    @allure.title("点击指定行编辑按钮，修改颜色信息 保存成功")
    @allure.description("点击指定行编辑按钮，修改颜色信息 颜色名称Zh=123->456,颜色名称Eh=ABC->zzz,备注=123->aaa，保存成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_001(self, drivers):
        color = ColorLibrary(drivers)
        color.precondition_addtestdata(drivers)
        color.precondition_selecttestdata("ABC")
        color.edit_button("ABC")
        color.edit_color("ABC",{"颜色名称Zh":"456","颜色名称En":"EFG","备注":"456"})
        color.save_button()
        color.list_assert("456", {"3": "456"})  # 页面列表数据断言
        color.clear_testdata("456", "EFG", "456", "隆江")

    @allure.story("修改颜色库数据")
    @allure.title("[异常]点击指定行编辑按钮，修改颜色信息必填项 为空 保存失败")
    @allure.description("点击指定行编辑按钮，修改颜色信息 颜色名称Zh=123->空,保存失败")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_002(self, drivers):
        color = ColorLibrary(drivers)
        color.precondition_addtestdata(drivers)
        color.precondition_selecttestdata("ABC")
        color.edit_button("ABC")
        color.edit_color("ABC",{"颜色名称Zh":""})
        color.save_button()
        color.clear_testdata("123", "ABC", "123", "隆江")

    @allure.story("修改颜色库数据")
    @allure.title("点击指定行编辑按钮，修改颜色状态为禁用")
    @allure.description("点击指定行编辑按钮，修改颜色由启用 修改为禁用，保存成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_003(self, drivers):
        color = ColorLibrary(drivers)
        color.precondition_addtestdata(drivers)
        color.precondition_selecttestdata("ABC")
        color.edit_state("ABC")
        color.screen_assert("状态","禁用")
        color.clear_testdata("123", "ABC", "123", "隆江")

    @allure.story("修改颜色库数据")
    @allure.title("点击指定行编辑按钮，修改颜色状态由禁用 改为启用")
    @allure.description("点击指定行编辑按钮，修改颜色由禁用 修改为启用，保存成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_004(self, drivers):
        color = ColorLibrary(drivers)
        color.edit_stateStart(drivers)
        color.edit_state("ABC")
        color.precondition_selecttestdata("ABC","启用")
        color.screen_assert("状态","启用")
        color.clear_testdata("123", "ABC", "123", "隆江")
        color.reset_button()



if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/DRPDataMgmt_ColorLibrary.py'])
