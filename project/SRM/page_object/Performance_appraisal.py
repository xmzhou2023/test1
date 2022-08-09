import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class Performance(Base):
    """用户类"""

    @allure.step("查找工号")
    def PerformanceAppraisal(self):
        self.is_click(user['供应商绩效'])
        sleep()

if __name__ == '__main__':
    pass
