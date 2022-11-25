from time import sleep
from libs.common.read_element import Element
from project.TBM.page_object.Center_Component import CenterComponent
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class BareMobilePhoneBomCooperation(CenterComponent):
    """BOM协作_单机头BOM协作"""

    @allure.step("初始化页面")
    def refresh_webpage_click_menu(self):
        self.refresh_webpage()
        self.click_menu("BOM协作", "单机头BOM协作")

    @allure.step("单机头BOM协作新增页面-输入BOM信息组合")
    def add_bom_info(self):
        self.click_add()
        self.input_bom_info('制作类型', '单机头BOM制作')
        self.input_bom_info('品牌', 'itel')
        self.input_bom_info('机型', 'X572-1')
        self.input_bom_info('阶段', '试产阶段')
        self.input_bom_info('市场', '埃塞本地')
        self.input_bom_info('同时做衍生BOM', '否')
        self.base_get_img()

    @allure.step("单机头BOM协作新增组合")
    def add_bom(self):
        self.click_add()
        self.input_bom_info('制作类型', '单机头BOM制作')
        self.input_bom_info('品牌', 'itel')
        self.input_bom_info('机型', 'X572-1')
        self.input_bom_info('阶段', '试产阶段')
        self.input_bom_info('市场', '埃塞本地')
        self.input_bom_info('同时做衍生BOM', '否')
        self.base_get_img()
        self.click_add_bomtree()
        self.input_bomtree('单机头', 'BOM状态', '试产')
        self.input_bomtree('单机头', '物料编码', '12011061')
        self.input_bomtree('单机头', '用量', '1000')
        self.input_bomtree('指纹模组', '物料编码', '12200078')
        self.input_bomtree('指纹模组', '用量', '1000')
        self.select_business_review('李小素')
        self.click_add_submit()
        self.assert_toast('创建流程成功')
        self.refresh()

    @allure.step("新建流程后的后置删除处理")
    def delete_flow(self, code):
        self.recall_process(code)
        self.click_menu("BOM协作", "单机头BOM协作")
        self.click_delete(code)
        self.click_dialog_confirm()
        self.assert_toast('删除成功')

    @allure.step("补充工厂页面-流程组合")
    def supplementary_factory_flow(self, code):
        self.assert_my_todo_node(code, '补充工厂', True)
        self.enter_oneworks_edit(code)
        self.input_oneworks_plant_info('国内组包工厂', '1051')
        self.click_oneworks_slash()
        self.click_oneworks_plant_check('贴片工厂正确')
        self.assert_OneWorks_AgreeFlow()

    @allure.step("结构工程师审批页面-流程组合")
    def framework_engineer_flow(self, code):
        self.assert_my_todo_node(code, '结构工程师审批', True)
        self.enter_oneworks_edit(code)
        self.select_business_review('李小素', 'all')
        self.assert_OneWorks_AgreeFlow()

    @allure.step("业务审核审批页面-流程组合")
    def business_approve_flow(self, code):
        self.assert_my_todo_node(code, '业务审核', True)
        self.enter_oneworks_edit(code)
        self.click_self_inspection('业务类型', '手机')
        self.click_self_inspection('检查角色', '质量部(QPM)')
        self.scroll_self_inspection()
        self.input_self_inspection_result()
        self.assert_OneWorks_AgreeFlow()

    @allure.step("BOM工程师审批页面-流程组合")
    def bom_approve_flow(self, code):
        self.assert_my_todo_node(code, 'BOM工程师审批', True)
        self.enter_oneworks_edit(code)
        self.assert_OneWorks_AgreeFlow()

    def click_oneworks_approval_export(self):
        """
        BOM工程师审批页面 点击导出BOM
        """
        self.is_click_tbm(user['导出BOM'])
        sleep(0.5)
        self.is_click_tbm(user['确定'])

    def get_oneworks_approval_bomtree_info(self):
        """
        BOM工程师审批页面 获取BomTree数据
        """
        self.click_tree('单机头')
        info = self.find_elements_tbm(user['BomTree信息'])
        info_list = []
        for i in info:
            if len(i.text.split('\n')) != 3:
                info_list.append(i.text.split('\n'))
        logging.info('获取Oneworks-BOM工程师审批页面-BOMTree所有内容{}'.format(info_list))
        return info_list

    def assert_oneworks_approval_bominfo(self):
        """
        BOM工程师审批页面 导出的数据和Bom Tree的数据是一致的
        """
        page_info = self.get_oneworks_approval_bomtree_info()
        DomAssert(self.driver).assert_control(user['BomTreeTitle'])
        self.click_BOMTree_checkbox()
        self.click_oneworks_approval_export()
        excel_info = self.read_excel_flow()
        try:
            assert len(excel_info) != 0
            for i in range(1, len(excel_info) + 1):
                assert set(page_info[0][2:3]) <= set(excel_info[i - 1])
                assert set(page_info[i][2:-1]) <= set(excel_info[i - 1])
            logging.info('断言成功，导出的数据和BomTree的数据是一致的')
        except:
            self.base_get_img()
            logging.error('断言成功，导出的数据和BomTree的数据是不一致的')
            raise

    def click_oneworks_factory_export(self):
        """
        补充工厂页面 点击 生产工厂信息-导出
        """
        self.is_click_tbm(user['生产工厂信息-导出'])
        sleep(0.5)

    @allure.step("在补充工厂页面中，获取生产工厂信息数据")
    def get_oneworks_factoryinfo(self):
        state = self.get_element_attribute(user['生产工厂信息明细折叠按钮'], 'class')
        if 'expand' not in state:
            self.is_click_tbm(user['生产工厂信息'])
        DomAssert(self.driver).assert_control(user['生产工厂信息Title'])
        info = self.find_elements_tbm(user['生产工厂信息明细'])
        info_list = []
        for i in info:
            info_list.append(i.text.split('\n'))
        logging.info('获取Oneworks-补充工厂页面-生产工厂信息所有内容{}'.format(info_list))
        return info_list

    @allure.step("导出的生产工厂信息xlsx表的数据和页面的生产工厂信息数据是一致的")
    def assert_oneworks_factoryinfo(self):
        page_info = self.get_oneworks_factoryinfo()
        self.click_oneworks_factory_export()
        excel_info = self.read_excel_flow()
        try:
            assert len(excel_info) != 0
            for i in range(len(excel_info)):
                assert set(page_info[i][2:]) <= set(excel_info[i])
            logging.info('断言成功，导出的数据和生产工厂信息的数据是一致的')
        except:
            self.base_get_img()
            logging.error('断言成功，导出的数据和生产工厂信息的数据是不一致的')
            raise

    @allure.step("子阶BOM检查")
    def bom_check(self, result):
        act_result = self.element_text(user['子阶BOM检查-检查结果'])
        failed = self.element_text(user['子阶BOM检查-检查失败项数'])[6:]
        try:
            assert act_result == result
            try:
                if result == '成功':
                    assert failed == '0'
                elif result == '失败':
                    assert failed != '0'
                logging.info('断言成功，失败项数与实际相符：{}'.format(failed))
            except:
                self.base_get_img()
                logging.error('断言失败，失败项数与实际不符：{}'.format(failed))
                raise
        except:
            logging.error('断言失败，检查结果或失败项数与实际不符；检查结果：{}，失败项数：{}'.format(act_result, failed))
            raise

    @allure.step("点击子阶BOM检查-更多操作")
    def click_more(self):
        self.is_click(user['子阶BOM检查-更多操作'])

    @allure.step("点击子阶BOM检查-更多操作-更新子阶BOM")
    def click_update(self):
        self.is_click(user['子阶BOM检查-更多操作-更新子阶BOM'])

    @allure.step("点击子阶BOM检查-导出")
    def click_oneworks_bomcheck_export(self):
        self.is_click_tbm(user['子阶BOM检查-导出'])

    @allure.step("BOM工程师审批页面 获取子阶BOM检查数据")
    def get_oneworks_approval_bomcheck_info(self):
        info = self.find_elements_tbm(user['子阶BOM检查信息'])
        info_list = []
        for i in info:
            if len(i.text.split('\n')) != 3:
                info_list.append(i.text.split('\n'))
        logging.info('获取Oneworks-BOM工程师审批页面-子阶BOM检查所有内容{}'.format(info_list))
        return info_list

    @allure.step("BOM工程师审批页面 导出的数据和子阶BOM检查的数据是一致的")
    def assert_oneworks_approval_bomcheck(self):
        page_info = self.get_oneworks_approval_bomcheck_info()
        self.click_oneworks_bomcheck_export()
        excel_info = self.read_excel_flow()
        try:
            for i in range(len(excel_info)):
                page_info[i].pop(5)
                assert set(page_info[i]) <= set(excel_info[i])
            logging.info('断言成功，导出的数据和BomTree的数据是一致的')
        except:
            self.base_get_img()
            logging.error('断言成功，导出的数据和BomTree的数据是不一致的')
            raise


if __name__ == '__main__':
    pass
