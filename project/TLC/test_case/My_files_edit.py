import allure
import pytest


from public.base.assert_ui import DomAssert
from project.TLC.page_object.My_files_edit import UserPage
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("我的文件-编辑") # 模块名称
class TestMyFilesEdit:
    @allure.story("我的文件修改") # 场景名称
    @allure.title("我的文件-文件名修改_正例")  # 用例名称
    @allure.description("在导航菜单中点击我的文件，点击我的空间，选择对应的文件，右键选择重命名，输入合法的文件夹名，点击确认按钮，修改文件夹成功，系统给出正常的提示")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增确认')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_files_pri_001')
        tools.input('重命名输入框', 'auto_testing_add_files_pri_002')
        tools.click('重命名按钮', '1')
        DomAssert(drivers).assert_att('修改成功')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_files_pri_002')
        tools.click('删除确定')
      

    @allure.story("我的文件修改")  # 场景名称
    @allure.title("我的文件-文件重命名_反例")  # 用例名称
    @allure.description(
        "在导航菜单中点击我的文件，点击我的空间，选择对应的文件，右键选择重命名，输入 空 ，点击确认按钮，系统提示 文件名不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增确认')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_files_pri_001')
        tools.click('清空按钮')
        tools.click('重命名按钮', '1')
        DomAssert(drivers).assert_att('不能为空')
        tools.click('重命名按钮', '2')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_files_pri_001')
        tools.click('删除确定')
      

    @allure.story("我的文件修改")  # 场景名称
    @allure.title("我的文件-我的空间-文件名修改_删除对话框取消")  # 用例名称
    @allure.description(
        "在导航菜单中点击我的文件，点击我的空间，选择对应的文件，右键选择重命名，在弹出的修改对话框中，点击取消按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增确认')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_files_pri_001')
        tools.click('重命名按钮', '2')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_files_pri_001')
        tools.click('删除确定')
      

    @allure.story("我的文件修改")  # 场景名称
    @allure.title("我的文件-我的空间-文件名修改对话框关闭")  # 用例名称
    @allure.description(
        "在导航菜单中点击我的文件，点击我的空间，选择对应的文件，右键选择重命名，在弹出的修改对话框中，点击 x 按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增确认')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_files_pri_001')
        tools.click('重命名X')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_files_pri_001')
        tools.click('删除确定')
      

    @allure.story("我的文件修改")  # 场景名称
    @allure.title("我的文件-我的空间-文件名修改_正例")  # 用例名称
    @allure.description(
        "在导航菜单中点击我的文件，点击公共空间，选择对应的文件，右键选择重命名，输入合法的文件夹名，点击确认按钮，修改文件夹成功，系统给出正常的提示")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pub_001', 'name')
        tools.click('新增确认')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_files_pub_001')
        tools.input('重命名输入框', 'auto_testing_add_files_pub_002')
        tools.click('重命名按钮', '1')
        DomAssert(drivers).assert_att('修改成功')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_files_pub_002')
        tools.click('删除确定')
      

    @allure.story("我的文件修改")  # 场景名称
    @allure.title("我的文件-公共空间_文件名修改_反例")  # 用例名称
    @allure.description(
        "在导航菜单中点击我的文件，点击公共空间，选择对应的文件，右键选择重命名，输入 空 ，点击确认按钮，系统提示 文件名不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_006(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        # 新增
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pub_001', 'name')
        tools.click('新增确认')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_files_pub_001')
        tools.click('清空按钮')
        tools.click('重命名按钮', '1')
        DomAssert(drivers).assert_att('不能为空')
        tools.click('重命名按钮', '2')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_files_pub_001')
        tools.click('删除确定')

      

    @allure.story("我的文件修改")  # 场景名称
    @allure.title("我的文件-公共空间-文件名修改对话框取消")  # 用例名称
    @allure.description(
        "在导航菜单中点击我的文件，点击公共空间，选择对应的文件，右键选择重命名，在弹出的修改对话框中，点击取消按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_007(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pub_001', 'name')
        tools.click('新增确认')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_files_pub_001')
        tools.click('重命名按钮', '2')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_files_pub_001')
        tools.click('删除确定')
      

    @allure.story("我的文件修改")  # 场景名称
    @allure.title("我的文件-公共空间_文件名修改对话框关闭")  # 用例名称
    @allure.description(
        "在导航菜单中点击我的文件，点击公共空间，选择对应的文件，右键选择重命名，在弹出的修改对话框中，点击 x 按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_008(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pub_001', 'name')
        tools.click('新增确认')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'rename', 'auto_testing_add_files_pub_001')
        tools.click('重命名X')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('下拉菜单', 'remove', 'auto_testing_add_files_pub_001')
        tools.click('删除确定')
      

if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/My_files_edit.py'])
