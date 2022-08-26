import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class PlatformLibrary(Base):
    """平台库"""

    @allure.step("展开平台、物料状态、可用状态 下拉框")
    def screenCondition(self, condition):
        self.is_click(user['查询条件'],condition)
        logging.info("查询项:{}".format(condition))

    @allure.step("选择指定选项")
    def screenOption(self, condition, option):
        pullDown = self.find_elements(user['下拉列表'])
        optionList = []
        for i in range(len(pullDown)):
            optionList.append(pullDown[i].text)
        if option in optionList:
            self.is_click(user['输入框下拉'], option)
        elif option not in optionList:
            self.is_click(user['查询条件'], condition)
        else:
            self.is_click(user['筛选框断言'])
        logging.info("查询选项：{}".format(option))

    @allure.step("选择指定选项")
    def queryButton(self):
        self.is_click(user['查询按钮'])
        logging.info("点击查询按钮")



if __name__ == '__main__':
    pass



