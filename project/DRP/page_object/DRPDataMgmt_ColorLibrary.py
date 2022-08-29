import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class ColorLibrary(Base):
    """颜色库"""

    @allure.step("选择指定选项")
    def screenOption(self, condition,option):
        self.is_click(user['查询条件'],condition)
        self.input_text(user['查询条件'], option)
        logging.info("颜色：{}".format(option))

    @allure.step("点击查询按钮")
    def queryButton(self):
        self.is_click(user['查询按钮'])
        logging.info("点击查询按钮")






if __name__ == '__main__':
    pass
