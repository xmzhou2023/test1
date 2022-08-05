from time import sleep
from selenium.webdriver import Keys
from libs.common.read_element import Element
from libs.config.conf import BASE_DIR
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

    @allure.step("点击新增")
    def click_add(self):
        self.is_click_tbm(user['新增'])
        sleep(1)

    @allure.step("单机头BOM协作新增页面-输入BOM信息")
    def input_add_bom_info(self, info, select):
        """
        单机头BOM协作新增页面-输入BOM信息
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
            sleep(0.5)
            self.scroll_into_view(user['BOM信息输入框选择'], select)
            sleep(1)
            self.is_click_tbm(user['BOM信息输入框选择'], select)
            logging.info('选择点击Bom信息:{}'.format(select))

    @allure.step("单机头BOM协作新增页面-输入BOM信息组合")
    def add_bom_info(self):
        self.click_add()
        self.input_add_bom_info('制作类型', '单机头BOM制作')
        self.input_add_bom_info('品牌', 'itel')
        self.input_add_bom_info('机型', 'X572-1')
        self.input_add_bom_info('阶段', '试产阶段')
        self.input_add_bom_info('市场', '埃塞本地')
        self.input_add_bom_info('同时做衍生BOM', '否')
        self.base_get_img()

    @allure.step("点击提交")
    def click_add_submit(self):
        self.scroll_into_view(user['提交'])
        sleep(0.5)
        self.is_click_tbm(user['提交'])

    @allure.step("点击新增bom")
    def click_add_bomtree(self):
        self.is_click_tbm(user['新增BomTree'])
        logging.info('点击新增Bom')
        sleep(0.5)

    def assert_add_bomtree_exist(self, result):
        """点击新增bom"""
        DomAssert(self.driver).assert_control(user['新增BomTree'], result)

    @allure.step("输入BomTree内容")
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

    @allure.step("根据Tree点击删除按钮")
    def click_bomtree_delete(self, tree):
        self.is_click_tbm(user['BOMTree删除'], tree)

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
        self.is_click_tbm(user['成员确定'])

    @allure.step("oneworks-审核人设置-组合")
    def oneworsk_review(self):
        self.select_business_review('李小素', '质量部')
        self.select_business_review('李小素', '结构部')
        self.select_business_review('李小素', '硬件')
        self.select_business_review('李小素', '影像部')
        self.select_business_review('李小素', '音频')
        self.select_business_review('李小素', '预研组')
        self.select_business_review('李小素', '中试部')
        self.select_business_review('李小素', '采购部')
        self.select_business_review('李小素', '结构经理')
        self.select_business_review('李小素', '啊啊啊')
        self.base_get_img()

    @allure.step("获取单机头BOM协作第一列内容")
    def get_info(self):
        """
        获取单机头BOM协作第一列内容
        @return:返回文本及索引位置分别是'流程编码':1; '制作类型':2; '机型'：3; '品牌':4; '市场':5; '阶段':6; '单据状态':7; '同步状态':8; '申请人':9; '创建时间':10;
        """
        self.click_menu("BOM协作", "单机头BOM协作")
        sleep(1)
        info = self.find_elements_tbm(user['表格内容'])
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    def get_specify_info(self, code):
        """
        获取单机头BOM协作指定流程编码的表格内容
        @return:返回文本及索引位置分别是'流程编码':1; '制作类型':2; '机型'：3; '品牌':4; '市场':5; '阶段':6; '单据状态':7; '同步状态':8; '申请人':9; '创建时间':10;
        """
        self.click_menu("BOM协作", "单机头BOM协作")
        sleep(1)
        info = self.find_elements_tbm(user['指定编码表格内容'], code)
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    @allure.step("断言单机头BOM协作新增成功后，页面表格内容是否正确")
    def assert_add_result(self, *content):
        """
        断言单机头BOM协作新增成功后，页面表格内容是否正确
        :param content: 需要，可以一次传入多个
        """
        try:
            contents = self.get_info()
            assert set(content) <= set(contents)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise

    @allure.step("BomTree信息根据Tree在指定列表输入内容")
    def input_optional_bomtree(self, tree, header, content):
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

    def click_optional_material(self):
        """
        点击新增物料
        """
        self.is_click_tbm(user['新增物料'])
        logging.info('点击新增物料')

    @allure.step("新增物料对焦")
    def move_to_add_material(self, tree):
        """
        新增物料后，根据上级物料 点击新增加的物料列进行对焦
        """
        self.is_click_tbm(user['BOMTree新增物料对焦'], tree)

    @allure.step("新增物料输入内容")
    def input_optional_material(self, tree, header, content):
        """
        新增物料后，模版信息根据条件在新增的物料输入内容并且点击
        @param content:输入的内容
        @param header: BomTree要输入的表头；{'BOM类型':'2','BOM状态':'3','物料编码':'6','用量':'9','替代组':'10','份额':'11',}
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
            logging.info("输入需要操作的表头：('BOM类型','BOM状态','物料编码','用量','替代组','份额',)")



    def click_delete(self, code):
        """
        根据流程编码点击删除 进行删除操作
        @param code:流程编码
        """
        self.is_click_tbm(user['删除'], code)
        self.is_click_tbm(user['确定'])

    def click_one_press(self):
        """
        点击一键填写
        """
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
        sleep(0.5)

    def click_one_press_cancel(self):
        """
        点击取消
        """
        self.is_click_tbm(user['BOM信息一键填写取消'])
        sleep(0.5)
        logging.info('点击取消')

    @allure.step("获取BOMTREE指定列内容")
    def get_bomtree_info(self, material):
        """
        获取单机头BOM协作-BOMTREE指定列内容
        @param material:物料名
        @return:返回文本及索引位置分别是  1:'BOM状态'; 2:'Tree';4:'物料编码'; 5:'物料描述'; 6:'物料属性'; 7:'用量'; 8:'替代组'; 9:'份额';
        """
        info = self.find_elements_tbm(user['BomTree内容'], material)
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

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

    def assert_batch_delete(self, result):
        """
        断言：判断是否存在批量删除
        """
        try:
            assert self.element_exist(user['批量删除']) is result
            logging.info('断言成功')
        except:
            self.base_get_img()
            logging.error('断言失败')
            raise

    @allure.step("点击批量删除")
    def click_batch_delete(self):
        self.is_click_tbm(user['批量删除'])
        logging.info('点击批量删除')

    @allure.step("点击确定")
    def click_batch_confirm(self):
        self.is_click_tbm(user['确定'])
        logging.info('确定')
        sleep(0.5)

    @allure.step("点击导入BOM")
    def click_bom_import(self):
        self.is_click_tbm(user['导入BOM'])
        logging.info('点击导入BOM')

    @allure.step("导入-上传文件")
    def upload_import(self, file):
        ele = self.driver.find_element(By.XPATH,
                                       "//div[not(contains(@style,'display: none')) and @class='el-dialog__wrapper']/div/div[2]/div[1]/div/input")
        ele.send_keys(file)
        logging.info('点击导入-上传文件')

    # def upload_import(self, file):
    #     """
    #     导入-上传文件
    #     """
    #     self.upload_file(user['选择文件'], file)

    @allure.step("断言导入错误内容后，页面状态是否正确")
    def assert_wrongcontent_simple_upload_result(self):
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

    @allure.step("点击应用")
    def click_apply(self):
        self.is_click_tbm(user['应用'])
        logging.info('点击应用')
        sleep(1)

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
                content_list.append(tuple(i))
            assert set(content) <= set(content_list)
            logging.info(content_list)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            self.base_get_img()
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise

    @allure.step("导入BOM-上传错误文件")
    def upload_wrong_file(self):
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', 'worng_file_text.txt')
        self.upload_import(path)

    @allure.step("导入BOM-上传正确文件")
    def upload_true_file(self):
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', '单机头结构工程师发起导入模板.xlsx')
        self.upload_import(path)

    @allure.step("导入BOM-上传错误内容文件")
    def upload_wrongcontent_file(self):
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', '单机头结构工程师发起导入模板错误内容.xlsx')
        self.upload_import(path)
        sleep(2)
        DomAssert(self.driver).assert_att('电池_Infinix_BL_51BX_5100mAh_ATL_IN_BIS')

    def get_bomtree_upload_info(self):
        """
        获取导入BOM-结果内容
        """
        info = self.find_elements_tbm(user['导入BOM内容'])
        infolist = []
        for i in info:
            infolist.append(i.text.split('\n'))
        # logging.info(infolist)
        # infolist = list(info.text.split('\n'))
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

    @allure.step("新建流程后的后置删除处理")
    def delete_flow(self, code):
        self.recall_process(code)
        self.click_menu("BOM协作", "单机头BOM协作")
        self.click_delete(code)
        self.assert_toast('删除成功')

    @allure.step("在补充工厂页面-流程组合")
    def supplementary_factory_flow(self, code):
        self.enter_oneworks_edit(code)
        self.input_oneworks_plant_info('国内组包工厂', '1051')
        self.click_oneworks_slash()
        self.click_oneworks_plant_check('贴片工厂正确')
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    def click_check(self, code):
        """
        根据流程编码点击查看 进行查看操作
        @param code:流程编码
        """
        self.is_click_tbm(user['查看'], code)

    @allure.step("进入oneworks查看流程页面")
    def enter_onework_check(self, code):
        sleep(1)
        self.click_check(code)
        self.switch_window(1)
        sleep(1)
        self.frame_enter(user['待办列表-我申请的-iframe'])
        sleep(1)

    @allure.step("获取oneworks页面的Bom信息")
    def get_onework_bominfo(self, select):
        """
        获取oneworks页面的Bom信息
        @param select:需要获取的信息类型： 制作类型， 品牌， 机型， 阶段， 市场， 模板， 自研/外研
        """
        if select == '机型':
            return self.element_text(user['OneworksBom信息-机型'])
        else:
            return self.element_input_text(user['BOM信息输入框'], select)

    def get_oneworks_bomtree_info(self):
        """
        获取BOMTree所有内容
        """
        info = self.find_elements_tbm(user['OneworksBomTree全部内容'])
        infolist = []
        for i in info:
            infolist.append(i.text.split('\n'))
        logging.info('获取Oneworks-BOMTree所有内容{}'.format(infolist))
        return infolist

    @allure.step("断言导入BOM-导入后，页面表格内容是否正确")
    def assert_oneworks_bomtree_result(self, *content):
        """
        断言导入BOM-导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            self.click_tree('单机头')
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

    @allure.step("补充工厂页面输入生产工厂信息")
    def input_oneworks_plant_info(self, plant, content):
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

    @allure.step("补充工厂页面点击’一键/‘")
    def click_oneworks_slash(self):
        self.is_click_tbm(user['补充工厂一键/'])

    @allure.step("补充工厂页面点击 一键填写按钮")
    def click_oneworks_onepress_write(self):
        self.is_click_tbm(user['补充工厂一键填写'])

    @allure.step("补充工厂页面点击 一键填写-确定按钮")
    def click_oneworks_onepress_write_confirm(self):
        self.is_click_tbm(user['补充工厂一键填写确定'])

    @allure.step("补充工厂页面点击检查贴片工厂，选择贴片工厂正确/不正确")
    def click_oneworks_plant_check(self, select):
        """
        补充工厂页面点击检查贴片工厂，选择贴片工厂正确/不正确
        :param select: 输入’贴片工厂不正确‘ 或者 ’贴片工厂正确‘
        """
        if select in ('贴片工厂不正确', '贴片工厂正确'):
            self.is_click_tbm(user['补充工厂检查贴片工厂'])
            self.is_click_tbm(user['补充工厂检查贴片工厂选择'], select)
        else:
            print('请输入’贴片工厂不正确‘ 或者 ’贴片工厂正确‘')

    @allure.step("断言: 在补充工厂页面中，未进行选择BOM，点击一键填写按钮，按钮无法被点击")
    def assert_oneworks_onepress_write(self):
        try:
            write = self.find_element(user['补充工厂一键填写'])
            assert 'is-disabled' in write.get_attribute('class')
            logging.info('断言成功，一键填写按钮不可点击')
        except:
            self.base_get_img()
            logging.error('断言失败，请检查按钮状态')
            raise

    @allure.step("补充工厂页面 根据material点击指定复选框")
    def click_oneworks_checkbox(self, code='all'):
        """
        补充工厂页面 根据material点击指定复选框，默认全选
        @param code:物料编码，传入物料编码；默认‘all’表示点击全选复选框
        """
        sleep(2)
        if code == 'all':
            self.is_click_tbm(user['补充工厂复选框全选'])
        else:
            self.is_click_tbm(user['补充工厂复选框单选'], code)
        logging.info('点击复选框')

    @allure.step("BOM工程师审批页面 点击BomTree全选框")
    def click_oneworks_approval_checkbox(self):
        """
        BOM工程师审批页面 点击BomTree全选框
        """
        self.is_click_tbm(user['BOM工程师审批复选框全选'])
        sleep(0.5)

    def click_oneworks_approval_export(self):
        """
        BOM工程师审批页面 点击导出BOM
        """
        self.is_click_tbm(user['BOM工程师导出BOM'])
        sleep(0.5)
        self.is_click_tbm(user['确定'])

    def get_oneworks_approval_bomtree_info(self):
        """
        BOM工程师审批页面 获取BomTree数据
        """
        self.click_tree('单机头')
        info = self.find_elements_tbm(user['BOM工程师BomTree信息'])
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

    def click_oneworks_factory_export(self):
        """
        补充工厂页面 点击 生产工厂信息-导出
        """
        self.is_click_tbm(user['补充工厂生产工厂信息-导出'])
        sleep(0.5)

    def get_oneworks_factoryinfo(self):
        """
        在补充工厂页面中，获取生产工厂信息数据
        """
        info = self.find_elements_tbm(user['补充工厂生产工厂信息'])
        info_list = []
        for i in info:
            if len(i.text.split('\n')) != 3:
                info_list.append(i.text.split('\n'))
        logging.info('获取Oneworks-补充工厂页面-生产工厂信息所有内容{}'.format(info_list))
        return info_list

    def assert_oneworks_factoryinfo(self):
        """
        在补充工厂页面中，点击导出，导出的xlsx表的数据和页面的生产工厂信息数据是一致的
        """
        page_info = self.get_oneworks_factoryinfo()
        excel_info = self.read_excel_flow()
        try:
            for i in range(len(excel_info)):
                assert set(page_info[i][2:]) <= set(excel_info[i])
            logging.info('断言成功，导出的数据和生产工厂信息的数据是一致的')
        except:
            self.base_get_img()
            logging.error('断言成功，导出的数据和生产工厂信息的数据是不一致的')
            raise

    @allure.step("断言：在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑")
    def assert_oneworks_bomtree_edit(self):
        """
        在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑
        """
        self.mouse_double_click(user['物料编码编辑验证'])
        sleep(0.5)
        DomAssert(self.driver).assert_control(user['物料编码编辑验证'], True)

if __name__ == '__main__':
    pass
