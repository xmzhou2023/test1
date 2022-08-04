import time

import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class LoginPage(Base):
    """登录类"""

    @allure.step("登录")
    def login(self,elsAccount,elsSubAccount):
        self.input_text(user["主账号"],txt=elsAccount)
        self.input_text(user["子账号"],txt=elsSubAccount)
        # self.input_text(user["密码"],txt=password)
        self.input_text(user["密码"],"1qaz@WSX")
        self.is_click(user["验证码框"])
        code=self.get_graphical_code(user["验证码"])
        print(code)
        self.input_text(user["验证码框"],code)
        # time.sleep(3)
        self.is_click(user["登录"])








if __name__ == '__main__':
    pass
