from public.base.basics import Base
from libs.common.read_element import Element
from libs.common.time_ui import sleep
from libs.common.read_config import *
from ..test_case.conftest import *
import logging

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)
ini = ReadConfig(pro_name, "prod")


class DCRLoginPage(Base):
    """DCR登录类"""
    def input_account(self, content):
        """输入工号"""
        self.input_text(user['工号输入框'], txt=content)

    def input_passwd(self, content):
        """输入密码"""
        self.input_text(user['密码输入框'], txt=content)

    def switch_lanuage(self, content):
        """语言切换"""
        self.is_click(user['语言切换'])
        self.is_click(user['选择英文'], content)

    def click_check_box(self):
        """判断是否被选中"""
        self.is_click(user['隐私保护勾选'])

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

    def click_loginOut(self):
        """点击退出登录"""
        sleep(2)
        self.is_click(user['退出登录'])
        sleep(2)

    @allure.step("进入首页，获取当前登录用户名")
    def get_login_user_name(self):
        self.element_text(user['首页当前登录用户'])


    @allure.step("获取当前打开状态的菜单class值")
    def get_open_menu_class(self):
        ss = self.find_element(user['打开状态的菜单'])
        get_menu_class = ss.get_attribute('class')
        return get_menu_class

    @allure.step("关闭当天打开状态的菜单")
    def click_close_open_menu(self):
        self.is_click(user['关闭当前打开的菜单'])

    """登录方法"""
    def dcr_login(self, drivers, account, passwd):
        user = DCRLoginPage(drivers)
        user.get_url(ini.url)
        sleep(4)
        user.input_account(account)
        user.input_passwd(passwd)
        sleep(1.5)
        get_check_class = user.get_check_box_class()
        if "is-checked" not in str(get_check_class):
            user.click_check_box()
        user.click_loginsubmit()
        #Base.assert_current_login_user(self, user['首页当前登录用户'])
        DomAssert(self.driver).assert_att('testsupervisor')


    """查找菜单"""
    def click_gotomenu(self, *content):
        """前往左侧菜单栏"""
        self.refresh()
        self.is_click(user['菜单栏'])
        self.refresh()
        level = []
        navstr = ""
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        for i in range(len(content)):
            logging.info(user[level[i]])
            sleep(3.5)
            self.scroll_into_view(user[level[i]])
            sleep(3.5)
            self.is_click(user[level[i]])
        self.element_exist(user['Loading'])


if __name__ == '__main__':
    pass
