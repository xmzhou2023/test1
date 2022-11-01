import string
from datetime import datetime
from selenium.webdriver.common.by import By

import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from .Center_Component import NavPage
from ..test_case.conftest import *
import random

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class WOSerializedAssignSpareToWO(Base):
    """序列化工单派料类"""

    @allure.step("序列化工单派料")
    def woassigntowo(self, workorder):
        self.refresh()
        self.wait.until(EC.presence_of_element_located(user["序列化工单派料页Add按钮"]), message="页面刷新失败")
        self.is_click(user["序列化工单派料页单号输入框WO Serialized No"])
        logging.info("序列化工单号={}".format(workorder))
        self.input_text(user["序列化工单派料页单号输入框WO Serialized No"], txt=workorder)
        # if status != "Assigned To Technician":
        self.is_click(user["序列化工单派料页OK按钮"])



    @allure.step("获取序列化工单号")
    def getworkorderno(self, row=None, column=None, status=None):
        self.refresh()
        self.is_click(user['序列化工单查询页From Date输入框'])
        self.hover(user['序列化工单查询页From Date输入框'])
        self.is_click(user['序列化工单查询页From Date清除按钮'])
        self.is_click(user['序列化工单查询页Document Status输入框'])
        self.hover(user['序列化工单查询页Document Status下拉选择'], choice=status)
        self.find_element(user['序列化工单查询页Document Status下拉选择'], status).click()
        self.is_click(user['序列化工单Hide Completed勾选框'])
        self.is_click(user["Search按钮"])
        logging.info("开始获取第一行序列化工单号")
        word = self.driver.find_element(By.XPATH, "//tr[{}]/td[{}]//div[normalize-space(text())]".format(row, column)).text
        logging.info("定位到的序列化工单号为:{}".format(word))
        sleep(2)
        return word







# if __name__ == '__main__':
#     pass
