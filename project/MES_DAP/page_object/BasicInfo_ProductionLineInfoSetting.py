# -*- coding: utf-8 -*-
# @Time    : 2022-08-02 17:15
# @Author  : wuqi
# @Email   : qi.wu@transsion.com
# @File    : BasicInfo_ProductionLineInfoSetting.py
# @Software: PyCharm

import allure
from ..test_case.conftest import *
from libs.common.read_element import Element
from public.base.basics import Base

object_name = os.path.basename(__file__).split('.')[0]
basic = Element(pro_name, object_name)


class ProductionLineInfoSetting(Base):
    """看板参数配置"""

    @allure.step("选择工段")
    def choice_workshop_section(self, content):
        self.is_click(basic["工段下拉选择框"])
        self.is_click(basic["下拉选项"], content)

    @allure.step("选择产线")
    def choice_line(self, content):
        self.is_click(basic["产线下拉选择框"])
        self.is_click(basic["下拉选项"], content)

    @allure.step("选择产线类分类")
    def choice_line_type(self, content):
        self.is_click(basic["产线分类下拉选择框"])
        self.is_click(basic["下拉选项"], content)

    @allure.step("点击新增按钮")
    def click_insert(self):
        self.is_click(basic["新增按钮"])

    @allure.step("点击查询按钮")
    def click_search(self):
        self.is_click(basic["查询按钮"])

    @allure.step("点击重置按钮")
    def click_reset(self):
        self.is_click(basic["重置按钮"])

    @allure.step("点击导出按钮")
    def click_export(self, content):
        # self.is_click(basic["导出按钮"])
        self.check_download(basic["导出按钮"], content)

    @allure.step("点击编辑按钮")
    def click_edit(self, row):
        self.is_click(basic["编辑按钮"], row)

    @allure.step("点击删除按钮")
    def click_del(self, row):
        self.is_click(basic["删除按钮"], row)

    @allure.step("填写表单")
    def fill_form(self, kwargs):
        """
        :param kwargs:dict (key为表单行数， value为录入内容)
        """
        for k, v in kwargs.items():
            if int(k) < 7:
                self.is_click(basic["新增/编辑弹窗第n行表单"], k)
                self.is_click(basic["新增/编辑弹窗下拉选项"], v)
            elif 6 < int(k) < 11:
                self.input_text(basic["新增/编辑弹窗第n行表单"], v, k)
            else:
                assert False, "填入内容行数错误"

    @allure.step("确认保存")
    def click_form_accept(self):
        self.is_click(basic["新增/编辑弹窗确认"])

    @allure.step("取消保存")
    def click_form_cancel(self):
        self.is_click(basic["新增/编辑弹窗取消"])

    @allure.step("删除弹窗确认")
    def click_del_accept(self):
        self.is_click(basic["删除弹窗确认"])

    @allure.step("删除弹窗确认")
    def click_del_cancel(self):
        self.is_click(basic["删除弹窗取消"])
