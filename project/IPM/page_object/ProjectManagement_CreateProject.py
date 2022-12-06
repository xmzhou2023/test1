'''创建项目'''

from project.IPM.page_base.basics_IPM import PubicMethod
from libs.common.time_ui import *
from project.IPM.page_base.assert_pubic import *
now_times = strftime('%Y-%m-%d%H:%M:%S')
now_t = strftime('%Y-%m-%d')
time_ipm=f'ipm自动化{now_times}'
class CreateProject(PubicMethod):

    def __init__(self,driver,element_yaml='ProjectManagement_CreateProject',expect='ProjectManagement_CreateProject.yaml'):
        super().__init__(driver, element_yaml,expect=expect)


    def click_project(self):
        '''
        点击项目管理
        '''
        self.click_IPM('项目管理')
        sleep(2)

    def click_add(self):
        '''点击新增'''
        self.click_IPM('新增')
        sleep(2)

    def Select_Template(self,choice):
        '''
        选择模板
        :param choice：模板名字（IT项目模板，IT需求项目模板等）
        '''
        self.click_IPM('选择模板',choice=choice)
        sleep(2)

    def projecy_name(self,nametext):
        '''项目名字'''
        self.input_text_IPM('项目名称',nametext)
        sleep(2)

    def projecy_Description(self,Descriptiontext=None):
        '''项目描述'''
        self.input_text_IPM('项目描述',text=Descriptiontext)
        sleep(2)

    def projecy_preservation(self):
        '''保存'''
        self.click_IPM('保存')
        sleep(2)

    def projecy_cancel(self):
        '''取消'''
        self.click_IPM('取消')
        sleep(2)

    def Create_project(self,templatename,Save_or_Cancel,nametext,Descriptiontext=f'测试描述名称{now_time}'):
        self.click_project()
        self.click_add()
        self.Select_Template(templatename)
        self.projecy_name(nametext)
        self.projecy_Description(Descriptiontext)
        if Save_or_Cancel == '保存':
            self.projecy_preservation()
        else:
            self.projecy_cancel()
        sleep(2)


#断言
class Assert_result(AssertMode):
    def __init__(self,driver,element_yaml='ProjectManagement_CreateProject', expect='ProjectManagement_CreateProject.yaml'):
        super().__init__(driver, element_yaml,expect=expect)

    def assert_Create_project(self,projectname):
        print("预期结果",projectname)
        self.assert_element_equal('断言新建项目的名字',projectname)


