import allure
import pytest
from project.TLC.page_object.RecycleBin import RecycleBin
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("回收站") # 模块名称
class TestRecycleBin:
    @allure.story("我的空间-回收站操作")  # 场景名称
    @allure.title("我的空间-回收站彻底删除文件夹")  # 用例名称
    @allure.description("回收站彻底删除文件夹")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = RecycleBin(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_files_pri_001')
        # 彻底删除
        tools.click_menu('组件中心', '回收站')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('彻底删除', 'auto_testing_add_files_pri_001')
        DomAssert(drivers).assert_att('删除成功')
        pass

    @allure.story("我的空间-回收站操作")  # 场景名称
    @allure.title("我的空间-回收站彻底删除组件")  # 用例名称
    @allure.description("回收站彻底删除组件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = RecycleBin(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 彻底删除
        tools.click_menu('组件中心', '回收站')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('彻底删除', 'auto_testing_add_components_pri_001')
        DomAssert(drivers).assert_att('删除成功')
        pass

    @allure.story("我的空间-回收站操作")  # 场景名称
    @allure.title("我的空间-回收站还原文件夹")  # 用例名称
    @allure.description("回收站还原文件夹")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = RecycleBin(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_files_pri_001')
        # 还原
        tools.click_menu('组件中心', '回收站')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('还原', 'auto_testing_add_files_pri_001')
        tools.click('还原确定')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_files_pri_001')
        pass

    @allure.story("我的空间-回收站操作")  # 场景名称
    @allure.title("我的空间-回收站还原组件")  # 用例名称
    @allure.description("回收站还原组件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = RecycleBin(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 还原
        tools.click_menu('组件中心', '回收站')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('还原', 'auto_testing_add_components_pri_001')
        tools.click('还原确定')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass

    @allure.story("我的空间-回收站操作")  # 场景名称
    @allure.title("我的空间-回收站还原组件code相同场景")  # 用例名称
    @allure.description("回收站还原组件code相同场景")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = RecycleBin(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 新增相同code组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 还原
        tools.click_menu('组件中心', '回收站')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('还原', 'auto_testing_add_components_pri_001')
        tools.click('还原确定')

        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass

    @allure.story("公共空间-回收站操作")  # 场景名称
    @allure.title("公共空间-回收站彻底删除文件夹")  # 用例名称
    @allure.description("回收站彻底删除文件夹")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = RecycleBin(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_files_pri_001')
        # 彻底删除
        tools.click_menu('组件中心', '回收站')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('彻底删除', 'auto_testing_add_files_pri_001')
        DomAssert(drivers).assert_att('删除成功')
        pass

    @allure.story("公共空间-回收站操作")  # 场景名称
    @allure.title("公共空间-回收站彻底删除组件")  # 用例名称
    @allure.description("回收站彻底删除组件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = RecycleBin(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 彻底删除
        tools.click_menu('组件中心', '回收站')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('彻底删除', 'auto_testing_add_components_pri_001')
        DomAssert(drivers).assert_att('删除成功')
        pass

    @allure.story("公共空间-回收站操作")  # 场景名称
    @allure.title("公共空间-回收站还原文件夹")  # 用例名称
    @allure.description("回收站还原文件夹")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = RecycleBin(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_files_pri_001')
        # 还原
        tools.click_menu('组件中心', '回收站')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('还原', 'auto_testing_add_files_pri_001')
        tools.click('还原确定')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_files_pri_001')
        pass

    @allure.story("公共空间-回收站操作")  # 场景名称
    @allure.title("公共空间-回收站还原组件")  # 用例名称
    @allure.description("回收站还原组件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = RecycleBin(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 还原
        tools.click_menu('组件中心', '回收站')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('还原', 'auto_testing_add_components_pri_001')
        tools.click('还原确定')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass

    @allure.story("公共空间-回收站操作")  # 场景名称
    @allure.title("公共空间-回收站还原组件code相同场景")  # 用例名称
    @allure.description("回收站还原组件code相同场景")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = RecycleBin(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 新增相同code组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 还原
        tools.click_menu('组件中心', '回收站')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('还原', 'auto_testing_add_components_pri_001')
        tools.click('还原确定')

        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass

if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/RecycleBin.py'])