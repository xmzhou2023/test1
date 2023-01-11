'''工作台'''
import logging

from project.IPM.page_base.basics_IPM import PubicMethod
from libs.common.time_ui import *
from project.IPM.page_base.assert_pubic import *
from project.IPM.api.APIRequest import *
import random
from project.IPM.page_object.Generalmethods import General_methods
from project.IPM.page_base.import_ipm import *
from project.IPM.page_object.ApplicationCenter import ApplicationCenter
from project.IPM.page_base.pathconfig import *
Api = APIRequest()

now_times = strftime('%Y-%m-%d%H:%M:%S')
now_t = strftime('%Y-%m-%d')
time_ipm=f'ipm自动化{now_times}'

class SystemManagement(General_methods):
    def __init__(self,driver,element_yaml='system_management',expect='system_management.yaml'):
        super().__init__(driver, element_yaml,expect=expect)

    def get_url_system_management_object(self):
        self.get_url("http://ipm-uat.transsion.com/#/system-manage/object-manage")
        sleep(2)

    def system_management_object_all(self,objectaname,*levelname):
        '''
        系统管理_对象管理_树结构展开
        :param objectaname: 需要点击的对象名称
        :param levelname: 需要展开的对象名称
        '''
        if levelname:
            for i in levelname:
                self.click_IPM('对象_展开树结构',i)
        self.click_IPM('对象_点击对象名称',objectaname)
        sleep(2)
    def system_management_object_newbaseclass(self,baseclass,text=None):
        '''
        系统管理_对象管理_新建基类
        :param objectaname: 需要点击的对象名称
        :param levelname: 需要展开的对象名称
        '''
        if baseclass == "名称" or baseclass=='RootModel':
            self.input_text_IPM('对象_树结构_新建基类_输入框',text,baseclass)
        elif baseclass =='确认' or baseclass=='取消':
            self.click_IPM('对象_树结构_新建基类_功能键',baseclass)
        else:
            logging.info('{}不存在，请在system_management_object_newbaseclass中扩展'.format(baseclass))
            raise ValueError('{}不存在，请在system_management_object_newbaseclass中扩展'.format(baseclass))
        sleep(2)


    def system_management_object_upper_function(self,function,text=None):
        '''
        系统管理_对象管理_树结果上方功能
        :param function: 功能
        :param text: 文本
        '''
        if function == '新建' or function == '删除'or function == '搜索'or function == '上移'or function == '下移'or function == '收起'or function == '展开':

            self.click_IPM('对象_树结构_上方功能键',function)
            sleep(2)
        elif function == '查询':
            objectele = self.element_exist_IPM('对象_树结构_上方查询框')
            if objectele == True:
                self.input_text_IPM('对象_树结构_上方查询框',text)
            else:
                logging.info('当前没有找到查询功能，请点击搜索功能打开')
                raise ValueError(('当前没有找到查询功能，请点击搜索功能打开'))
        elif function == '清空':
            objectele = self.element_exist_IPM('对象_树结构_上方查询框')
            if objectele == True:
                self.mouse_hover_IPM('对象_树结构_上方查询框',text)
                self.click_IPM("对象_树结构_新建基类_清空查询")
            else:
                logging.info('当前没有找到查询功能，请点击搜索功能打开')
                raise ValueError(('当前没有找到查询功能，请点击搜索功能打开'))
        else:
            logging.info('{}不存在，请在system_management_object_upper_function中扩展'.format(function))
            raise ValueError('{}不存在，请在system_management_object_upper_function中扩展'.format(function))
        sleep(2)




    def system_management_object_drag_and_drop(self,start_name,end_name):
        '''
        系统管理_对象管理_对象拖拉拽
        :param start_name: 需要拉的对象
        :param end_name: 将元素拉到哪个元素
        '''
        self.drag_and_drop_ipm("对象_点击对象名称",start_name,end_name)

    def system_management_object_editobject(self, objectname):
        '''
        系统管理_对象管理_编辑对象名称
        :param objectname: 对象名称
        '''
        self.input_text_IPM('对象_编辑树结构文本',objectname)
        sleep(2)

    def system_management_object_righ(self,objectaname,righname,textname=None):
        '''
        系统管理_对象管理_右键点击
        :param objectaname: 需要点击的对象名称
        :param righname: 对象右键展开的功能键，如：新建/检出/删除
        :param textname: 根据新增或删除传入正确的参数，如righname传入新增，则传入对象名字，如righname传入删除，则传入确认或取消
        '''
        self.mouse_right_click_ipm('对象_点击对象名称',objectaname)
        if righname == '新建':#新增对象
            self.click_IPM('对象_右键点击对象',righname)
            if textname !=None:
                self.system_management_object_editobject(textname)
            elif textname ==None:
                return self.find_elemens_ipm_yaml_get_attribute('对象_编辑树结构文本')
        elif righname == '检出':#打开检入功能
            self.click_IPM('对象_右键点击对象', righname)
        elif righname == '删除':#删除对象
            self.click_IPM('对象_右键点击对象', righname)
            if textname =='确定' or textname =='取消' :
                self.click_IPM('对象_右键点击_删除_功能键', textname)
            elif textname ==None:
                logging.info('当前没传入值，页面停留在提示页面')
            else:
                logging.info('传入的参数不存在，清输入确定或取消')
                raise ValueError('传入的参数不存在，清输入确定或取消')
        else:
            logging.info('传入的参数不存在，清输入检入、检入、删除')
            raise ValueError('传入的参数不存在，清输入检入、检入、删除，如有新增功能键，则在system_management_object_righ中补充')

    def system_management_object_functionkeys_confirm_cancel(self,functionkeys,Objectsoperatedon=None):
        '''
        系统管理_对象管理_功能按钮
        :param functionkeys: 功能键
        :param Objectsoperatedon: 需要操作的对象名称
        '''
        if  Objectsoperatedon == '新增属性':
            self.click_IPM('对象_检入中_新增属性_功能键',Objectsoperatedon,functionkeys)
        elif Objectsoperatedon !=None:
            objectname = self.element_exist_IPM('对象_点击对象名称', Objectsoperatedon)
            if objectname == True:
                self.mouse_hover_IPM('对象_点击对象名称', Objectsoperatedon)
                objname = self.element_exist_IPM('对象_树结构_对象右侧功能键', functionkeys)
                if objname == True:
                    self.click_IPM('对象_树结构_对象右侧功能键', functionkeys)
                else:
                    self.click_IPM('对象_右键点击_删除_功能键', functionkeys)

        else:
            objname = self.element_exist_IPM('对象_树结构_对象右侧功能键', functionkeys)
            if objname == True:
                self.click_IPM('对象_树结构_对象右侧功能键', functionkeys)
            else:
                UndoCheckOut = self.element_exist_IPM('对象_撤销检出_功能键', functionkeys)#撤销检出提示
                if UndoCheckOut == True:
                    self.click_IPM('对象_撤销检出_功能键', functionkeys)
                else:
                    self.click_IPM('对象_右键点击_删除_功能键', functionkeys)



    def system_management_object_functionkeys(self,functionkeys,Objectsoperatedon=None,textname=None,Subobject=None):
        '''
        系统管理_对象管理_功能按钮
        :param functionkeys: 删除/新建/检出/检入/撤销检出/暂存/新增/新增权限
        :param Objectsoperatedon: 需要操作的对象名称,如果functionkeys传入的是新建/删除，则传入对象名称，如果functionkeys传入的是编辑权限，请传入表单行数
        :param textname: 根据新增或删除传入正确的参数，如righname传入新增，则传入对象名字，如righname传入删除，则传入确认或取消
        :param Subobject: 子对象
        '''
        if functionkeys =='新建' :#functionkeys传入删除/新建，则需要传入对象的名字，不然不会显示对象隐藏的功能键
            self.mouse_hover_IPM('对象_点击对象名称',Objectsoperatedon)
            self.click_IPM('对象_树结构_对象右侧功能键', Objectsoperatedon,functionkeys)
            if textname =='确定' or textname =='取消' :
                self.system_management_object_editobject(Subobject)
                self.system_management_object_functionkeys_confirm_cancel(textname,Subobject)
            elif textname ==None:
                logging.info('当前没传入值，页面停留在提示页面')
            else:
                logging.info('传入的参数不存在，清输入确定或取消')
                raise ValueError('传入的参数不存在，清输入确定或取消')
        elif functionkeys =='删除':#functionkeys传入删除/新建，则需要传入对象的名字，不然不会显示对象隐藏的功能键
            self.mouse_hover_IPM('对象_点击对象名称',Objectsoperatedon)
            self.click_IPM('对象_树结构_对象右侧功能键', Objectsoperatedon,functionkeys)
            if textname =='确定' or textname =='取消' :
                self.system_management_object_functionkeys_confirm_cancel(textname,Subobject)
        elif functionkeys =='检出' or functionkeys == '检入' or functionkeys == '撤销检出'or functionkeys == '暂存':
            objectele = self.element_exist_IPM('对象_页面属性刷新')
            if objectele ==True:
                 checkele= self.element_exist_IPM('对象_检入检出功能键',functionkeys)
                 if checkele == True:
                    self.click_IPM('对象_检入检出功能键',functionkeys)
                 elif checkele == False:
                     logging.info(f'对象已在检出中，请检出或撤销检出再检入')
                     raise ValueError(f'对象已在检出中，请检出或撤销检出再检入')
        elif functionkeys =='新增':
            self.click_IPM('对象_检入中_新增属性及约束')#点击新增按钮
        elif functionkeys == '确定' or functionkeys =='取消' :#如果functionkeys传入确定或者取消，则需要传入对象的名字，不然不会显示对象隐藏的功能键
            self.system_management_object_functionkeys_confirm_cancel(functionkeys, Objectsoperatedon)
        elif functionkeys == '新增权限':
            self.click_IPM('对象_表单功能_权限_新增权限')#点击权限_新增权限按钮
        elif functionkeys == '新增权限':
            self.click_IPM('对象_表单功能_权限_新增权限')#点击权限_新增权限按钮
        elif functionkeys == '编辑权限':
            self.mouse_double_click_ipm('对象_表单功能_权限_表单编辑',Objectsoperatedon)#点击权限_编辑权限按钮
        sleep(2)



    def system_management_object_newattribute(self,field,assemblyortext,typename=None):
        '''
        系统管理_对象管理_检入中_新增属性及约束
        :param field: 新增属性的字段
        :param assemblyortext: 组件或文本
        :param typename: 组件类型
        '''
        if field == '类型':
            self.click_IPM('对象_检入中_新增属性及约束_新增属性',field)
            self.mouse_hover_IPM("对象_检入中_新增属性及约束_新增属性_类型选择",assemblyortext)
            self.click_IPM("对象_检入中_新增属性及约束_新增属性_类型选择",typename)
        if field in  '属性名(innerName)' or field in  '字段释义(explain)' :
            self.input_text_IPM('对象_检入中_新增属性及约束_新增属性',assemblyortext,field)



    def system_management_object_permissions_formediting(self,fillin,*value):

        '''
        系统管理_对象管理_检入中_权限表单编辑
        :param fillin: 权限_功能
        :param value: 如果fillin传入生命周期状态，则是传入下拉框中的值，
                      如果fillin传入的思操作权限，则是操作权限的查看/创建/编辑/删除/提升等，
                      如果传入的是保存删除，则传入编辑的表单行数
        '''
        if value:
            for i in value:
                if fillin == '角色':
                    self.click_IPM('对象_表单功能_权限_角色修改')
                elif fillin=='生命周期状态':
                    self.click_IPM('对象_表单功能_权限_生命周期状态')
                    self.DropDownBoxAcquiredField(i)
                elif fillin=='操作权限':
                    self.click_IPM('对象_表单功能_权限_角色修改')
                    self.click_IPM('对象_表单功能_权限_操作权限')
                elif fillin == '保存':
                    self.click_IPM("对象_表单功能_权限_操作_保存",i)
                elif fillin == '删除':
                    self.click_IPM("对象_表单功能_权限_操作_删除",i)
                elif fillin == '继承':
                    self.click_IPM('对象_表单功能_权限_操作_继承',i)
                else:
                    logging.info(f'{fillin}在方法（system_management_object_permissions_formediting）中不存在，请扩展或填写正确的值')
                    raise ValueError(f'{fillin}在方法（system_management_object_permissions_formediting）中不存在，请扩展或填写正确的值')







    def system_management_object_jurisdiction(self):
        pass


    def system_management_object_configuration(self,function):
        '''
         系统管理_对象管理_表单功能点击（tab）
         :param function: 表单功能，如：属性及约束/生命周期/视图/权限
         '''
        objectele = self.element_exist_IPM('对象_页面属性刷新')
        if objectele == True:
            self.click_IPM('对象_表单功能',function)

    def system_management_object_selectpermissionrole(self, textname=None, query=None, confirm_or_cancel=None):
        '''
        系统管理_对象管理_权限/视图_选择权限角色
        :param field: 新增属性的字段
        :param assemblyortext: 组件或文本
        :param typename: 组件类型
        想要先模糊查询再点击可以参考：
                    test.system_management_object_selectpermissionrole('IT','查询')
                    test.system_management_object_selectpermissionrole('IT运维',confirm_or_cancel='确认')
        '''
        element_not=self.element_exist_IPM('对象_表单功能_视图_选择权限角色_查询输入框')
        if element_not ==True:
            if query == '查询':
                self.input_text_IPM('对象_表单功能_视图_选择权限角色_查询输入框', textname)
            elif query == None:
                if textname != None:
                    self.click_IPM('对象_表单功能_权限_选择权限角色_选择角色', textname)
                if confirm_or_cancel == '确定' or confirm_or_cancel == "取消":
                    self.click_IPM('对象_表单功能_选择权限角色_功能键', confirm_or_cancel)
                elif confirm_or_cancel == None:
                    logging.info('当前没传入值，跳过此环节')
                else:
                    logging.info(f'{confirm_or_cancel}请输入确定或取消')
                    raise ValueError(f'{confirm_or_cancel}请输入确定或取消')
        else:
            if query == '查询':
                self.input_text_IPM('对象_表单功能_权限_选择权限角色_查询输入框', textname)
            elif query == None:
                if textname != None:
                    self.click_IPM('对象_表单功能_权限_选择权限角色_选择角色', textname)

                if confirm_or_cancel == '确定' or confirm_or_cancel == "取消":
                    self.click_IPM('对象_表单功能_选择权限角色_功能键', confirm_or_cancel)
                elif confirm_or_cancel == None:
                    logging.info('当前没传入值，跳过此环节')
                else:
                    logging.info(f'{confirm_or_cancel}请输入确定或取消')
                    raise ValueError(f'{confirm_or_cancel}请输入确定或取消')

    def system_management_object_checkingin(self,field,SelectValue=None,functionkeys=None):
        '''
        系统管理_对象管理_基本信息检入中
        :param field: 基本信息功能按钮
        :param SelectValue: 文本或选择
        :param functionkeys: 功能键
        '''

        if field == '编码' or field == '对象名称' :
            self.input_text_IPM('对象_检入中_字段输入框',SelectValue,field)
        elif field == '状态':
            self.click_IPM('对象_检入中_状态修改',field)
            self.system_management_object_statusenableprompt(SelectValue)
        elif field == '说明':
            self.input_text_IPM('对象_检入中_说明输入框',SelectValue,field)
        elif field == '选择图标':#如果field等于选择图标，则打开选择图标窗口
            element_not = self.element_exist_IPM('对象_检入中_选择图标')
            if element_not==True:
                self.click_IPM('对象_检入中_选择图标')
            if element_not == False:
                self.click_IPM('对象_检入中_选择图标_已存在图标')
            if SelectValue =="上传图标":
                self.click_IPM('对象_检入中_选择图标_上传图标')
                Improt_File_n(path_system_management,'上传图标.jpeg')
                if functionkeys == "确定" or functionkeys == "取消" :
                    self.click_IPM('对象_检入中_选择图标_上传图标_功能键',functionkeys)
            elif SelectValue == "确定" or SelectValue == "取消" :
                self.click_IPM('对象_检入中_选择图标_上传图标_功能键',SelectValue)




    def system_management_object_statusenableprompt(self,field):
        '''
        系统管理_对象管理_基本信息检入中_状态修改提示
        :param field: 确认/取消
        '''
        self.click_IPM('对象_状态修改_功能键',field)



class Assert_result_system_management(AssertMode):
    def __init__(self,driver,element_yaml='system_management', expect='system_management.yaml'):
        super().__init__(driver, element_yaml,expect=expect)















