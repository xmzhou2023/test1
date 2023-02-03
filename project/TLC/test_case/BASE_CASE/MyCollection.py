import allure
import pytest
from project.TLC.page_object.MyCollection import collection
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("我的收藏") # 模块名称
class TestMyCollection:
    @allure.story("我的空间收藏操作")  # 场景名称
    @allure.title("我的空间-文件夹收藏/取消收藏")  # 用例名称
    @allure.description("文件夹收藏，我的收藏存在文件夹；文件夹取消收藏，我的收藏不存在未收藏的文件夹")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = collection(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')

        # 收藏操作
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('收藏', 'auto_testing_add_files_pri_001')
        tools.click_menu('组件中心', '我的收藏')
        DomAssert(drivers).assert_att('auto_testing_add_files_pri_001')
        # 取消收藏操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('取消收藏', 'auto_testing_add_files_pri_001')
        tools.click_menu('组件中心', '我的收藏')
        DomAssert(drivers).assert_page_source('auto_testing_add_files_pri_001')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')
      


    @allure.story("我的空间收藏操作") # 场景名称
    @allure.title("我的空间-组件收藏/取消收藏")  # 用例名称
    @allure.description("组件收藏，我的收藏存在组件；组件取消收藏，我的收藏不存在未收藏的组件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_002(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        tools = collection(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch_tlc(1)
        # 收藏操作
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('收藏', 'auto_testing_add_components_pri_001')
        tools.click_menu('组件中心', '我的收藏')
        DomAssert(drivers).assert_att('auto_testing_add_components_pri_001')

        # 取消收藏操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('取消收藏', 'auto_testing_add_components_pri_001')
        tools.click_menu('组件中心', '我的收藏')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')

        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
      


    @allure.story("公共空间收藏操作")  # 场景名称
    @allure.title("公共空间-文件夹收藏/取消收藏")  # 用例名称
    @allure.description("文件夹收藏，我的收藏存在文件夹；文件夹取消收藏，我的收藏不存在未收藏的文件夹")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = collection(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')

        # 收藏操作
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('收藏', 'auto_testing_add_files_pri_001')
        tools.click_menu('组件中心', '我的收藏')
        DomAssert(drivers).assert_att('auto_testing_add_files_pri_001')

        # 取消收藏操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('取消收藏', 'auto_testing_add_files_pri_001')
        tools.click_menu('组件中心', '我的收藏')
        DomAssert(drivers).assert_page_source('auto_testing_add_files_pri_001')

        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')

    @allure.story("公共空间收藏操作")  # 场景名称
    @allure.title("公共空间-组件收藏/取消收藏")  # 用例名称
    @allure.description("组件收藏，我的收藏存在组件；组件取消收藏，我的收藏不存在未收藏的组件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = collection(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch_tlc(1)

        # 收藏操作
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('收藏', 'auto_testing_add_components_pri_001')
        tools.click_menu('组件中心', '我的收藏')
        DomAssert(drivers).assert_att('auto_testing_add_components_pri_001')
        # 取消收藏操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('取消收藏', 'auto_testing_add_components_pri_001')
        tools.click_menu('组件中心', '我的收藏')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
      

    @allure.story("我的空间收藏操作")  # 场景名称
    @allure.title("我的收藏界面查询组件功能正例")  # 用例名称
    @allure.description("我的收藏界面查询收藏的组件,可以匹配到新增的组件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = collection(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch_tlc(1)

        # 收藏操作
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('收藏', 'auto_testing_add_components_pri_001')
        # 收藏界面顶部搜索
        tools.click_menu('组件中心', '我的收藏')
        tools.hover('顶部搜索框')
        tools.readonly_input('顶部搜索框', 'auto_testing_add_components_pri_001', 'query')
        DomAssert(drivers).assert_att('auto_testing_add_components_pri_001')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
      

    @allure.story("我的空间收藏操作")  # 场景名称
    @allure.title("我的收藏界面查询组件功能反例")  # 用例名称
    @allure.description("我的收藏界面查询未收藏的组件,提示无数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = collection(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch_tlc(1)

        # 收藏界面顶部搜索
        tools.click_menu('组件中心', '我的收藏')
        tools.hover('顶部搜索框')
        tools.readonly_input('顶部搜索框', 'auto_testing_add_components_pri_001', 'query')
        DomAssert(drivers).assert_att('无数据')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
      

    @allure.story("我的空间收藏操作")  # 场景名称
    @allure.title("我的收藏界面查询文件夹功能正例")  # 用例名称
    @allure.description("我的收藏界面查询收藏的文件夹,可以匹配到新增的文件夹")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = collection(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')
        # 收藏操作
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('收藏', 'auto_testing_add_files_pri_001')
        tools.click_menu('组件中心', '我的收藏')
        DomAssert(drivers).assert_att('auto_testing_add_files_pri_001')
        # 收藏界面顶部搜索
        tools.click_menu('组件中心', '我的收藏')
        tools.hover('顶部搜索框')
        tools.readonly_input('顶部搜索框', 'auto_testing_add_files_pri_001', 'query')
        DomAssert(drivers).assert_att('auto_testing_add_files_pri_001')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')
      

    @allure.story("我的空间收藏操作")  # 场景名称
    @allure.title("我的收藏界面查询文件夹功能反例")  # 用例名称
    @allure.description("我的收藏界面查询未收藏的文件夹,提示无数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = collection(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('新增输入框', 'auto_testing_add_files_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('新增成功')
        # 收藏界面顶部搜索
        tools.click_menu('组件中心', '我的收藏')
        tools.hover('顶部搜索框')
        tools.readonly_input('顶部搜索框', 'auto_testing_add_files_pri_001', 'query')
        DomAssert(drivers).assert_att('无数据')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除确认')

    @allure.story("组件中心")  # 场景名称
    @allure.title("组件中心下载校验")  # 用例名称
    @allure.description("组件中心下载校验")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_004_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = collection(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch_tlc(1)

        # 下载操作
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('下载', 'auto_testing_add_components_pri_001')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
      

if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/MyCollection.py'])

