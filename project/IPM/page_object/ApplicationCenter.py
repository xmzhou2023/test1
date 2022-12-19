'''应用中心'''


import logging

import allure

from project.IPM.page_base.basics_IPM import PubicMethod
from libs.common.time_ui import *
from project.IPM.page_base.assert_pubic import *
from project.IPM.api.APIRequest import *
import random
Api = APIRequest()


class ApplicationCenter(PubicMethod):

    def __init__(self,driver,element_yaml='ApplicationCenter',expect='ApplicationCenter.yaml'):
        super().__init__(driver, element_yaml,expect=expect)


    @allure.step("应用中心入口")
    def ApplicationCenter_entrance(self):
        self.click_IPM('应用中心')
        sleep(1)

    @allure.step("应用中心_点击对应卡片")
    def Card_application(self,applyname):
        '''
        :param applyname: 应用名称,
        :param ApplyButton: 应用按钮，如： 进入详情/同意预约/拒绝预约
        '''
        self.click_IPM("应用",applyname)
        sleep(2)

    @allure.step("应用中心_DCP看板详情")
    def DCP_bulletinboard(self,projectname,ApplyButton):
        '''
        :param projectname: 预约上会的项目名称
        :param ApplyButton: 应用按钮，如： 进入详情/同意预约/拒绝预约
        '''
        self.click_IPM("操作按钮",projectname,ApplyButton)
        sleep(2)







