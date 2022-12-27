import allure, os
from public.base.basics import Base,sleep
from public.base.assert_ui import SQLAssert
from libs.common.read_element import Element
from pykeyboard import PyKeyboard
import logging
from project.POP.test_case.conftest import *
from project.POP.page_object.Center_Component import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

# class AddGoodParam(Base):
#     """新增商品参数类"""
#
#     @allure.step("点击新增")
#     def click_add(self):
#         self.is_click(user['参数新增按钮'])
#
#     @allure.step("输入参数名称")
#     def input_paramname(self,content):
#         self.input_text(user['参数名称输入框'],content)
#
#     @allure.step("选择商品类目")
#     def switch_category(self):
#         self.is_click_tbm(user['商品类目选择框'])
#         sleep(1)
#         # 由于商品类目输入框不能输入参数，下拉框展示数据不能定位元素，暂定措施默认全选所有类目（定位输入框，点击回车键即可）
#         key = PyKeyboard()  # 实例化一个键盘
#         key.press_key(key.enter_key)  # 按下enter键
#         sleep(0.5)
#
#     @allure.step("选择展示形式")
#     def switch_display_form(self,content):
#         self.is_click(user['展示形式选择框'])
#         self.is_click(user['展示形式'],content)
#
#     @allure.step("选择展示顺序")
#     def switch_order(self,content):
#         self.input_text(user['展示顺序输入框'],content)
#
#     @allure.step("默认输入三个参数值")
#     def input_parameters(self,param,param2,param3):
#         self.input_text(user['参数值输入框'],param)
#         # 点击add增加参数值行数
#         self.is_click(user['add按钮'])
#         self.input_text(user['参数值输入框2'], param2)
#         self.is_click(user['add按钮'])
#         self.input_text(user['参数值输入框3'], param3)
#
#     @allure.step("提交新增")
#     def click_submit(self):
#         self.is_click(user['提交按钮'])

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
