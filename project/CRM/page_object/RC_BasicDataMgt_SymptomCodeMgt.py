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
import random, string
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class SymCodePage(Base):
    """现象码"""


    @allure.step("刷新页面")
    def GoTo_refresh(self):
        self.refresh()


    @allure.step("进入现象码页面")
    def GoTo_Symp_Code(self):
        self.refresh()
        self.driver.implicitly_wait(5)  # 隐式等待页面加载成功
        self.is_click(user['一级菜单'], choice='Repair Center')
        self.is_click(user['Basic Data Mgt'])
        self.is_click(user['Symptom Code Mgt'])
        self.wait.until(EC.presence_of_element_located(user["Search_Button"]), message='数据加载不成功')  # 显示等待数据加载成功

    @allure.step("获取页面列表表头")
    def Get_List_Header(self):
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


    @allure.step("save&add添加现象码")
    def SaveAdd_Symp_Code(self, code, grouping, description):
        self.is_click(user['Symptom_Code_Add'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Add"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        self.input_text(user['Symptom_Code_Input'], txt=code, choice='symptomCode')  # 添加页面输入现象码Code
        self.is_click(user['Symptom_Code_Input'], choice='symptomGroupId')
        self.input_text(user['Symptom_Code_Input'], txt=grouping, choice='symptomGroupId')  # 添加页面输入grouping
        self.hover(user['Symptom_Grouping_Select'], choice=grouping)
        self.is_click(user['Symptom_Grouping_Select'], choice=grouping)
        self.input_text(user['Symptom_Code_Input'], txt=description, choice='description')  # 添加页面输入描述
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_SaveAdd"]), message='save未出现')  # 显示等待页面加载成功
        self.is_click(user['Symptom_Code_SaveAdd'])

    @allure.step("添加窗口数据为空时，save&add不成功,获取提示")
    def All_Is_Empty(self):
        self.is_click(user['Symptom_Code_SaveAdd'])
        code_tip = self.element_text(user['Code_Null_Tip'])
        grouping_tip = self.element_text(user['Grouping_Null_Tip'])
        description_tip = self.element_text(user['Description_Null_Tip'])
        return code_tip, grouping_tip, description_tip


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


    @allure.step("添加现象码界面获取现象组")
    def Add_Interface_Grouping(self, grouping):
        self.is_click(user['Symptom_Code_Add'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Add"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        self.is_click(user['Symptom_Code_Input'], choice='symptomGroupId')
        self.input_text(user['Symptom_Code_Input'], txt=grouping, choice='symptomGroupId')  # 添加页面输入grouping
        self.hover(user['Symptom_Grouping_Select'], choice=grouping)
        grouping_name = self.element_text(user['Symptom_Grouping_Select'], grouping)
        self.is_click(user['Symptom_Grouping_Select'], choice=grouping)
        return grouping_name

    @allure.step("添加现象码界面获取现象组")
    def Add_No_Grouping(self, grouping):
        self.is_click(user['Symptom_Code_Add'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Add"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        self.is_click(user['Symptom_Code_Input'], choice='symptomGroupId')
        self.input_text(user['Symptom_Code_Input'], txt=grouping, choice='symptomGroupId')  # 添加页面输入grouping
        self.hover(user['Grouping_No_Data'])
        grouping_name = self.element_text(user['Grouping_No_Data'])
        return grouping_name

    @allure.step("添加或编辑重复名称报错提示")
    def Name_Repeat_Tip(self):
        name_repeat_tip = self.element_text(user['Already_Exits'])
        return name_repeat_tip

    @allure.step("关闭现象码添加或编辑界面")
    def Close_Symp(self, operation):
        self.is_click(user['Close_Button'], choice=operation)
        self.is_click(user['Close_Confirm'])

    @allure.step("关闭现象码空白添加界面")
    def Close_Code(self, operation):
        self.is_click(user['Close_Button'], choice=operation)

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
        get_record_code = self.element_text(user['Search_Data_name_tr1'], '3')
        get_record_group = self.element_text(user['Search_Data_name_tr1'], '5')
        get_record_description = self.element_text(user['Search_Data_name_tr1'], '4')
        return get_record_code, get_record_group, get_record_description

    @allure.step("查询现象码，无数据返回")
    def Get_No_Data(self, name):
        self.input_text(user['Input_Exact_Word'], txt=name)
        self.is_click(user['Search_Button'])
        get_record = self.element_text(user['Get_No_Data'], 'No Data')
        return get_record


    @allure.step("查询现象码，返回查询到的现象码人、时间")
    def Get_Code_DATE_BY(self, name):
        self.input_text(user['Input_Exact_Word'], txt=name)
        self.is_click(user['Search_Button'])
        created_date = self.element_text(user['List_Tr1_Td'], "6")
        created_by = self.element_text(user['List_Tr1_Td'], "7")
        modified_on = self.element_text(user['List_Tr1_Td'], "8")
        modified_by = self.element_text(user['List_Tr1_Td'], "9")
        return created_date, created_by, modified_on, modified_by

    @allure.step("Status Enable查询现象码")
    def Get_Status_Code(self, status):
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Status'], status)  # 选择状态查询
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Symptom_Total'])
        num = get_total.split(" ", 1)
        number = num[1]
        self.scroll_into_view_CRM(user['Page_Num'])
        page_num = self.elements_num(user['Page_Num'])  #
        logging.info(page_num)
        txt = self.element_text(user['Page_Specified'], f'{page_num}')  # 获取页码个数
        logging.info(txt)
        specified_page = random.randint(1, int(txt))
        logging.info("随机数为：")
        logging.info(specified_page)
        self.input_text(user['Page_Input'], txt=f'{specified_page}')  # 随机输入页码跳转
        self.send_enter()
        # 验证随机页码里的现象码状态正确
        th_num = self.elements_num(user['Current_Status_Num'])  # 获取当前页码上现象码个数
        list1 = []
        for i in range(1, th_num + 1):
                logging.info(f'{i}')
                txt = self.element_text(user['Current_Page_Staus'], f'{i}')
                logging.info(txt)
                list1.append(txt)
                logging.info(list1)
        self.refresh()
        return number, th_num, list1

    @allure.step("跳转页码")
    def input_page_code(self, num):
        self.input_text(user['Page_Input'], txt=num)  # 随机输入页码跳转
        self.send_enter()
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

    # @allure.step("跳转页码")
    # def Get_Status_Code(self, status):
    #     self.is_click(user['Search_Arrow'])
    #     self.is_click(user['Search_Arrow'])
    #     self.is_click(user['Search_Status'], status)
    #     self.is_click(user['Search_Button'])
    #     get_total = self.element_text(user['Symptom_Total'])
    #     num = get_total.split(" ", 1)
    #     number = num[1]
    #     # get_enable = self.element_text(user['Enable_Return'])
    #     # get_record = self.element_text(user['Search_Data_name'], choice="1")
    #     th_num = self.elements_num(user['页码个数'])  #
    #     txt = self.element_text(user['Current_Page_Staus'], choice=f'{th_num}')  # 获取页码个数
    #     list1 = []
    #     for i in range(1, th_num + 1):
    #             logging.info(f'{i}')
    #             txt = self.element_text(user['Current_Page_Staus'], choice=f'{i}')
    #             logging.info(txt)
    #             list1.append(txt)
    #             logging.info(list1)

    @allure.step("更改现象码状态")   # 需要加个判断
    def Edit_Code_Status(self, status):
        self.is_click(user['Status_Button'], choice=status)
        self.is_click(user["Edit_Status_Yes"])
        self.wait.until(EC.presence_of_element_located(user["Search_Button"]), message='数据加载不成功')  # 显示等待数据加载成功

    @allure.step("编辑现象码，修改描述")
    def Edit_Code_Description(self, description):
        self.is_click(user['Edit_Button'], choice="1")
        self.input_text(user['Symptom_Code_Input'], txt=description, choice='description')  # 添加页面输入描述
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Save"]), message='save未出现')  # 显示等待页面加载成功
        self.is_click(user['Symptom_Code_Save'])
        self.wait.until(EC.presence_of_element_located(user["Search_Button"]), message='数据加载不成功')  # 显示等待数据加载成功

    @allure.step("编辑现象码，修改所属现象组")
    def Edit_Code_Grouping(self, grouping):
        self.is_click(user['Edit_Button'], choice="1")
        self.is_click(user['Symptom_Code_Input'], choice='symptomGroupId')
        self.input_text(user['Symptom_Code_Input'], txt=grouping, choice='symptomGroupId')  # 添加页面输入grouping
        self.hover(user['Symptom_Grouping_Select'], choice=grouping)
        self.is_click(user['Symptom_Grouping_Select'], choice=grouping)
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Save"]), message='save未出现')  # 显示等待页面加载成功
        self.is_click(user['Symptom_Code_Save'])
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
