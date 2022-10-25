import allure
import pytest
from project.TLC.page_object.Cooperation import Cooperater
from public.base.assert_ui import DomAssert, ValueAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("协作者") # 模块名称
class Testcooperator:
    @allure.story("添加协作者")  # 场景名称
    @allure.title("组件添加协作者-编辑者权限")  # 用例名称
    @allure.description("组件添加协作者,授权编辑者权限")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Cooperater(drivers)
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 组件协作者菜单操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.click('添加协作者')
        # 成员添加弹框操作
        tools.click('成员添加选择框', '2')
        tools.click('角色选择', '编辑者')
        tools.click('成员添加选择框', '1')
        # 人员列表弹框操作
        tools.input('人员列表输入框', 'jieruzhao001')
        tools.click('选择人员', 'jieruzhao001')
        tools.click('人员列表确认')
        # 添加编辑者
        tools.click('成员添加按钮', 'confirm')
        DomAssert(drivers).assert_att('添加成功')
        # 查看协作者
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.value_assert('协作成员页面', '赵婕如001', result=True)
        tools.click('协作成员页面', '完成')
        # 切换协作者登录
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        DomAssert(drivers).assert_att('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass

    @allure.story("添加协作者")  # 场景名称
    @allure.title("组件添加协作者-阅读者权限")  # 用例名称
    @allure.description("组件添加协作者,授权阅读者权限")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Cooperater(drivers)
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 组件协作者菜单操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.click('添加协作者')
        # 成员添加弹框操作
        tools.click('成员添加选择框', '2')
        tools.click('角色选择', '阅读者')
        tools.click('成员添加选择框', '1')
        # 人员列表弹框操作
        tools.input('人员列表输入框', 'jieruzhao001')
        tools.click('选择人员', 'jieruzhao001')
        tools.click('人员列表确认')
        # 添加编辑者
        tools.click('成员添加按钮', 'confirm')
        DomAssert(drivers).assert_att('添加成功')
        # 查看协作者
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.value_assert('协作成员页面', '赵婕如001', result=True)
        tools.click('协作成员页面', '完成')
        # 切换协作者登录
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        DomAssert(drivers).assert_att('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass

    @allure.story("协作者权限变更")  # 场景名称
    @allure.title("协作者权限编辑者更改为阅读者")  # 用例名称
    @allure.description("组件添加协作者授权为编辑者后,更改权限为阅读者")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Cooperater(drivers)
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 组件协作者菜单操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.click('添加协作者')
        # 成员添加弹框操作
        tools.click('成员添加选择框', '2')
        tools.click('角色选择', '编辑者')
        tools.click('成员添加选择框', '1')
        # 人员列表弹框操作
        tools.input('人员列表输入框', 'jieruzhao001')
        tools.click('选择人员', 'jieruzhao001')
        tools.click('人员列表确认')
        # 添加编辑者
        tools.click('成员添加按钮', 'confirm')
        DomAssert(drivers).assert_att('添加成功')
        # 切换协作者
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        # 编辑者操作权限校验
        tools.click('组件Item')
        tools.switch_window(1)
        tools = Cooperater(drivers)
        tools.value_assert('加锁按钮', result=True)
        tools.close_switch(1)
        # 切换创建者登录
        tools.relogin('18647503')
        # 编辑者权限更改为阅读者
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.click('协作成员角色点击')
        tools.click('协作成员角色切换', '可阅读')
        tools.click('协作成员页面', '完成')
        # 切换协作者
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        # 阅读者操作权限校验
        tools.click('组件Item')
        tools.switch_window(1)
        tools.value_assert('加锁按钮', result=False)
        tools.close_switch(1)
        # 切换创建者登录
        tools.relogin('18647503')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass

    @allure.story("协作者权限变更")  # 场景名称
    @allure.title("协作者权限阅读者更改为编辑者")  # 用例名称
    @allure.description("组件添加协作者授权为阅读者后,更改权限为编辑者")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Cooperater(drivers)
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 组件协作者菜单操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.click('添加协作者')
        # 成员添加弹框操作
        tools.click('成员添加选择框', '2')
        tools.click('角色选择', '阅读者')
        tools.click('成员添加选择框', '1')
        # 人员列表弹框操作
        tools.input('人员列表输入框', 'jieruzhao001')
        tools.click('选择人员', 'jieruzhao001')
        tools.click('人员列表确认')
        # 添加编辑者
        tools.click('成员添加按钮', 'confirm')
        DomAssert(drivers).assert_att('添加成功')
        # 切换协作者
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        # 编辑者操作权限校验
        tools.click('组件Item')
        tools.switch_window(1)
        tools = Cooperater(drivers)
        tools.value_assert('加锁按钮', result=False)
        tools.close_switch(1)
        # 切换创建者登录
        tools.relogin('18647503')
        # 编辑者权限更改为阅读者
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.click('协作成员角色点击')
        tools.click('协作成员角色切换', '可编辑')
        tools.click('协作成员页面', '完成')
        # 切换协作者
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        # 阅读者操作权限校验
        tools.click('组件Item')
        tools.switch_window(1)
        tools.value_assert('加锁按钮', result=True)
        tools.close_switch(1)
        # 切换创建者登录
        tools.relogin('18647503')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass

    @allure.story("组件删除-与我协作界面")  # 场景名称
    @allure.title("组件添加协作者-删除组件")  # 用例名称
    @allure.description("组件添加协作者,删除组件,协作者权限被收回")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Cooperater(drivers)
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 组件协作者菜单操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.click('添加协作者')
        # 成员添加弹框操作
        tools.click('成员添加选择框', '2')
        tools.click('角色选择', '编辑者')
        tools.click('成员添加选择框', '1')
        # 人员列表弹框操作
        tools.input('人员列表输入框', 'jieruzhao001')
        tools.click('选择人员', 'jieruzhao001')
        tools.click('人员列表确认')
        # 添加编辑者
        tools.click('成员添加按钮', 'confirm')
        DomAssert(drivers).assert_att('添加成功')
        # 切换协作者登录
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        DomAssert(drivers).assert_att('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 组件删除协作者与我协作页面校验
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        pass

    @allure.story("组件删除-与我协作界面")  # 场景名称
    @allure.title("组件添加协作者-删除组件后还原组件")  # 用例名称
    @allure.description("组件添加协作者,删除组件,协作者权限被收回,还原组件,删除还原的组件没有协作权限")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Cooperater(drivers)
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 组件协作者菜单操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.click('添加协作者')
        # 成员添加弹框操作
        tools.click('成员添加选择框', '2')
        tools.click('角色选择', '编辑者')
        tools.click('成员添加选择框', '1')
        # 人员列表弹框操作
        tools.input('人员列表输入框', 'jieruzhao001')
        tools.click('选择人员', 'jieruzhao001')
        tools.click('人员列表确认')
        # 添加编辑者
        tools.click('成员添加按钮', 'confirm')
        DomAssert(drivers).assert_att('添加成功')
        # 切换协作者登录
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        DomAssert(drivers).assert_att('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 组件删除协作者与我协作页面校验
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 切换创建者账号,还原组件
        tools.relogin('18647503')
        tools.click_menu('组件中心', '回收站')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('还原', 'auto_testing_add_components_pri_001')
        tools.click('还原确定')
        # 切换协作者校验与我协作页面,删除后还原的组件,没有协作权限
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass

    @allure.story("组件删除-我的收藏界面")  # 场景名称
    @allure.title("协作者收藏组件-组件删除")  # 用例名称
    @allure.description("组件添加协作者,协作者添加收藏,删除组件后,协作者收藏界面无取消协作的组件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_004_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Cooperater(drivers)
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 组件协作者菜单操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.click('添加协作者')
        # 成员添加弹框操作
        tools.click('成员添加选择框', '2')
        tools.click('角色选择', '编辑者')
        tools.click('成员添加选择框', '1')
        # 人员列表弹框操作
        tools.input('人员列表输入框', 'jieruzhao001')
        tools.click('选择人员', 'jieruzhao001')
        tools.click('人员列表确认')
        # 添加编辑者
        tools.click('成员添加按钮', 'confirm')
        DomAssert(drivers).assert_att('添加成功')
        # 切换协作者登录
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('收藏', 'auto_testing_add_components_pri_001')
        tools.click_menu('组件中心', '我的收藏')
        DomAssert(drivers).assert_att('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 组件删除协作者与我协作页面校验
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '我的收藏')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        pass

    @allure.story("组件删除-我的收藏界面")  # 场景名称
    @allure.title("协作者收藏组件-组件删除后还原")  # 用例名称
    @allure.description("组件添加协作者,协作者添加收藏,删除组件后还原,协作者收藏界面无取消协作的组件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_004_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Cooperater(drivers)
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 组件协作者菜单操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.click('添加协作者')
        # 成员添加弹框操作
        tools.click('成员添加选择框', '2')
        tools.click('角色选择', '编辑者')
        tools.click('成员添加选择框', '1')
        # 人员列表弹框操作
        tools.input('人员列表输入框', 'jieruzhao001')
        tools.click('选择人员', 'jieruzhao001')
        tools.click('人员列表确认')
        # 添加编辑者
        tools.click('成员添加按钮', 'confirm')
        DomAssert(drivers).assert_att('添加成功')
        # 切换协作者登录
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('收藏', 'auto_testing_add_components_pri_001')
        tools.click_menu('组件中心', '我的收藏')
        DomAssert(drivers).assert_att('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 组件删除协作者我的收藏界面校验
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '我的收藏')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 切换创建者账号,还原组件
        tools.relogin('18647503')
        tools.click_menu('组件中心', '回收站')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('还原', 'auto_testing_add_components_pri_001')
        tools.click('还原确定')
        # 切换协作者校验与我协作页面,删除后还原的组件,没有协作权限
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '我的收藏')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass

    @allure.story("删除协作者")  # 场景名称
    @allure.title("删除协助者-编辑者权限")  # 用例名称
    @allure.description("组件添加协作者,删除协助者-编辑者")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_005_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Cooperater(drivers)
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 组件协作者菜单操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.click('添加协作者')
        # 成员添加弹框操作
        tools.click('成员添加选择框', '2')
        tools.click('角色选择', '编辑者')
        tools.click('成员添加选择框', '1')
        # 人员列表弹框操作
        tools.input('人员列表输入框', 'jieruzhao001')
        tools.click('选择人员', 'jieruzhao001')
        tools.click('人员列表确认')
        # 添加编辑者
        tools.click('成员添加按钮', 'confirm')
        DomAssert(drivers).assert_att('添加成功')
        # 切换协作者登录
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        DomAssert(drivers).assert_att('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        # 取消协助者权限
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.hover('协作成员页面', '赵婕如001')
        tools.hover('移除图标')
        tools.click('移除图标')
        DomAssert(drivers).assert_att('移除成功')
        tools.click('协作成员页面', '完成')
        # 切换协作者
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass

    @allure.story("删除协作者")  # 场景名称
    @allure.title("删除协助者-阅读者权限")  # 用例名称
    @allure.description("组件添加协作者,删除协助者-阅读者")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_005_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Cooperater(drivers)
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 组件协作者菜单操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.click('添加协作者')
        # 成员添加弹框操作
        tools.click('成员添加选择框', '2')
        tools.click('角色选择', '阅读者')
        tools.click('成员添加选择框', '1')
        # 人员列表弹框操作
        tools.input('人员列表输入框', 'jieruzhao001')
        tools.click('选择人员', 'jieruzhao001')
        tools.click('人员列表确认')
        # 添加编辑者
        tools.click('成员添加按钮', 'confirm')
        DomAssert(drivers).assert_att('添加成功')
        # 切换协作者登录
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        DomAssert(drivers).assert_att('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        # 取消协助者权限
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.hover('协作成员页面', '赵婕如001')
        tools.hover('移除图标')
        tools.click('移除图标')
        DomAssert(drivers).assert_att('移除成功')
        tools.click('协作成员页面', '完成')
        # 切换协作者
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass

    @allure.story("与我协作界面-组件查询")  # 场景名称
    @allure.title("组件查询_正例")  # 用例名称
    @allure.description("与我协作输入存在的组件,可以匹配到组件")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_006_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Cooperater(drivers)
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 组件协作者菜单操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.click('添加协作者')
        # 成员添加弹框操作
        tools.click('成员添加选择框', '2')
        tools.click('角色选择', '编辑者')
        tools.click('成员添加选择框', '1')
        # 人员列表弹框操作
        tools.input('人员列表输入框', 'jieruzhao001')
        tools.click('选择人员', 'jieruzhao001')
        tools.click('人员列表确认')
        # 添加编辑者
        tools.click('成员添加按钮', 'confirm')
        DomAssert(drivers).assert_att('添加成功')
        # 切换协作者登录
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        # 顶部搜索
        tools.hover('顶部搜索框')
        tools.readonly_input('顶部搜索框', 'auto_testing_add_components', 'query')
        DomAssert(drivers).assert_att('auto_testing_add_components_pri_001')
        # 切换创建者登录
        tools.relogin('18647503')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass

    @allure.story("与我协作界面-组件查询")  # 场景名称
    @allure.title("组件查询_反例")  # 用例名称
    @allure.description("与我协作在顶部输入框中输入不存在的组件名称，搜索框下拉结果显示无数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_006_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = Cooperater(drivers)
        # 新增组件
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增Button', 'confirm')
        tools.close_switch(1)
        DomAssert(drivers).assert_att('新增成功')
        # 组件协作者菜单操作
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('协作', 'auto_testing_add_components_pri_001')
        tools.click('添加协作者')
        # 成员添加弹框操作
        tools.click('成员添加选择框', '2')
        tools.click('角色选择', '编辑者')
        tools.click('成员添加选择框', '1')
        # 人员列表弹框操作
        tools.input('人员列表输入框', 'jieruzhao001')
        tools.click('选择人员', 'jieruzhao001')
        tools.click('人员列表确认')
        # 添加编辑者
        tools.click('成员添加按钮', 'confirm')
        DomAssert(drivers).assert_att('添加成功')
        # 切换协作者登录
        tools.relogin('jieruzhao001')
        tools.click_menu('组件中心', '与我协作')
        # 顶部搜索
        tools.hover('顶部搜索框')
        tools.readonly_input('顶部搜索框', 'auto_testing_add_components111111111', 'query')
        DomAssert(drivers).assert_att('无数据')
        # 切换创建者登录
        tools.relogin('18647503')
        # 删除
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('组件Item')
        tools.click('组件Item more')
        tools.click('删除', 'auto_testing_add_components_pri_001')
        tools.click('删除确认')
        DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass



if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/Cooperation.py'])