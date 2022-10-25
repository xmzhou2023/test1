import allure, os

from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ShopReceipt(Base):
    """门店收货单"""

    @allure.step('点击自采收货')
    def receipt_click_menu_self_purchase(self, menu):
        self.is_click(user['菜单按钮'], menu)

    @allure.step('选择收货门店')
    def receipt_select_shop(self, shopname):
        self.is_click(user['自采收货-门店'])
        self.input_text(user['自采收货-门店'], shopname)
        sleep(2)
        self.is_click_dcr(user['选择搜索结果'], shopname)

    @allure.step('选择收货商品')
    def receipt_select_goods(self, goodsname):
        self.is_click(user['自采收货-商品'])
        self.input_text(user['自采收货-商品'], goodsname)
        sleep(1)
        self.is_click_tbm(user['选择搜索结果'], goodsname)

    @allure.step('点击搜索查询商品')
    def receipt_search_goods(self, button):
        self.is_click(user['查询重置按钮'], button)

    @allure.step('点击添加单个/多个收货商品')
    def receipt_add_goods(self):
        for i in range(1, 3):
            self.is_click_tbm(user['点击+添加商品'], str(i))
            self.is_click_tbm(user['添加商品数量'])

    @allure.step('点击提交')
    def receipt_click_submit(self, button):
        self.is_click(user['点击提交'], button)


if __name__ == '__main__':
    pass
