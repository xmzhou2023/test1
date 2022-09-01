from time import sleep

from project.TES.page_object.BOM import UserPage

import allure
import pytest

from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("脚本名称") # 模块名称
class TestUtil:
    @allure.story("二级标题") # 场景名称
    @allure.title("三级标题")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        instance = self.create_process(drivers)
        # ____________________________________________撤销流程____________________________________________
        instance.switch_location('http://bom-sit.transsion.com/#/archive/list')
        sleep(2)
        # 获取流程编码
        code = instance.getText('X559', '整机BOM协作')

        # 我的申请
        instance.switch_location('http://bom-sit.transsion.com/#/process/applicant')
        sleep(1)
        instance.refresh()
        # 进入iframe
        instance.switch_iframe('iframe')
        # 视图切换后要好选择一点
        instance.click('oneworks-视图切换')

        instance.click('oneworks-查看详情-by-code', code)

        # 此时会打开一个新窗口
        instance.switch_window(1)
        instance.click('button', '撤回')
        instance.click('提示-确定撤回')
        instance.close_switch(1)

        instance.switch_location('http://bom-sit.transsion.com/#/archive/list')
        # 刷新一下页面
        instance.click('button', '查询')
        instance.click('delete-by-code', code)
        instance.click('提示-确定撤回')
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("二级标题") # 场景名称
    @allure.title("三级标题")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_002(self, drivers):  # 新建流程并审批流程
        instance = self.create_process(drivers)
        # __________________________________审批流程_____________________________________________
        instance.switch_location('http://bom-sit.transsion.com/#/archive/list')
        sleep(2)
        # 获取流程编码
        code = instance.getText('X559')

        # 进入我的代办
        instance.switch_location('http://bom-sit.transsion.com/#/process/holdon')
        sleep(1)
        instance.refresh()
        # 进入iframe
        instance.switch_iframe('iframe')
        # 视图切换
        instance.click('oneworks-视图切换')
        instance.click('oneworks-查看详情-by-code', code)
        instance.switch_window(1)
        # 进入iframe
        sleep(2)
        instance.switch_iframe('iframe')
        instance.select_info_input('oneworks-dropdown', '1051', '国内组包工厂', '105', )
        instance.click('button', '一键/')

        instance.select_info_input('oneworks-footer-dropdown', '贴片工厂正确', '检查贴片工厂')

        instance.frame_exit()
        instance.click('button', '同 意')
        instance.click('确定同意')
        DomAssert(drivers).assert_att('处理成功')
        instance.close_switch(1)
        instance.switch_iframe('iframe')

        instance.click('oneworks-视图切换2')
        for i in range(7):
            sleep(1)
            instance.click("oneworks-刷新按钮")



    @allure.story("二级标题") # 场景名称
    @allure.title("三级标题")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_003(self, drivers):
        instance = self.create_process2(drivers)
        instance.switch_location('http://bom-sit.transsion.com/#/archive/single-list')
        sleep(2)
        # 获取流程编码
        code = instance.getText('X559', '单机头BOM协作')

        # 我的申请
        instance.switch_location('http://bom-sit.transsion.com/#/process/applicant')
        sleep(1)
        instance.refresh()
        # 进入iframe
        instance.switch_iframe('iframe')
        # 视图切换后要好选择一点
        instance.click('oneworks-视图切换')

        instance.click('oneworks-查看详情-by-code', code)

        # 此时会打开一个新窗口
        instance.switch_window(1)
        instance.click('button', '撤回')
        instance.click('提示-确定撤回')
        instance.close_switch(1)

        instance.switch_location('http://bom-sit.transsion.com/#/archive/single-list')
        # 刷新一下页面
        instance.click('button', '查询')
        instance.click('delete-by-code', code)
        instance.click('提示-确定撤回')
        DomAssert(drivers).assert_att('删除成功')

    def create_process2(self, drivers):
        """单机头BOM协作创建流程"""
        tableDict = {
            "Bom状态": '2',
            "物料编码": '5',
            "用量": '8',
        }
        instance = UserPage(drivers)
        homePage = 'http://bom-sit.transsion.com/#/archive/single-list'
        addPage = 'http://bom-sit.transsion.com/#/single-start-flow/add'
        instance.switch_location(addPage)

        # __________________________________BOM信息录入_______________________________________________________
        instance.select_info_input('form-input', '单机头BOM制作', '制作类型')
        instance.select_info_input('form-input', 'Infinix', '品牌', )
        instance.select_info_input('form-input', '(X559)X559', '机型', 'x559')
        instance.select_info_input('form-input', '否', '同时做衍生BOM')
        instance.select_info_input('form-input', '试产阶段', '阶段', )
        instance.select_info_input('form-input', '孟加拉', '市场',)
        sleep(2)


        # __________________________________衍生BOM制作需求________________________________________________
        instance.click('button', '新增Bom')
        instance.select_info_input('单机头-table-form-input', '试产', tableDict["Bom状态"])
        # 点击编辑按钮
        instance.click('单机头-新增Bom-operation-button', '编辑')
        # 新增BOM 物料编码
        instance.readonly_input_text('单机头-table-form-input', '12000001', tableDict["物料编码"])
        # 带搜索建议的下拉框需要点一下
        instance.click('dropdown-search-value', '12000001')

        # 新增BOM用量
        instance.readonly_input_text('单机头-table-form-input', '1000', tableDict["用量"])

        instance.click('单机头-新增Bom-operation-button', '确定')

        # __________________________________________业务评审_______________________________________
        instance.user_selector('MPM', '18645960')

        # ___________________________________________业务审核______________________________________
        instance.user_selector('采购部(NPS)', '18645960')

        # 提交
        instance.click('button', '提交')
        sleep(1)
        DomAssert(drivers).assert_att('创建流程成功')
        return instance

    def create_process(self, drivers):
        tableDict = {
            "Bom类型": '2',
            "Bom状态": '3',
            "物料编码": '6',
            "用量": '9',
        }
        instance = UserPage(drivers)
        # 直接进入 新增页面
        instance.switch_location('http://bom-sit.transsion.com/#/start-flow/add')

        # __________________________________BOM信息录入_______________________________________________________
        instance.select_info_input('form-input', '生产BOM', '制作类型', )
        instance.select_info_input('form-input', 'Infinix', '品牌', )
        instance.select_info_input('form-input', '(X559)X559', '机型',  'x559')
        instance.select_info_input('form-input', '试产阶段', '阶段', )
        instance.select_info_input('form-input', '孟加拉', '市场', )

        sleep(1)

        # __________________________________BOM Tree 录入________________________________________
        instance.click('button', '新增Bom')
        instance.select_info_input('table-form-input', '国内生产BOM', tableDict["Bom类型"])
        instance.select_info_input('table-form-input', '试产', tableDict["Bom状态"])
        # 点击编辑按钮
        instance.click('新增Bom-operation-button', '编辑')


        sleep(1)
        # 新增BOM 物料编码
        instance.readonly_input_text('table-form-input', '10000001', tableDict["物料编码"])
        # 带搜索建议的下拉框需要点一下
        instance.click('dropdown-search-value', '10000001')

        # 新增BOM用量
        instance.readonly_input_text('table-form-input', '1000', tableDict["用量"])

        # __________________________________________录入结束_______________________________________
        instance.click('新增Bom-operation-button', '确定')

        # __________________________________________业务评审_______________________________________
        instance.user_selector('MPM', '18645960')

        # ___________________________________________业务审核______________________________________
        instance.user_selector('采购部', '18645960')

        # 提交
        instance.click('button', '提交')
        sleep(1)
        DomAssert(drivers).assert_att('创建流程成功')
        return instance

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
