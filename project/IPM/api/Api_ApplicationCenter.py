
'''应用中心'''
from project.IPM.api.APIRequest import *
from libs.common.time_ui import *
from public.data.unified_login.unified import *

def get_applicationcenter_DCP_agree(env_name,proname,task_name):
    '''
    应用中心_DCP看板_同意预约
    param templname:项目模板名称
    param projectname:项目名称
    '''
    Api=APIRequest(env_name)
    probid=Api.Api_project_Scheduled_action(proname,task_name)
    print(probid[2],probid[0])
    data = {"taskId":probid[0],"objInsBid":probid[2],"templateType":"2"}
    headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()[0],'p-rtoken': Api.Api_login()[1]}
    response = Api.api_request('应用中心_DCP看板_同意预约', data, headers)
    bid = response['body']['message']
    if bid == '请求成功':
        logging.info('当前同意预约调用结果为{}'.format(bid))
    else:
        logging.info('当前同意预约调用结果为{}'.format(bid))
        raise ValueError('当前同意预约调用结果为{}'.format(bid))

def get_applicationcenter_DCP_agree_sendMail(env_name,proname,task_name):
    '''
    应用中心_DCP看板_同意预约_发送邮件
    param templname:项目模板名称
    param projectname:项目名称
    '''
    Api=APIRequest(env_name)
    probid=Api.Api_project_Scheduled_action(proname,task_name)
    data = {"appointmentDate":None,"taskId":probid[0],"objInsBid":probid[2],"title":F"【预约成功】({proname})计划DCP1月12日IPMT上会申请 ","content":F"Hi ，已收到({proname})计划DCP1月12日IPMT上会申请，请于1月5日18:00前提交上会资料，office审核无误报备IPMT后将通知你启动干系人沟通。","mailReceivers":["18646295"],"copyReceivers":[]}
    headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()[0],'p-rtoken': Api.Api_login()[1]}
    response = Api.api_request('应用中心_DCP看板_同意预约_发送邮件', data, headers)
    bid = response['body']['message']
    print(bid)
    if bid == '请求成功':
        logging.info('当前同意预约调用结果为{}'.format(bid))
    else:
        logging.info('当前同意预约调用结果为{}'.format(bid))
        raise ValueError('当前同意预约调用结果为{}'.format(bid))
def get_applicationcenter_DCP_agree_approveAppointment(env_name,proname,task_name):
    '''
    应用中心_DCP看板_同意预约_审批
    param templname:项目模板名称
    param projectname:项目名称
    '''
    Api=APIRequest(env_name)
    probid=Api.Api_project_Scheduled_action(proname,task_name)
    data = {"btnType":1,"objInsBid":probid[2],"taskIds":[probid[0]]}
    headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()[0],'p-rtoken': Api.Api_login()[1]}
    response = Api.api_request('应用中心_DCP看板_同意预约_预约成功', data, headers)
    bid = response['body']['message']
    print(bid)
    if bid == '请求成功':
        logging.info('当前同意预约调用结果为{}'.format(bid))
    else:
        logging.info('当前同意预约调用结果为{}'.format(bid))
        raise ValueError('当前同意预约调用结果为{}'.format(bid))

if __name__ == '__main__':
    #env_name为全局变量，获取当前运行环境的
    # print(get_applicationcenter_DCP_agree(env_name,"IPM自动化测试2022-12-2316:56:38","任务名称2022-12-2316:56:38"))
    # print(get_applicationcenter_DCP_agree_sendMail(env_name,"IPM自动化测试2022-12-2216:24:36","任务名称2022-12-2216:24:36"))
    print(get_applicationcenter_DCP_agree_approveAppointment(env_name,"IPM自动化测试2022-12-2216:24:36","任务名称2022-12-2216:24:36"))