
'''
#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/5/18 16:00
# @Author : 李小素
# @File : test_area_cfg.py
# @Software: PyCharm
# @title:个人组件
'''
import pywinauto
from pywinauto.keyboard import send_keys
from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.Basics import *
from libs.common.logger_ui import log
from project.IPM.page_base.yamlbase import *
from selenium.webdriver.common.by import By
import allure
from libs.common.connect_sql import *

# chome=Element('E_RD02')
# filelist=YamlRead(r'assert_RD02.yaml')


class PubicMethod(Base):
    def __init__(self, driver,element_yaml,expect=None):
        super().__init__(driver)
        self.chome = Element(element_yaml)
        self.filelist = YamlRead(expect)




    def max_class(self,maxclass=None):
        '''
        maxclass：传入大类元素
        test:大类元素获取
        '''
        try:
            self.is_click(self.chome[maxclass])
            log.info(f"大类中找到{maxclass}")
        except:
            self.scroll_into_view(self.chome[maxclass])
            self.is_click(self.chome[maxclass])
            log.info(f"滑动后大类中找到{maxclass}")


    def in_class(self,medium):
        '''
        medium：传入中类元素
        test:中类元素获取
        '''
        try:
            self.is_click(self.chome[medium])
            log.info(f"中类中找到{medium}")
        except:
            self.scroll_into_view(self.chome[medium])
            self.is_click(self.chome[medium])
            log.info(f"滑动后大类中找到{medium}")


    def min_class(self, Subclass):
        '''
        Subclass：传入小类元素
        test:小类元素获取
        '''
        try:
            self.is_click(self.chome[Subclass])
            log.info(f"中类中找到{Subclass}")
        except:
            self.scroll_into_view(self.chome[Subclass])
            self.is_click(self.chome[Subclass])
            log.info(f"滑动后大类中找到{Subclass}")



    # def material_type(self,
    #                   title=None,
    #                   Application_type=None,
    #                   maxclass=None,
    #                   medium=None,
    #                   Subclass=None):
    #     '''
    #     基本信息
    #     title：基本信息标题
    #     Application_type：申请类型
    #     maxclass:大类选择
    #     medium：中类选择
    #     Subclass:小类选择
    #     test:申请单据，自动带出的物料类型
    #     '''
    #     self.information(title=title,Application_type=Application_type)
    #     if Application_type==None:
    #         log.info('申请类型为空，找不到物料类型')
    #     else:
    #         try:
    #             self.is_click(self.chome['物料类型'])
    #             sleep(1)
    #             self.max_class(maxclass=maxclass)
    #             sleep(1)
    #             self.in_class(medium=medium)
    #             if Subclass != None:
    #                 self.min_class(Subclass=Subclass)
    #             sleep(2)
    #         except:
    #             raise


    def material_types(self,maxclass,medium,Subclass=None):
        '''
        maxclass:大类选择
        medium：中类选择
        Subclass:小类选择
        test:新增物料类型模块
        '''
        title='物料类型+1'
        try:
            self.is_click(self.chome[title])
            log.info(f"中类中找到{Subclass}")
            self.max_class(maxclass=maxclass)
            self.in_class(medium=medium)
            if Subclass != None:
                self.min_class(Subclass=Subclass)
        except:
            self.scroll_into_view(self.chome[title])
            self.max_class(maxclass=maxclass)
            self.in_class(medium=medium)
            log.info(f"中类中找到{Subclass}")
            if Subclass != None:
                self.min_class(Subclass=Subclass)
        sleep(2)



    def form_zj100(self):
        '''展开表单'''

        self.is_click(self.chome['展开/折叠'])
        sleep(1)




    def form_elements(self,formheader,get_attributs='innerText'):
        '''
        formheader：表头获取
        test:读取表头字段
        '''
        form = self.find_elements(self.chome[formheader])
        formlist = []
        for i in form:
            formlist.append(i.get_attribute(get_attributs))
        log.info(f'获取表单字段{formlist}')
        return formlist


    def form_element(self,formheader,choice=None,get_attributs='innerText'):
        '''
        formheader：表头获取
        test:读取表头字段
        '''
        form = self.find_element(self.chome[formheader],choice=choice)
        res=form.get_attributs(get_attributs)

        return res

    def split_lines(self,s):
        '''
        字段读取特殊处理
        '''
        return s.split('\n')

    def elements_detail_special(self,formheader,choice=None,get_attributs='innerText'):
        '''
        formheader：表单字段获取
        test:读取元素的内容存储在字典中
        '''
        try:
            form = self.find_elements(self.chome[formheader],choice=choice)
            filelistw = []
            for i in form:
                filelistw.append(i.get_attribute(get_attributs).replace(' ', ''))
            lis = ''.join(filelistw)
            form_list = self.split_lines(lis)
            lists=list(filter(None,form_list))
            log.info(f'获取表单字段{lists}')
            return lists
        except Exception as e:
            log.info(f'找不到{formheader}元素信息,{e}')
            raise e

    def elements_detail_special_t(self,formheader,choice=None,get_attributs='innerText'):
        '''
        formheader：表单字段获取
        test:读取元素的内容存储在字典中
        '''
        try:
            form = self.find_elements(self.chome[formheader],choice=choice)
            filelistw = []
            for i in form:
                filelistw.append(i.get_attribute(get_attributs).replace(' ', ''))
            lis = ''.join(filelistw)
            form_list = lis.split('\t')
            lists=list(filter(None,form_list))
            log.info(f'获取表单字段{lists}')
            return lists
        except Exception as e:
            log.info(f'找不到{formheader}元素信息,{e}')
            raise e



    def add_form(self):
        '''点击新增'''
        add='新增'
        try:
            self.is_click(self.chome[add])
            log.info(f"点击新增：{add}")
        except:
            self.scroll_into_view(self.chome[add])
            self.is_click(self.chome[add])
            log.info(f"滑动后点击新增：{add}")


    def add_Subform(self):
        add='增加'
        try:
            self.is_click(self.chome[add])
            log.info(f"点击增加：{add}")
        except:
            self.scroll_into_view(self.chome[add])
            self.is_click(self.chome[add])
            log.info(f"滑动后点击增加：{add}")


    def form_copy(self):
        copy='复制'
        try:
            self.is_click(self.chome[copy])
            log.info(f"点击复制：{copy}")
        except:
            self.scroll_into_view(self.chome[copy])
            self.is_click(self.chome[copy])
            log.info(f"滑动后点击复制：{copy}")
        sleep(2)

    def form_delete(self):
        delete='删除'
        try:
            self.is_click(self.chome[delete])
            log.info(f"点击删除：{delete}")
        except:
            self.scroll_into_view(self.chome[delete])
            self.is_click(self.chome[delete])
            log.info(f"滑动后点击删除：{delete}")
        sleep(2)

    def get_url_f(self,url):
        self.get_url( self.filelist.yaml_read(url))
        sleep(1)

    def rop_down_box(self,click_choice,chioce=None):
        '''点击'''
        try:
            self.is_click(self.chome[click_choice],choice=chioce)
        except:
            self.scroll_into_view(self.chome[click_choice],choice=chioce)
            self.is_click(self.chome[click_choice], choice=chioce)



    def c_move_to_element(self,moveelement,click_choice,chioce=None):
        '''点击'''
        try:
            self.hover(self.chome[moveelement],choice=chioce)
            self.is_click(self.chome[click_choice],choice=chioce)
        except:
            self.scroll_into_view(self.chome[click_choice],choice=chioce)
            self.is_click(self.chome[click_choice], choice=chioce)

    def scroll_into_views(self,click_choice,chioce=None):
        '''点击'''
        self.scroll_into_view(self.chome[click_choice],choice=chioce)
        self.is_click(self.chome[click_choice], choice=chioce)

    def rop_down_boxs(self,chioce=None):
        '''点击'''
        try:
            self.is_click(self.chome['currency'],choice=chioce)
        except:
            self.scroll_into_view(self.chome['currency'],choice=chioce)
            self.is_click(self.chome['currency'], choice=chioce)

    def double_click_element(self,doubleclick):
        '''双击打开获取'''
        self.double_clicks(self.chome[doubleclick])

    def input_texts(self,elements='currency',text=None,choice=None):
        '''
        elements:元素
        text：输入值
        '''
        self.input_text(locator=self.chome[elements], txt=text,choice=choice)

    def double_click_choice(self,doublecelemet=None,inputelemet=None,inputtext=None,chioce=None):
        '''
        doublecelemet：传入元素
        inputelemet:传入元素
        inputtext：输入值
        '''
        try:
            if doublecelemet != None:
                self.double_click_element(doubleclick=doublecelemet)
                log.info(f'点击元素：{doublecelemet}')
                if inputelemet != None:
                    self.input_texts(elements=inputelemet,text=inputtext)
                    log.info(f'点击元素：{inputelemet},输入：{inputtext}')
                    if chioce != None:
                        sleep(1)
                        self.rop_down_box(click_choice='text_path',chioce=chioce)
                        print(f'sss:{chioce}')
                        log.info(f'点击元素：{chioce}')
        except:
            log.info('元素未找到')

    def click_choice(self,
                     inputelemet='currency',
                     Field_name=None,
                     input_text=None,
                     click_choice='dict_currency',
                     choice_text=None):
        '''
         inputelemet：选择字段元素,
         Field_name：选择字段名,
         input_text：传入内容,
         click_choice：筛选后选择,
         choice_text:传入内容
        test:点击选择框，获取下拉框值
        '''
        try:
            self.rop_down_boxs(chioce=Field_name)
            self.input_texts(elements=inputelemet, text=input_text,choice=Field_name)
            log.info(f'点击元素：{inputelemet},输入：{input_text}')
            self.rop_down_box(click_choice=click_choice,chioce=choice_text)
            log.info(f'点击元素：{choice_text}')

        except:
            log.info(f'元素信息报错:{Field_name},{choice_text}')
            raise

    def click_choices(self,
                     inputelemet='currency',
                     Field_name=None,
                     input_text=None,
                     click_choice='dict_currency',
                     choice_text=None):

        '''
        inputelemet:点击选择框元素
        Field_name=选择框传入变量值,
        input_text=在选择框中输入值,
        click_choice=下拉框元素获取,
        choice_text=填写选择框输入的值
        选择框'''

        try:
            self.rop_down_box(click_choice=inputelemet, chioce=Field_name)
            self.input_texts(elements=inputelemet, text=input_text, choice=Field_name)
            log.info(f'点击元素：{inputelemet},输入：{input_text}')
            sleep(1)
            self.rop_down_box(click_choice=click_choice, chioce=choice_text)
            log.info(f'点击元素：{choice_text}')
        except:
            log.info(f'元素信息报错:{Field_name},{choice_text}')
            raise

    def db_delete(self,databases,sql):
        delete_db(databases=databases,sql=self.filelist.yaml_read(sql))

    def db_updata(self,databases,sql):
        change_db(databases=databases,sql=self.filelist.yaml_read(sql))

    def multi_library(self,databases_one,sql_one,listname_one,databases_two,sql_two,listname_two):
        '''
        databases_one:数据库表名
        sql_one：sql
        listname_one:查询字段名
        databases_two：第二个数据库名
        sql_two：sql
        listname_two：查询字段名
        '''
        '''多个数据库之间的关联查询'''
        generatelist(databases_one,
                     self.filelist.yaml_read(sql_one),
                     listname_one,databases_two,
                     self.filelist.yaml_read(sql_two),
                     listname_two)


    def get_element_handling(self,element,chioce=None,get_attribute='innerText'):
        result=self.find_elements(self.chome[element],choice=chioce)
        filelistw = []
        for i in result:
            filelistw.append(i.get_attribute(get_attribute))
        lis = ''.join(filelistw)
        form_list = lis.split('\t')
        del_list = ['No.', '']
        l = [x for x in form_list if x not in del_list]
        return l


def Improt_File_n(pathDIR,path_filename):
    '''

    :param pathDIR: 导入的文件路径
    :param path_filename: 文件名
    :param mumo_lis: 异常备注
    :return:
    '''
    try:
        # 打开文件选择框
        # 创建操作桌面的对象
        app = pywinauto.Desktop()
        # 获取弹窗的窗口标题
        dlg = app["打开"]
        # 打印窗口的所有控件信息
        # dlg.print_ctrl_ids()

        # 选择文件地址输入控件
        dlg["Toolbar3"].click()
        send_keys(pathDIR)
        send_keys("{VK_RETURN}")
        sleep(2)

        # 输入文件名
        dlg["文件名(&N):Edit"].type_keys(path_filename)
        send_keys("{VK_RETURN}")
        sleep(2)
    except Exception as e:
        print('文件导入失败')
        raise Exception(e)


if __name__ == '__main__':
    pass










