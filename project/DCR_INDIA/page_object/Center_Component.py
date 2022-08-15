import logging
import os
import allure
from libs.common.read_config import ReadConfig
from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
pro_env = 'prod' # 需要手动配置测试环境
user = Element(pro_name, object_name)
ini = ReadConfig(pro_name, pro_env)


class LoginPage(Base):
    """DCR登录类"""
    def input_account(self, content):
        """输入工号"""
        self.input_text(user['工号输入框'], txt=content)
        sleep(1)

    def input_passwd(self, content):
        """输入密码"""
        self.input_text(user['密码输入框'], txt=content)
        sleep(1)

    def switch_lanuage(self, content):
        """语言切换"""
        self.is_click(user['语言切换'])
        self.is_click(user['选择英文'], content)

    def click_check_box(self):
        """判断是否被选中"""
        self.is_click(user['隐私保护勾选'])
        sleep(1)

    def get_check_box_class(self):
        """获取复选框对应的 Class属性是否包含is-checked"""
        ss = self.find_element(user['隐私保护勾选'])
        get_check_state = ss.get_attribute('class')
        return get_check_state

    def check_box(self):
        """判断是否被选中"""
        checkbox = self.select_state(user['隐私保护勾选'])
        return checkbox

    def click_loginsubmit(self):
        """点击帐号密码登录"""
        self.is_click(user['登录'])
        sleep(8)

    def click_loginOut(self):
        """点击退出登录"""
        sleep(2)
        self.is_click(user['退出登录'])
        sleep(2)


    @allure.step("登录方法")
    def dcr_login(self, drivers, account, passwd):
        #user = LoginPageDCR(drivers)
        self.get_url(ini.url)
        sleep(7)
        self.input_account(account)
        self.input_passwd(passwd)
        sleep(1)
        get_check_class = self.get_check_box_class()
        if "is-checked" not in str(get_check_class):
            self.click_check_box()
        self.click_loginsubmit()


    @allure.step("点击菜单")
    def click_gotomenu(self, *content):
        """前往左侧菜单栏"""
        level = []
        navstr = ""
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        for i in range(len(content)):
            logging.info(user[level[i]])
            sleep(3.5)
            self.scroll_into_view(user[level[i]])
            sleep(4)
            self.is_click(user[level[i]])
        sleep(5)



if __name__ == '__main__':
    pass
