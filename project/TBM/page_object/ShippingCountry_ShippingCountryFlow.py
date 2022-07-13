import allure

import datetime
from time import sleep

import requests

import logging
from libs.common.read_element import Element
from project.TBM.api.api import APIRequest
from public.base.assert_ui import DomAssert
from project.TBM.page_object.Center_Component import CenterComponent
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)


class ShippingCountryFlow(CenterComponent, APIRequest):
    """出货国家_出货国家流程"""

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

    @allure.step("初始化页面")
    def refresh_webpage_click_menu(self):
        self.refresh_webpage()
        self.click_menu("出货国家", "出货国家流程")

    def quit_shipping_country_flow_onework(self):
        """
        退出oneworks查看流程页面
        """
        self.frame_exit()
        self.close_switch(1)
        self.refresh()
        self.frame_exit()
        sleep(1)

    def enter_shipping_country_flow_my_application(self):
        """
        进入我申请的页面
        """
        self.click_menu('待办列表', '我申请的')
        self.refresh()
        iframe = self.find_element(user['待办列表-我申请的-iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(1)
        self.is_click_tbm(user['待办列表-刷新'])

    def click_shipping_country_flow_delete(self, code):
        """
        根据流程编码点击删除 进行删除操作
        @param code:流程编码
        """
        self.is_click_tbm(user['删除'], code)
        self.is_click_tbm(user['确定'])

    def recall_shipping_country_flow_process(self, code):
        """
        提交流程申请后，在待办列表-我申请的 根据流程编码对流程进行撤回操作
        @param code:流程编码
        """
        self.enter_shipping_country_flow_my_application()
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
        self.click_menu("出货国家", "出货国家流程")

    def delete_shipping_country_flow(self, process_code):
        """
        新建流程后的后置删除处理
        """
        logging.info(f'开始撤回流程：{process_code}')
        self.recall_shipping_country_flow_process(process_code)
        self.click_shipping_country_flow_delete(process_code)
        DomAssert(self.driver).assert_att('请求成功')
        logging.info('撤回删除流程成功')

    def enter_shipping_country_flow_my_todo(self):
        """
        进入我的待办页面
        """
        self.click_menu('待办列表', '我的待办')
        iframe = self.find_element(user['待办列表-我申请的-iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(1)
        self.is_click_tbm(user['待办列表-刷新'])

    def enter_shipping_country_flow_onework_edit(self, code):
        """
        进入oneworks我的待办页面
        当前页获取流程编码，进入‘我的待办’点击对应查看详情，进入页面
        """
        self.enter_shipping_country_flow_my_todo()
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

    def click_shipping_country_flow_add(self):
        """点击新增"""
        self.is_click_tbm(user['新增'])
        sleep(1)

    def input_shipping_country_flow_add_item_info(self, info, select):
        """
        出货国家流程新增页面 - 输入项目信息
        :param info: 选择要输入的信息
        :param select: 选择信息内容
        """
        if info == '品牌':
            self.is_click_tbm(user['项目信息输入框'], info)
            logging.info('点击项目信息输入框:{}'.format(info))
            self.scroll_into_view(user['项目信息输入框选择'], select)
            sleep(1)
            self.is_click_tbm(user['项目信息输入框选择'], select)
            logging.info('选择项目信息 品牌:{}'.format(select))

        elif info == '项目':
            self.input_text(user['项目信息输入框'], select, info)
            logging.info('输入项目信息 项目:{}'.format(select))
        elif info == '描述':
            self.input_text(user['项目信息文本框'], select, info)
            logging.info('输入项目信息 描述:{}'.format(select))
        else:
            print('请选择正确的项目信息输入：品牌 or 项目 or 描述')

    def input_shipping_country_flow_add_product_definition_info(self, header, content):
        """
        出货国家流程新增页面 - 新增产品定义信息
        :param info: 选择要输入的信息
        :param select: 选择信息内容
        """
        definition_dict = {'全球版本': '4', '市场名称': '5', '项目名称': '6', 'MEMORY': '7', 'BANDSTRATEGY': '8',
                           '产品经理': '9', '项目经理': '10', 'aaa': '12', 'bbb': '13'}
        select_list = ['全球版本', 'MEMORY', 'BANDSTRATEGY']
        select1_list = ['aaa', 'bbb']
        input_list = ['市场名称', '项目名称']
        member_list = ['产品经理', '项目经理']
        if header in select_list:
            self.is_click_tbm(user['产品定义信息输入框'], definition_dict[header])
            self.is_click_tbm(user['产品定义信息选择'], content)
        if header in select1_list:
            self.is_click_tbm(user['产品定义信息输入框2'], definition_dict[header])
            self.is_click_tbm(user['产品定义信息选择'], content)
        elif header in input_list:
            self.input_text(user['产品定义信息输入框'], content, definition_dict[header])
        elif header in member_list:
            self.is_click_tbm(user['产品定义信息输入框2'], definition_dict[header])
            self.input_text(user['产品定义信息成员列表输入框'], content)
            sleep(1)
            self.is_click_tbm(user['成员选择'], content)
            self.is_click_tbm(user['产品定义信息成员确定'])
        else:
            print(f'请输入正确选项：{definition_dict}')

    def request_shipping_country_flow_add(self, data, headers):
        """
        TBM 出货国家流程 新增接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家流程新增接口')
        return self.api_request('出货国家流程新增接口', data, headers)

    def request_shipping_country_flow_search(self, data, headers):
        """
        TBM 出货国家流程 TBM查询接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家流程查询接口')
        return self.api_request('出货国家流程查询接口', data, headers)

    @allure.step("出货国家流程新增接口")
    def api_shipping_country_flow_add(self):
        """
        TBM 出货国家流程新增接口
        """
        logging.info('发起流程接口：出货国家流程新增流程')
        token = self.tbm_login()
        titletime = datetime.datetime.now().strftime('%Y-%m-%d')
        flowStartdate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        querytime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        add_data = {"prdInfoVOS": [{"scPrdBaseInfoVO": {"bizType": "create", "globalVersion": "ver1",
                                                        "marketName": f"市场名称{querytime}",
                                                        "projectName": f"项目名称{querytime}", "memory": "128+8",
                                                        "bandStrategy": "latinAmericaMarket",
                                                        "productManager": "18645960", "projectManager": "18645960",
                                                        "brandCode": "infinix", "editStatus": 'true', "isAdd": 'true'},
                                    "scPrdUniversalInfoMap": {"aaaa": "Standard1", "bbb": "Chipset1"},
                                    "countryProperties": {}}],
                    "flowMainVO": {"title": f"[李小素]-[{titletime}]", "flowNo": "", "flowProposer": "18645960",
                                   "flowDept": "PI_系统四部", "flowStartdate": f"{flowStartdate}", "remark": "",
                                   "busiType": "", "flowProposerName": "李小素"},
                    "scProjectVO": {"brandCode": "infinix", "projectName": f"项目名称{querytime}",
                                    "templateBid": "989123709249916928"}, "submitType": "submit", "approvers": {
                "bisSupplyApprovers": [{"role": "", "roleKey": "verb", "userName": "", "userNo": "18645960"}],
                "bisSupplySenders": [{"role": "", "roleKey": "verc", "userName": "", "userNo": "18645960"}]},
                    "areas": [], "uploadList": [], "fields": [
                {"id": 'null', "bid": "989123712022351872", "fieldName": "aaa", "fieldIdent": "aaaa",
                 "fieldType": "select", "fieldTypeRef": "Standard", "necessary": 1, "fieldOrder": 0, "valid": 'true',
                 "constraint": "{\"key\": \"Standard\"}", "value": 'null'},
                {"id": 'null', "bid": "989123712022351873", "fieldName": "bbb", "fieldIdent": "bbb",
                 "fieldType": "select", "fieldTypeRef": "Chipset", "necessary": 1, "fieldOrder": 1, "valid": 'true',
                 "constraint": "{\"key\": \"Chipset\"}", "value": 'null'}]}
        search_data = {"param": {"title": "", "flowNo": "", "projectName": f"项目名称{querytime}", "brandCode": "",
                                 "createdTimeFrom": "", "createdTimeTo": "", "flowProposer": "", "status": "",
                                 "flowStartdate": ""}, "current": 1, "size": 10}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        self.request_shipping_country_flow_add(add_data, headers)
        search_reponse = self.request_shipping_country_flow_search(search_data, headers)
        search_reponse_data = search_reponse['body']['data']['data']
        logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，bid：{}'.format(search_reponse_data[0]['flowNo'], search_reponse_data[0]['instanceId'], search_reponse_data[0]['bid']))
        logging.info('流程接口结束：出货国家流程新增流程')
        return search_reponse_data[0]['flowNo'], search_reponse_data[0]['instanceId'], search_reponse_data[0]['bid']

    def request_shipping_country_flow_delete(self, data, headers):
        """
        TBM 出货国家流程删除已撤回接口
        @param instanceId:oneworks撤回流程编码
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家流程删除已撤回接口')
        return self.api_request('出货国家流程删除已撤回接口', data, headers)

    @allure.step("出货国家流程撤回删除接口")
    def api_shipping_country_flow_delete(self, instanceid, bid):
        """
        通过调用接口发起撤回流程
        调用接口：oneworks流程撤回接口，出货国家流程删除已撤回接口
        @param instanceid:oneworks撤回流程编码
        @param flowid:流程ID
        """
        logging.info('发起流程接口：出货国家流程撤回流程')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        delete_data = {"flowBid": bid}
        self.tbm_oneworks_recall(instanceid, headers)
        self.request_shipping_country_flow_delete(delete_data, headers)
        logging.info('流程接口结束：出货国家流程撤回流程')

    def click_shipping_country_flow_product_definition_confirm(self):
        """点击新增"""
        self.is_click_tbm(user['产品定义信息确定'])

    def select_shipping_country_flow_signatory(self, choice, name):
        """
        出货国家流程新增页面 - 选择汇签/抄送人员
        :param info: 选择要输入的信息
        :param select: 选择信息内容
        """
        self.is_click_tbm(user['汇签/抄送人员选择框'], choice)
        self.is_click_tbm(user['成员列表清空'], choice)
        self.input_text(user['成员列表输入框'], name)
        sleep(1)
        self.is_click_tbm(user['成员选择'], name)
        self.is_click_tbm(user['成员确定'])

    def click_shipping_country_flow_add_submit(self):
        """点击提交"""
        self.scroll_into_view(user['提交'])
        sleep(0.5)
        self.is_click_tbm(user['提交'])

    def get_shipping_country_flow_info(self, item):
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

    def shipping_country_flow_add_item_info(self, item):
        """
        出货国家流程新增页面 - 项目信息组合
        """
        self.input_shipping_country_flow_add_item_info('品牌', 'Infinix')
        self.input_shipping_country_flow_add_item_info('项目', item)
        self.input_shipping_country_flow_add_item_info('描述', '出货国家流程新增描述test')

    def shipping_country_flow_add_product_definition_info(self, item):
        """
        出货国家流程新增页面 - 产品定义信息组合
        """
        self.click_shipping_country_flow_add()
        self.input_shipping_country_flow_add_product_definition_info('全球版本', '版本1')
        self.input_shipping_country_flow_add_product_definition_info('市场名称', f'市场名称{item}')
        self.input_shipping_country_flow_add_product_definition_info('项目名称', item)
        self.input_shipping_country_flow_add_product_definition_info('MEMORY', '128+8')
        self.input_shipping_country_flow_add_product_definition_info('BANDSTRATEGY', '拉美市场')
        self.input_shipping_country_flow_add_product_definition_info('项目经理', '李小素')
        self.input_shipping_country_flow_add_product_definition_info('aaa', '2G')
        self.input_shipping_country_flow_add_product_definition_info('bbb', 'MT6761')
        self.click_shipping_country_flow_product_definition_confirm()

    def shipping_country_flow_add_flow(self, item):
        """
        出货国家流程新增流程 组合
        """
        self.click_shipping_country_flow_add()
        self.shipping_country_flow_add_item_info(item)
        self.shipping_country_flow_add_product_definition_info(item)
        self.select_shipping_country_flow_signatory('汇签人员', '李小素')
        self.click_shipping_country_flow_add_submit()
        DomAssert(self.driver).assert_att('请求成功')

    def shipping_country_flow_product_department_administrator_review(self, code):
        """
        出货国家流程 新增流程 产品部管理员审核 组合
        """
        self.assert_shipping_country_flow_my_todo_node(code, '产品部管理员审核', True)
        self.enter_shipping_country_flow_onework_edit(code)
        self.click_onework_shipping_country_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_shipping_country_flow_onework()
        self.assert_shipping_country_flow_my_todo_node(code, '产品部汇签', True)

    def shipping_country_flow_product_department_sign(self, code):
        """
        出货国家流程 新增流程 产品部汇签 组合
        """
        self.enter_shipping_country_flow_onework_edit(code)
        self.click_onework_shipping_country_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_shipping_country_flow_onework()
        self.assert_shipping_country_flow_my_todo_node(code, '产品经理修改', True)

    def shipping_country_flow_product_manager_modification(self, code):
        """
        出货国家流程 新增流程 产品经理修改 组合
        """
        self.enter_shipping_country_flow_onework_edit(code)
        querytime = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        self.input_oneworks_shipping_country_flow_product_definition_info('全球版本', '版本2')
        self.input_oneworks_shipping_country_flow_product_definition_info('市场名称', f'市场名称test{querytime}')
        self.input_oneworks_shipping_country_flow_product_definition_info('项目名称', f'项目名称test{querytime}')
        self.input_oneworks_shipping_country_flow_product_definition_info('MEMORY', '64+8')
        self.input_oneworks_shipping_country_flow_product_definition_info('BANDSTRATEGY', '公开市场')
        self.input_oneworks_shipping_country_flow_product_definition_info('项目经理', '李小素')
        self.input_oneworks_shipping_country_flow_product_definition_info('aaa', '1G')
        self.input_oneworks_shipping_country_flow_product_definition_info('bbb', 'G70')
        self.click_onework_shipping_country_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_shipping_country_flow_onework()
        self.assert_shipping_country_flow_my_todo_node(code, '产品部管理员复核', True)

    def shipping_country_flow_product_department_administrator_re_review(self, code):
        """
        出货国家流程 新增流程 产品经理修改 组合
        """

        self.enter_shipping_country_flow_onework_edit(code)
        self.click_onework_shipping_country_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_shipping_country_flow_onework()
        self.assert_shipping_country_flow_my_todo_node(code, '项目经理审批', True)

    def click_onework_shipping_country_flow_agree(self):
        """
        点击同意-确定
        """
        self.frame_exit()
        self.is_click_tbm(user['同意'])
        self.is_click_tbm(user['确定'])
        logging.info('点击同意-确定')

    def assert_shipping_country_flow_my_todo_node(self, code, node, exist=False):
        """
        我的待办页面-断言：成功处理了流程后，我的待办中存在/不存在该条单据在指定审核节点
        @param code:流程编码
        @param node:节点名称
        @param exist:断言存在或者不存在
        """
        self.enter_shipping_country_flow_my_todo()
        actual_node = self.element_text(user['待办列表-我的待办-当前节点'], code)
        if exist is False:
            try:
                assert actual_node != node
                logging.info('断言成功，我的待办中该条单据不存在:{} 节点，实际在:{} 节点'.format(node, actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我的待办中存在该条单据在:{} 审核节点'.format(actual_node))
                raise
            finally:
                self.frame_exit()
        else:
            try:
                assert actual_node == node
                logging.info('断言成功，我的待办中存在该条单据在:{} 审核节点'.format(actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我的待办中该条单据不存在:{} 节点，实际在:{} 节点'.format(node, actual_node))
                raise
            finally:
                self.frame_exit()

    def assert_shipping_country_flow_my_application_node(self, code, node, exist=False):
        """
        我申请的页面-断言：成功处理了流程后，我申请的中存在/不存在该条单据在指定审核节点
        @param code:流程编码
        @param node:节点名称
        @param exist:断言存在或者不存在
        """
        self.enter_shipping_country_flow_my_application()
        actual_node = self.element_text(user['待办列表-我申请的-当前节点'], code)
        if exist is False:
            try:
                assert actual_node != node
                logging.info('断言成功，我申请的中该条单据不存在:{} 节点，实际在:{} 节点'.format(node, actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中存在该条单据在:{} 节点'.format(actual_node))
                raise
            finally:
                self.frame_exit()
        else:
            try:
                assert actual_node == node
                logging.info('断言成功，我申请的中存在该条单据在:{} 审核节点'.format(actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中该条单据不存在:{} 节点，实际在:{} 节点'.format(node, actual_node))
                raise
            finally:
                self.frame_exit()

    def input_oneworks_shipping_country_flow_product_definition_info(self, header, content):
        """
        oneworks-节点：产品经理修改-查看详情页面
        编辑产品定义信息
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
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-编辑'])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-输入框'], definition_dict[header])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-选择'], content)
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-确定'])
        if header in select1_list:
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-编辑'])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-输入框2'], definition_dict[header])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-选择'], content)
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-确定'])
        elif header in input_list:
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-编辑'])
            self.input_text(user['oneworks-节点-产品经理修改-产品定义信息-输入框'], content, definition_dict[header])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-确定'])
        elif header in member_list:
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-编辑'])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-输入框2'], definition_dict[header])
            self.input_text(user['产品定义信息成员列表输入框'], content)
            sleep(1)
            self.is_click_tbm(user['成员选择'], content)
            self.is_click_tbm(user['产品定义信息成员确定'])
            self.is_click_tbm(user['oneworks-节点-产品经理修改-产品定义信息-确定'])
        else:
            print(f'请输入正确选项：{definition_dict}')

    def assert_shipping_country_flow_my_application_flow(self, code, flow, exist=True):
        """
        我申请的页面-断言：成功处理了流程后，我申请的中存在/不存在该条单据在指定流程中
        @param code:流程编码
        @param flow:流程名称
        @param exist:断言存在或者不存在
        """
        self.enter_shipping_country_flow_my_application()
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
                self.frame_exit()
        elif exist is False:
            try:
                assert actual_flow != flow
                logging.info('断言成功，我申请的中该条单据不在:{}流程，实际在:{}流程'.format(flow, actual_flow))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中该条单据在:{}流程'.format(actual_flow))
                raise
            finally:
                self.frame_exit()


if __name__ == '__main__':
    pass
