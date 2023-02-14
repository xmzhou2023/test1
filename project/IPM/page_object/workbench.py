'''工作台'''
import logging

from project.IPM.page_base.basics_IPM import PubicMethod
from libs.common.time_ui import *
from project.IPM.page_base.assert_pubic import *
from project.IPM.api.APIRequest import *
import random
from project.IPM.page_object.ipm_publiclibrary import *
from project.IPM.page_object.ApplicationCenter import ApplicationCenter



now_times = strftime('%Y-%m-%d%H:%M:%S')
now_t = strftime('%Y-%m-%d')
time_ipm=f'ipm自动化{now_times}'

class WorkBench(ipm_publiclibrary):
    def __init__(self,driver,env_name,element_yaml='workbench',expect='workbench.yaml'):
        super().__init__(driver, element_yaml,expect=expect)
        self.Api = APIRequest(env_name)
        self.ini = ReadConfig(pro_name, env_name)

        self.Api = APIRequest(env_name)
    def get_url_workbench(self):
        self.get_url(f"{self.ini._get('HOST', 'url_ipm')}/#/panel")
        sleep(2)

    @allure.step("工作台_筛选")
    def workbench_tap_choice_find(self,Workbench_filtering,Text,OKResetCancel=None):
        '''
        工作台_筛选功能
        :param Workbench_filtering: 传入查询条件
        :param Text: 根据查询条件传入，如文本框，则输入文本，人员框则输入工号或姓名，下拉框则输入下拉框的值
        '''
        sleep(1)
        ele_not=self.element_exist_IPM('工作台_筛选_过滤标题')
        if ele_not ==False:
            self.click_IPM('工作台_筛选')
        if Workbench_filtering == '标题' or Workbench_filtering == '流程编码':
            self.input_text_IPM('工作台_筛选_条件',Text,Workbench_filtering)
        elif Workbench_filtering == '申请人' or Workbench_filtering == '审批人':
            self.click_IPM('工作台_筛选_条件',Workbench_filtering)
            self.personnel_list(Text)
        elif Workbench_filtering == '状态':
            self.DropDownBox('工作台_筛选_字段',Workbench_filtering,'工作台_筛选_条件_状态',Text)
        else:
            logging.info('{}在工作台_筛选功能中不存在，请传入正确的查询条件'.format(Workbench_filtering))
            raise ValueError('{}在工作台_筛选功能中不存在，请传入正确的查询条件'.format(Workbench_filtering))
        if OKResetCancel == '确定' or OKResetCancel == '重置' or OKResetCancel == '删除':
            self.click_IPM('工作台_筛选_按钮',OKResetCancel)
        elif OKResetCancel ==None:
            logging.info('工作台_筛选_按钮中为空，不需要做任何操作')
        else:
            logging.info('工作台_筛选_按钮中{}功能键不存在，请输入存在的功能键'.format(OKResetCancel))
            raise ValueError('工作台_筛选_按钮中{}功能键不存在，请输入存在的功能键'.format(OKResetCancel))











    @allure.step("工作台_tap")
    def workbench_tap_choice(self,tabname):
        '''
        选择模板
        :param tabname：tap名字，如（我参与的任务，流程任务，我的TR，风险等）
        '''
        self.click_IPM('span',tabname)
        # if tabname =='我参与的任务':
        #     pass
        # if tabname =='流程任务':
        #     pass
        #
        # if tabname =='我的TR':
        #     pass
        #
        # if  tabname =='风险':
        #     pass
        #
        # if  tabname =='问题':
        #     pass
        #
        # if  tabname =='交付物':
        #     pass
        #
        # if  tabname =='硬件测试':
        #     pass
        #
        # if  tabname =='软件任务':
        #     pass
        #
        # sleep(1)