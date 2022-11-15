import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class PolicyPage(Base):
    """政策页"""

    @allure.step("筛选框查询")
    def search_policy(self,country=None, brand=None, project=None, keyword=None,status=None, countrycode=None):
        self.refresh()
        if country is not None:  # 判断输入筛选框
            self.is_click(user["筛选框"],choice="country")  # 点击country的筛选框
            self.input_text(user["筛选框"],choice="country",txt=country)  # 在country筛选框内，输入country变量的值
            logging.info("国家筛选框输入{}".format(country))
            sleep(0.5)
            self.is_click(user["下拉筛选框_第一条数据"])
        if brand is not None:
            self.is_click(user["筛选框"],choice="brandCategory")
            self.input_text(user["筛选框"],choice="brandCategory", txt=brand)
            logging.info("品牌品类筛选框输入{}".format(brand))
            sleep(0.5)
            self.is_click_tbm(user["下拉筛选框_第二条数据"])
        if project is not None:
            self.is_click(user["筛选框"],choice="projectName")
            self.input_text(user["筛选框"],choice="projectName", txt=project)
            logging.info("机型筛选框输入{}".format(project))
            sleep(0.5)
            self.is_click(user["下拉筛选框_第一条数据"])
        if keyword is not None:
            self.is_click(user["筛选框"], choice="keyword")
            self.input_text(user["筛选框"], choice="keyword", txt=keyword)
            logging.info("keyword筛选框输入{}".format(keyword))
            sleep(0.5)
        if status is not None:
            self.is_click(user["筛选框"], choice="isEnable")
            sleep(4)
            self.is_click(user["下拉框_启用禁用切换"])
            logging.info("status切换到禁用{}".format(status))
        if countrycode is not None:
            self.is_click(user["筛选框"],choice="countryCode")
            self.input_text(user["筛选框"],choice="countryCode",txt=countrycode)
            logging.info("国家筛选框输入{}".format(countrycode))
            sleep(0.5)
            self.is_click(user["下拉筛选框_第一条数据"])
        self.is_click(user["搜索按钮"])
        sleep(0.5)

    def sql_search(self, countrycode=None, status=None, keyword=None):
        if countrycode is not None:
            user = SQL("CRM", "test")  # 链接数据库
            sql_search = user.query_db('SELECT COUNT(*) FROM crm_mdm_sunking_policy WHERE country_code = "{}"'.format(countrycode))
            sql_qty = sql_search[0].get("COUNT(*)")
        elif status is not None:
            user = SQL("CRM", "test")  # 链接数据库
            sql_search = user.query_db('SELECT COUNT(*) FROM crm_mdm_sunking_policy WHERE is_enable = "{}"'.format(status))
            sql_qty = sql_search[0].get("COUNT(*)")
        elif keyword is not None:
            user = SQL("CRM", "test")  # 链接数据库
            sql_search = user.query_db('SELECT COUNT(*) FROM crm_mdm_sunking_policy WHERE country_code = "SL" AND material_code = "{}"'.format(keyword))
            sql_qty = sql_search[0].get("COUNT(*)")
        return sql_qty




    def get_total(self):
        sleep(0.5)
        total = self.element_text(user["total数量"])
        logging.info("获取total文本{}".format(total))
        num = total.split(" ",1)
        number = num[1]
        return number


if __name__ == '__main__':
    pass
