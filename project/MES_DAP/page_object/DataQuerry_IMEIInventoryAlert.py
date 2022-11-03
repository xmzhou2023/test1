import logging

import allure
from ..test_case.conftest import *
from libs.common.read_element import Element
from public.base.basics import Base

object_name = os.path.basename(__file__).split('.')[0]
data = Element(pro_name, object_name)


class IMEIInventoryAlert(Base):
    """码段库存预警"""

    @allure.step("切换tab")
    def switch_tab(self, content):
        self.is_click(data["tab"], content)

    @allure.step("选择项目")
    def choice_project(self, tab, project):
        self.is_click(data["项目选择框"], tab)
        self.is_click(data["下拉选项"], project)

    @allure.step("选择开始时间")
    def choice_start_date(self, tab, start_date):
        self.input_text(data["开始时间选择框"], start_date, tab)

    @allure.step("选择结束时间")
    def choice_end_date(self, tab, end_date):
        self.input_text(data["结束时间选择框"], end_date, tab)

    @allure.step("点击查询按钮")
    def click_search(self, tab):
        self.is_click(data["查询按钮"], tab)

    @allure.step("点击重置按钮")
    def click_reset(self, tab):
        self.is_click(data["重置按钮"], tab)

    @allure.step("点击导出按钮")
    def click_export(self, tab):
        self.is_click(data["导出按钮"], tab)

    @allure.step("获取列表title")
    def get_titles(self, tab):
        return self.element_text(data["表格title"], tab).split()


    @allure.step("根据列名获取列数据")
    def get_cols_values(self, *title, tab):
        values = {}
        titles = self.get_titles(tab)
        for i in list(title):
            if i:
                try:
                    col_elements = self.find_elements(data["表格第n列"], tab, str(titles.index(i)+1))
                    col_texts = []
                    for j in range(len(col_elements)):
                        col_texts.append(col_elements[j].text)
                    values[i] = col_texts
                except:
                    logging.info("列名(%s)不存在" % i)
        return values