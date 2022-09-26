import logging

import allure
from ..test_case.conftest import *
from libs.common.read_element import Element
from public.base.basics import Base

object_name = os.path.basename(__file__).split('.')[0]
data = Element(pro_name, object_name)


class SoftwareOfflineUpgradele(Base):
    """软件离线升级跟踪表"""

    @allure.step("选择品牌")
    def choice_brand(self, brand):
        self.is_click(data["品牌选择框"])
        if brand:
            self.is_click(data["下拉选项"], brand)
        else:
            self.is_click(data["品牌选择框"])


    @allure.step("选择主板")
    def choice_pcba(self, pcba):
        self.is_click(data["主板选择框"])
        if pcba:
            self.is_click(data["下拉选项"], pcba)
        else:
            self.is_click(data["主板选择框"])

    @allure.step("输入物料编码")
    def input_material_code(self, material_code):
        self.input_text(data["物料编码输入框"], material_code)

    @allure.step("输入SN")
    def input_sn(self, sn):
        self.input_text(data["SN输入框"], sn)

    @allure.step("选择升级开始日期")
    def choice_start_date(self, start_date):
        self.input_text(data["升级开始日期"], start_date)

    @allure.step("选择升级结束日期")
    def choice_end_date(self, end_date):
        self.input_text(data["升级结束日期"], end_date)

    @allure.step("点击查询按钮")
    def click_search(self):
        self.is_click(data["查询按钮"])

    @allure.step("点击重置按钮")
    def click_reset(self):
        self.is_click(data["重置按钮"])

    @allure.step("点击导出按钮")
    def click_export(self):
        self.is_click(data["导出按钮"])

    @allure.step("获取列表title")
    def get_titles(self):
        return self.element_text(data["表格title"]).split()


    @allure.step("根据列名获取列数据")
    def get_cols_values(self, *title):
        values = {}
        titles = self.get_titles()
        for i in list(title):
            if i:
                try:
                    col_elements = self.find_elements(data["表格第n列"], str(titles.index(i)+1))
                    col_texts = []
                    for j in range(len(col_elements)):
                        col_texts.append(col_elements[j].text)
                    values[i] = col_texts
                except:
                    logging.info("列名(%s)不存在" % i)
        return values