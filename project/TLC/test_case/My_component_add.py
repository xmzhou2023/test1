import allure
import pytest


from project.TLC.page_object.My_component_add import UserPage
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("我的组件-新增") # 模块名称
class TestMyComponentAdd:
    @allure.story("我的文件-组件新增") # 场景名称
    @allure.title("组件新增-我的空间_正例")  # 用例名称
    @allure.description("在我的文件中，点击我的空间，点击新增按钮，选择新增组件，输入合法的组件名称、code，点击确定按钮，系统提示新增成功")
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
        DomAssert(drivers).assert_att('新增成功')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确定')
        pass

    @allure.story("我的文件-组件新增")  # 场景名称
    @allure.title("组件新增-我的空间_反例1")  # 用例名称
    @allure.description(
        "在我的文件中，点击我的空间，点击新增按钮，选择新增组件，code值输入为 空 ，输入合法的组件名称，点击确定按钮，系统提示code不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', '', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        DomAssert(drivers).assert_att('不能为空')
        tools.click('新增Button', 'cancel')
        pass

    @allure.story("我的文件-组件新增")  # 场景名称
    @allure.title("组件新增-我的空间_反例2")  # 用例名称
    @allure.description(
        "在我的文件中，点击我的空间，点击新增按钮，选择新增组件，输入重复的code值 ，输入合法的组件名称，点击确定按钮，系统提示组件重复")
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
        tools.switch_window(0)
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        DomAssert(drivers).assert_att('code不能重复')
        tools.click('新增Button', 'cancel')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确定')

        pass

    @allure.story("我的文件-组件新增")  # 场景名称
    @allure.title("组件新增-我的空间_反例3")  # 用例名称
    @allure.description(
        "在我的文件中，点击我的空间，点击新增按钮，选择新增组件，输入合法的code值 ，名称输入 空 ，点击确定按钮，系统提示不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', '', 'name')
        tools.click('新增Button', 'confirm')
        DomAssert(drivers).assert_att('不能为空')
        tools.click('新增Button', 'cancel')
        pass

    @allure.story("我的文件-组件新增")  # 场景名称
    @allure.title("组件新增-我的空间_新增对话框关闭")  # 用例名称
    @allure.description(
        "在我的文件中，点击我的空间，点击新增按钮，选择新增组件，当对话框出现后，点击右上角的 x 按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.click('x')
        pass

    @allure.story("我的文件-组件新增")  # 场景名称
    @allure.title("组件新增-我的空间_新增对话框取消")  # 用例名称
    @allure.description(
        "在我的文件中，点击我的空间，点击新增按钮，选择新增组件，当对话框出现后，点击 取消按钮 按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_006(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.click('新增Button', 'cancel')
        pass

    @allure.story("我的文件-组件新增")  # 场景名称
    @allure.title("组件新增-公共空间_正例")  # 用例名称
    @allure.description(
        "在我的文件中，点击公共空间，点击新增按钮，选择新增组件，输入合法的组件名称、code，点击确定按钮，系统提示新增成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_007(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.switch_window(0)
        DomAssert(drivers).assert_att('新增成功')
        tools.click('空间', '公共空间')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('删除', 'auto_testing_add_components_pub_001')
        tools.click('删除确定')
        pass

    @allure.story("我的文件-组件新增")  # 场景名称
    @allure.title("组件新增-公共空间_反例1")  # 用例名称
    @allure.description(
        "在我的文件中，点击我的空间，点击新增按钮，选择新增组件，code值输入为 空 ，输入合法的组件名称，点击确定按钮，系统提示code不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_008(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', '', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        tools.click('新增Button', 'confirm')
        DomAssert(drivers).assert_att('不能为空')
        tools.click('新增Button', 'cancel')
        pass

    @allure.story("我的文件-组件新增")  # 场景名称
    @allure.title("组件新增-公共空间_反例2")  # 用例名称
    @allure.description(
        "在我的文件中，点击我的空间，点击新增按钮，选择新增组件，输入重复的code值 ，输入合法的组件名称，点击确定按钮，系统提示组件重复")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_009(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.switch_window(0)
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'name')
        DomAssert(drivers).assert_att('code不能重复')
        tools.click('新增Button', 'cancel')
        tools.click('空间', '公共空间')
        tools.hover('组件item')
        tools.click('组件item more')
        tools.click('删除', 'auto_testing_add_components_pub_001')
        tools.click('删除确定')
        pass

    @allure.story("我的文件-组件新增")  # 场景名称
    @allure.title("组件新增-公共空间_反例3")  # 用例名称
    @allure.description(
        "在我的文件中，点击我的空间，点击新增按钮，选择新增组件，输入合法的code值 ，名称输入 空 ，点击确定按钮，系统提示不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_0010(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pub_001', 'code')
        tools.input('新增输入框', '', 'name')
        tools.click('新增Button', 'confirm')
        DomAssert(drivers).assert_att('不能为空')
        tools.click('新增Button', 'cancel')
        pass

    @allure.story("我的文件-组件新增")  # 场景名称
    @allure.title("组件新增-公共空间_新增对话框关闭")  # 用例名称
    @allure.description(
        "在我的文件中，点击我的空间，点击新增按钮，选择新增组件，当对话框出现后，点击右上角的 x 按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_0011(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.click('x')
        pass

    @allure.story("我的文件-组件新增")  # 场景名称
    @allure.title("组件新增-公共空间_新增对话框取消")  # 用例名称
    @allure.description(
        "在我的文件中，点击我的空间，点击新增按钮，选择新增组件，当对话框出现后，点击 取消按钮 按钮")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_0012(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.click('新增Button', 'cancel')
        pass
if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/My_component_add.py'])
