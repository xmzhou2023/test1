import logging

from project.IPM.api.APIRequest import *
from libs.common.time_ui import *
from public.data.unified_login.unified import *
pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

usernum=account[15]['usernum']
username=account[15]['username']
email=account[15]['email']


now_times = strftime('%Y-%m-%d%H:%M:%S')
# ApplyList=Api.Api_applyList(20220810085734677324)
# Api.Api_queryDeptAndEmployee(20220810085734677324)
Api = APIRequest()
def get_project_create(templname,projectname):
    '''
    项目创建

    '''

    field_att = Api.Api_templ_bid(templname)
    data = {"param":{"templBid":field_att,"name":projectname}}
    headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()}
    response = Api.api_request('项目管理_创建项目', data, headers)
    bid = response['body']['data']
    probid = bid.get("permission_bid")
    return probid

def get_project_Team_member_delete(objInsBid,roleBid,usernum_pro,bid,username_pro):
    '''
    项目管理_团队_成员删除
    param objInsBid:项目BID
    param roleBid:角色名称
    param usernum_pro:工号
    param bid:角色BID（由get_project_Team_member_find接口返回）
    param username_pro:姓名
    '''
    data ={"objInsBid":objInsBid,"roleBid":roleBid,"jobNumber":usernum_pro,"bid":bid,"name":username_pro,"type":"member"}
    headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()}
    response = Api.api_request('项目管理_团队_角色成员删除', data, headers)
    bid = response['body']['message']
    if bid == '请求成功':
        logging.info('当前人员删除结果为{}'.format(bid))
    else:
        logging.info('当前人员删除结果为{}'.format(bid))



def get_project_Team_member_find(projectname,rolename):
    '''
    项目管理_团队_成员查询
    param probid:项目BID
    param rolename:角色
    '''
    probid=Api.Api_project_bid(projectname)
    data = {"objInsBid":probid[0],"roleBid":rolename,"isQuerySonRole":False}
    headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()}
    response = Api.api_request('项目管理_团队_角色成员查询', data, headers)
    value = response['body']['data']
    for id in value:
        if id != '':
            bid=id.get('bid')
            jobNumber=id.get('jobNumber')
            objInsBid=id.get('objInsBid')
            name=id.get('name')
            roleBid=id.get('roleBid')
            get_project_Team_member_delete(objInsBid,roleBid,jobNumber,bid,name)
        else:
            print('为空放弃吧')


def get_project_Team_member_add(templname,projectname,*rolename):
    '''
    项目管理_团队_成员新增
    param templname:项目模板名称
    param projectname:项目名称
    '''
    probid=get_project_create(templname,projectname)
    for role in rolename:
        get_project_Team_member_find(projectname,role)
        if role == 'PQA':

            data = [{"employeeName":username,"type":"member","employeeNo":usernum,"accountType":"01","route":True,"jobNumber":usernum,"objInsBid":probid,"roleBid":role}]
            headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()}
            response = Api.api_request('项目管理_团队_成员新增', data, headers)
            bid = response['body']['message']
            if bid == '请求成功':
                logging.info('当前人员状态添加结果为{}'.format(bid))
            else:
                logging.info('当前人员状态添加结果为{}'.format(bid))
                raise ValueError('当前人员状态添加结果为{}'.format(bid))
        if role == 'LPDT':
            data = [{"employeeName":username,"type":"member","employeeNo":usernum,"accountType":"01","route":True,"jobNumber":usernum,"objInsBid":probid,"roleBid":role}]
            headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()}
            response = Api.api_request('项目管理_团队_成员新增', data, headers)
            bid = response['body']['message']
            if bid == '请求成功':
                logging.info('当前人员状态添加结果为{}'.format(bid))
            else:
                logging.info('当前人员状态添加结果为{}'.format(bid))
                raise ValueError('当前人员状态添加结果为{}'.format(bid))
        if role == 'HRBP':
            data = [{"employeeName":username,"type":"member","employeeNo":usernum,"accountType":"01","route":True,"jobNumber":usernum,"objInsBid":probid,"roleBid":role}]
            headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()}
            response = Api.api_request('项目管理_团队_成员新增', data, headers)
            bid = response['body']['message']
            if bid == '请求成功':
                logging.info('当前人员状态添加结果为{}'.format(bid))
            else:
                logging.info('当前人员状态添加结果为{}'.format(bid))
                raise ValueError('当前人员状态添加结果为{}'.format(bid))
        if role == 'PMToffice':
            data = [{"employeeName":username,"type":"member","employeeNo":usernum,"accountType":"01","route":True,"jobNumber":usernum,"objInsBid":probid,"roleBid":role}]
            headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()}
            response = Api.api_request('项目管理_团队_成员新增', data, headers)
            bid = response['body']['message']
            if bid == '请求成功':
                logging.info('当前人员状态添加结果为{}'.format(bid))
            else:
                logging.info('当前人员状态添加结果为{}'.format(bid))
                raise ValueError('当前人员状态添加结果为{}'.format(bid))
        if role == 'PMT区域组长': #
            data = [{"employeeName":username,"type":"member","employeeNo":usernum,"accountType":"01","route":True,"jobNumber":usernum,"objInsBid":probid,"roleBid":'PMTQYZZ'}]
            headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()}
            response = Api.api_request('项目管理_团队_成员新增', data, headers)
            bid = response['body']['message']
            if bid == '请求成功':
                logging.info('当前人员状态添加结果为{}'.format(bid))
            else:
                logging.info('当前人员状态添加结果为{}'.format(bid))
                raise ValueError('当前人员状态添加结果为{}'.format(bid))
        if role == 'PMToffice内审': #
            data = [{"employeeName":username,"type":"member","employeeNo":usernum,"accountType":"01","route":True,"jobNumber":usernum,"objInsBid":probid,"roleBid":'PMToffice_IA'}]
            headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()}
            response = Api.api_request('项目管理_团队_成员新增', data, headers)
            bid = response['body']['message']
            if bid == '请求成功':
                logging.info('当前人员状态添加结果为{}'.format(bid))
            else:
                logging.info('当前人员状态添加结果为{}'.format(bid))
                raise ValueError('当前人员状态添加结果为{}'.format(bid))
        else:
            logging.info('{}不在角色范围内，请再get_project_Team_member_add中添加'.format(role))



if __name__ == '__main__':
    # get_project_create('IPD模块化项目模板','测试1+1_{}'.format(now_times))
    # get_project_Team_member_find('IPM自动化测试2023-01-0318:33:16','PMToffice')
    # get_project_Team_member_delete('1059888241785835520', 'PMToffice', '18646295', '1059900121430495232', '陈万红')
    get_project_Team_member_add('IPD模块化项目模板', now_times, 'PQA', 'HRBP', 'PMT区域组长', 'LPDT','PMToffice')