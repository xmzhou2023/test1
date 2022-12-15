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

class QueryCountry(Page_Operation,General_button):
    """查询类"""
    select_list = {"国家城市框": "国家城市", "是否禁用框": "是否禁用", "城市等级框": "城市等级"}
    def querycountry(self, select, content):
        if select in self.select_list:
            self.single_condition_input_boxquery(select, self.select_list[select], content)
            sleep()
            self.query()
        else:
            logging.error("系统检测没有此筛选项，请检查后重新输入")



class ExportCountryCity(Base):
    """导出国家城市列表类"""

    @allure.step("点击导出按钮")
    def click_export(self):
        self.is_click_tbm(user['导出'])



if __name__ == '__main__':
    pass
