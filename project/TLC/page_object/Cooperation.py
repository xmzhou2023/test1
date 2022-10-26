import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from public.base.assert_ui import DomAssert, ValueAssert
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class Cooperater(Base):

    @allure.step('导航菜单')
    def click_menu(self, fType, sType):
        self.mouse_hover(user['一级菜单'], fType)
        self.is_click(user['二级菜单'], sType)
        sleep(1)
        self.refresh()

    @allure.step('处理输入')
    def input(self, yaml, txt, choice=None):
        self.input_text(user[yaml], txt, choice)

    def readonly_input(self, ymal, txt, choice = None):
        self.readonly_input_text(user[ymal], txt, choice)
        sleep(3)

    @allure.step('处理点击')
    def click(self, yaml, choice = None):
        sleep(1)
        self.is_click_dcr(user[yaml], choice)
        sleep(2)

    @allure.step('hover')
    def hover(self, yaml, choice = None):
        self.mouse_hover(user[yaml], choice)

    @allure.step('退出登录')
    def logout(self):
        """点击退出登录"""
        self.is_click_dcr(user['用户管理'])
        sleep(1)
        self.is_click_dcr(user['用户退出'])
        sleep(2)

    def click_accountlogin(self):
        """点击帐号密码登录"""
        self.is_click(user['账号密码登录'])

    def input_account(self, content):
        """输入工号"""
        self.input_text(user['工号输入框'], txt=content)
        sleep()

    def input_passwd(self, content):
        """输入密码"""
        self.input_text(user['密码输入框'], txt=content)
        sleep()

    def check_box(self):
        """判断是否被选中"""
        return self.select_state(user['隐私保护勾选框'])

    def click_checkbox(self):
        """点击复选框"""
        if not self.check_box():
            self.is_click(user['隐私保护勾选框'])

    def click_loginsubmit(self):
        """点击帐号密码登录"""
        self.is_click(user['登录'])
        sleep(6)

    def relogin(self, username):
        """统一登录֤"""
        self.logout() # 退出登录
        self.click_accountlogin() # 点击帐户密码登录
        self.input_account(username) # 输入帐户名
        self.input_passwd('xLily6x') # 输入密码
        self.click_loginsubmit()

    @allure.step("元素是否存在")
    def element_exist_TLC(self, yaml, choice = None):
        """校验元素是否存在"""
        result = True
        try:
            self.find_elements_tbm(user[yaml], choice)
            logging.info('存在元素：{}'.format(yaml))
            return result
        except:
            logging.error('{}元素不存在'.format(yaml))
            result = False
            return result


    @allure.step("断言元素是否存在")
    def value_assert(self, element, choice = None, result=True):
        control = self.element_exist_TLC(element, choice)
        try:
            assert control is result, logging.warning('断言失败，元素：{}存在结果与期望结果：{}不符'.format(element, result))
            logging.info('断言成功，元素：{}存在结果为：{}'.format(element, result))
        except Exception as e:
            logging.error(e)
            raise


if __name__ == '__main__':
    pass