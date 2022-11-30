import allure
import pytest


from public.base.assert_ui import DomAssert
from project.TLC.page_object.My_files_delete import UserPage
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("我的文件-删除") # 模块名称
class TestMyFilesDelete:
    @allure.story("我的文件删除") # 场景名称
    @allure.title("文件删除-我的空间文件删除_正例")  # 用例名称
    @allure.description("在我的文件中，点击我的空间，然后选择对应的文件进行删除，删除成功后，系统能给出正常的提示，该文件夹在对应的文件夹列表中消失")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('名称输入框', 'auto_testing_add_files_pri_001')
        tools.click('新增确定')

        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除弹框', '确定')
        DomAssert(drivers).assert_att('删除成功')
      

    @allure.story("我的文件删除")  # 场景名称
    @allure.title("文件删除-我的空间_删除对话框取消")  # 用例名称
    @allure.description("在我的文件中，点击我的空间，然后选择对应的文件进行删除，点击 取消按钮 ，文件夹取消删除")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('名称输入框', 'auto_testing_add_files_pri_001')
        tools.click('新增确定')

        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除弹框', '取消')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除弹框', '确定')
      

    @allure.story("我的文件删除")  # 场景名称
    @allure.title("文件删除-我的空间_删除对话框关闭")  # 用例名称
    @allure.description("在我的文件中，点击我的空间，然后选择对应的文件进行删除，点击 x按钮 ，文件夹取消删除")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('名称输入框', 'auto_testing_add_files_pri_001')
        tools.click('新增确定')

        tools.click('空间', '我的空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('x')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pri_001')
        tools.click('删除弹框', '确定')
      

    @allure.story("我的文件删除")  # 场景名称
    @allure.title("文件删除-公共空间_正例")  # 用例名称
    @allure.description("在我的文件中，点击公共空间，然后选择对应的文件进行删除，删除成功后，系统能给出正常的提示，该文件夹在对应的文件夹列表中消失")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('名称输入框', 'auto_testing_add_files_pub_001')
        tools.click('新增确定')

        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pub_001')
        tools.click('删除弹框', '确定')
        DomAssert(drivers).assert_att('删除成功')
      

    @allure.story("我的文件删除")  # 场景名称
    @allure.title("文件删除-公共空间_删除对话框取消")  # 用例名称
    @allure.description("在我的文件中，点击公共空间，然后选择对应的文件进行删除，点击 取消按钮 ，文件夹取消删除")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('名称输入框', 'auto_testing_add_files_pub_001')
        tools.click('新增确定')

        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pub_001')
        tools.click('删除弹框', '取消')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pub_001')
        tools.click('删除弹框', '确定')
      

    @allure.story("我的文件删除")  # 场景名称
    @allure.title("文件删除-公共空间_删除对话框关闭")  # 用例名称
    @allure.description("在我的文件中，点击公共空间，然后选择对应的文件进行删除，点击 x按钮 ，文件夹取消删除")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_006(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = UserPage(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('新增')
        tools.click('新增文件夹')
        tools.input('名称输入框', 'auto_testing_add_files_pub_001')
        tools.click('新增确定')

        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pub_001')
        tools.click('x')
        tools.click('空间', '公共空间')
        tools.click('空间', '公共空间')
        tools.hover('文件Item')
        tools.click('文件Item more')
        tools.click('删除', 'auto_testing_add_files_pub_001')
        tools.click('删除弹框', '确定')
      
if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/My_files_delete.py'])
