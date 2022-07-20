from libs.common.time_ui import sleep
from project.IPM.page_object.home import ProcessHome
from project.IPM.page_base.pathconfig import *
from project.IPM.page_object.Center_Component import *

rows = {'1': '2', '2': '3', '3': '4', '4': '5',
        '5': '6', '6': '7', '7': '8', '8': '9'}


class FlowLayout():

    def click_home(self,drivers):
        '''进入流程配置'''
        home = ProcessHome(filename='public_method', driver=drivers)
        home.click_home(public='span', title='流程中心')
        sleep(1)
        home.click_home(public='物料申请')


class MaterialRequisition(PubicMethod):
    def __init__(self, driver, element_yaml='ProcessCenter_MaterialRequisition_Add', expect='ProcessCenter_MaterialRequisition_Add.yaml'):
        super().__init__(driver, element_yaml,expect=expect)

    def url_MaterialRequisition(self):
        '''跳转地址'''
        self.get_url_f(url='申请物料跳转地址')


    def information(self,title=None,Application_type=None):
        '''
        title：基本信息标题
        Application_type：申请类型（手机物料/ODM物料/二级物料/手机物料-二级物料。配件物料）
        test:基本信息模块
        '''
        sleep(1)
        self.switch_window(-1)
        # 项目名称
        sleep(1)
        if title!=None:
            self.input_texts('标题',title)
            log.info(f'输入标题：{title}')
        if Application_type!=None:
            self.rop_down_box('申请类型')
            sleep(1)
            self.rop_down_box('span',Application_type)
            log.info(f'选择申请类型：{Application_type}')

    def import_material(self,Max_class,Medium_class,Subclass,filename):
        '''导入'''
        self.rop_down_box("span","导入")
        sleep(0.5)
        self.rop_down_box('选择物料类型')
        sleep(0.5)
        self.rop_down_box('导入大类',Max_class)
        sleep(0.5)
        self.rop_down_box('导入中类',Medium_class)
        sleep(0.5)
        self.rop_down_box('导入小类',Subclass)
        sleep(0.5)
        self.rop_down_box('span','选择文件')
        sleep(0.5)
        Improt_File_n(DATA, filename)
        log.info('')
        sleep(0.5)
        self.rop_down_box('span',"应用")

    def delete_MaterialType(self,row):
        '''删除物料类信息模块'''
        self.rop_down_box('删除物料类型',rows.get(row))

    def Material_Comparison(self,row):
        '''物料描述对比'''
        self.rop_down_box('物料描述对比', rows.get(row))




