import allure
import pytest

from project.TLC.page_object.My_files_check import UserPage
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("我的文件-查询") # 模块名称
class TestMyFilesCheck:
    @allure.story("我的文件查询") # 场景名称
    @allure.title("文件查询_正例")  # 用例名称
    @allure.description("我的文件页面中，在顶部框输入对应的文件名，系统能够正常显示公共空间和我的空间中与之匹配的文件夹名")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        # 新增
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增确认')

        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pub_001', 'name')
        tools.click('新增确认')

        # check
        tools.handle_readonly_input('顶部搜索框', 'auto_testing_add_files')
        DomAssert(drivers).assert_att('auto_testing_add_files_pri_001')
        DomAssert(drivers).assert_att('auto_testing_add_files_pub_001')

        # 删除
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pub_001')
        tools.click('删除确认')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')
      

    @allure.story("我的文件查询")  # 场景名称
    @allure.title("文件查询_反例")  # 用例名称
    @allure.description(
        "我的文件页面中，在顶部框输入不存在的字符串，系统显示无数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')

        # 新增
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增确认')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pub_001', 'name')
        tools.click('新增确认')

        # check
        tools.handle_readonly_input('顶部搜索框', 'auto_testing_add_files_111111111111111111111111111')
        DomAssert(drivers).assert_att('无数据')

        # 删除
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pub_001')
        tools.click('删除确认')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')
      

if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/My_files_check.py'])
