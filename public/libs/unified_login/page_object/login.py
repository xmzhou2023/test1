from public.base.basics import Base, sleep
from libs.common.read_public_element import Element

login = Element('login')

class LoginPage(Base):
    """登录类"""
    def switch_lanuage(self, content):
        """语言切换"""
        self.is_click(login['语言展开'])
        sleep(2)
        try:
            if content == "英文":
                self.is_click(login['语言切换'], "2")
            elif content == "法文":
                self.is_click(login['语言切换'], "3")
            else:
                self.is_click(login['语言切换'], "1")
        except:
            self.is_click(login['语言展开'])

    def click_accountlogin(self):
        """点击帐号密码登录"""
        self.is_click(login['账号密码登录'])

    def input_account(self, content):
        """输入工号"""
        self.input_text(login['工号输入框'], txt=content)
        sleep()

    def input_passwd(self, content):
        """输入密码"""
        self.input_text(login['密码输入框'], txt=content)
        sleep()

    def check_box(self):
        """判断是否被选中"""
        return self.select_state(login['隐私保护勾选框'])

    def click_checkbox(self):
        """点击复选框"""
        if not self.check_box():
            self.is_click(login['隐私保护勾选框'])

    def click_loginsubmit(self):
        """点击帐号密码登录"""
        self.is_click(login['登录'])
        sleep(4)


"""DCR登录类"""
class DcrLoginPage(Base):
    def dcr_input_account(self, content):
        """输入工号"""
        self.input_text(login['工号输入框dcr'], txt=content)
        sleep(1)

    def dcr_input_passwd(self, content):
        """输入密码"""
        self.input_text(login['密码输入框dcr'], txt=content)
        sleep(1)

    def dcr_switch_lanuage(self, content):
        """语言切换"""
        self.is_click(login['语言切换dcr'])
        self.is_click(login['选择英文dcr'], content)

    def dcr_click_check_box(self):
        """判断是否被选中"""
        self.is_click(login['隐私保护勾选dcr'])
        sleep(1)

    def dcr_get_check_box_class(self):
        """获取复选框对应的 Class属性是否包含is-checked"""
        ss = self.find_element(login['隐私保护勾选dcr'])
        get_check_state = ss.get_attribute('class')
        return get_check_state

    def dcr_check_box(self):
        """判断是否被选中"""
        checkbox = self.select_state(login['隐私保护勾选dcr'])
        return checkbox

    def dcr_click_loginsubmit(self):
        """点击帐号密码登录"""
        self.is_click(login['登录dcr'])

    def dcr_click_loginOut(self):
        """点击退出登录"""
        sleep(2)
        self.is_click(login['退出登录dcr'])
        sleep(2)



if __name__ == '__main__':
    pass
