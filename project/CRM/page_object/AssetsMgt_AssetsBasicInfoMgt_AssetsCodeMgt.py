import allure, os
from public.base.basics import *
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
import datetime
import string
import random
import logging
import os.path

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
        self.refresh()
        self.is_click(user['筛选框'], choice)
        self.input_text(user['筛选框'], status, choice)
        self.hover(user['下拉框data'], status)
        self.is_click(user['下拉框data'], status)
        self.is_click(user['搜索按钮'])

    @allure.step("AssetsCode页点击新增按钮")
    def assets_add(self):
        self.refresh()
        self.is_click(user["add按钮"])
        logging.info("点击新增按钮")

    @allure.step("AssetsCode页点击编辑")
    def assets_edit(self, operate):
        self.is_click(user["operate按钮"], operate)
        logging.info("点击{}按钮".format(operate))

    @allure.step("AssetsCode页滚动页面")
    def assets_scroll(self):
        sleep(0.5)
        self.scroll_into_view(user["新增页cancel"])
        logging.info("滑动到底部")



    @allure.step("AssetsCode页点击保存/提交")
    def assets_button(self, btn):
        sleep(0.5)
        self.is_click(user["新增页button"], btn)
        logging.info("点击{}按钮".format(btn))

    @allure.step("新增页输入")
    def Add_input(self, txt, price, file, unit, choice):
        self.input_text(user["reason输入框"], txt)
        self.is_click(user["infomation输入框"], "purchaseType")
        sleep(1)
        self.is_click(user["下拉筛选框数据"], choice)
        self.input_text(user["infomation输入框"], txt, "nameChinese")
        self.input_text(user["infomation输入框"], txt, "nameEnglish")
        self.input_text(user["infomation输入框"], price, "referencePrice")
        self.is_click(user["infomation输入框"], "unit")
        self.input_text(user["infomation输入框"], unit, "unit")
        self.hover(user["unit下拉框"], unit)
        self.is_click(user["unit下拉框"], unit)
        self.upload_file(user["upload"], file)

    @allure.step("AssetsCode页获取文本")
    def assets_get_text(self):
        sleep(1)
        purchasetype = self.element_input_text(user["infomation输入框"], "purchaseType")
        return purchasetype

    @allure.step("AssetsCode页获取文本")
    def assets_get_status(self):
        sleep(1)
        status = self.element_text(user["第一行approve状态"])
        logging.info("status 的值是：{}".format(status))
        return status

if __name__ == '__main__':
    pass
