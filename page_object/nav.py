#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging

from page_base.webpage import WebPage, sleep
from common.readelement import Element
from tools.loggerUI import log

nav = Element('nav')


class NavPage(WebPage):
    """Nav类"""

    def click_gotonav(self, *content):
        """前往菜单"""
        level = []
        navstr = ""
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        for i in range(len(content)):
            self.is_click(nav[level[i]])
            sleep()

    def input_account(self, content):
        """输入工号"""
        self.input_text(nav['工号输入框'], txt=content)
        sleep()

    #
    # def input_passwd(self, content):
    #     """输入密码"""
    #     self.input_text(login['密码输入框'], txt=content)
    #     sleep()
    #
    # def check_box(self):
    #     """判断是否被选中"""
    #     return self.select_state(login['隐私保护勾选框'])
    #
    # def click_checkbox(self):
    #     """点击复选框"""
    #     self.is_click(login['隐私保护勾选框'])
    #
    # def click_loginsubmit(self):
    #     """点击帐号密码登录"""
    #     self.is_click(login['登录'])

if __name__ == '__main__':
    pass
