from public.base.basics import Base
# from libs.common.read_config import ini
from public.libs.unified_login.page_object.login import LoginPage
from time import sleep

class Login(Base):
    """登录类"""
    def login(self, drivers, url, username, passwd):
        """统一登录֤"""
        user = LoginPage(drivers)
        user.get_url(url) # 跳转到指定网页
        user.switch_lanuage("中文") # 传参为"中文"，"英文"，"法文"
        user.click_accountlogin() # 点击帐户密码登录
        user.input_account(username) # 输入帐户名
        user.input_passwd(passwd) # 输入密码
        user.click_checkbox()
        user.click_loginsubmit()
