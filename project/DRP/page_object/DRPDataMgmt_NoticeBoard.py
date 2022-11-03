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


class NoticeBoard(Base):
    """通告板"""

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

    @allure.step("选择创建人")
    def choose_creatby(self, creatby):
        self.is_click(user['查询条件 创建人'])
        try:
            a = self.element_text(user['创建人_无下拉选项'])
            if a == "无数据":
                logging.info("此提报周期内 无通告数据")
        except:
            if creatby is True:
                self.is_click(user['品牌_下拉选项'], "1")
                logging.info("选择创建人：{}".format(creatby))

    @allure.step("输入通告标题")
    def enter_title(self,title):
        self.input_text(user['查询条件 通告标题'],title)
        logging.info("输入通告标题：{}".format(title))

    @allure.step("点击查询按钮")
    def query_button(self):
        self.is_click(user['查询按钮'])
        logging.info("点击查询按钮")
        sleep(2)

    @allure.step("点击重置按钮")
    def reset_button(self):
        self.is_click(user['重置按钮'])
        logging.info("点击重置按钮")

    @allure.step("返回通告标题 用做断言")
    def get_listText(self,brand):
        """
        断言问题待解决


        """
        s = self.element_text(user['列表数据统计'])
        print(s)
        s1 = s.split(" ")[1]
        print(s1)
        d = []
        for i in range(8):
            a = self.find_element(user['获取通告标题'], str(i+1))
            b = a.get_attribute("innerHTML")
            print(b)
            c = re.findall('<div class="cell">(.*?)</div>', b)
            print(c)
            d.append(c)
            print("通告标题有：",d)
            if i+1 > s1:
                break
        print("通告标题有：",d)
        assert brand in d ,logging.warning("断言失败")
        logging.info("断言成功")






    @allure.step("查询数据库 用做断言")
    def SQL_assert(self, year= None, month= None, brand= None):
        """查询通告标题"""
        user = SQL("DRP", "test")
        if month is not None:
            num = user.query_db(
                "select country_qty from md_round_off_maintain where fyear = '{}' and fmonth = '{}' and brand_code = '{}';".format(
                    year,month, brand))
            for item in num:
                for k, v in item.items():
                    logging.info("获取数据库 提报数量:{}".format(v))
                    return str(v)
        else:
            num = user.query_db(
                "select count(*) from md_round_off_maintain where fyear = '{}' and fmonth > 0 ;".format(
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
        self.is_click(user['点击 查看按钮'],"1")
        logging.info("点击查看按钮")
        sleep(2)

    @allure.step("关闭编辑标签页")
    def close_tab(self,title):
        self.is_click(user['关闭标签页'],title)
        logging.info("关闭月度清尾任务查看 页签")














if __name__ == '__main__':
    pass