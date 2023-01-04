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
import time
import openpyxl
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from libs.config.conf import LOCATE_MODE, DOWNLOAD_PATH, IMAGE_PATH, BASE_DIR
from libs.common.time_ui import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import logging
import allure
import datetime
import ddddocr
import random, string
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class JSPage(Base):
    """JS手机工单"""


    @allure.step("合起菜单")
    def Close_Up_First_Menu(self, menu):
        self.is_click(user['一级菜单'], choice=menu)


    @allure.step("进入JS List页面")
    def GoTo_JS_List(self):
        self.refresh()
        self.driver.implicitly_wait(5)  # 隐式等待页面加载成功
        self.is_click(user['一级菜单'], choice='Repair Center')
        self.is_click(user['二级菜单'], choice='JS Mgt')
        self.is_click(user['三级菜单'], choice='JS List')
        self.wait.until(EC.presence_of_element_located(user["Search_Button"]), message='数据加载不成功')  # 显示等待数据加载成功

    @allure.step("获取页面列表表头")
    def Get_List_Header(self):
        logging.info("获取列表数据")
        th_num = self.elements_num(user['表头字段个数'])
        list1 = []
        for i in range(1, 10):
            logging.info(f'{i}')
            txt = self.element_text(user['表头字段'], f'{i}')
            logging.info(txt)
            list1.append(txt)
            logging.info(list1)
        self.driver.execute_script("document.documentElement.scrollTop=600")
       #  left = self.find_element(user['Scroll_Data'], 'is-scrolling')
       #  # middle = self.find_element(user['Scroll_Data'], 'is-scrolling-middle')
       #  # right = self.find_element(user['Scroll_Data'], 'is-scrolling-right')
       # # self.drag_and_drop(user['Scroll_Data'], 'is-scrolling-left', 'is-scrolling-middle')
       #  kw_x = left.location.get('x')#x坐标
       #  kw_y = left.location.get('y')#y坐标
       #  logging.info(kw_x)
       #  logging.info(kw_y)
       #  sleep(5)
       #  self.click_and_hold(user['Scroll_Data'], 'is-scrolling', 500, kw_y)
       #  #ActionChains(self).drag_and_drop_by_offset(left, kw_x+300, kw_y).perform()
       #  for i in range(10, 16):
       #      logging.info(f'{i}')
       #      #self.scroll_into_view_CRM(user['表头字段'], f'{i}')
       #      txt = self.element_text(user['表头字段'], f'{i}')
       #      logging.info(txt)
       #      list1.append(txt)
       #      logging.info(list1)
       #  sleep(5)
       #  self.click_and_hold(user['Scroll_Data'], 'is-scrolling', 700, kw_y)
       #  #ActionChains(self).drag_and_drop_by_offset(left, kw_x+600, kw_y).perform()
       #  for i in range(16, th_num+1):
       #      logging.info(f'{i}')
       #      #self.scroll_into_view_CRM(user['表头字段'], f'{i}')
       #      txt = self.element_text(user['表头字段'], f'{i}')
       #      logging.info(txt)
       #      list1.append(txt)
       #      logging.info(list1)
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

    @allure.step("工单save按钮")
    def Save_JS(self):
        self.is_click(user['JS_Save'])
        self.is_click(user['JS_Save'])
        self.wait.until(EC.presence_of_element_located(user["Search_Button"]), message='save不成功')


    @allure.step("添加JS,输入Basic Info信息")
    def Add_JS_Basic_Info(self, reference_from, imei, physical, symptom, item):
        self.is_click(user['JS_Add'])
        self.wait.until(EC.presence_of_element_located(user["Reference_From"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        sleep(2)
        self.is_click(user['Reference_From'])
        self.hover(user['JS_From_Data'], choice=reference_from)
        self.is_click(user['JS_From_Data'], choice=reference_from)  # 选择方式
        self.is_click(user['IMEI_Input'])
        self.input_text(user['IMEI_Input'], txt=imei)  # 添加页面输入JS IMEI
        self.hover(user['IMEI_Select'], choice=imei)
        self.is_click(user['IMEI_Select'], choice=imei)  # 点击查询到的IMEI
        #self.find_element(user["Quickly_Repair_JS"])
        #self.is_click(user['Quickly_Repair_JS'])
        self.driver.execute_script("document.documentElement.scrollTop=300")  # 往下滑动以便找到Physical Condition
        self.is_click(user['Physical_Condition'])
        self.input_text(user['Physical_Condition'], txt=physical)  # 添加页面输入physical
        self.hover(user['JS_Data'], choice=physical)
        self.is_click(user['JS_Data'], physical)
        self.driver.execute_script("document.documentElement.scrollTop=800")  # 往下滑动以便找到Symptoms List
        self.is_click(user['Symptoms_List'])
        self.input_text(user['Symptoms_List'], txt=symptom)  # 添加页面输入symptom
        self.hover(user['JS_Data'], choice=symptom)
        self.is_click(user['JS_Data'], symptom)
        self.is_click(user['Add_Symptom'])  # 点击+将选择的现象码加入列表
        symptom_code = self.element_text(user["Symptom_Code"])
        self.is_click(user['Item_Received'], item)
        return symptom_code


    @allure.step("添加JS,输入Customer Info信息")
    def Add_JS_Customer_Info(self, recevied_from, customer_name, country, mobile_area, mobile_no):
        self.wait.until(EC.presence_of_element_located(user["Region"]), message='滑动页面不成功')
        self.is_click(user['JS_Info'], choice="receiveSourceCode")
        self.hover(user['JS_Data'], choice=recevied_from)
        self.is_click(user['JS_Data'], choice=recevied_from)  # 选择客户类型
        self.driver.execute_script("document.documentElement.scrollTop=900")
        self.is_click(user["JS_Info"], "customerName")
        self.input_text(user['JS_Info'], txt=customer_name, choice="customerName")  # 输入客户姓名
        self.is_click(user['JS_Info'], "regionSelected")
        self.input_text(user['JS_Info'], txt=country, choice="regionSelected")  # 添加页面输入客户国家
        self.hover(user['Region_Data'], country)
        self.is_click(user['Region_Data'], country)
        self.is_click(user['JS_Info'], "mobileNo")
        self.input_text(user['JS_Info'], txt=mobile_area, choice="mobileNo")  # 添加页面输入客户电话区号
        self.hover(user['JS_Data'], choice=mobile_area)
        self.is_click(user['JS_Data'], choice=mobile_area)
        self.input_text(user['Mobile_No'], txt=mobile_no)  # 输入客户电话号码

    @allure.step("添加JS,切换页签")
    def Add_JS_Change_Tab(self, tab):
        self.driver.execute_script("document.documentElement.scrollTop=100")
        self.is_click(user['JS_Add_Tab'], choice=tab)


    @allure.step("添加JS,输入报价信息")
    def Add_JS_Quote_Info(self, approval_status, service_type, material, symptom):
        self.is_click(user['JS_Info'], choice="approvalStatus")
        self.hover(user['JS_From_Data'], choice=approval_status)
        self.is_click(user['JS_From_Data'], choice=approval_status)  # 选择报价状态
        self.is_click(user['JS_Info'], choice="typeName")
        self.hover(user['JS_From_Data'], choice=service_type)
        self.is_click(user['JS_From_Data'], choice=service_type)  # 选择报价类型
        self.is_click(user['JS_Info'], choice="selectMaterial")
        self.input_text(user['JS_Info'], txt=material, choice="selectMaterial")
        self.hover(user['JS_Data'], choice=material)
        self.is_click(user['JS_Data'], choice=material)  # 选择物料组
        self.is_click(user['JS_Info'], choice="symptomId")
        self.input_text(user['JS_Info'], txt=symptom, choice="symptomId")
        self.hover(user['JS_Data'], choice=symptom)
        self.is_click(user['JS_Data'], choice=symptom)  # 选择现象组
        self.is_click(user['JS_Info'], choice="faultId")
        self.input_text(user['JS_Info'], txt=symptom, choice="faultId")  #
        self.hover(user['JS_Data'], choice=symptom)
        self.is_click(user['JS_Data'], choice=symptom)  # 选择手机问题
        self.is_click(user['JS_From_Data'], choice="Add To List")  # 加入列表









    @allure.step("save&add添加JS")
    def SaveAdd_Symp_Code(self, code, grouping, description):
        self.is_click(user['Symptom_Code_Add'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Add"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        self.input_text(user['Symptom_Code_Input'], txt=code, choice='symptomCode')  # 添加页面输入JSCode
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


    @allure.step("重复添加JS")
    def Repeat_Add_Code(self, code, grouping, description):
        self.is_click(user['Symptom_Code_Add'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Add"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        self.input_text(user['Symptom_Code_Input'], txt=code, choice='symptomCode')  # 添加页面输入JSCode
        self.is_click(user['Symptom_Code_Input'], choice='symptomGroupId')
        self.input_text(user['Symptom_Code_Input'], txt=grouping, choice='symptomGroupId')  # 添加页面输入grouping
        self.hover(user['Symptom_Grouping_Select'], choice=grouping)
        self.is_click(user['Symptom_Grouping_Select'], choice=grouping)
        self.input_text(user['Symptom_Code_Input'], txt=description, choice='description')  # 添加页面输入描述
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Save"]), message='save未出现')  # 显示等待页面加载成功
        self.is_click(user['Symptom_Code_Save'])
        name_repeat_tip = self.element_text(user['Already_Exits'])
        return name_repeat_tip

    @allure.step("添加JS未save")
    def Add_Symp_Code_Not_Save(self, code, grouping, description):
        self.is_click(user['Symptom_Code_Add'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Add"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        self.input_text(user['Symptom_Code_Input'], txt=code, choice='symptomCode')  # 添加页面输入JSCode
        self.is_click(user['Symptom_Code_Input'], choice='symptomGroupId')
        self.input_text(user['Symptom_Code_Input'], txt=grouping, choice='symptomGroupId')  # 添加页面输入grouping
        self.hover(user['Symptom_Grouping_Select'], choice=grouping)
        self.is_click(user['Symptom_Grouping_Select'], choice=grouping)
        self.input_text(user['Symptom_Code_Input'], txt=description, choice='description')  # 添加页面输入描述
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Save"]), message='save未出现')  # 显示等待页面加载成功


    @allure.step("添加JS界面获取现象组")
    def Add_Interface_Grouping(self, grouping):
        self.is_click(user['Symptom_Code_Add'])
        self.wait.until(EC.presence_of_element_located(user["Symptom_Code_Add"]), message='添加页面加载不成功')  # 显示等待页面加载成功
        self.is_click(user['Symptom_Code_Input'], choice='symptomGroupId')
        self.input_text(user['Symptom_Code_Input'], txt=grouping, choice='symptomGroupId')  # 添加页面输入grouping
        self.hover(user['Symptom_Grouping_Select'], choice=grouping)
        grouping_name = self.element_text(user['Symptom_Grouping_Select'], choice=grouping)
        self.is_click(user['Symptom_Grouping_Select'], choice=grouping)
        return grouping_name

    @allure.step("添加JS界面获取现象组")
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

    @allure.step("关闭JS添加或编辑界面")
    def Close_Symp(self, operation):
        self.is_click(user['Close_Button'], choice=operation)
        self.is_click(user['Close_Confirm'])

    @allure.step("关闭JS空白添加界面")
    def Close_Code(self, operation):
        self.is_click(user['Close_Button'], choice=operation)

    @allure.step("清空JS查询框，恢复查询条件为默认值")
    def Code_Clear_Get(self):
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Status'], choice="Enable")  # 将状态查询框恢复为默认Enable
        try:
            self.is_click(user['Input_Exact_Word'])
            self.hover(user['Input_Clear'])
            self.is_click(user['Input_Clear'])  # 将JS名称查询框清空
        except:
            logging.info("搜索框无数据")

    @allure.step("清空查询框，恢复查询条件为默认值")
    def Clear_Get(self):
        self.refresh()



    @allure.step("JS页面，清空查询条件")
    def JS_Clear_Query_Conditions(self):
        self.is_click(user['Created_Date_Input'], choice="Start Date")
        self.hover(user['Created_Date_Clear'], choice="Start Date")
        self.is_click(user['Created_Date_Clear'], choice="Start Date")  # 清空时间查询条件
        self.is_click(user['Hide_Return'])  # 取消隐藏100状态的
        self.is_click(user['Scope_Select'], choice="scopeType")
        self.is_click(user['Scope_Select_Data'], choice="All")  # 设置范围为所有

    @allure.step("产生新窗口时切换回原窗口")
    def Swith_Original_Window(self):
        self.driver.switch_to.window((self.driver.window_handles[-1]))
        #self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        logging.info("回到原窗口")


    @allure.step("默认条件查询JS，返回查询到的JS名称")
    def Search_JS(self):
        self.wait.until(EC.presence_of_element_located(user["Search_Button"]), message='界面加载不成功')
        self.is_click(user['Search_Button'])

    @allure.step("获取查询到的最新JS数据")
    def Get_New_JS(self):
        imei = self.element_text(user['JS_List_Data'], "1", "el-table_3_column_21")
        customer_name = self.element_text(user['JS_List_Data'], "1", "el-table_3_column_17")
        warranty_status = self.element_text(user["JS_List_Data"], "1", "el-table_3_column_13")
        js_no = self.element_text(user['JS_NO'], "1", "el-table_3_column_7")
        return imei, customer_name, js_no, warranty_status

    @allure.step("获取查询到的JS的状态和类型")
    def Get_JS_Status_Type(self):
        document_status = self.element_text(user['JS_List_Data'], "1", "el-table_3_column_8")
        serivice_type = self.element_text(user['JS_List_Data'], "1", "el-table_3_column_12")
        return document_status, serivice_type


    @allure.step("JS页面，随机获取一个JS NO")
    def Get_JS_No(self, i):
        js_no = self.element_text(user['JS_NO'], i, "el-table_3_column_7")
        return js_no

    @allure.step("JS页面，Exact Word查询")
    def Get_Exact_Word_JS(self, js_no):
        self.is_click(user['JS_Info'], "keyword")
        self.input_text(user['JS_Info'], txt=js_no, choice="keyword")
        self.is_click(user['Search_Button'])
        get_js_no = self.element_text(user['JS_NO'], "1", "el-table_3_column_7")
        return get_js_no

    @allure.step("JS页面，Created On查询")
    def Get_Created_On_JS(self, date):
        self.is_click(user['Start_Date'])
        self.is_click(user['Start_Date_Month'])
        self.is_click(user['Start_Date_Day'], date)

    @allure.step("JS页面，Document Status下拉框查询")
    def Get_Document_Status_JS(self, status):
        self.is_click(user['Document_Status_Input'])
        self.input_text(user['Document_Status_Input'], txt=status)
        self.hover(user['Status_Select'], choice=status)
        self.is_click(user['Status_Select'], choice=status)
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Data_Total'])
        num = get_total.split(" ", 1)
        number = int(num[1])
        if number == 0:
            logging.info("查询无数据")
        else:
            self.scroll_into_view_CRM(user['Page_Num'])
            th_num = self.elements_num(user['Document_Data_Num'])
            for i in range(1, th_num+1):
                txt = self.element_text(user['Search_Data'], f'{i}')
                logging.info(txt)
                ValueAssert.value_assert_In(status, txt)
            self.refresh()
        return number



    @allure.step("JS页面，Shorage Status下拉框查询")
    def Get_Shortage_Status_JS(self, status):
        self.is_click(user['Status_Input'], choice="Shortage Status")
        self.input_text(user['Status_Input'], txt=status, choice="Shortage Status")
        self.hover(user['Status_Select'], choice=status)
        self.is_click(user['Status_Select'], choice=status)
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Data_Total'])
        num = get_total.split(" ", 1)
        number = int(num[1])
        if number == 0:
            logging.info("查询无数据")
        else:
            self.scroll_into_view_CRM(user['Page_Num'])
            th_num = self.elements_num(user['Shortage_Data_Num'])
            for i in range(1, th_num+1):
                txt = self.element_text(user['Search_Shortage_Data'], f'{i}')
                logging.info(txt)
                ValueAssert.value_assert_In(status, txt)
            self.refresh()
        return number

    @allure.step("JS页面，Service Type下拉框查询")
    def Get_Service_Status_JS(self, status):
        self.is_click(user['Status_Input'], choice="Service Type")
        self.input_text(user['Status_Input'], txt=status, choice="Service Type")
        self.hover(user['Status_Select'], choice=status)
        self.is_click(user['Status_Select'], choice=status)
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Data_Total'])
        num = get_total.split(" ", 1)
        number = int(num[1])
        if number == 0:
            logging.info("查询无数据")
        else:
            self.scroll_into_view_CRM(user['Page_Num'])
            th_num = self.elements_num(user['Service_Data_Num'])
            for i in range(1, th_num+1):
                txt = self.element_text(user['Service_Shortage_Data'], f'{i}')
                logging.info(txt)
                ValueAssert.value_assert_In(status, txt)
            self.refresh()
        return number

    @allure.step("JS页面，Quote Status下拉框查询")
    def Get_Quote_Status_JS(self, status):
        self.is_click(user['Status_Input'], choice="Quote Status")
        self.input_text(user['Status_Input'], txt=status, choice="Quote Status")
        self.hover(user['Status_Select'], choice=status)
        self.is_click(user['Status_Select'], choice=status)
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Data_Total'])
        num = get_total.split(" ", 1)
        number = int(num[1])
        return number


    @allure.step("JS的Scope查询")
    def Get_Scope_JS(self, condition, data):
        self.is_click(user['Scope_Select'], choice=condition)
        self.input_text(user['Scope_Select'], choice=condition, txt=data)
        self.hover(user['Status_Select'], choice=data)
        self.is_click(user['Status_Select'], choice=data)
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Data_Total'])
        num = get_total.split(" ", 1)
        number = int(num[1])

        if number == 0:
            logging.info("查询无数据")
        else:
            self.scroll_into_view_CRM(user['Page_Num'])
            th_num = self.elements_num(user['Scope_Data_Num'])
            # onload = "document.body.scrollWidth,0"
            # self.driver.execute_script(onload)
            list1 = []
            for i in range(1, th_num + 1):
                logging.info(f'{i}')
                txt = self.element_text(user['Current_Page_data'], f'{i}')
                logging.info(txt)
                list1.append(txt)
                logging.info(list1)
            self.refresh()
            return number, th_num, list1

    def Get_IsEcalate_JS(self, data):
        self.is_click(user['Scope_Select'], choice="isEscalate")
        self.input_text(user['Scope_Select'], txt=data, choice="isEscalate")
        self.hover(user['Is_Query_Select'], choice=data)
        self.is_click(user['Is_Query_Select'], choice=data)
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Data_Total'])
        num = get_total.split(" ", 1)
        number = int(num[1])

        if number == 0:
            logging.info("查询无数据")
        else:
            self.scroll_into_view_CRM(user['Page_Num'])
            th_num = self.elements_num(user['Ecalate_Data_Num'])
            # onload = "document.body.scrollWidth,0"
            # self.driver.execute_script(onload)
            list1 = []
            for i in range(1, th_num + 1):
                logging.info(f'{i}')
                txt = self.element_text(user['Current_Ecalate_data'], f'{i}')
                logging.info(txt)
                list1.append(txt)
                logging.info(list1)
            self.refresh()
            return number, th_num, list1

    def Get_IsQuickRepair_JS(self, data):
        self.is_click(user['Scope_Select'], choice="isQuickRepair")
        self.input_text(user['Scope_Select'], choice="isQuickRepair", txt=data)
        self.hover(user['Is_Query_Select'], choice=data)
        self.is_click(user['Is_Query_Select'], choice=data)
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Data_Total'])
        num = get_total.split(" ", 1)
        number = int(num[1])

        if number == 0:
            logging.info("查询无数据")
        else:
            self.scroll_into_view_CRM(user['Page_Num'])
            th_num = self.elements_num(user['QuickRepair_Data_Num'])
            # onload = "document.body.scrollWidth,0"
            # self.driver.execute_script(onload)
            list1 = []
            for i in range(1, th_num + 1):
                logging.info(f'{i}')
                txt = self.element_text(user['Current_QuickRepair_data'], f'{i}')
                logging.info(txt)
                list1.append(txt)
                logging.info(list1)
            self.refresh()
            return number, th_num, list1

    def Get_Warranty_JS(self, data):
        self.is_click(user['Scope_Select'], choice="warrantyStatus")
        self.input_text(user['Scope_Select'], choice="warrantyStatus", txt=data)
        self.hover(user['Is_Query_Select'], choice=data)
        self.is_click(user['Is_Query_Select'], choice=data)
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Data_Total'])
        num = get_total.split(" ", 1)
        number = int(num[1])

        if number == 0:
            logging.info("查询无数据")
        else:
            self.scroll_into_view_CRM(user['Page_Num'])
            th_num = self.elements_num(user['Warranty_Data_Num'])
            # onload = "document.body.scrollWidth,0"
            # self.driver.execute_script(onload)
            list1 = []
            for i in range(1, th_num + 1):
                logging.info(f'{i}')
                txt = self.element_text(user['Current_Warranty_data'], f'{i}')
                logging.info(txt)
                list1.append(txt)
                logging.info(list1)
            self.refresh()
            return number, th_num, list1


    @allure.step("查询JS，无数据返回")
    def Get_No_Data(self, name):
        self.input_text(user['Input_Exact_Word'], txt=name)
        self.is_click(user['Search_Button'])
        get_record = self.element_text(user['Get_No_Data'], 'No Data')
        return get_record


    @allure.step("查询JS，返回查询到的JS人、时间")
    def Get_Code_DATE_BY(self, name):
        self.input_text(user['Input_Exact_Word'], txt=name)
        self.is_click(user['Search_Button'])
        created_date = self.element_text(user['List_Tr1_Td'], "6")
        created_by = self.element_text(user['List_Tr1_Td'], "7")
        modified_on = self.element_text(user['List_Tr1_Td'], "8")
        modified_by = self.element_text(user['List_Tr1_Td'], "9")
        return created_date, created_by, modified_on, modified_by

    @allure.step("Status Enable查询JS")
    def Get_Status_Code(self, status):
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Status'], status)  # 选择状态查询
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Symptom_Total'])
        num = get_total.split(" ", 1)
        number = int(num[1])
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
        # 验证随机页码里的JS状态正确
        th_num = self.elements_num(user['Current_Status_Num'])  # 获取当前页码上JS个数
        list1 = []
        for i in range(1, th_num + 1):
                logging.info(f'{i}')
                txt = self.element_text(user['Current_Page_Staus'], f'{i}')
                logging.info(txt)
                list1.append(txt)
                logging.info(list1)
        self.refresh()
        return number, th_num, list1

    @allure.step("现象组查询框查询JS功能")
    def Group_Get_Code(self, grouping):
        self.is_click(user['Input_Grouping'])
        self.input_text(user['Input_Grouping'], txt=grouping)  # 添加页面输入grouping
        self.hover(user['Symptom_Grouping_Select'], choice=grouping)
        self.is_click(user['Symptom_Grouping_Select'], choice=grouping)
        self.is_click(user['Search_Button'])
        get_record_code = self.element_text(user['Search_Data_name_tr1'], '3')
        get_record_group = self.element_text(user['Search_Data_name_tr1'], '5')
        get_record_description = self.element_text(user['Search_Data_name_tr1'], '4')
        return get_record_code, get_record_group, get_record_description


    @allure.step("跳转页码")
    def input_page_code(self, num):
        self.input_text(user['Page_Input'], txt=num)  # 随机输入页码跳转
        self.send_enter()
    @allure.step("Status Disable查询JS")
    def Get_Disable_Status_Code(self, status):
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Arrow'])
        self.is_click(user['Search_Status'], choice=status)
        self.is_click(user['Search_Button'])
        get_total = self.element_text(user['Symptom_Total'])
        num = get_total.split(" ", 1)
        number = int(num[1])
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
    #     number = int(num[1])
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

    @allure.step("更改JS状态")   # 需要加个判断
    def Edit_Code_Status(self, status):
        self.is_click(user['Status_Button'], choice=status)
        self.is_click(user["Edit_Status_Yes"])
        self.wait.until(EC.presence_of_element_located(user["Search_Button"]), message='数据加载不成功')  # 显示等待数据加载成功

    @allure.step("JS保内工单报价物料类型")
    def Qte_20_Status(self, material, qty, symptom, fault):
        self.is_click(user['JS_Info'], choice='approvalStatus')  # 报价状态选择20
        self.hover(user['Qte_Select'], choice="20-Estimation Approved")
        self.is_click(user['Qte_Select'], choice="20-Estimation Approved")
        self.is_click(user['JS_Info'], choice='typeName')  # 选择报价类型
        self.hover(user['Qte_Select_Type'], choice="Material")
        self.is_click(user['Qte_Select_Type'], choice="Material")
        self.is_click(user['JS_Info'], choice='selectMaterial')  # 选择物料组
        self.input_text(user['JS_Info'], choice='selectMaterial', txt=material)  # 输入物料组
        self.hover(user['Qte_Select_Type'], choice=material)
        self.is_click(user['Qte_Select_Type'], choice=material)
        self.is_click(user['JS_Info'], choice='qty')  #
        self.input_text(user['JS_Info'], choice='qty', txt=qty)  # 输入物料数量
        self.is_click(user['JS_Info'], choice='symptomId')  # 选择现象码
        self.input_text(user['JS_Info'], choice='symptomId', txt=symptom)
        self.hover(user['Qte_Select_Type'], choice=symptom)
        self.is_click(user['Qte_Select_Type'], choice=symptom)
        self.is_click(user['JS_Info'], choice='faultId')  # 选择错误码
       # self.input_text(user['JS_Info'], choice='faultId', txt=fault)
        self.hover(user['Qte_Select_Type'], choice=fault)
        self.is_click(user['Qte_Select_Type'], choice=fault)
        self.is_click(user['Qte_Select'], choice="Enable")  # 点击enable
        self.driver.execute_script("document.documentElement.scrollTop=800")

    @allure.step("JS保外工单报价物料类型")
    def Qte_Out_JS(self, grade,material, qty, symptom, fault):
        self.is_click(user['JS_Info'], choice='approvalStatus')  # 报价状态选择20
        self.hover(user['Qte_Select'], choice="20-Estimation Approved")
        self.is_click(user['Qte_Select'], choice="20-Estimation Approved")
        self.is_click(user['JS_Info'], choice='typeName')  # 选择报价类型
        self.hover(user['Qte_Select_Type'], choice="Material")
        self.is_click(user['Qte_Select_Type'], choice="Material")
        self.is_click(user['Status_Input'], choice='Material Grade')  # 选择物料等级
        self.input_text(user['Status_Input'], choice='Material Grade', txt=grade)  # 输入物料等级
        self.hover(user['Qte_Select_Type'], choice=grade+"-"+grade)
        self.is_click(user['Qte_Select_Type'], choice=grade+"-"+grade)
        self.is_click(user['JS_Info'], choice='selectMaterial')  # 选择物料组
        self.input_text(user['JS_Info'], choice='selectMaterial', txt=material)  # 输入物料组
        self.hover(user['Qte_Select_Type'], choice=material)
        self.is_click(user['Qte_Select_Type'], choice=material)
        self.is_click(user['JS_Info'], choice='qty')  #
        self.input_text(user['JS_Info'], choice='qty', txt=qty)  # 输入物料数量
        self.is_click(user['JS_Info'], choice='symptomId')  # 选择现象码
        self.input_text(user['JS_Info'], choice='symptomId', txt=symptom)
        self.hover(user['Qte_Select_Type'], choice=symptom)
        self.is_click(user['Qte_Select_Type'], choice=symptom)
        self.is_click(user['JS_Info'], choice='faultId')  # 选择错误码
       # self.input_text(user['JS_Info'], choice='faultId', txt=fault)
        self.hover(user['Qte_Select_Type'], choice=fault)
        self.is_click(user['Qte_Select_Type'], choice=fault)
        self.is_click(user['Qte_Select'], choice="Enable")  # 点击enable
        self.driver.execute_script("document.documentElement.scrollTop=800")

    @allure.step("新建JS，返回报价列表数据")
    def Get_Quote_List_DATA(self):
        item = self.element_text(user['Qte_List'], "3")
        material_group = self.element_text(user['Qte_List'], "4")
        sleep(3)
        qty_num = self.element_text(user['Qte_List'], "8")
        vat = self.element_text(user['Qte_List'], "12")
        tax_amt = self.element_text(user['Qte_List'], "13")
        est_amt = self.element_text(user['Qte_List'], "14")
        return item, material_group, qty_num, vat, tax_amt, est_amt










    @allure.step("导出JS")
    def Export_Symp(self):
        self.is_click(user['Symptom_Export'])
        self.is_click(user['Export_OK'])

if __name__ == '__main__':
    pass
