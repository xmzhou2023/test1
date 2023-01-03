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



class QueryMaterial(Page_Operation,General_button):
    """按条件查询员工"""
    select_list1 = {"是否绑定商品框":"是否绑定商品","商品名称框":"商品名称","品牌名称框":"品牌名称"}
    select_list2 = {"市场名称框":"市场名称","物料名称框":"物料名称"}
    def querymaterial(self,select,content,ele2=None,enddate=None):
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
        elif select == "开始日期框":
            self.date_range(select,ele2,content,enddate)
            self.query()
        else:
            logging.error("系统检测没有此筛选项，请检查后重新输入")

class QueryMore(Base):
    """查看更多筛选条件"""

    @allure.step("点击更多")
    def click_more(self):
        self.is_click_tbm(user['更多按钮'])


class ExportMaterial(Base):
    """物料信息导出类"""

    @allure.step("点击导出")
    def click_export(self):
        self.is_click_tbm(user['导出'])


if __name__ == '__main__':
    pass
