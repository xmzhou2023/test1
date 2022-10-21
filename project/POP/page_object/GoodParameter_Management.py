import allure, os
from public.base.basics import Base,sleep
from public.base.assert_ui import SQLAssert
from libs.common.read_element import Element
from pykeyboard import PyKeyboard
import logging
from project.POP.test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AddGoodParam(Base):
    """新增商品参数类"""

    @allure.step("点击新增")
    def click_add(self):
        self.is_click(user['参数新增按钮'])

    @allure.step("输入参数名称")
    def input_paramname(self,content):
        self.input_text(user['参数名称输入框'],content)

    @allure.step("选择商品类目")
    def switch_category(self):
        self.is_click(user['商品类目选择框'])
        sleep(1)
        # 由于商品类目输入框不能输入参数，下拉框展示数据不能定位元素，暂定措施默认全选所有类目（定位输入框，点击回车键即可）
        key = PyKeyboard()  # 实例化一个键盘
        key.press_key(key.enter_key)  # 按下enter键
        key.release_key(key.enter_key)

    @allure.step("选择展示形式")
    def switch_display_form(self,content):
        self.is_click(user['展示形式选择框'])
        self.is_click(user['展示形式'],content)

    @allure.step("选择展示顺序")
    def switch_order(self,content):
        self.input_text(user['展示顺序输入框'],content)

    @allure.step("默认输入三个参数值")
    def input_parameters(self,param,param2,param3):
        self.input_text(user['参数值输入框'],param)
        # 点击add增加参数值行数
        self.is_click(user['add按钮'])
        self.input_text(user['参数值输入框2'], param2)
        self.is_click(user['add按钮'])
        self.input_text(user['参数值输入框3'], param3)

    @allure.step("提交新增")
    def click_submit(self):
        self.is_click(user['提交按钮'])

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

if __name__ == '__main__':
    pass
