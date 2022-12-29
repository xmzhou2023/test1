import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
from project.POP.page_object.Center_Component import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AddSalesLevel(Base):
    """新增门店销量等级类"""

    @allure.step("点击新增按钮")
    def click_add(self):
        self.is_click_tbm(user['新增按钮'])

    @allure.step("选择组织")
    def switch_organization(self,organization):
        self.input_text(user['组织选择框'],organization)
        self.is_click_tbm(user['选择组织'],organization)

    @allure.step("选择区域")
    def switch_region(self,region):
        self.is_click_tbm(user['区域选择框'])
        self.input_text(user['区域选择框'],region)
        sleep(0.5)
        self.is_click_tbm(user['选择区域'],region)

    @allure.step("点击新增门店销量等级参数")
    def add_saleslevel(self):
        self.is_click_tbm(user['新增销量等级'])

    @allure.step("选择等级名称")
    def switch_level(self,level):
        self.is_click_tbm(user['等级名称'])
        self.input_text(user['等级名称'],level)
        sleep(0.5)
        self.is_click_tbm(user['选择等级'],level)

    @allure.step("输入月度销售范围")
    def input_salesdata(self,minsales,maxsales):
        self.is_click_tbm(user['月度销售范围下限值'])
        self.input_text(user['月度销售范围下限值'],minsales)
        self.input_text(user['月度销售范围上限值'],maxsales)

    @allure.step("点击保存")
    def click_preservation(self):
        self.scroll_into_view(user['保存按钮'])
        self.is_click_tbm(user['保存按钮'])

    @allure.step("新增数据删除")
    def delete_data(self):
        self.is_click_tbm(user['新增数据选中按钮'])
        self.is_click_tbm(user['删除按钮'])
        sleep(1)
        self.is_click_tbm(user['二次弹窗确定'])

class QuerySalesLevel(Page_Operation,General_button):
    """查询类"""
    select_list = {"门店销售等级-组织框": "门店销售等级-组织", "门店销售等级-区域框": "门店销售等级-区域", "门店销售等级-等级名称框": "门店销售等级-等级名称"}
    def querysaleslevel(self, select, content):
        if select in self.select_list:
            self.single_condition_input_boxquery(select, self.select_list[select], content)
            sleep()
            self.query()
        else:
            logging.error("系统检测没有此筛选项，请检查后重新输入")




if __name__ == '__main__':
    pass
