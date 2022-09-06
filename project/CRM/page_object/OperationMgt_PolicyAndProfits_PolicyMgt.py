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
    def search_policy(self,country=None, brand=None, project=None, keyword=None):
        self.refresh()
        if country is not None:
            self.is_click(user["筛选框"],choice="country")
            self.input_text(user["筛选框"],choice="country",txt=country)
            logging.info("国家筛选框输入{}".format(country))
            sleep(0.5)
            self.is_click(user["下拉筛选框_第一条数据"])
        if brand is not None:
            self.is_click(user["筛选框"],choice="brandCategory")
            self.input_text(user["筛选框"],choice="brandCategory", txt=brand)
            logging.info("品牌品类筛选框输入{}".format(brand))
            sleep(0.5)
            self.is_click(user["下拉筛选框_第二条数据"])
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
        self.is_click(user["搜索按钮"])
        sleep(0.5)


    def get_total(self):
        sleep(0.5)
        total = self.element_text(user["total数量"])
        logging.info("获取total文本{}".format(total))
        num = total.split(" ",1)
        number = num[1]
        return number


if __name__ == '__main__':
    pass
