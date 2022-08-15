# -*- coding: utf-8 -*-
# @Time    : 2022-07-26 11:15
# @Author  : wuqi
# @Email   : qi.wu@transsion.com
# @File    : Center_Component.py
# @Software: PyCharm
import os
import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class PageInfo(Base):

    @allure.step("获取查询结果条数")
    def get_count(self):
        """"""
        # return self.element_text(user["查询结果条数"])
        return int("".join(list(filter(str.isdigit, self.element_text(user["查询结果条数"])))))

    @allure.step("获取提示消息")
    def get_tips(self):
        return self.element_text(user["提示消息"])


class NavPage(Base):
    def click_gotonav(self, *content):
        for i in range(len(content)):
            self.is_click(user["菜单"], content[i])
        self.is_click(user["菜单"], content[0])


class MESDAPLogin(Base):
    """MES_DAP登录类"""

    def mes_input_username(self, content):
        """输入账号"""
        self.input_text(user["mesDAP账号输入框"], content)

    def mes_input_password(self, content):
        """输入密码"""
        self.input_text(user["mesDAP密码输入框"], content)

    def mes_click_login(self):
        """点击登录按钮"""
        self.is_click(user["mesDAP登录按钮"])

    def mes_switch_language(self, content):
        """切换语言"""
        self.is_click(user["mesDAP语言下拉按钮"])
        self.is_click(user["mesDAP语言下拉选项"], content)


class Login(Base):
    """登录类"""

    def mes_dap_login(self, drivers, url, username, passwd):
        user = MESDAPLogin(drivers)
        user.get_url(url)
        user.mes_switch_language("ZH")
        user.mes_input_username(username)
        user.mes_input_password(passwd)
        user.mes_click_login()
        sleep(2)
