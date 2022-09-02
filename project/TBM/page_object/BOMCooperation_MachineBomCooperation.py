from selenium.webdriver import Keys
from libs.common.read_element import Element
from libs.config.conf import BASE_DIR
from project.TBM.page_object.Center_Component import CenterComponent
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class MachineBOMCollaboration(CenterComponent):
    """BOM协作_整机BOM协作"""

    @allure.step("初始化页面")
    def refresh_webpage_click_menu(self):
        self.refresh_webpage()
        self.click_menu("BOM协作", "整机BOM协作")

    @allure.step("整机BOM协作新增页面-输入BOM信息")
    def input_add_bom_info(self, type, content):
        """
        整机BOM协作新增页面 - 输入BOM信息
        :param type: 字段名
        :param content: 选择信息内容
        """
        if type == '机型':
            self.input_text(user['BOM信息输入框'], content, type)
            sleep(1)
            self.is_click_tbm(user['BOM信息输入框机型选择'], content)
        else:
            self.is_click_tbm(user['BOM信息输入框'], type)
            self.scroll_into_view(user['BOM信息输入框选择'], content)
            sleep(0.5)
            self.is_click_tbm(user['BOM信息输入框选择'], content)
        logging.info('输入BOM信息:输入字段{}， 输入内容：{}'.format(type, content))

    @allure.step("整机BOM协作新增页面-输入BOM信息 组合方法")
    def add_bom_info(self):
        self.click_add()
        self.input_add_bom_info('制作类型', '生产BOM')
        self.input_add_bom_info('品牌', 'Infinix')
        self.input_add_bom_info('机型', 'X572-1')
        self.input_add_bom_info('阶段', '试产阶段')
        self.input_add_bom_info('市场', '埃塞本地')
        self.base_get_img()
        logging.info('整机BOM协作新增页面-输入BOM信息 组合方法')

    @allure.step("点击提交")
    def click_add_submit(self):
        self.scroll_into_view(user['提交'])
        sleep(0.5)
        self.is_click_tbm(user['提交'])

    @allure.step("点击新增bom")
    def click_add_bomtree(self):
        self.is_click_tbm(user['新增BomTree'])
        logging.info('点击新增Bom')

    @allure.step("整机BOM协作新增页面-输入BOMTree 组合方法")
    def add_bomtree(self):
        self.click_add_bomtree()
        self.input_bomtree('产成品', 'BOM类型', '国内生产BOM')
        self.input_bomtree('产成品', 'BOM状态', '试产')
        self.input_bomtree('产成品', '物料编码', '10018955')
        self.input_bomtree('产成品', '用量', '1000')
        self.base_get_img()
        logging.info('整机BOM协作新增页面-输入BOMTree 组合方法')

    @allure.step("点击复制审批人")
    def click_copy_review(self):
        self.scroll_into_view(user['复制审批人'])
        self.is_click_tbm(user['复制审批人'])
        logging.info('点击复制审批人')
        DomAssert(self.driver).assert_att('选择单据号')

    @allure.step("单据号查询")
    def doc_num_search(self, type, content):
        """
        复制审批人-单据号查询
        @param type:输入的用户名
        @param content:输入的用户名
        """
        if type == '申请人':
            self.is_click_tbm(user['选择单据号输入框'], type)
            self.input_text(user['复制审批人-成员列表输入框'], content)
            self.is_click_tbm(user['成员选择'], content)
            self.is_click_tbm(user['成员确定'])
        else:
            self.input_text(user['选择单据号输入框'], content, type)
        logging.info('单据号查询:查询字段{}， 查询内容：{}'.format(type, content))

    @allure.step("点击查询")
    def click_search(self):
        self.is_click_tbm(user['查询'])
        logging.info('点击查询')

    @allure.step("复制审批人-单据号内容")
    def get_doc_info(self):
        """
        复制审批人-单据号内容
        """
        info = self.find_elements_tbm(user['复制审批人-单据号内容'])
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText').replace('\n','').split('\t'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    @allure.step("断言：复制审批人弹框，查询结果正确显示")
    def assert_doc_result(self, *content):
        """
        复制审批人弹框，查询结果正确显示
        :param content: 断言内容，可以一次传入多个
        """
        try:
            contents = self.get_doc_info()
            for row in contents:
                assert set(list(content)) <= set(row)
            logging.info('断言成功，选项值包含：{}'.format(content))
        except:
            logging.error('断言失败，选项值不包含：{}'.format(content))
            raise

    @allure.step("断言：复制审批人弹框，查询结果正确显示")
    def click_doc_select(self, doc):
        self.is_click_tbm(user['复制审批人-单据选择'], doc)
        logging.info('选择单据：{}'.format(doc))

    @allure.step("断言：复制审批人成功，审核人正确设置")
    def assert_doc_copy(self, audit, type):
        copy_audit = self.element_input_text(user['审核人类别'], type)
        ValueAssert.value_assert_equal(audit, copy_audit)

    @allure.step("审核人设置")
    def select_business_review(self, audit, type='all'):
        """
        审核人设置-业务评审-：选择用户
        @param type:选择的类别
        @param audit:输入的用户名
        """
        self.scroll_into_view(user['审核人设置'])
        if type == 'all':
            info = self.find_elements_tbm(user['审核人名单'])
            infolist = []
            for i in info:
                infolist.append(i.text)
                self.is_click_tbm(user['审核人类别'], i.text)
                self.input_text(user['成员列表输入框'], audit)
                sleep(1)
                self.is_click_tbm(user['成员选择'], audit)
                self.is_click_tbm(user['成员确定'])
            self.base_get_img()
            logging.info('获取审核人名单:{}'.format(infolist))
        else:
            self.is_click_tbm(user['审核人类别'], type)
            self.input_text(user['成员列表输入框'], audit)
            sleep(1)
            self.is_click_tbm(user['成员选择'], audit)
            self.is_click_tbm(user['成员确定'])
            self.base_get_img()
        logging.info('审核人填写:字段{}， 审核人：{}'.format(type, audit))

    @allure.step("获取整机BOM协作第一列内容")
    def get_info(self):
        """
        获取整机BOM协作第一列内容 @return:返回文本及索引位置分别是'No.'：0; '流程编码':1; '制作类型':2; '机型'：3; '品牌':4; '市场':5; '阶段':6; '单据状态':7;
        '同步状态':8; '申请人':9; '创建时间':10; '操作':11
        """
        self.click_menu("BOM协作", "整机BOM协作")
        sleep(1)
        info = self.find_elements_tbm(user['表格内容'])
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    def get_assigned_info(self, code):
        """
        获取整机BOM协作第一列内容 @return:返回文本及索引位置分别是'No.'：0; '流程编码':1; '制作类型':2; '机型'：3; '品牌':4; '市场':5; '阶段':6; '单据状态':7;
        '同步状态':8; '申请人':9; '创建时间':10; '操作':11
        """
        self.click_menu("BOM协作", "整机BOM协作")
        sleep(1)
        info = self.find_elements_tbm(user['表格指定编码内容'], code)
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    @allure.step("断言整机BOM协作新增成功后，页面表格内容是否正确")
    def assert_add_result(self, *content):
        """
        断言整机BOM协作新增成功后，页面表格内容是否正确
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
    def input_bomtree(self, tree, header, content):
        """
        BomTree信息根据Tree在指定列表输入内容
        @param tree:输入选择
        @param header: BomTree要输入的表头；【BOM类型， BOM状态， 物料编码， 用量， 替代组， 份额】
        @param content:输入的内容
        """
        if header == 'BOM类型':
            self.is_click_tbm(user['BOMTreeBOM类型'], tree)
            self.is_click_tbm(user['BOMTree输入框选择'], content)
        elif header == 'BOM状态':
            self.is_click_tbm(user['BOMTreeBOM状态'], tree)
            self.is_click_tbm(user['BOMTree输入框选择'], content)
        elif header == '物料编码':
            self.is_click_tbm(user['BOMTree编辑'], tree)
            self.readonly_input_text(user['BOMTree物料编码'], content, tree)
            sleep(1)
            self.is_click_tbm(user['物料编码选择'], content)
            self.is_click_tbm(user['BOMTree确定'], tree)
        elif header == '用量':
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

    @allure.step("点击新增物料")
    def click_add_material(self):
        self.is_click_tbm(user['新增物料'])
        logging.info('点击新增物料')

    @allure.step("点击新增加的物料列进行对焦")
    def move_to_add_material(self, tree):
        self.is_click_tbm(user['BOMTree新增物料对焦'], tree)

    @allure.step("BomTree新增物料根据Tree在指定列表输入内容")
    def input_optional_material(self, tree, header, content):
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

    @allure.step("根据流程编码进行删除操作")
    def click_delete(self, code):
        """
        @param code:流程编码
        """
        self.is_click_tbm(user['删除'], code)
        self.is_click_tbm(user['确定'])

    @allure.step("点击一键填写")
    def click_one_press(self):
        self.is_click_tbm(user['BOM信息一键填写'])

    @allure.step("一键填写")
    def input_one_press(self, key, value):
        """
        一键填写-根据key选择字段名称，根据value输入字段值
        @param key:字段名称
        @param value:字段值
        """
        self.click_one_press()
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

    @allure.step("点击取消")
    def click_one_press_cancel(self):
        self.is_click_tbm(user['BOM信息一键填写取消'])
        logging.info('点击取消')

    @allure.step("获取整机BOM协作-BOMTREE指定列内容")
    def get_bomtree_info(self, material):
        """
        获取整机BOM协作-BOMTREE指定列内容
        @param material:物料名
        @return:返回文本及索引位置分别是  0:'No.'; 1:'BOM类型'; 2:'BOM状态'; 3:'Tree'; 4:'复选框'; 5:'物料编码';
                                    6:'物料描述'; 7:'物料属性'; 8:'用量'; 9:'替代组'; 10:'份额'; 11:'操作'
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

    @allure.step("判断是否存在批量删除")
    def assert_batch_delete(self, result):
        try:
            ac_result = self.element_exist(user['批量删除'])
            assert ac_result is result
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

    @allure.step("点击简易导入")
    def click_simple_import(self):
        self.is_click_tbm(user['简易导入'])
        logging.info('点击导入-简易模式')

    @allure.step("导入-上传文件")
    def upload_import(self, file):
        """
        导入-上传文件
        """
        ele = self.driver.find_element(By.XPATH,
                                       "//div[not(contains(@style,'display: none')) and "
                                       "@class='el-dialog__wrapper']/div/div[2]/div[1]/div/input")
        ele.send_keys(file)
        logging.info('点击导入-上传文件')

    @allure.step("上传错误文件")
    def simple_upload_wrong_file(self):
        """
        简易导入-上传文件
        """
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', 'worng_file_text.txt')
        self.upload_import(path)

    @allure.step("上传正常文件")
    def simple_upload_true_file(self):
        """
        简易导入-上传文件
        """
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', '生产BOM项目经理简易模式导入.xls')
        self.upload_import(path)

    @allure.step("上传内容错误文件")
    def simple_upload_wrongcontent_file(self):
        """
        简易导入-上传文件
        """
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', '生产BOM项目经理简易模式导入错误内容.xls')
        self.upload_import(path)
        sleep(5)

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

    def get_bomtree_simple_upload_info(self):
        """
        获取导入BOM-结果内容
        """
        info = self.find_elements_tbm(user['简易导入内容'])
        infolist = []
        for i in info:
            infolist.append(i.text.split('\n'))
        logging.info('获取BOM导入结果{}'.format(infolist))
        return infolist

    @allure.step("断言导入BOM-简易导入后，页面表格内容是否正确")
    def assert_simple_upload_result(self, *content):
        """
        断言导入BOM-简易导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            contents = self.get_bomtree_simple_upload_info()
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

    @allure.step("点击应用")
    def click_apply(self):
        self.is_click_tbm(user['应用'])
        logging.info('点击应用')
        sleep(1)

    @allure.step("点击展开")
    def click_tree(self, tree):
        """
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

    @allure.step("断言导入BOM-简易导入后，页面表格内容是否正确")
    def assert_tree_result(self, *content):
        """
        断言导入BOM-简易导入后，页面表格内容是否正确
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

    @allure.step("点击导入BOM")
    def click_bom_import(self):
        """
        点击导入BOM
        """
        self.is_click_tbm(user['导入BOM'])
        logging.info('点击导入BOM')

    @allure.step("上传错误文件")
    def upload_wrong_file(self):
        """
        导入BOM-上传文件
        """
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', 'worng_file_text.txt')
        self.upload_import(path)

    @allure.step("上传正常文件")
    def upload_true_file(self):
        """
        导入BOM-上传文件
        """
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', '生产bom项目经理导入模板.xlsx')
        self.upload_import(path)

    @allure.step("上传内容错误文件")
    def upload_wrongcontent_file(self):
        """
        导入BOM-上传文件
        """
        path = os.path.join(BASE_DIR, 'project', 'TBM', 'data', '生产bom项目经理导入模板错误内容.xlsx')
        self.upload_import(path)
        sleep(5)

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

    @allure.step("断言导入BOM-简易导入后，页面表格内容是否正确")
    def assert_upload_result(self, *content):
        """
        断言导入BOM-简易导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            contents = self.get_bomtree_upload_info()
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

    @allure.step("新建流程后的后置删除处理")
    def delete_flow(self, code):
        self.recall_process(code)
        self.click_menu("BOM协作", "整机BOM协作")
        self.click_delete(code)
        self.assert_toast('删除成功')

    @allure.step("发起流程,点击新增，输入BOM信息，输入BOMTree信息后点击提交")
    def add_flow(self):
        """
        发起流程
        点击新增，输入BOM信息，输入BOMTree信息后点击提交
        """
        self.click_add()
        self.input_add_bom_info('制作类型', '生产BOM')
        self.input_add_bom_info('品牌', 'itel')
        self.input_add_bom_info('机型', 'X572-1')
        self.input_add_bom_info('阶段', '试产阶段')
        self.input_add_bom_info('市场', '埃塞本地')
        self.click_add_bomtree()
        self.input_bomtree('BOM类型', '国内生产BOM')
        self.input_bomtree('BOM状态', '试产')
        self.input_bomtree('物料编码', '10018956')
        self.input_bomtree('用量', '1000')
        self.select_business_review('李小素', 'MPM')
        self.select_business_review('李小素', 'NPS')
        self.click_add_submit()
        sleep(1)
        self.assert_toast('创建流程成功')

    @allure.step("在补充工厂页面，填写信息，点击同意")
    def supplementary_factory_flow(self, code):
        self.enter_oneworks_edit(code)
        self.input_oneworks_plant_info('国内组包工厂', '1051')
        self.click_oneworks_slash()
        self.click_oneworks_plant_check('贴片工厂正确')
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("在BOM工程师审批页面，填写信息，点击同意")
    def engineer_approve_flow(self, code):
        self.enter_oneworks_edit(code)
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("在业务审批页面，填写信息，点击同意")
    def business_approve_flow(self, code):
        self.enter_oneworks_edit(code)
        self.click_oneworks_businessapprove_self_inspection('业务类型', '手机')
        self.click_oneworks_businessapprove_self_inspection('检查角色', '音频')
        self.scroll_oneworks_businessapprove_self_inspection()
        self.input_oneworks_businessapprove_inspection_result()
        self.click_oneworks_agree()
        self.click_oneworks_confirm()
        self.assert_toast()
        self.quit_oneworks()

    @allure.step("点击查看")
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
        sleep(2)
        DomAssert(self.driver).assert_att('基本信息')

    @allure.step("获取oneworks页面的Bom信息")
    def get_onework_bominfo(self, select):
        """
        获取oneworks页面的Bom信息
        @param select:需要获取的信息类型： 制作类型， 品牌， 机型， 阶段， 市场， 模板， 自研/外研
        """
        self.scroll_into_view(user['BOM工程师-BomTree'])
        DomAssert(self.driver).assert_control(user['BOM工程师-BomTreeTitle'])
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

    @allure.step("断言导入BOM-简易导入后，页面表格内容是否正确")
    def assert_oneworks_bomtree_result(self, *content):
        """
        断言导入BOM-简易导入后，页面表格内容是否正确
        :param content: 需要断言的内容，可以一次传入多个
        """
        try:
            self.click_tree('产成品')
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

    @allure.step("补充工厂页面点击-一键/")
    def click_oneworks_slash(self):
        self.is_click_tbm(user['补充工厂一键/'])

    @allure.step("补充工厂页面点击 一键填写按钮")
    def click_oneworks_onepress_write(self):
        self.is_click_tbm(user['补充工厂一键填写'])

    @allure.step("补充工厂页面点击 一键填写-确定按钮")
    def click_oneworks_onepress_write_confirm(self):
        """
        补充工厂页面点击 一键填写-确定按钮
        """
        self.is_click_tbm(user['补充工厂一键填写确定'])

    @allure.step("补充工厂页面点击检查贴片工厂，选择贴片工厂正确/不正确")
    def click_oneworks_plant_check(self, select):
        """
        :param select: 输入贴片工厂不正确 或者 贴片工厂正确
        """
        if select in ('贴片工厂不正确', '贴片工厂正确'):
            self.is_click_tbm(user['补充工厂检查贴片工厂'])
            self.is_click_tbm(user['补充工厂检查贴片工厂选择'], select)
        else:
            print('请输入’贴片工厂不正确‘ 或者 ’贴片工厂正确‘')

    @allure.step("在补充工厂页面中，未进行选择BOM，点击一键填写按钮，按钮无法被点击")
    def assert_oneworks_onepress_write(self):
        try:
            write = self.find_element(user['补充工厂一键填写'])
            assert 'is-disabled' in write.get_attribute('class')
            logging.info('断言成功，一键填写按钮不可点击')
        except:
            self.base_get_img()
            logging.error('断言失败，请检查按钮状态')
            raise

    @allure.step("补充工厂页面,点击指定复选框")
    def click_oneworks_checkbox(self, code='all'):
        """
        补充工厂页面 根据material点击指定复选框，默认全选
        @param code:物料编码，传入物料编码；默认‘all’表示点击全选复选框
        """
        sleep(3)
        if code == 'all':
            self.is_click_tbm(user['补充工厂复选框全选'])
        else:
            self.is_click_tbm(user['补充工厂复选框单选'], code)

    def click_oneworks_approval_checkbox(self):
        """
        BOM工程师审批页面 点击BomTree全选框
        """
        DomAssert(self.driver).assert_control(user['BOM工程师-BomTreeTitle'])
        self.is_click_tbm(user['BOM工程师审批复选框全选'])

    def click_oneworks_approval_export(self):
        """
        BOM工程师审批页面 点击导出BOM
        """
        self.is_click_tbm(user['BOM工程师导出BOM'])
        self.is_click_tbm(user['确定'])

    @allure.step("BOM工程师审批页面 获取BomTree数据")
    def get_oneworks_approval_bomtree_info(self):
        # self.click_tree('产成品')
        info = self.find_elements_tbm(user['BOM工程师BomTree信息'])
        info_list = []
        for i in info:
            # if len(i.get_attribute('innerText').split('\n')) != 3:
            if len(i.text.split('\n')) != 3:
                info_list.append(i.text.split('\n'))
        logging.info('获取Oneworks-BOM工程师审批页面-BOMTree所有内容{}'.format(info_list))
        return info_list

    @allure.step("断言：BOM工程师审批页面 导出的数据和Bom Tree的数据是一致的")
    def assert_oneworks_approval_bominfo(self):
        self.click_tree('产成品')
        page_info = self.get_oneworks_approval_bomtree_info()
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
        self.is_click_tbm(user['补充工厂生产工厂信息-导出'])

    @allure.step("在补充工厂页面中，获取生产工厂信息数据")
    def get_oneworks_factoryinfo(self):
        state = self.get_element_attribute(user['补充工厂生产工厂信息明细折叠按钮'], 'class')
        if 'expand' not in state:
            self.is_click_tbm(user['补充工厂生产工厂信息'])
        DomAssert(self.driver).assert_control(user['生产工厂信息Title'])
        info = self.find_elements_tbm(user['补充工厂生产工厂信息明细'])
        info_list = []
        for i in info:
            if len(i.text.split('\n')) != 3:
                info_list.append(i.text.split('\n'))
        logging.info('获取Oneworks-补充工厂页面-生产工厂信息所有内容{}'.format(info_list))
        return info_list

    @allure.step("在补充工厂页面中，点击导出，导出的xlsx表的数据和页面的生产工厂信息数据是一致的")
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

    @allure.step("BOM工程师审批页面 根据tree点击删除")
    def click_oneworks_approval_delete(self, tree):
        """
        BOM工程师审批页面 根据tree点击删除
        @param tree:bomtree
        """
        self.is_click_tbm(user['BOM工程师BomTree删除'], tree)

    @allure.step("业务审核页面 点击 生产工厂信息展开表格")
    def click_oneworks_approve_unfold_factoryinfo(self):
        """
        业务审核页面 点击 生产工厂信息展开表格
        """
        self.is_click_tbm(user['生产工厂信息'])

    @allure.step("断言：在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑")
    def assert_oneworks_businessapprove_bomtree_edit(self):
        """
        在业务审核页面中，多次点击产成品一列数据，该列数据是不能再进行编辑
        """
        self.mouse_double_click(user['业务审核编辑验证-用量'])
        sleep(0.5)
        DomAssert(self.driver).assert_control(user['业务审核编辑验证-用量'], True)

    @allure.step("业务审核页面 点击 自检清单")
    def click_oneworks_businessapprove_self_inspection(self, box, option):
        """
        业务审核页面 点击 自检清单
        @param box:输入框
        @param option:选项
        """
        self.is_click_tbm(user['业务审核-自检清单-输入框'], box)
        self.is_click_tbm(user['业务审核-自检清单-选项'], option)

    @allure.step("业务审核页面 滑动到 自检清单")
    def scroll_oneworks_businessapprove_self_inspection(self):
        self.scroll_into_view(user['业务审核-自检清单'])

    @allure.step("业务审核页面 自检清单 点击输入检查结果")
    def input_oneworks_businessapprove_inspection_result(self, rule='all', result='通过'):
        if rule == 'all' and result == '通过':
            num = self.elements_num(user['业务审核-自检清单-检查结果-规则数量'])
            for i in range(1, num + 1):
                if result == '通过':
                    try:
                        self.is_click_tbm(user['业务审核-自检清单-检查结果-通过'], str(i))
                    except:
                        self.scroll_into_view(user['业务审核-自检清单-检查结果-通过'], str(i))
                        self.is_click_tbm(user['业务审核-自检清单-检查结果-通过'], str(i))
        elif rule == 'all' and result == '不通过':
            num = self.elements_num(user['业务审核-自检清单-检查结果-规则数量'])
            for i in range(1, num + 1):
                try:
                    self.is_click_tbm(user['业务审核-自检清单-检查结果-不通过'], str(i))
                except:
                    self.scroll_into_view(user['业务审核-自检清单-检查结果-不通过'], str(i))
                    self.is_click_tbm(user['业务审核-自检清单-检查结果-不通过'], str(i))
        elif rule == 'all' and result == '不涉及':
            num = self.elements_num(user['业务审核-自检清单-检查结果-规则数量'])
            for i in range(1, num + 1):
                try:
                    self.is_click_tbm(user['业务审核-自检清单-检查结果-不涉及'], str(i))
                except:
                    self.scroll_into_view(user['业务审核-自检清单-检查结果-不涉及'], str(i))
                    self.is_click_tbm(user['业务审核-自检清单-检查结果-不涉及'], str(i))

    @allure.step("数据组审批 页面 点击 生产工厂信息 全选框")
    def click_oneworks_datagroup_checkbox(self):
        self.is_click_tbm(user['oneworks-节点-数据组审批-生产工厂信息-复选框'])

    @allure.step("BOM工程师审批页面 获取BomTree数据")
    def get_oneworks_datagroup_factory_info(self):
        info = self.find_elements_tbm(user['BOM工程师BomTree信息'])
        info_list = []
        for i in info:
            if len(i.text.split('\n')) != 3:
                info_list.append(i.text.split('\n'))
        logging.info('获取Oneworks-BOM工程师审批页面-BOMTree所有内容{}'.format(info_list))
        return info_list

    @allure.step("断言：BOM工程师审批页面 导出的数据和Bom Tree的数据是一致的")
    def assert_oneworks_datagroup_factoryinfo(self):
        page_info = self.get_oneworks_datagroup_factory_info()
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

    @allure.step("BOM工程师页面点击设置市场/配置")
    def click_config(self):
        self.scroll_into_view(user['BOM工程师-BomTree'])
        DomAssert(self.driver).assert_control(user['BOM工程师-BomTreeTitle'])
        self.is_click_tbm(user['BOM工程师-设置市场/配置'])
        DomAssert(self.driver).assert_att('修订BOM的市场及机型')

    @allure.step("BOM工程师页面修改设置市场/配置")
    def modify_config(self, num, type, content):
        """
        @param num:物料编号
        @param type:配置类型
        @param content:配置内容
        """
        if type == '组号':
            self.input_text(user['BOM工程师-设置市场/配置-修改组号'], content, num)
        elif type == '销售市场':
            self.is_click_tbm(user['BOM工程师-设置市场/配置-修改销售市场'], num)
            self.is_click_tbm(user['BOM工程师-设置市场/配置-市场/机型-选择'], content)
        elif type == '机型配置':
            self.is_click_tbm(user['BOM工程师-设置市场/配置-修改机型配置'], num)
            self.is_click_tbm(user['BOM工程师-设置市场/配置-市场/机型-选择'], content)

    @allure.step("BOM工程师页面设置市场/配置确定")
    def click_config_confirm(self):
        self.is_click(user['BOM工程师-设置市场/配置-确定'])

    @allure.step("断言：BOM工程师页面，Bom Tree数据包含指定数据")
    def assert_oneworks_add_material(self, content):
        page_info = self.get_oneworks_approval_bomtree_info()
        try:
            assert content in page_info
        except:
            self.base_get_img()
            raise


if __name__ == '__main__':
    pass
