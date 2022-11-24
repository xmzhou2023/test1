import allure
import pytest


from project.TLC.page_object.My_component_edit import UserPage
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("我的组件-编辑") # 模块名称
class TestMyComponentEdit:
    @allure.story("我的文件-组件编辑") # 场景名称
    @allure.title("我的文件-我的空间_组件名称编辑_正例")  # 用例名称
    @allure.description("在我的文件页面中，点击我的空间，选择对应的组件，右键点击重命名，输入合法的组件名称，点击确定，系统提示名称修改成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_002_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch_tlc(1)
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_components_pri_001')
        tools.input('重命名输入框', 'auto_testing_add_components_pri_002')
        tools.click('重命名按钮', '1')
        DomAssert(drivers).assert_att('修改成功')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_components_pri_002')
        tools.click('删除确定')
      

    @allure.story("我的文件-组件编辑")  # 场景名称
    @allure.title("我的文件-我的空间_组件名称编辑_反例1")  # 用例名称
    @allure.description(
        "在我的文件页面中，点击我的空间，选择对应的组件，右键点击重命名，输入 空 ，点击确定，系统提示名称不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch_tlc(1)
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_components_pri_001')
        tools.click('清空按钮')
        tools.click('重命名按钮', '1')
        DomAssert(drivers).assert_att('不能为空')
        tools.click('重命名按钮', '2')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_components_pri_001')
        tools.click('删除确定')
      


    @allure.story("我的文件-组件编辑")  # 场景名称
    @allure.title("我的文件-我的空间_组件名称编辑对话框取消")  # 用例名称
    @allure.description(
        "在我的文件页面中，点击我的空间，选择对应的组件，右键点击重命名，点击取消，关闭对话框")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch_tlc(1)
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_components_pri_001')
        tools.click('重命名按钮', '2')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_components_pri_001')
        tools.click('删除确定')
      

    @allure.story("我的文件-组件编辑")  # 场景名称
    @allure.title("我的文件-我的空间_组件名称编辑对话框关闭")  # 用例名称
    @allure.description(
        "在我的文件页面中，点击我的空间，选择对应的组件，右键点击重命名，点击 X，关闭对话框")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch_tlc(1)
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_components_pri_001')
        tools.click('重命名X')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_components_pri_001')
        tools.click('删除确定')
      

    @allure.story("我的文件-组件编辑")  # 场景名称
    @allure.title("我的文件-公共空间_组件名称编辑_正例")  # 用例名称
    @allure.description(
        "在我的文件页面中，点击公共空间，选择对应的组件，右键点击重命名，输入合法的组件名称，点击确定，系统提示名称修改成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch_tlc(1)
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_components_pub_001')
        tools.input('重命名输入框', 'auto_testing_add_components_pub_002')
        tools.click('重命名按钮', '1')
        DomAssert(drivers).assert_att('修改成功')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_components_pub_002')
        tools.click('删除确定')
      

    @allure.story("我的文件-组件编辑")  # 场景名称
    @allure.title("我的文件-公共空间_组件名称编辑_反例")  # 用例名称
    @allure.description(
        "在我的文件页面中，点击公共空间，选择对应的组件，右键点击重命名，输入 空 ，点击确定，系统提示名称不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_006(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch_tlc(1)
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_components_pub_001')
        tools.click('清空按钮')
        tools.click('重命名按钮', '1')
        DomAssert(drivers).assert_att('不能为空')
        tools.click('重命名按钮', '2')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_components_pub_001')
        tools.click('删除确定')

      

    @allure.story("我的文件-组件编辑")  # 场景名称
    @allure.title("我的文件-我的空间_组件名称编辑对话框取消")  # 用例名称
    @allure.description(
        "在我的文件页面中，点击公共空间，选择对应的组件，右键点击重命名，点击取消，关闭对话框")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_007(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch_tlc(1)
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_components_pub_001')
        tools.click('重命名按钮', '2')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_components_pub_001')
        tools.click('删除确定')
      

    @allure.story("我的文件-组件编辑")  # 场景名称
    @allure.title("我的文件-公共空间_组件名称编辑对话框关闭")  # 用例名称
    @allure.description(
        "在我的文件页面中，点击公共空间，选择对应的组件，右键点击重命名，点击 X，关闭对话框")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_008(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch_tlc(1)
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_components_pub_001')
        tools.click('重命名X')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_components_pub_001')
        tools.click('删除确定')
      


if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/My_component_edit.py'])
