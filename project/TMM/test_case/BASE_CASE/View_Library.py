import allure
import pytest

from project.TMM.page_object.View_Library import ViewLibraryPage

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("视图库") # 模块名称
class TestUtil:
    @allure.story("视图库页面操作") # 场景名称
    @allure.title("切入视图库")  # 用例名称
    @allure.description("进入视图库模块页面")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        project = ViewLibraryPage(drivers)
        ViewLibraryTitle = project.goto_ViewLibrary()
        assert '视图库' in ViewLibraryTitle, '进入视图库模块失败！'

    @allure.story("视图库页面操作")  # 场景名称
    @allure.title("新增视图")  # 用例名称
    @allure.description("新增一个视图")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = ViewLibraryPage(drivers)
        AddViewTitle = project.AddView('lhjce1', 'lhjce1_edit')
        assert '默认视图设置' in AddViewTitle, '新增视图失败'