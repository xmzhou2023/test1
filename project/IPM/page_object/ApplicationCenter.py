'''应用中心'''


import logging

import allure

from project.IPM.page_base.basics_IPM import PubicMethod
from libs.common.time_ui import *
from project.IPM.page_base.assert_pubic import *
from project.IPM.api.APIRequest import *
from project.IPM.page_object.Generalmethods import *
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
        :param applyname: 应用名称
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

    @allure.step("应用中心_DCP看板详情_表单操作按钮_同意预约_发送通知")
    def DCP_bulletinboard_operation_AgreeToMakeAnAppointment_SendOut(self):
        self.click_IPM("设置通知内容_发送通知")
        sleep(1)

    @allure.step("应用中心_DCP看板详情_表单操作按钮_同意预约_取消")
    def DCP_bulletinboard_operation_AgreeToMakeAnAppointment_cancel(self):
        self.click_IPM("设置通知内容_取消")
        sleep(1)

    @allure.step("应用中心_DCP看板详情_表单操作按钮_同意预约_收件人")
    def DCP_Cc(self,JobNo):
        self.click_IPM("设置通知内容_抄送人")
        personnel=General_methods(self.driver)
        personnel.personnel_list(JobNo)
        sleep(1)

    @allure.step("应用中心_DCP看板详情_表单操作按钮_同意预约_收件人")
    def DCP_addressee(self,JobNo):
        self.click_IPM("设置通知内容_收件人")
        personnel=General_methods(self.driver)
        personnel.personnel_list(JobNo)
        sleep(1)

    @allure.step("应用中心_DCP看板详情_表单操作按钮")
    def DCP_bulletinboard_operation(self,projectname,ApplyButton,addresseeJobNo,CcJobNo,SendOut_Or_Cancel=None):
        '''
        :param projectname: 预约上会的项目名称
        :param ApplyButton: 应用按钮，如： 进入详情/同意预约/拒绝预约
        '''
        self.ApplicationCenter_entrance()
        self.Card_application("DCP看板")
        self.switch_window(-1)
        self.DCP_bulletinboard(projectname,ApplyButton)
        if ApplyButton == "同意预约":
            self.DCP_addressee(addresseeJobNo)
            self.DCP_Cc(CcJobNo)
            if SendOut_Or_Cancel ==None or SendOut_Or_Cancel=="发送通知":
                self.DCP_bulletinboard_operation_AgreeToMakeAnAppointment_SendOut()
            else:
                self.DCP_bulletinboard_operation_AgreeToMakeAnAppointment_cancel()












