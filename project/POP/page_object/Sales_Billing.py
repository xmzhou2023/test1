import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from project.POP.test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class SalesBilling(Base):
    """销售开单类"""

    @allure.step("点击开单按钮")
    def click_billing(self):
        self.is_click(user['开单按钮'])

    @allure.step("选择门店")
    def switch_shop(self,content,code):
        self.is_click(user['门店输入框'])     # 点击定位到门店选择框
        self.input_text(user['门店输入框'],content)    # 输入门店名下拉框会下拉展示门店
        variable = content + " " + code   # 下拉展示”门店名称 门店编码“ 例如：”我的测试门店 PBD00020“
        self.is_click(user['开单选择的门店'],variable)   # 根据输入门店下拉展示数据点击对应门店

    @allure.step("选择促销员")
    def switch_promoter(self,content,code):
        self.is_click(user['促销员选择框'])  # 点击定位到促销员选择框
        self.input_text(user['促销员选择框'], content)  # 输入促销员姓名下拉框会下拉展示促销员
        variable = content + " - " + code  # 下拉展示”促销员名称 - 门店编码“ 例如：”Wenqiang Zhang -  PEEC000010“
        self.is_click(user['选择的促销员'], variable)  # 根据输入促销员下拉展示数据点击对应促销员

    @allure.step("输入消费者手机号")
    def input_phone(self,phone):
        self.input_text(user['消费者手机号输入框'],phone)

    @allure.step("输入商品编码")
    def input_goodscode(self,goodcode):
        self.input_enter(user['商品编码输入框'],goodcode)

    @allure.step("输入价格")
    def input_price(self,price):
        self.is_click(user['价格按钮'])
        self.is_click(user['价格输入框'])
        self.input_text(user['价格输入框'],price)

    @allure.step("输入实收金额")
    def input_money(self,cash,bankcard,other):
        self.input_text(user['现金金额输入框'],cash)
        self.input_text(user['银行卡金额输入框'],bankcard)
        self.input_text(user['其他支付输入框'],other)

    @allure.step("填写备注")
    def input_remarks(self,cusremarks,saleremarks):
        self.input_text(user['客户备注输入框'],cusremarks)
        self.input_text(user['销售备注输入框'],saleremarks)

    @allure.step("点击完成收款")
    def click_Collection(self):
        self.is_click(user['完成收款按钮'])
        sleep(3)

    @allure.step("断言")
    def assert_sales_order_num(self,drivers,expect):
        DomAssert(drivers).assert_exact_att(expect)
if __name__ == '__main__':
    pass
