from project.IPM.api.APIRequest import *
from libs.common.time_ui import *
from public.data.unified_login.unified import *
pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
usernum=account[15]['usernum']
enName=account[15]['enName']
username=account[15]['usernum']
deptId=account[15]['deptId']
deptName=account[15]['deptName']
email=account[15]['email']
uid=account[15]['uid']

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
def get_project_Team_member_find(probid,rolename):
    '''
    项目管理_团队_成员查询
    param templname:项目模板名称
    param projectname:项目名称
    '''
    # probid=get_project_create(templname,projectname)
    data = {"objInsBid":probid,"roleBid":rolename,"isQuerySonRole":False}
    headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()}
    response = Api.api_request('项目管理_团队_角色成员查询', data, headers)
    bid = response['body']
    return bid

def get_project_Team_member_add(templname,projectname,rolename):
    '''
    项目管理_团队_成员新增
    param templname:项目模板名称
    param projectname:项目名称
    '''
    probid=get_project_create(templname,projectname)
    get_project_Team_member_find(probid,rolename)
    data = [{"employeeName":"陈万红","enName":"WanHong Chen","type":"member","employeeNo":"18646295","deptId":"52002529","deptName":"PI_系统四部","phone":"15217725353","email":"WANHONG.CHEN@TRANSSION.COM","employeeNickName":"WanHong Chen","accountType":"01","route":True,"uid":"476402463000903680","jobNumber":"18646295","objInsBid":probid,"roleBid":rolename}]
    headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()}
    response = Api.api_request('项目管理_团队_成员新增', data, headers)
    bid = response['body']
    print(bid)
if __name__ == '__main__':
    # get_project_create('IPD模块化项目模板','测试1+1_{}'.format(now_times))
    # get_project_Team_member_find('1057371514845925376','HRBP')
    get_project_Team_member_add('IPD模块化项目模板','测试1+1_{}'.format(now_times),'HRBP')