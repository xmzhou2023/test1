import conftest
from project.IPM.page_base.assert_pubic import *

class CenterComponent(PubicMethod):
    def __init__(self,driver,element_yaml='Center_Component',expect=None):
        super().__init__(driver, element_yaml,expect=expect)
    def current_url_ipm(self):
        """获取当前页面地址"""
        url = self.driver.current_url
        return url

    def ipm_input_account_KT5(self, content):
        """登录-输入工号"""
        self.input_text_IPM('工号输入框IPM_KT', text=content)

    def ipm_input_passwd_KT5(self, content):
        """登录-输入密码"""
        self.input_text_IPM('密码输入框IPM_KT', text=content)

    def ipm_click_login_KT5(self):
        """登录-点击登录"""
        sleep(2)
        self.click_IPM('登录IPM_KT')
        sleep(2)


