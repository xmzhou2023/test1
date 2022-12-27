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

class AssetsMgtPage(Base):
    """AssetsMgt页"""

    @allure.step("获取列表第某列文本值")
    def get_columnValue(self, choice):
        self.refresh()
        eles = self.find_elements(user["第某列文本"], choice)
        columnValue = []
        for n in eles:
            columnValue.append(n.text)
        return columnValue


    @allure.step("Assets Code页面，筛选框下拉框查询")
    def Get_search(self, status, choice):
        self.is_click(user['筛选框'], choice)
        self.input_text(user['筛选框'], status, choice)
        self.hover(user['下拉框data'], status)
        self.is_click(user['下拉框data'], status)
        self.is_click(user['搜索按钮'])

if __name__ == '__main__':
    pass
