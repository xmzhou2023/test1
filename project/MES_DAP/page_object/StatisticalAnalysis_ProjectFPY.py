import logging
import os

import allure

from public.base.basics import Base
from ..test_case.conftest import *
from libs.common.read_element import Element

object_name = os.path.basename(__file__).split('.')[0]
statistical = Element(pro_name, object_name)


class ProjectFPY(Base):
    """项目直通率"""

    @allure.step("选择工段")
    def choice_workshop_section(self, content):
        self.is_click(statistical["工段选择框"])
        if content:
            self.is_click(statistical["下拉选项"], content)
        else:
            self.is_click(statistical["工段选择框"])

    @allure.step("选择开始时间")
    def choice_start_date(self, start_date):
        logging.info(start_date)
        if start_date:
            self.input_text(statistical["开始时间选择框"], start_date)
            self.is_click(statistical["开始时间选择框"])

    @allure.step("选择结束时间")
    def choice_end_date(self, end_date):
        logging.info(end_date)
        if end_date:
            self.input_text(statistical["结束时间选择框"], end_date)
            self.is_click(statistical["结束时间选择框"])

    @allure.step("选择站点")
    def choice_station(self, *content):
        self.is_click(statistical["站点选择框"])
        for i in content:
            if i and i is not None:
                self.is_click(statistical["下拉选项"], i)
                self.is_click(statistical["站点选择框"])
            else:
                self.is_click(statistical["站点选择框"])

    @allure.step("选择项目")
    def choice_project(self, content):
        self.is_click(statistical["项目选择框"])
        if content:
            self.is_click(statistical["下拉选项"], content)
        else:
            self.is_click(statistical["项目选择框"])

    @allure.step("点击查询按钮")
    def click_search(self):
        self.is_click(statistical["查询按钮"])

    @allure.step("点击重置按钮")
    def click_reset(self):
        self.is_click(statistical["重置按钮"])

    @allure.step("点击导出按钮")
    def click_export(self, content):
        self.check_download(statistical["导出按钮"], content)

    @allure.step("获取列表title")
    def get_titles(self):
        return self.element_text(statistical["表格title"]).split()


    @allure.step("根据列名获取列数据")
    def get_cols_values(self, *title):
        values = {}
        titles = self.get_titles()
        for i in list(title):
            if i:
                try:
                    col_elements = self.find_elements(statistical["表格第n列"], str(titles.index(i)+1))
                    col_texts = []
                    for j in range(len(col_elements)):
                        col_texts.append(col_elements[j].text)
                    values[i] = col_texts
                except:
                    logging.info("列名(%s)不存在" % i)
        return values