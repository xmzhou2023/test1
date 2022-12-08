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
    def __init__(self,uasername=18645960):
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
        return probid,objbid


    def Api_project_field(self,proname):
        """
        项目管理基本信息显示字段获取
        """
        bid=self.Api_project_bid(proname)
        logging.info('项目管理基本信息显示字段获取')
        data = {"domainBid":bid[0],"objBid":bid[1]}
        headers = {'Content-Type': 'application/json', 'Authorization': self.Api_login()}
        response = self.api_request('项目管理基本信息字段获取', data, headers)
        node = response['body']['data']
        print(node)
        field_properties = []
        for i in node:
            pro = '字段名', '类型', '是否可读', '是否必填', '是否展示','文本类型'
            properties = i.get('displayName'), i.get("type"), i.get("readonly"), i.get("required"), i.get("visible"), i.get("dataType")
            res = dict(zip(pro, properties))
            field_properties.append(res)
        return field_properties



if __name__ == '__main__':
    Api=APIRequest(18645960)
    # ApplyList=Api.Api_applyList(20220810085734677324)
    # Api.Api_queryDeptAndEmployee(20220810085734677324)
    print(Api.Api_project_bid("开模流程测试"))
    print(Api.Api_project_field("IPM自动化2022-12-0813:39:12"))
