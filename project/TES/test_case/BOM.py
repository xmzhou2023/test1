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
        code = instance.getText('X559')

        # 我的申请
        instance.switch_location('http://bom-sit.transsion.com/#/process/applicant')
        sleep(1)
        instance.refresh()
        # 进入iframe
        instance.switch_iframe('iframe')
        # 视图切换后要好选择一点
        instance.click('oneworks-视图切换')

        instance.click('oneworks-查看详情-var', code)

        # 此时会打开一个新窗口
        instance.switch_window(1)
        instance.click('button', '撤回')
        instance.click('提示-确定撤回')
        instance.close_switch(1)

        instance.switch_location('http://bom-sit.transsion.com/#/archive/list')
        # 刷新一下页面
        instance.click('button', '查询')
        instance.click('删除-var', code)
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
        instance.click('oneworks-查看详情-var', code)
        instance.switch_window(1)
        # 进入iframe
        sleep(2)
        instance.switch_iframe('iframe')
        instance.select_info_input('国内组包工厂', '1051', '105', 'oneworks-dropdown')
        instance.click('button', '一键/')

        instance.select_info_input('检查贴片工厂', '贴片工厂正确', None, 'oneworks-footer-dropdown')

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
        self.create_process2(drivers)

    def create_process2(self, drivers):
        """单机头BOM协作"""
        instance = UserPage(drivers)
        homePage = 'http://bom-sit.transsion.com/#/archive/single-list'
        addPage = 'http://bom-sit.transsion.com/#/single-start-flow/add'
        instance.switch_location(addPage)

    def create_process(self, drivers):
        tHeadDict = {
            "Bom类型": '2',
            "Bom状态": '3',
            "物料编码": '6',
            "用量": '9',
        }
        instance = UserPage(drivers)
        # 直接进入 新增页面
        instance.switch_location('http://bom-sit.transsion.com/#/start-flow/add')

        # __________________________________BOM信息录入_______________________________________________________
        instance.select_info_input('制作类型', '生产BOM')
        instance.select_info_input('品牌', 'Infinix')
        instance.select_info_input('机型', '(X559)X559', 'x559')
        instance.select_info_input('阶段', '试产阶段')
        instance.select_info_input('市场', '孟加拉')

        sleep(1)

        # __________________________________BOM Tree 录入________________________________________
        instance.click('button', '新增Bom')
        instance.select_info_input(tHeadDict["Bom类型"], '国内生产BOM', '', 'tHead-var')
        instance.select_info_input(tHeadDict["Bom状态"], '试产', '', 'tHead-var')
        # 点击编辑按钮
        instance.click('新增Bom-右侧按钮', '编辑')

        sleep(1)
        # 新增BOM 物料编码
        instance.readonly_input_text(tHeadDict["物料编码"], '10000001')
        # 带搜索建议的下拉框需要点一下
        instance.click('dropdown-search-value-var', '10000001')

        # 新增BOM用量
        instance.readonly_input_text(tHeadDict["用量"], '1000')

        # __________________________________________录入结束_______________________________________
        instance.click('新增Bom-右侧按钮', '确定')

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
