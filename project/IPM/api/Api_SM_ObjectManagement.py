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



def get_object_delete(env_name,objectname):
    '''
    系统管理_对象管理_对象删除
    param objectname:对象名称
    '''
    Api=APIRequest(env_name)
    object=Api.Api_object_bid()
    for i in object:
        if objectname in i.get("name"):
            data = {"name":objectname,"stateCode":"off","rootModel":i.get("rootModel"),"bid":i.get("name"),"modelCode":i.get("modelCode")}
            headers = {'Content-Type': 'application/json', 'Authorization': Api.Api_login()[0],'p-rtoken': Api.Api_login()[1]}
            response = Api.api_request('系统管理_对象管理_对象删除', data, headers)
            bid = response['body']
            print(bid)


if __name__ == '__main__':
    get_object_delete('测试')
    # get_object_delete(env_name,"巍峨哇")
    # get_object_delete(env_name,"IPM自动化测试对象2023-02-0712:08:40")
    # get_object_delete(env_name,"IPM自动化测试对象2023-02-0712:11:00")
    # get_object_delete(env_name,"IPM自动化测试对象2023-02-0714:15:49")
    # get_object_delete(env_name,"IPM自动化测试对象2023-02-0714:17:55")
    # get_object_delete(env_name,"IPM自动化测试对象2023-02-0714:43:01")
    # get_object_delete(env_name,"IPM自动化测试对象2023-02-0715:03:47")
    # get_object_delete(env_name,"IPM自动化测试对象2023-02-0711:50:45")
    # get_object_delete(env_name,"IPM自动化测试对象2023-02-0710:55:57")
    # get_object_delete(env_name,"IPM自动化测试对象2023-02-0711:56:18")