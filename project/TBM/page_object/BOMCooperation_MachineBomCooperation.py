from libs.common.read_element import Element
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

    @allure.step("整机BOM协作新增页面-输入BOM信息 组合方法")
    def add_bom_info(self):
        self.click_add()
        self.input_bom_info('制作类型', '生产BOM')
        self.input_bom_info('品牌', 'Infinix')
        self.input_bom_info('机型', 'X572-1')
        self.input_bom_info('阶段', '试产阶段')
        self.input_bom_info('市场', '埃塞本地')
        self.base_get_img()
        logging.info('整机BOM协作新增页面-输入BOM信息 组合方法')

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

    @allure.step("复制审批人-单据号内容")
    def get_doc_info(self):
        """
        复制审批人-单据号内容
        """
        info = self.find_elements_tbm(user['复制审批人-单据号内容'])
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText').replace('\n', '').split('\t'))
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

    @allure.step("点击简易导入")
    def click_simple_import(self):
        self.is_click_tbm(user['简易导入'])
        logging.info('点击导入-简易模式')

    @allure.step("新建流程后的后置删除处理")
    def delete_flow(self, code):
        self.recall_process(code)
        self.click_menu("BOM协作", "整机BOM协作")
        self.click_delete(code)
        self.click_dialog_confirm()
        self.assert_toast('删除成功')

    @allure.step("发起流程,点击新增，输入BOM信息，输入BOMTree信息后点击提交")
    def add_flow(self):
        """
        发起流程
        点击新增，输入BOM信息，输入BOMTree信息后点击提交
        """
        self.click_add()
        self.input_bom_info('制作类型', '生产BOM')
        self.input_bom_info('品牌', 'itel')
        self.input_bom_info('机型', 'X572-1')
        self.input_bom_info('阶段', '试产阶段')
        self.input_bom_info('市场', '埃塞本地')
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
        self.assert_OneWorks_AgreeFlow()

    @allure.step("在BOM工程师审批页面，填写信息，点击同意")
    def engineer_approve_flow(self, code):
        self.enter_oneworks_edit(code)
        self.assert_OneWorks_AgreeFlow()

    @allure.step("在BOM工程师审批页面，填写信息，点击同意")
    def engineer_Derivedapprove_flow(self, code):
        self.enter_oneworks_edit(code)
        self.click_handle_bom()
        self.assert_toast('处理成功，请检查！')
        self.assert_OneWorks_AgreeFlow()

    @allure.step("在业务审批页面，填写信息，点击同意")
    def business_approve_flow(self, code):
        self.enter_oneworks_edit(code)
        self.click_self_inspection('业务类型', '手机')
        self.click_self_inspection('检查角色', '音频')
        self.scroll_self_inspection()
        self.input_self_inspection_result()
        self.assert_OneWorks_AgreeFlow()

    def click_oneworks_approval_export(self):
        """
        BOM工程师审批页面 点击导出BOM
        """
        self.is_click_tbm(user['导出BOM'])
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
        self.scroll_into_view(user['BomTree'])
        DomAssert(self.driver).assert_control(user['BomTreeTitle'])
        self.is_click_tbm(user['BOM工程师-设置市场/配置'])
        DomAssert(self.driver).assert_att('修订BOM的市场及机型')

    @allure.step("BOM工程师页面修改设置市场/配置")
    def modify_config(self, code, type, content):
        """
        @param code:物料编号
        @param type:配置类型
        @param content:配置内容
        """
        col = self.get_table_info(user['表格字段'], type)
        if type == '组号':
            self.input_text(user['BOM工程师-设置市场/配置-修改'], content, code, col)
        elif type == '销售市场' or type == '机型配置':
            self.is_click_tbm(user['BOM工程师-设置市场/配置-修改'], code, col)
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

    @allure.step("点击衍生BOM制作需求-新增")
    def click_Derived_add(self):
        self.is_click_tbm(user['衍生BOM制作需求-新增'])
        logging.info('点击衍生BOM制作需求-新增')
        sleep(0.5)

    @allure.step("点击衍生BOM处理信息-新增")
    def click_OneworksDerived_add(self):
        self.is_click_tbm(user['衍生BOM处理信息-新增'])
        logging.info('衍生BOM处理信息-新增')
        sleep(0.5)

    @allure.step("输入衍生BOM制作需求信息")
    def input_Derived_info(self, header, info, serial=1):
        click_list = ['新BOM类型', 'BOM类型', '操作']
        select_list = ['新BOM编码', '原始BOM编码', '原始BOM工厂', '父阶物料编码', '子阶物料编码']
        input_list = ['用量', '替代组', '份额']
        column = self.get_table_info(user['表格字段'], header)
        if header in click_list:
            self.is_click_tbm(user['衍生BOM制作需求-输入框'], serial, column)
            self.is_click_tbm(user['衍生BOM制作需求-选择'], info)
        elif header in select_list:
            self.is_click_tbm(user['衍生BOM制作需求-输入框'], serial, column)
            self.input_text(user['衍生BOM制作需求-输入框'], info, serial, column)
            self.is_click_tbm(user['衍生BOM制作需求-选择2'], info)
        elif header in input_list:
            self.input_text(user['衍生BOM制作需求-输入框'], info, serial, column)

    @allure.step("输入衍生BOM处理信息")
    def input_OneworksDerived_info(self, header, info, serial=1):
        click_list = ['新BOM类型', 'BOM类型', '操作']
        select_list = ['新BOM编码', '原始BOM编码', '原始BOM工厂', '父阶物料编码', '子阶物料编码']
        input_list = ['用量', '替代组', '份额']
        column = self.get_table_info(user['衍生BOM处理信息-字段'], header)
        if header in click_list:
            self.is_click_tbm(user['衍生BOM处理信息-输入框'], serial, column)
            self.is_click_tbm(user['衍生BOM处理信息-选择'], info)
        elif header in select_list:
            self.is_click_tbm(user['衍生BOM处理信息-输入框'], serial, column)
            self.input_text(user['衍生BOM处理信息-输入框'], info, serial, column)
            self.is_click_tbm(user['衍生BOM处理信息-选择2'], info)
        elif header in input_list:
            self.input_text(user['衍生BOM处理信息-输入框'], info, serial, column)

    @allure.step("点击衍生需求导入")
    def click_Derived_import(self):
        self.is_click_tbm(user['衍生BOM制作需求-导入'])
        logging.info('点击衍生BOM制作需求-导入')

    @allure.step("点击处理BOM")
    def click_handle_bom(self):
        self.is_click_tbm(user['处理BOM'])


if __name__ == '__main__':
    pass
