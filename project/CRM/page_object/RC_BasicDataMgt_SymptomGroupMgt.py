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

    @allure.step("合起菜单")
    def Close_Up_First_Menu(self, menu):
        self.is_click(user['一级菜单'], choice=menu)

    @allure.step("进入现象组页面")
    def GoTo_Symp(self):
        self.refresh()
        self.driver.implicitly_wait(5)  # 隐式等待页面加载成功
        self.is_click(user['一级菜单'], choice='Repair Center')
        self.is_click(user['Basic Data Mgt'])
        self.is_click(user['Symptom Group Mgt'])
        self.wait.until(EC.presence_of_element_located(user["Search_Button"]), message='数据加载不成功')  # 显示等待数据加载成功

    @allure.step("获取页面列表表头")
    def Group_List_Header(self):
        logging.info("获取列表数据")
        th_num = self.elements_num(user['表头字段个数'])
        list1 = []
        for i in range(1, th_num+1):
            logging.info(f'{i}')
            txt = self.element_text(user['表头字段'], f'{i}')
            logging.info(txt)
            list1.append(txt)
            logging.info(list1)
        return th_num, list1

    @allure.step("进入下载任务页面")
    def GoTo_Task(self):
        self.refresh()
        self.driver.implicitly_wait(5)  # 隐式等待页面加载成功
        self.is_click(user['一级菜单'], choice='Report Center')
        self.is_click(user['Asynchronous Report Mgt'])
        self.is_click(user['Task List'])
        self.driver.implicitly_wait(5)  # 隐式等待页面加载成功

    @allure.step("关闭打开的页面")
    def Close_Page(self):
        self.is_click(user['Close_Page'])

    @allure.step("下载导出的excel")
    def Download_Symp(self, name, content):
        self.is_click(user['Hide_Enabled_Task'])
        self.input_text(user['Menu_Name_Input'], txt=name)
        self.is_click(user['Search_Button'])
        task_status = self.element_text(user['Task_Status'])
        if task_status == '100-Finished':
            logging.info("状态为100，可以直接下载")
            self.check_download(user['Download_Task'], content)
        elif task_status != '100-Finished':
            while task_status != '100-Finished':
                self.is_click(user['Search_Button'])
                task_status = self.element_text(user['Task_Status'])
            self.check_download(user['Download_Task'], content)
        else:
            self.is_click(user['Search_Button'])
            self.wait.until(EC.presence_of_element_located(user["Download_Task"]), message='进度不是100')
            task_status = self.element_text(user['Task_Status'])
            self.check_download(user['Download_Task'], content)

    @allure.step("默认条件查询现象组，返回查询到的现象组名称")
    def Get_Defualt_Symp(self):
        self.is_click(user['Search_Button'])




    @allure.step("添加现象组")
    def Add_Symp(self, name):
        self.wait.until(EC.presence_of_element_located(user["Symptom_Group_Add"]), message='页面加载不成功')
        self.is_click(user['Symptom_Group_Add'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Group_Input"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        self.input_text(user['Symptom_Group_Input'], txt=name)
        self.wait.until(EC.presence_of_element_located(user["Symptom_Group_Save"]), message='save未出现')  # 显示等待页面加载成功
        self.is_click(user['Symptom_Group_Save'])
        self.wait.until(EC.presence_of_element_located(user["Search_Input"]), message='添加页面未关闭')  # 显示等待页面加载成功


    @allure.step("重复添加现象组")
    def Repeat_Add_Symp(self, name):
        self.is_click(user['Symptom_Group_Add'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Group_Input"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        self.input_text(user['Symptom_Group_Input'], txt=name)
        self.is_click(user['Symptom_Group_Save'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Group_Save"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        name_repeat_tip = self.element_text(user['Already_Exits'])
        return name_repeat_tip

    @allure.step("添加或编辑重复名称报错提示")
    def Name_Repeat_Tip(self):
        name_repeat_tip = self.element_text(user['Already_Exits'])
        return name_repeat_tip

    @allure.step("关闭现象组添加或编辑界面")
    def Close_Symp(self, operation):
        self.is_click(user['Close_Button'], choice=operation)
        self.is_click(user['Close_Confirm'])

    @allure.step("清空现象组查询框，恢复查询条件为默认值")
    def Clear_Get(self):
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Status'], choice="Enable")  # 将状态查询框恢复为默认Enable
        try:
            self.is_click(user['Search_Input'])
            self.hover(user['Input_Clear'])
            self.is_click(user['Input_Clear'])  # 将名称查询框清空
        except:
            logging.info("搜索框无数据")



    @allure.step("查询现象组，返回查询到的现象组名称")
    def Get_Symp(self, name):
        self.input_text(user['Search_Input'], txt=name)
        self.is_click(user['Search_Button'])
        get_record = self.element_text(user['Search_Data_name'], '1')
        return get_record

    @allure.step("查询现象组，返回查询到的现象组人、时间")
    def Get_Symp_DATE_BY(self, name):
        self.input_text(user['Search_Input'], txt=name)
        self.is_click(user['Search_Button'])
        created_date = self.element_text(user['List_Tr1_Td'], "5")
        created_by = self.element_text(user['List_Tr1_Td'], "6")
        modified_on = self.element_text(user['List_Tr1_Td'], "7")
        modified_by = self.element_text(user['List_Tr1_Td'], "8")
        return created_date, created_by, modified_on, modified_by

    @allure.step("Status Enable查询现象组")
    def Get_Enable_Status_Symp(self, status):
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Status'], status)
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Symptom_Total'])
        num = get_total.split(" ", 1)
        number = num[1]
        get_enable = self.element_text(user['Enable_Return'])
        get_record = self.element_text(user['Search_Data_name'], "1")
        return number, get_enable, get_record

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


    @allure.step("更改现象组状态")   # 需要加个判断
    def Edit_Symp_Status(self, status):
        self.is_click(user['Status_Button'], choice=status)
        self.is_click(user["Edit_Status_Yes"])
        self.wait.until(EC.presence_of_element_located(user["Search_Button"]), message='数据加载不成功')  # 显示等待数据加载成功

    @allure.step("编辑现象组")
    def Edit_Symp(self, name):
        self.is_click(user['Edit_Button'], choice="1")
        self.input_text(user['Symptom_Group_Input'], txt=name)
        self.is_click(user['Symptom_Group_Save'])
        self.wait.until(EC.presence_of_element_located(user["Search_Button"]), message='数据加载不成功')  # 显示等待数据加载成功

    @allure.step("编辑现象组为重复名称")
    def Repeat_Edit_Symp(self, name):
        self.is_click(user['Edit_Button'], choice="2")
        self.input_text(user['Symptom_Group_Input'], txt=name)
        self.is_click(user['Symptom_Group_Save'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Group_Save"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        name_repeat_tip = self.element_text(user['Already_Exits'])
        return name_repeat_tip

    @allure.step("导出现象组")
    def Export_Symp(self):
        self.is_click(user['Symptom_Export'])
        self.is_click(user['Export_OK'])

if __name__ == '__main__':
    pass
