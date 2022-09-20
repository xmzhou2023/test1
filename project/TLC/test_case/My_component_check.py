import allure
import pytest

from project.TLC.page_object.My_component_check import UserPage
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("我的组件-查询") # 模块名称
class TestMyComponentCheck:
    @allure.story("我的文件-组件查询") # 场景名称
    @allure.title("组件查询_正例")  # 用例名称
    @allure.description("在我的文件页面中，在顶部输入框中输入存在的组件名称，搜索框下拉结果中正常显示对应的组件信息")
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
        tools.switch_window(0)

        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.switch_window(0)
        tools.readonly_input('顶部搜索框', 'auto_testing_add_components', 'query')
        DomAssert(drivers).assert_att('auto_testing_add_components_pri_001')
        DomAssert(drivers).assert_att('auto_testing_add_components_pub_001')

        tools.click('空间', '公共空间')  #删除公共空间新增组件
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('删除', 'auto_testing_add_components_pub_001')
        tools.click('删除确定')


        tools.click('空间', '我的空间')   #删除我的空间新增组件
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确定')


        pass

    @allure.story("我的文件-组件查询")  # 场景名称
    @allure.title("组件查询_反例")  # 用例名称
    @allure.description("在我的文件页面中，在顶部输入框中输入不存在的组件名称，搜索框下拉结果显示无数据")
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
        tools.switch_window(0)

        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.switch_window(0)
        tools.readonly_input('顶部搜索框', 'auto_testing_add_components111111111111111', 'query')
        DomAssert(drivers).assert_att('无数据')

        tools.click('空间', '公共空间')  # 删除公共空间新增组件
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('删除', 'auto_testing_add_components_pub_001')
        tools.click('删除确定')

        tools.click('空间', '我的空间')  # 删除我的空间新增组件
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确定')
        pass

if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/My_component_check.py'])
