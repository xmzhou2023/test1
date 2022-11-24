from libs.common.read_element import Element
from project.TBM.page_object.Center_Component import CenterComponent
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class ForeignBom(CenterComponent):
    """用户类"""

    @allure.step("初始化页面")
    def refresh_webpage_click_menu(self):
        self.refresh_webpage()
        self.click_menu("BOM协作", "外研BOM协作")

    @allure.step("外研BOM协作新增页面-输入BOM信息组合")
    def add_bom_info(self):
        self.click_add()
        self.input_bom_info('制作类型', '客供BOM制作')
        self.input_bom_info('品牌', 'itel')
        self.input_bom_info('机型', 'JMB-01')
        self.input_bom_info('阶段', '量产阶段')
        self.input_bom_info('市场', '埃塞本地')
        self.input_bom_info('模式', '零价值客供')
        self.base_get_img()

    @allure.step("外研BOM协作新增页面-输入BOMtree组合")
    def add_bomtree_info(self):
        self.click_add_bomtree()
        self.input_bomtree('客供BOM', 'BOM状态', '量产')
        self.input_bomtree('客供BOM', '物料编码', '12004871')
        self.input_bomtree('客供BOM', '用量', '1000')
        self.click_add_material()
        self.input_add_material('12004871', '物料编码', '12800002')
        self.input_add_material('12004871', '用量', '1000')
        self.base_get_img()

    @allure.step("新建流程后的后置删除处理")
    def delete_flow(self, code):
        self.recall_process(code)
        self.click_menu("BOM协作", "外研BOM协作")
        self.click_delete(code)
        self.click_dialog_confirm()
        self.assert_toast('删除成功')

    @allure.step("点击应用取消")
    def click_applyCancel(self):
        self.is_click_tbm(user['应用取消'])
        logging.info('点击应用取消')


    @allure.step("业务审核审批页面-流程组合")
    def business_approve_flow(self, code):
        self.assert_my_todo_node(code, '业务审核', True)
        self.enter_oneworks_edit(code)
        self.assert_OneWorks_AgreeFlow()


if __name__ == '__main__':
    pass
