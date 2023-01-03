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
pro_env = 'uat' # 需要手动配置测试环境
ini = ReadConfig(pro_name, pro_env)

class APIRequest:
    def __init__(self,uasername=18646295):
        self.username=uasername

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
        elif method == 'get':
            response = requests.get(url=eval(ini._get('API', request)),
                                       headers=headers)


        response_dicts = dict()
        response_dicts['body'] = response.json()
        logging.info('接口响应内容为：%s', response_dicts)
        return response_dicts

    def Api_login(self):
        """
        登录接口
        return token
        """

        logging.info('发起请求：登录接口')
        data = {
            "username":f"{self.username}",
            "pwd":"eExpbHk2eA=="
            }
        headers = {'Content-Type': 'application/json'}
        response = self.api_request('登录接口', data, headers)
        token = response['body']['data']['token']
        logging.info('获取token：%s', token)
        return token



    def Api_applyList(self,flow_id):
        """
        获取单据的节点审批角色和审批节点
        return token
        """
        logging.info('发起请求：流程节点获取审批角色/节点')
        data = {"size":1,"param":{"code": f"{flow_id}"}}
        headers = {'Content-Type': 'application/json', 'Authorization': self.Api_login()}
        response = self.api_request('流程节点获取审批角色', data, headers)
        personnel = response['body']['data']["list"][0]["assignee"]
        s_personnel=tuple(personnel.split(","))
        logging.info('获取审批人：%s', s_personnel)
        node = response['body']['data']["list"][0]["taskName"]
        s_node=tuple(node.split(","))
        logging.info('获取审批节点：%s', s_node)
        return s_personnel,s_node


    def Api_queryDeptAndEmployee(self,flow_id):
        """
        审批人获取
        return applyList
        """
        applyList=self.Api_applyList(flow_id)[0]
        logging.info('发起请求：工号查询')
        list_queryDeptAndEmployee=[]
        for data in applyList:
            headers = {'Content-Type': 'application/json', 'Authorization': self.Api_login()}
            response =  requests.post(url='https://pfgateway.transsion.com:9199/service-cp-uc-extend/cp-uc-extend/Department/queryDeptAndEmployee',
                      data=data.encode('utf-8'), headers=headers).json()['data'][0]['employeeNo']
            result = response
            logging.info('工号查询：%s', result)
            list_queryDeptAndEmployee.append(result)
        print(list_queryDeptAndEmployee)
        return list_queryDeptAndEmployee

    def Api_project_bid(self,proname):
        """
        获取项目管理项目的项目ID和对象ID
        """
        data = {"size":100,"current":1,"param":{"name":f"{proname}","typeCode":"","stateCode":["preparation","underway"]}}
        headers = {'Content-Type': 'application/json', 'Authorization': self.Api_login()}
        response = self.api_request('项目管理获取项目模板的BID', data, headers)
        bid = response['body']['data']['data'][0]
        probid=bid.get("permissionBid")
        objbid=bid.get("model_bid")
        templ_bid=bid.get("templ_bid")
        return probid,objbid,templ_bid





    def Api_project_getPlanTaskTree(self,proname):
        """
        项目管理基本信息显示字段获取
        """
        bid=self.Api_project_bid(proname)
        logging.info('项目管理基本信息显示字段获取')
        data = {"projBid":bid[0]}
        headers = {'Content-Type': 'application/json', 'Authorization': self.Api_login()}
        response = self.api_request('项目管理_计划_任务', data, headers)
        node = response['body']['data']

        field_propertie01 = []
        field_propertie02 = []
        field_propertie03 = []
        field_propertie04 = []
        for i in node:
            children=i.get("children")
            pro = '字段名', 'namebid', "children"
            if i.get("children") !=None:
                for j in children:
                    prop_02 = j.get('name'), j.get("bid")
                    res02 = dict(zip(pro, prop_02))
                    field_propertie02.append(res02)
                    if i.get("children") != None:
                        for j in children:
                            prop_03 = j.get('name'), j.get("bid")
                            res03 = dict(zip(pro, prop_03))
                            field_propertie03.append(res03)
                            if i.get("children") != None:
                                for j in children:
                                    prop_04 = j.get('name'), j.get("bid")
                                    res04 = dict(zip(pro, prop_04))
                                    field_propertie04.append(res04)
            pro_01 = i.get('name'), i.get("bid")
            res01 = dict(zip(pro, pro_01))
            field_propertie01.append(res01)
        listtask=field_propertie01+field_propertie02+field_propertie03+field_propertie04
        return listtask


            #
            # return field_properties
    def Api_tasktree(self,proname,task_name):
        """
        :param proname: 项目名称
        :param task_name: 任务名 如：概念阶段，TR1，计划阶段，开发阶段
        """
        tasksbid= self.Api_project_getPlanTaskTree(proname)
        for i in tasksbid:
            if i.get("字段名")==task_name:
                return i.get("namebid")
            else:
                logging.info("{}:不存在，请传入正确的任务名称".format(task_name))


    def Api_project_Scheduled_action(self,proname,task_name):
        """
        项目管理基本信息显示字段获取
        """
        bid=self.Api_project_bid(proname)
        tasksbid= self.Api_tasktree(proname,task_name)
        logging.info('项目管理基本信息显示字段获取')
        data = {"actionMethod":"get","targetModel":"task","sourceModel":"","targetModelBid":"","sourceModelBid":"","targetDataMap":
            {"bid":tasksbid,"projBid":bid[0]},"targetModelAttrList":[],"sourceRefTargetDataMap":{},"sourceRefTargetModelAttrList":[]}
        headers = {'Content-Type': 'application/json', 'Authorization': self.Api_login()}
        response = self.api_request('项目管理_计划_任务基本信息字段获取', data, headers)
        node = response['body']['data']
        taskbid=node.get("bid")
        objbid=node.get("objBid")
        projbid=node.get("projBid")
        return taskbid,objbid,projbid



    def Api_project_field(self,proname,domainbid=None):
        """
        项目管理基本信息显示字段获取
        """
        if domainbid==None:
            bid=self.Api_project_bid(proname)
            logging.info('项目管理基本信息显示字段获取')
            data = {"domainBid":bid[0],"objBid":bid[1]}
            headers = {'Content-Type': 'application/json', 'Authorization': self.Api_login()}
            response = self.api_request('项目管理基本信息字段获取', data, headers)
            node = response['body']['data']
            field_properties = []
            for i in node:
                pro = '字段名', '类型', '是否可读', '是否必填', '是否展示','文本类型'
                properties = i.get('displayName'), i.get("type"), i.get("readonly"), i.get("required"), i.get("visible"), i.get("dataType")
                res = dict(zip(pro, properties))
                field_properties.append(res)
            return field_properties
        else:
            bid=self.Api_project_bid(proname)
            logging.info('项目管理基本信息显示字段获取')
            data = {"domainBid":domainbid,"objBid":bid[1]}
            headers = {'Content-Type': 'application/json', 'Authorization': self.Api_login()}
            response = self.api_request('项目管理基本信息字段获取', data, headers)
            node = response['body']['data']
            field_properties = []
            for i in node:
                pro = '字段名', '类型', '是否可读', '是否必填', '是否展示','文本类型'
                properties = i.get('displayName'), i.get("type"), i.get("readonly"), i.get("required"), i.get("visible"), i.get("dataType")
                res = dict(zip(pro, properties))
                field_properties.append(res)
            return field_properties

    def Api_project_task(self,proname,task_name,objectname=None):
        """
        项目管理计划任务基本字段信息获取—对象属性及约束字段获取
        :param proname: 项目名称
        :param task_name: 任务名 如：概念阶段，TR1，计划阶段，开发阶段
        """
        if objectname ==None:
            bid=self.Api_project_Scheduled_action(proname,task_name)
            logging.info('项目管理基本信息显示字段获取')
            data = {"objBid":bid[1],"domainBid":bid[2],"modelBid":"task","modelInsBid":bid[0],"tag":"not_started"}
            headers = {'Content-Type': 'application/json', 'Authorization': self.Api_login()}
            response = self.api_request('项目管理_计划_任务字段属性获取', data, headers)
            node = response['body']['data']
            print(node)
            field_properties = []
            for i in node:
                pro = '字段名', '类型', '是否可读', '是否必填', '是否展示','文本类型'
                properties = i.get('displayName'), i.get("type"), i.get("readonly"), i.get("required"), i.get("visible"), i.get("dataType")
                res = dict(zip(pro, properties))
                field_properties.append(res)
            return field_properties
        else:
            bid = self.Api_project_bid(proname)
            object_bid = self.Api_object_bid()
            logging.info('项目管理基本信息显示字段获取')
            for i in object_bid:
                if i.get('对象名称') == '问题':
                    data = {"objBid": i.get('对象BID'), "domainBid": bid[0], "tag": ""}
                    headers = {'Content-Type': 'application/json', 'Authorization': self.Api_login()}
                    response = self.api_request('项目管理_计划_任务字段属性获取', data, headers)
                    node = response['body']['data']
                    field_properties = []
                    for i in node:
                        pro = '字段名', '类型', '是否可读', '是否必填', '是否展示', '文本类型'
                        properties = i.get('displayName'), i.get("type"), i.get("readonly"), i.get("required"), i.get(
                            "visible"), i.get("dataType")
                        res = dict(zip(pro, properties))
                        field_properties.append(res)
                    print(field_properties)
                    return field_properties


    def Api_templ_bid(self,objtemplname):
        """
        系统管理-项目模板BID获取
        """
        data = {"count":True,"param":{"name":objtemplname},"name":"IT","current":1,"size":20}
        headers = {'Content-Type': 'application/json', 'Authorization': self.Api_login()}
        response = self.api_request('系统管理_项目模板_BID获取', data, headers)
        bid = response['body']['data']['data'][0]
        probid=bid.get("bid")
        return probid

    def Api_object_bid(self):
        """
        系统管理-对象BID获取
        """

        headers = {'Content-Type': 'application/json', 'Authorization': self.Api_login()}
        response = self.api_request('系统管理_对象_对象BID获取', headers=headers,method='get')
        object_bid=[]
        bid = response['body']['data']
        for i in bid:
            pro = '对象名称', '对象BID',
            properties = i.get('name'), i.get("rootBid")
            res = dict(zip(pro, properties))
            object_bid.append(res)
        return object_bid





if __name__ == '__main__':
    Api=APIRequest()
    # ApplyList=Api.Api_applyList(20220810085734677324)
    # Api.Api_queryDeptAndEmployee(20220810085734677324)
    # print(Api.Api_project_bid("IPM自动化测试2022-12-1517:02:50"))
    print(Api.Api_project_task("IPM自动化测试2022-12-1517:02:50","概念阶段"))
    # print(Api.Api_project_field("5435345"))
    # print(Api.Api_project_getPlanTaskTree("655人TV v"))
    #   任务流程名