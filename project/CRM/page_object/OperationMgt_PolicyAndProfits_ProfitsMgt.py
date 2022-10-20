import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
import datetime
import string
import random
import logging

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ProfitsPage(Base):
    """权益页"""

    @allure.step("获取列表第4列文本")
    def get_columnValue(self, choice):
        self.refresh()
        eles = self.find_elements(user["第4列文本"], choice)
        columnValue = []
        for n in eles:
            columnValue.append(n.text)
        return columnValue

    @allure.step("Profits权益页查询")
    def profits_search(self, profitstype, keyword):
        self.input_text(user["筛选框"],keyword,choice="keyword")
        self.is_click(user["搜索按钮"])
        sleep(1)
        self.is_click(user["筛选框"],"profitsTypeId")
        self.input_text(user["筛选框"],profitstype, choice="profitsTypeId")
        sleep(1)
        if profitstype == "Spare Warranty":
            self.is_click(user["筛选下拉框第二条数据"])
        else:
            self.is_click(user["筛选下拉框数据"])
        self.is_click(user["搜索按钮"])

if __name__ == '__main__':
    pass
