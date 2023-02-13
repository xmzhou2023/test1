import allure
import pytest

from project.TMM.page_object.Attribute_Library import AttributeLibraryPage

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("属性库") # 模块名称
class TestUtil:
    @allure.story("属性库页面操作") # 场景名称
    @allure.title("切入属性库")  # 用例名称
    @allure.description("进入属性库模块页面")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        project = AttributeLibraryPage(drivers)
        AttributeLibraryTitle = project.goto_AttributeLibrary()
        assert '属性库' in AttributeLibraryTitle, '进入属性库模块失败！'

    @allure.story("属性库页面操作")  # 场景名称
    @allure.title("新增属性")  # 用例名称
    @allure.description("新增一个属性")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = AttributeLibraryPage(drivers)
        AddAttributeTitle = project.AddAttribute('lhjce1', 'lhjce1', 'lhjce1_edit')
        assert 'SAP属性编码' in AddAttributeTitle, '新增属性失败！'

    @allure.story("属性库页面操作")  # 场景名称
    @allure.title("编辑属性")  # 用例名称
    @allure.description("编辑一个属性")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = AttributeLibraryPage(drivers)
        EditAttributeTitle = project.EditAttribute('lhjce2', 'lhjce2', 'lhjce1_edit')
        assert 'SAP属性编码' in EditAttributeTitle, '新增属性失败！'

    @allure.story("属性库页面操作")  # 场景名称
    @allure.title("属性搜索")  # 用例名称
    @allure.description("对一个属性进行搜索")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        project = AttributeLibraryPage(drivers)
        project.SearchAttribute('lhjce1')