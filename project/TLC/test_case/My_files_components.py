import allure
import pytest

from project.TLC.page_object.My_files_components import Tool
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("我的文件-文件夹-组件增删") # 模块名称
class TestMyfileAddComponents:
    @allure.story("文件-组件增删") # 场景名称
    @allure.title("文件_组件增删-我的空间_正例")  # 用例名称
    @allure.description("在我的文件我的空间中，新增一个文件夹，在文件夹中新增组件，输入正确的name和code值，系统提示新增成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        tools = Tool(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')

        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_in_file_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_in_file_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_in_file_pri_001')
        tools.click('删除确认')

        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')
        pass

    @allure.story("文件-组件增删")  # 场景名称
    @allure.title("文件_组件增删-公共空间")  # 用例名称
    @allure.description(
        "在我的文件我的空间中，新增一个文件夹，在文件夹中新增组件，输入正确的name和code值，系统提示新增成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Tool(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pub_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')

        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_in_file_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_in_file_pub_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_in_file_pub_001')
        tools.click('删除确认')

        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pub_001')
        tools.click('删除确认')
        pass

if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/My_files_components.py'])
