'''
# -*- coding: utf-8 -*-
# @Time : 2022/6/20 14:00
# @Author : 李小素
# @File :
# @Software: PyCharm
# @project: 流程配置
'''

from project.IPM.page_object.home import ProcessHome
from project.IPM.page_object.Center_Component import *
from project.IPM.page_object.Center_Personal import *


class FlowLayout():

    def click_home(self,drivers):
        '''进入流程配置'''
        home = ProcessHome(filename='public_method', driver=drivers)
        home.click_home(public='span', title='系统管理')
        sleep(1)
        home.click_home(public='span', title='流程配置')


#节点管理
class RoleManagement(PubicMethod):
    def __init__(self, driver, element_yaml='AsystemManagement_FlowConfig', expect='AsystemManagement_FlowConfig.yaml'):
        super().__init__(driver, element_yaml,expect=expect)


    def url_RoleManagent(self):
        '''跳转地址'''
        self.get_url_f(url='流程配置URL')

    def add_RoleManagent(self):
        '''新增'''
        self.rop_down_box('新增')

    def Edit_RoleManagent(self,chioce="0"):
        '''编辑'''
        self.rop_down_box(click_choice='编辑', chioce=chioce)

    def Preservation_RoleManagent(self):
        '''保存'''
        self.rop_down_box('span', '保存')

    def delete_RoleManagent(self,chioce):
        '''删除'''
        '''
        @ chioce:行数
        '''
        self.rop_down_box(click_choice='删除', chioce=chioce)

    def sort_RoleManagent(self,choice,text):
        '''排序'''
        '''
        @ choice:行数
        @ text：输入文本
        '''
        self.input_texts(elements='排序', choice=choice, text=text)

    def state_RoleManagent(self):
        '''状态修改'''
        self.rop_down_box(click_choice='状态修改')

    def cancek_RoleManagent(self):
        '''点击取消'''
        self.rop_down_box(click_choice='点击取消')

    def cinfirm_RoleManagent(self):
        '''点击确认'''
        self.rop_down_box(click_choice='点击确定')

    def NodeName_RoleManagent(self,Number,text):
        '''节点名称选择'''
        '''
        @ Number:行数
        @ text:节点名称
        '''
        self.click_choices(inputelemet='节点名称',
                          Field_name=Number,
                          input_text=text,
                          click_choice='下拉框选择',
                          choice_text=text)

    def NodeRole_RoleManagent(self,Number,text):
        '''节点角色选择'''
        '''        
        @ Number:行数
        @ text:节点角色
        '''
        self.click_choices(inputelemet='节点角色',
                          Field_name=Number,
                          input_text=text,
                          click_choice='下拉框选择',
                          choice_text=text)

#角色管理
class RoleManagent(PubicMethod):
    def __init__(self, driver, element_yaml='AsystemManagement_FlowConfig',expect='AsystemManagement_FlowConfig.yaml'):
        super().__init__(driver, element_yaml,expect=expect)

    def url_RoleManagent(self):
        self.get_url_f(url='流程配置URL')


    def Role_Management(self):
        '''角色管理'''
        self.rop_down_box('角色管理')


    def RoleManagement_Query_material_type(self,*click_choice):
        '''角色管理物料类型查询'''
        try:
            if len(click_choice) == 0:
                pass
            elif len(click_choice) != 0:
                self.rop_down_box(click_choice='点击选择框')
                for idx, item in enumerate(click_choice):
                    self.rop_down_box(click_choice='选择', chioce=item)
        except:
            log.info('角色管理-物料类型查询存在异常')
            raise

    def RoleManagement_Query_Personnel(self,Personnel):
        '''角色管理人员查询'''
        self.input_texts(elements='人员',text=Personnel)

    def RoleManagement_Query(self):
        '''角色管理查询按钮'''
        self.rop_down_box('查询')

    def RoleManagement_Query_Reset(self):
        '''角色管理重置按钮'''
        self.rop_down_box('重置')

    def RoleManagement_Add(self):
        '''角色管理新增按钮'''
        self.rop_down_box('角色管理新增')

    def RoleManagement_Import(self):
        '''角色管理导入按钮'''
        self.rop_down_box('角色管理导入')

    def RoleManagement_Export(self):
        '''角色管理导出增按钮'''
        self.rop_down_box('角色管理导出')

    def RoleManagement_Edit(self):
        '''角色管理编辑按钮'''
        self.rop_down_box('角色管理编辑')

    def RoleManagement_Delete(self):
        '''角色管理删除按钮'''
        self.rop_down_box('角色管理删除')



#断言
class Assert_result(AssertMode):
    def __init__(self,driver,element_yaml='AsystemManagement_FlowConfig', expect='AsystemManagement_FlowConfig.yaml'):
        super().__init__(driver, element_yaml,expect=expect)

    def db_assert_elements_equal_Assert_result(self,actual_results,expected_results,listname):
        '''
                expected_results:表头预期结果
                actual_results：表头实际结果字段获取
                listname:列表名
                test:从数据库中查询出结果与页面表单结果对比
                '''
        self.db_assert_elements_equal(expected_results,
                                         listname,
                                         actual_results,
                                         db_ipm_config_uat)





















