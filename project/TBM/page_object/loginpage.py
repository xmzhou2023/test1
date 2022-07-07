#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from libs.common.read_element import Element
from libs.common.time_ui import sleep
from project.TBM.page_base.webpage import WebPage
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class LoginPage(WebPage):
    """登录类"""
    def switch_lanuage(self, content):
        """语言切换"""
        self.is_click_tbm(user['语言按钮'])
        self.is_click_tbm(user['语言切换'], content)

    def click_accountlogin(self):
        """点击帐号密码登录"""
        self.is_click_tbm(user['账号密码登录'])

    def input_account(self, content):
        """输入工号"""
        self.input_text(user['工号输入框'], txt=content)
        sleep()

    def input_passwd(self, content):
        """输入密码"""
        self.input_text(user['密码输入框'], txt=content)
        sleep()

    def check_box(self):
        """判断是否被选中"""
        return self.select_state(user['隐私保护勾选框'])

    def click_checkbox(self):
        """点击复选框"""
        self.is_click_tbm(user['隐私保护勾选框'])

    def click_loginsubmit(self):
        """点击帐号密码登录"""
        self.is_click_tbm(user['登录'])

if __name__ == '__main__':
    pass
