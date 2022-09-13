import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from project.POP.test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class Query_GoodDetail(Base):
    """查看参数详情类"""

    @allure.step("点击详情")
    def click_detail(self,excpt):
        self.is_click(user['参数详情按钮'])
        # 断言
        test = self.element_text(user['参数详情'])
        ValueAssert.value_assert_equal(test,excpt)

if __name__ == '__main__':
    pass
