#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:huangqin
# @time:2022/3/10 15:08

'''
loginpage类；专门用于实现登录页面对象的文件
主体内容包含：
1.核心的页面元素：账号，密码，登录按钮
2.核心的业务流：
用户的登录行为
'''

from pages.basePages import TestBasePages
from selenium.webdriver.common.by import By
import pytest

# from time import sleep
class TestLoginPage(TestBasePages):
    def haha(self):
        print("haha")
    # # 核心元素
    # url = 'http://10.248.39.163:10101/#/c-login?lang=zh&source=SCM_DRP&type=simple&redirect=http%3A%2F%2F10.250.112.166%3A9000%2F%23%2F'
    # user = (By.XPATH, '//*[@id="pane-account"]/form/div[1]/div/div/input')  # 元组是为了便于管理
    # passwd = (By.XPATH, '//*[@id="pane-account"]/form/div[2]/div/div[1]/input')
    # login_button = (By.XPATH, '//*[@id="pane-account"]/form/button')

   # # 核心业务流
   #  def login(self, url, username, pwd):
   #      self.initial_driver()
    #     self.visit(url)
    #     self.input_text(self.user, username)
    #     self.input_text(self.passwd, pwd)
    #     self.click_element(self.login_button)


if __name__ == '__main__':
    pytest.main(['-vs', './base_object/login_page.py'])
