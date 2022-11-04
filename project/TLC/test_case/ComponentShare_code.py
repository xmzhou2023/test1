import allure
import pytest
from project.TLC.page_object.ComponentShare_code import Share
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("组件分享") # 模块名称
class TestComponentSharing:
    @allure.story("我的空间-组件分享")  # 场景名称
    @allure.title("我的空间-组件分享")  # 用例名称
    @allure.description("我的空间，新增组件，分享链接操作")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Share(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 分享
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('分享', 'auto_testing_add_components_pri_001')
        tools.click('复制链接')
        DomAssert(drivers).assert_att('复制成功')
        tools.click('复制弹框取消')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
      

    @allure.story("公共空间-组件分享")  # 场景名称
    @allure.title("公共空间-组件分享")  # 用例名称
    @allure.description("公共空间，新增组件，分享链接操作")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Share(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 分享
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('分享', 'auto_testing_add_components_pub_001')
        tools.click('复制链接')
        DomAssert(drivers).assert_att('复制成功')
        tools.click('复制弹框取消')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pub_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pub_001')
      

    @allure.story("组件code校验")  # 场景名称
    @allure.title("组件code查看与复制")  # 用例名称
    @allure.description("新增组件，复制code")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Share(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.switch_window(1)
        # 查看code
        tools.hover('编码查看')
        DomAssert(drivers).assert_att('auto_testing_add_components_pri_001')
        tools.close_switch(1)
        # 复制code
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('复制编码', 'auto_testing_add_components_pri_001')
        DomAssert(drivers).assert_att('复制成功')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
      
if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/ComponentShare_code.py'])
