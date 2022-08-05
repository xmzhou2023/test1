import time

import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class LoginPage(Base):
    """登录类"""

    @allure.step("登录")
    def login(self,url,elsAccount,elsSubAccount):
        self.get_url(url)
        self.input_text(user["主账号"],txt=elsAccount)
        self.input_text(user["子账号"],txt=elsSubAccount)
        # self.input_text(user["密码"],txt=password)
        self.input_text(user["密码"],"1qaz@WSX")
        for i in range(10):
            self.is_click(user["验证码框"])
            code=self.get_graphical_code(user["验证码"])
            self.input_text(user["验证码框"],code)
            self.is_click(user["登录"])
            if "login" in self.driver.current_url:
                time.sleep(2)
                continue
            else:
                break
            # sub_errmsg = self.find_element(user["登录报错码提示框"]).text
            # try:
            #     sub_errmsg = self.find_element(user["登录报错码提示框"]).text
            #     print('errmsg',sub_errmsg)
            #     if '验证码错误' in sub_errmsg:
            #         self.is_click(user["验证码"])
            #         continue
            #     else:
            #         break
            # except:
            #     break








if __name__ == '__main__':
    pass
