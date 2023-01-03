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

class QueryShopApproval(Page_Operation, General_button):
    """按条件查询门店审批"""
    select_list1 = {"门店审批-门店框": "门店审批-门店", "门店审批-组织框": "门店审批-组织", "门店审批-国家框": "门店审批-国家","门店审批-状态框":"门店审批-状态"}
    select_list2 = {"门店审批-区域框":"门店审批-区域"}

    def queryhopapproval(self, select, content, ele2=None, enddate=None):
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
        elif select == "开始日期框":
            self.date_range(select, ele2, content, enddate)
            self.query()
        else:
            logging.error("系统检测没有此筛选项，请检查后重新输入")

if __name__ == '__main__':
    pass
