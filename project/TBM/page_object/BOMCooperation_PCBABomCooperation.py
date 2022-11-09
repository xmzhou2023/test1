from time import sleep

from selenium.webdriver import Keys

from libs.common.read_element import Element
from libs.config.conf import BASE_DIR
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

    @allure.step("BOM协作新增页面，输入BOM信息")
    def input_bom_info(self, info, select):
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
        self.input_bom_info('制作类型', 'PCBA BOM制作')
        self.input_bom_info('品牌', 'Infinix')
        self.input_bom_info('机型', 'JMB-01')
        self.input_bom_info('阶段', '试产阶段')

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

    @allure.step("点击新增bom")
    def click_add_material(self):
        self.is_click_tbm(user['新增物料'])
        logging.info('点击新增物料')
        sleep(0.5)

    @allure.step("断言新增bom是否存在")
    def assert_add_bomtree_exist(self, result):
        """断言 新增bom是否存在"""
        DomAssert(self.driver).assert_control(user['新增BomTree'], result=result)

    @allure.step("BomTree信息输入")
    def input_bomtree(self, tree, header, content):
        """
        模版信息根据条件输入内容并且点击
        @param tree:Tree列，或者其他行内唯一的文本
        @param header: BomTree要输入的表头
        @param content:输入的内容
        """
        BomTree_dict = {'BOM状态': '2', '物料编码': '5', '数量': '8', '位号': '9', '替代组': '10', '份额': '11'}
        select_list = ['BOM状态']
        input_list = ['物料编码', '数量', '替代组', '份额', '位号']
        if header in select_list:
            self.is_click_tbm(user['BOMTree填写'], tree, BomTree_dict[header])
            self.is_click_tbm(user['BOMTree输入框选择'], content)
        elif header in input_list:
            self.is_click_tbm(user['BOMTree编辑'], tree)
            self.readonly_input_text(user['BOMTree填写'], content, tree, BomTree_dict[header])
            sleep(1)
            if header == '物料编码':
                self.is_click_tbm(user['物料编码选择'], content)
            self.is_click_tbm(user['BOMTree确定'], tree)
        else:
            logging.info("输入需要操作的表头：('BOM类型','BOM状态','物料编码','用量','替代组','份额',)")

    @allure.step("新增物料输入内容")
    def input_optional_material(self, tree, header, content):
        """
        新增物料后，模版信息根据条件在新增的物料输入内容并且点击
        @param tree:点击新增物料后，需填写位置的上一个物料编码
        @param content:输入的内容
        @param header: BomTree要输入的表头
        """
        BomTree_dict = {'物料编码': '5', '数量': '8', '位号': '9', '替代组': '10', '份额': '11'}
        if header == '物料编码':
            self.is_click_tbm(user['BOMTree新增物料编辑'], tree)
            self.readonly_input_text(user['BOMTree新增物料填写'], content, tree, BomTree_dict[header])
            sleep(1)
            self.is_click_tbm(user['物料编码选择'], content)
            self.is_click_tbm(user['BOMTree新增物料确定'], tree)
        elif header == '数量' or header == '位号' or header == '替代组' or header == '份额':
            self.is_click_tbm(user['BOMTree新增物料编辑'], tree)
            self.readonly_input_text(user['BOMTree新增物料填写'], content, tree, BomTree_dict[header])
            self.is_click_tbm(user['BOMTree新增物料确定'], tree)
        else:
            logging.info("输入需要操作的表头：('BOM类型','BOM状态','物料编码','用量','替代组','份额',)")

    @allure.step("点击一键填写")
    def click_one_press(self):
        self.is_click_tbm(user['BOM信息一键填写'])

    @allure.step("BOM信息一键填写")
    def input_one_press(self, key, value):
        """
        一键填写-根据key选择字段名称，根据value输入字段值
        @param key:字段名称
        @param value:字段值
        """
        self.click_one_press()
        sleep(0.5)
        self.is_click_tbm(user['BOM信息一键填写-字段名称'])
        sleep(0.5)
        self.is_click_tbm(user['BOM信息一键填写-字段名称选择'], key)
        sleep(0.5)
        if key == '数量':
            if value == '':
                self.find_element(user['BOM信息一键填写-字段值默认']).send_keys(Keys.CONTROL + 'a')
                self.find_element(user['BOM信息一键填写-字段值默认']).send_keys(Keys.BACKSPACE)
            self.input_text(user['BOM信息一键填写-字段值默认'], value)
        else:
            if value == '':
                self.find_element(user['BOM信息一键填写-字段值']).send_keys(Keys.CONTROL + 'a')
                self.find_element(user['BOM信息一键填写-字段值']).send_keys(Keys.BACKSPACE)
            self.input_text(user['BOM信息一键填写-字段值'], value)
        sleep(0.5)
        self.is_click_tbm(user['确定'])
        sleep(0.5)

    @allure.step("点击复选框")
    def click_checkbox(self, material='all'):
        """
        TOM Tree根据material点击指定复选框，默认全选
        @param material:物料名，传入BomTree的物料名称；默认‘all’表示点击全选复选框
        """
        if material == 'all':
            self.is_click_tbm(user['复选框全选'])
        else:
            self.is_click_tbm(user['复选框单选'], material)
        sleep(0.5)

    @allure.step("断言：BomTree数据")
    def assert_BomTree_result(self, row, header, content, hearder_type=None):
        column = self.get_table_info(user['BomTree表格字段'], header)
        if hearder_type == 'Tree':
            ac_content = self.element_text(user['BomTree表格指定Tree内容'], row, column)
        else:
            ac_content = self.element_text(user['BomTree表格指定内容'], row, column)
        try:
            assert content in ac_content
            logging.info("断言成功，结果:{}包含指定内容:{}".format(ac_content, content))
        except:
            logging.error("断言失败，结果不包含指定内容")
            raise

    @allure.step("根据Tree点击删除按钮")
    def click_bomtree_delete(self, tree):
        self.is_click_tbm(user['BOMTree删除'], tree)

    @allure.step("点击确定")
    def click_batch_confirm(self):
        self.is_click_tbm(user['确定'])
        logging.info('确定')
        sleep(0.5)

    @allure.step("断言：判断是否存在批量删除")
    def assert_batch_delete(self, result):
        DomAssert(self.driver).assert_control(user['批量删除'], result=result)

    @allure.step("导入-上传文件")
    def upload_import(self, file):
        ele = self.driver.find_element(By.XPATH,
                                       "//div[not(contains(@style,'display: none')) and @class='el-dialog__wrapper']/div/div[2]/div[1]/div/input")
        ele.send_keys(file)
        logging.info('点击导入-上传文件')

    @allure.step("导入BOM-上传正确文件")
    def upload_true_file(self):
        file_path = os.path.join(PEROJECT_PATH, 'TBM', 'data', 'PCBA发起导入模板.xlsx')
        self.upload_import(file_path)
        DomAssert(self.driver).assert_control(user['导入BOM校验结果成功状态'])

    @allure.step("导入BOM-上传错误文件")
    def upload_wrong_file(self):
        file_path = os.path.join(PEROJECT_PATH, 'TBM', 'data', 'worng_file_text.txt')
        self.upload_import(file_path)

    @allure.step("导入BOM-上传错误内容文件")
    def upload_wrongcontent_file(self):
        file_path = os.path.join(PEROJECT_PATH, 'TBM', 'data', 'PCBA发起导入模板错误内容.xlsx')
        self.upload_import(file_path)
        sleep(2)
        DomAssert(self.driver).assert_att('贴片主板_SU385_A1_32GB+2GB_V1.1_自制')
        DomAssert(self.driver).assert_control(user['导入BOM校验结果失败状态'])

    @allure.step("断言导入错误内容后，页面状态是否正确")
    def assert_wrongcontent_upload_result(self):
        try:
            apply = self.find_element(user['导入BOM应用状态'])
            check = self.find_element(user['导入BOM导出校验状态'])
            assert 'is-disabled' in apply.get_attribute('class')
            assert 'is-disabled' not in check.get_attribute('class')
            logging.info('断言成功，导出校验可点击，应用不可点击')
        except:
            self.base_get_img()
            logging.error('断言失败，请检查按钮状态')
            raise

    def get_bomtree_upload_info(self):
        """
        获取导入BOM-结果内容
        """
        info = self.find_elements_tbm(user['导入BOM内容'])
        infolist = []
        for i in info:
            infolist.append(i.text.split('\n'))
        logging.info('获取BOM导入结果{}'.format(infolist))
        return infolist

    @allure.step("断言导入后，页面表格内容是否正确")
    def assert_upload_result(self, *content):
        """
        断言导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            contents = self.get_bomtree_upload_info()
            content_list = []
            for i in contents:
                content_list.append(tuple(i))
            logging.info(content_list)
            assert set(content) <= set(content_list)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            self.base_get_img()
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise

    @allure.step("点击应用")
    def click_apply(self):
        self.is_click_tbm(user['应用'])
        logging.info('点击应用')

    @allure.step("点击展开+图标")
    def click_tree(self, tree):
        """
        点击展开+图标
        :param tree: 物料名称
        """
        self.is_click_tbm(user['展开'], tree)
        logging.info('点击展开')

    def get_bomtree_tree_info(self):
        """
        获取BOMTree所有内容
        """
        info = self.find_elements_tbm(user['BomTree全部内容'])
        infolist = []
        for i in info:
            infolist.append(i.text.split('\n'))
        logging.info('获取BOMTree所有内容{}'.format(infolist))
        return infolist


    @allure.step("断言导入BOM-导入后，页面表格内容是否正确")
    def assert_tree_result(self, *content):
        """
        断言导入BOM-导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            contents = self.get_bomtree_tree_info()
            content_list = []
            for i in contents:
                if len(i) <= 3:
                    continue
                content_list.append(tuple(i))
            assert set(content) <= set(content_list)
            logging.info(content_list)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            self.base_get_img()
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise


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

    @allure.step("点击导入BOM")
    def click_bom_import(self):
        self.is_click_tbm(user['导入BOM'])
        logging.info('点击导入BOM')

    @allure.step("新建流程后的后置删除处理")
    def delete_flow(self, code):
        self.recall_process(code)
        self.click_menu("BOM协作", "PCBA BOM协作")
        self.click_delete(code)
        self.click_delete_confirm()
        self.assert_toast('删除成功')

    @allure.step("断言:页面表格内容是否正确")
    def assert_oneworks_bomtree_result(self, *content):
        """
        断言导入BOM-导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            self.click_tree('PCBA')
            contents = self.get_oneworks_bomtree_info()
            content_list = []
            for i in contents:
                content_list.append(tuple(i))
            assert set(content) <= set(content_list)
            logging.info(content_list)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            self.base_get_img()
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise

    @allure.step("点击附件")
    def click_Accessory(self):
        self.is_click_tbm(user['Oneworks附件'])

    @allure.step("上传附件")
    def send_Accessory(self, name):
        Accessory_path = os.path.join(PEROJECT_PATH, 'TBM', 'data', name)
        self.upload_file(user['Oneworks附件上传'], Accessory_path)
        logging.info('上传附件')

    @allure.step("点击衍生BOM制作需求-新增")
    def click_Derived_add(self):
        self.is_click_tbm(user['衍生BOM制作需求-新增'])
        logging.info('点击衍生BOM制作需求-新增')
        sleep(0.5)

    @allure.step("输入衍生BOM制作需求信息")
    def input_Derived_info(self, header, info, serial=1):
        select_list = ['操作']
        input_list = ['数量', '替代组', '份额', '位号']
        if header in select_list:
            column = self.get_table_info(user['衍生BOM制作需求-操作'])
            self.is_click_tbm(user['衍生BOM制作需求-输入框2'], column, serial, column)
            self.is_click_tbm(user['衍生BOM制作需求-操作选择'], info)
        elif header in input_list:
            column = self.get_table_info(user['衍生BOM制作需求-字段'], header)
            self.input_text(user['衍生BOM制作需求-输入框2'], info, column, serial, column)
        else:
            column = self.get_table_info(user['衍生BOM制作需求-字段'], header)
            self.is_click_tbm(user['衍生BOM制作需求-输入框2'], column, serial, column)
            self.input_text(user['衍生BOM制作需求-输入框2'], info, column, serial, column)
            self.is_click_tbm(user['衍生BOM制作需求-选择'], info)

    @allure.step("删除衍生BOM制作需求信息")
    def delete_Derived_info(self):
        column = self.get_table_info(user['衍生BOM制作需求-操作删除框'])
        self.is_click_tbm(user['衍生BOM制作需求-删除'], column)

    @allure.step("断言：衍生BOM制作需求-暂无数据")
    def assert_Derived_None(self):
        DomAssert(self.driver).assert_control(user['衍生BOM制作需求-暂无数据'])

    @allure.step("断言：生产工厂信息-暂无数据")
    def assert_Factory_None(self):
        DomAssert(self.driver).assert_control(user['生产工厂信息-暂无数据'])

    @allure.step("点击衍生差异")
    def click_Derived_differ(self):
        self.is_click_tbm(user['衍生差异'])
        logging.info('点击衍生差异')
        sleep(0.5)

    @allure.step("点击生成BOM")
    def click_Creat_BOM(self):
        self.is_click_tbm(user['生成BOM'])
        logging.info('点击生成BOM')
        sleep(2)

    @allure.step("点击衍生需求导入")
    def click_Derived_import(self):
        self.is_click_tbm(user['衍生BOM制作需求-导入'])
        logging.info('点击衍生BOM制作需求-导入')

    @allure.step("衍生BOM制作需求-导入-上传正确文件")
    def upload_Derived_file(self, name):
        self.upload_file_tbm(user['衍生BOM制作需求-选择文件'], name)
        DomAssert(self.driver).assert_control(user['应用成功状态'])

    @allure.step("点击生产工厂信息导入")
    def click_Factory_import(self):
        self.is_click_tbm(user['生产工厂信息-导入'])
        logging.info('点击生产工厂信息-导入')

    @allure.step("生产工厂信息-导入-上传正确文件")
    def upload_Factory_file(self, name):
        self.upload_file_tbm(user['生产工厂信息-选择文件'], name)
        DomAssert(self.driver).assert_control(user['应用成功状态'])

    @allure.step("在补充BOM页面，填写信息，点击同意")
    def supplement_bom_flow(self, code):
        self.enter_oneworks_edit(code)
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("在补充工厂页面，填写信息，点击同意")
    def supplementary_factory_flow(self, code):
        self.enter_oneworks_edit(code)
        self.input_oneworks_plant_info('国内贴片工厂', '1051')
        self.click_oneworks_slash()
        self.click_oneworks_plant_check('贴片工厂正确')
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("基带工程师审批页面中，填写信息，点击同意")
    def Structure_flow(self, code):
        self.enter_oneworks_edit(code)
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("采购审核（NPS）审批页面中，填写信息，点击同意")
    def Purchase_flow(self, code):
        self.enter_oneworks_edit(code)
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("在业务审批页面，填写信息，点击同意")
    def business_approve_flow(self, code):
        self.enter_oneworks_edit(code)
        self.click_oneworks_businessapprove_self_inspection('业务类型', '手机')
        self.click_oneworks_businessapprove_self_inspection('检查角色', '检查人')
        self.scroll_oneworks_businessapprove_self_inspection()
        self.input_oneworks_businessapprove_inspection_result()
        self.click_Accessory()
        self.send_Accessory('检查结果.PNG')
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()
if __name__ == '__main__':
    pass
