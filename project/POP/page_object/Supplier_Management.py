import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class SupplierManagement(Base):
    """供应商管理查询类"""

    @allure.step("选择卖家")
    def switch_seller(self,seller):
        self.is_click_tbm(user['卖家输入框'])
        self.input_text(user['卖家输入框'],seller)
        self.is_click_tbm(user['选择卖家'],seller)
    @allure.step("选择卖家类型")
    def switch_sellertype(self,sellertype):
        self.is_click_tbm(user['卖家类型'])
        self.input_text(user['卖家类型'],sellertype)
        self.is_click_tbm(user['选择卖家类型'],sellertype)

    @allure.step("选择卖家所属国家")
    def switch_sellercountry(self, sellercountry):
        self.is_click_tbm(user['卖家所属国家'])
        self.input_text(user['卖家所属国家'], sellercountry)
        self.is_click_tbm(user['选择所属国家'], sellercountry)

    @allure.step("选择门店")
    def switch_shop(self,shop):
        self.is_click_tbm(user['门店输入框'])
        self.input_text(user['门店输入框'], shop)
        self.is_click_tbm(user['选择门店'], shop)

    @allure.step("选择卖家国家")
    def switch_shopcountry(self,shopcountry):
        self.is_click_tbm(user['门店国家输入框'])
        self.input_text(user['门店国家输入框'],shopcountry)
        self.is_click_tbm(user['选择门店国家'],shopcountry)

    @allure.step("选择归属组织")
    def switch_division(self, division):
        self.is_click_tbm(user['归属机构选择框'])
        self.input_text(user['归属机构选择框'], division)
        self.is_click_tbm(user['选择归属机构'], division)

    @allure.step("点击查询")
    def click_query(self):
        self.is_click_tbm(user['查询按钮'])

    @allure.step("点击更多")
    def click_more(self):
        self.is_click_tbm(user['更多按钮'])

    @allure.step("点击更多查询")
    def click_morequery(self):
        self.is_click_tbm(user['更多筛选页查询按钮'])

    @allure.step("点击关闭更多筛选页")
    def click_close(self):
        self.is_click_tbm(user['关闭筛选页按钮'])


class ExportSupplier(Base):
    """供应商导出类"""

    @allure.step("点击导出")
    def click_export(self):
        self.is_click_tbm(user['导出按钮'])


if __name__ == '__main__':
    pass
