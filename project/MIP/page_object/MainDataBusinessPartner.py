import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
import random
import string
import re

object_name = os.path.basename(__file__).split('.')[0]
data = Element(pro_name, object_name)


class MainDataBusinessPartner(Base):
    """主数据- BP主数据"""

    @allure.step("输入BP编码查询条件")
    def input_BPCode(self, itemL=None, itemR=None, scene=None):
        """多选功能没用"""
        if scene is None:
            self.input_text(data['BP编码 左'], itemL)
            self.input_text(data['BP编码 右'], itemR)
            logging.info("输入BP编码 {}到{}".format(itemL, itemR))
        elif scene == "单一物料查询":
            self.input_text(data['BP编码 左'], itemL)
            logging.info("输入BP编码 {}".format(itemL))
        elif scene == "到某一物料截止":
            self.input_text(data['BP编码 右'], itemR)
            logging.info("输入BP编码 0到{}".format(itemR))

    @allure.step("选择地区查询条件")
    def choice_region(self, region):
        self.is_click(data['地区下拉'])
        self.input_text(data['地区下拉'],region)
        self.is_click(data['选择下拉项'],region)
        logging.info("选择地区：{}".format(region))

    @allure.step("输入BP名称查询条件")
    def input_BPName(self, BPName):
        self.input_text(data['BP名称 文本框'], BPName)
        logging.info("输入BP名称：{}".format(BPName))

    @allure.step("选择省/邦查询条件")
    def choice_province(self, province):
        self.is_click(data['省或邦 下拉'])
        self.is_click(data['选择下拉项'],province)
        logging.info("选择省/邦：{}".format(province))

    @allure.step("输入联系人查询条件")
    def input_contacts(self, contacts):
        self.input_text(data['联系人 文本框'], contacts)
        logging.info("输入联系人：{}".format(contacts))

    @allure.step("选择BP类型查询条件")
    def choice_BPType(self, BPType=None):
        if BPType is not None:
            self.is_click(data['BP类型 下拉'])
            self.is_click(data['选择下拉项'],BPType)
            logging.info("选择BP类型：{}".format(BPType))
        else:
            self.button_query()
            txt = self.element_text(data['BP类型 必填报错信息'])
            assert txt == 'BP类型 不能为空',logging.info("断言失败")
            logging.info("断言成功，BP类型为空，查询失败")
            self.refresh()

    @allure.step("输入城市查询条件")
    def input_city(self, city):
        self.input_text(data['城市 文本框'], city)
        logging.info("输入城市：{}".format(city))

    @allure.step("展开 高级搜索")
    def button_spread(self):
        txt = self.element_text(data['展开 按钮'])
        if txt == "展开":
            self.is_click(data['展开 按钮'])
            logging.info("展开 高级搜索")
            sleep(1)
        else:
            self.is_click(data['收起 按钮'])
            logging.info("收起 高级搜索")

    @allure.step("点击查询按钮")
    def button_query(self):
        self.is_click(data['查询 按钮'])
        logging.info("点击查询按钮")
        sleep(1)

    @allure.step("点击查看详情按钮")
    def button_viewDetails(self):
        self.is_click(data['查看详情 按钮'])
        logging.info("点击查看详情按钮")
        sleep(1)

    @allure.step("点击清空按钮 清空查询条件")
    def button_empty(self):
        self.is_click(data['清空 按钮'])
        logging.info("点击清空按钮")
        sleep(1)

    @allure.step("获取列表数据数量，用做断言")
    def get_listNum(self):
        txt = self.element_text(data['获取列表数量'])
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

    @allure.step("返回BP主数据页面")
    def return_BPMianDataPage(self):
        self.is_click(data['BP 主数据页面'])
        logging.info("返回BP 主数据页面")
        sleep(1)

    @allure.step("勾选主数据")
    def select_itemData(self,selectorMode=None):
        if selectorMode is None:
            self.is_click(data['复选框'],str(1))
            logging.info("勾选主数据")
        else:
            self.is_click(data['全选'])
            logging.info("全选主数据")

    @allure.step("获取详情页 BP编码文本，用做断言")
    def return_BPCode(self):
        txt = self.element_input_text(data['获取 BP编码'])
        logging.info("获取详情页BP编码：{}".format(txt))
        return txt

    @allure.step("点击列表中的BP编码")
    def hyperlink_BPCode(self, BPCode):
        txt = self.element_text(data['BP编码'],str(1))
        if txt == BPCode:
            self.is_click(data['BP编码'],str(1))
            logging.info("点击列表中的BP编码：{}，进入详情页".format(txt))
        else:
            logging.info("查询结果与预期结果不一致")
        sleep(1)



if __name__ == '__main__':
    pass