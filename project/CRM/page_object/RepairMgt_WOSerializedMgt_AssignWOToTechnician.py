import string
from datetime import datetime

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

class WOSerializedAssignToTech(Base):

    """序列化工单分派技术员类"""
    @allure.step("序列化工单分派技术员")
    def woassigntotech(self, workorder, status, row=None, column=None):
        self.refresh()
        self.is_click(user["序列化工单分派技术员页Exact Word输入框"])
        logging.info("序列化工单号={}".format(workorder))
        self.input_text(user["序列化工单分派技术员页Exact Word输入框"], txt=workorder)
        self.is_click(user["Search按钮"])

        if status == "Created":
            self.driver.find_element(By.XPATH, "//tr[{0}]/td[{1}]//span[contains(@class,'input')]".format(row, column)).click()
            self.is_click(user["Assign To输入框"])
            self.is_click(user["Assign To下拉选择框"])
            self.is_click(user["序列化工单分派技术员页Assign Select按钮"])
            self.is_click(user["序列化工单分派技术员二次确认弹框Yes"])
            sleep(1)

        else:
            search_total = self.get_element_attribute(user['序列化工单分派技术员页工单total数'], 'textContent')
            total = ''.join(filter(str.isdigit, search_total))
            total = int(total)
            logging.info('序列化工单分派技术员页工单查询total数量:{}'.format(total))
            return total


    @allure.step("获取序列化工单号")
    def getworkorderno(self, row=None, column=None, status=None):
        self.is_click(user['序列化工单查询页From Date输入框'])
        self.hover(user['序列化工单查询页From Date输入框'])
        self.is_click(user['序列化工单查询页From Date清除按钮'])
        self.is_click(user['序列化工单查询页Document Status输入框'])
        self.hover(user['序列化工单查询页Document Status下拉选择'], choice=status)
        self.find_element(user['序列化工单查询页Document Status下拉选择'], status).click()
        self.is_click(user["Search按钮"])
        logging.info("开始获取第一行序列化工单号")
        word = self.driver.find_element(By.XPATH, "//tr[{}]/td[{}]//div[normalize-space(text())]".format(row, column)).text

        logging.info("定位到的序列化工单号为:{}".format(word))
        sleep(2)


        return word


if __name__ == '__main__':
    pass
