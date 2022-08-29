import allure, os
from public.base.basics import Base, sleep
from selenium.webdriver.support.select import Select
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

class SymCodePage(Base):
    """现象码"""

    @allure.step("进入现象码页面")
    def GoTo_Symp_Code(self):
        self.refresh()
        self.driver.implicitly_wait(5)  # 隐式等待页面加载成功
        self.is_click(user['一级菜单'], choice='Repair Center')
        self.is_click(user['Basic Data Mgt'])
        self.is_click(user['Symptom Code Mgt'])
        self.wait.until(EC.presence_of_element_located(user["Search_Button"]), message='数据加载不成功')  # 显示等待数据加载成功


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
    def Download_Symp_Code(self, name, content):
        self.is_click(user['Hide_Enabled_Task'])
        self.input_text(user['Menu_Name_Input'], txt=name)
        self.is_click(user['Search_Button'])
        task_status = self.element_text(user['Task_Status'])
        if task_status =='95-Failed':
            assert False, '导出失败,状态为95-Failed'
        elif task_status != '100-Finished':
            while task_status != '100-Finished':
                self.is_click(user['Search_Button'])
                task_status = self.element_text(user['Task_Status'])
            self.check_download(user['Download_Task'], content)
        elif task_status == '100-Finished':
            self.check_download(user['Download_Task'], content)




    @allure.step("添加现象码")
    def Add_Symp_Code(self, code, grouping, description):
        self.is_click(user['Symptom_Code_Add'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Add"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        self.input_text(user['Symptom_Code_Input'], txt=code, choice='symptomCode')  # 添加页面输入现象码Code
        self.is_click(user['Symptom_Code_Input'], choice='symptomGroupId')
        self.input_text(user['Symptom_Code_Input'], txt=grouping, choice='symptomGroupId')  # 添加页面输入grouping
        self.hover(user['Symptom_Grouping_Select'], choice=grouping)
        self.is_click(user['Symptom_Grouping_Select'], choice=grouping)
        self.input_text(user['Symptom_Code_Input'], txt=description, choice='description')  # 添加页面输入描述
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Save"]), message='save未出现')  # 显示等待页面加载成功
        self.is_click(user['Symptom_Code_Save'])
        self.wait.until(EC.presence_of_element_located(user["Input_Exact_Word"]), message='添加页面未关闭')  # 显示等待页面加载成功


    @allure.step("重复添加现象码")
    def Repeat_Add_Code(self, code, grouping, description):
        self.is_click(user['Symptom_Code_Add'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Add"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        self.input_text(user['Symptom_Code_Input'], txt=code, choice='symptomCode')  # 添加页面输入现象码Code
        self.is_click(user['Symptom_Code_Input'], choice='symptomGroupId')
        self.input_text(user['Symptom_Code_Input'], txt=grouping, choice='symptomGroupId')  # 添加页面输入grouping
        self.hover(user['Symptom_Grouping_Select'], choice=grouping)
        self.is_click(user['Symptom_Grouping_Select'], choice=grouping)
        self.input_text(user['Symptom_Code_Input'], txt=description, choice='description')  # 添加页面输入描述
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Save"]), message='save未出现')  # 显示等待页面加载成功
        self.is_click(user['Symptom_Code_Save'])
        name_repeat_tip = self.element_text(user['Already_Exits'])
        return name_repeat_tip

    @allure.step("添加现象码未save")
    def Add_Symp_Code_Not_Save(self, code, grouping, description):
        self.is_click(user['Symptom_Code_Add'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Add"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        self.input_text(user['Symptom_Code_Input'], txt=code, choice='symptomCode')  # 添加页面输入现象码Code
        self.is_click(user['Symptom_Code_Input'], choice='symptomGroupId')
        self.input_text(user['Symptom_Code_Input'], txt=grouping, choice='symptomGroupId')  # 添加页面输入grouping
        self.hover(user['Symptom_Grouping_Select'], choice=grouping)
        self.is_click(user['Symptom_Grouping_Select'], choice=grouping)
        self.input_text(user['Symptom_Code_Input'], txt=description, choice='description')  # 添加页面输入描述
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Save"]), message='save未出现')  # 显示等待页面加载成功

    @allure.step("添加或编辑重复名称报错提示")
    def Name_Repeat_Tip(self):
        name_repeat_tip = self.element_text(user['Already_Exits'])
        return name_repeat_tip

    @allure.step("关闭现象码添加或编辑界面")
    def Close_Symp(self, operation):
        self.is_click(user['Close_Button'], choice=operation)
        self.is_click(user['Close_Confirm'])

    @allure.step("清空现象码查询框，恢复查询条件为默认值")
    def Code_Clear_Get(self):
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Status'], choice="Enable")  # 将状态查询框恢复为默认Enable
        try:
            self.is_click(user['Input_Exact_Word'])
            self.hover(user['Input_Clear'])
            self.is_click(user['Input_Clear'])  # 将现象码名称查询框清空
        except:
            logging.info("搜索框无数据")

    @allure.step("清空现象组查询框，恢复查询条件为默认值")
    def Group_Clear_Get(self):
        try:
            self.is_click(user['Input_Grouping'])
            self.hover(user['Input_Clear'])
            self.is_click(user['Input_Clear'])  # 将现象组名称查询框清空
        except:
            logging.info("搜索框无数据")


    @allure.step("默认条件查询现象码，返回查询到的现象码名称")
    def Get_Defualt_Symp_Code(self):
        self.is_click(user['Search_Button'])

    @allure.step("查询现象码，返回查询到的现象码名称")
    def Get_Symp_Code(self, name):
        self.input_text(user['Input_Exact_Word'], txt=name)
        self.is_click(user['Search_Button'])
        get_record_code = self.element_text(user['Search_Data_name_tr1'], choice='3')
        get_record_group = self.element_text(user['Search_Data_name_tr1'], choice='5')
        get_record_description = self.element_text(user['Search_Data_name_tr1'], choice='4')
        return get_record_code, get_record_group, get_record_description

    @allure.step("查询现象码，无数据返回")
    def Get_No_Data(self, name):
        self.input_text(user['Input_Exact_Word'], txt=name)
        self.is_click(user['Search_Button'])
        get_record = self.element_text(user['Get_No_Data'], choice='No Data')
        return get_record


    @allure.step("查询现象码，返回查询到的现象码人、时间")
    def Get_Symp_DATE_BY(self, name):
        self.input_text(user['Input_Exact_Word'], txt=name)
        self.is_click(user['Search_Button'])
        created_date = self.element_text(user['List_Tr1_Td'], choice="5")
        created_by = self.element_text(user['List_Tr1_Td'], choice="6")
        modified_on = self.element_text(user['List_Tr1_Td'], choice="7")
        modified_by = self.element_text(user['List_Tr1_Td'], choice="8")
        return created_date, created_by, modified_on, modified_by

    @allure.step("Status Enable查询现象码")
    def Get_Enable_Status_Code(self, status):
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Status'], status)
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Symptom_Total'])
        num = get_total.split(" ", 1)
        number = num[1]
        get_enable = self.element_text(user['Enable_Return'])
        get_record = self.element_text(user['Search_Data_name'], choice="1")
        return number, get_enable, get_record

    @allure.step("Status Disable查询现象码")
    def Get_Disable_Status_Code(self, status):
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Status'], choice=status)
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Symptom_Total'])
        num = get_total.split(" ", 1)
        number = num[1]
        get_record = self.element_text(user['Disable_Return'])
        return number, get_record


    @allure.step("更改现象码状态")   # 需要加个判断
    def Edit_Symp_Status(self, status):
        self.is_click(user['Status_Button'], choice=status)
        self.is_click(user["Edit_Status_Yes"])
        self.wait.until(EC.presence_of_element_located(user["Search_Button"]), message='数据加载不成功')  # 显示等待数据加载成功

    @allure.step("编辑现象码")
    def Edit_Symp(self, name):
        self.is_click(user['Edit_Button'], choice="1")
        self.input_text(user['Symptom_Group_Input'], txt=name)
        self.is_click(user['Symptom_Group_Save'])
        self.wait.until(EC.presence_of_element_located(user["Search_Button"]), message='数据加载不成功')  # 显示等待数据加载成功

    @allure.step("编辑现象码为重复名称")
    def Repeat_Edit_Symp(self, name):
        self.is_click(user['Edit_Button'], choice="2")
        self.input_text(user['Symptom_Group_Input'], txt=name)
        self.is_click(user['Symptom_Group_Save'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Group_Save"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        name_repeat_tip = self.element_text(user['Already_Exits'])
        return name_repeat_tip

    @allure.step("导出现象码")
    def Export_Symp(self):
        self.is_click(user['Symptom_Export'])
        self.is_click(user['Export_OK'])

if __name__ == '__main__':
    pass
