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


class SupplierManagement(Page_Operation,General_button):
    """查询类"""
    select_list1 = {"卖家名称框": "卖家", "卖家类型框": "卖家类型", "卖家国家框": "卖家国家","供应商门店框":"供应商门店"}
    select_list2 = {"门店国家框": "门店国家", "归属机构框": "归属机构"}
    def querysupplier(self, select, content):
        if select in self.select_list1:
            self.single_condition_input_boxquery(select, self.select_list1[select], content)
            sleep()
            self.query()
        elif select in self.select_list2:
            self.more()
            sleep()
            self.single_condition_input_boxquery(select, self.select_list2[select], content)
            sleep()
            self.more_query()
        else:
            logging.error("系统检测没有此筛选项，请检查后重新输入")

    @allure.step("点击更多")
    def click_more(self):
        self.is_click_tbm(user['更多按钮'])

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
