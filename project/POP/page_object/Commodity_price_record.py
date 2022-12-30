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

class QueryCommodityPrice(Page_Operation,General_button):
    """按条件查询商品定义价格"""
    select_list1 = {"商品价格记录-商品名称框":"商品价格记录-商品名称","商品价格记录-品牌名称框":"商品价格记录-品牌名称","商品价格记录-产品名称框":"商品价格记录-产品名称"}
    select_list2 = {"商品价格记录-自采标记框":"商品价格记录-自采标记","商品价格记录-区域框":"商品价格记录-区域","商品价格记录-创建人框":"商品价格记录-创建人"}
    def querycommodityprice(self,select,content,ele2=None,enddate=None):
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
        elif select == "商品价格记录-开始日期框":
            self.date_range(select,ele2,content,enddate)
            self.query()
        else:
            logging.error("系统检测没有此筛选项，请检查后重新输入")



if __name__ == '__main__':
    pass
