#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:huangqin
# @time:2022/3/10 18:13
'''
loginpage类；专门用于实现用户管理页面对象的文件
主体内容包含：
1.核心的页面元素：工号，姓名，查询按钮，重置按钮，新增，配置按钮，编辑按钮
2.核心的业务流：
用户的查询行为，重置行为，配置行为，编辑行为
'''

from UIPOMTest.pages.basePages import TestBasePages
from selenium.webdriver.common.by import By
# from time import sleep
class TestLoginPage(TestBasePages):
    # 核心元素
    url = 'http://10.248.39.163:10101/#/c-login?lang=zh&source=SCM_DRP&type=simple&redirect=http%3A%2F%2F10.250.112.166%3A9000%2F%23%2F'
    user = (By.XPATH, '//*[@id="pane-account"]/form/div[1]/div/div/input')  # 元组是为了便于管理
    passwd = (By.XPATH, '//*[@id="pane-account"]/form/div[2]/div/div[1]/input')
    login_button = (By.XPATH, '//*[@id="pane-account"]/form/button')

    # 核心业务流
    def login(self, username, pwd):
        self.visit()
        self.input_text(self.user, username)
        self.input_text(self.passwd, pwd)
        self.click_element(self.login_button)

        # 添加一个返回值，用于文本返回信息
