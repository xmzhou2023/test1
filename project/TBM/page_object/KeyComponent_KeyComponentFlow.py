import datetime
from time import sleep
import allure
import requests
from libs.common.read_element import Element
from project.TBM.api.api import APIRequest
from libs.common.connect_sql import *
from project.TBM.page_object.Center_Component import CenterComponent
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class KeyComponentsFlow(CenterComponent, APIRequest):
    """关键器件_关键器件流程"""

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
        self.click_menu("关键器件", "关键器件流程")

    def quit_key_components_flow_onework(self):
        """
        退出oneworks查看流程页面
        """
        self.frame_exit()
        self.close_switch(1)
        self.refresh()
        self.frame_exit()
        sleep(1)

    def click_key_components_flow_add(self):
        """点击新增"""
        self.is_click_tbm(user['新增'])
        sleep(1)

    def input_key_components_flow_add_item_info(self, info, select):
        """
        关键器件流程新增页面 - 输入项目信息
        :param info: 选择要输入的信息
        :param select: 选择信息内容
        """
        if info == '品牌' or info == '基线名称':
            self.is_click_tbm(user['项目信息输入框'], info)
            logging.info('点击项目信息输入框:{}'.format(info))
            self.scroll_into_view(user['项目信息输入框选择'], select)
            sleep(1)
            self.is_click_tbm(user['项目信息输入框选择'], select)
            logging.info('选择项目信息:{}'.format(select))

        elif info == '项目':
            self.readonly_input_text(user['项目信息输入框'], select, info)
            sleep(1)
            self.is_click_tbm(user['项目信息输入框选择'], select)
            logging.info('选择点击项目信息:{}'.format(select))

        else:
            self.input_text(user['项目信息输入框'], select, info)

    @allure.step("关键器件流程新增页面-项目信息组合")
    def key_components_flow_add_item_info(self):
        self.input_key_components_flow_add_item_info('品牌', 'itel')
        self.input_key_components_flow_add_item_info('项目', '50A1S')
        self.input_key_components_flow_add_item_info('基线名称', '基线GP2325')
        self.input_key_components_flow_add_item_info('平台', '测试平台')
        self.input_key_components_flow_add_item_info('上市时间', '2022-06-20')
        self.input_key_components_flow_add_item_info('月度需求', '1')
        self.input_key_components_flow_add_item_info('总需求', '1')
        self.input_key_components_flow_add_item_info('目标市场', '深圳')
        self.input_key_components_flow_add_item_info('生命周期', '1')

    def select_key_components_flow_business_review(self, type, audit):
        """
        业务审核 - 选择用户
        @param type:选择的类别
        @param audit:输入的用户名
        """
        self.is_click_tbm(user['业务审核类别'], type)
        self.input_text(user['成员列表输入框'], audit)
        sleep(1)
        self.is_click_tbm(user['成员选择'], audit)
        self.is_click_tbm(user['成员确定'])

    @allure.step("关键器件流程新增页面-业务审核组合")
    def key_components_flow_add_business_review(self):
        self.select_key_components_flow_business_review('摄像头+闪光灯', '李小素')
        self.select_key_components_flow_business_review('硬件电子料-基带', '李小素')
        self.select_key_components_flow_business_review('标准化代表', '李小素')
        self.select_key_components_flow_business_review('采购代表', '李小素')

    def click_key_components_flow_submit(self):
        """点击提交"""
        self.is_click_tbm(user['提交'])
        sleep(1)

    @allure.step("关键器件流程新增组合流程")
    def key_components_flow_add(self):
        """
        关键器件流程新增 组合流程
        """
        self.click_key_components_flow_add()
        self.key_components_flow_add_item_info()
        self.key_components_flow_add_business_review()
        self.click_key_components_flow_submit()
        DomAssert(self.driver).assert_att('请求成功')

    def request_key_components_flow_add(self, data, headers):
        """
        TBM 关键器件流程 新增接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程新增接口')
        return self.api_request('关键器件流程新增接口', data, headers)

    def request_key_components_flow_search(self, data, headers):
        """
        TBM 关键器件流程 TBM查询接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程查询接口')
        return self.api_request('关键器件流程查询接口', data, headers)

    @allure.step("关键器件流程新增接口")
    def api_key_components_flow_add(self):
        """
        TBM 关键器件流程新增接口
        """
        logging.info('发起流程接口：关键器件流程新增流程')
        token = self.tbm_login()
        querytime = datetime.datetime.now().strftime('%Y-%m-%d')
        add_data = {
            "flowMainVO": {"flowProposer": "18645960", "flowProposerName": "李小素", "flowDept": "PI_系统四部",
                           "title": f"[50A1S]-[李小素]-[{querytime}]"},
            "deviceVO": {"brand": "itel", "model": "50A1S", "templateBid": "956136840950321152",
                         "basiclineName": "baseline_GP", "platform": "测试平台", "onMarketDate": "2022-06-20",
                         "monthNeeds": "1", "totalNeeds": "1", "targetMarket": "深圳", "lifecycle": "1"},
            "approvers": {
                "domainRole": [{"domainName": "摄像头+闪光灯", "domainCode": "dev_image", "approver": "18645960"},
                               {"domainName": "硬件电子料-基带", "domainCode": "dev_hardware",
                                "approver": "18645960"}],
                "assessRole": [{"domainName": "标准化代表", "domainCode": "standard_deputy", "approver": "18645960"},
                               {"domainName": "采购代表", "domainCode": "purchase_deputy",
                                "approver": "18645960"}]}, "uploadList": [], "saveType": "submit"}
        search_data = {"current": 1, "size": 10, "param": {}}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        add_reponse = self.request_key_components_flow_add(add_data, headers)
        bid = add_reponse['body']['data']['bid']
        search_reponse = self.request_key_components_flow_search(search_data, headers)
        search_reponse_data = search_reponse['body']['data']['data']
        for i in search_reponse_data:
            if i['bid'] == bid:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，bid：{}'.format(i['flowNo'], i['instanceId'], i['bid']))
                logging.info('流程接口结束：关键器件流程新增流程')
                return i['flowNo'], i['instanceId'], i['bid']

    def request_key_components_flow_recall(self, instanceId, headers):
        """
        oneworks TBM 关键器件流程撤回接口
        @param instanceId:oneworks撤回流程编码
        @param headers:接口头部
        """
        logging.info('发起请求：oneworks流程撤回接口')
        logging.info(f'接口请求地址为：http://10.250.112.14:8090/oneworks/base_api/process-center/instance/{instanceId}/revoke')
        recall_response = requests.delete(
            url=f'http://10.250.112.14:8090/oneworks/base_api/process-center/instance/{instanceId}/revoke',
            headers=headers)
        response_dicts = dict()
        response_dicts['body'] = recall_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        return response_dicts

    def request_key_components_flow_delete(self, bid, headers):
        """
        TBM 关键器件流程删除已撤回接口
        @param bid:流程bid
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程删除已撤回接口')
        logging.info(f'接口请求地址为：http://pfgatewayidct.transsion.com:9088/plm-key-device-main/key-device/flow/deleteFlow'
                     f'?flowBid={bid}')
        recall_response = requests.get(
            url=f'http://pfgatewayidct.transsion.com:9088/plm-key-device-main/key-device/flow/deleteFlow?flowBid={bid}',
            headers=headers)
        response_dicts = dict()
        response_dicts['body'] = recall_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        return response_dicts

    @allure.step("关键器件流程撤回删除接口")
    def api_key_components_flow_delete(self, instanceid, bid):
        """
        通过调用接口发起撤回流程
        调用接口：oneworks流程撤回接口，关键器件流程删除已撤回接口
        @param instanceid:oneworks撤回流程编码
        @param bid:流程ID
        """
        logging.info('发起流程接口：关键器件流程撤回流程')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        self.request_key_components_flow_recall(instanceid, headers)
        self.request_key_components_flow_delete(bid, headers)
        logging.info('流程接口结束：关键器件流程撤回流程')

    def get_key_components_flow_info(self):
        """
        获取关键器械第一列内容
        @return:返回文本及索引位置分别是'No.'==0; '流程编码'==1; '流程类型'==2; '项目'==3; '品牌'==4; '单据状态'==5; '申请人'==6; '申请时间'==7; '操作'==8;
        """
        self.click_menu("关键器件", "关键器件流程")
        sleep(1)
        info = self.find_elements_tbm(user['表格内容'])
        infolist = []
        for i in info:
            infolist.append(i.get_attribute('innerText'))
        logging.info('获取表格搜索结果的所有信息文本{}'.format(infolist))
        return infolist

    def enter_key_components_flow_my_application(self):
        """
        进入我申请的页面
        """
        self.click_menu('待办列表', '我申请的')
        self.refresh()
        iframe = self.find_element(user['待办列表-我申请的-iframe'])
        self.driver.switch_to.frame(iframe)
        sleep(1)
        self.is_click_tbm(user['待办列表-刷新'])

    def click_key_components_flow_delete(self, code):
        """
        根据流程编码点击删除 进行删除操作
        @param code:流程编码
        """
        self.is_click_tbm(user['删除'], code)
        self.is_click_tbm(user['确定'])

    def recall_key_components_flow_process(self, code):
        """
        提交流程申请后，在待办列表-我申请的 根据流程编码对流程进行撤回操作
        @param code:流程编码
        """
        self.enter_key_components_flow_my_application()
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
        self.quit_onework()
        self.click_menu("关键器件", "关键器件流程")

    def delete_key_components_flow_flow(self, process_code):
        """
        新建流程后的后置删除处理
        """
        self.recall_key_components_flow_process(process_code)
        self.click_key_components_flow_delete(process_code)
        DomAssert(self.driver).assert_att('删除成功')

    def enter_key_components_flow_my_todo(self):
        """
        进入我的待办页面
        """
        ele = self.element_text(user['当前菜单']).strip()
        if ele == '我的待办':
            iframe = self.find_element(user['待办列表-我申请的-iframe'])
            self.driver.switch_to.frame(iframe)
            sleep(1)
            self.is_click_tbm(user['待办列表-刷新'])
        else:
            self.click_menu('待办列表', '我的待办')
            self.refresh()
            iframe = self.find_element(user['待办列表-我申请的-iframe'])
            self.driver.switch_to.frame(iframe)
            sleep(1)
            self.is_click_tbm(user['待办列表-刷新'])

    def click_key_components_flow_onework_edit(self, code, node):
        """
        进入oneworks-关键器件流程-查看详情页面
        输入流程编码过滤后，根据当前节点名称点击查看详情进入详情页面
        @param code:流程编码
        """
        try:
            self.is_click_tbm(user['待办列表-筛选框'])
            self.input_text(user['待办列表-筛选框-单据号'], code)
            self.is_click_tbm(user['待办列表-筛选框-筛选'])
            self.is_click_tbm(user['待办列表-我申请的-查看详情(节点名称)'], node)
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

    def click_onework_key_components_flow_unfold(self, key):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击指定关键器件左侧三角按钮展开
        @param key:关键器件
        """
        self.is_click_tbm(user['oneworks-节点-维护关键器件-关键器件展开'], key)

    def click_onework_key_components_flow_module(self, module):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击指定物料模块
        @param module:物料模块
        """
        self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块'], module)

    def click_onework_key_components_flow_code_add(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击物料编码右侧的加号
        """
        self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块-物料编码加号'])

    def click_onework_key_components_flow_material_add(self, code):
        """
        oneworks-节点：维护关键器件-查看详情页面
        鼠标悬停在物料右侧，点击加号
        @param code:物料模块
        """
        self.hover(user['oneworks-节点-维护关键器件-物料模块-物料编码按钮组'], code)
        self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块-物料编码按钮组-加号'], code)

    def click_onework_key_components_flow_material_pending_code(self, code):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击待申请编码，打开物料详情（参数）
        @param code:待申请编码
        """
        self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块-物料编码-待申请编码'], code)

    def input_onework_key_components_flow_material_details(self, choice, details):
        """
        oneworks-节点：维护关键器件-查看详情页面
        物料详情-输入物料详情
        @param details:详情
        @param choice:输入框名称
        """
        self.input_text(user['oneworks-节点-维护关键器件-物料模块-物料编码-物料详情'], details, choice)

    def scroll_onework_key_components_flow_material_param(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        物料详情-滚动显示全部参数
        """
        self.scroll_into_view(user['oneworks-节点-物料模块-物料编码-物料详情-参数'])

    def scroll_onework_key_components_flow_material_details(self, param):
        """
        oneworks-节点：维护关键器件-查看详情页面
        物料详情-滚动显示
        """
        self.scroll_into_view(user['oneworks-节点-物料模块-物料编码-物料详情'], param)

    def input_onework_key_components_flow_material_parameter(self, choice, details, mode=True):
        """
        oneworks-节点：维护关键器件-查看详情页面
        物料详情-输入物料参数
        @param details:内容
        @param choice:参数名称
        @param mode:默认True为输入框，如果是选择框则输入False
        """
        if mode is True:
            self.input_text(user['oneworks-节点-维护关键器件-物料模块-物料编码-物料参数'], details, choice)
        else:
            self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块-物料编码-物料参数'], choice)
            self.scroll_into_view(user['oneworks-节点-维护关键器件-物料模块-物料编码-物料参数选择'], details)
            self.is_click_tbm(user['oneworks-节点-维护关键器件-物料模块-物料编码-物料参数选择'], details)

    def onework_key_components_flow_flowone(self, code):
        """
        oneworks-节点：维护关键器件-查看详情页面
        摄像头+闪光灯 页面填写 组合流程
        """
        self.enter_key_components_flow_my_todo()
        self.click_key_components_flow_onework_edit(code, '摄像头+闪光灯')
        self.click_onework_key_components_flow_unfold('摄像头+闪光灯')
        self.click_onework_key_components_flow_module('CTP')
        self.click_onework_key_components_flow_code_add()
        self.click_onework_key_components_flow_material_add('CTP(1供)')
        self.click_onework_key_components_flow_material_pending_code('CTP(1供)')
        self.input_onework_key_components_flow_material_details('物料属性', '属性test')
        self.scroll_onework_key_components_flow_material_param()
        self.input_onework_key_components_flow_material_parameter('技术类型', 'GFF', False)
        self.input_onework_key_components_flow_material_parameter('CG颜色', 'CG颜色test')
        self.input_onework_key_components_flow_material_parameter('接口类型', '接口类型test')
        self.input_onework_key_components_flow_material_parameter('连接方式', '焊接', False)
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_onework()

    def onework_key_components_flow_flowtwo(self, code):
        """
        oneworks-节点：维护关键器件-查看详情页面
        摄像头+闪光灯 页面填写 组合流程
        """
        self.enter_key_components_flow_my_todo()
        self.click_key_components_flow_onework_edit(code, '硬件电子料-基带')
        self.click_onework_key_components_flow_unfold('硬件电子料-基带')
        self.click_onework_key_components_flow_module('CPU')
        self.click_onework_key_components_flow_code_add()
        self.click_onework_key_components_flow_material_add('CPU(1供)')
        self.click_onework_key_components_flow_material_pending_code('CPU(1供)')
        self.input_onework_key_components_flow_material_details('物料属性', '属性test')
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_onework()

    def onework_key_components_flow_flowthree(self, code):
        """
        oneworks-节点：标准化代表-查看详情页面
        页面填写 组合流程
        """
        self.enter_key_components_flow_my_todo()
        self.click_key_components_flow_onework_edit(code, '标准化代表')
        self.click_onework_key_components_flow_checkbox()
        self.click_onework_key_components_flow_onepress()
        self.input_onework_key_components_flow_onepress('责任人', '李小素')
        self.click_onework_key_components_flow_onepress_confirm()
        self.click_onework_key_components_flow_onepress_cancel()
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_onework()

    def onework_key_components_flow_flowfour(self, code):
        """
        oneworks-节点：标准化代表-查看详情页面
        页面填写 组合流程
        """
        self.enter_key_components_flow_my_todo()
        self.click_key_components_flow_onework_edit(code, '采购代表')
        self.click_onework_key_components_flow_checkbox()
        self.click_onework_key_components_flow_onepress()
        self.input_onework_key_components_flow_onepress('资源商务', '李小素')
        self.click_onework_key_components_flow_onepress_confirm()
        self.input_onework_key_components_flow_onepress('采购执行', '李小素')
        self.click_onework_key_components_flow_onepress_confirm()
        self.input_onework_key_components_flow_onepress('采购PTC', '李小素')
        self.click_onework_key_components_flow_onepress_confirm()
        self.input_onework_key_components_flow_onepress('采购SQM', '李小素')
        self.click_onework_key_components_flow_onepress_confirm()
        self.click_onework_key_components_flow_onepress_cancel()
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_onework()

    def onework_key_components_flow_flowfive(self, code):
        """
        oneworks-节点：资源商务评估-查看详情页面
        页面填写 组合流程
        """
        self.enter_key_components_flow_my_todo()
        self.click_key_components_flow_onework_edit(code, '资源商务评估')
        self.click_onework_key_components_flow_unfold('摄像头+闪光灯')
        self.click_onework_key_components_flow_module('CTP')
        self.click_onework_key_components_flow_material_pending_code('CTP(1供)')
        self.input_onework_key_components_flow_procurement_evaluation('供应商名称', 'TEST', False)
        self.input_onework_key_components_flow_procurement_evaluation('是否新供应商', '否', False)
        self.input_onework_key_components_flow_procurement_evaluation('国产化属性', '0', False)
        self.input_onework_key_components_flow_procurement_evaluation('供应商选择原因类别', '成本因素', False)
        self.input_onework_key_components_flow_procurement_evaluation('供应商选择原因', '供应商选择原因TEST')
        self.input_onework_key_components_flow_procurement_evaluation('份额', '50')
        self.input_onework_key_components_flow_procurement_evaluation('是否客供物料', '是', False)
        self.input_onework_key_components_flow_procurement_evaluation('价格趋势（6个月）', '持平', False)
        self.input_onework_key_components_flow_procurement_evaluation('是否NUDD', '是', False)
        self.input_onework_key_components_flow_procurement_evaluation('NUDD说明', 'NUDD说明TEST')
        self.input_onework_key_components_flow_procurement_evaluation('NUDD管理方案', 'NUDD管理方案TEST')
        self.input_onework_key_components_flow_procurement_evaluation('评审结论', '通过', False)
        self.input_onework_key_components_flow_procurement_evaluation('原因及修改建议', '原因及修改建议TEST')
        self.click_onework_key_components_flow_unfold('硬件电子料-基带')
        self.click_onework_key_components_flow_module('CPU')
        self.click_onework_key_components_flow_material_pending_code('CPU(1供)')
        self.input_onework_key_components_flow_procurement_evaluation('供应商名称', 'TEST', False)
        self.input_onework_key_components_flow_procurement_evaluation('是否新供应商', '否', False)
        self.input_onework_key_components_flow_procurement_evaluation('国产化属性', '0', False)
        self.input_onework_key_components_flow_procurement_evaluation('供应商选择原因类别', '成本因素', False)
        self.input_onework_key_components_flow_procurement_evaluation('供应商选择原因', '供应商选择原因TEST')
        self.input_onework_key_components_flow_procurement_evaluation('份额', '50')
        self.input_onework_key_components_flow_procurement_evaluation('是否客供物料', '是', False)
        self.input_onework_key_components_flow_procurement_evaluation('价格趋势（6个月）', '持平', False)
        self.input_onework_key_components_flow_procurement_evaluation('是否NUDD', '是', False)
        self.input_onework_key_components_flow_procurement_evaluation('NUDD说明', 'NUDD说明TEST')
        self.input_onework_key_components_flow_procurement_evaluation('NUDD管理方案', 'NUDD管理方案TEST')
        self.input_onework_key_components_flow_procurement_evaluation('评审结论', '通过', False)
        self.input_onework_key_components_flow_procurement_evaluation('原因及修改建议', '原因及修改建议TEST')
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_onework()

    def onework_key_components_flow_flowsix(self, code):
        """
        oneworks-节点：采购执行评估-查看详情页面
        页面填写 组合流程
        """
        self.enter_key_components_flow_my_todo()
        self.click_key_components_flow_onework_edit(code, '采购执行评估')
        self.click_onework_key_components_flow_unfold('摄像头+闪光灯')
        self.click_onework_key_components_flow_module('CTP')
        self.click_onework_key_components_flow_material_pending_code('CTP(1供)')
        self.scroll_onework_key_components_flow_material_details('采购执行')
        self.input_onework_key_components_flow_procurement_execution('L/T(天)', '1')
        self.input_onework_key_components_flow_procurement_execution('最小下单量(pcs)', '1')
        self.input_onework_key_components_flow_procurement_execution('此项目峰值需求(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('供应商总产能(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('分配传音产能(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('供应弹性(%)', '1')
        self.input_onework_key_components_flow_procurement_execution('共用项目需求合计(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('此项目产能分配(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('共用项目名', '共用项目名test')
        self.input_onework_key_components_flow_procurement_execution('产能评审结论', '通过', False)
        self.input_onework_key_components_flow_procurement_execution('原因及修改建议', '原因及修改建议test')
        self.input_onework_key_components_flow_procurement_execution('备料建议', '备料建议test')
        self.click_onework_key_components_flow_unfold('硬件电子料-基带')
        self.click_onework_key_components_flow_module('CPU')
        self.click_onework_key_components_flow_material_pending_code('CPU(1供)')
        self.scroll_onework_key_components_flow_material_details('采购执行')
        self.input_onework_key_components_flow_procurement_execution('L/T(天)', '1')
        self.input_onework_key_components_flow_procurement_execution('最小下单量(pcs)', '1')
        self.input_onework_key_components_flow_procurement_execution('此项目峰值需求(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('供应商总产能(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('分配传音产能(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('供应弹性(%)', '1')
        self.input_onework_key_components_flow_procurement_execution('共用项目需求合计(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('此项目产能分配(K/M)', '1')
        self.input_onework_key_components_flow_procurement_execution('共用项目名', '共用项目名test')
        self.input_onework_key_components_flow_procurement_execution('产能评审结论', '通过', False)
        self.input_onework_key_components_flow_procurement_execution('原因及修改建议', '原因及修改建议test')
        self.input_onework_key_components_flow_procurement_execution('备料建议', '备料建议test')
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_onework()

    def onework_key_components_flow_ptc(self, code):
        """
        oneworks-节点：采购PTC评估-查看详情页面
        页面填写 组合流程
        """
        self.enter_key_components_flow_my_todo()
        self.click_key_components_flow_onework_edit(code, '采购PTC评估')
        self.click_onework_key_components_flow_unfold('摄像头+闪光灯')
        self.click_onework_key_components_flow_module('CTP')
        self.click_onework_key_components_flow_material_pending_code('CTP(1供)')
        self.scroll_onework_key_components_flow_material_details('PTC')
        self.input_onework_key_components_flow_ptc('评审结论', '同意')
        self.input_onework_key_components_flow_ptc('原因及修改建议', '原因及修改建议test')
        self.click_onework_key_components_flow_unfold('硬件电子料-基带')
        self.click_onework_key_components_flow_module('CPU')
        self.click_onework_key_components_flow_material_pending_code('CPU(1供)')
        self.scroll_onework_key_components_flow_material_details('PTC')
        self.input_onework_key_components_flow_ptc('评审结论', '同意')
        self.input_onework_key_components_flow_ptc('原因及修改建议', '原因及修改建议test')
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_onework()

    def onework_key_components_flow_sqm(self, code):
        """
        oneworks-节点：采购SQM评估-查看详情页面
        页面填写 组合流程
        """
        self.enter_key_components_flow_my_todo()
        self.click_key_components_flow_onework_edit(code, '采购SQM评估')
        self.click_onework_key_components_flow_unfold('摄像头+闪光灯')
        self.click_onework_key_components_flow_module('CTP')
        self.click_onework_key_components_flow_material_pending_code('CTP(1供)')
        self.scroll_onework_key_components_flow_material_details('SQM')
        self.input_onework_key_components_flow_sqm('评审结论', '同意')
        self.input_onework_key_components_flow_sqm('原因及修改建议', '原因及修改建议test')
        self.click_onework_key_components_flow_unfold('硬件电子料-基带')
        self.click_onework_key_components_flow_module('CPU')
        self.click_onework_key_components_flow_material_pending_code('CPU(1供)')
        self.scroll_onework_key_components_flow_material_details('SQM')
        self.input_onework_key_components_flow_sqm('评审结论', '同意')
        self.input_onework_key_components_flow_sqm('原因及修改建议', '原因及修改建议test')
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_onework()

    def onework_key_components_flow_standardized_evaluation(self, code):
        """
        oneworks-节点：标准化部评估-查看详情页面
        页面填写 组合流程
        """
        self.enter_key_components_flow_my_todo()
        self.click_key_components_flow_onework_edit(code, '标准化部评估')
        self.click_onework_key_components_flow_unfold('摄像头+闪光灯')
        self.click_onework_key_components_flow_module('CTP')
        self.click_onework_key_components_flow_material_pending_code('CTP(1供)')
        self.input_onework_key_components_flow_standardized_evaluation('认证状态', '认证通过')
        self.input_onework_key_components_flow_standardized_evaluation('原因及修改建议', '原因及修改建议test')
        self.click_onework_key_components_flow_unfold('硬件电子料-基带')
        self.click_onework_key_components_flow_module('CPU')
        self.click_onework_key_components_flow_material_pending_code('CPU(1供)')
        self.input_onework_key_components_flow_standardized_evaluation('认证状态', '认证通过')
        self.input_onework_key_components_flow_standardized_evaluation('原因及修改建议', '原因及修改建议test')
        self.click_onework_key_components_flow_agree()
        DomAssert(self.driver).assert_att('审核通过')
        self.quit_onework()

    def click_onework_key_components_flow_agree(self):
        """
        点击同意-确定
        """
        self.frame_exit()
        self.is_click_tbm(user['同意'])
        self.is_click_tbm(user['确定'])
        self.base_get_img('result')
        logging.info('点击确定')

    def click_onework_key_components_flow_checkbox(self, sort='all'):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击复选框
        @param sort:物料编码，传入物料编码；默认‘all’表示点击全选复选框
        """
        if sort == 'all':
            self.is_click_tbm(user['oneworks-节点-评估关键器件-复选框全选'])
        else:
            self.is_click_tbm(user['oneworks-节点-评估关键器件-复选框单选'], sort)
        logging.info('点击复选框')

    def click_onework_key_components_flow_onepress(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击一键填写
        """
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写'])

    def click_onework_key_components_flow_onepress_confirm(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击一键填写-确定
        """
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写-确定'])

    def click_onework_key_components_flow_onepress_cancel(self):
        """
        oneworks-节点：维护关键器件-查看详情页面
        点击一键填写-取消
        """
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写-取消'])

    def input_onework_key_components_flow_onepress(self, field, name):
        """
        oneworks-节点：维护关键器件-查看详情页面
        输入一键填写内容
        """
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写-字段名称'])
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写-字段名称选择'], field)
        self.is_click_tbm(user['oneworks-节点-评估关键器件-一键填写-责任人'])
        self.input_text(user['成员列表输入框'], name)
        sleep(1)
        self.is_click_tbm(user['成员选择'], name)
        self.is_click_tbm(user['成员确定'])

    def input_onework_key_components_flow_procurement_evaluation(self, choice, details, mode=True):
        """
        oneworks-节点：资源商务评估-查看详情页面
        物料详情-采购评估
        @param details:内容
        @param choice:参数名称
        @param mode:默认True为输入框，如果是选择框则输入False
        """
        if mode is True:
            self.readonly_input_text(user['oneworks-节点-资源商务评估-采购评估-资源商务-输入框'], details, choice)
        else:
            self.is_click_tbm(user['oneworks-节点-资源商务评估-采购评估-资源商务-输入框'], choice)
            try:
                self.is_click_tbm(user['oneworks-节点-下拉框-选择'], details)
            except:
                self.scroll_into_view(user['oneworks-节点-下拉框-选择'], details)
                self.is_click_tbm(user['oneworks-节点-下拉框-选择'], details)

    def input_onework_key_components_flow_procurement_execution(self, choice, details, mode=True):
        """
        oneworks-节点：采购执行评估-查看详情页面
        物料详情-采购执行
        @param details:内容
        @param choice:参数名称
        @param mode:默认True为输入框，如果是选择框则输入False
        """
        if mode is True:
            self.readonly_input_text(user['oneworks-节点-资源商务评估-采购评估-采购执行-输入框'], details, choice)
        else:
            self.is_click_tbm(user['oneworks-节点-资源商务评估-采购评估-采购执行-输入框'], choice)
            try:
                self.is_click_tbm(user['oneworks-节点-下拉框-选择'], details)
            except:
                self.scroll_into_view(user['oneworks-节点-下拉框-选择'], details)
                self.is_click_tbm(user['oneworks-节点-下拉框-选择'], details)

    def input_onework_key_components_flow_ptc(self, choice, details):
        """
        oneworks-节点：采购PTC评估-查看详情页面
        物料详情-采购PTC评估
        @param details:内容
        @param choice:参数名称
        """
        if choice == '原因及修改建议':
            self.readonly_input_text(user['oneworks-节点-采购PTC评估-采购评估-PTC-输入框'], details, choice)
        elif choice == '评审结论':
            self.is_click_tbm(user['oneworks-节点-采购PTC评估-采购评估-PTC-输入框'], choice)
            self.is_click_tbm(user['oneworks-节点-下拉框-选择'], details)

    def input_onework_key_components_flow_sqm(self, choice, details):
        """
        oneworks-节点：采购SQM评估-查看详情页面
        物料详情-采购SQM评估
        @param details:内容
        @param choice:参数名称
        """
        if choice == '原因及修改建议':
            self.readonly_input_text(user['oneworks-节点-采购PTC评估-采购评估-SQM-输入框'], details, choice)
        elif choice == '评审结论':
            self.is_click_tbm(user['oneworks-节点-采购PTC评估-采购评估-SQM-输入框'], choice)
            self.is_click_tbm(user['oneworks-节点-下拉框-选择'], details)

    def input_onework_key_components_flow_standardized_evaluation(self, choice, details):
        """
        oneworks-节点：标准化评估-查看详情页面
        物料详情-标准化评估
        @param details:内容
        @param choice:参数名称
        """
        if choice == '原因及修改建议':
            self.readonly_input_text(user['oneworks-节点-标准化部评估-标准化评估-文本框'], details, choice)
        elif choice == '认证状态' or '评审结论':
            self.is_click_tbm(user['oneworks-节点-标准化部评估-标准化评估-输入框'], choice)
            self.is_click_tbm(user['oneworks-节点-下拉框-选择'], details)

    def assert_key_components_flow_my_application_node(self, code, node, exist=False):
        """
        我申请的页面-断言：成功处理了流程后，我申请的中存在/不存在该条单据在指定审核节点
        @param code:流程编码
        @param node:节点名称
        @param exist:断言存在或者不存在
        """
        self.enter_key_components_flow_my_application()
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
                self.frame_exit()
        else:
            try:
                assert actual_node == node
                logging.info('断言成功，我申请的中存在该条单据在:{}审核节点'.format(actual_node))
            except:
                self.base_get_img()
                logging.error('断言失败，我申请的中不存在该条单据在:{}审核节点'.format(actual_node))
                raise
            finally:
                self.frame_exit()

    def assert_key_components_flow_my_application_flow(self, code, flow, exist=True):
        """
        我申请的页面-断言：成功处理了流程后，我申请的中存在/不存在该条单据在指定流程中
        @param code:流程编码
        @param flow:流程名称
        @param exist:断言存在或者不存在
        """
        self.enter_key_components_flow_my_application()
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

    @staticmethod
    def delete_key_components_flow_sql(model):
        """
        使用sql脚本修改删除流程数据
        """
        a = SQL('TBM', 'test')
        a.change_db(
            f"UPDATE kd_flow_main SET is_deleted = 1 WHERE device_bid IN ( SELECT bid FROM kd_device_info WHERE model "
            f"= '{model}')",
        )
        logging.info('调用sql脚本修改数据库数据')


if __name__ == '__main__':
    pass
