#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging

from page_base.webpage import WebPage, sleep
from common.readelement import Element
from tools.loggerUI import log

user = Element('user')


class UserPage(WebPage):
    """用户类"""

    def search_user(self, jobnum=None,name=None):
        """工号，姓名查询"""
        if jobnum is not None:
            self.readonly_input_text(user['工号输入框'], txt=jobnum)
            sleep(2)
            self.jobnum_choice_click(user['工号下拉列表'], jobnum)
        if name is not None:
            self.readonly_input_text(user['姓名输入框'], txt=name)
            sleep(2)
            self.name_choice_click(user['姓名下拉列表'], name)
        self.is_click(user['查询'])
        sleep()

    def input_account(self, content):
        """输入工号"""
        log.info(user['工号输入框'])
        self.readonly_input_text(user['工号输入框'], txt=content)
        sleep(20)

    def input_name(self, content):
        """输入工号"""
        log.info(user['姓名输入框'])
        self.readonly_input_text(user['姓名输入框'], txt=content)
        sleep(20)

    def search_account(self):
        """查询工号"""
        log.info(user['查询'])
        self.is_click(user['查询'])
        sleep()

    def reset_account(self):
        """重置工号"""
        self.is_click(user['重置'])
        sleep()

    def append_account(self,):
        """新增工号"""
        self.is_click(user['新增'])
        sleep()

class UserDetailPage(WebPage):
    """用户详情类"""

    def input_passwd(self, content):
        """输入密码"""
        self.input_text(login['密码输入框'], txt=content)
        sleep()

if __name__ == '__main__':
    pass
