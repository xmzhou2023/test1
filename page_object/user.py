#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging

from page_base.webpage import WebPage, sleep
from common.readelement import Element
from tools.loggerUI import log

user = Element('user')


class UserPage(WebPage):
    """用户类"""

    def search_user(self, jobnumber):
        """工号查询"""
        self.input_text(user['工号输入框'], txt=jobnumber)

        # self.input_text(user['姓名输入框'], txt=name)
        self.is_click(user['查询'])
        sleep()

    # def search_name(self,content):
    #     """姓名查询"""
    #     self.input_text(login['密码输入框'], txt=content)
    #     sleep()

class UserDetailPage(WebPage):
    """用户详情类"""

    def input_passwd(self, content):
        """输入密码"""
        self.input_text(login['密码输入框'], txt=content)
        sleep()

    # def input_account(self, content):
    #     """输入工号"""
    #     self.input_text(login['工号输入框'], txt=content)
    #     sleep()
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
