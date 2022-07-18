from time import sleep
from libs.common.read_element import Element
from project.TBM.page_object.ShippingCountry_ShippingCountryFlow import ShippingCountryFlow
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)
shipping_country_flow = Element(pro_name, 'ShippingCountry_ShippingCountryFlow')


class ShippingCountrySearch(ShippingCountryFlow):
    """出货国家_出货国家查询"""

    @allure.step("初始化页面")
    def refresh_webpage_click_menu(self):
        self.refresh_webpage()
        self.click_menu("出货国家", "出货国家查询")

    def enter_shipping_country_search_my_application(self):
        """
        进入我申请的页面
        """
        self.click_menu('待办列表', '我申请的')
        self.refresh()
        iframe = self.find_element(user['待办列表-我申请的-iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(1)
        self.is_click_tbm(user['待办列表-刷新'])

    def click_shipping_country_search_delete(self, code):
        """
        根据流程编码点击删除 进行删除操作
        @param code:流程编码
        """
        self.is_click_tbm(user['删除'], code)
        self.is_click_tbm(user['确定'])

    def recall_shipping_country_search_process(self, code):
        """
        提交流程申请后，在待办列表-我申请的 根据流程编码对流程进行撤回操作
        @param code:流程编码
        """
        self.enter_shipping_country_search_my_application()
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
        self.quit_shipping_country_flow_onework()
        self.click_menu("出货国家", "出货国家查询")

    def enter_shipping_country_search_my_todo(self):
        """
        进入我的待办页面
        """
        self.click_menu('待办列表', '我的待办')
        iframe = self.find_element(user['待办列表-我申请的-iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(1)
        self.is_click_tbm(user['待办列表-刷新'])

    def enter_shipping_country_search_onework_edit(self, code):
        """
        进入oneworks我的待办页面
        当前页获取流程编码，进入‘我的待办’点击对应查看详情，进入页面
        """
        self.enter_shipping_country_search_my_todo()
        try:
            self.is_click_tbm(user['待办列表-我申请的-查看详情'], code)
        except:
            self.base_get_img()
            raise
        self.switch_window(1)
        sleep(0.5)
        self.frame_exit()
        sleep(0.5)
        iframe = self.find_element(user['待办列表-我申请的-iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(1)

    def click_shipping_country_search_search(self):
        """点击查询"""
        self.is_click_tbm(user['查询'])
        sleep(1)

    def input_shipping_country_search_condition(self, codition, content):
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

    def get_shipping_country_search_cty_status(self, item):
        """
        获取出货国家查询指定列内容
        @parma item:项目名称
        @return:返回地区状态
        """
        self.click_menu("出货国家", "出货国家查询")
        sleep(1)
        self.input_shipping_country_search_condition('品牌', 'Infinix')
        self.input_shipping_country_search_condition('项目名称', item)
        self.click_shipping_country_search_search()
        info = self.find_elements_tbm(user['表格指定行内容'], item)
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        logging.info('返回表格搜索结果的国家状态{}'.format(infolist[5:11]))
        return infolist[5:11]

    def check_reset_shipping_country_search_cty_status(self, item, cty):
        """
        待修改！！！！！！！！！！！！！
        检查出货国家查询地区状态是否为未配置状态，如果是否则清除配置
        @parma item:项目名称
        @parma cty:区域
        """
        cty_status = self.get_shipping_country_search_cty_status(item)
        status_result = [True, True, True]
        x = 0
        z = 0
        if cty == '东亚':
            for i in cty_status[0:3]:
                if i != '':
                    status_result[x] = False
                x += 1
            if False in status_result:
                self.click_shipping_country_search_checkbox(item)
                self.click_shipping_country_search_change('变更国家')
                self.click_shipping_country_search_change_select('东亚')
                self.click_oneworks_shipping_country_search_product_definition_info_edit(item)
                ctr = ['EE1', '乍得', '中国']
                for i in status_result:
                    if i is False:
                        self.edit_shipping_country_search_product_definition_closd_ctyinfo(ctr[z])
                    z += 1
                self.click_oneworks_shipping_country_search_product_definition_info_confirm()
                self.select_shipping_country_flow_signatory('汇签人员', '李小素')
                self.click_shipping_country_flow_add_submit()
                DomAssert(self.driver).assert_att('请求成功')
                process_code = self.get_shipping_country_flow_info(item)[2]
                self.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
                self.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
                self.shipping_country_search_onework_agree_flow(process_code, '产品经理修改')
                self.shipping_country_search_onework_agree_flow(process_code, '项目经理审批')
                self.refresh_webpage_click_menu()
                self.input_shipping_country_search_condition('品牌', 'Infinix')
                self.input_shipping_country_search_condition('项目名称', item)
                self.click_shipping_country_search_search()

    def get_shipping_country_search_project_name(self):
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

    @allure.step("勾选指定项目复选框")
    def click_shipping_country_search_checkbox(self, name):
        """
        出货国家查询 勾选指定项目复选框
        @name:'表格内容名称'
        """
        self.is_click_tbm(user['指定复选框'], name)

    @allure.step("点击变更产品/变更国家")
    def click_shipping_country_search_change(self, type):
        """
        出货国家查询 点击变更产品/变更国家
        @type:变更产品/变更国家
        """
        self.is_click_tbm(user['变更'], type)
        sleep(1)

    def assert_shipping_country_search_change_tip(self):
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

    def click_shipping_country_search_change_select(self, cty):
        """
        出货国家查询 点击变更国家 选择地区
        @cty: 地区
        """
        self.is_click_tbm(user['变更国家选择'], cty)
        self.is_click_tbm(user['变更国家选择确定'])

    def click_oneworks_shipping_country_search_product_definition_info_edit(self, item):
        """
        oneworks-国家出货查询 变更产品/国家 进入oneworks页面
        根据表格内容点击 产品定义信息 编辑按钮
        :param item: 表格内容
        """
        self.is_click_tbm(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-指定-编辑'], item)

    def click_oneworks_shipping_country_search_product_definition_info_confirm(self):
        """
        oneworks-国家出货查询 变更产品/国家 进入oneworks页面
        根据表格内容点击 产品定义信息 确认按钮
        """
        self.is_click_tbm(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-确定'])

    @allure.step("编辑修改产品定义信息")
    def edit_oneworks_shipping_country_search_product_definition_info(self, header, content):
        """
        oneworks-国家出货查询 变更产品/国家 发起页面/oneworks页面
        编辑修改产品定义信息
        :param header: 选择要输入的信息
        :param content: 选择信息内容
        """
        definition_dict = {'全球版本': '4', '市场名称': '5', '项目名称': '6', 'MEMORY': '7', 'BANDSTRATEGY': '8',
                           '产品经理': '9', '项目经理': '10', 'aaa': '12', 'bbb': '13'}
        select_list = ['全球版本', 'MEMORY', 'BANDSTRATEGY']
        select1_list = ['aaa', 'bbb']
        input_list = ['市场名称', '项目名称']
        member_list = ['产品经理', '项目经理']
        if header in select_list:
            self.is_click_tbm(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-变更-输入框'], definition_dict[header])
            self.is_click_tbm(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-选择'], content)
        if header in select1_list:
            self.is_click_tbm(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-变更-输入框'], definition_dict[header])
            self.is_click_tbm(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-选择'], content)
        elif header in input_list:
            self.input_text(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-变更-输入框'], content, definition_dict[header])
        elif header in member_list:
            self.is_click_tbm(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-变更-输入框'], definition_dict[header])
            self.input_text(shipping_country_flow['产品定义信息成员列表输入框'], content)
            sleep(1)
            self.is_click_tbm(shipping_country_flow['成员选择'], content)
            self.is_click_tbm(shipping_country_flow['产品定义信息成员确定'])
        else:
            print(f'请输入正确选项：{definition_dict}')

    def edit_shipping_country_search_product_definition_ctyinfo(self, header, content):
        """
        国家出货查询 变更国家 进入流程页面
        编辑修改产品定义信息
        :param header: 选择要选择的区域
        :param content: 选择信息内容
        """
        definition_dict = {'EE1': '14', '乍得': '15', '中国': '16', '2马其顿2': '17', '孟加拉': '18', '韩国': '19'}
        self.is_click_tbm(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-变更-输入框'], definition_dict[header])
        self.is_click_tbm(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-选择'], content)

    def edit_shipping_country_search_product_definition_closd_ctyinfo(self, header='all'):
        """
        oneworks-国家出货查询 变更国家 进入流程页面
        编辑修改产品定义信息
        :param header: 选择要选择的区域
        """
        ele = self.find_element(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-变更-操作框'])
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", ele, 'style',
                                   'display: none;')
        definition_dict = {'EE1': '14', '乍得': '15', '中国': '16', '2马其顿2': '17', '孟加拉': '18', '韩国': '19'}
        if header == 'all':
            for header in ['EE1', '乍得', '中国']:
                self.hover(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-变更-输入框'], definition_dict[header])
                self.is_click_tbm(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-变更-输入框删除'], definition_dict[header])
        else:
            self.hover(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-变更-输入框'], definition_dict[header])
            self.is_click_tbm(shipping_country_flow['oneworks-节点-产品经理修改-产品定义信息-变更-输入框删除'], definition_dict[header])
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", ele, 'style',
                                   'width: 120px; bottom: 5px;')

    def enter_shipping_country_search_onework_iframe(self):
        """
        进入oneworks框架
        """
        iframe = self.find_element(shipping_country_flow['待办列表-我申请的-iframe'])
        self.driver.switch_to.frame(iframe)

    def shipping_country_search_onework_agree_flow(self, code, node):
        self.assert_shipping_country_flow_my_todo_node(code, node, True)
        self.enter_shipping_country_flow_onework_edit(code)
        self.click_onework_shipping_country_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_shipping_country_flow_onework()

    def assert_flow_compelete(self, code):
        sleep(60)
        self.screening_code(code)
        self.assert_shipping_country_flow_my_application_flow(code, '审批完成')

    def shipping_country_flow_change_country_flow(self, item, cty):
        """待修改"""
        self.refresh_webpage_click_menu()
        self.input_shipping_country_search_condition('品牌', 'Infinix')
        self.input_shipping_country_search_condition('项目名称', item)
        self.click_shipping_country_search_search()
        self.click_shipping_country_search_checkbox(item)
        self.click_shipping_country_search_change('变更国家')
        self.click_shipping_country_search_change_select(cty)
        self.click_oneworks_shipping_country_search_product_definition_info_edit(item)
        self.edit_shipping_country_search_product_definition_ctyinfo('EE1', '●')
        self.click_oneworks_shipping_country_search_product_definition_info_confirm()
        self.select_shipping_country_flow_signatory('汇签人员', '李小素')
        self.click_shipping_country_flow_add_submit()
        DomAssert(self.driver).assert_att('请求成功')
        process_code = self.get_shipping_country_flow_info(item)[2]
        self.shipping_country_search_onework_agree_flow(process_code, '产品部管理员审核')
        self.shipping_country_search_onework_agree_flow(process_code, '产品部汇签')
        self.shipping_country_search_onework_agree_flow(process_code, '产品经理修改')
        self.shipping_country_search_onework_agree_flow(process_code, '项目经理审批')


if __name__ == '__main__':
    pass
