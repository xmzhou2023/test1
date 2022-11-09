#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/6/17
# @Author : ***
# @File : api.py
# @Software: PyCharm
from datetime import datetime

import allure
import requests
import logging

from libs.common.read_config import *
from libs.common.time_ui import sleep

pro_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).split('\\')[-1]
pro_env = 'test'  # 需要手动配置测试环境
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
        response_dicts = response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        return response_dicts

    @allure.step("TBM登录接口")
    def tbm_login(self, username='18645960'):
        """
        return token
        """
        logging.info('发起请求：TBM登录接口')
        data = {'lang': 'zh', 'pwd': 'eExpbHk2eA==', 'username': username, 'privacyAgreement': 'true',
                'redirect': 'http://bom-sit.transsion.com', 'source': 'TBM',
                'verifyKey': 'edbae420160748f48107e693ffeb1582', 'readVersion': '1.1.0'}
        headers = {'Content-Type': 'application/json'}
        response = self.api_request('TBM登录接口', data, headers)
        token = response['data']['token']
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

    def Request_Bom_Search(self, data, headers):
        """
        TBM BOM协作 TBM查询接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：BOM协作查询接口')
        return self.api_request('BOM协作查询接口', data, headers)

    @allure.step("Oneworks撤回接口")
    def Oneworks_Recall(self, instanceId, headers):
        """
        oneworks TBM BOM协作流程撤回接口
        @param instanceId:oneworks撤回流程编码
        @param headers:接口头部
        """
        logging.info('发起请求：oneworks流程撤回接口')
        logging.info(f'接口请求地址为：https://pfgatewayidct.transsion.com:9188/process-center/process-center/instance/{instanceId}/revoke')
        recall_response = requests.delete(
            url=f'https://pfgatewayidct.transsion.com:9188/process-center/process-center/instance/{instanceId}/revoke',
            headers=headers)
        response_dicts = recall_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        return response_dicts

    def Request_Bom_Delete(self, data, headers):
        """
        TBM BOM协作 TBM删除已撤回流程接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：BOM协作删除已撤回接口')
        return self.api_request('BOM协作删除已撤回接口', data, headers)

    def Request_Machine_Factory(self, data, headers):
        """
        TBM 整机BOM协作 oneworks 补充工厂
        @param data: 接口body
        @param headers:接口头部
        """
        logging.info('发起请求：整机BOM协作补充工厂接口')
        return self.api_request('整机BOM协作补充工厂接口', data, headers)

    def Request_Machine_bomEnginner(self, data, headers):
        """
        TBM 整机BOM协作 oneworks BOM工程师审批
        @param data: 接口body
        @param headers:接口头部
        """
        logging.info('发起请求：整机BOM协作BOM工程师审批接口')
        return self.api_request('整机BOM协作BOM工程师审批接口', data, headers)

    def Request_Machine_Approve(self, data, headers):
        """
        TBM 整机BOM协作 oneworks 务审核
        @param data: 接口body
        @param headers:接口头部
        """
        logging.info('发起请求：整机BOM协作业务审核接口')
        return self.api_request('整机BOM协作业务审核接口', data, headers)

    @allure.step("整机BOM协作新增接口")
    def API_Machine_Add(self):
        logging.info('发起流程：整机BOM协作新增流程')
        token = self.tbm_login()
        querytime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        add_data = {"flowId": None, "flowNodeName": "start",
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
        add_response = self.Request_Machine_Add(add_data, headers)
        flowId = add_response['data']
        search_response = self.Request_Bom_Search(search_data, headers)
        search_response_data = search_response['data']['data']
        for i in search_response_data:
            if i['flowId'] == flowId:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，FlowID：{}'.format(i['flowNo'], i['instanceId'], flowId))
                logging.info('流程结束：整机BOM协作新增流程')
                return i['flowNo'], i['instanceId'], flowId

    @allure.step("整机BOM协作新增接口")
    def API_Derive_Machine_Add(self):
        logging.info('发起流程：整机BOM协作新增流程')
        token = self.tbm_login()
        querytime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        add_data = {
            "flowId": None,
            "flowNodeName": "start",
            "bomArchive": {
                "flowNo": "",
                "flowProposer": "18645960",
                "flowProposerName": "李小素",
                "flowStartdate": querytime,
                "bomVer": "",
                "bomVersion": "batch",
                "brandCode": "infinix",
                "market": "ET",
                "produceClass": "derive",
                "templateId": 1017718,
                "templateName": "q",
                "isLocalPurchase": "",
                "bomClass": "",
                "model": "X572-1",
                "note": "",
                "title": f"[李小素]-[{querytime[:10]}]",
                "researchType": "selfResearch",
                "flowDept": "PI_系统四部"
            },
            "bomDeriveList": [
                {
                    "row": 1,
                    "checkResultMessage": "",
                    "newBomType": "deliver",
                    "newBomCode": "11000002",
                    "newBomName": "CKD_itel_A44_F3706_玫瑰金_IN_BCFL_8+1_P05_E",
                    "originalBomCode": "10026373",
                    "originalBomName": "整机_Infinix_PR652C_F6319_B1_海洋之心32+2_欧规_Ⅰ",
                    "originalBomFactory": "PL01",
                    "rightNewBomName": "CKD_itel_A44_F3706_玫瑰金_IN_BCFL_8+1_P05_E",
                    "rightOriginalBomName": "整机_Infinix_PR652C_F6319_B1_海洋之心32+2_欧规_Ⅰ",
                    "statusCode": None,
                    "diffColor": None,
                    "diffMarket": None,
                    "diffConfig": None,
                    "no": "",
                    "repeat": True,
                    "newBomTypeLabel": "发货BOM"
                }
            ],
            "bomTreeVOList": [],
            "approvers": {
                "bisReviewApprovers": [
                    {
                        "role": "audio",
                        "userNo": "18645960"
                    },
                    {
                        "role": "market",
                        "userNo": ""
                    },
                    {
                        "role": "nps",
                        "userNo": ""
                    },
                    {
                        "role": "opmPm",
                        "userNo": ""
                    },
                    {
                        "role": "pilot",
                        "userNo": ""
                    },
                    {
                        "role": "pmSuper",
                        "userNo": ""
                    },
                    {
                        "role": "preResearch",
                        "userNo": ""
                    },
                    {
                        "role": "qpm",
                        "userNo": ""
                    },
                    {
                        "role": "structure",
                        "userNo": ""
                    }
                ],
                "bisSupplyApprovers": [
                    {
                        "role": "mpm",
                        "userNo": "18645960"
                    }
                ]
            },
            "uploadList": [],
            "submitType": "submit"
        }
        search_data = {
            "param": {"title": "", "flowNo": "", "bomCode": "", "produceClass": "", "model": "", "brandCode": "",
                      "bomVer": "", "market": "", "statusCode": "", "synStatus": "", "createdBy": "",
                      "createdTimeFrom": "", "createdTimeTo": ""}, "current": 1, "size": 10}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        add_response = self.Request_Machine_Add(add_data, headers)
        flowId = add_response['data']
        search_response = self.Request_Bom_Search(search_data, headers)
        search_response_data = search_response['data']['data']
        for i in search_response_data:
            if i['flowId'] == flowId:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，FlowID：{}'.format(i['flowNo'], i['instanceId'], flowId))
                logging.info('流程结束：整机BOM协作新增流程')
                return i['flowNo'], i['instanceId'], flowId

    @allure.step("整机BOM协作-补充工厂审批通过接口")
    def API_Machine_Factory(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：整机BOM协作-补充工厂审批通过流程')
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        MachineInfo = self.Oneworks_queryInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "fillFactory",
            "type": "fillFactory",
            "bomArchive":
                MachineInfo['data']['bomArchive'],
            "approvers":
                MachineInfo['data']['approvers'],
            "bomTreeVOList":
                MachineInfo['data']['bomTreeVOList'],
            "refFactoryList": [
                {
                    "note": MachineInfo['data']['bomTreeVOList'][0]['note'],
                    "matCode": MachineInfo['data']['bomTreeVOList'][0]['matCode'],
                    "isOversea": None,
                    "homePackagingFactory": "1051",
                    "homeChipFactory": "/",
                    "overseasPackagingFactory": "/",
                    "overseasChipFactory": "/",
                    "applyScope": "domesticProd",
                    "bomNodeCode": None,
                    "statusCode": "trial",
                    "bomNo": "1",
                    "factory": None,
                    "applyScopeList": [
                        "domesticProd"
                    ],
                    "childNodes": None,
                    "existFactory": False,
                    "statusCodeLabel": "试产"
                }
            ],
            "bomDeriveList": None,
            "copyRuleList": None,
            "otherDeriveList": None,
            "uploadList": [],
            "bomImportKeyDeviceList": None,
            "purchaseList": None,
            "role": "mpm,nps",
            "bomDeriveTreeVOList": [],
            "virtualChipList": None,
            "diffCollectList": None,
            "checkFactory": "patchTrue"
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_Machine_Factory(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：整机BOM协作-补充工厂审批通过流程')

    @allure.step("整机BOM协作-补充工厂审批通过接口")
    def API_Derive_Machine_Factory(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：整机BOM协作-补充工厂审批通过流程')
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        MachineInfo = self.Oneworks_queryInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "fillFactory",
            "type": "fillFactory",
            "bomArchive":
                MachineInfo['data']['bomArchive'],
            "approvers":
                MachineInfo['data']['approvers'],
            "bomTreeVOList":
                MachineInfo['data']['bomTreeVOList'],
            "refFactoryList":
                [
                    {
                        "note": "CKD_itel_A44_F3706_玫瑰金_IN_BCFL_8+1_P05_E",
                        "matCode": "11000002",
                        "isOversea": None,
                        "homePackagingFactory": "1051",
                        "homeChipFactory": "/",
                        "overseasPackagingFactory": "/",
                        "overseasChipFactory": "/",
                        "applyScope": "deliver",
                        "bomNodeCode": None,
                        "statusCode": "batch",
                        "bomNo": "1",
                        "factory": None,
                        "applyScopeList": [
                            "deliver"
                        ],
                        "childNodes": None,
                        "existFactory": False,
                        "statusCodeLabel": "量产",
                        "deleteValidate": False
                    }
                ],
            "bomDeriveList": MachineInfo['data']['bomDeriveList'],
            "copyRuleList": None,
            "otherDeriveList": None,
            "uploadList": [],
            "bomImportKeyDeviceList": None,
            "purchaseList": None,
            "role": MachineInfo['data']['role'],
            "bomDeriveTreeVOList": [],
            "virtualChipList": None,
            "diffCollectList": None,
            "checkFactory": "patchTrue"
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_Machine_Factory(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：整机BOM协作-补充工厂审批通过流程')

    @allure.step("整机BOM协作-BOM工程师审批通过接口")
    def API_Machine_bomEnginner(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：整机BOM协作-结构工程师审批通过流程')
        self.API_Machine_Factory(flowNo, instanceid, flowid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        MachineInfo = self.Oneworks_queryInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "bomArchReview",
            "bomArchive":
                MachineInfo['data']['bomArchive'],
            "approvers":
                MachineInfo['data']['approvers'],
            "bomTreeVOList":
                MachineInfo['data']['bomTreeVOList'],
            "refFactoryList":
                MachineInfo['data']['refFactoryList'],
            "bomDeriveList": None,
            "copyRuleList": None,
            "otherDeriveList": None,
            "uploadList": [],
            "bomImportKeyDeviceList": None,
            "purchaseList": None,
            "role": "mpm,nps",
            "bomDeriveTreeVOList": [],
            "virtualChipList": None,
            "diffCollectList": None,

        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_Machine_bomEnginner(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：整机BOM协作-结构工程师审批通过流程')

    @allure.step("整机BOM协作-BOM工程师审批通过接口")
    def API_Derive_Machine_bomEnginner(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：整机BOM协作-结构工程师审批通过流程')
        self.API_Derive_Machine_Factory(flowNo, instanceid, flowid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        MachineInfo = self.Oneworks_queryInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "bomArchReview",
            "bomArchive":
                MachineInfo['data']['bomArchive'],
            "approvers":
                MachineInfo['data']['approvers'],
            "bomTreeVOList":
                MachineInfo['data']['bomTreeVOList'],
            "refFactoryList":
                MachineInfo['data']['refFactoryList'],
            "bomDeriveList":
                MachineInfo['data']['bomDeriveList'],
            "copyRuleList": None,
            "otherDeriveList": None,
            "uploadList": [],
            "bomImportKeyDeviceList": None,
            "purchaseList": None,
            "role":
                MachineInfo['data']['role'],
            "bomDeriveTreeVOList": [],
            "virtualChipList": None,
            "diffCollectList": None,

        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_Machine_bomEnginner(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：整机BOM协作-结构工程师审批通过流程')

    @allure.step("整机BOM协作-业务审核通过接口")
    def API_Machine_Approval(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：整机BOM协作-业务审核通过流程')
        self.API_Machine_bomEnginner(flowNo, instanceid, flowid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        MachineInfo = self.Oneworks_queryInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "bisReview",
            "bomArchive":
                MachineInfo['data']['bomArchive'],
            "approvers":
                MachineInfo['data']['approvers'],
            "bomTreeVOList":
                MachineInfo['data']['bomTreeVOList'],
            "refFactoryList":
                MachineInfo['data']['refFactoryList'],
            "bomDeriveList": None,
            "copyRuleList": None,
            "otherDeriveList": None,
            "uploadList": [],
            "bomImportKeyDeviceList": None,
            "purchaseList": None,
            "role": "mpm,nps",
            "bomDeriveTreeVOList": [],
            "virtualChipList": None,
            "diffCollectList": None,
            "recordReqVO": {
                "checkRole": "audio",
                "listBid": "917411787551412224",
                "listName": "wqe",
                "records": [
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "963830756885532672",
                        "ruleName": "阿道夫weeeeee222asdfasdf"
                    },
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "963830756885532673",
                        "ruleName": "12"
                    },
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "963830756885532674",
                        "ruleName": "111"
                    },
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "963830756885532675",
                        "ruleName": "2131"
                    },
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "963830756885532676",
                        "ruleName": "1"
                    },
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "963830756885532677",
                        "ruleName": "q"
                    },
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "963830756885532678",
                        "ruleName": "测试-zql"
                    },
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "963830756885532679",
                        "ruleName": "http://bom-sit.transsion.com/#/check-config/self-inspection-rule-managehttp://bom-sit.transsion.com/"
                    },
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "963830756885532680",
                        "ruleName": "计划的空间"
                    },
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "963830756885532681",
                        "ruleName": "aa"
                    }
                ],
                "bomLevel": "complete",
                "checker": "18645960",
                "flowId": flowid
            }
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_Machine_Approve(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：整机BOM协作业务审核通过流程')

    @allure.step("整机BOM协作-业务审核通过接口")
    def API_Derive_Machine_Approval(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：整机BOM协作-业务审核通过流程')
        self.API_Derive_Machine_bomEnginner(flowNo, instanceid, flowid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        MachineInfo = self.Oneworks_queryInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "bisReview",
            "bomArchive":
                MachineInfo['data']['bomArchive'],
            "approvers":
                MachineInfo['data']['approvers'],
            "bomTreeVOList":
                MachineInfo['data']['bomTreeVOList'],
            "refFactoryList":
                MachineInfo['data']['refFactoryList'],
            "bomDeriveList":
                MachineInfo['data']['bomDeriveList'],
            "copyRuleList": None,
            "otherDeriveList":
                MachineInfo['data']['otherDeriveList'],
            "uploadList": [],
            "bomImportKeyDeviceList": None,
            "purchaseList": None,
            "role":
                MachineInfo['data']['role'],
            "bomDeriveTreeVOList": [],
            "virtualChipList": None,
            "diffCollectList": None,
            "recordReqVO": {
                "checkRole": "audio",
                "listBid": "966650555156008960",
                "listName": "in",
                "records": [
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "966650555172786176",
                        "ruleName": "整机BOM"
                    }
                ],
                "bomLevel": "complete",
                "checker": "18645960",
                "flowId": flowid
            }
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_Machine_Approve(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：整机BOM协作业务审核通过流程')

    @allure.step("BOM协作撤回删除接口")
    def API_Bom_Delete(self, instanceid, flowid):
        """
        TBM BOM协作 oneworks撤回接口 TBM删除已撤回流程接口
        @param instanceid:oneworks撤回流程编码
        @param flowid:流程ID
        """
        logging.info('发起流程：BOM协作撤回流程')
        token = self.tbm_login()
        delete_data = {"id": flowid}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        self.Oneworks_Recall(instanceid, headers)
        self.Request_Bom_Delete(delete_data, headers)
        logging.info('流程结束：BOM协作撤回流程')

    def Request_BarePhone_Add(self, data, headers):
        """
        TBM 单机头BOM协作 新增接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：单机头BOM协作新增接口')
        return self.api_request('单机头BOM协作新增接口', data, headers)

    @allure.step("Oneworks查询流程历史")
    def Oneworks_History(self, instanceId, headers):
        """
        TBM oneworks 查询流程历史
        @param instanceId:oneworks  流程实例id
        @param headers:接口头部
        """
        logging.info('发起请求：oneworks查询流程历史接口')
        logging.info(f'接口请求地址为：https://pfgatewayidct.transsion.com:9188/process-center/process-center/history/0/{instanceId}/get-historic-communication-detail')
        history_response = requests.get(
            url=f'https://pfgatewayidct.transsion.com:9188/process-center/process-center/history/0/{instanceId}/get-historic-communication-detail',
            headers=headers)
        response_dicts = history_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        logging.info('请求结束：oneworks查询流程历史接口')
        return response_dicts

    @allure.step("流程查询接口")
    def API_getHistoric(self, flowNo, node=None):
        logging.info('发起流程接口：TBM-流程查询接口')
        Search_Result = self.API_MyApply_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        History_response = self.Oneworks_History(Search_Result[0], headers)
        if node is None:
            assignee = History_response['data']['historyCourse'][-1]['assignee']
            logging.info('发起人：{}'.format(assignee))
            logging.info('流程接口结束：TBM-我的待办-查询')
            return assignee
        else:
            historyCourse_list = History_response['data']['historyCourse']
            for i in historyCourse_list:
                if i['taskName'] == node:
                    logging.info('节点：{}的审批人：{}'.format(node, i['assignee']))
                    logging.info('流程接口结束：TBM-我的待办-查询')
                    return i['assignee']

    @allure.step("Oneworks-查询单机头流程历史")
    def Oneworks_queryBomSingleHeadInfo(self, flowId, headers):
        """
        TBM oneworks 查询流程历史
        @param flowId:oneworks  流程实例id
        @param headers:接口头部
        """
        logging.info('发起请求：oneworks查询单机头流程历史接口')
        logging.info(f'接口请求地址为：http://pfgatewayidct.transsion.com:9088/service-bom-archive/bom-singleHead/bomSingleHead/queryBomSingleHeadInfoByFlowId?flowId={flowId}&esId=')
        history_response = requests.get(
            url=f'http://pfgatewayidct.transsion.com:9088/service-bom-archive/bom-singleHead/bomSingleHead/queryBomSingleHeadInfoByFlowId?flowId={flowId}&esId=',
            headers=headers)
        response_dicts = history_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        logging.info('请求结束：oneworks查询单机头流程历史接口')
        return response_dicts

    def Oneworks_queryInfo(self, flowId, headers):
        """
        TBM oneworks 查询流程历史
        @param flowId:oneworks  流程实例id
        @param headers:接口头部
        """
        logging.info('发起请求：oneworks查询流程历史接口')
        logging.info(f'接口请求地址为：http://pfgatewayidct.transsion.com:9088/service-bom-archive/bom-arc/bomArch/queryInfoByFlowId?flowId={flowId}')
        history_response = requests.get(
            url=f'http://pfgatewayidct.transsion.com:9088/service-bom-archive/bom-arc/bomArch/queryInfoByFlowId?flowId={flowId}',
            headers=headers)
        response_dicts = history_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        logging.info('请求结束：oneworks查询流程历史接口')
        return response_dicts

    def Request_BarePhone_Factory(self, data, headers):
        """
        TBM 单机头BOM协作 oneworks 补充工厂
        @param data: 接口body
        @param headers:接口头部
        """
        logging.info('发起请求：单机头BOM协作补充工厂接口')
        return self.api_request('单机头BOM协作补充工厂接口', data, headers)

    def Request_BarePhone_StructureEnginner(self, data, headers):
        """
        TBM 单机头BOM协作 oneworks 结构工程师审批
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：单机头BOM协作结构工程师审批接口')
        return self.api_request('单机头BOM协作结构工程师审批接口', data, headers)

    def Request_BarePhone_Approval(self, data, headers):
        """
        TBM 单机头BOM协作 oneworks 业务审核
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：单机头BOM协作业务审核接口')
        return self.api_request('单机头BOM协作业务审核接口', data, headers)

    def Request_BarePhone_BomEngineer(self, data, headers):
        """
        TBM 单机头BOM协作 oneworks BOM工程师审批
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：单机头BOM协作BOM工程师审批接口')
        return self.api_request('单机头BOM协作BOM工程师审批接口', data, headers)

    def Request_Oneworks_Complete(self, data, headers):
        """
        oneworks统一审批
        @param data: 接口body
        @param headers:接口头部
        """
        logging.info('发起请求：oneworks统一审批接口')
        return self.api_request('oneworks统一审批接口', data, headers)

    def Request_Todo_Search(self, data, headers):
        """
        TBM 我的待办 查询
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：我的待办查询接口')
        return self.api_request('我的待办查询接口', data, headers)

    def Request_Apply_Search(self, data, headers):
        """
        TBM 我申请的 查询
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：我申请的查询接口')
        return self.api_request('我申请的查询接口', data, headers)

    @allure.step("TBM-我的待办-查询")
    def API_Mytodu_Search(self, flowNo, username='18645960'):
        logging.info('发起流程接口：TBM-我的待办-查询')
        token = self.tbm_login(username)
        search_data = {"code": flowNo}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        search_response = self.Request_Todo_Search(search_data, headers)
        for i in range(20):
            if len(search_response['data']['list']) == 0:
                sleep(1)
                search_response = self.Request_Todo_Search(search_data, headers)
        response_data = search_response['data']['list'][0]
        logging.info('接口返回数据：taskId：{}'.format(response_data['taskId']))
        logging.info('流程接口结束：TBM-我的待办-查询')
        return response_data['taskId'], token

    @allure.step("TBM-我申请的-查询")
    def API_MyApply_Search(self, flowNo):
        logging.info('发起流程接口：TBM-我的待办-查询')
        token = self.tbm_login()
        search_data = {"code": flowNo}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        search_response = self.Request_Apply_Search(search_data, headers)
        for i in range(20):
            if len(search_response['data']['list']) == 0:
                sleep(1)
                search_response = self.Request_Apply_Search(search_data, headers)
        response_data = search_response['data']['list'][0]
        logging.info('接口返回数据：instanceId：{}'.format(response_data['instanceId']))
        logging.info('流程接口结束：TBM-我的待办-查询')
        return response_data['instanceId'], token

    @allure.step("单机头BOM协作新增接口")
    def API_BarePhone_Add(self):
        logging.info('发起流程接口：单机头BOM协作新增流程')
        token = self.tbm_login()
        titletime = datetime.now().strftime('%Y-%m-%d')
        flowStartdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        add_data = {"flowId": None, "flowNodeName": "start",
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
        add_response = self.Request_BarePhone_Add(add_data, headers)
        flowId = add_response['data']
        search_response = self.Request_Bom_Search(search_data, headers)
        search_response_data = search_response['data']['data']
        for i in search_response_data:
            if i['flowId'] == flowId:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，bid：{}'.format(i['flowNo'], i['instanceId'], i['flowId']))
                logging.info('流程接口结束：单机头BOM协作新增流程')
                return i['flowNo'], i['instanceId'], i['flowId'], flowStartdate

    @allure.step("单机头BOM协作新增接口-子阶BOM失败例子")
    def API_BarePhone_Fail_Add(self):
        logging.info('发起流程接口：单机头BOM协作新增流程')
        token = self.tbm_login()
        titletime = datetime.now().strftime('%Y-%m-%d')
        flowStartdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        add_data = {"flowId": None, "flowNodeName": "start",
                    "bomArchive": {"flowNo": "", "flowProposer": "18645960", "flowProposerName": "李小素",
                                   "flowStartdate": f"{flowStartdate}", "bomVer": "", "bomVersion": "trial",
                                   "brandCode": "itel", "market": "ET", "produceClass": "singleHead",
                                   "templateId": 1017733,
                                   "templateName": "itel单机头", "isLocalPurchase": "", "bomClass": "", "model": "X572-1",
                                   "note": "", "title": f"[李小素]-[{titletime}]", "researchType": "selfResearch",
                                   "flowDept": "PI_系统四部", "doDeriveSame": 'false', "curFlowCode": "structureStart"},
                    "bomDeriveList": [], "otherDeriveList": [], "bomTreeVOList": [
                {"id": "new_bom_3000", "matGroup": "120", "bomName": "单机头", "statusCode": "trial", "baseQty": "1000",
                 "nodeClass": "actual",
                 "businessRole": "qpm,pm,mpm,structure,hardware,screenage,audio,preResearch,cmf,pilot,nps",
                 "tempNodeId": 3732, "childNodes": [
                    {"id": "new_bom_3001", "matGroup": "121", "bomName": "PCBA", "nodeClass": "actual",
                     "businessRole": "hardware", "tempNodeId": 3733, "childNodes": [], "index": 0, "serialNo": "1.1"},
                    {"id": "new_bom_3002", "matGroup": "250", "bomName": "电池", "nodeClass": "actual",
                     "businessRole": "preResearch", "tempNodeId": 3734, "childNodes": [], "index": 1,
                     "serialNo": "1.2"}, {"id": "new_bom_3003", "matGroup": "176", "bomName": "指纹模组", "baseQty": "1000",
                                          "nodeClass": "actual", "businessRole": "preResearch", "tempNodeId": 3735,
                                          "childNodes": [], "index": 2, "serialNo": "1.3", "matCode": "12200078",
                                          "deleteValidate": 'false', "note": "预加工_电池盖_X5514_砂岩黑_YX"},
                    {"id": "new_bom_3004", "matGroup": "232", "bomName": "镜片", "nodeClass": "actual",
                     "businessRole": "structure", "tempNodeId": 3736, "childNodes": [], "index": 3, "serialNo": "1.4"},
                    {"id": "new_bom_3005", "matGroup": "123", "bomName": "虚拟共用件", "nodeClass": "actual",
                     "businessRole": "structure", "tempNodeId": 3737, "childNodes": [
                        {"id": "new_bom_3006", "matGroup": "172", "bomName": "摄像头", "nodeClass": "actual",
                         "businessRole": "structure", "tempNodeId": 3738, "childNodes": [], "index": 0,
                         "serialNo": "1.5.1"},
                        {"id": "new_bom_3007", "matGroup": "195", "bomName": "听筒", "nodeClass": "actual",
                         "businessRole": "structure", "tempNodeId": 3739, "childNodes": [], "index": 1,
                         "serialNo": "1.5.2"}], "index": 4, "serialNo": "1.5"}], "isRoot": 'true', "index": 0,
                 "serialNo": 1, "matCode": "12011061", "deleteValidate": 'false',
                 "note": "单机头_Infinix_X655-V_H6210_F1_海浪_32+3", "matAttr": "可选"}], "bomDeriveTreeVOList": [],
                    "approvers": {"bisReviewApprovers": [],
                                  "bisSupplyApprovers": [{"role": "mpm", "userNo": "18645960"},
                                                         {"role": "pm", "userNo": ""},
                                                         {"role": "cmf", "userNo": ""}, {"role": "qpm", "userNo": ""},
                                                         {"role": "structure", "userNo": ""},
                                                         {"role": "hardware", "userNo": ""},
                                                         {"role": "screenage", "userNo": ""},
                                                         {"role": "audio", "userNo": ""},
                                                         {"role": "preResearch", "userNo": ""},
                                                         {"role": "pilot", "userNo": ""},
                                                         {"role": "nps", "userNo": ""}]},
                    "uploadList": [], "submitType": "submit"}
        search_data = {
            "param": {"title": "", "flowNo": "", "bomCode": "", "produceClass": "", "model": "", "brandCode": "",
                      "bomVer": "", "market": "", "statusCode": "", "synStatus": "", "createdBy": "",
                      "createdTimeFrom": "", "createdTimeTo": "", "bomType": "singleHeadBom"}, "current": 1, "size": 10}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        add_response = self.Request_BarePhone_Add(add_data, headers)
        flowId = add_response['data']
        search_response = self.Request_Bom_Search(search_data, headers)
        search_response_data = search_response['data']['data']
        for i in search_response_data:
            if i['flowId'] == flowId:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，bid：{}'.format(i['flowNo'], i['instanceId'], i['flowId']))
                logging.info('流程接口结束：单机头BOM协作新增流程')
                return i['flowNo'], i['instanceId'], i['flowId']

    @allure.step("单机头BOM协作-补充工厂审批通过接口")
    def API_BarePhone_Factory(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：单机头BOM协作-补充工厂审批通过流程')
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        BomSingleHeadInfo = self.Oneworks_queryBomSingleHeadInfo(flowid, headers)
        approve_data = {"flowId": flowid, "refFactoryList": [
            {"note": BomSingleHeadInfo['data']['bomTreeVOList'][0]['note'], "matCode": BomSingleHeadInfo['data']['bomTreeVOList'][0]['matCode'], "isOversea": None,
             "homePackagingFactory": "1051", "homeChipFactory": "/", "overseasPackagingFactory": "/",
             "overseasChipFactory": "/", "applyScope": "singleHeadBom", "bomNodeCode": None, "statusCode": "trial",
             "bomNo": "1", "factory": "/", "applyScopeList": ["singleHeadBom"], "childNodes": None,
             "existFactory": 'false', "statusCodeLabel": "试产", "deleteValidate": 'false'}],
                        "produceClass": "singleHead"}
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_BarePhone_Factory(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：单机头BOM协作-补充工厂审批通过流程')

    @allure.step("单机头BOM协作-结构工程师审批通过接口")
    def API_BarePhone_StructureEnginner(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：单机头BOM协作-结构工程师审批通过流程')
        self.API_BarePhone_Factory(flowNo, instanceid, flowid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        BomSingleHeadInfo = self.Oneworks_queryBomSingleHeadInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "structureReview",
            "bomArchive":
                BomSingleHeadInfo['data']['bomArchive'],
            "approvers": {
                "bisReviewApprovers": [
                    {
                        "role": "qpm",
                        "userNo": "18645960"
                    },
                    {
                        "role": "structure",
                        "userNo": "18645960"
                    },
                    {
                        "role": "hardware",
                        "userNo": "18645960"
                    },
                    {
                        "role": "screenage",
                        "userNo": "18645960"
                    },
                    {
                        "role": "audio",
                        "userNo": "18645960"
                    },
                    {
                        "role": "preResearch",
                        "userNo": "18645960"
                    },
                    {
                        "role": "pilot",
                        "userNo": "18645960"
                    },
                    {
                        "role": "nps",
                        "userNo": "18645960"
                    },
                    {
                        "role": "structure2",
                        "userNo": "18645960"
                    },
                    {
                        "role": "aaa",
                        "userNo": "18645960"
                    }
                ],
                "bisSupplyApprovers": []
            },
            "bomTreeVOList":
                BomSingleHeadInfo['data']['bomTreeVOList'],
            "refFactoryList":
                BomSingleHeadInfo['data']['refFactoryList'],
            "bomDeriveList": [],
            "copyRuleList": [],
            "otherDeriveList": [],
            "uploadList": [],
            "bomImportKeyDeviceList": [],
            "purchaseList": None,
            "role": "mpm",
            "bomDeriveTreeVOList": [],
            "virtualChipList": None,
            "diffCollectList": None,
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_BarePhone_StructureEnginner(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：单机头BOM协作-结构工程师审批通过流程')

    @allure.step("单机头BOM协作-业务审核通过接口")
    def API_BarePhone_Approval(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：单机头BOM协作-业务审核通过流程')
        self.API_BarePhone_StructureEnginner(flowNo, instanceid, flowid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        BomSingleHeadInfo = self.Oneworks_queryBomSingleHeadInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "bisReview",
            "bomArchive":
                BomSingleHeadInfo['data']['bomArchive'],
            "approvers":
                BomSingleHeadInfo['data']['approvers'],
            "bomTreeVOList":
                BomSingleHeadInfo['data']['bomTreeVOList'],
            "refFactoryList":
                BomSingleHeadInfo['data']['refFactoryList'],
            "bomDeriveList": [],
            "copyRuleList": [],
            "otherDeriveList": [],
            "uploadList": [],
            "bomImportKeyDeviceList": [],
            "purchaseList": None,
            "role": "mpm,qpm,structure,hardware,screenage,audio,preResearch,pilot,nps,structure2,aaa",
            "bomDeriveTreeVOList": [],
            "virtualChipList": None,
            "diffCollectList": None,
            "recordReqVO": {
                "checkRole": "qpm",
                "listBid": "963466084747448320",
                "listName": "单机头itel",
                "records": [
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "963466084776808448",
                        "ruleName": "恶趣味"
                    }
                ],
                "bomLevel": "single",
                "checker": "18645960",
                "flowId": flowid
            }
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_BarePhone_Approval(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：单机头BOM协作-业务审核通过流程')

    @allure.step("单机头BOM协作-BOM工程师审批通过接口")
    def API_BarePhone_bomEnginner(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：单机头BOM协作-业务审核通过流程')
        self.API_BarePhone_Approval(flowNo, instanceid, flowid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        BomSingleHeadInfo = self.Oneworks_queryBomSingleHeadInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "bomArchReview",
            "bomType": False,
            "bomArchive":
                BomSingleHeadInfo['data']['bomArchive'],
            "approvers":
                BomSingleHeadInfo['data']['approvers'],
            "bomTreeVOList":
                BomSingleHeadInfo['data']['bomTreeVOList'],
            "refFactoryList":
                BomSingleHeadInfo['data']['refFactoryList'],
            "bomDeriveList": [],
            "copyRuleList": [],
            "otherDeriveList": [],
            "uploadList": [],
            "bomImportKeyDeviceList": [],
            "purchaseList": None,
            "role": "mpm,qpm,structure,hardware,screenage,audio,preResearch,pilot,nps,structure2,aaa",
            "bomDeriveTreeVOList": [],
            "virtualChipList": None,
            "diffCollectList": None,
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_BarePhone_BomEngineer(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：单机头BOM协作-BOM工程师审批通过接口')

    def Request_KeyDevice_Add(self, data, headers):
        """
        TBM 关键器件流程 新增接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程新增接口')
        return self.api_request('关键器件流程新增接口', data, headers)

    def Request_KeyDevice_Search(self, data, headers):
        """
        TBM 关键器件流程 TBM查询接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程查询接口')
        return self.api_request('关键器件流程查询接口', data, headers)

    def Request_KeyDevice_flowInfo(self, data, headers):
        """
        TBM 关键器件流程 flowInfo查询接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程查询流程信息接口')
        return self.api_request('关键器件流程查询流程信息接口', data, headers)

    def Request_KeyDevice_nodeMatAdd(self, data, headers):
        """
        TBM 关键器件流程 节点nodeMat Add接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程nodeMat保存接口')
        return self.api_request('关键器件流程nodeMat保存接口', data, headers)

    def Request_KeyDevice_nodeMatSubmit(self, data, headers):
        """
        TBM 关键器件流程 节点nodeMat Submit接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程nodeMat提交接口')
        return self.api_request('关键器件流程nodeMat提交接口', data, headers)

    def Request_KeyDevice_FlowDetail(self, deviceBid, headers):
        """
        TBM 关键器件流程 查询FlowDetail
        @param deviceBid:deviceBid
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程FlowDetail查询接口')
        logging.info(f'接口请求地址为：http://pfgatewayidct.transsion.com:9088/plm-key-device-main/key-device/nodeMat/queryFlowDetailByDeviceBid?deviceBid=={deviceBid}&flowNodeCode=')
        recall_response = requests.get(
            url=f'http://pfgatewayidct.transsion.com:9088/plm-key-device-main/key-device/nodeMat/queryFlowDetailByDeviceBid?deviceBid={deviceBid}&flowNodeCode=',
            headers=headers)
        response_dicts = recall_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        logging.info('请求结束：关键器件流程FlowDetail查询接口')
        return response_dicts

    def Request_KeyDevice_Approver(self, data, headers):
        """
        TBM 关键器件流程 代表节点Approver接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程代表提交接口')
        return self.api_request('关键器件流程代表提交接口', data, headers)

    def Request_KeyDevice_MatList(self, data, headers):
        """
        TBM 关键器件流程 节点MatList查询接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程MatList查询接口')
        return self.api_request('关键器件流程MatList查询接口', data, headers)

    def Request_KeyDevice_procurement(self, data, headers):
        """
        TBM 关键器件流程 procurement保存接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程procurement保存接口')
        return self.api_request('关键器件流程procurement保存接口', data, headers)

    def Request_KeyDevice_evaluation(self, data, headers):
        """
        TBM 关键器件流程 evaluation提交接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程evaluation提交接口')
        return self.api_request('关键器件流程evaluation提交接口', data, headers)

    def Request_KeyDevice_FlowNodeApprover(self, deviceBid, flowBid, headers):
        """
        TBM 关键器件流程 查询FlowNodeApprover
        @param deviceBid:deviceBid
        @param headers:接口头部
        """
        logging.info('发起请求：关键器件流程FlowNodeApprover查询接口')
        logging.info(f'接口请求地址为：http://pfgatewayidct.transsion.com:9088/plm-key-device-main/key-device/getFlowNodeApprover?deviceBid={deviceBid}&businissType=1&flowBid={flowBid}')
        recall_response = requests.get(
            url=f'http://pfgatewayidct.transsion.com:9088/plm-key-device-main/key-device/getFlowNodeApprover?deviceBid={deviceBid}&businissType=1&flowBid={flowBid}',
            headers=headers)
        response_dicts = recall_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        logging.info('请求结束：关键器件流程FlowNodeApprover查询接口')
        return response_dicts

    def Request_KeyDevice_Delete(self, bid, headers):
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
        response_dicts = recall_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        return response_dicts

    @allure.step("关键器件流程新增接口")
    def API_KeyDevice_Add(self):
        logging.info('发起流程接口：关键器件流程新增流程')
        token = self.tbm_login()
        querytime = datetime.now().strftime('%Y-%m-%d')
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
        add_response = self.Request_KeyDevice_Add(add_data, headers)
        bid = add_response['data']['bid']
        search_response = self.Request_KeyDevice_Search(search_data, headers)
        search_response_data = search_response['data']['data']
        for i in search_response_data:
            if i['bid'] == bid:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，bid：{}'.format(i['flowNo'], i['instanceId'], i['bid']))
                logging.info('流程接口结束：关键器件流程新增流程')
                return i['flowNo'], i['instanceId'], i['bid']

    @allure.step("关键器件流程新增接口")
    def API_KeyDevice_Revise(self):
        logging.info('发起流程接口：关键器件流程新增流程')
        token = self.tbm_login()
        querytime = datetime.now().strftime('%Y-%m-%d')
        revise_data = {
            "flowMainVO": {
                "flowProposer": "18645960",
                "flowProposerName": "李小素",
                "flowDept": "PI_系统四部",
                "title": f"修订-[50A710U]-[李小素]-[{querytime}]",
                "businissType": "2",
                "deviceBid": "1032318756598190080"
            },
            "deviceVO": {
                "brand": "itel",
                "model": "50A710U",
                "basiclineName": None,
                "note": "",
                "platform": "1",
                "onMarketDate": "1",
                "monthNeeds": "1",
                "totalNeeds": "1",
                "targetMarket": "1",
                "lifecycle": "1",
                "templateBid": "956136840950321152",
                "version": "V1.0"
            },
            "approvers": {
                "domainRole": [
                    {
                        "domainName": "摄像头+闪光灯",
                        "domainCode": "dev_image",
                        "approver": "18645960"
                    },
                    {
                        "domainName": "硬件电子料-基带",
                        "domainCode": "dev_hardware",
                        "approver": "18651509"
                    }
                ],
                "assessRole": [
                    {
                        "domainName": "标准化代表",
                        "domainCode": "standard_deputy",
                        "approver": "18645960"
                    },
                    {
                        "domainName": "采购代表",
                        "domainCode": "purchase_deputy",
                        "approver": "18645960"
                    }
                ]
            },
            "uploadList": [],
            "saveType": "submit",
            "kdNodeAuthVO": [
                {
                    "nodeName": "摄像头+闪光灯",
                    "nodeBid": "956136841009041409"
                },
                {
                    "nodeName": "LCM！",
                    "nodeBid": "956136841009041410",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "CTP",
                    "nodeBid": "956136841009041426",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "前摄1",
                    "nodeBid": "956136841009041440",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "前摄2",
                    "nodeBid": "956136841009041453",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "后摄1",
                    "nodeBid": "956136841009041466",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "后摄2",
                    "nodeBid": "956136841009041479",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "后摄3",
                    "nodeBid": "956136841009041493",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "后摄4",
                    "nodeBid": "956136841009041506",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "后摄5",
                    "nodeBid": "956136841009041519",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "前闪1",
                    "nodeBid": "956136841009041532",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "前闪2",
                    "nodeBid": "956136841009041536",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "后闪1",
                    "nodeBid": "956136841009041540",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "后闪2",
                    "nodeBid": "956136841013235715",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "后闪3",
                    "nodeBid": "956136841013235719",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "指纹",
                    "nodeBid": "956136841013235723",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "摄像头+闪光灯_16",
                    "nodeBid": "956136841013235729",
                    "parentName": "摄像头+闪光灯"
                },
                {
                    "nodeName": "硬件电子料-基带",
                    "nodeBid": "956136841013235731"
                },
                {
                    "nodeName": "PCB",
                    "nodeBid": "956136841013235732",
                    "parentName": "硬件电子料-基带"
                },
                {
                    "nodeName": "CPU",
                    "nodeBid": "956136841013235735",
                    "parentName": "硬件电子料-基带"
                },
                {
                    "nodeName": "Memory",
                    "nodeBid": "956136841013235740",
                    "parentName": "硬件电子料-基带"
                },
                {
                    "nodeName": "晶体振",
                    "nodeBid": "956136841013235755",
                    "parentName": "硬件电子料-基带"
                },
                {
                    "nodeName": "音频PA1",
                    "nodeBid": "956136841013235763",
                    "parentName": "硬件电子料-基带"
                },
                {
                    "nodeName": "音频PA2",
                    "nodeBid": "956136841013235771",
                    "parentName": "硬件电子料-基带"
                },
                {
                    "nodeName": "Sensor",
                    "nodeBid": "956136841013235779",
                    "parentName": "硬件电子料-基带"
                },
                {
                    "nodeName": "电源类",
                    "nodeBid": "956136841013235786",
                    "parentName": "硬件电子料-基带"
                },
                {
                    "nodeName": "驱动IC",
                    "nodeBid": "956136841013235803",
                    "parentName": "硬件电子料-基带"
                }
            ]
        }
        search_data = {"current": 1, "size": 10, "param": {}}
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        add_response = self.Request_KeyDevice_Add(revise_data, headers)
        bid = add_response['data']['bid']
        search_response = self.Request_KeyDevice_Search(search_data, headers)
        search_response_data = search_response['data']['data']
        for i in search_response_data:
            if i['bid'] == bid:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，bid：{}'.format(i['flowNo'], i['instanceId'], i['bid']))
                logging.info('流程接口结束：关键器件流程新增流程')
                return i['flowNo'], i['instanceId'], i['bid']

    @allure.step("关键器件流程：摄像头+闪光灯审批接口")
    def API_KeyDevice_image(self, flowNo, instanceid, bid):
        logging.info('发起流程接口：关键器件流程：摄像头+闪光灯审批接口')
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        flowInfo_body = {"flowBid": bid}
        flowInfo_response = self.Request_KeyDevice_flowInfo(flowInfo_body, headers)
        FlowDetail_response = self.Request_KeyDevice_FlowDetail(flowInfo_response['data']['flowMainVO']['deviceBid'], headers)
        domainNodeVOList = FlowDetail_response['data']['domainNodeVOList']
        nodeMatAdd_body = {
            "domainDeviceVO": {
                "deviceMatVOList": [
                    {
                        "group": 1,
                        "deviceGroupName": "CTP(1供)",
                        "groupCode": "CTP1",
                        "defineId": 1,
                        "isAddRow": True,
                        "matList": [
                            {
                                "group": 1,
                                "deviceType": "parameter",
                                "parentId": 1,
                                "deviceGroupName": "CTP(1供)",
                                "deviceMatParamBusinessVOList": [
                                    {
                                        "paramBid": "956136841009041427",
                                        "paramValue": "GFF"
                                    },
                                    {
                                        "paramBid": "956136841009041428"
                                    },
                                    {
                                        "paramBid": "956136841009041429",
                                        "paramValue": "CG颜色test"
                                    },
                                    {
                                        "paramBid": "956136841009041430"
                                    },
                                    {
                                        "paramBid": "956136841009041431"
                                    },
                                    {
                                        "paramBid": "956136841009041432",
                                        "paramValue": "接口类型test"
                                    },
                                    {
                                        "paramBid": "956136841009041433"
                                    },
                                    {
                                        "paramBid": "956136841009041434"
                                    },
                                    {
                                        "paramBid": "956136841009041438",
                                        "paramValue": "焊接"
                                    },
                                    {
                                        "paramBid": "956136841009041436"
                                    },
                                    {
                                        "paramBid": "956136841009041437"
                                    },
                                    {
                                        "paramBid": "956136841009041435"
                                    },
                                    {
                                        "paramBid": "956136841009041439"
                                    }
                                ],
                                "defineId": 2,
                                "matCode": "NA",
                                "baseQty": 1,
                                "reason": "标准件",
                                "matNote": "待申请编码",
                                "matAttr": "属性test"
                            }
                        ]
                    }
                ],
                "nodeBid": '956136841009041426'
            },
            "kdDeviceVO": flowInfo_response['data']['deviceVO'],
            "kdFlowMainVO": flowInfo_response['data']['flowMainVO']
        }
        self.Request_KeyDevice_nodeMatAdd(nodeMatAdd_body, headers)
        nodeMatSubmit_body = {
            "domainNodeVOList": domainNodeVOList,
            "deviceBid": flowInfo_response['data']['flowMainVO']['deviceBid']
        }
        self.Request_KeyDevice_nodeMatSubmit(nodeMatSubmit_body, headers)
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1,
                         "comment": ""}
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：关键器件流程：摄像头+闪光灯审批接口')

    @allure.step("关键器件流程：硬件电子料-基带审批接口")
    def API_KeyDevice_hardware(self, flowNo, instanceid, bid, username='18645960'):
        logging.info('发起流程接口：关键器件流程：硬件电子料-基带审批接口')
        Search_Result = self.API_Mytodu_Search(flowNo, username)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        flowInfo_body = {"flowBid": bid}
        flowInfo_response = self.Request_KeyDevice_flowInfo(flowInfo_body, headers)
        FlowDetail_response = self.Request_KeyDevice_FlowDetail(flowInfo_response['data']['flowMainVO']['deviceBid'], headers)
        domainNodeVOList = FlowDetail_response['data']['domainNodeVOList']
        nodeMatAdd_body = {
            "domainDeviceVO": {
                "deviceMatVOList": [
                    {
                        "group": 1,
                        "deviceGroupName": "CPU(1供)",
                        "groupCode": "CPU1",
                        "defineId": 1,
                        "isAddRow": True,
                        "matList": [
                            {
                                "group": 1,
                                "deviceType": "parameter",
                                "parentId": 1,
                                "deviceGroupName": "CPU(1供)",
                                "deviceMatParamBusinessVOList": [
                                    {
                                        "paramBid": "956136841013235738"
                                    },
                                    {
                                        "paramBid": "956136841013235736"
                                    },
                                    {
                                        "paramBid": "956136841013235739"
                                    },
                                    {
                                        "paramBid": "956136841013235737"
                                    }
                                ],
                                "defineId": 2,
                                "matCode": "NA",
                                "baseQty": 1,
                                "reason": "标准件",
                                "matNote": "待申请编码",
                                "matAttr": "属性test"
                            }
                        ]
                    }
                ],
                "nodeBid": '956136841013235735'
            },
            "kdDeviceVO": flowInfo_response['data']['deviceVO'],
            "kdFlowMainVO": flowInfo_response['data']['flowMainVO']
        }
        self.Request_KeyDevice_nodeMatAdd(nodeMatAdd_body, headers)
        nodeMatSubmit_body = {
            "domainNodeVOList": domainNodeVOList,
            "deviceBid": flowInfo_response['data']['flowMainVO']['deviceBid']
        }
        self.Request_KeyDevice_nodeMatSubmit(nodeMatSubmit_body, headers)
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1,
                         "comment": ""}
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：关键器件流程：硬件电子料-基带审批接口')

    @allure.step("关键器件流程：标准化代表审批接口")
    def API_KeyDevice_StandardDeputy(self, flowNo, instanceid, bid):
        logging.info('发起流程接口：关键器件流程：标准化代表审批接口')
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        flowInfo_body = {"flowBid": bid}
        flowInfo_response = self.Request_KeyDevice_flowInfo(flowInfo_body, headers)
        FlowDetail_response = self.Request_KeyDevice_FlowNodeApprover(flowInfo_response['data']['flowMainVO']['deviceBid'], bid, headers)
        Approver_body = {
            "flowNodeApproverList": FlowDetail_response['data'],
            "flowBid": bid,
            "flowType": "standard_deputy"
        }
        for i in FlowDetail_response['data']:
            for j in i['childList']:
                j['standardBehalf'] = "18645960"
        self.Request_KeyDevice_Approver(Approver_body, headers)
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1,
                         "comment": ""}
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：关键器件流程：标准化代表审批接口')

    @allure.step("关键器件流程：采购代表审批接口")
    def API_KeyDevice_PurchaseDeputy(self, flowNo, instanceid, bid):
        logging.info('发起流程接口：关键器件流程：采购代表审批接口')
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        flowInfo_body = {"flowBid": bid}
        flowInfo_response = self.Request_KeyDevice_flowInfo(flowInfo_body, headers)
        FlowDetail_response = self.Request_KeyDevice_FlowNodeApprover(flowInfo_response['data']['flowMainVO']['deviceBid'], bid, headers)
        Approver_body = {
            "flowNodeApproverList": FlowDetail_response['data'],
            "flowBid": bid,
            "flowType": "purchase_deputy"
        }
        for i in FlowDetail_response['data']:
            for j in i['childList']:
                j['resourcesBusiness'] = "18645960"
                j['procurementExecution'] = "18645960"
                j['procurementPtc'] = "18645960"
                j['procurementSqm'] = "18645960"
        self.Request_KeyDevice_Approver(Approver_body, headers)
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1,
                         "comment": ""}
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：关键器件流程：采购代表审批接口')

    @allure.step("关键器件流程撤回删除接口")
    def API_KeyDevice_Delete(self, instanceid, bid):
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
        self.Request_KeyDevice_Delete(bid, headers)
        logging.info('流程接口结束：关键器件流程撤回流程')

    def Request_SaleCountry_Add(self, data, headers):
        """
        TBM 出货国家流程 新增接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家流程新增接口')
        return self.api_request('出货国家流程新增接口', data, headers)

    def Request_SaleCountry_Search(self, data, headers):
        """
        TBM 出货国家流程 TBM查询接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家流程查询接口')
        return self.api_request('出货国家流程查询接口', data, headers)

    def Request_SaleCountry_Delete(self, data, headers):
        """
        TBM 出货国家流程删除已撤回接口
        @param data:oneworks撤回流程编码
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家流程删除已撤回接口')
        return self.api_request('出货国家流程删除已撤回接口', data, headers)

    def Request_Change_Product(self, data, headers):
        """
        TBM 出货国家查询 变更产品接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家查询变更产品接口')
        return self.api_request('出货国家查询变更产品接口', data, headers)

    def Request_SaleCountry_Audit(self, data, headers):
        """
        TBM 出货国家查询 产品部管理员审核 产品部汇签 产品部管理员复核 用同一接口
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家流程审核接口')
        return self.api_request('出货国家流程审核接口', data, headers)

    def Request_SaleCountry_managerModify(self, data, headers):
        """
        TBM 出货国家查询 产品经理修改审核
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家流程产品经理修改审核接口')
        return self.api_request('出货国家流程产品经理修改审核接口', data, headers)

    def Request_SaleCountry_PageList(self, data, headers):
        """
        TBM 出货国家查询 列表查询
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家查询列表查询接口')
        return self.api_request('出货国家查询列表查询接口', data, headers)

    def Request_SaleCountry_getScFlowInfoFirst(self, data, headers):
        """
        TBM 出货国家查询 列表查询
        @param data:接口body
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家查询信息获取接口')
        return self.api_request('出货国家查询信息获取接口', data, headers)

    def Request_SaleCountry_LastedTemp(self, brandCode, headers):
        """
        TBM 出货国家流程 品牌模板
        @param bid:流程bid
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家流程获取品牌模板接口')
        logging.info(f'接口请求地址为：http://pfgatewayidct.transsion.com:9088/service-bom-archive/sale-country/template/getLastedTemp?brandCode={brandCode}&type=frontEnd')
        recall_response = requests.get(
            url=f'http://pfgatewayidct.transsion.com:9088/service-bom-archive/sale-country/template/getLastedTemp?brandCode={brandCode}&type=frontEnd',
            headers=headers)
        response_dicts = recall_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        logging.info('请求结束：出货国家流程获取品牌模板接口')
        return response_dicts

    def Request_SaleCountry_Info(self, bid, headers):
        """
        TBM 出货国家流程 获取单据信息
        @param bid:流程bid
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家流程获取单据信息接口')
        logging.info(f'接口请求地址为：http://pfgatewayidct.transsion.com:9088/service-bom-archive/sale-country/flow/queryScInfoByFlowBId?flowBid={bid}')
        recall_response = requests.get(
            url=f'http://pfgatewayidct.transsion.com:9088/service-bom-archive/sale-country/flow/queryScInfoByFlowBId?flowBid={bid}',
            headers=headers)
        response_dicts = recall_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        logging.info('请求结束：出货国家流程获取单据信息接口')
        return response_dicts

    def Request_SaleCountry_queryArchDetail(self, bid, headers):
        """
        TBM 出货国家查询 获取流程明细
        @param bid:流程bid
        @param headers:接口头部
        """
        logging.info('发起请求：出货国家查询获取流程明细接口')
        logging.info(f'接口请求地址为：http://pfgatewayidct.transsion.com:9088/service-bom-archive/sale-country/arch/queryArchDetailByBId?bid={bid}')
        recall_response = requests.get(
            url=f'http://pfgatewayidct.transsion.com:9088/service-bom-archive/sale-country/arch/queryArchDetailByBId?bid={bid}',
            headers=headers)
        response_dicts = recall_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        logging.info('请求结束：出货国家查询获取流程明细接口')
        return response_dicts

    @allure.step("出货国家流程新增接口")
    def API_SaleCountry_Add(self):
        logging.info('发起流程接口：出货国家流程新增流程')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        titletime = datetime.now().strftime('%Y-%m-%d')
        flowStartdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        querytime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        LastedTemp = self.Request_SaleCountry_LastedTemp('infinix', headers)
        add_data = {
            "prdInfoVOS": [
                {
                    "scPrdBaseInfoVO": {
                        "bizType": "create",
                        "globalVersion": "ver1",
                        "marketName": f"市场名称{querytime}",
                        "projectName": f"项目名称{querytime}",
                        "memory": "128+8",
                        "bandStrategy": "latinAmericaMarket",
                        "productManager": "18645960",
                        "projectManager": "18645960",
                        "brandCode": "infinix",
                        "editStatus": True,
                        "isAdd": True
                    },
                    "scPrdUniversalInfoMap": {
                        "camera": "摄像头",
                        "type": "型号",
                        "new": "新增",
                        "anthor": "Standard2",
                        "Color": [
                            "Aqua Blue"
                        ],
                        "inch": [
                            "RearCamera1"
                        ],
                        "FirstProductionTime": titletime
                    },
                    "countryProperties": {}
                }
            ],
            "flowMainVO": {
                "title": f"[李小素]-[{titletime}]",
                "flowNo": "",
                "flowProposer": "18645960",
                "flowDept": "PI_系统四部",
                "flowStartdate": flowStartdate,
                "remark": "",
                "busiType": "",
                "type": "frontEnd",
                "flowProposerName": "李小素"
            },
            "scProjectVO": {
                "brandCode": "infinix",
                "projectName": f"项目名称{querytime}",
                "templateBid": LastedTemp['data']['bid']
            },
            "submitType": "submit",
            "approvers": {
                "bisSupplyApprovers": [
                    {
                        "role": "",
                        "roleKey": "verb",
                        "userName": "",
                        "userNo": "18645960"
                    }
                ],
                "bisSupplySenders": [
                    {
                        "role": "",
                        "roleKey": "verc",
                        "userName": "",
                        "userNo": "18645960"
                    }
                ]
            },
            "areas": [],
            "uploadList": [],
            "fields": LastedTemp['data']['fields']
        }

        search_data = {"param": {"title": "", "flowNo": "", "projectName": f"项目名称{querytime}", "brandCode": "",
                                 "createdTimeFrom": "", "createdTimeTo": "", "flowProposer": "", "status": "",
                                 "flowStartdate": ""}, "current": 1, "size": 10}
        self.Request_SaleCountry_Add(add_data, headers)
        search_response = self.Request_SaleCountry_Search(search_data, headers)
        search_response_data = search_response['data']['data']
        logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，bid：{}'.format(search_response_data[0]['flowNo'],
                                                                    search_response_data[0]['instanceId'],
                                                                    search_response_data[0]['bid']))
        logging.info('流程接口结束：出货国家流程新增流程')
        return search_response_data[0]['flowNo'], search_response_data[0]['instanceId'], search_response_data[0]['bid']

    @allure.step("出货国家流程撤回删除接口")
    def API_SaleCountry_Delete(self, instanceid, bid):
        """
        通过调用接口发起撤回流程
        调用接口：oneworks流程撤回接口，出货国家流程删除已撤回接口
        @param instanceid:oneworks撤回流程编码
        @param bid:流程ID
        """
        logging.info('发起流程接口：出货国家流程撤回流程')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        delete_data = {"flowBid": bid}
        self.Oneworks_Recall(instanceid, headers)
        self.Request_SaleCountry_Delete(delete_data, headers)
        logging.info('流程接口结束：出货国家流程撤回流程')

    @allure.step("出货国家查询变更产品接口")
    def API_Change_Product(self, projectName):
        logging.info('发起流程接口：出货国家查询变更产品接口')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        LastedTemp = self.Request_SaleCountry_LastedTemp('infinix', headers)
        PageList_body = {
            "current": 1,
            "size": 10,
            "param": {
                "brandCode": "infinix",
                "nationCodes": [],
                "projectName": projectName
            }
        }
        PageList = self.Request_SaleCountry_PageList(PageList_body, headers)
        queryArchDetail = self.Request_SaleCountry_queryArchDetail(PageList['data']['data'][0]['bid'], headers)
        titletime = datetime.now().strftime('%Y-%m-%d')
        flowStartdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        testdate = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        change_data = {
            "prdInfoVOS": [
                {
                    "scPrdBaseInfoVO": {
                        "createdBy": "18645960",
                        "createdTime": queryArchDetail['data']['scArchiveProductVO']['createdTime'],
                        "updatedBy": "18645960",
                        "updatedTime":queryArchDetail['data']['scArchiveProductVO']['updatedTime'],
                        "companyId": queryArchDetail['data']['scArchiveProductVO']['companyId'],
                        "id": queryArchDetail['data']['scArchiveProductVO']['id'],
                        "bid": queryArchDetail['data']['scArchiveProductVO']['bid'],
                        "flowBid": queryArchDetail['data']['scArchiveProductVO']['flowBid'],
                        "bizType": "update",
                        "globalVersion": "ver3",
                        "marketName": f'{projectName}{testdate}',
                        "projectName": projectName,
                        "memory": "256+8",
                        "brandCode": "infinix",
                        "bandStrategy": "Indianmarket",
                        "productManager": "18645960",
                        "projectManager": "18645960",
                        "isDeleted": "0",
                        "rootBid": queryArchDetail['data']['scArchiveProductVO']['rootBid'],
                        "checkResultMessage": None,
                        "baseArchBid": None,
                        "countryProperties": {},
                        "countryField": None,
                        "dictMap": queryArchDetail['data']['scArchiveProductVO']['dictMap'],
                        "editStatus": False
                    },
                    "scPrdUniversalInfoMap": {
                        "camera": "摄像头test",
                        "type": "型号test",
                        "new": "新增test",
                        "anthor": "Standard2",
                        "Color": [
                            "Aqua Blue"
                        ],
                        "inch": ["RearCamera1"],
                        "FirstProductionTime": titletime
                    },
                    "countryProperties": {}
                }
            ],
            "flowMainVO": {
                "title": f"[李小素]-[{testdate}]",
                "flowNo": "",
                "flowProposer": "18645960",
                "flowDept": "PI_系统四部",
                "flowStartdate": flowStartdate,
                "remark": "",
                "type": "frontEnd",
                "busiType": "insOrUpdProduct",
                "flowProposerName": "李小素"
            },
            "scProjectVO": {
                "createdBy": None,
                "createdTime": None,
                "updatedBy": None,
                "updatedTime": None,
                "companyId": None,
                "id": None,
                "bid": None,
                "flowBid": None,
                "templateBid": LastedTemp['data']['bid'],
                "brandCode": queryArchDetail['data']['scArchiveProductVO']['brandCode'],
                "projectName": queryArchDetail['data']['scArchiveProductVO']['projectName'],
                "remark": None,
                "isDeleted": "0",
                "areaCodes": None,
                "areaCodeArr": None
            },
            "submitType": "submit",
            "approvers": {
                "bisSupplyApprovers": [
                    {
                        "role": "",
                        "roleKey": "verb",
                        "userName": "",
                        "userNo": "18645960"
                    }
                ],
                "bisSupplySenders": [
                    {
                        "role": "",
                        "roleKey": "verc",
                        "userName": "",
                        "userNo": "18645960"
                    }
                ]
            },
            "areas": [],
            "uploadList": [],
            "fields": LastedTemp['data']['fields']
        }
        search_data = {"param": {"title": f"[李小素]-[{testdate}]", "flowNo": "", "projectName": projectName, "brandCode": "",
                                 "createdTimeFrom": "", "createdTimeTo": "", "flowProposer": "", "status": "",
                                 "flowStartdate": ""}, "current": 1, "size": 10}
        self.Request_Change_Product(change_data, headers)
        search_response = self.Request_SaleCountry_Search(search_data, headers)
        for i in range(20):
            if len(search_response['data']['data']) == 0:
                sleep(1)
                search_response = self.Request_SaleCountry_Search(search_data, headers)
        search_response_data = search_response['data']['data']
        logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，bid：{}'.format(search_response_data[0]['flowNo'],
                                                                    search_response_data[0]['instanceId'],
                                                                    search_response_data[0]['bid']))
        logging.info('流程接口结束：出货国家查询变更产品接口')
        return search_response_data[0]['flowNo'], search_response_data[0]['instanceId'], search_response_data[0]['bid']

    @allure.step("出货国家查询变更国家接口")
    def API_Change_Country(self, projectName):
        logging.info('发起流程接口：出货国家查询变更国家接口')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        PageList_body = {
            "current": 1,
            "size": 10,
            "param": {
                "brandCode": "infinix",
                "nationCodes": [],
                "projectName": projectName
            }
        }
        PageList = self.Request_SaleCountry_PageList(PageList_body, headers)
        LastedTemp = self.Request_SaleCountry_LastedTemp('infinix', headers)
        getScFlowInfoFirst_body = {
            "archBids": [
                PageList['data']['data'][0]['bid']
            ],
            "brandCode": "infinix",
            "templateBid": LastedTemp['data']['bid'],
            "areaCodes": [
                "B12270"
            ],
            "itemType": "updCountry"
        }
        getScFlowInfoFirst = self.Request_SaleCountry_getScFlowInfoFirst(getScFlowInfoFirst_body, headers)
        titletime = datetime.now().strftime('%Y-%m-%d')
        flowStartdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        change_data = {
            "prdInfoVOS": [
                {
                    "scPrdBaseInfoVO": getScFlowInfoFirst['data']['prdInfoVOS'][0]['scPrdBaseInfoVO'],
                    "scPrdUniversalInfoMap": getScFlowInfoFirst['data']['prdInfoVOS'][0]['scPrdUniversalInfoMap'],
                    "countryProperties": {
                        "1231": "attestationBackups"
                    }
                }
            ],
            "flowMainVO": {
                "title": f"[李小素]-[{titletime}]",
                "flowNo": "",
                "flowProposer": "18645960",
                "flowDept": "PI_系统四部",
                "flowStartdate": flowStartdate,
                "remark": "",
                "busiType": "updCountry",
                "flowProposerName": "李小素"
            },
            "scProjectVO": getScFlowInfoFirst['data']['scProjectVO'],
            "submitType": "submit",
            "approvers": {
                "bisSupplyApprovers": [
                    {
                        "role": "",
                        "roleKey": "verb",
                        "userName": "",
                        "userNo": "18645960"
                    }
                ],
                "bisSupplySenders": [
                    {
                        "role": "",
                        "roleKey": "verc",
                        "userName": "",
                        "userNo": "18645960"
                    }
                ]
            },
            "areas": LastedTemp['data']['areas'],
            "uploadList": [],
            "fields": LastedTemp['data']['fields']
        }
        search_data = {"param": {"title": "", "flowNo": "", "projectName": projectName, "brandCode": "",
                                 "createdTimeFrom": "", "createdTimeTo": "", "flowProposer": "", "status": "",
                                 "flowStartdate": ""}, "current": 1, "size": 10}
        self.Request_Change_Product(change_data, headers)
        search_response = self.Request_SaleCountry_Search(search_data, headers)
        for i in range(20):
            if len(search_response['data']['data']) == 0:
                sleep(1)
                search_response = self.Request_SaleCountry_Search(search_data, headers)
        search_response_data = search_response['data']['data']
        logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，bid：{}'.format(search_response_data[0]['flowNo'],
                                                                    search_response_data[0]['instanceId'],
                                                                    search_response_data[0]['bid']))
        logging.info('流程接口结束：出货国家查询变更产品接口')
        return search_response_data[0]['flowNo'], search_response_data[0]['instanceId'], search_response_data[0]['bid']

    @allure.step("出货国家流程产品部管理员审核接口")
    def API_Change_Audit(self, flowNo, instanceid, bid):
        logging.info('发起流程接口：出货国家流程产品部管理员审核接口')
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        Info = self.Request_SaleCountry_Info(bid, headers)
        change_data = {
            "currentNodeCode": "productor_admin",
            "flowMainVO":
                Info['data']['flowMainVO'],
            "scProjectVO":
                Info['data']['scProjectVO'],
            "prdInfoVOS":
                Info['data']['prdInfoVOS'],
            "uploadList": [],
            "fields":
                Info['data']['fields'],
            "prdModifyInfoVOS":
                Info['data']['prdModifyInfoVOS'],
            "approvers":
                Info['data']['approvers'],
            "areas": Info['data']['areas']
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1,
                         "comment": ""}
        self.Request_SaleCountry_Audit(change_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：出货国家流程产品部管理员审核接口')

    @allure.step("出货国家流程产品部汇签审核接口")
    def API_Change_Join(self, flowNo, instanceid, bid):
        logging.info('发起流程接口：出货国家流程产品部汇签审核接口')
        self.API_Change_Audit(flowNo, instanceid, bid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        Info = self.Request_SaleCountry_Info(bid, headers)
        change_data = {
            "currentNodeCode": "productor_join",
            "flowMainVO":
                Info['data']['flowMainVO'],
            "scProjectVO":
                Info['data']['scProjectVO'],
            "prdInfoVOS":
                Info['data']['prdInfoVOS'],
            "uploadList": [],
            "fields":
                Info['data']['fields'],
            "prdModifyInfoVOS":
                Info['data']['prdModifyInfoVOS'],
            "approvers":
                Info['data']['approvers'],
            "areas": Info['data']['areas']
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1,
                         "comment": ""}
        self.Request_SaleCountry_Audit(change_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：出货国家流程产品部汇签审核接口')

    @allure.step("出货国家流程产品经理修改审核接口")
    def API_Change_managerModify(self, flowNo, instanceid, bid):
        logging.info('发起流程接口：出货国家流程产品经理修改审核接口')
        self.API_Change_Join(flowNo, instanceid, bid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        Info = self.Request_SaleCountry_Info(bid, headers)
        querytime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        titletime = datetime.now().strftime('%Y-%m-%d')
        LastedTemp = self.Request_SaleCountry_LastedTemp('infinix', headers)
        change_data = {
            "prdInfoVOS": [
                {
                    "scPrdBaseInfoVO": {
                        "createdBy": "18645960",
                        "createdTime": Info['data']['prdInfoVOS'][0]['scPrdBaseInfoVO']['createdTime'],
                        "updatedBy": "18645960",
                        "updatedTime": Info['data']['prdInfoVOS'][0]['scPrdBaseInfoVO']['updatedTime'],
                        "companyId": Info['data']['prdInfoVOS'][0]['scPrdBaseInfoVO']['companyId'],
                        "id": Info['data']['prdInfoVOS'][0]['scPrdBaseInfoVO']['id'],
                        "bid": Info['data']['prdInfoVOS'][0]['scPrdBaseInfoVO']['bid'],
                        "flowBid": Info['data']['prdInfoVOS'][0]['scPrdBaseInfoVO']['flowBid'],
                        "bizType": "update",
                        "globalVersion": "ver3",
                        "marketName": f"市场修改{querytime}",
                        "projectName": f"项目修改{querytime}",
                        "memory": "128+8",
                        "brandCode": "infinix",
                        "bandStrategy": "africanMarket",
                        "productManager": "18645960",
                        "projectManager": "18645960",
                        "isDeleted": "0",
                        "rootBid": Info['data']['prdInfoVOS'][0]['scPrdBaseInfoVO']['rootBid'],
                        "checkResultMessage": None,
                        "baseArchBid": None,
                        "countryProperties": {},
                        "countryField": "{}",
                        "dictMap": Info['data']['prdInfoVOS'][0]['scPrdBaseInfoVO']['dictMap'],
                        "editStatus": False
                    },
                    "scPrdUniversalInfoMap": {
                        "camera": "摄像头test",
                        "type": "型号test",
                        "new": "新增test",
                        "anthor": "Standard2",
                        "Color": [
                            "Aqua Blue"
                        ],
                        "inch": "RearCamera1",
                        "FirstProductionTime": titletime
                    },
                    "countryProperties": {}
                }
            ],
            "flowMainVO": Info['data']['flowMainVO'],
            "scProjectVO": Info['data']['scProjectVO'],
            "approvers": {
                "bisSupplyApprovers": [
                    {
                        "role": "",
                        "roleKey": "verb",
                        "userName": "",
                        "userNo": "18645960"
                    }
                ],
                "bisSupplySenders": [
                    {
                        "role": "",
                        "roleKey": "verc",
                        "userName": "",
                        "userNo": "18645960"
                    }
                ]
            },
            "areas": [],
            "fields": LastedTemp['data']['fields']
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1,
                         "comment": ""}
        self.Request_SaleCountry_managerModify(change_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：出货国家流程产品经理修改审核接口')

    @allure.step("出货国家流程产品部管理员复核接口")
    def API_Change_Audit2(self, flowNo, instanceid, bid):
        logging.info('发起流程接口：出货国家流程产品部管理员审核接口')
        self.API_Change_managerModify(flowNo, instanceid, bid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        Info = self.Request_SaleCountry_Info(bid, headers)
        change_data = {
            "currentNodeCode": "productor_admin2",
            "flowMainVO":
                Info['data']['flowMainVO'],
            "scProjectVO":
                Info['data']['scProjectVO'],
            "prdInfoVOS":
                Info['data']['prdInfoVOS'],
            "uploadList": [],
            "fields":
                Info['data']['fields'],
            "prdModifyInfoVOS":
                Info['data']['prdModifyInfoVOS'],
            "approvers":
                Info['data']['approvers'],
            "areas": Info['data']['areas']
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1,
                         "comment": ""}
        self.Request_SaleCountry_Audit(change_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：出货国家流程产品部管理员审核接口')

    def Request_Foreign_Add(self, data, headers):
        """
        TBM 外研BOM协作 新增流程
        @param data: 接口body
        @param headers:接口头部
        """
        logging.info('发起请求：外研BOM协作新增接口')
        return self.api_request('外研BOM协作新增接口', data, headers)

    @allure.step("外研BOM协作新增接口")
    def API_Foreign_Add(self):
        logging.info('发起流程：外研BOM协作新增接口')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        querytime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        add_data = {
            "flowId": None,
            "flowNodeName": "start",
            "bomArchive": {
                "flowNo": "",
                "flowProposer": "18645960",
                "flowProposerName": "李小素",
                "flowStartdate": querytime,
                "bomVer": "",
                "bomVersion": "batch",
                "brandCode": "itel",
                "market": "ET",
                "produceClass": "userProvi",
                "templateId": None,
                "templateName": "",
                "isLocalPurchase": "",
                "bomClass": "",
                "model": "JMB-01",
                "note": "",
                "title": f"[李小素]-[{querytime[:10]}]",
                "flowDept": "PI_系统四部",
                "bomModel": "retailValueModel",
                "curFlowCode": "structureStart"
            },
            "refFactoryList": [
                {
                    "matCode": "12004875",
                    "note": "单机头_Spice_Z301_G282Z2_蓝色_无卡_IN",
                    "statusCodeLabel": "量产",
                    "statusCode": "batch",
                    "homePackagingFactory": "1201",
                    "homeChipFactory": "/",
                    "overseasPackagingFactory": "/",
                    "overseasChipFactory": "/"
                }
            ],
            "bomTreeVOList": [
                {
                    "id": "new_bom_3000",
                    "bomName": "客供BOM",
                    "statusCode": "batch",
                    "baseQty": "1000",
                    "childNodes": [
                        {
                            "id": 1002,
                            "baseQty": "1000",
                            "index": 0,
                            "serialNo": "1.1",
                            "matCode": "12800002",
                            "deleteValidate": False,
                            "note": "整机外包料Infinix_X5010_AW878_黑_A欧_P02_Ⅰ",
                            "matAttr": "外研"
                        }
                    ],
                    "isRoot": True,
                    "index": 0,
                    "serialNo": 1,
                    "matCode": "12004875",
                    "deleteValidate": False,
                    "note": "单机头_Spice_Z301_G282Z2_蓝色_无卡_IN",
                    "matAttr": "可选"
                }
            ],
            "approvers": {
                "bisReviewApprovers": [
                    {
                        "role": "qpm_review",
                        "userNo": "18645960"
                    },
                    {
                        "role": "ppm_review",
                        "userNo": "18645960"
                    },
                    {
                        "role": "foreign_purchase",
                        "userNo": ""
                    },
                    {
                        "role": "hardware",
                        "userNo": ""
                    },
                    {
                        "role": "rf_review",
                        "userNo": ""
                    },
                    {
                        "role": "video",
                        "userNo": ""
                    },
                    {
                        "role": "structure",
                        "userNo": ""
                    },
                    {
                        "role": "skd_mpm",
                        "userNo": ""
                    },
                    {
                        "role": "ckd_mpm",
                        "userNo": ""
                    },
                    {
                        "role": "other",
                        "userNo": ""
                    }
                ],
                "bisSupplyApprovers": []
            },
            "uploadList": [],
            "submitType": "submit"
        }
        search_data = {
            "param": {
                "bomCode": "12004875",
                "bomType": "foreignBom",
                "createdTimeFrom": "",
                "createdTimeTo": ""
            },
            "current": 1,
            "size": 10
        }
        add_response = self.Request_Foreign_Add(add_data, headers)
        flowId = add_response['data']
        search_response = self.Request_Bom_Search(search_data, headers)
        search_response_data = search_response['data']['data']
        for i in search_response_data:
            if i['flowId'] == flowId:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，FlowID：{}'.format(i['flowNo'], i['instanceId'], flowId))
                logging.info('流程结束：外研BOM协作新增接口')
                return i['flowNo'], i['instanceId'], flowId

    @allure.step("外研BOM协作-衍生-新增接口")
    def API_Foreign_Derived_Add(self):
        logging.info('发起流程：外研BOM协作新增接口')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        querytime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        add_data = {
            "flowId": None,
            "flowNodeName": "start",
            "bomArchive": {
                "flowNo": "",
                "flowProposer": "18645960",
                "flowProposerName": "李小素",
                "flowStartdate": querytime,
                "bomVer": "",
                "bomVersion": "batch",
                "brandCode": "itel",
                "market": "ET",
                "produceClass": "userProviDerive",
                "templateId": None,
                "templateName": "",
                "isLocalPurchase": "",
                "bomClass": "",
                "model": "JMB-01",
                "note": "",
                "title": f"[李小素]-[{querytime[:10]}]",
                "flowDept": "PI_系统四部",
                "bomModel": "retailValueModel",
                "curFlowCode": "structureStart"
            },
            "bomDeriveList": [
                {
                    "no": None,
                    "newBomCode": "12000003",
                    "newBomName": "单机头_TECNO_T722_E680B1_红色_4G",
                    "rightBomName": "单机头_TECNO_T722_E680B1_红色_4G",
                    "originalBomCode": "12014351",
                    "originalBomName": "单机头_TECNO_AC8_H853_A1_莫奈之夏_PK_256+8",
                    "rightOriginalBomName": "单机头_TECNO_AC8_H853_A1_莫奈之夏_PK_256+8",
                    "originalBomFactory": "PL01",
                    "checkResultMessage": "",
                    "matMap": {
                        "originalBomCode": "单机头_TECNO_AC8_H853_A1_莫奈之夏_PK_256+8",
                        "newBomCode_matAttr": "可选",
                        "newBomCode": "单机头_TECNO_T722_E680B1_红色_4G",
                        "originalBomCode_matAttr": "可选"
                    }
                }
            ],
            "otherDeriveList": [
                {
                    "no": "1",
                    "pMatCode": "12000003",
                    "pMatNote": "单机头_TECNO_T722_E680B1_红色_4G",
                    "rightBomName": "单机头_TECNO_T722_E680B1_红色_4G",
                    "operation": "add",
                    "childMaterialCode": "12800001",
                    "childMaterialNote": "整机外包料Infinix_X5010_AW878_金_A欧_P01_Ⅰ",
                    "rightMatDescZh": "整机外包料Infinix_X5010_AW878_金_A欧_P01_Ⅰ",
                    "baseQty": "1000",
                    "replaceGroup": None,
                    "usePercent": None,
                    "checkResultMessage": "",
                    "matMap": {
                        "pMatCode_matAttr": "可选",
                        "pMatCode": "单机头_TECNO_T722_E680B1_红色_4G",
                        "childMaterialCode_matAttr": "外研",
                        "childMaterialCode": "整机外包料Infinix_X5010_AW878_金_A欧_P01_Ⅰ"
                    }
                }
            ],
            "refFactoryList": [
                {
                    "checkResultMessage": "",
                    "num": 1,
                    "matCode": "12000003",
                    "note": "单机头_TECNO_T722_E680B1_红色_4G",
                    "statusCode": "batch",
                    "homePackagingFactory": "1201",
                    "homeChipFactory": "/",
                    "overseasPackagingFactory": "/",
                    "overseasChipFactory": "/",
                    "rightNote": None,
                    "matMap": {
                        "matCode_matAttr": "可选",
                        "matCode": "单机头_TECNO_T722_E680B1_红色_4G"
                    },
                    "statusCodeLabel": "量产"
                }
            ],
            "bomDeriveTreeVOList": [
                {
                    "bomNodeCode": "1030523214364807229",
                    "bomNo": "1",
                    "bomName": "客供BOM",
                    "isArchive": 0,
                    "applyScope": "userProviDerive",
                    "matCode": "12000003",
                    "baseQty": "1000",
                    "note": "单机头_TECNO_T722_E680B1_红色_4G",
                    "statusCode": "batch",
                    "isRoot": True,
                    "matAttr": "可选",
                    "bomUseage": "1",
                    "isDerive": 1,
                    "nativePcbfactory": "PL01",
                    "childNodes": [
                        {
                            "bomNodeCode": "1030523214532579328",
                            "matCode": "12800001",
                            "baseQty": "1000",
                            "note": "整机外包料Infinix_X5010_AW878_金_A欧_P01_Ⅰ",
                            "matAttr": "外研",
                            "dealDelFlag": False,
                            "operation": "add",
                            "id": "1030523214532579328",
                            "index": 0,
                            "serialNo": "1.1"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1030523214364807575",
                            "isArchive": 0,
                            "matCode": "12106748",
                            "baseQty": "1000",
                            "note": "贴片副板_H853_FLASH_1_A_V1.2_自制",
                            "matAttr": "可选",
                            "bomUseage": "1",
                            "parentNodeCode": "1030523214364807229",
                            "sapLevel": 1,
                            "dealDelFlag": False,
                            "id": "1030523214364807575",
                            "index": 1,
                            "serialNo": "1.2"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1030523214364807341",
                            "isArchive": 0,
                            "matCode": "12106917",
                            "baseQty": "1000",
                            "note": "贴片主板_H853_A1_256GB+8GB_V1.4_自制",
                            "matAttr": "可选",
                            "bomUseage": "1",
                            "parentNodeCode": "1030523214364807229",
                            "sapLevel": 1,
                            "dealDelFlag": False,
                            "id": "1030523214364807341",
                            "index": 2,
                            "serialNo": "1.3"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1030523214364807300",
                            "isArchive": 0,
                            "matCode": "12106918",
                            "baseQty": "1000",
                            "note": "贴片副板_H853_1_A1_V1.3_自制",
                            "matAttr": "可选",
                            "bomUseage": "1",
                            "parentNodeCode": "1030523214364807229",
                            "sapLevel": 1,
                            "dealDelFlag": False,
                            "id": "1030523214364807300",
                            "index": 3,
                            "serialNo": "1.4"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1030523214364807289",
                            "isArchive": 0,
                            "matCode": "12202727",
                            "baseQty": "1000",
                            "note": "预加工_中框+组合件(触摸屏+显示屏)_AC8_莫奈之夏",
                            "matAttr": "可选",
                            "bomUseage": "1",
                            "parentNodeCode": "1030523214364807229",
                            "sapLevel": 1,
                            "dealDelFlag": False,
                            "id": "1030523214364807289",
                            "index": 4,
                            "serialNo": "1.5"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1030523214364807238",
                            "isArchive": 0,
                            "matCode": "12304722",
                            "baseQty": "1000",
                            "note": "虚拟共用件_TECNO_AC8",
                            "matAttr": "可选",
                            "bomUseage": "1",
                            "parentNodeCode": "1030523214364807229",
                            "sapLevel": 1,
                            "dealDelFlag": False,
                            "id": "1030523214364807238",
                            "index": 5,
                            "serialNo": "1.6"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1030523214364807237",
                            "isArchive": 0,
                            "matCode": "21204821",
                            "baseQty": "1000",
                            "note": "电池盖组件_AC8_莫奈之夏",
                            "matAttr": "可选",
                            "bomUseage": "1",
                            "parentNodeCode": "1030523214364807229",
                            "sapLevel": 1,
                            "dealDelFlag": False,
                            "id": "1030523214364807237",
                            "index": 6,
                            "serialNo": "1.7"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1030523214364807236",
                            "isArchive": 0,
                            "matCode": "21303385",
                            "baseQty": "1000",
                            "note": "音量键组件_AC8_莫奈之夏",
                            "matAttr": "可选",
                            "bomUseage": "1",
                            "parentNodeCode": "1030523214364807229",
                            "sapLevel": 1,
                            "dealDelFlag": False,
                            "id": "1030523214364807236",
                            "index": 7,
                            "serialNo": "1.8"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1030523214364807235",
                            "isArchive": 0,
                            "matCode": "21303386",
                            "baseQty": "1000",
                            "note": "电源键组件_AC8_莫奈之夏",
                            "matAttr": "可选",
                            "bomUseage": "1",
                            "parentNodeCode": "1030523214364807229",
                            "sapLevel": 1,
                            "dealDelFlag": False,
                            "id": "1030523214364807235",
                            "index": 8,
                            "serialNo": "1.9"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1030523214364807234",
                            "isArchive": 0,
                            "matCode": "23202306",
                            "baseQty": "1000",
                            "note": "后摄像头镜片_AC8_康宁3代_0.6mm_莫奈之夏",
                            "matAttr": "可选",
                            "bomUseage": "1",
                            "parentNodeCode": "1030523214364807229",
                            "sapLevel": 1,
                            "dealDelFlag": False,
                            "id": "1030523214364807234",
                            "index": 9,
                            "serialNo": "1.10"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1030523214364807233",
                            "isArchive": 0,
                            "matCode": "23504286",
                            "baseQty": "1000",
                            "note": "后摄装饰件组件_AC8_莫奈之夏",
                            "matAttr": "可选",
                            "bomUseage": "1",
                            "parentNodeCode": "1030523214364807229",
                            "sapLevel": 1,
                            "dealDelFlag": False,
                            "id": "1030523214364807233",
                            "index": 10,
                            "serialNo": "1.11"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1030523214364807232",
                            "isArchive": 0,
                            "matCode": "23504287",
                            "baseQty": "1000",
                            "note": "卡托组件_AC8_莫奈之夏",
                            "matAttr": "可选",
                            "bomUseage": "1",
                            "parentNodeCode": "1030523214364807229",
                            "sapLevel": 1,
                            "dealDelFlag": False,
                            "id": "1030523214364807232",
                            "index": 11,
                            "serialNo": "1.12"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1030523214364807231",
                            "isArchive": 0,
                            "matCode": "23603441",
                            "baseQty": "1000",
                            "note": "保护膜_三层_AC8_透明",
                            "matAttr": "可选",
                            "bomUseage": "1",
                            "parentNodeCode": "1030523214364807229",
                            "sapLevel": 1,
                            "dealDelFlag": False,
                            "id": "1030523214364807231",
                            "index": 12,
                            "serialNo": "1.13"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1030523214364807230",
                            "isArchive": 0,
                            "matCode": "23603454",
                            "baseQty": "1000",
                            "note": "单层膜_全包膜_AC8",
                            "matAttr": "可选",
                            "bomUseage": "1",
                            "parentNodeCode": "1030523214364807229",
                            "sapLevel": 1,
                            "dealDelFlag": False,
                            "id": "1030523214364807230",
                            "index": 13,
                            "serialNo": "1.14"
                        }
                    ],
                    "parentNodeCode": "0",
                    "nodeName": "单机头",
                    "sapLevel": 0,
                    "dealDelFlag": False,
                    "id": "1030523214364807229",
                    "index": 0,
                    "serialNo": 1
                }
            ],
            "approvers": {
                "bisReviewApprovers": [
                    {
                        "role": "qpm_review",
                        "userNo": "18645960"
                    },
                    {
                        "role": "ppm_review",
                        "userNo": "18645960"
                    },
                    {
                        "role": "foreign_purchase",
                        "userNo": ""
                    },
                    {
                        "role": "hardware",
                        "userNo": ""
                    },
                    {
                        "role": "rf_review",
                        "userNo": ""
                    },
                    {
                        "role": "video",
                        "userNo": ""
                    },
                    {
                        "role": "structure",
                        "userNo": ""
                    },
                    {
                        "role": "skd_mpm",
                        "userNo": ""
                    },
                    {
                        "role": "ckd_mpm",
                        "userNo": ""
                    },
                    {
                        "role": "other",
                        "userNo": ""
                    }
                ],
                "bisSupplyApprovers": []
            },
            "uploadList": [],
            "submitType": "submit"
        }
        search_data = {
            "param": {
                "bomCode": "12000003",
                "bomType": "foreignBom",
                "createdTimeFrom": "",
                "createdTimeTo": ""
            },
            "current": 1,
            "size": 10
        }
        add_response = self.Request_Foreign_Add(add_data, headers)
        flowId = add_response['data']
        search_response = self.Request_Bom_Search(search_data, headers)
        search_response_data = search_response['data']['data']
        for i in search_response_data:
            if i['flowId'] == flowId:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，FlowID：{}'.format(i['flowNo'], i['instanceId'], flowId))
                logging.info('流程结束：外研BOM协作新增接口')
                return i['flowNo'], i['instanceId'], flowId

    @allure.step("外研BOM协作新增接口")
    def API_Foreign_Failed_Add(self):
        logging.info('发起流程：外研BOM协作新增接口')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        querytime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        add_data = {
            "flowId": None,
            "flowNodeName": "start",
            "bomArchive": {
                "flowNo": "",
                "flowProposer": "18645960",
                "flowProposerName": "李小素",
                "flowStartdate": querytime,
                "bomVer": "",
                "bomVersion": "batch",
                "brandCode": "itel",
                "market": "ET",
                "produceClass": "userProvi",
                "templateId": None,
                "templateName": "",
                "isLocalPurchase": "",
                "bomClass": "",
                "model": "JMB-01",
                "note": "",
                "title": f"[李小素]-[{querytime[:10]}]",
                "flowDept": "PI_系统四部",
                "bomModel": "retailValueModel",
                "curFlowCode": "structureStart"
            },
            "refFactoryList": [
                {
                    "matCode": "12300083",
                    "note": "虚拟单机头包_TECNO_L7_QP18_蓝色_16GB+2GB",
                    "statusCodeLabel": "量产",
                    "statusCode": "batch",
                    "homePackagingFactory": "1201",
                    "homeChipFactory": "/",
                    "overseasPackagingFactory": "/",
                    "overseasChipFactory": "/"
                }
            ],
            "bomTreeVOList": [
                {
                    "id": "new_bom_3000",
                    "bomName": "客供BOM",
                    "statusCode": "batch",
                    "baseQty": "1000",
                    "childNodes": [
                        {
                            "id": 1002,
                            "baseQty": "1000",
                            "index": 0,
                            "serialNo": "1.1",
                            "matCode": "12800002",
                            "deleteValidate": False,
                            "note": "整机外包料Infinix_X5010_AW878_黑_A欧_P02_Ⅰ",
                            "matAttr": "外研"
                        }
                    ],
                    "isRoot": True,
                    "index": 0,
                    "serialNo": 1,
                    "matCode": "12300083",
                    "deleteValidate": False,
                    "note": "虚拟单机头包_TECNO_L7_QP18_蓝色_16GB+2GB",
                    "matAttr": "可选"
                }
            ],
            "approvers": {
                "bisReviewApprovers": [
                    {
                        "role": "qpm_review",
                        "userNo": "18645960"
                    },
                    {
                        "role": "ppm_review",
                        "userNo": "18645960"
                    },
                    {
                        "role": "foreign_purchase",
                        "userNo": ""
                    },
                    {
                        "role": "hardware",
                        "userNo": ""
                    },
                    {
                        "role": "rf_review",
                        "userNo": ""
                    },
                    {
                        "role": "video",
                        "userNo": ""
                    },
                    {
                        "role": "structure",
                        "userNo": ""
                    },
                    {
                        "role": "skd_mpm",
                        "userNo": ""
                    },
                    {
                        "role": "ckd_mpm",
                        "userNo": ""
                    },
                    {
                        "role": "other",
                        "userNo": ""
                    }
                ],
                "bisSupplyApprovers": []
            },
            "uploadList": [],
            "submitType": "submit"
        }
        search_data = {
            "param": {
                "bomCode": "12300083",
                "bomType": "foreignBom",
                "createdTimeFrom": "",
                "createdTimeTo": ""
            },
            "current": 1,
            "size": 10
        }
        add_response = self.Request_Foreign_Add(add_data, headers)
        flowId = add_response['data']
        search_response = self.Request_Bom_Search(search_data, headers)
        search_response_data = search_response['data']['data']
        for i in search_response_data:
            if i['flowId'] == flowId:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，FlowID：{}'.format(i['flowNo'], i['instanceId'], flowId))
                logging.info('流程结束：外研BOM协作新增接口')
                return i['flowNo'], i['instanceId'], flowId

    def Request_Foreign_Approval(self, data, headers):
        """
        TBM 外研BOM协作 业务审核流程
        @param data: 接口body
        @param headers:接口头部
        """
        logging.info('发起请求：外研BOM协作业务审核接口')
        return self.api_request('外研BOM协作业务审核接口', data, headers)

    def Oneworks_queryBomForeignInfo(self, flowId, headers):
        """
        TBM oneworks 查询外研流程信息
        @param flowId:oneworks  flowId
        @param headers:接口头部
        """
        logging.info('发起请求：oneworks查询流程历史接口')
        logging.info(f'接口请求地址为：http://pfgatewayidct.transsion.com:9088/service-bom-archive/bom-arc/foreign/queryBomInfoByFlowId?flowId={flowId}')
        history_response = requests.get(
            url=f'http://pfgatewayidct.transsion.com:9088/service-bom-archive/bom-arc/foreign/queryBomInfoByFlowId?flowId={flowId}',
            headers=headers)
        response_dicts = history_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        logging.info('请求结束：oneworks查询流程历史接口')
        return response_dicts

    @allure.step("外研BOM协作-业务审核通过接口")
    def API_Foreign_Approval(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：外研BOM协作-业务审核通过流程')
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        BomForeignInfo = self.Oneworks_queryBomForeignInfo(flowid, headers)
        approve_data = {
            "flowId": "flowid",
            "flowNodeName": "bisReview",
            "bomArchive":
                BomForeignInfo['data']['bomArchive'],
            "approvers":
                BomForeignInfo['data']['approvers'],
            "bomTreeVOList":
                BomForeignInfo['data']['bomTreeVOList'],
            "refFactoryList":
                BomForeignInfo['data']['refFactoryList'],
            "bomDeriveList":
                BomForeignInfo['data']['bomDeriveList'],
            "copyRuleList": [],
            "otherDeriveList":
                BomForeignInfo['data']['otherDeriveList'],
            "uploadList": [],
            "bomImportKeyDeviceList": [],
            "purchaseList": None,
            "role": "qpm_review,ppm_review",
            "bomDeriveTreeVOList":
                BomForeignInfo['data']['bomDeriveTreeVOList'],
            "virtualChipList": None,
            "diffCollectList": None
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_Foreign_Approval(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：外研BOM协作-业务审核通过流程')

    def Request_PCBA_Add(self, data, headers):
        """
        TBM PCBABOM协作 新增流程
        @param data: 接口body
        @param headers:接口头部
        """
        logging.info('发起请求：PCBABOM协作新增接口')
        return self.api_request('PCBABOM协作新增接口', data, headers)

    @allure.step("PCBABOM协作新增接口")
    def API_PCBA_Add(self):
        logging.info('发起流程：外研BOM协作新增接口')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        querytime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        add_data = {
            "flowId": None,
            "flowNodeName": "start",
            "bomArchive": {
                "flowNo": "",
                "flowProposer": "18645960",
                "flowProposerName": "李小素",
                "flowStartdate": querytime,
                "bomVer": "",
                "bomVersion": "trial",
                "brandCode": "infinix",
                "produceClass": "pcba",
                "templateId": 1017727,
                "templateName": "infinix_001_临时模板",
                "isLocalPurchase": "",
                "doVirtualChip": False,
                "checkKeyDevice": True,
                "bomClass": "",
                "model": "JMB-01",
                "note": "",
                "title": f"[李小素]-[{querytime[:10]}]",
                "researchType": "selfResearch",
                "flowDept": "PI_系统四部",
                "curFlowCode": "structureStart"
            },
            "bomDeriveList": [],
            "otherDeriveList": [],
            "bomTreeVOList": [
                {
                    "id": "new_bom_3000",
                    "matGroup": "121,123,129,131,144",
                    "bomName": "PCBA",
                    "statusCode": "trial",
                    "matCount": "1",
                    "nodeClass": "actual",
                    "businessRole": "rf,baseBand,nps,structure,mpm,other",
                    "tempNodeId": 3649,
                    "childNodes": [
                        {
                            "id": "new_bom_3001",
                            "matGroup": "155,158",
                            "bomName": "PCB155/158",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3650,
                            "childNodes": [],
                            "index": 0,
                            "serialNo": "1.1"
                        },
                        {
                            "id": "new_bom_3002",
                            "matGroup": "140,156",
                            "bomName": "CPU",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3651,
                            "childNodes": [],
                            "index": 1,
                            "serialNo": "1.2"
                        },
                        {
                            "id": "new_bom_3003",
                            "matGroup": "142",
                            "bomName": "存储器142",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3652,
                            "childNodes": [],
                            "index": 2,
                            "serialNo": "1.3"
                        },
                        {
                            "id": "new_bom_3004",
                            "matGroup": "141,157",
                            "bomName": "套片141/157",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3653,
                            "childNodes": [],
                            "index": 3,
                            "serialNo": "1.4"
                        },
                        {
                            "id": "new_bom_3005",
                            "matGroup": "156",
                            "bomName": "IC器件156",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3654,
                            "childNodes": [],
                            "index": 4,
                            "serialNo": "1.5"
                        },
                        {
                            "id": "new_bom_3006",
                            "matGroup": "143",
                            "bomName": "IC143",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3655,
                            "childNodes": [],
                            "index": 5,
                            "serialNo": "1.6"
                        },
                        {
                            "id": "new_bom_3007",
                            "matGroup": "144",
                            "bomName": "IC144",
                            "matCount": 5,
                            "position": "U1001,U1002,U1003,U1004,U1005",
                            "nodeClass": "actual",
                            "businessRole": "baseBand,nps",
                            "tempNodeId": 3656,
                            "childNodes": [],
                            "index": 6,
                            "serialNo": "1.7",
                            "matCode": "14400003",
                            "deleteValidate": False,
                            "note": "IC-Gsensor,2axis,8bit,WLCSP6,H1.015",
                            "matAttr": "可选",
                            "positionCount": 5
                        },
                        {
                            "id": "new_bom_3008",
                            "matGroup": "145",
                            "bomName": "IC145",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3657,
                            "childNodes": [],
                            "index": 7,
                            "serialNo": "1.8"
                        },
                        {
                            "id": "new_bom_3009",
                            "matGroup": "146",
                            "bomName": "IC146",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3658,
                            "childNodes": [],
                            "index": 8,
                            "serialNo": "1.9"
                        },
                        {
                            "id": "new_bom_3010",
                            "matGroup": "147",
                            "bomName": "IC147",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3659,
                            "childNodes": [],
                            "index": 9,
                            "serialNo": "1.10"
                        },
                        {
                            "id": "new_bom_3011",
                            "matGroup": "148",
                            "bomName": "IC148",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3660,
                            "childNodes": [],
                            "index": 10,
                            "serialNo": "1.11"
                        },
                        {
                            "id": "new_bom_3012",
                            "matGroup": "149",
                            "bomName": "晶体149",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3661,
                            "childNodes": [],
                            "index": 11,
                            "serialNo": "1.12"
                        },
                        {
                            "id": "new_bom_3013",
                            "matGroup": "150",
                            "bomName": "二极管",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3662,
                            "childNodes": [],
                            "index": 12,
                            "serialNo": "1.13"
                        },
                        {
                            "id": "new_bom_3014",
                            "matGroup": "151",
                            "bomName": "磁珠151",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3663,
                            "childNodes": [],
                            "index": 13,
                            "serialNo": "1.14"
                        },
                        {
                            "id": "new_bom_3015",
                            "matGroup": "151",
                            "bomName": "电感151",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3664,
                            "childNodes": [],
                            "index": 14,
                            "serialNo": "1.15"
                        },
                        {
                            "id": "new_bom_3016",
                            "matGroup": "151",
                            "bomName": "电容151",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3665,
                            "childNodes": [],
                            "index": 15,
                            "serialNo": "1.16"
                        },
                        {
                            "id": "new_bom_3017",
                            "matGroup": "151",
                            "bomName": "电阻151",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3666,
                            "childNodes": [],
                            "index": 16,
                            "serialNo": "1.17"
                        },
                        {
                            "id": "new_bom_3018",
                            "matGroup": "151",
                            "bomName": "功率电感151",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3667,
                            "childNodes": [],
                            "index": 17,
                            "serialNo": "1.18"
                        },
                        {
                            "id": "new_bom_3019",
                            "matGroup": "151",
                            "bomName": "其他151",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3668,
                            "childNodes": [],
                            "index": 18,
                            "serialNo": "1.19"
                        },
                        {
                            "id": "new_bom_3020",
                            "matGroup": "192",
                            "bomName": "MIC192",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3669,
                            "childNodes": [],
                            "index": 19,
                            "serialNo": "1.20"
                        },
                        {
                            "id": "new_bom_3021",
                            "matGroup": "152,153",
                            "bomName": "结构贴片料",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3670,
                            "childNodes": [],
                            "index": 20,
                            "serialNo": "1.21"
                        },
                        {
                            "id": "new_bom_3022",
                            "matGroup": "154",
                            "bomName": "弹片/屏蔽罩",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3671,
                            "childNodes": [],
                            "index": 21,
                            "serialNo": "1.22"
                        }
                    ],
                    "isRoot": True,
                    "index": 0,
                    "serialNo": 1,
                    "matCode": "12100001",
                    "deleteValidate": False,
                    "note": "PCBA_Mainboard_NL01_128MB+64MB_T630S",
                    "matAttr": "可选"
                }
            ],
            "bomDeriveTreeVOList": [
                {
                    "id": "new_bom_3000",
                    "matGroup": "121,123,129,131,144",
                    "bomName": "PCBA",
                    "statusCode": "trial",
                    "matCount": "1",
                    "nodeClass": "actual",
                    "businessRole": "rf,baseBand,nps,structure,mpm,other",
                    "tempNodeId": 3649,
                    "childNodes": [
                        {
                            "id": "new_bom_3001",
                            "matGroup": "155,158",
                            "bomName": "PCB155/158",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3650,
                            "childNodes": [],
                            "index": 0,
                            "serialNo": "1.1"
                        },
                        {
                            "id": "new_bom_3002",
                            "matGroup": "140,156",
                            "bomName": "CPU",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3651,
                            "childNodes": [],
                            "index": 1,
                            "serialNo": "1.2"
                        },
                        {
                            "id": "new_bom_3003",
                            "matGroup": "142",
                            "bomName": "存储器142",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3652,
                            "childNodes": [],
                            "index": 2,
                            "serialNo": "1.3"
                        },
                        {
                            "id": "new_bom_3004",
                            "matGroup": "141,157",
                            "bomName": "套片141/157",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3653,
                            "childNodes": [],
                            "index": 3,
                            "serialNo": "1.4"
                        },
                        {
                            "id": "new_bom_3005",
                            "matGroup": "156",
                            "bomName": "IC器件156",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3654,
                            "childNodes": [],
                            "index": 4,
                            "serialNo": "1.5"
                        },
                        {
                            "id": "new_bom_3006",
                            "matGroup": "143",
                            "bomName": "IC143",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3655,
                            "childNodes": [],
                            "index": 5,
                            "serialNo": "1.6"
                        },
                        {
                            "id": "new_bom_3007",
                            "matGroup": "144",
                            "bomName": "IC144",
                            "matCount": 5,
                            "position": "U1001,U1002,U1003,U1004,U1005",
                            "nodeClass": "actual",
                            "businessRole": "baseBand,nps",
                            "tempNodeId": 3656,
                            "childNodes": [],
                            "index": 6,
                            "serialNo": "1.7",
                            "matCode": "14400003",
                            "deleteValidate": False,
                            "note": "IC-Gsensor,2axis,8bit,WLCSP6,H1.015",
                            "matAttr": "可选",
                            "positionCount": 5
                        },
                        {
                            "id": "new_bom_3008",
                            "matGroup": "145",
                            "bomName": "IC145",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3657,
                            "childNodes": [],
                            "index": 7,
                            "serialNo": "1.8"
                        },
                        {
                            "id": "new_bom_3009",
                            "matGroup": "146",
                            "bomName": "IC146",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3658,
                            "childNodes": [],
                            "index": 8,
                            "serialNo": "1.9"
                        },
                        {
                            "id": "new_bom_3010",
                            "matGroup": "147",
                            "bomName": "IC147",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3659,
                            "childNodes": [],
                            "index": 9,
                            "serialNo": "1.10"
                        },
                        {
                            "id": "new_bom_3011",
                            "matGroup": "148",
                            "bomName": "IC148",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3660,
                            "childNodes": [],
                            "index": 10,
                            "serialNo": "1.11"
                        },
                        {
                            "id": "new_bom_3012",
                            "matGroup": "149",
                            "bomName": "晶体149",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3661,
                            "childNodes": [],
                            "index": 11,
                            "serialNo": "1.12"
                        },
                        {
                            "id": "new_bom_3013",
                            "matGroup": "150",
                            "bomName": "二极管",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3662,
                            "childNodes": [],
                            "index": 12,
                            "serialNo": "1.13"
                        },
                        {
                            "id": "new_bom_3014",
                            "matGroup": "151",
                            "bomName": "磁珠151",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3663,
                            "childNodes": [],
                            "index": 13,
                            "serialNo": "1.14"
                        },
                        {
                            "id": "new_bom_3015",
                            "matGroup": "151",
                            "bomName": "电感151",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3664,
                            "childNodes": [],
                            "index": 14,
                            "serialNo": "1.15"
                        },
                        {
                            "id": "new_bom_3016",
                            "matGroup": "151",
                            "bomName": "电容151",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3665,
                            "childNodes": [],
                            "index": 15,
                            "serialNo": "1.16"
                        },
                        {
                            "id": "new_bom_3017",
                            "matGroup": "151",
                            "bomName": "电阻151",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3666,
                            "childNodes": [],
                            "index": 16,
                            "serialNo": "1.17"
                        },
                        {
                            "id": "new_bom_3018",
                            "matGroup": "151",
                            "bomName": "功率电感151",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3667,
                            "childNodes": [],
                            "index": 17,
                            "serialNo": "1.18"
                        },
                        {
                            "id": "new_bom_3019",
                            "matGroup": "151",
                            "bomName": "其他151",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3668,
                            "childNodes": [],
                            "index": 18,
                            "serialNo": "1.19"
                        },
                        {
                            "id": "new_bom_3020",
                            "matGroup": "192",
                            "bomName": "MIC192",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3669,
                            "childNodes": [],
                            "index": 19,
                            "serialNo": "1.20"
                        },
                        {
                            "id": "new_bom_3021",
                            "matGroup": "152,153",
                            "bomName": "结构贴片料",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3670,
                            "childNodes": [],
                            "index": 20,
                            "serialNo": "1.21"
                        },
                        {
                            "id": "new_bom_3022",
                            "matGroup": "154",
                            "bomName": "弹片/屏蔽罩",
                            "nodeClass": "actual",
                            "businessRole": "baseBand",
                            "tempNodeId": 3671,
                            "childNodes": [],
                            "index": 21,
                            "serialNo": "1.22"
                        }
                    ],
                    "isRoot": True,
                    "index": 0,
                    "serialNo": 1,
                    "matCode": "12100001",
                    "deleteValidate": False,
                    "note": "PCBA_Mainboard_NL01_128MB+64MB_T630S",
                    "matAttr": "可选"
                }
            ],
            "virtualChipList": [],
            "approvers": {
                "bisReviewApprovers": [],
                "bisSupplyApprovers": [
                    {
                        "role": "mpm",
                        "userNo": "18645960"
                    },
                    {
                        "role": "rf",
                        "userNo": ""
                    },
                    {
                        "role": "pm",
                        "userNo": ""
                    }
                ]
            },
            "uploadList": [],
            "submitType": "submit"
        }
        search_data = {
            "param": {
                "title": "",
                "flowNo": "",
                "bomCode": "",
                "produceClass": "",
                "model": "",
                "brandCode": "",
                "bomVer": "",
                "statusCode": "",
                "synStatus": "",
                "createdBy": "",
                "createdTimeFrom": "",
                "createdTimeTo": "",
                "bomType": "pcba"
            },
            "current": 1,
            "size": 10
        }
        add_response = self.Request_PCBA_Add(add_data, headers)
        flowId = add_response['data']
        search_response = self.Request_Bom_Search(search_data, headers)
        search_response_data = search_response['data']['data']
        for i in search_response_data:
            if i['flowId'] == flowId:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，FlowID：{}'.format(i['flowNo'], i['instanceId'], flowId))
                logging.info('流程结束：外研BOM协作新增接口')
                return i['flowNo'], i['instanceId'], flowId

    @allure.step("PCBABOM协作新增接口")
    def API_PCBA_Derived_Add(self):
        logging.info('发起流程：外研BOM协作新增接口')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        querytime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        add_data = {
            "flowId": None,
            "flowNodeName": "start",
            "bomArchive": {
                "flowNo": "",
                "flowProposer": "18645960",
                "flowProposerName": "李小素",
                "flowStartdate": querytime,
                "bomVer": "",
                "bomVersion": "trial",
                "brandCode": "infinix",
                "produceClass": "pcbaDerive",
                "templateId": 1017727,
                "templateName": "infinix_001_临时模板",
                "isLocalPurchase": "",
                "doVirtualChip": False,
                "checkKeyDevice": False,
                "bomClass": "",
                "model": "JMB-01",
                "note": "",
                "title": f"[李小素]-[{querytime[:10]}]",
                "researchType": "selfResearch",
                "flowDept": "PI_系统四部",
                "curFlowCode": "structureStart"
            },
            "bomDeriveList": [
                {
                    "statusCode": "试产",
                    "no": None,
                    "newBomCode": "12198883",
                    "newBomName": "PCBA_itel_it1655S_M30B_4+512_单卡_SKU4",
                    "originalBomCode": "12106993",
                    "originalBomName": "贴片副板_F6316_1_J_V1.0_自制",
                    "originalBomFactory": "C105",
                    "checkResultMessage": "",
                    "matMap": {
                        "originalBomCode": "贴片副板_F6316_1_J_V1.0_自制",
                        "newBomCode_matAttr": "",
                        "newBomCode": "PCBA_itel_it1655S_M30B_4+512_单卡_SKU4",
                        "originalBomCode_matAttr": "可选"
                    }
                }
            ],
            "otherDeriveList": [
                {
                    "no": None,
                    "pMatCode": "12198883",
                    "pMatNote": "PCBA_itel_it1655S_M30B_4+512_单卡_SKU4",
                    "operation": "add",
                    "childMaterialCode": "12105695",
                    "childMaterialNote": "贴片副板_H850A_A1_TEST_PCBA_V3.0_自制",
                    "matCount": 1,
                    "position": None,
                    "replaceGroup": None,
                    "usePercent": None,
                    "checkResultMessage": "",
                    "matMap": {
                        "pMatCode_matAttr": "",
                        "pMatCode": "PCBA_itel_it1655S_M30B_4+512_单卡_SKU4",
                        "childMaterialCode_matAttr": "可选",
                        "childMaterialCode": "贴片副板_H850A_A1_TEST_PCBA_V3.0_自制"
                    }
                }
            ],
            "bomTreeVOList": [
                {
                    "bomNodeCode": "1034767881574944768",
                    "bomName": "PCBA",
                    "isArchive": 0,
                    "applyScope": "pcbaBom",
                    "matCode": "12198883",
                    "baseQty": "1000",
                    "note": "PCBA_itel_it1655S_M30B_4+512_单卡_SKU4",
                    "statusCode": "trial",
                    "tempNodeId": 3649,
                    "isRoot": True,
                    "matGroup": "121,123,129,131,144",
                    "bomUseage": "2",
                    "isDerive": 1,
                    "nativePcbfactory": "C105",
                    "childNodes": [
                        {
                            "companyId": 100,
                            "bomNodeCode": "1034767881574944807",
                            "bomName": "PCB155/158",
                            "isArchive": 0,
                            "matCode": "15800648",
                            "baseQty": "1000",
                            "note": "副板PCB_F6316_SUB_PCB_1_4L_V1.0_ZBX",
                            "tempNodeId": 3650,
                            "matGroup": "155,158",
                            "matAttr": "可选",
                            "bomUseage": "2",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "PCB155/158",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "155,158",
                            "seqNo": 1,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "matCount": 1,
                            "id": "1034767881574944807",
                            "index": 0,
                            "serialNo": "1.1"
                        },
                        {
                            "bomNodeCode": "1034767881574944806",
                            "bomName": "CPU",
                            "tempNodeId": 3651,
                            "matGroup": "140,156",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "CPU",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "140,156",
                            "seqNo": 2,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944806",
                            "index": 1,
                            "serialNo": "1.2"
                        },
                        {
                            "bomNodeCode": "1034767881574944805",
                            "bomName": "存储器142",
                            "tempNodeId": 3652,
                            "matGroup": "142",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "存储器142",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "142",
                            "seqNo": 3,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944805",
                            "index": 2,
                            "serialNo": "1.3"
                        },
                        {
                            "bomNodeCode": "1034767881574944804",
                            "bomName": "套片141/157",
                            "tempNodeId": 3653,
                            "matGroup": "141,157",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "套片141/157",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "141,157",
                            "seqNo": 4,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944804",
                            "index": 3,
                            "serialNo": "1.4"
                        },
                        {
                            "bomNodeCode": "1034767881574944803",
                            "bomName": "IC器件156",
                            "tempNodeId": 3654,
                            "matGroup": "156",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "IC器件156",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "156",
                            "seqNo": 5,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944803",
                            "index": 4,
                            "serialNo": "1.5"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1034767881574944802",
                            "bomName": "IC143",
                            "isArchive": 0,
                            "matCode": "14301313",
                            "baseQty": "1000",
                            "note": "天线开关:IC-ANT TUNE,SP4T,0.5-2.7G,MXD8544A",
                            "tempNodeId": 3655,
                            "matGroup": "143",
                            "matAttr": "标准",
                            "bomUseage": "2",
                            "position": "U1",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "IC143",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "143",
                            "seqNo": 6,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "matCount": 1,
                            "id": "1034767881574944802",
                            "index": 5,
                            "serialNo": "1.6"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1034767881574944801",
                            "bomName": "IC144",
                            "isArchive": 0,
                            "matCode": "14401255",
                            "baseQty": "1000",
                            "note": "过压保护芯片:IC-OVP,12balls,50ns,ET9540CL",
                            "tempNodeId": 3656,
                            "matGroup": "144",
                            "matAttr": "标准",
                            "bomUseage": "2",
                            "position": "U3",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "IC144",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "144",
                            "seqNo": 7,
                            "dealDelFlag": False,
                            "businessRole": "baseBand,nps",
                            "matCount": 1,
                            "id": "1034767881574944801",
                            "index": 6,
                            "serialNo": "1.7"
                        },
                        {
                            "bomNodeCode": "1034767881574944800",
                            "bomName": "IC145",
                            "tempNodeId": 3657,
                            "matGroup": "145",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "IC145",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "145",
                            "seqNo": 8,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944800",
                            "index": 7,
                            "serialNo": "1.8"
                        },
                        {
                            "bomNodeCode": "1034767881574944799",
                            "bomName": "IC146",
                            "tempNodeId": 3658,
                            "matGroup": "146",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "IC146",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "146",
                            "seqNo": 9,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944799",
                            "index": 8,
                            "serialNo": "1.9"
                        },
                        {
                            "bomNodeCode": "1034767881574944798",
                            "bomName": "IC147",
                            "tempNodeId": 3659,
                            "matGroup": "147",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "IC147",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "147",
                            "seqNo": 10,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944798",
                            "index": 9,
                            "serialNo": "1.10"
                        },
                        {
                            "bomNodeCode": "1034767881574944797",
                            "bomName": "IC148",
                            "tempNodeId": 3660,
                            "matGroup": "148",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "IC148",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "148",
                            "seqNo": 11,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944797",
                            "index": 10,
                            "serialNo": "1.11"
                        },
                        {
                            "bomNodeCode": "1034767881574944796",
                            "bomName": "晶体149",
                            "tempNodeId": 3661,
                            "matGroup": "149",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "晶体149",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "149",
                            "seqNo": 12,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944796",
                            "index": 11,
                            "serialNo": "1.12"
                        },
                        {
                            "bomNodeCode": "1034767881574944791",
                            "bomName": "二极管",
                            "tempNodeId": 3662,
                            "matGroup": "150",
                            "childNodes": [
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944793",
                                    "isArchive": 0,
                                    "matCode": "15001184",
                                    "baseQty": "1000",
                                    "note": "TVS-EOS-Nonpolar,24V,350pF,SOD-123FL",
                                    "matAttr": "优选",
                                    "bomUseage": "2",
                                    "position": "D1",
                                    "parentNodeCode": "1034767881574944791",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944793",
                                    "index": 0,
                                    "serialNo": "1.13.1"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944795",
                                    "isArchive": 0,
                                    "matCode": "15001090",
                                    "baseQty": "1000",
                                    "note": "TVS-polar,2-Lines,5V,1.4pF,0402",
                                    "matAttr": "优选",
                                    "bomUseage": "2",
                                    "position": "T1",
                                    "parentNodeCode": "1034767881574944791",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944795",
                                    "index": 1,
                                    "serialNo": "1.13.2"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944794",
                                    "isArchive": 0,
                                    "matCode": "15001143",
                                    "baseQty": "2000",
                                    "note": "TVS-5.0V,10pF,0402",
                                    "replaceGroup": "D1",
                                    "usePercent": 70,
                                    "matAttr": "优选",
                                    "bomUseage": "2",
                                    "position": "T5,T6",
                                    "priority": 2,
                                    "strategy": "2",
                                    "parentNodeCode": "1034767881574944791",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 2,
                                    "id": "1034767881574944794",
                                    "index": 2,
                                    "serialNo": "1.13.3"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944792",
                                    "isArchive": 0,
                                    "matCode": "15001197",
                                    "baseQty": "2000",
                                    "note": "瞬态抑制二极管;TVS-Nonpolar,5V,10pF-0402",
                                    "replaceGroup": "D1",
                                    "usePercent": 30,
                                    "matAttr": "优选",
                                    "bomUseage": "2",
                                    "position": "T5,T6",
                                    "priority": 1,
                                    "strategy": "2",
                                    "parentNodeCode": "1034767881574944791",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 2,
                                    "id": "1034767881574944792",
                                    "index": 3,
                                    "serialNo": "1.13.4"
                                }
                            ],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "二极管",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "150",
                            "seqNo": 13,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944791",
                            "index": 12,
                            "serialNo": "1.13"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1034767881574944790",
                            "bomName": "磁珠151",
                            "isArchive": 0,
                            "matCode": "15102740",
                            "baseQty": "2000",
                            "note": "磁珠:BEAD,1.25R,1000R@100M,250mA,0402H0.65",
                            "tempNodeId": 3663,
                            "matGroup": "151",
                            "matAttr": "优选",
                            "bomUseage": "2",
                            "position": "R10,R7",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "磁珠151",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "151",
                            "seqNo": 14,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "matCount": 2,
                            "id": "1034767881574944790",
                            "index": 13,
                            "serialNo": "1.14"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1034767881574944789",
                            "bomName": "电感151",
                            "isArchive": 0,
                            "matCode": "15102116",
                            "baseQty": "1000",
                            "note": "电感:IND-ML,1.8NH,±0.1NH,0201,Sunlord",
                            "tempNodeId": 3664,
                            "matGroup": "151",
                            "matAttr": "标准",
                            "bomUseage": "2",
                            "position": "C10",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "电感151",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "151",
                            "seqNo": 15,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "matCount": 1,
                            "id": "1034767881574944789",
                            "index": 14,
                            "serialNo": "1.15"
                        },
                        {
                            "bomNodeCode": "1034767881574944782",
                            "bomName": "电容151",
                            "tempNodeId": 3665,
                            "matGroup": "151",
                            "childNodes": [
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944787",
                                    "isArchive": 0,
                                    "matCode": "15100124",
                                    "baseQty": "6000",
                                    "note": "CAP-33pF,+/-5%,COG,50V,0201",
                                    "matAttr": "可选",
                                    "bomUseage": "2",
                                    "position": "C1,C2,C3,C4,C5,C6",
                                    "parentNodeCode": "1034767881574944782",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 6,
                                    "id": "1034767881574944787",
                                    "index": 0,
                                    "serialNo": "1.16.1"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944785",
                                    "isArchive": 0,
                                    "matCode": "15100147",
                                    "baseQty": "2000",
                                    "note": "CAP-1uF,6.3V,±20%,X5R,0201",
                                    "matAttr": "可选",
                                    "bomUseage": "2",
                                    "position": "C11,C14",
                                    "parentNodeCode": "1034767881574944782",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 2,
                                    "id": "1034767881574944785",
                                    "index": 1,
                                    "serialNo": "1.16.2"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944788",
                                    "isArchive": 0,
                                    "matCode": "15100076",
                                    "baseQty": "1000",
                                    "note": "CAP-27pF,+/-5%,COG,25V,0201",
                                    "matAttr": "可选",
                                    "bomUseage": "2",
                                    "position": "C16",
                                    "parentNodeCode": "1034767881574944782",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944788",
                                    "index": 2,
                                    "serialNo": "1.16.3"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944786",
                                    "isArchive": 0,
                                    "matCode": "15100139",
                                    "baseQty": "1000",
                                    "note": "CAP-2.2pF,+/-0.25pF,COG,50V,0201",
                                    "matAttr": "可选",
                                    "bomUseage": "2",
                                    "position": "C17",
                                    "parentNodeCode": "1034767881574944782",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944786",
                                    "index": 3,
                                    "serialNo": "1.16.4"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944783",
                                    "isArchive": 0,
                                    "matCode": "15102447",
                                    "baseQty": "1000",
                                    "note": "电容:CAP-1uF,+/-10%,X5R,25V,0402,H0.55",
                                    "matAttr": "优选",
                                    "bomUseage": "2",
                                    "position": "C8",
                                    "parentNodeCode": "1034767881574944782",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944783",
                                    "index": 4,
                                    "serialNo": "1.16.5"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944784",
                                    "isArchive": 0,
                                    "matCode": "15101831",
                                    "baseQty": "1000",
                                    "note": "CAP-1uF,+/-10%,X5R,16V-0402",
                                    "matAttr": "优选",
                                    "bomUseage": "2",
                                    "position": "C9",
                                    "parentNodeCode": "1034767881574944782",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944784",
                                    "index": 5,
                                    "serialNo": "1.16.6"
                                }
                            ],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "电容151",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "151",
                            "seqNo": 16,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944782",
                            "index": 15,
                            "serialNo": "1.16"
                        },
                        {
                            "bomNodeCode": "1034767881574944778",
                            "bomName": "电阻151",
                            "tempNodeId": 3666,
                            "matGroup": "151",
                            "childNodes": [
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944781",
                                    "isArchive": 0,
                                    "matCode": "15100060",
                                    "baseQty": "4000",
                                    "note": "RES-0R,+/-5%,1/20W,0201",
                                    "matAttr": "可选",
                                    "bomUseage": "2",
                                    "position": "R1,R2,R3,R6",
                                    "parentNodeCode": "1034767881574944778",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 4,
                                    "id": "1034767881574944781",
                                    "index": 0,
                                    "serialNo": "1.17.1"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944779",
                                    "isArchive": 0,
                                    "matCode": "15101545",
                                    "baseQty": "1000",
                                    "note": "RES-100K,1%,1/20W,0201",
                                    "matAttr": "优选",
                                    "bomUseage": "2",
                                    "position": "R5",
                                    "parentNodeCode": "1034767881574944778",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944779",
                                    "index": 1,
                                    "serialNo": "1.17.2"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944780",
                                    "isArchive": 0,
                                    "matCode": "15100063",
                                    "baseQty": "1000",
                                    "note": "RES-10K,+/-5%,1/20W,0201",
                                    "matAttr": "可选",
                                    "bomUseage": "2",
                                    "position": "R8",
                                    "parentNodeCode": "1034767881574944778",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944780",
                                    "index": 2,
                                    "serialNo": "1.17.3"
                                }
                            ],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "电阻151",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "151",
                            "seqNo": 17,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944778",
                            "index": 16,
                            "serialNo": "1.17"
                        },
                        {
                            "bomNodeCode": "1034767881574944777",
                            "bomName": "功率电感151",
                            "tempNodeId": 3667,
                            "matGroup": "151",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "功率电感151",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "151",
                            "seqNo": 18,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944777",
                            "index": 17,
                            "serialNo": "1.18"
                        },
                        {
                            "bomNodeCode": "1034767881574944776",
                            "bomName": "其他151",
                            "tempNodeId": 3668,
                            "matGroup": "151",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "其他151",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "151",
                            "seqNo": 19,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944776",
                            "index": 18,
                            "serialNo": "1.19"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1034767881574944775",
                            "bomName": "MIC192",
                            "isArchive": 0,
                            "matCode": "19201021",
                            "baseQty": "1000",
                            "note": "MIC-C,2.2K,-42dB±3dB,直径4*1.55,带防尘网,Goer",
                            "tempNodeId": 3669,
                            "matGroup": "192",
                            "matAttr": "标准",
                            "bomUseage": "2",
                            "position": "U2",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "MIC192",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "192",
                            "seqNo": 20,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "matCount": 1,
                            "id": "1034767881574944775",
                            "index": 19,
                            "serialNo": "1.20"
                        },
                        {
                            "bomNodeCode": "1034767881574944771",
                            "bomName": "结构贴片料",
                            "tempNodeId": 3670,
                            "matGroup": "152,153",
                            "childNodes": [
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944773",
                                    "isArchive": 0,
                                    "matCode": "15201166",
                                    "baseQty": "1000",
                                    "note": "板板连接器,T/H=0.7,7.80x1.90x0.7,30PIN,JAE",
                                    "matAttr": "标准",
                                    "bomUseage": "2",
                                    "position": "J1",
                                    "parentNodeCode": "1034767881574944771",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944773",
                                    "index": 0,
                                    "serialNo": "1.21.1"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944774",
                                    "isArchive": 0,
                                    "matCode": "15201023",
                                    "baseQty": "1000",
                                    "note": "USS RF CONN,T/H1.3,2.0x2.0x0.7,ECT",
                                    "matAttr": "标准",
                                    "bomUseage": "2",
                                    "position": "J2",
                                    "parentNodeCode": "1034767881574944771",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944774",
                                    "index": 1,
                                    "serialNo": "1.21.2"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944772",
                                    "isArchive": 0,
                                    "matCode": "15301324",
                                    "baseQty": "1000",
                                    "note": "USB,B,T/S-1.3,5.85*9.6*2.45,5PIN",
                                    "matAttr": "标准",
                                    "bomUseage": "2",
                                    "position": "J3",
                                    "parentNodeCode": "1034767881574944771",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944772",
                                    "index": 2,
                                    "serialNo": "1.21.3"
                                }
                            ],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "结构贴片料",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "152,153",
                            "seqNo": 21,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944771",
                            "index": 20,
                            "serialNo": "1.21"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1034767881574944770",
                            "bomName": "弹片/屏蔽罩",
                            "isArchive": 0,
                            "matCode": "15401620",
                            "baseQty": "4000",
                            "note": "Antenna Spring,WH=0.6,1.8*1*1.0",
                            "tempNodeId": 3671,
                            "matGroup": "154",
                            "matAttr": "标准",
                            "bomUseage": "2",
                            "position": "ANT1,ANT2,ANT3,ANT4",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "弹片/屏蔽罩",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "154",
                            "seqNo": 22,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "matCount": 4,
                            "id": "1034767881574944770",
                            "index": 21,
                            "serialNo": "1.22"
                        },
                        {
                            "bomNodeCode": "1034767881574944769",
                            "bomName": "其他",
                            "isArchive": 0,
                            "matCode": "12105695",
                            "baseQty": "1000",
                            "note": "贴片副板_H850A_A1_TEST_PCBA_V3.0_自制",
                            "tempNodeId": -999,
                            "matAttr": "可选",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "其他",
                            "nodeClass": "other",
                            "seqNo": 999999999,
                            "dealDelFlag": False,
                            "operation": "add",
                            "matCount": 1,
                            "id": "1034767881574944769",
                            "index": 22,
                            "serialNo": "1.23"
                        }
                    ],
                    "parentNodeCode": "0",
                    "nodeName": "PCBA",
                    "nodeClass": "actual",
                    "sapLevel": 0,
                    "templateMatGroup": "121,123,129,131,144",
                    "seqNo": 1,
                    "dealDelFlag": False,
                    "businessRole": "rf,baseBand,nps,structure,mpm,other",
                    "matCount": 1,
                    "id": "1034767881574944768",
                    "index": 0,
                    "serialNo": 1
                }
            ],
            "bomDeriveTreeVOList": [
                {
                    "bomNodeCode": "1034767881574944768",
                    "bomName": "PCBA",
                    "isArchive": 0,
                    "applyScope": "pcbaBom",
                    "matCode": "12198883",
                    "baseQty": "1000",
                    "note": "PCBA_itel_it1655S_M30B_4+512_单卡_SKU4",
                    "statusCode": "trial",
                    "tempNodeId": 3649,
                    "isRoot": True,
                    "matGroup": "121,123,129,131,144",
                    "bomUseage": "2",
                    "isDerive": 1,
                    "nativePcbfactory": "C105",
                    "childNodes": [
                        {
                            "companyId": 100,
                            "bomNodeCode": "1034767881574944807",
                            "bomName": "PCB155/158",
                            "isArchive": 0,
                            "matCode": "15800648",
                            "baseQty": "1000",
                            "note": "副板PCB_F6316_SUB_PCB_1_4L_V1.0_ZBX",
                            "tempNodeId": 3650,
                            "matGroup": "155,158",
                            "matAttr": "可选",
                            "bomUseage": "2",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "PCB155/158",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "155,158",
                            "seqNo": 1,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "matCount": 1,
                            "id": "1034767881574944807",
                            "index": 0,
                            "serialNo": "1.1"
                        },
                        {
                            "bomNodeCode": "1034767881574944806",
                            "bomName": "CPU",
                            "tempNodeId": 3651,
                            "matGroup": "140,156",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "CPU",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "140,156",
                            "seqNo": 2,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944806",
                            "index": 1,
                            "serialNo": "1.2"
                        },
                        {
                            "bomNodeCode": "1034767881574944805",
                            "bomName": "存储器142",
                            "tempNodeId": 3652,
                            "matGroup": "142",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "存储器142",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "142",
                            "seqNo": 3,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944805",
                            "index": 2,
                            "serialNo": "1.3"
                        },
                        {
                            "bomNodeCode": "1034767881574944804",
                            "bomName": "套片141/157",
                            "tempNodeId": 3653,
                            "matGroup": "141,157",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "套片141/157",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "141,157",
                            "seqNo": 4,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944804",
                            "index": 3,
                            "serialNo": "1.4"
                        },
                        {
                            "bomNodeCode": "1034767881574944803",
                            "bomName": "IC器件156",
                            "tempNodeId": 3654,
                            "matGroup": "156",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "IC器件156",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "156",
                            "seqNo": 5,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944803",
                            "index": 4,
                            "serialNo": "1.5"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1034767881574944802",
                            "bomName": "IC143",
                            "isArchive": 0,
                            "matCode": "14301313",
                            "baseQty": "1000",
                            "note": "天线开关:IC-ANT TUNE,SP4T,0.5-2.7G,MXD8544A",
                            "tempNodeId": 3655,
                            "matGroup": "143",
                            "matAttr": "标准",
                            "bomUseage": "2",
                            "position": "U1",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "IC143",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "143",
                            "seqNo": 6,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "matCount": 1,
                            "id": "1034767881574944802",
                            "index": 5,
                            "serialNo": "1.6"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1034767881574944801",
                            "bomName": "IC144",
                            "isArchive": 0,
                            "matCode": "14401255",
                            "baseQty": "1000",
                            "note": "过压保护芯片:IC-OVP,12balls,50ns,ET9540CL",
                            "tempNodeId": 3656,
                            "matGroup": "144",
                            "matAttr": "标准",
                            "bomUseage": "2",
                            "position": "U3",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "IC144",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "144",
                            "seqNo": 7,
                            "dealDelFlag": False,
                            "businessRole": "baseBand,nps",
                            "matCount": 1,
                            "id": "1034767881574944801",
                            "index": 6,
                            "serialNo": "1.7"
                        },
                        {
                            "bomNodeCode": "1034767881574944800",
                            "bomName": "IC145",
                            "tempNodeId": 3657,
                            "matGroup": "145",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "IC145",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "145",
                            "seqNo": 8,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944800",
                            "index": 7,
                            "serialNo": "1.8"
                        },
                        {
                            "bomNodeCode": "1034767881574944799",
                            "bomName": "IC146",
                            "tempNodeId": 3658,
                            "matGroup": "146",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "IC146",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "146",
                            "seqNo": 9,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944799",
                            "index": 8,
                            "serialNo": "1.9"
                        },
                        {
                            "bomNodeCode": "1034767881574944798",
                            "bomName": "IC147",
                            "tempNodeId": 3659,
                            "matGroup": "147",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "IC147",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "147",
                            "seqNo": 10,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944798",
                            "index": 9,
                            "serialNo": "1.10"
                        },
                        {
                            "bomNodeCode": "1034767881574944797",
                            "bomName": "IC148",
                            "tempNodeId": 3660,
                            "matGroup": "148",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "IC148",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "148",
                            "seqNo": 11,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944797",
                            "index": 10,
                            "serialNo": "1.11"
                        },
                        {
                            "bomNodeCode": "1034767881574944796",
                            "bomName": "晶体149",
                            "tempNodeId": 3661,
                            "matGroup": "149",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "晶体149",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "149",
                            "seqNo": 12,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944796",
                            "index": 11,
                            "serialNo": "1.12"
                        },
                        {
                            "bomNodeCode": "1034767881574944791",
                            "bomName": "二极管",
                            "tempNodeId": 3662,
                            "matGroup": "150",
                            "childNodes": [
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944793",
                                    "isArchive": 0,
                                    "matCode": "15001184",
                                    "baseQty": "1000",
                                    "note": "TVS-EOS-Nonpolar,24V,350pF,SOD-123FL",
                                    "matAttr": "优选",
                                    "bomUseage": "2",
                                    "position": "D1",
                                    "parentNodeCode": "1034767881574944791",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944793",
                                    "index": 0,
                                    "serialNo": "1.13.1"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944795",
                                    "isArchive": 0,
                                    "matCode": "15001090",
                                    "baseQty": "1000",
                                    "note": "TVS-polar,2-Lines,5V,1.4pF,0402",
                                    "matAttr": "优选",
                                    "bomUseage": "2",
                                    "position": "T1",
                                    "parentNodeCode": "1034767881574944791",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944795",
                                    "index": 1,
                                    "serialNo": "1.13.2"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944794",
                                    "isArchive": 0,
                                    "matCode": "15001143",
                                    "baseQty": "2000",
                                    "note": "TVS-5.0V,10pF,0402",
                                    "replaceGroup": "D1",
                                    "usePercent": 70,
                                    "matAttr": "优选",
                                    "bomUseage": "2",
                                    "position": "T5,T6",
                                    "priority": 2,
                                    "strategy": "2",
                                    "parentNodeCode": "1034767881574944791",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 2,
                                    "id": "1034767881574944794",
                                    "index": 2,
                                    "serialNo": "1.13.3"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944792",
                                    "isArchive": 0,
                                    "matCode": "15001197",
                                    "baseQty": "2000",
                                    "note": "瞬态抑制二极管;TVS-Nonpolar,5V,10pF-0402",
                                    "replaceGroup": "D1",
                                    "usePercent": 30,
                                    "matAttr": "优选",
                                    "bomUseage": "2",
                                    "position": "T5,T6",
                                    "priority": 1,
                                    "strategy": "2",
                                    "parentNodeCode": "1034767881574944791",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 2,
                                    "id": "1034767881574944792",
                                    "index": 3,
                                    "serialNo": "1.13.4"
                                }
                            ],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "二极管",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "150",
                            "seqNo": 13,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944791",
                            "index": 12,
                            "serialNo": "1.13"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1034767881574944790",
                            "bomName": "磁珠151",
                            "isArchive": 0,
                            "matCode": "15102740",
                            "baseQty": "2000",
                            "note": "磁珠:BEAD,1.25R,1000R@100M,250mA,0402H0.65",
                            "tempNodeId": 3663,
                            "matGroup": "151",
                            "matAttr": "优选",
                            "bomUseage": "2",
                            "position": "R10,R7",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "磁珠151",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "151",
                            "seqNo": 14,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "matCount": 2,
                            "id": "1034767881574944790",
                            "index": 13,
                            "serialNo": "1.14"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1034767881574944789",
                            "bomName": "电感151",
                            "isArchive": 0,
                            "matCode": "15102116",
                            "baseQty": "1000",
                            "note": "电感:IND-ML,1.8NH,±0.1NH,0201,Sunlord",
                            "tempNodeId": 3664,
                            "matGroup": "151",
                            "matAttr": "标准",
                            "bomUseage": "2",
                            "position": "C10",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "电感151",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "151",
                            "seqNo": 15,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "matCount": 1,
                            "id": "1034767881574944789",
                            "index": 14,
                            "serialNo": "1.15"
                        },
                        {
                            "bomNodeCode": "1034767881574944782",
                            "bomName": "电容151",
                            "tempNodeId": 3665,
                            "matGroup": "151",
                            "childNodes": [
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944787",
                                    "isArchive": 0,
                                    "matCode": "15100124",
                                    "baseQty": "6000",
                                    "note": "CAP-33pF,+/-5%,COG,50V,0201",
                                    "matAttr": "可选",
                                    "bomUseage": "2",
                                    "position": "C1,C2,C3,C4,C5,C6",
                                    "parentNodeCode": "1034767881574944782",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 6,
                                    "id": "1034767881574944787",
                                    "index": 0,
                                    "serialNo": "1.16.1"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944785",
                                    "isArchive": 0,
                                    "matCode": "15100147",
                                    "baseQty": "2000",
                                    "note": "CAP-1uF,6.3V,±20%,X5R,0201",
                                    "matAttr": "可选",
                                    "bomUseage": "2",
                                    "position": "C11,C14",
                                    "parentNodeCode": "1034767881574944782",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 2,
                                    "id": "1034767881574944785",
                                    "index": 1,
                                    "serialNo": "1.16.2"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944788",
                                    "isArchive": 0,
                                    "matCode": "15100076",
                                    "baseQty": "1000",
                                    "note": "CAP-27pF,+/-5%,COG,25V,0201",
                                    "matAttr": "可选",
                                    "bomUseage": "2",
                                    "position": "C16",
                                    "parentNodeCode": "1034767881574944782",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944788",
                                    "index": 2,
                                    "serialNo": "1.16.3"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944786",
                                    "isArchive": 0,
                                    "matCode": "15100139",
                                    "baseQty": "1000",
                                    "note": "CAP-2.2pF,+/-0.25pF,COG,50V,0201",
                                    "matAttr": "可选",
                                    "bomUseage": "2",
                                    "position": "C17",
                                    "parentNodeCode": "1034767881574944782",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944786",
                                    "index": 3,
                                    "serialNo": "1.16.4"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944783",
                                    "isArchive": 0,
                                    "matCode": "15102447",
                                    "baseQty": "1000",
                                    "note": "电容:CAP-1uF,+/-10%,X5R,25V,0402,H0.55",
                                    "matAttr": "优选",
                                    "bomUseage": "2",
                                    "position": "C8",
                                    "parentNodeCode": "1034767881574944782",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944783",
                                    "index": 4,
                                    "serialNo": "1.16.5"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944784",
                                    "isArchive": 0,
                                    "matCode": "15101831",
                                    "baseQty": "1000",
                                    "note": "CAP-1uF,+/-10%,X5R,16V-0402",
                                    "matAttr": "优选",
                                    "bomUseage": "2",
                                    "position": "C9",
                                    "parentNodeCode": "1034767881574944782",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944784",
                                    "index": 5,
                                    "serialNo": "1.16.6"
                                }
                            ],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "电容151",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "151",
                            "seqNo": 16,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944782",
                            "index": 15,
                            "serialNo": "1.16"
                        },
                        {
                            "bomNodeCode": "1034767881574944778",
                            "bomName": "电阻151",
                            "tempNodeId": 3666,
                            "matGroup": "151",
                            "childNodes": [
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944781",
                                    "isArchive": 0,
                                    "matCode": "15100060",
                                    "baseQty": "4000",
                                    "note": "RES-0R,+/-5%,1/20W,0201",
                                    "matAttr": "可选",
                                    "bomUseage": "2",
                                    "position": "R1,R2,R3,R6",
                                    "parentNodeCode": "1034767881574944778",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 4,
                                    "id": "1034767881574944781",
                                    "index": 0,
                                    "serialNo": "1.17.1"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944779",
                                    "isArchive": 0,
                                    "matCode": "15101545",
                                    "baseQty": "1000",
                                    "note": "RES-100K,1%,1/20W,0201",
                                    "matAttr": "优选",
                                    "bomUseage": "2",
                                    "position": "R5",
                                    "parentNodeCode": "1034767881574944778",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944779",
                                    "index": 1,
                                    "serialNo": "1.17.2"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944780",
                                    "isArchive": 0,
                                    "matCode": "15100063",
                                    "baseQty": "1000",
                                    "note": "RES-10K,+/-5%,1/20W,0201",
                                    "matAttr": "可选",
                                    "bomUseage": "2",
                                    "position": "R8",
                                    "parentNodeCode": "1034767881574944778",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944780",
                                    "index": 2,
                                    "serialNo": "1.17.3"
                                }
                            ],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "电阻151",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "151",
                            "seqNo": 17,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944778",
                            "index": 16,
                            "serialNo": "1.17"
                        },
                        {
                            "bomNodeCode": "1034767881574944777",
                            "bomName": "功率电感151",
                            "tempNodeId": 3667,
                            "matGroup": "151",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "功率电感151",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "151",
                            "seqNo": 18,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944777",
                            "index": 17,
                            "serialNo": "1.18"
                        },
                        {
                            "bomNodeCode": "1034767881574944776",
                            "bomName": "其他151",
                            "tempNodeId": 3668,
                            "matGroup": "151",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "其他151",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "151",
                            "seqNo": 19,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944776",
                            "index": 18,
                            "serialNo": "1.19"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1034767881574944775",
                            "bomName": "MIC192",
                            "isArchive": 0,
                            "matCode": "19201021",
                            "baseQty": "1000",
                            "note": "MIC-C,2.2K,-42dB±3dB,直径4*1.55,带防尘网,Goer",
                            "tempNodeId": 3669,
                            "matGroup": "192",
                            "matAttr": "标准",
                            "bomUseage": "2",
                            "position": "U2",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "MIC192",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "192",
                            "seqNo": 20,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "matCount": 1,
                            "id": "1034767881574944775",
                            "index": 19,
                            "serialNo": "1.20"
                        },
                        {
                            "bomNodeCode": "1034767881574944771",
                            "bomName": "结构贴片料",
                            "tempNodeId": 3670,
                            "matGroup": "152,153",
                            "childNodes": [
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944773",
                                    "isArchive": 0,
                                    "matCode": "15201166",
                                    "baseQty": "1000",
                                    "note": "板板连接器,T/H=0.7,7.80x1.90x0.7,30PIN,JAE",
                                    "matAttr": "标准",
                                    "bomUseage": "2",
                                    "position": "J1",
                                    "parentNodeCode": "1034767881574944771",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944773",
                                    "index": 0,
                                    "serialNo": "1.21.1"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944774",
                                    "isArchive": 0,
                                    "matCode": "15201023",
                                    "baseQty": "1000",
                                    "note": "USS RF CONN,T/H1.3,2.0x2.0x0.7,ECT",
                                    "matAttr": "标准",
                                    "bomUseage": "2",
                                    "position": "J2",
                                    "parentNodeCode": "1034767881574944771",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944774",
                                    "index": 1,
                                    "serialNo": "1.21.2"
                                },
                                {
                                    "companyId": 100,
                                    "bomNodeCode": "1034767881574944772",
                                    "isArchive": 0,
                                    "matCode": "15301324",
                                    "baseQty": "1000",
                                    "note": "USB,B,T/S-1.3,5.85*9.6*2.45,5PIN",
                                    "matAttr": "标准",
                                    "bomUseage": "2",
                                    "position": "J3",
                                    "parentNodeCode": "1034767881574944771",
                                    "sapLevel": 1,
                                    "dealDelFlag": False,
                                    "matCount": 1,
                                    "id": "1034767881574944772",
                                    "index": 2,
                                    "serialNo": "1.21.3"
                                }
                            ],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "结构贴片料",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "152,153",
                            "seqNo": 21,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "id": "1034767881574944771",
                            "index": 20,
                            "serialNo": "1.21"
                        },
                        {
                            "companyId": 100,
                            "bomNodeCode": "1034767881574944770",
                            "bomName": "弹片/屏蔽罩",
                            "isArchive": 0,
                            "matCode": "15401620",
                            "baseQty": "4000",
                            "note": "Antenna Spring,WH=0.6,1.8*1*1.0",
                            "tempNodeId": 3671,
                            "matGroup": "154",
                            "matAttr": "标准",
                            "bomUseage": "2",
                            "position": "ANT1,ANT2,ANT3,ANT4",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "弹片/屏蔽罩",
                            "nodeClass": "actual",
                            "sapLevel": 1,
                            "templateMatGroup": "154",
                            "seqNo": 22,
                            "dealDelFlag": False,
                            "businessRole": "baseBand",
                            "matCount": 4,
                            "id": "1034767881574944770",
                            "index": 21,
                            "serialNo": "1.22"
                        },
                        {
                            "bomNodeCode": "1034767881574944769",
                            "bomName": "其他",
                            "isArchive": 0,
                            "matCode": "12105695",
                            "baseQty": "1000",
                            "note": "贴片副板_H850A_A1_TEST_PCBA_V3.0_自制",
                            "tempNodeId": -999,
                            "matAttr": "可选",
                            "childNodes": [],
                            "parentNodeCode": "1034767881574944768",
                            "nodeName": "其他",
                            "nodeClass": "other",
                            "seqNo": 999999999,
                            "dealDelFlag": False,
                            "operation": "add",
                            "matCount": 1,
                            "id": "1034767881574944769",
                            "index": 22,
                            "serialNo": "1.23"
                        }
                    ],
                    "parentNodeCode": "0",
                    "nodeName": "PCBA",
                    "nodeClass": "actual",
                    "sapLevel": 0,
                    "templateMatGroup": "121,123,129,131,144",
                    "seqNo": 1,
                    "dealDelFlag": False,
                    "businessRole": "rf,baseBand,nps,structure,mpm,other",
                    "matCount": 1,
                    "id": "1034767881574944768",
                    "index": 0,
                    "serialNo": 1
                }
            ],
            "virtualChipList": [],
            "approvers": {
                "bisReviewApprovers": [
                    {
                        "role": "pm",
                        "userNo": ""
                    },
                    {
                        "role": "structure",
                        "userNo": "18645960"
                    },
                    {
                        "role": "nps",
                        "userNo": "18645960"
                    },
                    {
                        "role": "rf",
                        "userNo": "18645960"
                    },
                    {
                        "role": "other",
                        "userNo": ""
                    },
                    {
                        "role": "check",
                        "userNo": "18645960"
                    }
                ],
                "bisSupplyApprovers": [
                    {
                        "role": "mpm",
                        "userNo": "18645960"
                    }
                ]
            },
            "uploadList": [],
            "submitType": "submit"
        }
        search_data = {
            "param": {
                "title": "",
                "flowNo": "",
                "bomCode": "",
                "produceClass": "",
                "model": "",
                "brandCode": "",
                "bomVer": "",
                "statusCode": "",
                "synStatus": "",
                "createdBy": "",
                "createdTimeFrom": "",
                "createdTimeTo": "",
                "bomType": "pcba"
            },
            "current": 1,
            "size": 10
        }
        add_response = self.Request_PCBA_Add(add_data, headers)
        flowId = add_response['data']
        search_response = self.Request_Bom_Search(search_data, headers)
        search_response_data = search_response['data']['data']
        for i in search_response_data:
            if i['flowId'] == flowId:
                logging.info('接口返回数据：FlowNo：{}，InstanceID：{}，FlowID：{}'.format(i['flowNo'], i['instanceId'], flowId))
                logging.info('流程结束：外研BOM协作新增接口')
                return i['flowNo'], i['instanceId'], flowId

    def Oneworks_queryPCBAInfo(self, flowId, headers):
        """
        TBM oneworks 查询流程历史
        @param flowId:oneworks  流程实例id
        @param headers:接口头部
        """
        logging.info('发起请求：oneworks查询流程历史接口')
        logging.info(f'接口请求地址为：http://pfgatewayidct.transsion.com:9088/service-bom-archive/bom-arc/pcba/queryBomInfoByFlowId?flowId={flowId}')
        history_response = requests.get(
            url=f'http://pfgatewayidct.transsion.com:9088/service-bom-archive/bom-arc/pcba/queryBomInfoByFlowId?flowId={flowId}',
            headers=headers)
        response_dicts = history_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        logging.info('请求结束：oneworks查询流程历史接口')
        return response_dicts

    def Request_PCBA_Factory(self, data, headers):
        """
        TBM 单机头BOM协作 oneworks 补充工厂
        @param data: 接口body
        @param headers:接口头部
        """
        logging.info('发起请求：PCBABOM协作补充工厂接口')
        return self.api_request('PCBABOM协作补充工厂接口', data, headers)

    @allure.step("PCBABOM协作-补充工厂审批通过接口")
    def API_PCBA_Factory(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：PCBABOM协作-补充工厂审批通过流程')
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        BomPCBAInfo = self.Oneworks_queryPCBAInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "refFactoryList": [
                {
                    "note": BomPCBAInfo['data']['bomTreeVOList'][0]['note'],
                    "matCode": BomPCBAInfo['data']['bomTreeVOList'][0]['matCode'],
                    "isOversea": None,
                    "homePackagingFactory": "/",
                    "homeChipFactory": "1001",
                    "overseasPackagingFactory": "/",
                    "overseasChipFactory": "1001",
                    "applyScope": "pcbaBom",
                    "bomNodeCode": None,
                    "statusCode": "trial",
                    "bomNo": "1",
                    "factory": None,
                    "applyScopeList": None,
                    "childNodes": None,
                    "existFactory": False,
                    "statusCodeLabel": "试产",
                    "deleteValidate": False
                }
            ],
            "produceClass": BomPCBAInfo['data']['bomArchive']['produceClass']
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_PCBA_Factory(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：PCBABOM协作-补充工厂审批通过流程')

    def Request_PCBA_structure(self, data, headers):
        """
        TBM PCBABOM协作 oneworks 基带工程师审批接口
        @param data: 接口body
        @param headers:接口头部
        """
        logging.info('发起请求：PCBABOM协作基带工程师审批接口')
        return self.api_request('PCBABOM协作基带工程师审批接口', data, headers)

    def Oneworks_PCBA_queryInfo(self, flowId, headers):
        """
        TBM oneworks 查询流程历史
        @param flowId:oneworks  流程实例id
        @param headers:接口头部
        """
        logging.info('发起请求：oneworks查询流程历史接口')
        logging.info(f'接口请求地址为：http://pfgatewayidct.transsion.com:9088/service-bom-archive/bom-arc/pcba/queryBomInfoByFlowId?flowId={flowId}')
        history_response = requests.get(
            url=f'http://pfgatewayidct.transsion.com:9088/service-bom-archive/bom-arc/pcba/queryBomInfoByFlowId?flowId={flowId}',
            headers=headers)
        response_dicts = history_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        logging.info('请求结束：oneworks查询流程历史接口')
        return response_dicts

    @allure.step("PCBABOM协作-基带工程师审批通过接口")
    def API_PCBA_Structure(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：PCBABOM协作-基带工程师审批通过流程')
        self.API_PCBA_Factory(flowNo, instanceid, flowid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        PCBAInfo = self.Oneworks_PCBA_queryInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "baseBandReview",
            "bomArchive": PCBAInfo['data']['bomArchive'],
            "approvers": {
                "bisReviewApprovers": [
                    {
                        "role": "pm",
                        "userNo": ""
                    },
                    {
                        "role": "structure",
                        "userNo": "18645960"
                    },
                    {
                        "role": "nps",
                        "userNo": "18645960"
                    },
                    {
                        "role": "rf",
                        "userNo": ""
                    },
                    {
                        "role": "other",
                        "userNo": ""
                    },
                    {
                        "role": "check",
                        "userNo": "18645960"
                    }
                ],
                "bisSupplyApprovers": []
            },
            "bomTreeVOList": PCBAInfo['data']['bomTreeVOList'],
            "refFactoryList": PCBAInfo['data']['refFactoryList'],
            "bomDeriveList": [],
            "copyRuleList": [],
            "otherDeriveList": [],
            "uploadList": [],
            "bomImportKeyDeviceList": [],
            "purchaseList": None,
            "role": "mpm",
            "bomDeriveTreeVOList": None,
            "virtualChipList": [],
            "diffCollectList": [],
            "bomVersionList": PCBAInfo['data']['bomVersionList'],
            "produceClass": "pcba"
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_PCBA_structure(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：PCBABOM协作-基带工程师审批通过流程')

    @allure.step("PCBABOM协作-基带工程师审批通过接口")
    def API_Derived_PCBA_Structure(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：PCBABOM协作-基带工程师审批通过流程')
        self.API_PCBA_Factory(flowNo, instanceid, flowid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        PCBAInfo = self.Oneworks_PCBA_queryInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "baseBandReview",
            "bomArchive": PCBAInfo['data']['bomArchive'],
            "approvers": {
                "bisReviewApprovers": [
                    {
                        "role": "pm",
                        "userNo": ""
                    },
                    {
                        "role": "structure",
                        "userNo": "18645960"
                    },
                    {
                        "role": "nps",
                        "userNo": "18645960"
                    },
                    {
                        "role": "rf",
                        "userNo": ""
                    },
                    {
                        "role": "other",
                        "userNo": ""
                    },
                    {
                        "role": "check",
                        "userNo": "18645960"
                    }
                ],
                "bisSupplyApprovers": []
            },
            "bomTreeVOList": PCBAInfo['data']['bomTreeVOList'],
            "refFactoryList": PCBAInfo['data']['refFactoryList'],
            "bomDeriveList": PCBAInfo['data']['bomDeriveList'],
            "copyRuleList": [],
            "otherDeriveList": PCBAInfo['data']['otherDeriveList'],
            "uploadList": [],
            "bomImportKeyDeviceList": [],
            "purchaseList": None,
            "role": PCBAInfo['data']['role'],
            "bomDeriveTreeVOList": None,
            "virtualChipList": [],
            "diffCollectList": [],
            "bomVersionList": PCBAInfo['data']['bomVersionList'],
            "produceClass": PCBAInfo['data']['bomArchive']['produceClass']
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_PCBA_structure(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：PCBABOM协作-基带工程师审批通过流程')

    def Request_PCBA_Approve(self, data, headers):
        """
        TBM PCBABOM协作 oneworks 采购&业务审核接口
        @param data: 接口body
        @param headers:接口头部
        """
        logging.info('发起请求：PCBABOM协作采购&业务审核接口')
        return self.api_request('PCBABOM协作采购&业务审核接口', data, headers)

    @allure.step("PCBABOM协作-采购审核通过接口")
    def API_PCBA_Purchase(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：PCBABOM协作-采购审核通过流程')
        self.API_PCBA_Structure(flowNo, instanceid, flowid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        PCBAInfo = self.Oneworks_PCBA_queryInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "nps",
            "bomArchive": PCBAInfo['data']['bomArchive'],
            "approvers": PCBAInfo['data']['approvers'],
            "bomTreeVOList": PCBAInfo['data']['bomTreeVOList'],
            "refFactoryList": PCBAInfo['data']['refFactoryList'],
            "bomDeriveList": [],
            "copyRuleList": [],
            "otherDeriveList": [],
            "uploadList": [],
            "bomImportKeyDeviceList": [],
            "purchaseList": None,
            "role": "mpm,structure,nps,check",
            "bomDeriveTreeVOList": None,
            "virtualChipList": [],
            "diffCollectList": [],
            "bomVersionList": PCBAInfo['data']['bomVersionList']
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_PCBA_Approve(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：PCBABOM协作-采购审核通过流程')

    @allure.step("PCBABOM协作-采购审核通过接口")
    def API_Derived_PCBA_Purchase(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：PCBABOM协作-采购审核通过流程')
        self.API_Derived_PCBA_Structure(flowNo, instanceid, flowid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        PCBAInfo = self.Oneworks_PCBA_queryInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "nps",
            "bomArchive": PCBAInfo['data']['bomArchive'],
            "approvers": PCBAInfo['data']['approvers'],
            "bomTreeVOList": PCBAInfo['data']['bomTreeVOList'],
            "refFactoryList": PCBAInfo['data']['refFactoryList'],
            "bomDeriveList": PCBAInfo['data']['bomDeriveList'],
            "copyRuleList": [],
            "otherDeriveList": PCBAInfo['data']['otherDeriveList'],
            "uploadList": [],
            "bomImportKeyDeviceList": [],
            "purchaseList": None,
            "role": PCBAInfo['data']['role'],
            "bomDeriveTreeVOList": None,
            "virtualChipList": [],
            "diffCollectList": [],
            "bomVersionList": PCBAInfo['data']['bomVersionList']
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_PCBA_Approve(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：PCBABOM协作-采购审核通过流程')

    @allure.step("PCBABOM协作-业务审核通过接口")
    def API_PCBA_Business(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：PCBABOM协作-业务审核通过流程')
        self.API_PCBA_Purchase(flowNo, instanceid, flowid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        PCBAInfo = self.Oneworks_PCBA_queryInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "bisReview",
            "bomArchive": PCBAInfo['data']['bomArchive'],
            "approvers": PCBAInfo['data']['approvers'],
            "bomTreeVOList": PCBAInfo['data']['bomTreeVOList'],
            "refFactoryList": PCBAInfo['data']['refFactoryList'],
            "bomDeriveList": [],
            "copyRuleList": [],
            "otherDeriveList": [],
            "uploadList": [
                {
                    "id": None,
                    "mime": "image/png",
                    "flowBid": None,
                    "name": "检查结果.PNG",
                    "size": "0",
                    "uploadTime": None,
                    "uploader": None,
                    "url": "https://oss-sz-test-01.oss-cn-shenzhen.aliyuncs.com/plm-bom/bom/doc/20220919/202209191151-1021388177098805248/%E6%A3%80%E6%9F%A5%E7%BB%93%E6%9E%9C.PNG",
                    "systemName": None
                }
            ],
            "bomImportKeyDeviceList": [],
            "purchaseList": None,
            "role": "mpm,structure,nps,check",
            "bomDeriveTreeVOList": None,
            "virtualChipList": [],
            "diffCollectList": [],
            "bomVersionList": PCBAInfo['data']['bomVersionList'],
            "recordReqVO": {
                "checkRole": "mpm",
                "listBid": "922546228208734208",
                "listName": "32213",
                "records": [
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "922546228284231680",
                        "ruleName": "弱方法"
                    },
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "922546228284231681",
                        "ruleName": "测试1"
                    }
                ],
                "bomLevel": "pcba",
                "checker": "18645960",
                "flowId": flowid
            }
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_PCBA_Approve(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：PCBABOM协作-业务审核通过流程')

    @allure.step("PCBABOM协作-业务审核通过接口")
    def API_Derived_PCBA_Business(self, flowNo, instanceid, flowid):
        logging.info('发起流程接口：PCBABOM协作-业务审核通过流程')
        self.API_Derived_PCBA_Purchase(flowNo, instanceid, flowid)
        Search_Result = self.API_Mytodu_Search(flowNo)
        headers = {'Content-Type': 'application/json', 'Authorization': Search_Result[1]}
        PCBAInfo = self.Oneworks_PCBA_queryInfo(flowid, headers)
        approve_data = {
            "flowId": flowid,
            "flowNodeName": "bisReview",
            "bomArchive": PCBAInfo['data']['bomArchive'],
            "approvers": PCBAInfo['data']['approvers'],
            "bomTreeVOList": PCBAInfo['data']['bomTreeVOList'],
            "refFactoryList": PCBAInfo['data']['refFactoryList'],
            "bomDeriveList": PCBAInfo['data']['bomDeriveList'],
            "copyRuleList": [],
            "otherDeriveList": PCBAInfo['data']['otherDeriveList'],
            "uploadList": [
                {
                    "id": None,
                    "mime": "image/png",
                    "flowBid": None,
                    "name": "检查结果.PNG",
                    "size": "0",
                    "uploadTime": None,
                    "uploader": None,
                    "url": "https://oss-sz-test-01.oss-cn-shenzhen.aliyuncs.com/plm-bom/bom/doc/20220919/202209191151-1021388177098805248/%E6%A3%80%E6%9F%A5%E7%BB%93%E6%9E%9C.PNG",
                    "systemName": None
                }
            ],
            "bomImportKeyDeviceList": [],
            "purchaseList": None,
            "role": PCBAInfo['data']['role'],
            "bomDeriveTreeVOList": None,
            "virtualChipList": [],
            "diffCollectList": [],
            "bomVersionList": PCBAInfo['data']['bomVersionList'],
            "recordReqVO": {
                "checkRole": "check",
                "listBid": "1014225961337622528",
                "listName": "检查人",
                "records": [
                    {
                        "checkResult": 1,
                        "remark": "",
                        "ruleBid": "1014225961476034560",
                        "ruleName": "测试1"
                    }
                ],
                "bomLevel": "pcba",
                "checker": "18645960",
                "flowId": flowid
            }
        }
        complete_data = {"instanceId": instanceid, "taskId": Search_Result[0], "appId": 0, "approveResult": 1, "comment": ""}
        self.Request_PCBA_Approve(approve_data, headers)
        self.Request_Oneworks_Complete(complete_data, headers)
        logging.info('流程接口结束：PCBABOM协作-业务审核通过流程')

    def Request_TBM_ServiceDictList(self, data, headers):
        """
        TBM 字典服务接口
        @param data: 接口body
        @param headers:接口头部
        """
        logging.info('发起请求：TBM字典服务列表接口')
        return self.api_request('TBM字典服务列表接口', data, headers)

    @allure.step("TBM字典服务列表接口")
    def API_TBM_ServiceDictList(self):
        logging.info('发起流程接口：TBM字典服务接口')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        search_data = {
            "param": {
                "refAppCode": "TBM"
            },
            "current": 1,
            "size": 10
        }
        return self.Request_TBM_ServiceDictList(search_data, headers)

    @allure.step("TBM字典服务数据接口")
    def API_TBM_ServiceDictData(self, codes, appCode='tbm', status='enable'):
        logging.info('发起流程接口：TBM字典服务数据接口')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        logging.info(f'接口请求地址为：http://pfgatewayidct.transsion.com:9088/service-base-dictionary/base/dictionaries?codes={codes}&appCode={appCode}&status={status}')
        history_response = requests.get(
            url=f'http://pfgatewayidct.transsion.com:9088/service-base-dictionary/base/dictionaries?codes={codes}&appCode={appCode}&status={status}',
            headers=headers)
        response_dicts = history_response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        logging.info('请求结束：TBM字典服务数据接口')
        return response_dicts

    @allure.step("员工查询接口")
    def API_queryDeptAndEmployee(self, code):
        """
        @param code: 工号
        """
        logging.info('发起请求：员工查询接口')
        token = self.tbm_login()
        headers = {'Content-Type': 'application/json', 'Authorization': token}
        response = requests.post(
            url=eval(ini._get('API', '员工查询接口')),
            data=code.encode('utf-8'), headers=headers).json()
        logging.info('获取审批人：%s', response)
        return response
if __name__ == '__main__':
    a = APIRequest()
