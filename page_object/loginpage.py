#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page_base.webpage import WebPage, sleep
from common.readelement import Element

login = Element('login')


class LoginPage(WebPage):
    """登录类"""

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
        self.is_click(login['隐私保护勾选框'])

    def click_loginsubmit(self):
        """点击帐号密码登录"""
        self.is_click(login['登录'])

if __name__ == '__main__':
    pass
