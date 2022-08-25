import time
import random
import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class CustomerManagementPage(Base):

    # def gotomenu(self, metatitle, nestmenu):
    #     self.is_click(user['一级菜单'], metatitle)
    #     logging.info(f'点击一级菜单：{metatitle}')
    #     self.is_click(user['二级菜单'], nestmenu)
    #     logging.info(f'点击二级菜单：{nestmenu}')
    #     sleep(1)
    #     self.refresh()

    @allure.step("点击新增Add按钮")
    def click_add(self):
        self.is_click(user['Add'])

    @allure.step("随机生成客户名称")
    def cus_name_random(self):
        num = str(random.randint(100, 999))
        cus_name = 'C_test' + num
        return cus_name

    @allure.step("随机生成邮箱地址")
    def email_random(self):
        num = str(random.randint(100, 999))
        email = str("lhm" + num + "qq.com")
        return email

    @allure.step("随机生成联系人")
    def contact_name_random(self):
        num = str(random.randint(100, 999))
        contact_name = str("test_lhm" + num)
        return contact_name

    @allure.step("随机生成联系电话")
    def contact_no_random(self):
        num = str(random.randint(100, 999))
        contact_no = str("13873245" + num)
        return contact_no


    @allure.step("新增表单")
    def input_form_basic_info(self, flag, brand1, brand2, cname, region, sapid=None):
        """选择点击客户类型属性"""
        self.is_click(user['Customer Type'])
        self.is_click(user['Customer Type Select'], flag)
        """选择点击品牌属性"""
        self.is_click(user['Brand'])
        self.is_click(user['Brand Select'], brand1)
        self.is_click(user['Brand Select'], brand2)
        self.is_click(user['Brand finish'])
        self.is_click(user['Brand finish'])
        """输入客户名称属性"""
        self.is_click(user['Customer Name'])
        self.input_text(user['Customer Name'], cname)
        """输入销售区域属性"""
        self.is_click(user['Sales Region'])
        self.input_text(user['Sales Region'], region)
        sleep(2)
        self.is_click(user['Sales Region Select'], region)
        """如果客户类型为Distributor,则输入SAP Customer ID参数，否则为空 """
        if flag == 'Distributor':
            self.input_text(user['SAP Customer ID'], sapid)
        """点击客户等级属性"""
        self.is_click(user['Customer Grade'])
        self.is_click(user['Customer Grade Select'], 'A')
        sleep(0.8)
        """选择销售业务类型属性"""
        self.is_click(user['Business Type'])
        sleep(1.5)
        self.is_click(user['Business Type Selecte'], 'Retail&Wholesale')

    @allure.step("新增表单")
    def input_form_contact_info(self, contact_name, contact_no, email, country, addresss):
        self.input_text(user['Contact Name'], contact_name)
        self.input_text(user['Contact No'], contact_no)
        self.input_text(user['Email'], email)
        self.is_click(user['Country'])
        self.input_text(user['Country'], country)
        sleep(1)
        self.is_click(user['Country Select'], country)
        self.input_text(user['Customer Address'], addresss)
        self.is_click(user['Add Submit'])
        sleep(3)


    @allure.step("客户列表页面，根据客户ID条件筛选客户信息")
    def input_customer_query(self, customer_id):
        self.is_click_dcr(user['筛选Customer'])
        self.input_text_dcr(user['筛选Customer'], customer_id)
        sleep(2.5)
        Base.presence_sleep_dcr(self, user['筛选Customer Select'], customer_id)
        self.is_click(user['筛选Customer Select'], customer_id)

    @allure.step("客户列表页面，点击Search 查询按钮")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(3.5)

    @allure.step("客户列表页面，点击Reset 重置按钮")
    def click_reset(self):
        self.is_click(user['Reset'])
        sleep(4.5)

    @allure.step("获取新增客户ID")
    def get_customer_id(self):
        Base.presence_sleep_dcr(self, user['Get list Customer Id'])
        c_id = self.element_text(user['Get list Customer Id'])
        return c_id

    @allure.step("获取新增客户Name")
    def get_customer_name(self):
        c_name = self.element_text(user['Get list Customer Name'])
        return c_name

    @allure.step("获取新增客户Name")
    def get_brand(self):
        c_brand = self.element_text(user['Get list Brand'], 'Infinix,TECNO')
        return c_brand

    @allure.step("获取新增客户类型")
    def get_customer_type(self, type1):
        customer_type = self.element_text(user['Get Customer Type'], type1)
        return customer_type

    @allure.step("获取新增客户的Contact Name")
    def get_contact_name(self):
        sleep(1.5)
        self.scroll_into_view(user['Get Contact Name'])
        contact_name = self.element_text(user['Get Contact Name'])
        return contact_name

    @allure.step("获取新增客户的Contact No")
    def get_contact_no(self):
        contact_no = self.element_text(user['Get Contact No'])
        return contact_no

    @allure.step("关闭客户管理菜单")
    def click_close_customer_mgt(self):
        self.is_click(user['关闭客户管理菜单'])
        sleep(2)

    @allure.step("修改编辑二代表单,客户名称、联系人、联系电话")
    def edit_form_info(self, edit_c_name, edit_contact_name, edit_contact_no):
        self.is_click_dcr(user['Edit'])
        sleep(1.5)
        Base.presence_sleep_dcr(self, user['Customer Name'], edit_c_name)
        self.input_text(user['Customer Name'], edit_c_name)

        self.input_text(user['Contact Name'], edit_contact_name)
        self.input_text(user['Contact No'], edit_contact_no)
        self.is_click(user['Edit Submit'])
        sleep(4)


    @allure.step("删除新建的客户")
    def delete_customer(self):
        self.is_click_dcr(user['CheckBox'])
        self.is_click(user['More Options'])
        sleep(2)
        Base.presence_sleep_dcr(self, user['Delete'])
        self.is_click(user['Delete'])
        sleep(1.5)
        Base.presence_sleep_dcr(self, user['Delete Confirm'])
        self.is_click(user['Delete Confirm'])


if __name__ == '__main__':
    pass
