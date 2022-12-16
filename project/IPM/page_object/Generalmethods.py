import logging

from project.IPM.page_base.basics_IPM import PubicMethod
from libs.common.time_ui import *
from project.IPM.page_base.assert_pubic import *
from project.IPM.api.APIRequest import *
import random

class General_methods(PubicMethod):

    def __init__(self,driver,element_yaml='Generalmethods',expect='Generalmethods.yaml'):
        super().__init__(driver, element_yaml,expect=expect)
    def personnel_list(self, text, Confirm_or_Cancel=None):
        '''
        人员列表
        人员选择
        '''
        sleep(2)
        self.input_text_IPM("请输入姓名或工号", text)
        self.click_IPM("选择人员", text)
        if Confirm_or_Cancel == None or Confirm_or_Cancel == "确定":
            self.click_IPM("人员列表_确定")
        else:
            self.click_IPM("人员列表_取消")