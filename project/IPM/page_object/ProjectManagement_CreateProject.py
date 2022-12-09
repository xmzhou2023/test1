'''项目管理-创建项目'''

from project.IPM.page_base.basics_IPM import PubicMethod
from libs.common.time_ui import *
from project.IPM.page_base.assert_pubic import *
from project.IPM.api.APIRequest import *

Api = APIRequest()
# ApplyList=Api.Api_applyList(20220810085734677324)
# Api.Api_queryDeptAndEmployee(20220810085734677324)
def field_attribute_maintennance(self):
    field_att = Api.Api_project_field("开模流程测试")

now_times = strftime('%Y-%m-%d%H:%M:%S')
now_t = strftime('%Y-%m-%d')
time_ipm=f'ipm自动化{now_times}'
class CreateProject(PubicMethod):

    def __init__(self,driver,element_yaml='ProjectManagement_CreateProject',expect='ProjectManagement_CreateProject.yaml'):
        super().__init__(driver, element_yaml,expect=expect)

    def get_url_project(self):
        self.get_url("http://ipm-uat.transsion.com/#/project-manage")
        sleep(2)
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


    def projecy_cancel(self):
        '''取消'''
        self.click_IPM('取消')

    def click_project_entrance(self,projectname):
        '''点击卡片进入项目'''
        self.click_IPM('进入项目',projectname)

    def click_project_entrance_ch(self,projectname):
        '''点击...展开编辑/删除按钮'''
        self.mouse_hover_IPM('卡片展开按钮',projectname)

    def entrance_ch(self,):
        '''项目编辑按钮'''
        self.click_IPM('项目编辑按钮')

    def click_edit(self):
        '''编辑'''
        self.click_IPM('编辑')

    def perject_field_editing_save(self):

        '''基本信息编辑保存'''
        self.click_IPM('基本信息保存')

    def Start_project(self):
        '''启动项目'''
        self.click_IPM('启动项目')

    def Get_required_fields(self,proname,protime):
        '''
        获取项目管理字段获取

        '''
        Api = APIRequest()
        field_att = Api.Api_project_field(proname)
        for i in field_att:
            if i.get("是否展示") == True:
                if i.get("是否可读") == False:
                    if i.get("是否必填") == True:
                        if i.get("类型") == 'text':
                            if i.get("文本类型") == '1':
                                self.input_text_IPM('字段名称', text=1, choice=i.get("字段名"))
                                sleep(1)
                            else:
                                self.input_text_IPM('字段名称', text=f'{i.get("字段名")}{protime}', choice=i.get("字段名"))
                                sleep(1)
                        if i.get("类型") == 'select':
                            self.click_IPM('字段名称',choice=i.get("字段名"))
                            self.click_IPM('下拉框')
                            sleep(1)

                        if i.get("类型") == 'date':
                            self.input_text_IPM('字段名称', text=now_t, choice=i.get("字段名"))
                            sleep(1)
                    else:
                        if i.get("类型") == 'text':
                            if i.get("文本类型") == '1':
                                self.input_text_IPM('字段名称', text=1, choice=i.get("字段名"))
                                sleep(1)
                            else:
                                self.input_text_IPM('字段名称', text=f'{i.get("字段名")}{protime}', choice=i.get("字段名"))
                                sleep(1)
                            sleep(1)
                        if i.get("类型") == 'select':
                            self.click_IPM('字段名称', choice=i.get("字段名"))
                            self.click_IPM('下拉框')
                            sleep(1)

                        if i.get("类型") == 'date':
                            self.input_text_IPM('字段名称', text=now_t, choice=i.get("字段名"))
                            sleep(1)

    def Create_project(self, Save_or_Cancel, templatename=None, nametext=None, Descriptiontext=None):
        """
        创建项目
        :param templatename: 选择对应的项目模板名字
        :param nametext: 项目名称
        :param Descriptiontext: 项目描述
        :param Save_or_Cancel: 保存还是取消
        """

        self.click_project()
        self.click_add()
        if templatename != None:
            self.Select_Template(templatename)
        if nametext != None:
            self.projecy_name(nametext)
        if Descriptiontext != None:
            self.projecy_Description(Descriptiontext)
        if Save_or_Cancel == '保存':
            self.projecy_preservation()
        else:
            self.projecy_cancel()
        sleep(2)

    def enter_the_project(self,projectname):
        '''点击卡片进入项目详情'''
        self.click_project_entrance(projectname)
        sleep(1)
        self.switch_window(-1)

    def Click_the_button_to_enter(self,projectname):
        '''点击按钮进入进入项目详情'''
        self.click_project_entrance_ch(projectname)
        self.entrance_ch()
        sleep(1)
        self.switch_window(-1)
        sleep(3)

    def project_entrance(self,projectname,protime):
        '''
        编辑项目-保存

        '''
        self.enter_the_project(projectname)
        sleep(5)
        self.click_edit()
        sleep(1)
        self.Get_required_fields(projectname,protime)
        self.perject_field_editing_save()


    def field_attribute_maintennance(self):
        field_att=Api.Api_project_field("开模流程测试")



    def perject_field_editing(self,proname,protime):
        '''
        项目管理编辑页面字段维护
        '''

        self.Get_required_fields(proname,protime)



#断言
class Assert_result(AssertMode):
    def __init__(self,driver,element_yaml='ProjectManagement_CreateProject', expect='ProjectManagement_CreateProject.yaml'):
        super().__init__(driver, element_yaml,expect=expect)

    def assert_Create_project(self,actual,Expected):
        self.assert_element_equal(actual,Expected)




