import string
from datetime import datetime
from selenium.webdriver.common.by import By

import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from .Center_Component import NavPage
from ..test_case.conftest import *
import random

object_name = os.path.basename(__file__).split('.')[0]

user = Element(pro_name, object_name)


class AllocationSearch(Base):
    """入库单查询类"""
    # given_data = datetime.today().date()
    # logging.info('今天的日期: {} '.format(given_data))
    # first_day_of_month = given_data.replace(day=1)
    # logging.info('本月的第一天是:{}'.format(first_day_of_month))

    @allure.step("调拨单查询")
    def allocationsearch(self):
        self.refresh()
        self.wait.until(EC.presence_of_element_located(user["调拨单开始日期搜索框"]), message="页面刷新失败")
        self.is_click(user['调拨单开始日期搜索框'])
        self.hover(user['调拨单开始日期搜索框'])
        self.is_click(user['清除时间搜索框'])
        self.is_click(user['调拨单开始日期搜索框'])
        self.input_text(user['调拨单开始日期搜索框'], txt="2022-09-01")
        sleep(1)
        self.is_click(user['调拨单结束日期搜索框'])
        self.hover(user['调拨单结束日期搜索框'])
        self.is_click(user['清除结束日期搜索框'])
        self.input_text(user['调拨单结束日期搜索框'], txt="2022-09-30")
        sleep(1)
        self.is_click(user['Search按钮'])
        sleep(5)








if __name__ == '__main__':
    pass
