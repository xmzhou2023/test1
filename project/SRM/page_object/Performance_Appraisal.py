import time

import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
app= Element(pro_name, object_name)

class Performance(Base):
    """供应商绩效类"""

    @allure.step("进入供应商绩效考核")
    def PerformanceAppraisal(self):
        self.is_click(app['供应商绩效'])

    def appraisal_page_title(self):
       return self.find_element(app["供应商绩效标题"]).text


    def enter_SupplyCategory(self):
        self.frame_enter(app["供应商绩效iframe"])
        self.is_click(app["供应商绩效-评估代码供货品类配置"])

    def title_SupplyCategory(self):
       return self.find_element(app["评估代码供货品类配置页面标题"]).text


    def creat_SupplyCategory(self):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.is_click(app["评估代码供货品类配置-新建"])


    def get_title_creat(self):
        return self.find_element(app["评估代码供货品类配置-新建弹窗标题"]).text

    def creat_SupplyCategory_close(self):
        self.is_click(app["评估代码供货品类配置-新建弹窗-关闭"])

    def creat_SupplyCategory_cancel(self):
        self.is_click(app["评估代码供货品类配置-新建"])
        self.is_click(app["评估代码供货品类配置-新建-取消"])


    @allure.step("进入供应商绩效考核")
    def minimize(self):
        self.is_click(app['窗口最小化'])
    # def search(self):
    #     ele = self.find_elements_srm("//form[1]/button[2]/i")[3]
    #     print("测试")
    #     print(ele)
    #     ele.click()






if __name__ == '__main__':
    pass
