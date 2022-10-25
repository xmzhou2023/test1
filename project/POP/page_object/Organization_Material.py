import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class QueryMaterial(Base):
    """查询物料类"""
    @allure.step("输入商品名称")
    def input_good(self,good,code):
        self.is_click_tbm(user['商品名称输入框'])
        self.input_text(user['商品名称输入框'],good)
        goodcode = code + " " + good
        sleep(1)
        self.is_click_tbm(user['商品名'],goodcode)

    @allure.step("点击查询")
    def click_query(self):
        self.is_click_tbm(user['查询按钮'])

class QueryMore(Base):
    """查看更多筛选条件"""

    @allure.step("点击更多")
    def click_more(self):
        self.is_click_tbm(user['更多按钮'])


class ExportMaterial(Base):
    """物料信息导出类"""

    @allure.step("点击导出")
    def click_export(self):
        self.is_click_tbm(user['导出'])


if __name__ == '__main__':
    pass
