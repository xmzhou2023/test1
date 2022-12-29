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

class GoodSearch(Base):
    """商品类目搜索类"""

    @allure.step("输入商品类目")
    def input_goodcategory(self,category):
        self.is_click_tbm(user['商品类目搜索框'])
        self.input_text(user['商品类目搜索框'],category)
        sleep(1)
        self.is_click_tbm(user['搜索的商品类目'],category)

class QueryGood(Page_Operation,General_button):
    """按条件查询商品"""
    select_list1 = {"商品列表-商品名称框":"商品列表-商品名称","商品列表-自采标记框":"商品列表-自采标记"}
    select_list2 = {"商品列表-区域框":"商品列表-区域","商品列表-品牌名称框":"商品列表-品牌名称","商品列表-产品名称框":"商品列表-产品名称","商品列表-商品状态框":"商品列表-商品状态","商品列表-IMEI/SN管理框":"商品列表-IMEI/SN管理","商品列表-创建人框":"商品列表-创建人"}
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
        elif select == "商品列表-开始日期框":
            self.date_range(select,ele2,content,enddate)
            self.query()
        else:
            logging.error("系统检测没有此筛选项，请检查后重新输入")


class ExportList(Base):
    """导出商品列表类"""

    @allure.step("点击导出")
    def click_export(self):
        self.is_click_tbm(user['导出'])


if __name__ == '__main__':
    pass
