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
            self.readonly_input_text(user['用户管理-工号输入框'], txt=jobnum)
            sleep(2)
            self.is_click(user['用户管理-工号下拉列表'], jobnum)
        if name is not None:
            self.readonly_input_text(user['用户管理-姓名输入框'], txt=name)
            sleep(2)
            self.is_click(user['用户管理-姓名下拉列表'], name)
        self.is_click(user['用户管理-查询'])
        sleep()

    def input_account(self, content):
        """输入工号"""
        self.readonly_input_text(user['用户管理-工号输入框'], txt=content)
        sleep(20)

    def input_name(self, content):
        """输入姓名"""
        self.readonly_input_text(user['用户管理-姓名输入框'], txt=content)
        sleep(20)

    def search_account(self):
        """查询工号"""
        self.is_click(user['用户管理-查询'])
        sleep()

    def reset_account(self):
        """重置工号"""
        self.is_click(user['用户管理-重置'])
        sleep()

    def append_account(self,content):
        """新增工号"""
        self.is_click(user['用户管理-新增'])
        sleep()
        self.input_text(user['人员列表-新增人员搜索框'], txt=content)
        self.is_click(user['人员列表-新增选择人员'], content)
        self.is_click(user['人员列表-新增'])

    """用户详情类"""

    def edit_Permission(self, jobnum=None, dimension=None):
        """给指定用户配置权限"""
        self.search_user(jobnum=jobnum)
        if dimension is not None:
            self.is_click(user['用户管理-列表人员'])
            for (key, value) in dimension.items():
                self.is_click(user['编辑用户权限-维度'], key)
                for i in value:
                    # self.is_click(user['编辑用户权限-权限'], key)
        # self.permission_choice_click(user['编辑用户权限-维度'], dimension)


if __name__ == '__main__':
    pass
