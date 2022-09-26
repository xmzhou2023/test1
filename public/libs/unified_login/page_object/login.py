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

    def check_box_en(self):
        """判断是否被选中"""
        return self.select_state(login['隐私保护勾选框_英文'])

    def click_checkbox(self):
        """点击复选框"""
        if not self.check_box():
            self.is_click(login['隐私保护勾选框'])

    def click_checkbox_en(self):
        """点击复选框"""
        if not self.check_box_en():
            self.is_click(login['隐私保护勾选框_英文'])

    def click_loginsubmit(self):
        """点击帐号密码登录"""
        self.is_click(login['登录'])
        sleep(6)

    def input_imgcode(self):
        """识别图形验证码，输入验证码"""
        imgcode = self.get_graphical_code(login['图形验证码'])
        self.input_text(login['图形验证码输入框'], imgcode)


"""DCR登录类"""
class DcrLoginPage(Base):
    def dcr_input_account(self, content):
        """输入工号"""
        self.input_text(login['工号输入框dcr'], txt=content)

    def dcr_input_passwd(self, content):
        """输入密码"""
        self.input_text(login['密码输入框dcr'], txt=content)

    def dcr_switch_lanuage(self, content):
        """语言切换"""
        self.is_click(login['语言切换dcr'])
        self.is_click(login['选择英文dcr'], content)

    def dcr_click_check_box(self):
        """判断是否被选中"""
        self.is_click(login['隐私保护勾选dcr'])

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
        sleep(6)

    def dcr_click_loginOut(self):
        """点击退出登录"""
        sleep(2)
        self.is_click(login['退出登录dcr'])
        sleep(2)



"""SRM登录类"""
class SrmLoginPage(Base):
    """登录类"""
    def input_elsAccount(self,elsAccount):
        self.input_text(login["主账号srm"], txt=elsAccount)

    def input_elsSubAccount(self,elsSubAccount):
        self.input_text(login["子账号srm"], txt=elsSubAccount)

    def input_password(self):
        self.input_text(login["密码srm"], "1qaz@WSX")

    def input_code(self):
        self.is_click(login["验证码框srm"])
        code = self.get_graphical_code(login["验证码srm"])
        # print(code)
        self.input_text(login["验证码框srm"], code)
        # time.sleep(3)

    def click_login(self):
        self.is_click(login["登录srm"])

    def get_current_url(self):
        return self.driver.current_url


"""POP登陆类"""
class PopLoginPage(Base):
    # 输入账号
    def input_pop_account(self,account):
        self.input_text(login['pop账号输入框'],account)
    # 输入密码
    def input_pop_password(self,password):
        self.input_text(login['pop密码输入框'],password)
    # 切换语言--默认切换成中文
    def switch_language(self):
        self.is_click(login['pop切换语言框'])
        self.is_click(login['pop选择中文'])
    # 勾选隐私协议
    def click_privacy_policy(self):
        self.is_click(login['pop隐私协议勾选框'])
    # 点击登录
    def click_loginsubmit(self):
        self.is_click(login['pop登录按钮'])



class OALoginPage(Base):
    def input_passwd(self, content):
        """输入密码"""
        sleep(0.5)
        ele = self.find_element(login['密码输入框'])
        ele.clear()
        ele.send_keys(content)
        sleep(0.5)

if __name__ == '__main__':
    pass
