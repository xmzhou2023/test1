import time
import json
import requests
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from public.libs.unified_login.login import Login
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class OAdnluPage(Base):
    """登录类"""

    def switch_lanuage(self, content):
        """语言切换"""
        self.is_click(user['语言展开'])
        try:
            if content == "英文":
                self.is_click(user['语言切换'], "2")
            elif content == "法文":
                self.is_click(user['语言切换'], "3")
            else:
                self.is_click(user['语言切换'], "1")
        except:
            self.is_click(user['语言展开'])

    def click_accountuser(self):
        """点击帐号密码登录"""
        self.is_click(user['账号密码登录'])

    def click_accountlogin(self):
        """点击帐号密码登录"""
        self.is_click(user['密码登录'])

    def input_account(self, content):
        """输入工号"""
        self.input_text(user['工号输入框'], txt=content)

    def input_passwd(self, content):
        """输入密码"""
        self.input_text(user['密码输入框'], txt=content)

    def check_box(self):
        """判断是否被选中"""
        return self.select_state(user['隐私保护勾选框'])

    def check_box_en(self):
        """判断是否被选中"""
        return self.select_state(user['隐私保护勾选框_英文'])

    def click_checkbox(self):
        """点击复选框"""
        if not self.check_box():
            self.is_click(user['隐私保护勾选框'])

    def click_checkbox_en(self):
        """点击复选框"""
        if not self.check_box_en():
            self.is_click(user['隐私保护勾选框_英文'])

    def click_usersubmit(self):
        """点击帐号密码登录"""
        self.is_click(user['登录'])

    def input_imgcode(self):
        """识别图形验证码，输入验证码"""
        imgcode = self.get_graphical_code(user['图形验证码'])
        self.input_text(user['图形验证码输入框'], imgcode)

    @allure.step("打开应用系统巡检地址")
    def open_url(self, url):
        self.get_url(url)

    def click_loginsubmit(self):
        """点击帐号密码登录"""
        self.is_click(user['登录'])

    # 禅道登录界面功能--------------------------------------------------
    @allure.step("输入禅道用户名和密码")
    def input_Zenuser(self, name, password):
        self.input_text_oa(user['禅道用户名'], name)
        self.input_text_oa(user['禅道密码'], password)

    @allure.step("判断是否被选中")
    def check_Zen(self):
        return self.select_state(user['禅道保持登录勾选'])

    @allure.step("点击复选框")
    def click_Zencheckbox(self):
        if not self.check_Zen():
            self.is_click(user['禅道保持登录勾选'])

    @allure.step("点击禅道登录按钮")
    def click_Zensubmit(self):
        self.is_click(user['禅道登录按钮'])

    @allure.step("判断禅道是否登录成功，到home页面")
    def isZenlogin(self):
        itexis = self.element_exist(user["禅道登录成功界面"])
        return itexis

    def input_text_oa(self, locator, txt, *choice):
        """输入文本"""
        sleep(0.5)
        ele = self.find_element(locator, *choice)
        ele.clear()
        pwd_list = self.password()
        pwd_str = str(pwd_list[int(txt)]).lstrip("b'").rstrip("'")
        ele.send_keys(pwd_str)

    def password(self):
        aa = base64.decodebytes(bytes("MTg2NDcyMjA=\n", 'utf-8'))
        pa = base64.decodebytes(bytes("dGVkZHlAMjg2Mw==\n", 'utf-8'))
        DA = base64.decodebytes(bytes("VGVkZHlAMjg2Mw==\n", 'utf-8'))
        return aa, pa, DA

    def input_text_log_oa(self, locator, txt, *choice):
        """输入文本"""
        sleep(0.5)
        ele = self.find_element(locator, *choice)
        ele.clear()
        pwd_list = self.password()
        pwd_str = str(pwd_list[int(txt)]).lstrip("b'").rstrip("'")
        ele.send_keys(pwd_str)

    @allure.step("输入账号密码进行登录飞书到应用系统巡检系统")
    def input_account_password_log(self, name, password):
        self.input_text_oa(user['工号输入框'], name)
        self.input_text_oa(user['密码输入框'], password)

    @allure.step("判断档案管理系统是否登录成功到home页面")
    def isfile_login(self):
        itexis = self.element_exist(user["利用首页"])
        return itexis

    @allure.step("判断传音知识产权管理系统是否登录成功到home页面")
    def ispatent_login(self):
        itexis = self.element_exist(user["我的专利提案"])
        return itexis
