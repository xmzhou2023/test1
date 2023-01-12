import allure
import pytest

from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.SystemMgmt_DimensionManage import DimensionManage


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往 系统管理-维度管理 页面")
    user = NavPage(drivers)
    user.click_gotonav("系统管理", "维度管理")
    dom = DomAssert(drivers)
    dom.assert_url("/systemManage/dimensionManage")
    yield
    logging.info("后置条件:关闭 系统管理-维度管理 页面")
    user.close_page()
    dom.assert_url("/dashboard")


@allure.feature("系统管理-维度管理")
class TestGotoLabelPage:
    @allure.story("前往维度标签页")
    @allure.title("分别点击维度名称，进入对应标签页")
    @allure.description("分别点击维度名称，进入对应标签页成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.parametrize("labelPage",
                             ["管理维度", "市场分类", "国家", "数据版本", "市场划分", "大区", "组织", "阶段", "地区", "事业部", "部门", "品牌"])
    @pytest.mark.skip
    def test_001_001(self, drivers, labelPage):
        dimension = DimensionManage(drivers)
        dimension.goto_labelPage(labelPage)


@allure.feature("系统管理-维度管理")
class TestAddDimension:
    @allure.story("新增维度信息")
    @allure.title("进入 大区标签页，新增维度信息成功")
    @allure.description("进入 大区标签页，新增维度信息 编码=test001，名称zh=测试001，名称en=test001，新增成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.skip
    def test_002_001(self, drivers):
        dimension = DimensionManage(drivers)
        dimension.goto_labelPage("大区")
        dimension.add_button()
        dimension.input_testdata("test001", "测试001", "test001")
        dimension.save_button()
        dimension.query_value("测试001")
        dimension.assert_sql("事业部", "测试001")
        dimension.clear_testdata("事业部", "测试001")

    @allure.story("新增维度信息")
    @allure.title("[异常] 有必填项未维护，新增失败")
    @allure.description("进入 大区标签页，有必填项未维护，新增失败")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.parametrize("coding,name_zh,name_en",
                             [("test001", "", ""), ("test001", "测试001", ""), ("test001", "", "test001"),
                              ("", "测试001", ""), ("", "测试001", "test001"), ("", "", "test001"), ("", "", "")])
    @pytest.mark.skip
    def test_002_002(self, drivers, coding, name_zh, name_en):
        dimension = DimensionManage(drivers)
        dimension.goto_labelPage("大区")
        dimension.add_button()
        dimension.input_testdata(coding, name_zh, name_en)
        dimension.save_button()
        dimension.assert_sql("大区", name_zh, "反例")


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/SystemManage_DimensionManage.py'])
