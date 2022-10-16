import logging
from time import sleep

from selenium.webdriver import Keys

from libs.common.read_element import Element
from project.TBM.page_object.Center_Component import CenterComponent
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class ShippingCountrySearch(CenterComponent, APIRequest):
    """出货国家_出货国家查询"""

    @allure.step("初始化页面")
    def refresh_webpage_click_menu(self):
        self.refresh_webpage()
        self.click_menu("出货国家", "出货国家查询")

    @allure.step("新建流程后的后置删除处理")
    def delete_shipping_country_search(self, code):
        logging.info(f'开始撤回流程：{code}')
        self.recall_process(code)
        self.click_menu("出货国家", "出货国家流程")
        self.click_delete(code)
        self.click_delete_confirm()
        self.assert_toast()
        logging.info('撤回删除流程成功')

    @allure.step("出货国家查询 根据条件选择输入框 输入/选择内容")
    def input_condition(self, codition, content):
        """
        出货国家查询 根据条件选择输入框 输入/选择内容
        @parma codition:输入框名称
        @parma content:内容
        """
        select_list = ['全球版本', 'MEMORY', 'BAND STRATEGY', '产品状态']
        if codition == '品牌':
            self.is_click_tbm(user['输入框'], codition)
            self.is_click_tbm(user['输入框选择'], content)
        elif codition in select_list:
            self.readonly_input_text(user['输入框'], content, codition)
            self.is_click_tbm(user['输入框选择'], content)
        elif codition == '市场名称' or codition == '项目名称':
            self.input_text(user['输入框'], content, codition)

    @allure.step("出货国家查询 获取国家状态")
    def get_cty_status(self, item):
        """
        获取出货国家查询指定列内容
        @parma item:项目名称
        @return:返回地区状态
        """
        self.click_menu("出货国家", "出货国家查询")
        sleep(1)
        self.input_condition('品牌', 'Infinix')
        self.input_condition('项目名称', item)
        self.click_search()
        info = self.find_elements_tbm(user['表格指定行内容'], item)
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        logging.info('返回表格搜索结果的国家状态{}'.format(infolist[5:11]))
        return infolist[5:11]

    @allure.step("选择汇签/抄送人员")
    def select_signatory(self, choice, name):
        """
        出货国家流程新增页面 - 选择汇签/抄送人员
        :param choice: 汇签/抄送人员选择框
        :param name: 人员名字
        """
        self.is_click_tbm(user['汇签/抄送人员选择框'], choice)
        self.is_click_tbm(user['成员列表清空'], choice)
        self.input_text(user['成员列表输入框'], name)
        sleep(1)
        self.is_click_tbm(user['成员选择'], name)
        self.is_click_tbm(user['成员确定'])

    @allure.step("点击提交")
    def click_add_submit(self):
        """点击提交"""
        self.scroll_into_view(user['提交'])
        sleep(0.5)
        self.is_click_tbm(user['提交'])

    @allure.step("获取出货国家流程第一列内容")
    def get_info(self, item):
        """
        获取出货国家流程第一列内容
        @parma item:项目名称
        @return:返回文本及索引位置分别是'No.'==0; '标题'==1; '流程编码'==2; '业务类型'==3; '项目'==4; '品牌'==5; '单据状态'==6; '申请人'==7; '申请时间'==8; '操作'==9;
        """
        self.click_menu("出货国家", "出货国家流程")
        sleep(1)
        info = self.find_elements_tbm(user['表格指定行内容'], item)
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    @allure.step("检查出货国家查询地区状态是否为未配置状态，如果是否则清除配置")
    def check_reset_cty_status(self, item, cty):
        """
        待修改！！！！！！！！！！！！！
        检查出货国家查询地区状态是否为未配置状态，如果是否则清除配置
        @parma item:项目名称
        @parma cty:区域
        """
        cty_status = self.get_cty_status(item)
        status_result = [True, True, True]
        x = 0
        z = 0
        if cty == '东亚':
            for i in cty_status[0:3]:
                if i != '':
                    status_result[x] = False
                x += 1
            if False in status_result:
                self.click_checkbox(item)
                self.click_change('变更国家')
                self.click_change_select('东亚')
                self.click_oneworks_product_definition_info_edit(item)
                ctr = ['EE1', '乍得', '中国']
                for i in status_result:
                    if i is False:
                        self.edit_product_definition_closed_ctyinfo(ctr[z])
                    z += 1
                self.click_oneworks_product_definition_info_confirm()
                self.select_signatory('汇签人员', '李小素')
                self.click_add_submit()
                DomAssert(self.driver).assert_att('请求成功')
                process_code = self.get_info(item)[2]
                self.onework_agree_flow(process_code, '产品部管理员审核')
                self.onework_agree_flow(process_code, '产品部汇签')
                self.onework_agree_flow(process_code, '产品经理修改')
                self.onework_agree_flow(process_code, '项目经理审批')
                self.refresh_webpage_click_menu()
                self.input_condition('品牌', 'Infinix')
                self.input_condition('项目名称', item)
                self.click_search()

    @allure.step("获取 出货国家查询 第一列项目名称")
    def get_project_name(self):
        """
        获取 出货国家查询 第一列项目名称
        @return:'项目名称'
        """
        self.click_menu("出货国家", "出货国家查询")
        sleep(1)
        info = self.find_elements_tbm(user['表格内容'])
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist[4]

    @allure.step("勾选复选框")
    def click_checkbox(self, name):
        """
        出货国家查询 勾选指定项目复选框
        @name:'表格内容名称'
        """
        self.is_click_tbm(user['指定复选框'], name)

    @allure.step("点击变更产品/变更国家")
    def click_change(self, type):
        """
        出货国家查询 点击变更产品/变更国家
        @type:变更产品/变更国家
        """
        self.is_click_tbm(user['变更'], type)
        sleep(2)

    @allure.step("断言：变更产品的项目名称/变更产品的产品经理不一致提示")
    def assert_change_tip(self):
        if self.element_exist(user['提示语']):
            try:
                tip = self.element_text(user['提示语'])
                if tip == '变更产品的项目名称不一致，是否继续？' or tip == '变更产品的产品经理不是当前登录人，是否继续？':
                    self.is_click_tbm(user['确定'])
                else:
                    pass
            except:
                logging.error('断言失败，没有不一致提示')
                raise
            try:
                tip = self.element_text(user['提示语'])
                if tip == '变更产品的项目名称不一致，是否继续？' or tip == '变更产品的产品经理不是当前登录人，是否继续？':
                    self.is_click_tbm(user['确定'])
                else:
                    pass
            except:
                logging.error('断言失败，没有不一致提示')
                raise

    @allure.step("出货国家查询 点击变更国家 选择地区")
    def click_change_select(self, cty):
        """
        出货国家查询 点击变更国家 选择地区
        @cty: 地区
        """
        self.is_click_tbm(user['变更国家选择'], cty)
        self.is_click_tbm(user['变更国家选择确定'])

    @allure.step("oneworks-国家出货查询 变更产品/国家点击产品定义信息-编辑按钮")
    def click_oneworks_product_definition_info_edit(self, item):
        """
        oneworks-国家出货查询 变更产品/国家 进入oneworks页面
        根据表格内容点击 产品定义信息 编辑按钮
        :param item: 表格内容
        """
        sleep(1)
        self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-指定-编辑'], item)

    @allure.step("oneworks-国家出货查询 变更产品/国家点击产品定义信息-确定按钮")
    def click_oneworks_product_definition_info_confirm(self):
        """
        oneworks-国家出货查询 变更产品/国家 进入oneworks页面
        根据表格内容点击 产品定义信息 确认按钮
        """
        self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-确定'])

    @allure.step("编辑修改产品定义信息-区域")
    def edit_product_definition_ctyinfo(self, item, header, content):
        """
        国家出货查询 变更国家 进入流程页面
        编辑修改产品定义信息
        :param header: 选择要选择的区域
        :param content: 选择信息内容
        """
        definition_dict = {'EE1': '14', '乍得': '15', '中国': '16', '2马其顿2': '17', '孟加拉': '18', '韩国': '19'}
        self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-指定-编辑'], item)
        col = self.get_table_info(user['产品定义信息表格字段'], header)
        self.is_click_tbm(user['产品定义信息表格指定内容'], item, col)
        self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-选择'], content)
        self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-确定'])

    @allure.step("编辑修改产品定义信息-删除区域信息")
    def edit_product_definition_closed_ctyinfo(self, header='all'):
        """
        oneworks-国家出货查询 变更国家 进入流程页面
        编辑修改产品定义信息
        :param header: 选择要选择的区域
        """
        ele = self.find_element(user['oneworks-节点-产品经理修改-产品定义信息-变更-操作框'])
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", ele, 'style',
                                   'display: none;')
        definition_dict = {'EE1': '14', '乍得': '15', '中国': '16', '2马其顿2': '17', '孟加拉': '18', '韩国': '19'}
        if header == 'all':
            for header in ['EE1', '乍得', '中国']:
                self.hover(user['oneworks-节点-产品经理修改-产品定义信息-变更-输入框'], definition_dict[header])
                self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-变更-输入框删除'], definition_dict[header])
        else:
            self.hover(user['oneworks-节点-产品经理修改-产品定义信息-变更-输入框'], definition_dict[header])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-变更-输入框删除'], definition_dict[header])
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", ele, 'style',
                                   'width: 120px; bottom: 5px;')

    @allure.step("点击同意-确定")
    def click_onework_agree(self):
        self.frame_exit()
        self.is_click_tbm(user['同意'])
        self.is_click_tbm(user['确定'])
        logging.info('点击同意-确定')

    @allure.step("点击同意-确定")
    def onework_agree_flow(self, code, node=None):
        self.enter_oneworks_edit(code)
        self.click_onework_agree()
        self.assert_toast()
        self.quit_oneworks()
        if node is not None:
            self.assert_my_todo_node(code, node, True)

    def assert_flow_compelete(self, code):
        logging.info('等待一分钟，流程抄送到审批完成流转')
        sleep(60)
        self.assert_my_application_flow(code, '审批完成')



    @allure.step("点击市场名称，跳转连接")
    def click_TableLink(self, name):
        self.is_click_tbm(user['跳转连接'], name)
        sleep(1)

    @allure.step("点击变更记录")
    def click_ChangeHistory(self, name):
        self.is_click_tbm(user['变更记录'], name)

    @allure.step("断言版本记录有内容")
    def assert_VersionHistory(self):
        DomAssert(self.driver).assert_control(user['版本记录内容'], result=True)

    @allure.step("断言变更记录有内容")
    def assert_ChangeHistory(self):
        DomAssert(self.driver).assert_control(user['变更记录内容'], result=True)

    @allure.step("点击信息复选框全选")
    def click_InfoCheckBox(self):
        self.is_click_tbm(user['复选框全选'])

    @allure.step("点击批量修改")
    def click_Bulk_Editing(self):
        self.is_click_tbm(user['批量修改'])

    @allure.step("批量修改选择地区")
    def select_Bulk_Editing_cty(self, cty):
        """
        @param cty: 国家区域
        """
        self.is_click_tbm(user['国家区域'])
        cty_text = self.element_text(user['国家区域文本'])
        if cty_text == cty:
            self.is_click_tbm(user['国家区域选择'], cty)
        else:
            self.is_click_tbm(user['国家区域展开'])
            self.is_click_tbm(user['国家区域选择'], cty)
        self.is_click_tbm(user['一键填写标题'])

    @allure.step("批量修改选择出货/认证备份")
    def select_Bulk_Editing_status(self, status):
        """
        @param status: 出货/认证备份
        """
        self.is_click_tbm(user['出货/认证备份'])
        self.is_click_tbm(user['出货/认证备份选择'], status)

    @allure.step("批量修改确定")
    def select_Bulk_Editing_confirm(self):
        self.is_click_tbm(user['一键填写确定'])

    @allure.step("批量修改取消")
    def select_Bulk_Editing_cancel(self):
        self.is_click_tbm(user['一键填写取消'])
if __name__ == '__main__':
    pass
