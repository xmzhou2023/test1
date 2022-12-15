import allure
import pytest
from project.TLC.page_object.HistoricalVersion import Version
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("历史版本") # 模块名称
class TestHistoricalVersion:
    @allure.story("组件发布")  # 场景名称
    @allure.title("我的文件-组件发布")  # 用例名称
    @allure.description("我的空间，新增组件，发布组件；公共空间，新增组件，发布组件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Version(drivers)
        # 我的空间-组件发布
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.switch_window_tlc(1)
        tools.click('发布')
        tools.click('发布确定')
        DomAssert(drivers).assert_att('发布成功')
        tools.close_switch(1)
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        # 公共空间-组件发布
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.switch_window_tlc(1)
        tools.click('发布')
        tools.click('发布确定')
        DomAssert(drivers).assert_att('发布成功')
        tools.close_switch(1)
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pub_001')
        tools.click('删除确认')
      

    @allure.story("组件回退")  # 场景名称
    @allure.title("我的文件-组件回退")  # 用例名称
    @allure.description("我的空间，新增组件，发布组件，回退版本创建记录；公共空间，新增组件，发布组件，回退版本创建记录")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Version(drivers)
        # 我的空间-组件发布
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.switch_window_tlc(1)
        tools.click('发布')
        tools.click('发布确定')
        DomAssert(drivers).assert_att('发布成功')
        tools.close_switch(1)
        # 版本回退
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('版本', 'auto_testing_add_components_pri_001')
        tools.switch_window_tlc(1)
        tools.click('回退记录', '创建')
        tools.click('回退')
        DomAssert(drivers).assert_att('回退成功')
        tools.close_switch(1)
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        # 公共空间-组件发布
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.switch_window_tlc(1)
        tools.click('发布')
        tools.click('发布确定')
        DomAssert(drivers).assert_att('发布成功')
        tools.close_switch(1)
        # 版本回退
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('版本', 'auto_testing_add_components_pub_001')
        tools.switch_window_tlc(1)
        tools.click('回退记录', '创建')
        tools.click('回退')
        DomAssert(drivers).assert_att('回退成功')
        tools.close_switch(1)
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pub_001')
        tools.click('删除确认')
      


if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/HistoricalVersion.py'])
