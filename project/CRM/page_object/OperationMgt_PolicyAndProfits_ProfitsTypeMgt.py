import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
import string
import random

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ProfitsType(Base):
    """页面操作类"""

    @allure.step("权益类型配置页查询")
    def search_data(self,classname,choice):
        self.input_text(user["筛选按钮"],classname)
        self.is_click(user["搜索按钮"])
        try:
            self.find_element(user["无数据"])
            logging.info("查询的内容{}".format("无数据"))
        except:
            pass
        self.hover(user["筛选按钮"],choice)
        self.wait.until(EC.presence_of_element_located(user["筛选按钮"]),message="悬浮关闭按钮未显示")
        self.is_click(user["关闭筛选"])
        self.is_click(user["搜索按钮"])

    @allure.step("获取profitcode的值")
    def get_columnValue(self):
        eles = self.find_elements(user["ProfitCode一列的name"])
        columnValue = []
        for n in eles:
            columnValue.append(n.text)
        return columnValue


    # @allure.step("权益配置页新增重复校验")
    # def add_duplicate(self, classname):
    #     self.is_click(user['add按钮'])
    #     self.wait.until(EC.presence_of_element_located(user["ProfitCode输入框"]), message="warrantyclass字段不显示")
    #     self.input_text(user["ProfitCode输入框"], classname)
    #     self.input_text(user["ProfitCode输入框"], classname)


    # @allure.step("权益配置页新增弹框点击保存")
    # def click_save(self):
    #     self.is_click(user["save"])


    # @allure.step("新增框点击取消按钮")
    # def click_cancel(self):
    #     self.is_click(user["cancel"])
    #     self.wait.until(EC.presence_of_element_located(user["关闭弹窗上的confirm"]), message="关闭弹窗未出现")
    #     self.is_click(user["关闭弹窗上的confirm"])


    # @allure.step("获取输入文本纯数字name")
    # def get_Numbers(self):
    #     num = string.digits
    #     Numbers = "".join(random.sample(num, 5))
    #     return Numbers
    #
    #
    # @allure.step("获取输入文本数字+字母的name1")
    # def get_Numbersletters(self):
    #     num = string.ascii_letters + string.digits
    #     Numbersletters = "".join(random.sample(num, 5))
    #     return Numbersletters

    #
    # @allure.step("点击新增按钮")
    # def add_click(self):
    #     self.is_click(user['add按钮'])  # 点击add按钮


    @allure.step("对新增页输入行输入内容并保存")
    def input_profitline(self, txt):
        self.wait.until(EC.presence_of_element_located(user["ProfitCode输入框"]), message="添加页面加载失败")
        self.input_text(user["ProfitCode输入框"], txt)  # 输入内容
        self.input_text(user["ProfitDesc输入框"], txt)


    # @allure.step("编辑保修期限基础数据")
    # def edit_WarrantyDuration(self):
    #     self.is_click(user["第一行edit按钮"])


    # @allure.step("确认禁用弹框点击确定")
    # def disable(self):
    #     self.is_click(user["第一行enable按钮"])
    #     self.wait.until(EC.presence_of_element_located(user["确认disable弹窗的Yes按钮"]), message="确认禁用的弹窗未出现")
    #     self.is_click(user["确认disable弹窗的Yes按钮"])

if __name__ == '__main__':
    pass
