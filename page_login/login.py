from page_base.webpage import WebPage
from tools.loggerUI import log
from common.readconfig import ini
from selenium.webdriver.support.ui import WebDriverWait
from page_object.loginpage import LoginPage


class LoginView(WebPage):
    """登录类"""
    def login(self, drivers):
        """统一登录֤"""
        user = LoginPage(drivers)
        user.get_url(ini.url)
        # user.switch_lanuage('Chinese')
        user.click_accountlogin()
        user.input_account(eval(ini.usernum))
        user.input_passwd(eval(ini.passwd))
        if not user.check_box():
            user.click_checkbox()
        user.click_loginsubmit()