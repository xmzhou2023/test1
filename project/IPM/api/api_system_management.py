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


def get_object_delete(objectname):
    '''
    系统管理_对象管理_对象删除
    param objectname:对象名称
    '''
    object=Api.Api_object_bid()
    for i in object:
        if i.get("name")==objectname:
            data = {"name":objectname,"stateCode":"off","rootModel":i.get("rootModel"),"bid":i.get("name"),"modelCode":i.get("modelCode")}
            headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()}
            response = Api.api_request('系统管理_对象管理_对象删除', data, headers)
            bid = response['body']
            print(bid)


if __name__ == '__main__':
    get_object_delete("测试22222")