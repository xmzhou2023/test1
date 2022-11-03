import time

import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ApprovalPage(Base):
    """审批类"""

    @allure.step("进入审批列表")
    def enter_approval(self):
        self.is_click(user["审批列表"])
        time.sleep(2)
        self.frame_enter(user["审批列表iframe"])


    def close_approval(self):
        self.frame_exit()
        self.is_click(user["审批列表界面关闭"])

    @allure.step("获取审批列表标题")
    def get_page_title(self):
        return self.find_element(user["审批列表标题"]).text

    @allure.step("审批列表任务名称查询")
    def approval_search_name(self, name):
        # self.is_click(user["审批列表"])
        # time.sleep(2)
        # self.frame_enter(user["审批列表iframe"])
        self.is_click(user["任务名称"])
        self.input_text(user["任务名称"], txt=name)
        self.is_click(user["查询"])

    def Clear_input(self):
        self.clear_input(user["任务名称"])
        self.is_click(user["查询"])


    @allure.step("任务名称查询结果")
    def get_name_title(self):
        return self.find_element(user["任务名称结果"]).text

    @allure.step("审批列表按主题查询")
    def approval_search_task(self, subject):
        # 通过主题查找
        self.is_click(user["主题"])
        self.input_text(user["主题"], txt=subject)
        self.is_click(user["查询"])
        self.clear_input(user["主题"])
        self.is_click(user["查询"])


    @allure.step("按主题查询结果")
    def get_subject_title(self):
        return self.find_element(user["主题标题"]).text


    @allure.step("审批列表按发起人查询")
    def approval_search_initiator(self, initiator):
        self.is_click(user["更多"])
        self.is_click(user["发起人"])
        self.input_text(user["发起人"], txt=initiator)
        self.is_click(user["查询"])


    @allure.step("审批列表按任务名称和发起人查询")
    def combination_search2(self, name, initiator):
        self.is_click(user["任务名称"])
        self.input_text(user["任务名称"], txt=name)
        self.is_click(user["更多"])
        self.is_click(user["发起人"])
        self.input_text(user["发起人"], txt=initiator)
        self.is_click(user["查询"])
        self.clear_input(user["任务名称"])
        self.is_click(user["更多"])
        self.clear_input(user["发起人"])
        self.is_click(user["查询"])




    @allure.step("审批列表按任务名称，主题,发起人组合查询")
    def combination_search3(self,subject, name, initiator):
        self.is_click(user["主题"])
        self.input_text(user["主题"], txt=subject)
        self.is_click(user["任务名称"])
        self.input_text(user["任务名称"], txt=name)
        self.is_click(user["更多"])
        self.is_click(user["发起人"])
        self.input_text(user["发起人"], txt=initiator)
        self.is_click(user["查询"])
        self.clear_input(user["主题"])
        self.clear_input(user["任务名称"])
        self.is_click(user["更多"])
        self.clear_input(user["发起人"])
        self.is_click(user["查询"])




    def serch_value(self):
        self.frame_back()
        self.frame_enter(user["审批内容iframe"])
        return self.find_element(user["审批查询结果"]).text





    @allure.step("审批列表查看审批历史")
    def approval_history(self):
        self.is_click(user["审批历史"])



    @allure.step("获取审批历史标题")
    def get_history_title(self):
        self.frame_back()
        return self.find_element(user["审批历史标题"]).text


    def close_history(self):
        self.is_click(user["审批历史界面关闭"])
        self.frame_enter(user["审批列表iframe"])



    def history_subject(self, subject):
        self.frame_back()
        self.frame_enter(user["审批历史-iframe"])
        self.input_text(user["审批历史-主题"], subject)
        self.is_click(user["审批历史-查询"])



    def Clear_input_subject(self):
        self.clear_input(user["审批历史-主题"])
        self.is_click(user["查询"])
        self.frame_back()


    def history_task(self, task):
        self.frame_back()
        self.frame_enter(user["审批历史-iframe"])
        self.input_text(user["审批历史-任务名称"], task)
        self.is_click(user["审批历史-查询"])



    def Clear_input_task(self):
        self.clear_input(user["审批历史-任务名称"])
        self.is_click(user["查询"])
        self.frame_back()



    def history_search_combined(self, subject,task):
        self.frame_back()
        self.frame_enter(user["审批历史-iframe"])
        self.input_text(user["审批历史-主题"], subject)
        self.input_text(user["审批历史-任务名称"], task)
        self.is_click(user["审批历史-查询"])


    def Clear_input_all(self):
        self.clear_input(user["审批历史-任务名称"])
        self.clear_input(user["审批历史-主题"])
        self.is_click(user["查询"])
        self.frame_back()






    # @allure.step("审批最新一条通过")
    # def approval_pass(self):
    #     self.is_click(user["审批最新一条"])
    #     # self.frame_enter(user["审批内容iframe"])
    #     # time.sleep(2)
    #     # self.is_click(user["审批通过"])
    #     frame = self.find_elements_srm(user["审批内容iframe"])[1]
    #     print("frame",frame)
    #     self.driver.switch_to.iframe(frame)
    #     # time.sleep(2)
    #     self.is_click(user["审批通过"])


if __name__ == '__main__':
    pass
