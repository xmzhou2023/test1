import allure, os
from public.base.basics import Base,sleep
from public.base.assert_ui import SQLAssert
from libs.common.read_element import Element
import logging
from project.POP.test_case.conftest import *
from project.POP.page_object.Center_Component import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class Query_GoodDetail(Base):
    """查看参数详情类"""

    @allure.step("点击详情")
    def click_detail(self):
        self.is_click(user['参数详情按钮'])
        sleep(1)

class ExportGoodParam(Base):
    """导出商品参数类"""

    @allure.step("点击导出")
    def click_export(self):
        self.is_click_tbm(user['导出'])

class QueryGoodParameter(Page_Operation,General_button):
    """按条件查询商品参数"""
    select_list1 = {"商品参数-参数名称框":"商品参数-参数名称","商品参数-参数状态框":"商品参数-参数状态"}
    select_list2 = {"商品参数-创建人框":"商品参数-创建人"}
    def querygoodparam(self,select,content,ele2=None,enddate=None):
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
        elif select == "商品参数-开始日期框":
            self.date_range(select,ele2,content,enddate)
            self.query()
        else:
            logging.error("系统检测没有此筛选项，请检查后重新输入")

if __name__ == '__main__':
    pass
