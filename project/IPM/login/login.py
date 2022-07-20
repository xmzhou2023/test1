
from libs.common.read_config import ini
from project.IPM.page_object.loginpage import LoginPage
from public.base.Basics import Base


class LoginView(Base):
    """登录类"""
    def login(self, drivers,username=18645960):
        """统一登录֤"""
        user = LoginPage(drivers)
        user.get_url(ini.url)
        # user.switch_lanuage('Chinese')
        user.click_accountlogin()
        user.input_account(username)
        user.input_passwd(eval(ini._get('HOST', 'passwd')))
        if not user.check_box():
            user.click_checkbox()
        user.click_loginsubmit()

