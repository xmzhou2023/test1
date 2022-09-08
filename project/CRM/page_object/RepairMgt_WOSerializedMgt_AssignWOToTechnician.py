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
    def woassigntotech(self, workorder, status, scope="single", row=None, column=None):
        self.refresh()
        self.is_click(user["序列化工单分派技术员页Exact Word输入框"])
        logging.info("序列化工单号={}".format(workorder))
        self.input_text(user["序列化工单分派技术员页Exact Word输入框"], txt=workorder)
        self.is_click(user["Search按钮"])

        if status == "Created" and scope == "single":
            """单个10状态工单点击assign select分派技术员"""
            self.driver.find_element(By.XPATH, "//tr[{0}]/td[{1}]//span[contains(@class,'input')]".format(row, column)).click()
            self.is_click(user["Assign To输入框"])
            self.is_click(user["Assign To下拉选择框"])
            self.is_click(user["序列化工单分派技术员页Assign Select按钮"])
            self.is_click(user["序列化工单分派技术员二次确认弹框Yes"])
            sleep(1)
        elif status == "Created" and scope == "All":
            """单个10状态工单点击assign all分派技术员"""
            self.is_click(user["Assign To输入框"])
            self.is_click(user["Assign To下拉选择框"])
            self.is_click(user["序列化工单分派技术员页Assign All按钮"])
            self.is_click(user["序列化工单分派技术员二次确认弹框Yes"])
            sleep(1)

        elif status != "Created" and scope == "single":
            """非10状态工单在分派技术员页无法查到，所以判断的是查询结果是否为0"""
            search_total = self.get_element_attribute(user['序列化工单分派技术员页工单total数'], 'textContent')
            total = ''.join(filter(str.isdigit, search_total))
            total = int(total)
            logging.info('序列化工单分派技术员页工单查询total数量:{}'.format(total))
            return total
        elif status == "Created" and scope == "re-single":
            self.is_click(user["序列化工单分派技术员页Re-Assigned按钮"])
            self.is_click(user["Re-Assigned弹框页WO Serialized 输入框"])
            self.input_text(user["Re-Assigned弹框页WO Serialized 输入框"], txt=workorder)
            self.is_click(user["Re-Assigned弹框页Re-Assign To 输入框"])
            self.is_click()


        else:
            self.is_click(user["序列化工单分派技术员页Assign By Scan按钮"])
            self.is_click(user["Assign By Scan弹框页的Assign to 输入框"])
            self.is_click(user["Assign By Scan弹框页的Assign to下拉选择框"])
            self.is_click(user["Assign By Scan弹框页的WO Serialized No输入框"])
            self.input_text(user["Assign By Scan弹框页的WO Serialized No输入框"], txt=workorder)
            self.is_click(user["Assign By Scan弹框页的Add按钮"])

            if status == "Created" and scope == "Scan":
                """点击assign by scan后进入弹框页，输入10状态的工单可操作成功，此处校验了弹框页total数以及操作提示"""
                self.wait.until(EC.presence_of_element_located(user['Assign By Scan弹框页表格中的删除键']), message='分派技术员列表数据未添加成功')
                search_total = self.get_element_attribute(user['Assign By Scan弹框页的total数'], 'textContent')
                total = ''.join(filter(str.isdigit, search_total))
                total = int(total)
                if total >= 1:
                    self.is_click(user["Assign By Scan弹框页的Save按钮"])
                else:
                    logging.info("Assign By Scan弹框页表格中的total数值不准确")
                    self.is_click(user["Assign By Scan弹框页的Cancel按钮"])
            elif status != "Created" and scope == "Scan":
                """点击assign by scan后进入弹框页，输入非10状态的工单提示报错"""
                self.is_click(user["Assign By Scan弹框页的Cancel按钮"])
                self.is_click(user["Assign By Scan弹框页的二次确认框Confirm按钮"])

    @allure.step("序列化工单改派技术员")
    def woreassigntotech(self,workorder, status):
        self.refresh()
        self.is_click(user["序列化工单分派技术员页Re-Assigned按钮"])
        self.is_click(user["Re-Assigned弹框页WO Serialized 输入框"])
        self.input_text(user["Re-Assigned弹框页WO Serialized 输入框"], txt=workorder)
        self.is_click(user["Re-Assigned弹框页Re-Assign To 输入框"])
        self.is_click(user["Re-Assigned弹框页Re-Assign To下拉选择框"])
        if status == "Assigned To Technician":
            self.is_click(user["Re-Assigned弹框页Save按钮"])
        else:
            self.is_click(user["Re-Assigned弹框页Cancel按钮"])
            self.is_click(user["Re-Assigned弹框页的二次确认框Confirm按钮"])

    @allure.step("菜单刷新")
    def refresh_page(self):
        self.is_click(user['Dashboard'])
        self.refresh()
        self.wait.until(EC.presence_of_element_located(user['Dashboard']), message="页面刷新失败")


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
