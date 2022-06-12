from public.base.Basics import Base
from libs.common.read_config import ini
from public.libs.unified_login.page_object.login import LoginPage
from time import sleep

class Login(Base):
    """登录类"""
    def login(self, drivers, username, passwd):
        """统一登录֤"""
        user = LoginPage(drivers)
        user.get_url(ini.url)
        user.switch_lanuage("Chinese")
        user.click_accountlogin()
        user.input_account(username)
        user.input_passwd(passwd)
        if not user.check_box():
            user.click_checkbox()
        user.click_loginsubmit()
        sleep(10)

