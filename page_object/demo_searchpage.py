#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page_base.webpage import WebPage, sleep
from common.readelement import Element

search = Element('demo_search')


class SearchPage(WebPage):
    """搜索类"""

    def input_search(self, content):
        """输入搜索"""
        self.input_text(search['搜索框'], txt=content)
        sleep()

    @property
    def imagine(self):
        """搜索联想"""
        return [x.text for x in self.find_elements(search['候选'])]

    def click_search(self):
        """点击搜索"""
        self.is_click(search['搜索按钮'])

    def click_accountlogin(self):
        """点击帐号密码登录"""
        self.is_click()

if __name__ == '__main__':
    pass