from time import sleep
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

    @allure.step("点击新增")
    def click_add(self):
        self.is_click_tbm(user['新增'])
        sleep(1)

    @allure.step("BOM协作新增页面，输入BOM信息")
    def input_add_bom_info(self, info, select):
        """
        PCBA BOM协作新增页面 - 输入BOM信息
        :param info: 选择要输入的信息
        :param select: 选择信息内容
        """
        if info == '机型':
            self.input_text(user['BOM信息输入框'], select, info)
            sleep(1)
            self.is_click_tbm(user['BOM信息输入框机型选择'], select)
            logging.info('选择点击Bom信息:{}'.format(select))
        elif info == '检查关键器件' or info == '制作虚拟贴片/套片':
            self.is_click_tbm(user['BOM信息选择框'], info)
            sleep(1)
            self.is_click_tbm(user['BOM信息输入框选择'], select)
            logging.info('选择点击Bom信息:{}'.format(select))
        else:
            self.is_click_tbm(user['BOM信息输入框'], info)
            logging.info('点击Bom信息:{}输入框'.format(info))
            sleep(0.5)
            self.scroll_into_view(user['BOM信息输入框选择'], select)
            sleep(1)
            self.is_click_tbm(user['BOM信息输入框选择'], select)
            logging.info('选择点击Bom信息:{}'.format(select))

    @allure.step("PCBA BOM协作新增页面 - 输入BOM信息 组合方法")
    def add_bom_info(self):
        self.click_add()
        self.input_add_bom_info('制作类型', 'PCBA BOM制作')
        self.input_add_bom_info('品牌', 'itel')
        self.input_add_bom_info('机型', 'JMB-01')
        self.input_add_bom_info('阶段', '量产阶段')
        self.input_add_bom_info('制作虚拟贴片/套片', '否')

    @allure.step("点击提交")
    def click_add_submit(self):
        """点击提交"""
        self.scroll_into_view(user['提交'])
        sleep(0.5)
        self.is_click_tbm(user['提交'])

    @allure.step("点击新增bom")
    def click_add_bomtree(self):
        self.is_click_tbm(user['新增BomTree'])
        logging.info('点击新增Bom')
        sleep(0.5)

    @allure.step("断言新增bom是否存在")
    def assert_add_bomtree_exist(self, result):
        """断言 新增bom是否存在"""
        DomAssert(self.driver).assert_control(user['新增BomTree'], result)

    @allure.step("BomTree信息输入")
    def input_bomtree(self, header, content):
        """
        模版信息根据条件输入内容并且点击
        @param content:输入的内容
        @param header: BomTree要输入的表头；{'BOM类型':'2','BOM状态':'3','物料编码':'6','用量':'9','替代组':'10','份额':'11',}
        """
        BomTree_dict = {'BOM状态': '2', '物料编码': '5',
                        '用量': '8', '替代组': '9', '份额': '10', }
        if header == 'BOM状态':
            self.is_click_tbm(user['BOMTree输入框'], BomTree_dict[header])
            sleep(0.5)
            self.is_click_tbm(user['BOMTree输入框选择'], content)
        elif header == '物料编码':
            self.is_click_tbm(user['BOM编辑'])
            self.readonly_input_text(user['BOMTree输入框'], content, choice=BomTree_dict[header])
            sleep(1)
            self.is_click_tbm(user['物料编码选择'], content)
            self.is_click_tbm(user['BOM确定'])
        elif header == '用量' or header == '替代组' or header == '份额':
            try:
                self.is_click_tbm(user['BOM编辑'])
                self.readonly_input_text(user['BOMTree输入框'], content, choice=BomTree_dict[header])
                self.is_click_tbm(user['BOM确定'])
            except:
                self.is_click_tbm(user['BOM编辑'])
                self.readonly_input_text(user['BOMTree输入框'], content,
                                         choice=BomTree_dict[header])
                self.is_click_tbm(user['BOM确定'])
            sleep(0.5)

    @allure.step("审核人设置")
    def select_business_review(self, audit, type='MPM'):
        """
        审核人设置-业务评审-：选择用户
        @param type:选择的类别
        @param audit:输入的用户名
        """
        self.scroll_into_view(user['审核人设置'])
        sleep(0.5)
        self.is_click_tbm(user['审核人类别'], type)
        self.input_text(user['成员列表输入框'], audit)
        sleep(1)
        self.is_click_tbm(user['成员选择'], audit)
        sleep(2)
        self.is_click_tbm(user['成员确定'])

    @allure.step("获取PCBA BOM协作第一列内容")
    def get_info(self):
        """
        @return:返回文本及索引位置分别是'No.'：0; '流程编码':1; '制作类型':2; '机型'：3; '品牌':4; '市场':5; '阶段':6; '单据状态':7; '同步状态':8; '申请人':9; '创建时间':10; '操作':11
        """
        self.click_menu("BOM协作", "PCBA BOM协作")
        sleep(1)
        info = self.find_elements_tbm(user['表格内容'])
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    @allure.step("断言PCBA BOM协作新增成功后，页面表格内容是否正确")
    def assert_add_result(self, *content):
        """
        :param content: 需要，可以一次传入多个
        """
        try:
            contents = self.get_info()
            # content_list = []
            # for i in contents:
            #     content_list.append(i)
            assert set(content) <= set(contents)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise

    def click_delete(self, code):
        """
        根据流程编码点击删除 进行删除操作
        @param code:流程编码
        """
        self.is_click_tbm(user['删除'], code)
        sleep(1)
        self.is_click_tbm(user['确定'])

    @allure.step("点击导入BOM")
    def click_bom_import(self):
        self.is_click_tbm(user['导入BOM'])
        logging.info('点击导入BOM')

    @allure.step("新建流程后的后置删除处理")
    def delete_flow(self, code):
        self.recall_process(code)
        self.click_menu("BOM协作", "PCBA BOM协作")
        self.click_delete(code)
        self.assert_toast('删除成功')


if __name__ == '__main__':
    pass
