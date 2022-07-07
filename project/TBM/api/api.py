#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/6/17
# @Author : ***
# @File : api.py
# @Software: PyCharm
import datetime
import requests
import logging
from libs.common.read_config import *


class APIRequest:

    def api_request(self, request, data=None, headers=None, method='post'):
        """
        接口请求方法
        @param request:接口地址
        @param data:接口body
        @param headers:接口头部
        @param method:接口方式，待补充
        """
        logging.info('接口请求地址为：%s', eval(ini._get(API, request)))
        global response
        if method == 'post':
            response = requests.post(url=eval(ini._get(API, request)),
                                     json=data,
                                     headers=headers)
        elif method == 'delete':
            response = requests.delete(url=eval(ini._get(API, request)),
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

    def tbm_machine_bom_cooperation_add(self, data, headers):
        """
        TBM BOM整机协作 TBM新增接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：整机BOM协作新增接口')
        return self.api_request('整机BOM协作新增接口', data, headers)

    def tbm_machine_bom_cooperation_search(self, data, headers):
        """
        TBM BOM整机协作 TBM查询接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：整机BOM协作查询接口')
        return self.api_request('整机BOM协作查询接口', data, headers)

    def tbm_machine_bom_cooperation_add_flow(self):
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
                 "serialNo": 1, "matCode": "10000010", "deleteValidate": 'false',
                 "note": "1单机头(无卡)1移动电源1充电器1数据线1耳机1皮套1套包材", "matAttr": "可选"}], "approvers": {
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
        add_reponse = self.tbm_machine_bom_cooperation_add(add_data, headers)
        flowId = add_reponse['body']['data']
        search_reponse = self.tbm_machine_bom_cooperation_search(search_data, headers)
        search_reponse_data = search_reponse['body']['data']['data']
        for i in search_reponse_data:
            if i['flowId'] == flowId:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，FlowID：{}'.format(i['flowNo'], i['instanceId'], flowId))
                logging.info('流程结束：整机BOM协作新增流程')
                return i['flowNo'], i['instanceId'], flowId

    def tbm_machine_bom_cooperation_recall(self, instanceId, headers):
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

    def tbm_oneworks_recall(self, instanceId, headers):
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

    def tbm_machine_bom_cooperation_delete(self, data, headers):
        """
        TBM BOM协作 TBM删除已撤回流程接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：整机BOM协作删除已撤回接口')
        return self.api_request('整机BOM协作删除已撤回接口', data, headers)

    def tbm_machine_bom_cooperation_recall_flow(self, instanceid, flowid):
        """
        TBM BOM协作 oneworks撤回接口 TBM删除已撤回流程接口
        @param instanceid:oneworks撤回流程编码
        @param flowid:流程ID
        """
        logging.info('发起流程：整机BOM协作撤回流程')
        token = self.tbm_login()
        delete_data = {"id": flowid}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        self.tbm_machine_bom_cooperation_recall(instanceid, headers)
        self.tbm_machine_bom_cooperation_delete(delete_data, headers)
        logging.info('流程结束：整机BOM协作撤回流程')


if __name__ == '__main__':
    a = APIRequest()
    a.tbm_machine_bom_cooperation_add_flow()
