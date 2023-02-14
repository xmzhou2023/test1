import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class UserPage(Base):
    """用户类"""

    @allure.step("查找工号")
    def search_user(self, jobnum=None,name=None):
        if jobnum is not None:
            self.readonly_input_text(user['用户管理-工号输入框'], txt=jobnum)
            sleep(2)
            self.is_click(user['用户管理-工号下拉列表'], jobnum)
        if name is not None:
            self.readonly_input_text(user['用户管理-姓名输入框'], txt=name)
            sleep(2)
            self.is_click(user['用户管理-姓名下拉列表'], name)
        self.is_click(user['用户管理-查询'])
        sleep()


class CompetitorSalesQuery(Base):
    """用户类"""

    @allure.step("输入上传日期")
    def input_upload_date(self, startdate,enddate):
        self.is_click(user['上传日期开始'])
        self.input_text(user['上传日期开始'], txt=startdate)
        self.is_click(user['上传日期结束'])
        self.input_text(user['上传日期结束'], txt=enddate)
        sleep()

    @allure.step("选择品牌")
    def select_sale_brand(self, variable):
        self.is_click(user['brand品牌'])
        self.input_text(user['brand输入'], txt=variable)
        self.is_click(user['brand选择'],variable)
        self.is_click(user['销售区域'])

    @allure.step("选择销售区域")
    def select_sale_area(self, variable):
        self.is_click(user['销售区域'])
        self.input_text(user['销售区域'], txt=variable)
        sleep()
        self.is_click(user['选择销售区域'],variable)
        sleep()

    @allure.step("选择门店")
    def select_shop(self, variable):
        self.is_click(user['门店'])
        self.input_text(user['门店输入'], txt=variable)

    @allure.step("展开折叠")
    def click_unfold(self):
        self.is_click(user['展开折叠'])

    @allure.step("点击重置")
    def click_reset(self):
        self.is_click(user['重置'])
        self.element_exist(user['Loading'])

    @allure.step("点击查询")
    def click_search(self):
        self.is_click(user['查询'])
        self.element_exist(user['Loading'])

    @allure.step("获取表格文本")
    def get_table_txt(self,num):
        txt = self.element_text(user['列表第一行'],num)
        return txt

    @allure.step("输入销售日期")
    def input_sales_date(self, startdate,enddate):
        self.is_click(user['销售日期开始'])
        self.input_text(user['销售日期开始'], txt=startdate)
        self.is_click(user['销售日期结束'])
        self.input_text(user['销售日期结束'], txt=enddate)
        sleep()

    @allure.step("输入国家/城市")
    def input_country(self, country):
        self.is_click(user['国家输入'])
        self.input_text(user['国家输入'], txt=country)
        self.is_click(user['国家选择'],country)
        sleep()

    @allure.step("点击导出按钮")
    def click_export(self):
        self.is_click(user['导出'])

    @allure.step("获取导出状态")
    def export_status(self):
        txt=self.element_text(user['导出状态'])
        return txt


if __name__ == '__main__':
    pass
