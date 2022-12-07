import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
import datetime
import string
import random
import logging

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AssetsMgtPage(Base):
    """AssetsMgt页"""

    @allure.step("获取列表第某列文本值")
    def get_columnValue(self, choice):
        self.refresh()
        eles = self.find_elements(user["第某列文本"], choice)
        columnValue = []
        for n in eles:
            columnValue.append(n.text)
        return columnValue

    @allure.step("筛选框查询")
    def firsttype_search(self, Firsttype):
        self.is_click(user["筛选框"], "firstType")
        self.input_text(user["筛选框"], Firsttype, "firstType")
        sleep(1)
        if Firsttype == "Office Equipment":
            self.is_click(user["下拉筛选框数据"], 2)
        elif Firsttype == "Publicity Materials":
            self.is_click(user["下拉筛选框数据"], 3)
        elif Firsttype == "Warehouse Materials":
            self.is_click(user["下拉筛选框数据"], 4)
        else:
            self.is_click(user["下拉筛选框数据"], 1)
        sleep(1)
        self.is_click(user["搜索按钮"])

    @allure.step("sql查询")
    def SQL_search(self, Firsttype):
        user = SQL("CRM", "test")  # 链接数据库
        if Firsttype == "Office Equipment":
            s_ser = user.query_db('SELECT COUNT(*) FROM crm_wms_assets_code_application WHERE first_type = "FT001"')
            sql_qty = s_ser[0].get("COUNT(*)")
            logging.info("数据库获取的Office Equipment数量:{}".format(sql_qty))
        elif Firsttype == "Publicity Materials":
            s_ser = user.query_db('SELECT COUNT(*) FROM crm_wms_assets_code_application WHERE first_type = "FT003"')
            sql_qty = s_ser[0].get("COUNT(*)")
            logging.info("数据库获取的Publicity Materials数量:{}".format(sql_qty))
        elif Firsttype == "Warehouse Materials":
            s_ser = user.query_db('SELECT COUNT(*) FROM crm_wms_assets_code_application WHERE first_type = "FT004"')
            sql_qty = s_ser[0].get("COUNT(*)")
            logging.info("数据库获取的Warehouse Materials数量:{}".format(sql_qty))
        else:
            s_ser = user.query_db('SELECT COUNT(*) FROM crm_wms_assets_code_application WHERE first_type = "FT002"')
            sql_qty = s_ser[0].get("COUNT(*)")
            logging.info("数据库获取的Repair Tools数量:{}".format(sql_qty))
        return sql_qty



if __name__ == '__main__':
    pass
