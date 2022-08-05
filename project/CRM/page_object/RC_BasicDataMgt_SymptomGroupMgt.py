import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
import pytest
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class SymPage(Base):
    """现象组"""

    @allure.step("进入现象组页面")
    def GoTo_Symp(self):
        self.is_click(user['一级菜单'], choice='Repair Center')
        self.is_click(user['Basic Data Mgt'])
        self.is_click(user['Symptom Group Mgt'])
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located(user["Edit_Button"]), message='数据加载不成功')  # 显示等待数据加载成功

    @allure.step("进入下载任务页面")
    def GoTo_Task(self):
        self.is_click(user['一级菜单'], choice='Report Center')
        self.is_click(user['Asynchronous Report Mgt'])
        self.is_click(user['Task List'])
        self.driver.implicitly_wait(5)  # 隐式等待页面加载成功

    @allure.step("下载导出的excel")
    def Download_Symp(self, name, content):
        self.is_click(user['Hide_Enabled_Task'])
        self.input_text(user['Menu_Name_Input'], txt=name)
        self.is_click(user['Search_Button'])
        task_status = self.element_text(user['Task_Status'])
        while task_status != '100-Finished':
            self.is_click(user['Search_Button'])
            wait = WebDriverWait(self.driver, timeout=5, poll_frequency=0.5)
            wait.until(EC.presence_of_element_located(user["Task_Status"]), message='数据加载不成功')
            task_status = self.element_text(user['Task_Status'])
        self.check_download(user['Download_Task'], content)




    @allure.step("添加现象组")
    def Add_Symp(self, name):
        self.is_click(user['Symptom_Group_Add'])
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located(user["Symptom_Group_Input"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        self.input_text(user['Symptom_Group_Input'], txt=name)
        self.is_click(user['Symptom_Group_Save'])

    @allure.step("查询现象组，返回查询到的现象组名称")
    def Get_Symp(self, name):
        self.input_text(user['Search_Input'], txt=name)
        self.is_click(user['Search_Button'])
        get_record = self.element_text(user['Search_Data_NO1'])
        return get_record

    @allure.step("查询现象组，返回查询到的现象组人、时间")
    def Get_Symp_DATE_BY(self, name):
        self.input_text(user['Search_Input'], txt=name)
        self.is_click(user['Search_Button'])
        created_date = self.element_text(user['List_Td_Five'])
        created_by = self.element_text(user['List_Td_Six'])
        modified_on = self.element_text(user['List_Td_Seven'])
        modified_by = self.element_text(user['List_Td_Eight'])
        return created_date, created_by, modified_on, modified_by

    @allure.step("Status Enable查询现象组")
    def Get_Enable_Status_Symp(self,status):
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Status'], status)
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Symptom_Total'])
        num = get_total.split(" ", 1)
        number = num[1]
        get_record = self.element_text(user['Enable_Return'])
        return number, get_record

    @allure.step("Status Disable查询现象组")
    def Get_Disable_Status_Symp(self, status):
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Status'], choice=status)
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Symptom_Total'])
        num = get_total.split(" ", 1)
        number = num[1]
        get_record = self.element_text(user['Disable_Return'])
        return number, get_record


    @allure.step("更改现象组状态")
    def Edit_Symp_Status(self, status):
        self.is_click(user['Status_Button'], choice=status)
        self.is_click(user["Edit_Status_Yes"])
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located(user["Edit_Button"]), message='数据加载不成功')  # 显示等待数据加载成功

    @allure.step("编辑现象组")
    def Edit_Symp(self, name):
        self.is_click(user['Edit_Button'])
        self.input_text(user['Symptom_Group_Input'], txt=name)
        self.is_click(user['Symptom_Group_Save'])
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=0.5)
        wait.until(EC.presence_of_element_located(user["Edit_Button"]), message='数据加载不成功')  # 显示等待数据加载成功

    @allure.step("导出现象组")
    def Export_Symp(self):
        self.is_click(user['Symptom_Export'])
        self.is_click(user['Export_OK'])

if __name__ == '__main__':
    pass
