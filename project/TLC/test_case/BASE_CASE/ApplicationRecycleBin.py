import allure
import pytest
from project.TLC.page_object.ApplicationRecycleBin import RecycleBin
from public.base.assert_ui import DomAssert, ValueAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("应用中心") # 模块名称
class Teststory_1181:
    @allure.story("回收站")  # 场景名称
    @allure.title("回收站彻底删除应用")  # 用例名称
    @allure.description("新增应用-删除应用-回收站彻底删除应用")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test029(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = RecycleBin(drivers)
        # 新增应用
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用code')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用名称')
        tools.input('textarea输入框', 'auto_testing_add_Application_001', '应用描述')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'icon')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'cover')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('应用添加成功')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001' )
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')
        # 回收站彻底删除
        tools.click_menu('应用中心', '回收站')
        tools.hover('回收站应用Item', 'auto_testing_add_Application_001')
        tools.click('回收站应用Item more', 'auto_testing_add_Application_001')
        tools.click('回收站应用操作', '删除')
        tools.click('确定', '是否彻底删除该应用')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("回收站")  # 场景名称
    @allure.title("回收站还原应用")  # 用例名称
    @allure.description("新增应用-删除应用-回收站还原应用")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test030(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = RecycleBin(drivers)
        # 新增应用
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用code')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用名称')
        tools.input('textarea输入框', 'auto_testing_add_Application_001', '应用描述')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'icon')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'cover')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('应用添加成功')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')
        # 回收站还原
        tools.click_menu('应用中心', '回收站')
        tools.hover('回收站应用Item', 'auto_testing_add_Application_001')
        tools.click('回收站应用Item more', 'auto_testing_add_Application_001')
        tools.click('回收站应用操作', '还原')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('还原成功')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("回收站")  # 场景名称
    @allure.title("回收站还原code相同应用")  # 用例名称
    @allure.description("新增应用-删除应用-回收站还原code相同应用")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test031(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = RecycleBin(drivers)
        # 新增应用
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用code')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用名称')
        tools.input('textarea输入框', 'auto_testing_add_Application_001', '应用描述')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'icon')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'cover')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('应用添加成功')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')
        # 新增应用
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用code')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用名称')
        tools.input('textarea输入框', 'auto_testing_add_Application_001', '应用描述')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'icon')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'cover')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('应用添加成功')
        # 回收站还原
        tools.click_menu('应用中心', '回收站')
        tools.hover('回收站应用Item', 'auto_testing_add_Application_001')
        tools.click('回收站应用Item more', 'auto_testing_add_Application_001')
        tools.click('回收站应用操作', '还原')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('还原成功')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("回收站")  # 场景名称
    @allure.title("回收站一键清空")  # 用例名称
    @allure.description("应用中心-回收站-一键清空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test032(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = RecycleBin(drivers)
        # 一键清空
        tools.click_menu('应用中心', '回收站')
        tools.click('一键清空')
        tools.click('一键清空确认')
        DomAssert(drivers).assert_att('删除成功')

if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/ApplicationRecycleBin.py'])