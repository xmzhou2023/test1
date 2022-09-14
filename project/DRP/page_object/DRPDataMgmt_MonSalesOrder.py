import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
import re
import random
import string

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class MonSalesOrder(Base):
    """月度销售订单"""

    @allure.step("选择提报周期")
    def choose_reportedCycle(self, year=None, mom=None):
        self.is_click(user['查询条件 提报周期'])
        if year is not None:
            self.is_click(user['提报日期 年'])
            self.is_click(user['选择提报日期 年'], str(year))
            self.is_click(user['选择提报日期 月'], str(mom))
            logging.info("选择提报周期：{}年,{}".format(year,mom))
        else:
            self.is_click(user['选择提报日期 月'], str(mom))
            logging.info("选择提报周期：2022年,{}".format(mom))

    @allure.step("选择品牌")
    def choose_brand(self, brand):
        self.is_click(user['查询条件 品牌'])
        if brand == "Infinix":
            self.is_click(user['品牌_下拉选项'],"1")
        elif brand == "itel":
            self.is_click(user['品牌_下拉选项'],"2")
        elif brand == "TECNO":
            self.is_click(user['品牌_下拉选项'],"3")
        else:
            logging.info("品牌输入有误")
        logging.info("选择品牌：{}".format(brand))

    @allure.step("点击查询按钮")
    def query_button(self):
        self.is_click(user['查询按钮'])
        logging.info("点击查询按钮")

    @allure.step("点击重置按钮")
    def reset_button(self):
        self.is_click(user['重置按钮'])
        logging.info("点击重置按钮")

    @allure.step("返回提报数 用做断言")
    def get_listText(self,brand):
        dic_brand = {"TECNO":"1","itel":"2","Infinix":"3"}
        try:
            a = self.find_element(user['获取某品牌提报数'],dic_brand[brand])
            b = a.get_attribute("innerHTML")
            c = re.findall("<div>(.*?)</div>", b)[0]
            return c
        except Exception:
            a = self.find_element(user['获取某品牌提报数'],"1")
            b = a.get_attribute("innerHTML")
            c = re.findall("<div>(.*?)</div>", b)[0]
            return c

    @allure.step("查询数据库 用做断言")
    def SQL_assert(self, year= None, month= None, brand= None):
        user = SQL("DRP", "test")
        if month is not None:
            num = user.query_db(
                "select country_qty from md_nearly_3_week_sale_maintain where fyear = '{}' and fmonth = '{}' and brand_code = '{}';".format(
                    year,month, brand))
            for item in num:
                for k, v in item.items():
                    logging.info("获取数据库 提报数量:{}".format(v))
                    return str(v)
        else:
            num = user.query_db(
                "select count(*) from md_nearly_3_week_sale_maintain where fyear = '{}' and fmonth > 0 ;".format(
                    year))
            for item in num:
                for k, v in item.items():
                    logging.info("获取数据库 提报数量:{}".format(v))
                    return str(v)

    @allure.step("返回页面列表数据数量")
    def retrun_listNum(self):
        a = self.element_text(user['列表数据统计'])
        b = re.findall(" (.*?) ", a)[0]
        return b

    @allure.step("点击查看/编辑按钮")
    def check_details(self):
        a = self.element_text(user['获取 编辑/查看文本'],"1")
        if a== "编辑":
            self.is_click(user['点击 编辑/查看按钮'],"1")
            logging.info("点击编辑按钮")
        else:
            self.is_click(user['点击 编辑/查看按钮'],"1")
            logging.info("点击查看按钮")
        sleep(2)

    @allure.step("关闭编辑标签页")
    def close_tab(self,title):
        if title == "月度销售订单编辑":
            self.is_click(user['关闭标签页'],title)
            logging.info("关闭月度销售订单编辑 页签")
        elif title == "月度销售订单查看":
            self.is_click(user['关闭标签页'],title)
            logging.info("关闭月度销售订单查看 页签")














if __name__ == '__main__':
    pass