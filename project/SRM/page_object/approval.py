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

    @allure.step("审批")
    def approval_search_name(self, name):
        self.is_click(user["审批列表"])
        time.sleep(2)
        self.frame_enter(user["iframe"])
        self.is_click(user["任务名称"])
        self.input_text(user["任务名称"], txt=name)
        self.is_click(user["查询"])

    def approval_search_task(self,subject):
        pass
    #
    # def approval_pass(self):
    #     self.is_click(user["审批最新一条"])
    #     self.is_click(user["审批通过"])
    #
    # def approval_search_number(self, number):
    #     self.input_text(user["主题"],txt=number)


    #
    # def approval_search_initiator(self, initiator):
    #      self.input_text(user["发起人"], txt=initiator)


if __name__ == '__main__':
    pass
