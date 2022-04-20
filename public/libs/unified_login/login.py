from public.public_base.Basics import Base
from libs.common.read_config import ini
from public.public_libs.unified_login.page_object.login import LoginPage
from public.public_data.unified_login.unified import *

class Login(Base):
    """登录类"""
    def login(self, drivers):
        """统一登录֤"""
        user = LoginPage(drivers)
        user.get_url(ini.url)
        user.click_accountlogin()
        user.input_account(account[0]['usernum'])
        user.input_passwd(account[0]['passwd'])
        if not user.check_box():
            user.click_checkbox()
        user.click_loginsubmit()

