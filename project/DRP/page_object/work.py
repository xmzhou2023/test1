import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
pro_env = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, pro_env)

class jieru(Base):
    """区域管理"""

    @allure.step("前往树")
    def goto_tree(self, *content):
        for i in range(len(content)):
            if i == 0:
                self.is_click(user['表头itel事业部'], choice=content[0])
                sleep(2)
                self.is_click(user['一级itel事业部'], choice=content[0])
                sleep(2)
            elif i == 1:
                self.is_click(user['二级itel事业部'], choice=content[1])
                sleep(2)
            elif i == 2:
                self.is_click(user['三级itel事业部'], choice=content[2])
                sleep(2)
            elif i == 3:
                self.is_click(user['四级itel事业部'], choice=content[3])
                sleep(2)


if __name__ == '__main__':
    pass
