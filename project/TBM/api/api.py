#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/6/17
# @Author : ***
# @File : api.py
# @Software: PyCharm
import datetime

import allure
import requests
import logging
from libs.common.read_config import *

pro_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).split('\\')[-1]
pro_env = 'test' # 需要手动配置测试环境
ini = ReadConfig(pro_name, pro_env)

class APIRequest:

    def api_request(self, request, data=None, headers=None, method='post'):
        """
        接口请求方法
        @param request:接口地址
        @param data:接口body
        @param headers:接口头部
        @param method:接口方式，待补充
        """
        logging.info('接口请求地址为：%s', eval(ini._get('API', request)))
        global response
        if method == 'post':
            response = requests.post(url=eval(ini._get('API', request)),
                                     json=data,
                                     headers=headers)
        elif method == 'delete':
            response = requests.delete(url=eval(ini._get('API', request)),
                                       headers=headers)
        response_dicts = dict()
        response_dicts['body'] = response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        return response_dicts

    def tbm_login(self):
        """
        TBM登录接口
        return token
        """
        logging.info('发起请求：TBM登录接口')
        data = {'lang': 'zh', 'pwd': 'eExpbHk2eA==', 'username': '18645960', 'privacyAgreement': 'true',
                'redirect': 'http://bom-sit.transsion.com', 'source': 'TBM',
                'verifyKey': 'edbae420160748f48107e693ffeb1582', 'readVersion': '1.1.0'}
        headers = {'Content-Type': 'application/json'}
        response = self.api_request('TBM登录接口', data, headers)
        token = response['body']['data']['token']
        logging.info('获取token：%s', token)
        return token

    def Request_Machine_Add(self, data, headers):
        """
        TBM BOM整机协作 TBM新增接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：整机BOM协作新增接口')
        return self.api_request('整机BOM协作新增接口', data, headers)

    def Request_Machine_Search(self, data, headers):
        """
        TBM BOM整机协作 TBM查询接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：整机BOM协作查询接口')
        return self.api_request('整机BOM协作查询接口', data, headers)

    def Oneworks_Recall(self, instanceId, headers):
        """
        oneworks TBM BOM协作流程撤回接口
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

    def Request_Machine_Delete(self, data, headers):
        """
        TBM BOM协作 TBM删除已撤回流程接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：整机BOM协作删除已撤回接口')
        return self.api_request('整机BOM协作删除已撤回接口', data, headers)

    @allure.step("整机BOM协作新增接口")
    def API_Machine_Add(self):
        """
        TBM BOM整机BOM协作新增接口
        """
        logging.info('发起流程：整机BOM协作新增流程')
        token = self.tbm_login()
        querytime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        add_data = {"flowId": 'null', "flowNodeName": "start",
                    "bomArchive": {"flowNo": "", "flowProposer": "18645960", "flowProposerName": "李小素",
                                   "flowStartdate": querytime, "bomVer": "", "bomVersion": "trial", "brandCode": "itel",
                                   "market": "ET", "produceClass": "prod", "templateId": 1017732,
                                   "templateName": "itel智能机整机模板", "isLocalPurchase": "", "bomClass": "",
                                   "model": "X572-1",
                                   "note": "", "title": f"[李小素]-[{querytime[:10]}]", "researchType": "selfResearch",
                                   "flowDept": "PI_系统四部"}, "bomDeriveList": [], "bomTreeVOList": [
                {"id": "new_bom_3000", "matGroup": "107,100,110", "bomName": "产成品", "statusCode": "trial",
                 "baseQty": "1000", "applyScope": "domesticProd", "nodeClass": "actual", "businessRole": "market",
                 "tempNodeId": 3713, "childNodes": [
                    {"id": "new_bom_3001", "matGroup": "120,130", "bomName": "单机头", "nodeClass": "actual",
                     "businessRole": "opmPm", "tempNodeId": 3714, "childNodes": [], "index": 0, "serialNo": "1.1"},
                    {"id": "new_bom_3002", "bomName": "配件", "nodeClass": "manage", "tempNodeId": 3715, "childNodes": [
                        {"id": "new_bom_3003", "matGroup": "251", "bomName": "充电器", "nodeClass": "actual",
                         "businessRole": "preResearch", "tempNodeId": 3716, "childNodes": [
                            {"id": 1020, "matGroup": "251", "usePercent": "20", "replaceGroup": "A1", "baseQty": "1000",
                             "matCode": "10000011", "note": "1单机头(8G卡)1电池1充电器1USB数据线1耳机1网套1套包材", "matAttr": "可选",
                             "index": 0, "serialNo": "1.2.1.1", "deleteValidate": 'false'},
                            {"id": 1021, "usePercent": "80", "replaceGroup": "A1", "baseQty": "1000", "index": 1,
                             "serialNo": "1.2.1.2", "matCode": "10000012", "deleteValidate": 'false',
                             "note": "1单机头(8G)1电池1充电器1数据线1耳机1网套1套包材", "matAttr": "可选"}], "index": 0,
                         "serialNo": "1.2.1", "deleteValidate": 'false'},
                        {"id": "new_bom_3004", "matGroup": "253", "bomName": "数据线", "nodeClass": "actual",
                         "businessRole": "preResearch", "tempNodeId": 3717, "childNodes": [], "index": 1,
                         "serialNo": "1.2.2"},
                        {"id": "new_bom_3005", "matGroup": "250", "bomName": "电池", "nodeClass": "actual",
                         "businessRole": "preResearch", "tempNodeId": 3718, "childNodes": [], "index": 2,
                         "serialNo": "1.2.3"},
                        {"id": "new_bom_3006", "matGroup": "252", "bomName": "耳机", "nodeClass": "actual",
                         "businessRole": "audio", "tempNodeId": 3719, "childNodes": [], "index": 3,
                         "serialNo": "1.2.4"},
                        {"id": "new_bom_3007", "matGroup": "256", "bomName": "保护壳", "nodeClass": "actual",
                         "businessRole": "structure", "tempNodeId": 3720, "childNodes": [], "index": 4,
                         "serialNo": "1.2.5"},
                        {"id": "new_bom_3008", "matGroup": "235", "bomName": "取卡针", "nodeClass": "actual",
                         "businessRole": "market", "tempNodeId": 3721, "childNodes": [], "index": 5,
                         "serialNo": "1.2.6"}], "index": 1, "serialNo": "1.2"},
                    {"id": "new_bom_3009", "bomName": "包材", "nodeClass": "manage", "tempNodeId": 3722, "childNodes": [
                        {"id": "new_bom_3010", "matGroup": "238", "bomName": "标贴", "nodeClass": "actual",
                         "businessRole": "market,pilot", "tempNodeId": 3723, "childNodes": [], "index": 0,
                         "serialNo": "1.3.1"},
                        {"id": "new_bom_3011", "matGroup": "275", "bomName": "卡通箱", "nodeClass": "actual",
                         "businessRole": "market", "tempNodeId": 3724, "childNodes": [], "index": 1,
                         "serialNo": "1.3.2"},
                        {"id": "new_bom_3012", "matGroup": "271", "bomName": "包装盒", "nodeClass": "actual",
                         "businessRole": "market", "tempNodeId": 3725, "childNodes": [], "index": 2,
                         "serialNo": "1.3.3"},
                        {"id": "new_bom_3013", "matGroup": "273", "bomName": "配件盒", "nodeClass": "actual",
                         "businessRole": "market", "tempNodeId": 3726, "childNodes": [], "index": 3,
                         "serialNo": "1.3.4"},
                        {"id": "new_bom_3014", "matGroup": "236", "bomName": "保护膜", "nodeClass": "actual",
                         "businessRole": "market", "tempNodeId": 3727, "childNodes": [], "index": 4,
                         "serialNo": "1.3.5"},
                        {"id": "new_bom_3015", "matGroup": "274", "bomName": "说明书", "nodeClass": "actual",
                         "businessRole": "ROLE1", "tempNodeId": 3728, "childNodes": [], "index": 5,
                         "serialNo": "1.3.6"},
                        {"id": "new_bom_3016", "matGroup": "276", "bomName": "保修卡", "nodeClass": "actual",
                         "businessRole": "market", "tempNodeId": 3729, "childNodes": [], "index": 6,
                         "serialNo": "1.3.7"},
                        {"id": "new_bom_3017", "matGroup": "257", "bomName": "PE袋", "nodeClass": "actual",
                         "businessRole": "market", "tempNodeId": 3730, "childNodes": [], "index": 7,
                         "serialNo": "1.3.8"},
                        {"id": "new_bom_3018", "matGroup": "278", "bomName": "其他包材", "nodeClass": "actual",
                         "businessRole": "market,pilot", "tempNodeId": 3731, "childNodes": [], "index": 8,
                         "serialNo": "1.3.9"}], "index": 2, "serialNo": "1.3"}], "isRoot": 'true', "index": 0,
                 "serialNo": 1, "matCode": "10026418", "deleteValidate": 'false',
                 "note": "整机_Infinix_X695D_H854_N1_7度紫_PH_128+8_Ⅰ", "matAttr": "可选"}], "approvers": {
                "bisReviewApprovers": [{"role": "nps", "userNo": "18645960"}, {"role": "pmSuper", "userNo": ""},
                                       {"role": "qpm", "userNo": ""}],
                "bisSupplyApprovers": [{"role": "market", "userNo": ""}, {"role": "preResearch", "userNo": ""},
                                       {"role": "audio", "userNo": ""}, {"role": "structure", "userNo": ""},
                                       {"role": "pilot", "userNo": ""}, {"role": "ROLE1", "userNo": ""},
                                       {"role": "mpm", "userNo": "18645960"}]}, "uploadList": [],
                    "submitType": "submit"}
        search_data = {
            "param": {"title": "", "flowNo": "", "bomCode": "", "produceClass": "", "model": "", "brandCode": "",
                      "bomVer": "", "market": "", "statusCode": "", "synStatus": "", "createdBy": "",
                      "createdTimeFrom": "", "createdTimeTo": ""}, "current": 1, "size": 10}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        add_reponse = self.Request_Machine_Add(add_data, headers)
        flowId = add_reponse['body']['data']
        search_reponse = self.Request_Machine_Search(search_data, headers)
        search_reponse_data = search_reponse['body']['data']['data']
        for i in search_reponse_data:
            if i['flowId'] == flowId:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，FlowID：{}'.format(i['flowNo'], i['instanceId'], flowId))
                logging.info('流程结束：整机BOM协作新增流程')
                return i['flowNo'], i['instanceId'], flowId

    @allure.step("整机头BOM协作撤回删除接口")
    def API_Machine_Delete(self, instanceid, flowid):
        """
        TBM BOM协作 oneworks撤回接口 TBM删除已撤回流程接口
        @param instanceid:oneworks撤回流程编码
        @param flowid:流程ID
        """
        logging.info('发起流程：整机BOM协作撤回流程')
        token = self.tbm_login()
        delete_data = {"id": flowid}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        self.Oneworks_Recall(instanceid, headers)
        self.Request_Machine_Delete(delete_data, headers)
        logging.info('流程结束：整机BOM协作撤回流程')

    def Request_BarePhone_Add(self, data, headers):
        """
        TBM 单机头BOM协作 新增接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：单机头BOM协作新增接口')
        return self.api_request('单机头BOM协作新增接口', data, headers)

    def Request_BarePhone_Search(self, data, headers):
        """
        TBM 单机头BOM协作 TBM查询接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：单机头BOM协作查询接口')
        return self.api_request('单机头BOM协作查询接口', data, headers)

    def Request_BarePhone_Delete(self, data, headers):
        """
        TBM 单机头BOM协作删除已撤回接口
        @param data:oneworks撤回流程编码
        @param headers:接口头部
        """
        logging.info('发起请求：单机头BOM协作查询接口')
        return self.api_request('单机头BOM协作删除已撤回接口', data, headers)

    @allure.step("单机头BOM协作新增接口")
    def API_BarePhone_Add(self):
        """
        TBM 单机头BOM协作新增接口
        """
        logging.info('发起流程接口：单机头BOM协作新增流程')
        token = self.tbm_login()
        titletime = datetime.datetime.now().strftime('%Y-%m-%d')
        flowStartdate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        add_data = {"flowId": 'null', "flowNodeName": "start",
                    "bomArchive": {"flowNo": "", "flowProposer": "18645960", "flowProposerName": "李小素",
                                   "flowStartdate": f"{flowStartdate}", "bomVer": "", "bomVersion": "trial",
                                   "brandCode": "itel", "market": "ET", "produceClass": "singleHead",
                                   "templateId": 1017733, "templateName": "itel单机头", "isLocalPurchase": "",
                                   "bomClass": "", "model": "X572-1", "note": "", "title": f"[李小素]-[{titletime}]",
                                   "researchType": "selfResearch", "flowDept": "PI_系统四部", "doDeriveSame": 'false',
                                   "curFlowCode": "structureStart"}, "bomDeriveList": [], "otherDeriveList": [],
                    "bomTreeVOList": [{"id": "new_bom_3000", "matGroup": "120", "bomName": "单机头", "statusCode": "trial",
                                       "baseQty": "1000", "nodeClass": "actual",
                                       "businessRole": "qpm,pm,mpm,structure,hardware,screenage,audio,preResearch,cmf,pilot,nps",
                                       "tempNodeId": 3732, "childNodes": [
                            {"id": "new_bom_3001", "matGroup": "121", "bomName": "PCBA", "nodeClass": "actual",
                             "businessRole": "hardware", "tempNodeId": 3733, "childNodes": [], "index": 0,
                             "serialNo": "1.1"},
                            {"id": "new_bom_3002", "matGroup": "250", "bomName": "电池", "nodeClass": "actual",
                             "businessRole": "preResearch", "tempNodeId": 3734, "childNodes": [], "index": 1,
                             "serialNo": "1.2"},
                            {"id": "new_bom_3003", "matGroup": "176", "bomName": "指纹模组", "nodeClass": "actual",
                             "businessRole": "preResearch", "tempNodeId": 3735, "childNodes": [], "index": 2,
                             "serialNo": "1.3"},
                            {"id": "new_bom_3004", "matGroup": "232", "bomName": "镜片", "nodeClass": "actual",
                             "businessRole": "structure", "tempNodeId": 3736, "childNodes": [], "index": 3,
                             "serialNo": "1.4"},
                            {"id": "new_bom_3005", "matGroup": "123", "bomName": "虚拟共用件", "nodeClass": "actual",
                             "businessRole": "structure", "tempNodeId": 3737, "childNodes": [
                                {"id": "new_bom_3006", "matGroup": "172", "bomName": "摄像头", "nodeClass": "actual",
                                 "businessRole": "structure", "tempNodeId": 3738, "childNodes": [], "index": 0,
                                 "serialNo": "1.5.1"},
                                {"id": "new_bom_3007", "matGroup": "195", "bomName": "听筒", "nodeClass": "actual",
                                 "businessRole": "structure", "tempNodeId": 3739, "childNodes": [], "index": 1,
                                 "serialNo": "1.5.2"}], "index": 4, "serialNo": "1.5"}], "isRoot": 'true', "index": 0,
                                       "serialNo": 1, "matCode": "12012025", "deleteValidate": 'false',
                                       "note": "单机头_itel_it2173_G1812_B_深蓝_RU_4+4", "matAttr": "可选"}],
                    "bomDeriveTreeVOList": [], "approvers": {"bisReviewApprovers": [], "bisSupplyApprovers": [
                {"role": "mpm", "userNo": "18645960"}, {"role": "pm", "userNo": ""}, {"role": "cmf", "userNo": ""},
                {"role": "qpm", "userNo": ""}, {"role": "structure", "userNo": ""}, {"role": "hardware", "userNo": ""},
                {"role": "screenage", "userNo": ""}, {"role": "audio", "userNo": ""},
                {"role": "preResearch", "userNo": ""}, {"role": "pilot", "userNo": ""}, {"role": "nps", "userNo": ""}]},
                    "uploadList": [], "submitType": "submit"}
        search_data = {
            "param": {"title": "", "flowNo": "", "bomCode": "", "produceClass": "", "model": "", "brandCode": "",
                      "bomVer": "", "market": "", "statusCode": "", "synStatus": "", "createdBy": "",
                      "createdTimeFrom": "", "createdTimeTo": "", "bomType": "singleHeadBom"}, "current": 1, "size": 10}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        add_reponse = self.Request_BarePhone_Add(add_data, headers)
        flowId = add_reponse['body']['data']
        search_reponse = self.Request_BarePhone_Search(search_data, headers)
        search_reponse_data = search_reponse['body']['data']['data']
        for i in search_reponse_data:
            if i['flowId'] == flowId:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，bid：{}'.format(i['flowNo'], i['instanceId'], i['flowId']))
                logging.info('流程接口结束：单机头BOM协作新增流程')
                return i['flowNo'], i['instanceId'], i['flowId']

    @allure.step("单机头BOM协作撤回删除接口")
    def API_BarePhone_Delete(self, instanceid, flowid):
        """
        通过调用接口发起撤回流程
        调用接口：oneworks流程撤回接口，单机头BOM协作删除已撤回接口
        @param instanceid:oneworks撤回流程编码
        @param flowid:流程ID
        """
        logging.info('发起流程接口：单机头BOM协作撤回流程')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        delete_data = {"id": flowid}
        self.Oneworks_Recall(instanceid, headers)
        self.Request_BarePhone_Delete(delete_data, headers)
        logging.info('流程接口结束：单机头BOM协作撤回流程')

    def Request_Components_Add(self, data, headers):
        """
        TBM 关键器件流程 新增接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程新增接口')
        return self.api_request('关键器件流程新增接口', data, headers)

    def Request_Components_Search(self, data, headers):
        """
        TBM 关键器件流程 TBM查询接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程查询接口')
        return self.api_request('关键器件流程查询接口', data, headers)

    def Request_Components_Delete(self, bid, headers):
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

    @allure.step("关键器件流程新增接口")
    def API_Components_Add(self):
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
        add_reponse = self.Request_Components_Add(add_data, headers)
        bid = add_reponse['body']['data']['bid']
        search_reponse = self.Request_Components_Search(search_data, headers)
        search_reponse_data = search_reponse['body']['data']['data']
        for i in search_reponse_data:
            if i['bid'] == bid:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，bid：{}'.format(i['flowNo'], i['instanceId'], i['bid']))
                logging.info('流程接口结束：关键器件流程新增流程')
                return i['flowNo'], i['instanceId'], i['bid']

    @allure.step("关键器件流程撤回删除接口")
    def API_Components_Delete(self, instanceid, bid):
        """
        通过调用接口发起撤回流程
        调用接口：oneworks流程撤回接口，关键器件流程删除已撤回接口
        @param instanceid:oneworks撤回流程编码
        @param bid:流程ID
        """
        logging.info('发起流程接口：关键器件流程撤回流程')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        self.Oneworks_Recall(instanceid, headers)
        self.Request_Components_Delete(bid, headers)
        logging.info('流程接口结束：关键器件流程撤回流程')

    def Request_Shipping_Add(self, data, headers):
        """
        TBM 出货国家流程 新增接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家流程新增接口')
        return self.api_request('出货国家流程新增接口', data, headers)

    def Request_Shipping_Search(self, data, headers):
        """
        TBM 出货国家流程 TBM查询接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家流程查询接口')
        return self.api_request('出货国家流程查询接口', data, headers)

    def Request_Shipping_Delete(self, data, headers):
        """
        TBM 出货国家流程删除已撤回接口
        @param instanceId:oneworks撤回流程编码
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家流程删除已撤回接口')
        return self.api_request('出货国家流程删除已撤回接口', data, headers)

    @allure.step("出货国家流程新增接口")
    def API_Shipping_Add(self):
        """
        TBM 出货国家流程新增接口
        """
        logging.info('发起流程接口：出货国家流程新增流程')
        token = self.tbm_login()
        titletime = datetime.datetime.now().strftime('%Y-%m-%d')
        flowStartdate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        querytime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        add_data = {
            "prdInfoVOS": [{"scPrdBaseInfoVO": {"bizType": "create", "globalVersion": "ver1",
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
        self.Request_Shipping_Add(add_data, headers)
        search_reponse = self.Request_Shipping_Search(search_data, headers)
        search_reponse_data = search_reponse['body']['data']['data']
        logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，bid：{}'.format(search_reponse_data[0]['flowNo'], search_reponse_data[0]['instanceId'], search_reponse_data[0]['bid']))
        logging.info('流程接口结束：出货国家流程新增流程')
        return search_reponse_data[0]['flowNo'], search_reponse_data[0]['instanceId'], search_reponse_data[0]['bid']

    @allure.step("出货国家流程撤回删除接口")
    def API_Shipping_Delete(self, instanceid, bid):
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
        self.Oneworks_Recall(instanceid, headers)
        self.Request_Shipping_Delete(delete_data, headers)
        logging.info('流程接口结束：出货国家流程撤回流程')
if __name__ == '__main__':
    a = APIRequest()
