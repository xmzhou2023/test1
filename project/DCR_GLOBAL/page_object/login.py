from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.read_config import *
from libs.common.time_ui import sleep
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)
ini = ReadConfig(pro_name, pro_env)

class LoginPage(Base):
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
        sleep(1)


    def get_check_box_class(self):
        """获取复选框对应的 Class属性是否包含is-checked"""
        ss = self.find_element(user['隐私保护勾选'])
        get_check_state = ss.get_attribute('class')
        return get_check_state

    # def check_box(self):
    #     """判断是否被选中"""
    #     checkbox = self.select_state(user['隐私保护勾选'])
    #     return checkbox

    def click_loginsubmit(self):
        """点击帐号密码登录"""
        self.is_click(user['登录'])

    def click_loginOut(self):
        """点击退出登录"""
        sleep(2)
        self.is_click(user['退出登录'])
        sleep(2)

    def dcr_login(self, drivers, account, passwd):
        """"登录用例"""
        user = LoginPage(drivers)
        user.get_url(ini.url)
        sleep(3)
        user.input_account(account)
        user.input_passwd(passwd)
        sleep(2)
        get_check_class = user.get_check_box_class()
        if "is-checked" not in str(get_check_class):
            user.click_check_box()
        user.click_loginsubmit()


if __name__ == '__main__':
    pass
