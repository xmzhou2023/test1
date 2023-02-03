import allure
import pytest
from project.TLC.page_object.ApplicationPermission import Permission
from public.base.assert_ui import DomAssert, ValueAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("应用中心-权限管理") # 模块名称
class Teststory_1181:
    @allure.story("权限管理")  # 场景名称
    @allure.title("授权应用成功")  # 用例名称
    @allure.description("权限管理添加角色,授权成员授权应用,授权成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test025(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Permission(drivers)
        # 我的空间-组件发布
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.switch_window_tlc(1)
        tools.click('发布')
        tools.click('确定', '发布组件')
        DomAssert(drivers).assert_att('发布成功')
        tools.close_switch_tlc(1)
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
        # 添加应用菜单
        tools.click('应用Item', 'auto_testing_add_Application_001')
        tools.click('菜单添加+')
        tools.input('input输入框', 'auto_testing_add_Application_menu_001', '菜单名称')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('菜单添加成功')
        # 发布应用
        tools.click('应用配置header按钮', '发布')
        tools.click('确定', '发布应用')
        DomAssert(drivers).assert_att('发布成功')
        # 新增角色
        tools.click_menu('应用中心', '权限配置')
        tools.click('角色添加+')
        tools.input('input输入框', 'auto_testing_role_001', '角色名称')
        tools.click('确定', '新增角色')
        DomAssert(drivers).assert_att('新增成功')
        # 关联成员
        tools.click('角色tab切换', '成员管理')
        tools.click('权限类型添加按钮', '新增成员')
        tools.input('人员列表输入框', '18647503')
        tools.click('选择人员', '18647503')
        tools.click('确定', '人员列表')
        DomAssert(drivers).assert_att('添加成功')
        # 授权应用
        tools.click('角色tab切换', '权限管理')
        tools.click('权限类型添加按钮', '新增')
        tools.click('输入框选择', '2')
        tools.click('应用/版本选择', 'auto_testing_add_Application_001')
        tools.click('输入框选择', '3')
        tools.click('应用/版本选择', 'V1.0')
        tools.click('操作按钮', '1')
        DomAssert(drivers).assert_att('保存成功')
        # 删除角色
        tools.click_menu('应用中心', '权限配置')
        tools.hover('角色树', 'auto_testing_role_001')
        tools.click('角色删除', 'auto_testing_role_001')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')
        # 删除应用
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')
        # 删除组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('提示框确认')

    @allure.story("权限管理")  # 场景名称
    @allure.title("新增用户-删除用户")  # 用例名称
    @allure.description("权限管理添加角色,添加用户,删除用户")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test026(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Permission(drivers)
        # 新增角色
        tools.click_menu('应用中心', '权限配置')
        tools.click('角色添加+')
        tools.input('input输入框', 'auto_testing_role_001', '角色名称')
        tools.click('确定', '新增角色')
        DomAssert(drivers).assert_att('新增成功')
        # 关联成员
        tools.click('角色tab切换', '成员管理')
        tools.click('权限类型添加按钮', '新增成员')
        tools.input('人员列表输入框', '18647503')
        tools.click('选择人员', '18647503')
        tools.click('确定', '人员列表')
        DomAssert(drivers).assert_att('添加成功')
        # 删除用户
        tools.click('成员删除按钮')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')
        # 删除角色
        tools.click_menu('应用中心', '权限配置')
        tools.hover('角色树', 'auto_testing_role_001')
        tools.click('角色删除', 'auto_testing_role_001')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("权限管理")  # 场景名称
    @allure.title("角色编辑")  # 用例名称
    @allure.description("权限管理添加角色,编辑角色")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test027(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Permission(drivers)
        # 新增角色
        tools.click_menu('应用中心', '权限配置')
        tools.click('角色添加+')
        tools.input('input输入框', 'auto_testing_role_001', '角色名称')
        tools.click('确定', '新增角色')
        DomAssert(drivers).assert_att('新增成功')
        # 编辑角色
        tools.double_click('角色树', 'auto_testing_role_001')
        tools.input('角色编辑输入框', 'auto_testing_editrole_001')
        tools.click('编辑确认')
        DomAssert(drivers).assert_att('编辑成功')
        # 删除角色
        tools.click_menu('应用中心', '权限配置')
        tools.hover('角色树', 'auto_testing_editrole_001')
        tools.click('角色删除', 'auto_testing_editrole_001')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("权限管理")  # 场景名称
    @allure.title("新增用户-删除授权应用")  # 用例名称
    @allure.description("权限管理添加角色,授权应用,删除应用")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test028(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Permission(drivers)
        # 我的空间-组件发布
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.switch_window_tlc(1)
        tools.click('发布')
        tools.click('确定', '发布组件')
        DomAssert(drivers).assert_att('发布成功')
        tools.close_switch_tlc(1)
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
        # 添加应用菜单
        tools.click('应用Item', 'auto_testing_add_Application_001')
        tools.click('菜单添加+')
        tools.input('input输入框', 'auto_testing_add_Application_menu_001', '菜单名称')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('菜单添加成功')
        # 发布应用
        tools.click('应用配置header按钮', '发布')
        tools.click('确定', '发布应用')
        DomAssert(drivers).assert_att('发布成功')
        # 新增角色
        tools.click_menu('应用中心', '权限配置')
        tools.click('角色添加+')
        tools.input('input输入框', 'auto_testing_role_001', '角色名称')
        tools.click('确定', '新增角色')
        DomAssert(drivers).assert_att('新增成功')
        # 授权应用
        tools.click('角色tab切换', '权限管理')
        tools.click('权限类型添加按钮', '新增')
        tools.click('输入框选择', '2')
        tools.click('应用/版本选择', 'auto_testing_add_Application_001')
        tools.click('输入框选择', '3')
        tools.click('应用/版本选择', 'V1.0')
        tools.click('操作按钮', '1')
        DomAssert(drivers).assert_att('保存成功')
        # 取消应用授权
        tools.click('操作按钮', '2')
        tools.click('提示框确认')
        # 删除应用
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')
        # 删除角色
        tools.click_menu('应用中心', '权限配置')
        tools.hover('角色树', 'auto_testing_role_001')
        tools.click('角色删除', 'auto_testing_role_001')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')
        # 删除组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('提示框确认')


if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/ApplicationPermission.py'])