import allure
import pytest
from project.TLC.page_object.Component_pagetable import ComponentTable
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("组件应用场景") # 模块名称
class TestComponentTable:
    @allure.story("组件-折线图")  # 场景名称
    @allure.title("折线图")  # 用例名称
    @allure.description("组件-折线图")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        tools = ComponentTable(drivers)
        tools.click_menu('组件中心', '我的文件')
        tools.click('空间', '我的空间')
        tools.hover('新增')
        tools.click('新增组件')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'code')
        tools.input('新增输入框', 'auto_testing_add_components_pri_001', 'name')
        tools.click('新增对话框按钮', 'confirm')
        tools.switch_window(1)
        # 拖拽表单
        tools.drag_and_drop_tlc(52, 746, 1011, 463.33)
        # 拖拽日期组件到表单
        tools.drag_and_drop_tlc(195, 746, 1089, 335)
        # 拖拽按钮到表单
        tools.drag_and_drop_tlc(257, 597, 1089, 335)
        # 编辑日期组件
        tools.click('表单内组件选择...', '1')
        tools.click('组件编辑')
        tools.input('输入框', '时间', '名称')
        tools.click('日期属性框关闭按钮')
        # 编辑按钮组件
        tools.click('表单内组件选择...', '2')
        tools.click('组件编辑')
        tools.input('输入框', '查询', '名称')
        tools.click('按钮组件动态代码', '-1')
        tools.click('按钮动态代码输入')
        tools.input_edit(847, 789, 'function click() {')
        tools.input_line(847, 789, "const form = this.getComponentByKey('form')")
        tools.input_line(847, 789, "const table = this.getComponentByKey('line')")
        tools.input_line(847, 789, "table.refresh({param: form.getValue()})")
        tools.input_line(847, 789, '}')
        tools.click('按钮动态代码关闭')
        tools.click('按钮属性框关闭按钮')
        # 拖拽折线图
        tools.drag_and_drop_scroll(290, 729, 1011, 463.33)
        # 折线图属性配置
        tools.click('组件选择1...', '2')
        tools.click('组件编辑')
        tools.input('输入框', '24', '栅格')
        tools.input('输入框', '机型日销量数量', '标题')
        # 数据源配置
        tools.click('数据源配置编辑')
        tools.click('选择API', '-1')
        tools.input('输入框', 'https://pfgateway.transsion.com:9199/data-bff/api-call/page/chnl/sellDetailDly', '请求Url')
        tools.click('请求Method', '-1')
        tools.click('代码编辑点击框', '请求头')
        tools.input_edit(871, 476, '{"appKey":"u/H6m8AJtoVjdZNNKEeUFA=="}')
        tools.click('代码编辑器关闭按钮', '请求头')
        tools.input('输入框', 'data.rows', '结果过滤器')
        tools.click('请求数据')
        tools.click('发送请求')
        tools.scrollr(1910, 500)
        tools.click('横坐标轴', '横坐标轴')
        tools.click('坐标轴选择', 'item')
        tools.scrollr(1910, 500)
        tools.click('纵坐标轴', '3')
        tools.click('坐标轴选择', 'sum_sales_qty')
        tools.click('表格配置关闭按钮')
        tools.click('折线图属性框关闭按钮')
        tools.click('保存')
        # tools.close_switch(1)
        # 删除
        # tools.click_menu('组件中心', '我的文件')
        # tools.click('空间', '我的空间')
        # tools.hover('组件Item')
        # tools.click('组件Item more')
        # tools.click('删除', 'auto_testing_add_components_pri_001')
        # tools.click('删除确认')
        # DomAssert(drivers).assert_page_source('auto_testing_add_components_pri_001')
        pass

if __name__ == '__main__':
    pytest.main(['project/TLC/test_case/Component_pagetable.py'])
