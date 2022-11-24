from libs.common.read_element import Element
from project.TBM.page_object.Center_Component import CenterComponent
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)


class PCBABomCooperation(CenterComponent):
    """BOM协作_PCBA BOM协作"""

    @allure.step("初始化页面")
    def refresh_webpage_click_menu(self):
        self.refresh_webpage()
        self.click_menu("BOM协作", "PCBA BOM协作")

    @allure.step("PCBA BOM协作新增页面 - 输入BOM信息 组合方法")
    def add_bom_info(self):
        self.click_add()
        self.input_bom_info('制作类型', 'PCBA BOM制作')
        self.input_bom_info('品牌', 'Infinix')
        self.input_bom_info('机型', 'JMB-01')
        self.input_bom_info('阶段', '试产阶段')

    @allure.step("新建流程后的后置删除处理")
    def delete_flow(self, code):
        self.recall_process(code)
        self.click_menu("BOM协作", "PCBA BOM协作")
        self.click_delete(code)
        self.click_dialog_confirm()
        self.assert_toast('删除成功')

    @allure.step("点击附件")
    def click_Accessory(self):
        self.is_click_tbm(user['Oneworks附件'])

    @allure.step("在补充BOM页面，填写信息，点击同意")
    def supplement_bom_flow(self, code):
        self.enter_oneworks_edit(code)
        self.assert_OneWorks_AgreeFlow()

    @allure.step("在补充工厂页面，填写信息，点击同意")
    def supplementary_factory_flow(self, code):
        self.enter_oneworks_edit(code)
        self.input_oneworks_plant_info('国内贴片工厂', '1051')
        self.click_oneworks_slash()
        self.click_oneworks_plant_check('贴片工厂正确')
        self.assert_OneWorks_AgreeFlow()

    @allure.step("基带工程师审批页面中，填写信息，点击同意")
    def Structure_flow(self, code):
        self.enter_oneworks_edit(code)
        self.assert_OneWorks_AgreeFlow()

    @allure.step("采购审核（NPS）审批页面中，填写信息，点击同意")
    def Purchase_flow(self, code):
        self.enter_oneworks_edit(code)
        self.assert_OneWorks_AgreeFlow()

    @allure.step("在业务审批页面，填写信息，点击同意")
    def business_approve_flow(self, code):
        self.enter_oneworks_edit(code)
        self.click_self_inspection('业务类型', '手机')
        self.click_self_inspection('检查角色', '检查人')
        self.scroll_self_inspection()
        self.input_self_inspection_result()
        self.click_Accessory()
        self.add_upload_file('检查结果.PNG')
        self.assert_OneWorks_AgreeFlow()


if __name__ == '__main__':
    pass
