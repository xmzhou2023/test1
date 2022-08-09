import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
from datetime import datetime

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class WONonSerializedReport(Base):
    """非序列化工单报表"""

    @allure.step("选择开始时间")
    def input_date(self):

        """查询区域"""
        given_data = datetime.today().date()
        logging.info('今天的日期: {} '.format(given_data))
        first_day_of_month = given_data.replace(day=1)
        logging.info("输入框键入{}".format(first_day_of_month))
        self.input_text(user["WO Non Serialized Date开始日期搜索框"], str(first_day_of_month))
        sleep(1)

    @allure.step("选择国家")
    def input_country(self):
        """查询区域"""
        self.is_click(user["Country搜索框"])

        # logging.info("输入框键入{}".format())
        self.hover(user['Country下拉选择'], choice='SL')
        self.is_click(user["Country下拉选择"])
        # self.input_text(user["Country搜索框"], 'SL')
        sleep(1)

    @allure.step("执行报表查询")
    def search_report(self):
        """查询区域"""
        self.is_click(user['WO NonSerialized Report Search'])
        sleep(1)

    @allure.step("清空时间搜索框")
    def clear_date(self):
        self.is_click(user['清除时间搜索框'])
        # logging.info("输入框键入{}".format())
        sleep(1)

    @allure.step("清空国家搜索框")
    def clear_country(self):
        self.is_click(user['清除国家搜索框'])
        # logging.info("输入框键入{}".format())
        sleep(1)

    @allure.step("鼠标在时间搜索框悬停")
    def Stop_date(self):
        given_data = datetime.today().date()
        logging.info('今天的日期: {} '.format(given_data))
        first_day_of_month = given_data.replace(day=1)
        logging.info("First day of month:{}".format(first_day_of_month))

        self.hover(user['WO Non Serialized Date开始日期搜索框'], choice='first_day_of_month')
        # logging.info("输入框键入{}".format())
        sleep(1)

    @allure.step("鼠标在国家搜索框悬停")
    def Stop_country (self):
        self.hover(user['Country搜索框'], choice='SL')

        sleep(1)

    @allure.step("获取报表数据总量")
    def get_total(self):
        num = self.get_element_attribute(user['报表总数'], 'textContent')
        print(num)
        # logging.info("报表总数是:{}".format(''))
        return num
        sleep(1)

    @allure.step("报表导出")
    def download_report(self):
        self.is_click(user['WO NonSerialized Report Export'], 'Export')
        # self.alert_ok()
        self.is_click(user['确认导出'], 'OK')
        # logging.info("输入框键入{}".format(content))
        sleep(1)


if __name__ == '__main__':
    pass
