import logging

from project.IPM.page_base.basics_IPM import PubicMethod
from libs.common.time_ui import *
from project.IPM.page_base.assert_pubic import *
from project.IPM.api.APIRequest import *
import random

class ipm_publiclibrary(PubicMethod):

    def __init__(self,driver,element_yaml='ipm_publiclibrary',expect='ipm_publiclibrary.yaml'):
        super().__init__(driver, element_yaml,expect=expect)
    def personnel_list(self, text, Confirm_or_Cancel=None):
        '''
        人员列表
        人员选择
        '''
        sleep(2)
        self.input_text_IPM("请输入姓名或工号", text)
        self.click_IPM("选择人员", text)
        if Confirm_or_Cancel == None or Confirm_or_Cancel == "确定":
            self.click_IPM("人员列表_确定")
        else:
            self.click_IPM("人员列表_取消")

    def DropDownBox(self,element_field,FieldName,FieldElementBox,*Drop_down_value):
        """
        下拉框_多选
        :param element_field: 字段元素
        :param FieldName: 字段名字
        :param FieldElementBox 点击下拉框
        :param Drop_down_value: 下拉框的值，支持传入多个

        """

        field_att=self.find_elemens_ipm_yaml_get_attribute(element_field)
        for i in field_att:
            if i == FieldName:
                self.click_IPM(FieldElementBox, choice=i) #参考//div/label[text()=' variable ']/..//input
        eles_field = self.find_elemens_ipm_yaml_get_attribute("下拉值获取")
        if Drop_down_value =="添加全部":
            self.click_IPM('添加全部')
        else:
            for value in Drop_down_value:
                if value in eles_field:
                    self.click_IPM('下拉值选择',value)
                else:
                    logging.info("当前字段不存在")
        try:
            self.click_IPM('点击标题')
        except:
            logging.info("当前没有需要点击的元素")
    def DropDownBoxAcquiredField(self,*Drop_down_value):
        """
        下拉框_已经点击下拉框获取到下拉框中的值
        :param Drop_down_value: 下拉框的值，支持传入多个

        """
        eles_field = self.find_elemens_ipm_yaml_get_attribute("下拉值获取")
        if Drop_down_value =="添加全部":
            self.click_IPM('添加全部')
        else:
            for value in Drop_down_value:
                if value in eles_field:
                    self.click_IPM('下拉值选择',value)
                else:
                    logging.info("当前字段不存在")
        try:
            self.click_IPM('点击标题')
        except:
            logging.info("当前没有需要点击的元素")


