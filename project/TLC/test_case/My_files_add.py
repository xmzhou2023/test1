import allure
import pytest

from project.TLC.page_object.My_files_add import Tool
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("我的文件-新增") # 模块名称
class TestMyFilesAdd:
    @allure.story("我的文件新增")  # 场景名称  =》 自动化测试平台对应
    @allure.title("文件新增-我的空间_正例")  # 用例名称
    @allure.description("在我的空间中，点击新增文件夹按钮后，输入合法的文件名，系统新增文件夹成功")
    @allure.severity("normal")  # 用例等级
    def test_001_001(self, drivers):
        tools = Tool(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('名称输入框', 'auto_testing_add_files_pri_001')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')

        # 删除
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')
      

    @allure.story("我的文件新增")  # 场景名称
    @allure.title("文件新增-我的空间_反例")  # 用例名称
    @allure.description("在我的空间中，点击新增文件夹按钮后，输入 空 ，系统提示文件夹名不能为空")
    @allure.severity("normal")  # 用例等级
    def test_001_002(self, drivers):
        tools = Tool(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('名称输入框', '')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('不能为空')
        tools.click('新增对话框按钮', 'cancel')
      

    @allure.story("我的文件新增")  # 场景名称
    @allure.title("文件新增-我的空间_新增弹框取消")  # 用例名称
    @allure.description("在我的空间中，点击新增文件夹按钮后，点击取消按钮")
    @allure.severity("normal")  # 用例等级
    def test_001_003(self, drivers):
        tools = Tool(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.click('新增对话框按钮', 'cancel')
      

    @allure.story("我的文件新增")  # 场景名称
    @allure.title("文件新增-我的空间_新增弹框关闭")  # 用例名称
    @allure.description("在我的空间中，点击新增文件夹按钮后，点击 x 关闭对话框")
    @allure.severity("normal")  # 用例等级
    def test_001_004(self, drivers):
        tools = Tool(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.click('x')
      

    @allure.story("公共新增")  # 场景名称
    @allure.title("文件新增-公共空间_正例")  # 用例名称
    @allure.description("在公共空间中，点击新增文件夹按钮后，输入合法的文件名，系统新增文件夹成功")
    @allure.severity("normal")  # 用例等级
    def test_001_005(self, drivers):
        tools = Tool(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('名称输入框', 'auto_testing_add_files_pub_001')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')

        # 删除
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pub_001')
        tools.click('删除确认')
      

    @allure.story("公共新增")  # 场景名称
    @allure.title("文件新增-公共空间_反例")  # 用例名称
    @allure.description("在公共空间中，点击新增文件夹按钮后，输入 空，系统提示文件夹名不能为空")
    @allure.severity("normal")  # 用例等级
    def test_001_006(self, drivers):
        tools = Tool(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('名称输入框', '')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('不能为空')
        tools.click('新增对话框按钮', 'cancel')
      

    @allure.story("我的文件新增")  # 场景名称
    @allure.title("文件新增-公共空间_新增弹框取消")  # 用例名称
    @allure.description("在公共空间中，点击新增文件夹按钮后，点击取消按钮")
    @allure.severity("normal")  # 用例等级
    def test_001_007(self, drivers):
        tools = Tool(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.click('新增对话框按钮', 'cancel')
      

    @allure.story("我的文件新增")  # 场景名称
    @allure.title("文件新增-公共空间_新增弹框关闭")  # 用例名称
    @allure.description("在公共空间中，点击新增文件夹按钮后，点击 x 关闭对话框")
    @allure.severity("normal")  # 用例等级
    def test_001_008(self, drivers):
        tools = Tool(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.click('x')
      

if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/My_files_add.py'])
