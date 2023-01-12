import allure
import pytest
from project.TLC.page_object.ComponentPreview import ComponentPreview
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("组件预览") # 模块名称
class TestComponentPreview:
    @allure.story("我的空间-组件预览")  # 场景名称
    @allure.title("我的空间-组件code校验")  # 用例名称
    @allure.description("我的空间，新增组件，组件编辑页面校验code值")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = ComponentPreview(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.switch_window_tlc(1)
        tools.hover('编码查看')
        DomAssert(drivers).assert_att('private-auto_testing_add_components_pri_001')
        tools.close_switch_tlc(1)
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')
      

    @allure.story("公共空间-组件预览")  # 场景名称
    @allure.title("公共空间-组件code校验")  # 用例名称
    @allure.description("公共空间，新增组件，组件编辑页面校验code值")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = ComponentPreview(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.switch_window_tlc(1)
        tools.hover('编码查看')
        DomAssert(drivers).assert_att('public-auto_testing_add_components_pub_001')
        tools.close_switch_tlc(1)
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pub_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')
      

    @allure.story("组件加锁")  # 场景名称
    @allure.title("组件加锁/解锁")  # 用例名称
    @allure.description("我的空间，新增组件，组件默认为加锁状态,点击加锁,组件变为解锁状态")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = ComponentPreview(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.switch_window_tlc(1)
        DomAssert(drivers).assert_att('自动解锁时间为:')
        tools.click('加锁按钮')
        DomAssert(drivers).assert_att('解锁成功')
        tools.close_switch_tlc(1)
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')
      

if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/ComponentPreview.py'])