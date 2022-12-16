import logging

from project.IPM.page_base.basics_IPM import PubicMethod
from libs.common.time_ui import *
from project.IPM.page_base.assert_pubic import *
from project.IPM.api.APIRequest import *
import random


Api = APIRequest()
# ApplyList=Api.Api_applyList(20220810085734677324)
# Api.Api_queryDeptAndEmployee(20220810085734677324)
def field_attribute_maintennance(self):
    field_att = Api.Api_project_field("开模流程测试")

now_times = strftime('%Y-%m-%d%H:%M:%S')
now_t = strftime('%Y-%m-%d')
time_ipm=f'ipm自动化{now_times}'
class ProcessCenter(PubicMethod):

    def __init__(self,driver,element_yaml='ProcessCenter_Moldopeningprocess',expect='ProcessCenter_Moldopeningprocess.yaml'):
        super().__init__(driver, element_yaml,expect=expect)

    def fieldname(self,name):
        self.click_IPM('字段',name)


class ProcessCenter_Assert_result(AssertMode):
    def __init__(self,driver,element_yaml='ProcessCenter_Moldopeningprocess', expect='ProcessCenter_Moldopeningprocess.yaml'):
        super().__init__(driver, element_yaml,expect=expect)