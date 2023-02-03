import allure
import pytest
from project.TLC.page_object.ApplicationConfiguration import Configuration
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
    @allure.story("应用配置")  # 场景名称
    @allure.title("添加应用菜单")  # 用例名称
    @allure.description("应用菜单添加成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Configuration(drivers)
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
        tools.click('添加+')
        tools.input('input输入框', 'auto_testing_add_Application_menu_001', '菜单名称')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('菜单添加成功')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001' )
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用配置")  # 场景名称
    @allure.title("菜单名称必填校验")  # 用例名称
    @allure.description("新增菜单,新增弹框不输入名称,点击确认,菜单不能为空")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Configuration(drivers)
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
        tools.click('添加+')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('请输入菜单名称')
        tools.click('弹框X', '添加菜单')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用配置")  # 场景名称
    @allure.title("菜单编辑校验")  # 用例名称
    @allure.description("新增菜单成功,编辑菜单名称,编辑成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Configuration(drivers)
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
        tools.click('添加+')
        tools.input('input输入框', 'auto_testing_add_Application_menu_001', '菜单名称')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('菜单添加成功')
        # 编辑菜单名称
        tools.double_click('树结构', 'auto_testing_add_Application_menu_001')
        tools.input('菜单编辑输入框', 'auto_testing_edit_Application_menu_001')
        tools.click('编辑确认')
        DomAssert(drivers).assert_att('编辑成功')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用配置")  # 场景名称
    @allure.title("菜单删除校验")  # 用例名称
    @allure.description("新增菜单成功,删除菜单成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Configuration(drivers)
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
        tools.click('添加+')
        tools.input('input输入框', 'auto_testing_add_Application_menu_001', '菜单名称')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('菜单添加成功')
        # 删除菜单
        tools.hover('树结构', 'auto_testing_add_Application_menu_001')
        tools.click('菜单删除', 'auto_testing_add_Application_menu_001')
        tools.click('确定', '删除菜单')
        DomAssert(drivers).assert_att('删除成功')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用配置")  # 场景名称
    @allure.title("应用菜单-外部链接类型")  # 用例名称
    @allure.description("应用菜单选择外部链接类型")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Configuration(drivers)
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
        # 添加应用菜单
        tools.click('应用Item', 'auto_testing_add_Application_001')
        tools.click('添加+')
        tools.input('input输入框', 'auto_testing_add_Application_menu_001', '菜单名称')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('菜单添加成功')
        # 菜单配置
        tools.click('菜单类型', '1')
        tools.input('input输入框', 'https://www.baidu.com/', 'url')
        tools.upload('图片上传', 'D:/autopic/op.jpg', 'menuIcon')
        # 提交配置
        tools.click('菜单配置按钮', '1')
        DomAssert(drivers).assert_att('配置成功')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用配置")  # 场景名称
    @allure.title("应用菜单-组件类型")  # 用例名称
    @allure.description("应用菜单选择组件类型")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test006(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Configuration(drivers)
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
        tools.click('添加+')
        tools.input('input输入框', 'auto_testing_add_Application_menu_001', '菜单名称')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('菜单添加成功')
        # 菜单配置
        tools.click('菜单类型', '2')
        tools.click('组件选择hover')
        tools.click('组件选择', 'auto_testing_add_components_pri_001')
        tools.click('组件版本选择')
        # 提交配置
        tools.click('菜单配置按钮', '1')
        DomAssert(drivers).assert_att('配置成功')
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
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用配置")  # 场景名称
    @allure.title("应用发布校验")  # 用例名称
    @allure.description("新增应用,应用配置界面发布应用")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test007(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Configuration(drivers)
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
        tools.click('添加+')
        tools.input('input输入框', 'auto_testing_add_Application_menu_001', '菜单名称')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('菜单添加成功')
        # 发布应用
        tools.click('应用配置header按钮', '发布')
        tools.click('确定', '发布应用')
        DomAssert(drivers).assert_att('发布成功')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用配置")  # 场景名称
    @allure.title("应用预览校验")  # 用例名称
    @allure.description("新增应用,应用配置界面预览应用")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test008(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Configuration(drivers)
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
        tools.click('添加+')
        tools.input('input输入框', 'auto_testing_add_Application_menu_001', '菜单名称')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('菜单添加成功')
        # 预览应用
        tools.click('应用配置header按钮', '预览')
        DomAssert(drivers).assert_att('auto_testing_add_Application_menu_001')
        tools.close_switch_tlc(1)
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用配置")  # 场景名称
    @allure.title("应用预览校验")  # 用例名称
    @allure.description("新增应用,应用配置界面预览应用")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test009(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Configuration(drivers)
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
        tools.click('添加+')
        tools.input('input输入框', 'auto_testing_add_Application_menu_001', '菜单名称')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('菜单添加成功')
        # 预览应用
        tools.click('应用配置header按钮', '预览')
        DomAssert(drivers).assert_att('auto_testing_add_Application_menu_001')
        tools.close_switch_tlc(1)
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用配置")  # 场景名称
    @allure.title("应用分享-URL较验")  # 用例名称
    @allure.description("新增应用,应用配置界面分享应用,操作URL方式")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test010(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Configuration(drivers)
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
        tools.click('添加+')
        tools.input('input输入框', 'auto_testing_add_Application_menu_001', '菜单名称')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('菜单添加成功')
        # 预览应用
        tools.click('应用配置header按钮', '分享')
        tools.click('复制链接')
        DomAssert(drivers).assert_att('复制成功')
        tools.click('弹框X', '链接分享')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用配置")  # 场景名称
    @allure.title("应用分享-分享成员较验")  # 用例名称
    @allure.description("新增应用,应用配置界面分享应用,操作分享成员方式")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test011(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Configuration(drivers)
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
        tools.click('添加+')
        tools.input('input输入框', 'auto_testing_add_Application_menu_001', '菜单名称')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('菜单添加成功')
        # 分享应用
        tools.click('应用配置header按钮', '分享')
        tools.click('分享人员添加')
        tools.input('人员列表输入框', '18647503')
        tools.click('选择人员', '18647503')
        tools.click('确定', '人员列表')
        DomAssert(drivers).assert_att('分享成功')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用配置")  # 场景名称
    @allure.title("应用历史版本查看")  # 用例名称
    @allure.description("新增应用,应用配置界面历史版本查看")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test012(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Configuration(drivers)
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
        tools.click('添加+')
        tools.input('input输入框', 'auto_testing_add_Application_menu_001', '菜单名称')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('菜单添加成功')
        # 预览应用
        tools.click('应用配置header按钮', '历史版本')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("应用配置")  # 场景名称
    @allure.title("应用历史版本回退")  # 用例名称
    @allure.description("新增应用,应用配置界面操作历史版本,历史版本界面回退")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test013(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Configuration(drivers)
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
        tools.click('添加+')
        tools.input('input输入框', 'auto_testing_add_Application_menu_001', '菜单名称')
        tools.click('新增对话框按钮', 'confirm')
        DomAssert(drivers).assert_att('菜单添加成功')
        # 预览应用
        tools.click('应用配置header按钮', '历史版本')
        tools.click('回退记录', '创建了应用')
        tools.click('回退')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('回退成功')
        # 删除
        tools.click_menu('应用中心', '应用管理')
        tools.hover('应用Item', 'auto_testing_add_Application_001')
        tools.click('应用Item more', 'auto_testing_add_Application_001')
        tools.click('应用操作', '删除')
        tools.click('提示框确认')
        DomAssert(drivers).assert_att('删除成功')

if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/ApplicationConfiguration.py'])