import allure
import pytest

from project.TLC.page_object.ShowSwitch import ShowSwitch
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("组件中心-图标列表切换") # 模块名称
class TestShowSwitch:
    @allure.story("图标列表切换") # 场景名称
    @allure.title("我的文件-图标列表切换")  # 用例名称
    @allure.description("我的文件页面操作图标列表切换")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        tools = ShowSwitch(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.click('图标列表切换按钮')
        DomAssert(drivers).assert_att('所有者')
        tools.click('图标列表切换按钮')
        DomAssert(drivers).assert_page_source('所有者')
        pass

    @allure.story("图标列表切换")  # 场景名称
    @allure.title("我的收藏-图标列表切换")  # 用例名称
    @allure.description("我的收藏页面操作图标列表切换")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = ShowSwitch(drivers)
        tools.click_menu('组件中心', '我的收藏')
        tools.click('图标列表切换按钮')
        DomAssert(drivers).assert_att('所有者')
        tools.click('图标列表切换按钮')
        DomAssert(drivers).assert_page_source('所有者')
        pass

    @allure.story("图标列表切换")  # 场景名称
    @allure.title("回收站-图标列表切换")  # 用例名称
    @allure.description("回收站页面操作图标列表切换")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = ShowSwitch(drivers)
        tools.click_menu('组件中心', '回收站')
        tools.click('图标列表切换按钮')
        DomAssert(drivers).assert_att('所有者')
        tools.click('图标列表切换按钮')
        DomAssert(drivers).assert_page_source('所有者')
        pass

    @allure.story("与我协作切换")  # 场景名称
    @allure.title("与我协作-图标列表切换")  # 用例名称
    @allure.description("与我协作页面操作图标列表切换")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = ShowSwitch(drivers)
        tools.click_menu('组件中心', '与我协作')
        tools.click('图标列表切换按钮')
        DomAssert(drivers).assert_att('所有者')
        tools.click('图标列表切换按钮')
        DomAssert(drivers).assert_page_source('所有者')
        pass

if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/ShowSwitch.py'])
