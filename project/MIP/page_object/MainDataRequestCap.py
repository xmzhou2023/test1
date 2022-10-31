import logging
import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from ..test_case.conftest import *
import random
import string
import re

object_name = os.path.basename(__file__).split('.')[0]
requestCap = Element(pro_name, object_name)


class MainDataRequestCap(Base):
    """主数据-请购上限管理"""

    @allure.step("输入并选择物料编码")
    def input_itemCode(self, itemCode):
        self.is_click(requestCap['物料编码文本框'])
        self.input_text(requestCap['物料编码文本框'],itemCode)
        self.is_click(requestCap['下拉选项'],itemCode)
        logging.info("输入并选择物料编码：{}".format(itemCode))

    @allure.step("选择品牌")
    def choice_brand(self, brand):
        self.is_click(requestCap['品牌下拉'])
        self.is_click(requestCap['下拉选项'],brand)
        logging.info("选择品牌：{}".format(brand))

    @allure.step("选择状态")
    def choice_status(self, status):
        self.is_click(requestCap['状态下拉'])
        self.is_click(requestCap['下拉选项'],status)
        logging.info("选择状态：{}".format(status))

    @allure.step("点击查询按钮")
    def button_query(self):
        self.is_click(requestCap['查询 按钮'])
        logging.info("点击查询按钮")

    @allure.step("点击重置按钮")
    def button_reset(self):
        self.is_click(requestCap['重置 按钮'])
        logging.info("点击重置按钮")

    @allure.step("点击新增按钮")
    def button_newly(self):
        self.is_click(requestCap['新增 按钮'])
        sleep(1)
        txt = self.element_text(requestCap['弹出窗 断言'])
        assert txt == "新增", logging.warning("断言失败，新增窗口打开失败")
        logging.info("点击新增按钮，弹出新增窗口")

    @allure.step("维护弹窗信息")
    def edit_info(self,itemcode=None,upperLimit=None):
        self.is_click(requestCap['弹出窗 物料编码文本框'])
        self.input_text(requestCap['弹出窗 物料编码文本框'],itemcode)
        self.is_click(requestCap['下拉选项'],itemcode)
        self.is_click(requestCap['弹出窗 申请上限(箱)文本框'])
        self.input_text(requestCap['弹出窗 申请上限(箱)文本框'],upperLimit)
        self.is_click(requestCap['弹出窗 保存按钮'])
        sleep(2)
        # self.refresh()

    @allure.step("获取列表数据数量，用做断言")
    def get_listNum(self):
        txt = self.element_text(requestCap['获取列表数量'])
        num = re.findall(" (.*?) ", txt)[0]
        logging.info("列表数据数量：{}".format(num))
        return int(num)

    @allure.step("查询数据库 用做断言")
    def get_sqlResult(self, sql):
        user = SQL("MIP", "test")
        num = user.query_db(sql)
        num1 = [item[key] for item in num for key in item]
        logging.info("查询数据库数量：{}".format(num1[0]))
        return num1[0]

    @allure.step("清空测试数据")
    def clear_testData(self, itemcode):
        user = SQL("MIP", "test")
        user.delete_db("DELETE from mm_req_list_limit where mat_code = '{}' and enable_flag ='1'".format(itemcode))
        logging.info("清空测试数据")

    @allure.step("获取置灰文本")
    def get_hiddenText(self, ClassName, index):
        """获取置灰文本(用js)"""
        txt = self.driver.execute_script("document.getElementsByClassName('{}')[{}].value".format(ClassName, index))
        logging.info("获取隐藏文本：{}".format(txt))
        return txt
