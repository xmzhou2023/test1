from project.TBM.api.api import APIRequest
import requests

# cd C:\Program Files\Google\Chrome\Application
# chrome.exe --remote-debugging-port=9527 --user-data-dir="D:\selenium\AutomationProfile"
# http://10.250.112.166:9000/#/systemManage/userManage
# http://39.101.161.151/#/popupwindow
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# from page_base.webpage import WebPage

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = webdriver.Chrome(options=options)


import re
# # driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/div[2]/section/div/div/div[2]/div[4]/div[2]/table/tbody/tr/td[8]/div/div/button[1]/span").click()
a = driver.find_element(By.XPATH,"//div[@class='el-table__fixed-body-wrapper']//table[@class='el-table__body']//tr//td[2]").get_attribute("innerHTML")
c = driver.find_element(By.XPATH,"//div[@class='el-table__fixed-body-wrapper']//table[@class='el-table__body']//tr[2]//td[2]").get_attribute("innerHTML")
b = driver.find_element(By.XPATH,"//div[@class='el-table__fixed-body-wrapper']//table[@class='el-table__body']//tr//td[2]")
print(b.text)
print(re.findall("<div>(.*?)</div>", a)[0])
print(re.findall("<div>(.*?)</div>", c))


txt = '#*RD -015.92 +0000.C\r'
print(float(re.findall("#*RD(.*?)\+0000", txt)[0]))


# token = APIRequest().tbm_login()
# # body1 = {"status": "Process"}
# headers = {'Content-Type': 'application/json',
#            'Authorization': token}
# # url1 = 'https://pfgatewayidct.transsion.com:9188' \
# #        '/process-center/process-center/history/480999968208470016' \
# #        '/applyList?pageNo=1&pageSize=10'
# #
# # chaxundaiban = requests.post(url=url1, json=body1, headers=headers).json()['data']['list']
# # instanceId_list = []
# # for i in chaxundaiban:
# #     if 'taskName' not in i.keys():
# #         instanceId_list.append(i['instanceId'])
# # print(instanceId_list)
# # for i in instanceId_list:
# chaxun = requests.get(
#     url=f'https://pfgatewayidct.transsion.com:9188/process-center/process-center/tasks/getRunTriggerReceiveInfo/93fcdc48-1498-11ed-bee3-0242ac130002',
#     headers=headers).json()
# print(chaxun)
# jihuourl = 'https://pfgatewayidct.transsion.com:9188/process-center/process-center/tasks/sendTriggerReceive'
# jihuobody = {
#     "processInstId": '93fcdc48-1498-11ed-bee3-0242ac130002',
#     "executionId": chaxun
# }
# jihuo = requests.post(url=jihuourl, json=jihuobody, headers=headers)
# print(jihuo)
# chehui = requests.delete(url=f'https://pfgatewayidct.transsion.com:9188/process-center/process-center/instance/93fcdc48-1498-11ed-bee3-0242ac130002/revoke',
#                          headers=headers).json()
# print(chehui)
# login_body = {"username":"18645960", "pwd":"eExpbHk2eA=="}
# token = requests.post(url='http://pfgatewayuat.transsion.com:9099/service-pt-unified-auth/pt-unified-auth/login',
#                   json=login_body).json()['data']['token']
# headers = {'Content-Type': 'application/json',
#            'Authorization': token}
# list_body = {"current":1,"size":1,"param":{"code": "20220811025552978103"}}
# b = requests.post(url='https://pfgatewayuat.transsion.com:9199/service-hulk-workflow-transfer/workflow/task/applyList',
#                   json=list_body, headers=headers).json()['data']['list'][0]['applicant']
# # print(b)
# d='李小素'
# c = requests.post(url='https://pfgateway.transsion.com:9199/service-cp-uc-extend/cp-uc-extend/Department/queryDeptAndEmployee',
#                   data=d.encode('utf-8'), headers=headers).json()
# print(c)