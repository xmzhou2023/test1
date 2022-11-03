# -*- coding: utf-8 -*-
# @Time    : 2022-07-29 11:08
# @Author  : wuqi
# @Email   : qi.wu@transsion.com
# @File    : BasicInfo_DailyProductionPlan.py
# @Software: PyCharm
import time

import allure

from public.base.basics import Base
from libs.common.read_element import Element
from ..test_case.conftest import *


object_name = os.path.basename(__file__).split('.')[0]
basic = Element(pro_name, object_name)


class DailyProductionPlan(Base):
    """日生产计划"""

    @allure.step("查询条件输入日期")
    def input_date(self, date):
        self.input_text(basic["日期输入框"], date)

    @allure.step("查询条件选择工段")
    def choice_workshop_section(self, content):
        self.is_click(basic["工段下拉选择框"])
        self.is_click(basic["下拉选项"], content)

    @allure.step("查询条件选择项目/机型")
    def choice_workshop_section(self, content):
        self.is_click(basic["项目/机型选择框"])
        self.is_click(basic["下拉选项"], content)

    @allure.step("点击查询按钮")
    def click_search(self):
        self.is_click(basic["查询按钮"])

    @allure.step("点击重置按钮")
    def click_reset(self):
        self.is_click(basic["重置按钮"])

    @allure.step("点击下载按钮")
    def click_download(self, content):
        self.check_download(basic["下载模板按钮"], content)

    @allure.step("点击导入计划按钮")
    def click_import(self):
        self.is_click(basic["导入计划按钮"])

    @allure.step("点击导出按钮")
    def click_export(self, content):
        # self.is_click(basic["导出按钮"])
        self.check_download(basic["导出按钮"], content)

    @allure.step("导入计划")
    def fill_form(self, kwargs):
        """
        :param kwargs:dict (key为表单行数， value为录入内容)
        """
        for k, v in kwargs.items():
            if int(k) <= 2:
                self.is_click(basic["导入计划弹窗第n行表单"], k)
                self.is_click(basic["导入计划弹窗下拉选项"], v)
            elif int(k) == 3:
                self.upload_file(basic["导入计划弹窗文件选择"], v)
            else:
                assert False, "填入内容行数错误"

    @allure.step("上传服务器")
    def click_upload(self):
        self.is_click(basic["导入计划弹窗上传服务器按钮"])

    @allure.step("删除已选择文件")
    def del_file(self, file_name):
        self.is_click(basic["导入计划弹窗已选择文件"], file_name)


