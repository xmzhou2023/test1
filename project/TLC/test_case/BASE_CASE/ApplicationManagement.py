import allure
import pytest
from project.TLC.page_object.ApplicationManagement import Application
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
    @allure.story("应用管理")  # 场景名称
    @allure.title("新增应用成功")  # 用例名称
    @allure.description("应用中心-应用管理界面新增应用")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test014(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Application(drivers)
        # 新增组件
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
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用管理")  # 场景名称
    @allure.title("新增应用弹框取消操作")  # 用例名称
    @allure.description("应用中心-应用管理界面新增应用弹框,操作取消按钮,新增应用取消")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test015(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Application(drivers)
        # 新增组件
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用code')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用名称')
        tools.input('textarea输入框', 'auto_testing_add_Application_001', '应用描述')
        # 取消弹框
        tools.click('新增对话框按钮', 'cancel')

    @allure.story("应用管理")  # 场景名称
    @allure.title("新增应用弹框关闭操作")  # 用例名称
    @allure.description("应用中心-应用管理界面新增应用弹框,操作关闭按钮,新增弹框关闭")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test016(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Application(drivers)
        # 新增组件
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用code')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用名称')
        tools.input('textarea输入框', 'auto_testing_add_Application_001', '应用描述')
        # 关闭弹框
        tools.click('弹框X', '新建应用')

    @allure.story("应用管理")  # 场景名称
    @allure.title("应用code重复性校验")  # 用例名称
    @allure.description("应用中心-应用管理界面新增应用后,再新增相同code的应用,应用code不能重复,新增失败")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test017(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Application(drivers)
        # 新增组件
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用code')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用名称')
        tools.input('textarea输入框', 'auto_testing_add_Application_001', '应用描述')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'icon')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'cover')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('应用添加成功')
        # 新增重复code组件
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用code')
        DomAssert(drivers).assert_att('编码不能重复')
        # 关闭弹框
        tools.click('新增对话框按钮', 'cancel')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用管理")  # 场景名称
    @allure.title("应用code必填项")  # 用例名称
    @allure.description("应用中心-应用管理界面新增应用弹框不输入code,点击确认")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test018(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Application(drivers)
        # 新增组件
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', '', '应用code')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用名称')
        tools.input('textarea输入框', 'auto_testing_add_Application_001', '应用描述')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'icon')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'cover')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('请输入应用code')
        # 关闭弹框
        tools.click('新增对话框按钮', 'cancel')

    @allure.story("应用管理")  # 场景名称
    @allure.title("应用名称必填项")  # 用例名称
    @allure.description("应用中心-应用管理界面新增应用弹框不输入名称,点击确认")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test019(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Application(drivers)
        # 新增组件
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用code')
        tools.input('input输入框', '', '应用名称')
        tools.input('textarea输入框', 'auto_testing_add_Application_001', '应用描述')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'icon')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'cover')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('请输入应用名称')
        # 关闭弹框
        tools.click('新增对话框按钮', 'cancel')

    @allure.story("应用管理")  # 场景名称
    @allure.title("应用图标必填项")  # 用例名称
    @allure.description("应用中心-应用管理界面新增应用弹框不输入图标,点击确认")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test020(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Application(drivers)
        # 新增组件
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用code')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用名称')
        tools.input('textarea输入框', 'auto_testing_add_Application_001', '应用描述')
        # tools.upload('图片上传', '', 'icon')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'cover')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('请选择应用图标')
        # 关闭弹框
        tools.click('新增对话框按钮', 'cancel')

    @allure.story("应用管理")  # 场景名称
    @allure.title("应用封面必填项")  # 用例名称
    @allure.description("应用中心-应用管理界面新增应用弹框不输入封面,点击确认")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test021(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Application(drivers)
        # 新增组件
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用code')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用名称')
        tools.input('textarea输入框', 'auto_testing_add_Application_001', '应用描述')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'icon')
        # tools.upload('图片上传', '', 'cover')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('请选择应用封面')
        # 关闭弹框
        tools.click('新增对话框按钮', 'cancel')

    @allure.story("应用管理")  # 场景名称
    @allure.title("编辑应用成功")  # 用例名称
    @allure.description("应用中心-应用管理界面编辑应用信息")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test022(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Application(drivers)
        # 新增组件
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用code')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用名称')
        tools.input('textarea输入框', 'auto_testing_add_Application_001', '应用描述')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'icon')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'cover')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('应用添加成功')
        # 编辑应用
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '修改')
        tools.input('input输入框', 'auto_testing_edit_Application', '应用名称')
        tools.input('textarea输入框', 'auto_testing_edit_Application', '应用描述')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'icon')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'cover')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('auto_testing_edit_Application')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_edit_Application')
        tools.click('应用Item more', 'auto_testing_edit_Application')
        tools.click('应用操作', '删除')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用管理")  # 场景名称
    @allure.title("应用管理界面查询-正例")  # 用例名称
    @allure.description("应用中心-应用管理界面查询应用条件正确,数据匹配正确")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test023(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Application(drivers)
        # 新增组件
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用code')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用名称')
        tools.input('textarea输入框', 'auto_testing_add_Application_001', '应用描述')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'icon')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'cover')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('应用添加成功')
        # 应用查询
        tools.click('漏斗')
        tools.input('条件查询输入框', 'auto_testing_add_Application_001', '名称')
        tools.input('条件查询输入框', 'auto_testing_add_Application_001', '编码')
        tools.click('条件查询输入框', '状态')
        tools.click('状态选择', '2')
        tools.click('查询框按钮', '确定')
        DomAssert(drivers).assert_att('auto_testing_add_Application_001')
        # 重置
        tools.click('漏斗')
        tools.click('查询框按钮', '重置')
        tools.click('查询框按钮', '确定')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用管理")  # 场景名称
    @allure.title("应用管理界面查询-反例")  # 用例名称
    @allure.description("应用中心-应用管理界面查询应用条件错误,没有数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test024(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Application(drivers)
        # 新增组件
        tools.click_menu('应用中心', '应用管理')
        tools.click('新增')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用code')
        tools.input('input输入框', 'auto_testing_add_Application_001', '应用名称')
        tools.input('textarea输入框', 'auto_testing_add_Application_001', '应用描述')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'icon')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'cover')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('应用添加成功')
        # 应用查询
        tools.click('漏斗')
        tools.input('条件查询输入框', 'auto_testing_add_Application_001', '名称')
        tools.input('条件查询输入框', 'auto_testing_add_Application_001', '编码')
        tools.click('条件查询输入框', '状态')
        tools.click('状态选择', '1')
        tools.click('查询框按钮', '确定')
        DomAssert(drivers).assert_page_source('auto_testing_add_Application_001')
        # 重置
        tools.click('漏斗')
        tools.click('查询框按钮', '重置')
        tools.click('查询框按钮', '确定')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('删除确认')
        DomAssert(drivers).assert_att('删除成功')

if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/ApplicationManagement.py'])