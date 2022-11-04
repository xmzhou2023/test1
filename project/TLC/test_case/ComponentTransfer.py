import allure
import pytest
from project.TLC.page_object.ComponentTransfer import Transfer
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("迁移") # 模块名称
class TestComponentTransfer:
    @allure.story("我的空间-组件迁移")  # 场景名称
    @allure.title("我的空间-文件夹下组件迁移到我的空间")  # 用例名称
    @allure.description("我的空间，新增文件夹，新增组件，新增组件迁移到我的空间")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Transfer(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')
        # 新增组件
        tools.click('文件夹新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_in_file_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_in_file_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 迁移
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('迁移', 'auto_testing_add_components_in_file_pri_001')
        tools.click('迁移选择框')
        tools.click('下拉icon', '1')
        tools.click('迁移目标空间', '1')
        tools.click('迁移弹框按钮', 'confirm')
        DomAssert(drivers).assert_att('迁移成功')
        # 删除文件夹
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')
        # 删除组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_in_file_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')
      

    @allure.story("我的空间-组件迁移")  # 场景名称
    @allure.title("我的空间-组件迁移到我的空间文件夹下")  # 用例名称
    @allure.description("我的空间，新增组件，新增文件夹，新增组件迁移到我的空间新增文件夹下")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Transfer(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 迁移
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('迁移', 'auto_testing_add_components_pri_001')
        tools.click('迁移选择框')
        tools.click('下拉icon', '1')
        tools.click('迁移目标文件夹', '1')
        tools.click('迁移弹框按钮', 'confirm')
        DomAssert(drivers).assert_att('迁移成功')

        # 删除组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.click('文件Item')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')
        # 删除文件夹
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')
      

    @allure.story("我的空间-组件迁移")  # 场景名称
    @allure.title("我的空间-空间下组件迁移到公共空间下")  # 用例名称
    @allure.description("我的空间，新增组件；新增组件迁移到公共空间下")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Transfer(drivers)
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 迁移
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('迁移', 'auto_testing_add_components_pri_001')
        tools.click('迁移选择框')
        tools.click('下拉icon', '2')
        tools.click('迁移目标空间', '2')
        tools.click('迁移弹框按钮', 'confirm')
        DomAssert(drivers).assert_att('迁移成功')

        # 删除组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')
      

    @allure.story("我的空间-组件迁移")  # 场景名称
    @allure.title("我的空间-组件迁移到公共空间文件夹下")  # 用例名称
    @allure.description("我的空间，新增组件；公共空间新增文件夹，新增组件迁移到我的空间新增文件夹下")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Transfer(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pub_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 迁移
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('迁移', 'auto_testing_add_components_pri_001')
        tools.click('迁移选择框')
        tools.click('下拉icon', '2')
        tools.click('迁移目标文件夹', '2')
        tools.click('迁移弹框按钮', 'confirm')
        DomAssert(drivers).assert_att('迁移成功')
        # 删除组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('文件Item')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')
        # 删除文件夹
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pub_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')
      

    @allure.story("公共空间-组件迁移")  # 场景名称
    @allure.title("公共空间-文件夹下组件迁移到公共空间")  # 用例名称
    @allure.description("公共空间，新增文件夹，新增组件，新增组件迁移到公共空间")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Transfer(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pub_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')
        # 新增组件
        tools.click('文件夹新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_in_file_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_in_file_pub_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 迁移
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('迁移', 'auto_testing_add_components_in_file_pub_001')
        tools.click('迁移选择框')
        tools.click('下拉icon', '2')
        tools.click('迁移目标空间', '2')
        tools.click('迁移弹框按钮', 'confirm')
        DomAssert(drivers).assert_att('迁移成功')
        # 删除文件夹
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pub_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')
        # 删除组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_in_file_pub_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')
      

    @allure.story("公共空间-组件迁移")  # 场景名称
    @allure.title("公共空间-组件迁移到公共空间文件夹下")  # 用例名称
    @allure.description("公共空间，新增组件，新增文件夹，新增组件迁移到公共空间新增文件夹下")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Transfer(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pub_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 迁移
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('迁移', 'auto_testing_add_components_pub_001')
        tools.click('迁移选择框')
        tools.click('下拉icon', '2')
        tools.click('迁移目标文件夹', '2')
        tools.click('迁移弹框按钮', 'confirm')
        DomAssert(drivers).assert_att('迁移成功')
        # 删除组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('文件Item')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pub_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')
        # 删除文件夹
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pub_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')
      

if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/ComponentTransfer.py'])