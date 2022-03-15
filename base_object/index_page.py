#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:huangqin
# @time:2022/3/10 15:30
'''
index_page类；专门用于实现首页中国页面对象的文件
主体内容包含：
1.核心的页面元素：账号，密码，登录按钮
2.核心的业务流：
用户的登录行为
'''

from pages.basePages import TestBasePages
from selenium.webdriver.common.by import By
# from time import sleep
class TestIndexPage(TestBasePages):
    # 核心元素
    url = ''
    search_input = (By.NAME, 'pwd')
    search_button = (By.XPATH, '/HTML/......')

    # 核心业务流
    def search(self, txt):
        self.initial_driver()
        self.visit()
        self.input_text(self.search_input, txt)
        self.click_element(self.search_button)