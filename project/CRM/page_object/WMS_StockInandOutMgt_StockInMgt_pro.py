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

class StockInSearch(Base):
    """入库单查询类"""
    given_data = datetime.today().date()
    logging.info('今天的日期: {} '.format(given_data))
    first_day_of_month = given_data.replace(day=1)
    logging.info('本月的第一天是:{}'.format(first_day_of_month))

    @allure.step("入库单查询")
    def stockinsearch(self, scope, type=None):
        self.refresh()
        self.wait.until(EC.presence_of_element_located(user["入库单开始日期搜索框"]), message="页面刷新失败")
        self.is_click(user['入库单开始日期搜索框'])
        self.hover(user['入库单开始日期搜索框'])
        self.is_click(user['清除时间搜索框'])
        self.is_click(user['入库单开始日期搜索框'])
        self.input_text(user['入库单开始日期搜索框'], txt=str(StockInSearch.first_day_of_month))
        sleep(2)
        self.input_text(user['入库单type字段输入框'], txt=type)
        self.hover(user["入库单type字段下拉选择框"], choice=type)
        self.find_element(user['入库单type字段下拉选择框'], type).click()
        self.is_click(user['Search按钮'])
        sleep(10)



    # def stock_search(self, stock):
    #     sql = SQL('CRM', 'test')
    #     if stock == "all":
    #         # 查询序列化工单所有数据
    #         record = sql.query_db("SELECT count(*) FROM crm_wms_stockin WHERE is_deleted=0 AND is_enable=1")
    #
    #         logging.info("数据库查询了第一条语句")
    #     else:
    #         # 根据国家和时间过滤查询序列化工单数据
    #         record = sql.query_db("SELECT count(*) FROM crm_wms_stockin WHERE stockin_type_id = 'IN007' and creation_time >= '{}' and is_deleted=0 AND is_enable=1".format(StockInSearch.first_day_of_month))
    #         logging.info("数据库查询了第二条语句")
    #     dict_record = record[0]
    #     print(dict_record)
    #     record_value = dict_record['count(*)']
    #     logging.info('数据库查询到的序列化工单报表数据为:{}'.format(record_value))
    #     search_num = self.get_element_attribute(user['入库单总数'], 'textContent')
    #     num = ''.join(filter(str.isdigit, search_num))
    #     num = int(num)
    #     logging.info('序列化工单报表查询页查到的数量:{}'.format(num))
    #     return record_value, num











if __name__ == '__main__':
    pass
