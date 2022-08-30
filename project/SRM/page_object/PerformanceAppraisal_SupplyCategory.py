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
        # self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        # self.is_click(app["评估代码供货品类配置-新建"])
        # time.sleep(2)
        self.is_click(app["评估代码供货品类配置-新建弹窗-关闭"])
        self.frame_back()


    def creat_SupplyCategory_cancel(self):
        # self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        # self.is_click(app["评估代码供货品类配置-新建"])
        self.is_click(app["评估代码供货品类配置-新建-取消"])
        self.frame_back()

    def creat_select_code(self,code):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.is_click(app["评估代码供货品类配置-新建"])
        self.input_text(app['评估代码供货品类配置-新建-评估代码'],txt=code)


    def creat_select_material(self):
        self.is_click(app['评估代码供货品类配置-新建-小类搜索'])
        self.frame_back()
        self.frame_enter(app["评估代码供货品类配置-新建-小类iframe"])
        self.is_click(app['评估代码供货品类配置-新建-小类选择'])
        self.is_click(app['评估代码供货品类配置-新建-小类-确定'])
        self.frame_back()


    def creat_select_rule(self):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.is_click(app['评估代码供货品类配置-新建-评分规则'])
        self.frame_back()
        self.frame_enter(app["评估代码供货品类配置-新建-评分规则iframe"])
        self.is_click(app["评估代码供货品类配置-新建-评分规则-选择"])
        self.is_click(app["评估代码供货品类配置-新建-评分规则-确定"])


    def creat_SelectOK(self):
        self.frame_back()
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.is_click(app["评估代码供货品类配置-新建-确定"])
        self.frame_back()
        self.is_click(app["评估代码供货品类配置-新建-确定-保存确定"])


    @allure.step("获取新建成功弹窗提示内容")
    def get_alert_text(self):
        # 获取弹窗内容，srm使用
        return self.find_element(app["评估代码供货品类配置-新建-操作成功提示"]).text


    def search_code(self, code):
        self.frame_enter(app["评估代码供货品类配置页面内容iframe"])
        self.input_text(app["评估代码供货品类配置-评估代码查询输入框"], code)
        self.is_click(app["评估代码供货品类配置-查询"])
        self.frame_back()
        # time.sleep(3)
        # self.find_elements_choice('//button[text()=" 查询"]',1)


    def search_code_number(self):
        return self.find_element(app["评估代码搜索结果"]).text


    def search_material(self, material):
        self.input_text(app["评估代码供货品类配置-物料小类查询输入框"], material)
        self.is_click(app["评估代码供货品类配置-查询"])


    @allure.step("最小化供应商绩效考核窗口")
    def MinWindows(self):
        self.frame_exit()
        self.is_click(app['窗口最小化'])




if __name__ == '__main__':
    pass



