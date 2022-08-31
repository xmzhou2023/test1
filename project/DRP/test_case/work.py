import allure
import pytest
from public.base.assert_ui import *
from project.zztest.page_object.Center_Component import NavPage
from project.zztest.page_object.work import jieru

@allure.feature("系统管理-区域管理")
class Test001:

    @allure.story("查询区域")
    @allure.title("表头itel事业部")
    @allure.description("点击‘itel事业部’表头itel事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = jieru(drivers)
        user.goto_tree('itel事业部')

    @allure.story("查询区域")
    @allure.title("前往一级区域")
    @allure.description("点击‘itel事业部’一级itel事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = jieru(drivers)
        user.goto_tree('itel事业部')

    @pytest.mark.RT
    @allure.story("查询区域")
    @allure.title("前往二级区域")
    @allure.description("点击‘itel事业部’二级itel事业部")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = jieru(drivers)
        user.goto_tree('itel事业部', 'itel事业部')

    @allure.story("查询区域")
    @allure.title("前往三级区域")
    @allure.description("点击‘itel事业部’三级itel事业部")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = jieru(drivers)
        user.goto_tree('itel事业部', 'itel事业部', 'itel事业部')

    @allure.story("查询区域")
    @allure.title("前往四级区域")
    @allure.description("点击‘事业部备料’四级itel事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_005(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = jieru(drivers)
        user.goto_tree('itel事业部', 'itel事业部', 'itel事业部', '事业部备料')


if __name__ == '__main__':
    pytest.main(['project/zztest/test_case/work.py'])