import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class GoodSearch(Base):
    """商品类目搜索类"""

    @allure.step("输入商品类目")
    def input_goodcategory(self,category):
        self.is_click_tbm(user['商品类目搜索框'])
        self.input_text(user['商品类目搜索框'],category)
        sleep(1)
        self.is_click_tbm(user['搜索的商品类目'],category)




if __name__ == '__main__':
    pass
