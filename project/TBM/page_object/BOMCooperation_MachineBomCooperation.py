import os
from time import sleep
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import logging
from libs.common.read_element import Element
from libs.config.conf import BASE_DIR
from project.TBM.api.api import APIRequest
from public.base.assert_ui import DomAssert
from project.TBM.page_object.home import HomePage
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class MachineBOMCollaboration(HomePage, APIRequest):
    """BOM协作_整机BOM协作"""

    @allure.step("初始化页面")
    def refresh_webpage(self):
        self.refresh()
        self.driver.switch_to.default_content()
        handles = self.driver.window_handles
        logging.info('当前窗口：{}'.format(handles))
        if len(handles) != 1:
            for i in range(1, len(handles)):
                self.close_switch(1)
        else:
            self.switch_window(0)

    def refresh_webpage_click_menu(self):
        self.refresh_webpage()
        self.click_menu("BOM协作", "整机BOM协作")

    def click_machine_bom_cooperation_add(self):
        """点击新增"""
        self.is_click_tbm(user['新增'])
        sleep(1)

    def input_machine_bom_cooperation_add_bom_info(self, info, select):
        """
        整机BOM协作新增页面 - 输入BOM信息
        :param info: 选择要输入的信息
        :param select: 选择信息内容
        """
        if info == '机型':
            self.input_text(user['BOM信息输入框'], select, info)
            sleep(1)
            self.is_click_tbm(user['BOM信息输入框机型选择'], select)
            logging.info('选择点击Bom信息:{}'.format(select))
        else:
            self.is_click_tbm(user['BOM信息输入框'], info)
            logging.info('点击Bom信息:{}输入框'.format(info))
            self.scroll_into_view(user['BOM信息输入框选择'], select)
            sleep(1)
            self.is_click_tbm(user['BOM信息输入框选择'], select)
            logging.info('选择点击Bom信息:{}'.format(select))

    @allure.step("机BOM协作新增页面 - 输入BOM信息 组合方法")
    def machine_bom_cooperation_add_bom_info(self):
        self.click_machine_bom_cooperation_add()
        self.input_machine_bom_cooperation_add_bom_info('制作类型', '生产BOM')
        self.input_machine_bom_cooperation_add_bom_info('品牌', 'Infinix')
        self.input_machine_bom_cooperation_add_bom_info('机型', 'X572-1')
        self.input_machine_bom_cooperation_add_bom_info('阶段', '试产阶段')
        self.input_machine_bom_cooperation_add_bom_info('市场', '埃塞本地')

    def click_machine_bom_cooperation_add_submit(self):
        """点击提交"""
        self.scroll_into_view(user['提交'])
        sleep(0.5)
        self.is_click_tbm(user['提交'])

    def click_machine_bom_cooperation_close(self):
        """关闭"""
        try:
            self.is_click_tbm(user['关闭'])
            logging.info('关闭当前页')
        except:
            pass

    def click_machine_bom_cooperation_add_bomtree(self):
        """点击新增bom"""
        self.is_click_tbm(user['新增BomTree'])
        logging.info('点击新增Bom')

    def input_machine_bom_cooperation_bomtree(self, header, content):
        """
        模版信息根据条件输入内容并且点击
        @param content:输入的内容
        @param header: BomTree要输入的表头；{'BOM类型':'2','BOM状态':'3','物料编码':'6','用量':'9','替代组':'10','份额':'11',}
        """
        BomTree_dict = {'BOM类型': '2', 'BOM状态': '3', '物料编码': '6',
                        '用量': '9', '替代组': '10', '份额': '11', }
        if header == 'BOM类型' or header == 'BOM状态':
            self.is_click_tbm(user['BOMTree输入框'], BomTree_dict[header])
            self.is_click_tbm(user['BOMTree输入框选择'], content)
        elif header == '物料编码':
            self.is_click_tbm(user['BOM编辑'])
            self.readonly_input_text(user['BOMTree输入框'], content, choice=BomTree_dict[header])
            sleep(1)
            self.is_click_tbm(user['物料编码选择'], content)
        elif header == '用量' or header == '替代组' or header == '份额':
            self.is_click_tbm(user['BOM编辑'])
            self.readonly_input_text(user['BOMTree输入框'], content, choice=BomTree_dict[header])
            self.is_click_tbm(user['BOM确定'])

    @allure.step("整机BOM协作新增页面 - 输入BOMTree 组合方法")
    def machine_bom_cooperation_add_bomtree(self):
        self.click_machine_bom_cooperation_add_bomtree()
        self.input_machine_bom_cooperation_bomtree('BOM类型', '国内生产BOM')
        self.input_machine_bom_cooperation_bomtree('BOM状态', '试产')
        self.input_machine_bom_cooperation_bomtree('物料编码', '10018955')
        self.input_machine_bom_cooperation_bomtree('用量', '1000')

    def select_machine_bom_cooperation_business_review_mpm(self, audit):
        """
        审核人设置-业务评审-MPM：选择MPM用户
        @param audit:输入的用户名
        """
        self.scroll_into_view(user['审核人设置'])
        sleep(0.5)
        self.is_click_tbm(user['MPM'])
        self.input_text(user['成员列表输入框'], audit)
        sleep(1)
        self.is_click_tbm(user['成员选择'], audit)
        self.is_click_tbm(user['成员确定'])

    def select_machine_bom_cooperation_business_audit_nps(self, audit):
        """
        审核人设置-业务审核-采购部（NPS）：选择审核用户
        @param audit:输入的用户名
        """
        self.is_click_tbm(user['采购部(NPS)'])
        self.input_text(user['成员列表输入框'], audit)
        sleep(1)
        self.is_click_tbm(user['成员选择'], audit)
        self.is_click_tbm(user['成员确定'])

    def get_machine_bom_cooperation_info(self):
        """
        获取整机BOM协作第一列内容
        @return:返回文本及索引位置分别是'No.'：0; '流程编码':1; '制作类型':2; '机型'：3; '品牌':4; '市场':5; '阶段':6; '单据状态':7; '同步状态':8; '申请人':9; '创建时间':10; '操作':11
        """
        self.click_menu("BOM协作", "整机BOM协作")
        sleep(1)
        info = self.find_elements(user['表格内容'])
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    def get_machine_bom_cooperation_assigned_info(self, code):
        """
        获取整机BOM协作第一列内容
        @return:返回文本及索引位置分别是'No.'：0; '流程编码':1; '制作类型':2; '机型'：3; '品牌':4; '市场':5; '阶段':6; '单据状态':7; '同步状态':8; '申请人':9; '创建时间':10; '操作':11
        """
        self.click_menu("BOM协作", "整机BOM协作")
        sleep(1)
        info = self.find_elements(user['表格指定编码内容'], code)
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    def assert_machine_bom_cooperation_add_result(self, *content):
        """
        断言整机BOM协作新增成功后，页面表格内容是否正确
        :param content: 需要，可以一次传入多个
        """
        try:
            contents = self.get_machine_bom_cooperation_info()
            # content_list = []
            # for i in contents:
            #     content_list.append(i)
            assert set(content) <= set(contents)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise

    def input_machine_bom_cooperation_optional_bomtree(self, tree, header, content):
        """
        BomTree信息根据Tree在指定列表输入内容
        @param tree:输入选择
        @param header: BomTree要输入的表头；【BOM类型， BOM状态， 物料编码， 用量， 替代组， 份额】
        @param content:输入的内容
        """
        if header == '物料编码':
            self.is_click_tbm(user['BOMTree编辑'], tree)
            self.readonly_input_text(user['BOMTree物料编码'], content, tree)
            sleep(1)
            self.is_click_tbm(user['物料编码选择'], content)
            self.is_click_tbm(user['BOMTree确定'], tree)
        elif header == '用量':
            self.is_click_tbm(user['BOMTree编辑'], tree)
            try:
                self.readonly_input_text(user['BOMTree用量'], content, tree)
            except:
                self.is_click_tbm(user['BOMTree编辑'], tree)
                self.readonly_input_text(user['BOMTree用量'], content, tree)
            self.is_click_tbm(user['BOMTree确定'], tree)
        elif header == '替代组':
            self.is_click_tbm(user['BOMTree编辑'], tree)
            self.readonly_input_text(user['BOMTree替代组'], content, tree)
            self.is_click_tbm(user['BOMTree确定'], tree)
        elif header == '份额':
            self.is_click_tbm(user['BOMTree编辑'], tree)
            self.readonly_input_text(user['BOMTree份额'], content, tree)
            self.is_click_tbm(user['BOMTree确定'], tree)
        else:
            logging.info("输入需要操作的表头：('BOM类型','BOM状态','物料编码','用量','替代组','份额',)")

    def machine_bom_cooperation_optional_bomtree(self):
        self.input_machine_bom_cooperation_optional_bomtree('充电器', '物料编码', '10000011')
        self.input_machine_bom_cooperation_optional_bomtree('充电器', '用量', '1000')
        self.input_machine_bom_cooperation_optional_bomtree('充电器', '替代组', 'A1')
        self.input_machine_bom_cooperation_optional_bomtree('充电器', '份额', '20')
        self.click_machine_bom_cooperation_optional_material()
        self.move_to_add_material('10000011')
        self.input_machine_bom_cooperation_optional_material('10000011', '物料编码', '10000012')
        self.input_machine_bom_cooperation_optional_material('10000011', '用量', '1000')
        self.input_machine_bom_cooperation_optional_material('10000011', '替代组', 'A1')
        self.input_machine_bom_cooperation_optional_material('10000011', '份额', '20')

    def click_machine_bom_cooperation_optional_material(self):
        """
        点击新增物料
        """
        self.is_click_tbm(user['新增物料'])
        logging.info('点击新增物料')

    def move_to_add_material(self, tree):
        """
        新增物料后，根据上级物料 点击新增加的物料列进行对焦
        """
        self.is_click_tbm(user['BOMTree新增物料对焦'], tree)

    def input_machine_bom_cooperation_optional_material(self, tree, header, content):
        """
        模版信息根据条件输入内容并且点击
        @param content:输入的内容
        @param header: BomTree要输入的表头；{'BOM类型':'2','BOM状态':'3','物料编码':'6','用量':'9','替代组':'10','份额':'11',}
        @param tree:同级物料
        """
        if header == '物料编码':
            self.is_click_tbm(user['BOMTree新增物料编辑'], tree)
            self.readonly_input_text(user['BOMTree新增物料物料编码'], content, tree)
            sleep(1)
            self.is_click_tbm(user['物料编码选择'], content)
            self.is_click_tbm(user['BOMTree新增物料确定'], tree)
        elif header == '用量':
            self.is_click_tbm(user['BOMTree新增物料编辑'], tree)
            self.readonly_input_text(user['BOMTree新增物料用量'], content, tree)
            self.is_click_tbm(user['BOMTree新增物料确定'], tree)
        elif header == '替代组':
            self.is_click_tbm(user['BOMTree新增物料编辑'], tree)
            self.readonly_input_text(user['BOMTree新增物料替代组'], content, tree)
            self.is_click_tbm(user['BOMTree新增物料确定'], tree)
        elif header == '份额':
            self.is_click_tbm(user['BOMTree新增物料编辑'], tree)
            self.readonly_input_text(user['BOMTree新增物料份额'], content, tree)
            self.is_click_tbm(user['BOMTree新增物料确定'], tree)
        else:
            logging.info("输入需要操作的表头：('BOM类型','BOM状态','物料编码','用量','替代组','份额')")

    def recall_machine_bom_cooperation_process(self, code):
        """
        提交流程申请后，在待办列表-我申请的 根据流程编码对流程进行撤回操作
        @param code:流程编码
        """
        self.enter_machine_bom_cooperation_my_application()
        try:
            self.is_click_tbm(user['待办列表-我申请的-查看详情'], code)
        except:
            self.refresh()
            self.is_click_tbm(user['待办列表-我申请的-查看详情'], code)
        self.switch_window(1)
        self.refresh()
        try:
            self.is_click_tbm(user['撤回'])
            self.is_click_tbm(user['撤回确定'])
        except:
            self.base_get_img()
            self.refresh()
            self.is_click_tbm(user['撤回'])
            self.is_click_tbm(user['撤回确定'])
        self.quit_machine_bom_cooperation_onework()
        # self.quite_iframe()
        # self.switch_window(0)
        # # self.is_click_tbm(user['关闭我申请的'])
        # self.refresh()
        # self.quite_iframe()
        self.click_menu("BOM协作", "整机BOM协作")

    def click_machine_bom_cooperation_delete(self, code):
        """
        根据流程编码点击删除 进行删除操作
        @param code:流程编码
        """
        self.is_click_tbm(user['删除'], code)
        self.is_click_tbm(user['确定'])

    def click_machine_bom_cooperation_one_press(self):
        """
        点击一键填写
        """
        self.is_click_tbm(user['BOM信息一键填写'])

    def input_machine_bom_cooperation_one_press(self, key, value):
        """
        一键填写-根据key选择字段名称，根据value输入字段值
        @param key:字段名称
        @param value:字段值
        """
        self.click_machine_bom_cooperation_one_press()
        sleep(0.5)
        self.is_click_tbm(user['BOM信息一键填写-字段名称'])
        self.is_click_tbm(user['BOM信息一键填写-字段名称选择'], key)
        if key == '用量':
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

    def click_machine_bom_cooperation_one_press_cancel(self):
        """
        点击取消
        """
        self.is_click_tbm(user['BOM信息一键填写取消'])
        logging.info('点击取消')

    def get_machine_bom_cooperation_bomtree_info(self, material):
        """
        获取整机BOM协作-BOMTREE指定列内容
        @param material:物料名
        @return:返回文本及索引位置分别是  0:'No.'; 1:'BOM类型'; 2:'BOM状态'; 3:'Tree'; 4:'复选框'; 5:'物料编码';
                                    6:'物料描述'; 7:'物料属性'; 8:'用量'; 9:'替代组'; 10:'份额'; 11:'操作'
        """
        info = self.find_elements(user['BomTree内容'], material)
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    def click_machine_bom_cooperation_checkbox(self, material='all'):
        """
        TOM Tree根据material点击指定复选框，默认全选
        @param material:物料名，传入BomTree的物料名称；默认‘all’表示点击全选复选框
        """
        if material == 'all':
            self.is_click_tbm(user['复选框全选'])
        else:
            self.is_click_tbm(user['复选框单选'], material)

    def assert_machine_bom_cooperation_batch_delete(self, result):
        """
        断言：判断是否存在批量删除
        """
        try:
            ac_result = self.element_exist(user['批量删除'])
            assert ac_result is result
            logging.info('断言成功')
        except:
            self.base_get_img()
            logging.error('断言失败')
            raise

    def click_machine_bom_cooperation_batch_delete(self):
        """
        点击批量删除
        """
        self.is_click_tbm(user['批量删除'])
        logging.info('点击批量删除')

    def click_machine_bom_cooperation_batch_confirm(self):
        """
        点击确定
        """
        self.is_click_tbm(user['确定'])
        logging.info('确定')

    def click_machine_bom_cooperation_simple_import(self):
        """
        点击简易导入
        """
        self.is_click_tbm(user['简易导入'])
        logging.info('点击导入-简易模式')

    def upload_machine_bom_cooperation_import(self, file):
        """
        导入-上传文件
        """
        ele = self.driver.find_element(By.XPATH,
                                       "//div[not(contains(@style,'display: none')) and @class='el-dialog__wrapper']/div/div[2]/div[1]/div/input")
        ele.send_keys(file)
        logging.info('点击导入-上传文件')

    def simple_upload_machine_bom_cooperation_wrong_file(self):
        """
        简易导入-上传文件
        """
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', 'worng_file_text.txt')
        self.upload_machine_bom_cooperation_import(path)

    def simple_upload_machine_bom_cooperation_true_file(self):
        """
        简易导入-上传文件
        """
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', '生产BOM项目经理简易模式导入.xls')
        self.upload_machine_bom_cooperation_import(path)

    def simple_upload_machine_bom_cooperation_wrongcontent_file(self):
        """
        简易导入-上传文件
        """
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', '生产BOM项目经理简易模式导入错误内容.xls')
        self.upload_machine_bom_cooperation_import(path)
        sleep(2)

    def assert_machine_bom_cooperation_wrongcontent_simple_upload_result(self):
        """
        断言导入错误内容后，页面状态是否正确
        """
        try:
            apply = self.find_element(user['应用状态'])
            check = self.find_element(user['导出校验状态'])
            assert 'is-disabled' in apply.get_attribute('class')
            assert 'is-disabled' not in check.get_attribute('class')
            logging.info('断言成功，导出校验可点击，应用不可点击')
        except:
            self.base_get_img()
            logging.error('断言失败，请检查按钮状态')
            raise

    def assert_machine_bom_cooperation_wrongcontent_upload_result(self):
        """
        断言导入错误内容后，页面状态是否正确
        """
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

    def get_machine_bom_cooperation_bomtree_simple_upload_info(self):
        """
        获取导入BOM-结果内容
        """
        info = self.find_elements(user['简易导入内容'])
        infolist = []
        for i in info:
            infolist.append(i.text.split('\n'))
        logging.info('获取BOM导入结果{}'.format(infolist))
        return infolist

    def assert_machine_bom_cooperation_simple_upload_result(self, *content):
        """
        断言导入BOM-简易导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            contents = self.get_machine_bom_cooperation_bomtree_simple_upload_info()
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

    def click_machine_bom_cooperation_apply(self):
        """
        点击应用
        """
        self.is_click_tbm(user['应用'])
        logging.info('点击应用')
        sleep(1)

    def click_machine_bom_cooperation_tree(self, tree):
        """
        点击展开+图标
        :param tree: 物料名称
        """
        self.is_click_tbm(user['展开'], tree)
        logging.info('点击展开')

    def get_machine_bom_cooperation_bomtree_tree_info(self):
        """
        获取BOMTree所有内容
        """
        info = self.find_elements(user['BomTree全部内容'])
        infolist = []
        for i in info:
            infolist.append(i.text.split('\n'))
        logging.info('获取BOMTree所有内容{}'.format(infolist))
        return infolist

    def assert_machine_bom_cooperation_tree_result(self, *content):
        """
        断言导入BOM-简易导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            contents = self.get_machine_bom_cooperation_bomtree_tree_info()
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

    def click_machine_bom_cooperation_bom_import(self):
        """
        点击导入BOM
        """
        self.is_click_tbm(user['导入BOM'])
        logging.info('点击导入BOM')

    def upload_machine_bom_cooperation_wrong_file(self):
        """
        导入BOM-上传文件
        """
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', 'worng_file_text.txt')
        self.upload_machine_bom_cooperation_import(path)

    def upload_machine_bom_cooperation_true_file(self):
        """
        导入BOM-上传文件
        """
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', '生产bom项目经理导入模板.xlsx')
        self.upload_machine_bom_cooperation_import(path)

    def upload_machine_bom_cooperation_wrongcontent_file(self):
        """
        导入BOM-上传文件
        """
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', '生产bom项目经理导入模板错误内容.xlsx')
        self.upload_machine_bom_cooperation_import(path)
        sleep(2)

    def get_machine_bom_cooperation_bomtree_upload_info(self):
        """
        获取导入BOM-结果内容
        """
        info = self.find_elements(user['导入BOM内容'])
        infolist = []
        for i in info:
            infolist.append(i.text.split('\n'))
        logging.info('获取BOM导入结果{}'.format(infolist))
        return infolist

    def assert_machine_bom_cooperation_upload_result(self, *content):
        """
        断言导入BOM-简易导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            contents = self.get_machine_bom_cooperation_bomtree_upload_info()
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

    def delete_machine_bom_cooperation_flow(self, process_code):
        """
        新建流程后的后置删除处理
        """
        self.recall_machine_bom_cooperation_process(process_code)
        self.click_machine_bom_cooperation_delete(process_code)
        DomAssert(self.driver).assert_att('删除成功')

    def api_delete_machine_bom_cooperation_flow(self, instanceid, flowid):
        """
        通过调用接口发起撤回流程
        调用接口：oneworks流程撤回接口，整机BOM协作删除已撤回接口
        @param instanceid:oneworks撤回流程编码
        @param flowid:流程ID
        """
        self.tbm_machine_bom_cooperation_recall_flow(instanceid, flowid)

    def add_machine_bom_cooperation_flow(self):
        """
        发起流程
        点击新增，输入BOM信息，输入BOMTree信息后点击提交
        """
        self.click_machine_bom_cooperation_add()
        self.input_machine_bom_cooperation_add_bom_info('制作类型', '生产BOM')
        self.input_machine_bom_cooperation_add_bom_info('品牌', 'itel')
        self.input_machine_bom_cooperation_add_bom_info('机型', 'X572-1')
        self.input_machine_bom_cooperation_add_bom_info('阶段', '试产阶段')
        self.input_machine_bom_cooperation_add_bom_info('市场', '埃塞本地')
        self.click_machine_bom_cooperation_add_bomtree()
        self.input_machine_bom_cooperation_bomtree('BOM类型', '国内生产BOM')
        self.input_machine_bom_cooperation_bomtree('BOM状态', '试产')
        self.input_machine_bom_cooperation_bomtree('物料编码', '10018956')
        self.input_machine_bom_cooperation_bomtree('用量', '1000')
        self.select_machine_bom_cooperation_business_review_mpm('李小素')
        self.select_machine_bom_cooperation_business_audit_nps('李小素')
        self.click_machine_bom_cooperation_add_submit()
        sleep(1)
        DomAssert(self.driver).assert_att('创建流程成功')

    def api_add_machine_bom_cooperation_flow(self):
        """
        通过调用接口发起新增流程
        返回流程编码，instanceId
        """
        return self.tbm_machine_bom_cooperation_add_flow()

    def machine_bom_cooperation_supplementary_factory_flow(self, code):
        """
        在补充工厂页面，填写信息，点击同意
        """
        self.enter_machine_bom_cooperation_onework_edit(code)
        self.input_machine_bom_cooperation_oneworks_plant_info('国内组包工厂', '1051')
        self.click_machine_bom_cooperation_oneworks_slash()
        self.click_machine_bom_cooperation_oneworks_plant_check('贴片工厂正确')
        self.click_machine_bom_cooperation_oneworks_agree()
        self.click_machine_bom_cooperation_oneworks_confirm()
        DomAssert(self.driver).assert_att('处理成功，审核通过')
        self.quit_machine_bom_cooperation_onework()

    def machine_bom_cooperation_engineer_approve_flow(self, code):
        """
        在BOM工程师审批页面，填写信息，点击同意
        """
        self.enter_machine_bom_cooperation_onework_edit(code)
        self.click_machine_bom_cooperation_oneworks_agree()
        self.click_machine_bom_cooperation_oneworks_confirm()
        DomAssert(self.driver).assert_att('处理成功，审核通过')
        self.quit_machine_bom_cooperation_onework()

    def machine_bom_cooperation_business_approve_flow(self, code):
        """
        在业务审批页面，填写信息，点击同意
        """
        self.enter_machine_bom_cooperation_onework_edit(code)
        self.click_machine_bom_cooperation_oneworks_businessapprove_self_inspection('业务类型', '手机')
        self.click_machine_bom_cooperation_oneworks_businessapprove_self_inspection('检查角色', '音频')
        self.scroll_machine_bom_cooperation_oneworks_businessapprove_self_inspection()
        self.input_machine_bom_cooperation_oneworks_businessapprove_inspection_result()
        self.click_machine_bom_cooperation_oneworks_agree()
        self.click_machine_bom_cooperation_oneworks_confirm()
        DomAssert(self.driver).assert_att('处理成功，审核通过')
        self.quit_machine_bom_cooperation_onework()

    def click_machine_bom_cooperation_check(self, code):
        """
        根据流程编码点击查看 进行查看操作
        @param code:流程编码
        """
        self.is_click_tbm(user['查看'], code)

    def enter_machine_bom_cooperation_onework_check(self, code):
        """
        进入oneworks查看流程页面
        """
        sleep(1)
        self.click_machine_bom_cooperation_check(code)
        self.switch_window(1)
        sleep(1)
        iframe = self.find_element(user['待办列表-我申请的-iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(1)

    def quit_machine_bom_cooperation_onework(self):
        """
        退出oneworks查看流程页面
        """
        self.quite_iframe()
        self.close_switch(1)
        self.refresh()
        self.quite_iframe()
        sleep(1)

    def enter_machine_bom_cooperation_my_todo(self):
        """
        进入我的待办页面
        """
        ele = self.element_text(user['当前菜单']).strip()
        if ele == '我的待办':
            self.refresh()
            iframe = self.find_element(user['待办列表-我申请的-iframe'])
            self.driver.switch_to.frame(iframe)
            sleep(3)
            self.is_click_tbm(user['待办列表-刷新'])
        else:
            self.click_menu('待办列表', '我的待办')
            self.refresh()
            iframe = self.find_element(user['待办列表-我申请的-iframe'])
            self.driver.switch_to.frame(iframe)
            sleep(3)
            self.is_click_tbm(user['待办列表-刷新'])

    def enter_machine_bom_cooperation_my_application(self):
        """
        进入我申请的页面
        """
        self.click_menu('待办列表', '我申请的')
        self.refresh()
        iframe = self.find_element(user['待办列表-我申请的-iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(1)

    def quit_machine_bom_cooperation_my_todo(self):
        """
        退出我的待办页面框架
        """
        self.quite_iframe()

    def assert_machine_bom_cooperation_my_todo_node(self, code, node, exist=False):
        """
        我的待办页面-断言：成功处理了流程后，我的待办中存在/不存在该条单据在指定审核节点
        @param code:流程编码
        @param node:节点名称
        @param exist:断言存在或者不存在
        """
        self.enter_machine_bom_cooperation_my_todo()
        actual_node = self.element_text(user['待办列表-我的待办-当前节点'], code)
        if exist is False:
            try:
                assert actual_node != node
                logging.info('断言成功，我的待办中该条单据不存在:{}节点，实际在:{}节点'.format(node, actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我的待办中存在该条单据在:{}审核节点'.format(actual_node))
                raise
            finally:
                self.quite_iframe()
        else:
            try:
                assert actual_node == node
                logging.info('断言成功，我的待办中存在该条单据在:{}审核节点'.format(actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我的待办中该条单据不存在:{}节点，实际在:{}节点'.format(node, actual_node))
                raise
            finally:
                self.quite_iframe()

    def assert_machine_bom_cooperation_my_application_node(self, code, node, exist=False):
        """
        我申请的页面-断言：成功处理了流程后，我申请的中存在/不存在该条单据在指定审核节点
        @param code:流程编码
        @param node:节点名称
        @param exist:断言存在或者不存在
        """
        self.enter_machine_bom_cooperation_my_application()
        actual_node = self.element_text(user['待办列表-我申请的-当前节点'], code)
        if exist is False:
            try:
                assert actual_node != node
                logging.info('断言成功，我申请的中该条单据不存在:{}节点，实际在:{}节点'.format(node, actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中存在该条单据在:{}节点'.format(actual_node))
                raise
            finally:
                self.quite_iframe()
        else:
            try:
                assert actual_node == node
                logging.info('断言成功，我申请的中存在该条单据在:{}审核节点'.format(actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中不存在该条单据在:{}审核节点'.format(actual_node))
                raise
            finally:
                self.quite_iframe()

    def assert_machine_bom_cooperation_my_application_flow(self, code, flow, exist=True):
        """
        我申请的页面-断言：成功处理了流程后，我申请的中存在/不存在该条单据在指定流程中
        @param code:流程编码
        @param node:流程名称
        @param exist:断言存在或者不存在
        """
        self.enter_machine_bom_cooperation_my_application()
        actual_flow = self.element_text(user['待办列表-我申请的-当前流程'], code)
        if exist is True:
            try:
                assert actual_flow == flow
                logging.info('断言成功，我申请的中该条单据在:{}流程'.format(actual_flow))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中该条单据不在:{}流程，实际在:{}流程'.format(flow, actual_flow))
                raise
            finally:
                self.quite_iframe()
        elif exist is False:
            try:
                assert actual_flow != flow
                logging.info('断言成功，我申请的中该条单据不在:{}流程，实际在:{}流程'.format(flow, actual_flow))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中该条单据在:{}流程'.format(actual_flow))
                raise
            finally:
                self.quite_iframe()

    def enter_machine_bom_cooperation_onework_edit(self, process_code):
        """
        进入oneworks我的待办页面
        当前页获取流程编码，进入‘我的待办’点击对应查看详情，进入页面
        """
        self.enter_machine_bom_cooperation_my_todo()
        try:
            self.is_click_tbm(user['待办列表-我申请的-查看详情'], process_code)
        except:
            self.base_get_img()
            raise
        self.switch_window(1)
        sleep(0.5)
        self.quite_iframe()
        sleep(0.5)
        iframe = self.find_element(user['待办列表-我申请的-iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(1)

    def get_machine_bom_cooperation_onework_bominfo(self, select):
        """
        获取oneworks页面的Bom信息
        @param select:需要获取的信息类型： 制作类型， 品牌， 机型， 阶段， 市场， 模板， 自研/外研
        """
        if select == '机型':
            return self.element_text(user['OneworksBom信息-机型'])
        else:
            return self.element_input_text(user['BOM信息输入框'], select)

    def get_machine_bom_cooperation_oneworks_bomtree_info(self):
        """
        获取BOMTree所有内容
        """
        info = self.find_elements(user['OneworksBomTree全部内容'])
        infolist = []
        for i in info:
            infolist.append(i.text.split('\n'))
        logging.info('获取Oneworks-BOMTree所有内容{}'.format(infolist))
        return infolist

    def assert_machine_bom_cooperation_oneworks_bomtree_result(self, *content):
        """
        断言导入BOM-简易导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            self.click_machine_bom_cooperation_tree('产成品')
            contents = self.get_machine_bom_cooperation_oneworks_bomtree_info()
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

    def click_machine_bom_cooperation_oneworks_agree(self):
        """
        补充工厂页面点击同意
        """
        self.quite_iframe()
        self.is_click_tbm(user['补充工厂同意'])
        logging.info('点击同意')

    def click_machine_bom_cooperation_oneworks_confirm(self):
        """
        补充工厂页面点击确定
        """
        self.is_click_tbm(user['补充工厂同意确定'])
        logging.info('点击确定')

    def enter_machine_bom_cooperation_onework_iframe(self):
        """
        进入oneworks框架
        """
        iframe = self.find_element(user['待办列表-我申请的-iframe'])
        self.driver.switch_to.frame(iframe)

    def input_machine_bom_cooperation_oneworks_plant_info(self, plant, content):
        """
        补充工厂页面输入生产工厂信息
        :param plant: 选择工厂：国内组包工厂、 国内贴片工厂、 海外组包工厂、 海外贴片工厂
        :param content: 需要输入的工厂编号
        """
        if plant in ('国内组包工厂', '国内贴片工厂', '海外组包工厂', '海外贴片工厂'):
            self.readonly_input_text(user['生产工厂信息输入框'], content, plant)
            self.is_click_tbm(user['生产工厂信息输入框选择'], content)
        else:
            print('请输入正确的工厂')

    def click_machine_bom_cooperation_oneworks_slash(self):
        """
        补充工厂页面点击’一键/‘
        """
        self.is_click_tbm(user['补充工厂一键/'])

    def click_machine_bom_cooperation_oneworks_onepress_write(self):
        """
        补充工厂页面点击 一键填写按钮
        """
        self.is_click_tbm(user['补充工厂一键填写'])

    def click_machine_bom_cooperation_oneworks_onepress_write_confirm(self):
        """
        补充工厂页面点击 一键填写-确定按钮
        """
        self.is_click_tbm(user['补充工厂一键填写确定'])

    def click_machine_bom_cooperation_oneworks_plant_check(self, select):
        """
        补充工厂页面点击检查贴片工厂，选择贴片工厂正确/不正确
        :param select: 输入’贴片工厂不正确‘ 或者 ’贴片工厂正确‘
        """
        if select in ('贴片工厂不正确', '贴片工厂正确'):
            self.is_click_tbm(user['补充工厂检查贴片工厂'])
            self.is_click_tbm(user['补充工厂检查贴片工厂选择'], select)
        else:
            print('请输入’贴片工厂不正确‘ 或者 ’贴片工厂正确‘')

    def assert_machine_bom_cooperation_oneworks_onepress_write(self):
        """
        断言: 在补充工厂页面中，未进行选择BOM，点击一键填写按钮，按钮无法被点击
        """
        try:
            write = self.find_element(user['补充工厂一键填写'])
            assert 'is-disabled' in write.get_attribute('class')
            logging.info('断言成功，一键填写按钮不可点击')
        except:
            self.base_get_img()
            logging.error('断言失败，请检查按钮状态')
            raise

    def click_machine_bom_cooperation_oneworks_checkbox(self, code='all'):
        """
        补充工厂页面 根据material点击指定复选框，默认全选
        @param code:物料编码，传入物料编码；默认‘all’表示点击全选复选框
        """
        if code == 'all':
            self.is_click_tbm(user['补充工厂复选框全选'])
        else:
            self.is_click_tbm(user['补充工厂复选框单选'], code)

    def click_machine_bom_cooperation_oneworks_approval_checkbox(self):
        """
        BOM工程师审批页面 点击BomTree全选框
        """
        self.is_click_tbm(user['BOM工程师审批复选框全选'])

    def click_machine_bom_cooperation_oneworks_approval_export(self):
        """
        BOM工程师审批页面 点击导出BOM
        """
        self.is_click_tbm(user['BOM工程师导出BOM'])
        self.is_click_tbm(user['确定'])

    def get_machine_bom_cooperation_oneworks_approval_bomtree_info(self):
        """
        BOM工程师审批页面 获取BomTree数据
        """
        self.click_machine_bom_cooperation_tree('产成品')
        info = self.find_elements(user['BOM工程师BomTree信息'])
        info_list = []
        for i in info:
            if len(i.text.split('\n')) != 3:
                info_list.append(i.text.split('\n'))
        logging.info('获取Oneworks-BOM工程师审批页面-BOMTree所有内容{}'.format(info_list))
        return info_list

    def assert_machine_bom_cooperation_oneworks_approval_bominfo(self):
        """
        BOM工程师审批页面 导出的数据和Bom Tree的数据是一致的
        """
        page_info = self.get_machine_bom_cooperation_oneworks_approval_bomtree_info()
        excel_info = self.read_excel_flow()
        try:

            for i in range(1, len(excel_info) + 1):
                assert set(page_info[0][2:3]) <= set(excel_info[i - 1])
                assert set(page_info[i][2:-1]) <= set(excel_info[i - 1])
            logging.info('断言成功，导出的数据和BomTree的数据是一致的')
        except:
            self.base_get_img()
            logging.error('断言成功，导出的数据和BomTree的数据是不一致的')
            raise

    def click_machine_bom_cooperation_oneworks_factory_export(self):
        """
        补充工厂页面 点击 生产工厂信息-导出
        """
        self.is_click_tbm(user['补充工厂生产工厂信息-导出'])

    def get_machine_bom_cooperation_oneworks_factoryinfo(self):
        """
        在补充工厂页面中，获取生产工厂信息数据
        """
        info = self.find_elements(user['补充工厂生产工厂信息'])
        info_list = []
        for i in info:
            if len(i.text.split('\n')) != 3:
                info_list.append(i.text.split('\n'))
        logging.info('获取Oneworks-补充工厂页面-生产工厂信息所有内容{}'.format(info_list))
        return info_list

    def assert_machine_bom_cooperation_oneworks_factoryinfo(self):
        """
        在补充工厂页面中，点击导出，导出的xlsx表的数据和页面的生产工厂信息数据是一致的
        """
        page_info = self.get_machine_bom_cooperation_oneworks_factoryinfo()
        excel_info = self.read_excel_flow()
        try:
            for i in range(len(excel_info)):
                assert set(page_info[i][2:]) <= set(excel_info[i])
            logging.info('断言成功，导出的数据和生产工厂信息的数据是一致的')
        except:
            self.base_get_img()
            logging.error('断言成功，导出的数据和生产工厂信息的数据是不一致的')
            raise

    def click_machine_bom_cooperation_oneworks_approval_delete(self, tree):
        """
        BOM工程师审批页面 根据tree点击删除
        @param tree:bomtree
        """
        self.is_click_tbm(user['BOM工程师BomTree删除'], tree)

    def click_machine_bom_cooperation_oneworks_rollback(self, node):
        """
        BOM工程师审批 点击回退，根据node选择回退节点
        @param node:节点
        """
        self.quite_iframe()
        self.is_click_tbm(user['回退'])
        logging.info('点击回退')
        self.is_click_tbm(user['BOM工程师审批回退到'])
        node_dict = {'申请人':'申请人[Applicant]', node:node}
        self.is_click_tbm(user['BOM工程师审批回退选择'], node_dict[node])
        logging.info('回退到：{}'.format(node))

    def click_machine_bom_cooperation_oneworks_rollback_confirm(self):
        """
        BOM工程师审批页面 点击回退确定
        """
        self.is_click_tbm(user['BOM工程师审批回退确定'])
        logging.info('点击回退确定')

    def click_machine_bom_cooperation_oneworks_refer(self):
        """
        BOM工程师审批页面 点击转交
        """
        self.quite_iframe()
        self.is_click_tbm(user['转交'])
        logging.info('点击转交')

    def click_machine_bom_cooperation_oneworks_refer_comfirm(self):
        """
        BOM工程师审批页面 转交 点击确认
        """
        self.is_click_tbm(user['BOM工程师审批转交-确定'])
        logging.info('点击转交确定')

    def assert_machine_bom_cooperation_oneworks_comfirmrefer_exist(self, result):
        """
        断言： BOM工程师审批页面 是否存在确定转交按钮
        """
        DomAssert(self.driver).assert_page_control(user['BOM工程师审批确定转交'], result)

    def input_machine_bom_cooperation_oneworks_refer(self, referrer):
        """
        BOM工程师审批页面 转交 输入转交人
        @param referrer:转交人
        """
        self.input_text(user['BOM工程师审批转交-转交人输入'], referrer)
        logging.info('输入转交人：{}'.format(referrer))
        self.is_click_tbm(user['BOM工程师审批转交-查询'])
        logging.info('点击查询')

    def select_machine_bom_cooperation_oneworks_refer(self, referrer):
        """
        BOM工程师审批页面 转交 选择转交人
        @param referrer:转交人
        """
        self.is_click_tbm(user['BOM工程师审批转交-转交人选择'], referrer)
        logging.info('点击转交人')

    def click_machine_bom_cooperation_oneworks_refer_cancel(self):
        """
        BOM工程师审批页面 选择转交后 点击取消
        """
        self.is_click_tbm(user['BOM工程师审批取消'])
        logging.info('点击转交取消')

    def click_machine_bom_cooperation_oneworks_refer_comfirmrefer(self):
        """
        BOM工程师审批页面 选择转交后 点击确认转交
        """
        self.is_click_tbm(user['BOM工程师审批确定转交'])
        logging.info('点击确认转交')

    def assert_machine_bom_cooperation_oneworks_rollback_refer_exist(self, result):
        """
        断言： BOM工程师审批页面 是否存在转交，回退按钮
        """
        DomAssert(self.driver).assert_page_control(user['回退'], result)
        DomAssert(self.driver).assert_page_control(user['转交'], result)

    def assert_machine_bom_cooperation_flow_approver(self, code, name):
        """
        断言：BOM工程师审批页面 确认转交后，校验流程移交到转交人上
        @param code:流程编码
        @param name:审批人名称
        """
        self.enter_machine_bom_cooperation_my_application()
        approver = self.element_text(user['待办列表-我申请的-审批人'], code)
        try:
            assert approver == name
            logging.info('断言成功，审批人为:{}'.format(approver))
        except:
            self.base_get_img()
            logging.error('断言失败，审批人为:{}'.format(approver))
            raise
        finally:
            self.quite_iframe()

    def click_machine_bom_cooperation_oneworks_refuse(self):
        """
        BOM工程师审批页面 点击拒绝
        """
        self.quite_iframe()
        self.is_click_tbm(user['BOM工程师审批拒绝'])
        logging.info('点击拒绝')
        self.is_click_tbm(user['BOM工程师审批拒绝-确定'])
        logging.info('点击确定')

    def assert_machine_bom_cooperation_flow_refuse(self, code):
        """
        断言：BOM工程师审批页面 确认转交后，校验流程移交到转交人上
        @param code:流程编码
        """
        self.enter_machine_bom_cooperation_my_application()
        status = self.element_text(user['待办列表-我申请的-审批状态'], code)
        try:
            assert status == '审批拒绝'
            logging.info('断言成功，流程状态为:{}'.format(status))
        except:
            self.base_get_img()
            logging.error('断言失败，流程状态为:{}'.format(status))
            raise
        finally:
            self.quite_iframe()

    def click_machine_bom_cooperation_oneworks_approve_unfold_factoryinfo(self):
        """
        业务审核页面 点击 生产工厂信息展开表格
        """
        self.is_click_tbm(user['业务审核生产工厂信息'])

    def click_machine_bom_cooperation_oneworks_approve_export(self):
        """
        业务审核页面 点击 生产工厂信息-导出
        """
        self.is_click_tbm(user['补充工厂生产工厂信息-导出'])

    def assert_machine_bom_cooperation_oneworks_businessapprove_bomtree_edit(self):
        """
        在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑
        """
        self.mouse_double_click(user['业务审核编辑验证-用量'])
        sleep(0.5)
        DomAssert(self.driver).assert_page_control(user['业务审核编辑验证-用量'], True)

    def click_machine_bom_cooperation_oneworks_businessapprove_self_inspection(self, box, option):
        """
        业务审核页面 点击 自检清单
        @param box:输入框
        @param option:选项
        """
        self.is_click_tbm(user['业务审核-自检清单-输入框'], box)
        self.is_click_tbm(user['业务审核-自检清单-选项'], option)

    def scroll_machine_bom_cooperation_oneworks_businessapprove_self_inspection(self):
        """
        业务审核页面 滑动到 自检清单
        """
        self.scroll_into_view(user['业务审核-自检清单'])

    def input_machine_bom_cooperation_oneworks_businessapprove_inspection_result(self, rule='all', result='通过'):
        """
        业务审核页面 自检清单 点击输入检查结果
        """
        if rule == 'all' and result == '通过':
            num = self.elements_num(user['业务审核-自检清单-检查结果-规则数量'])
            for i in range(1, num+1):
                if result == '通过':
                    try:
                        self.is_click_tbm(user['业务审核-自检清单-检查结果-通过'], str(i))
                    except:
                        self.scroll_into_view(user['业务审核-自检清单-检查结果-通过'], str(i))
                        self.is_click_tbm(user['业务审核-自检清单-检查结果-通过'], str(i))
        elif rule == 'all' and result == '不通过':
            num = self.elements_num(user['业务审核-自检清单-检查结果-规则数量'])
            for i in range(1, num+1):
                try:
                    self.is_click_tbm(user['业务审核-自检清单-检查结果-不通过'], str(i))
                except:
                    self.scroll_into_view(user['业务审核-自检清单-检查结果-不通过'], str(i))
                    self.is_click_tbm(user['业务审核-自检清单-检查结果-不通过'], str(i))
        elif rule == 'all' and result == '不涉及':
            num = self.elements_num(user['业务审核-自检清单-检查结果-规则数量'])
            for i in range(1, num+1):
                try:
                    self.is_click_tbm(user['业务审核-自检清单-检查结果-不涉及'], str(i))
                except:
                    self.scroll_into_view(user['业务审核-自检清单-检查结果-不涉及'], str(i))
                    self.is_click_tbm(user['业务审核-自检清单-检查结果-不涉及'], str(i))

    def click_machine_bom_cooperation_oneworks_datagroup_checkbox(self):
        """
        数据组审批 页面 点击 生产工厂信息 全选框
        """
        self.is_click_tbm(user['oneworks-节点-数据组审批-生产工厂信息-复选框'])

    def get_machine_bom_cooperation_oneworks_datagroup_factory_info(self):
        """
        BOM工程师审批页面 获取BomTree数据
        """
        info = self.find_elements(user['BOM工程师BomTree信息'])
        info_list = []
        for i in info:
            if len(i.text.split('\n')) != 3:
                info_list.append(i.text.split('\n'))
        logging.info('获取Oneworks-BOM工程师审批页面-BOMTree所有内容{}'.format(info_list))
        return info_list

    def assert_machine_bom_cooperation_oneworks_datagroup_factoryinfo(self):
        """
        BOM工程师审批页面 导出的数据和Bom Tree的数据是一致的
        """
        page_info = self.get_machine_bom_cooperation_oneworks_datagroup_factory_info()
        excel_info = self.read_excel()
        try:

            for i in range(1, len(excel_info) + 1):
                assert set(page_info[0][2:3]) <= set(excel_info[i - 1])
                assert set(page_info[i][2:-1]) <= set(excel_info[i - 1])
            logging.info('断言成功，导出的数据和BomTree的数据是一致的')
        except:
            self.base_get_img()
            logging.error('断言成功，导出的数据和BomTree的数据是不一致的')
            raise

if __name__ == '__main__':
    pass