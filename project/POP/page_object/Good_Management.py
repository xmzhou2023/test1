import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from project.POP.test_case.conftest import *
from project.POP.page_object.Center_Component import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AddGood(Base):
    """新增商品类"""

    @allure.step("点击新增按钮")
    def click_add(self):
        self.is_click(user['商品管理新增按钮'])

    @allure.step("输入产品名称")
    def input_productname(self,content):
        self.is_click(user['产品名称输入框'])
        self.input_text(user['产品名称输入框'],content)
        sleep(1)

    @allure.step("选择商品类目")
    def switch_category(self,variable):
        self.is_click(user['商品类目选择框'])
        self.input_text(user['商品类目选择框'],variable)
        self.is_click(user['商品类目'],variable)

    @allure.step("选择商品区域")
    def switch_region(self,variable):
        self.is_click(user['区域选择框'])
        self.input_text(user['区域选择框'],variable)
        self.is_click(user['商品的区域'],variable)

    @allure.step("选择商品品牌")
    def switch_brand(self,variable):
        self.is_click(user['商品品牌选择框'])
        self.input_text(user['商品品牌选择框'],variable)
        self.is_click(user['商品品牌'],variable)

    @allure.step("选择IMEI是否被管理")
    def switch_imei(self, variable):
        self.is_click(user['IMEI/SN管理选择框'])
        self.is_click(user['IMEI/SN管理'],variable)

    @allure.step("新增商品信息")
    def add_goodinfo(self):
        self.is_click(user['商品信息新增按钮'])

    @allure.step("点击保存")
    def click_preserve(self):
        self.is_click(user['点击保存按钮'])
        sleep(3)

class QueryGood(Page_Operation,General_button):
    """按条件查询商品"""
    select_list1 = {"商品管理-产品名称框":"商品管理-产品名称","商品管理-自采标记框":"商品管理-自采标记"}
    select_list2 = {"商品管理-区域框":"商品管理-区域","商品管理-品牌名称框":"商品管理-品牌名称","商品管理-IMEI/SN管理框":"商品管理-IMEI/SN管理","商品管理-创建人框":"商品管理-创建人"}
    def querygood(self,select,content,ele2=None,enddate=None):
        if select in self.select_list1:
            self.single_condition_input_boxquery(select,self.select_list1[select],content)
            sleep()
            self.query()
        elif select in self.select_list2:
            self.more()
            sleep()
            self.single_condition_input_boxquery(select,self.select_list2[select],content)
            sleep()
            self.more_query()
        elif select == "商品管理-开始日期框":
            self.date_range(select,ele2,content,enddate)
            self.query()
        else:
            logging.error("系统检测没有此筛选项，请检查后重新输入")

class ExportGood(Base):
    """导出商品管理类"""

    @allure.step("点击导出")
    def click_export(self):
        self.is_click_tbm(user['导出'])



if __name__ == '__main__':
    pass
