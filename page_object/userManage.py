#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:huangqin
# @time:2022/3/16 14:36
from page_base.webpage import WebPage, sleep
from common.readelement import Element

login = Element('login')


class UserMngPage(WebPage):
    """用户管理类"""

    def click_query(self):
        """点击查询按钮"""
        self.is_click(login['查询'])

    def click_reset(self):
        """点击重置按钮"""
        self.is_click(login['重置'])

    def click_append(self):
        """点击新增按钮"""
        self.is_click(login['新增'])

    def input_account(self, content):
        """输入工号"""
        self.input_text(login['工号'], txt=content)
        sleep()

    def input_name(self, content):
        """输入姓名"""
        self.input_text(login['姓名'], txt=content)
        sleep()