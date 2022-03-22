#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from config.conf import LOCATE_MODE
from tools.times import sleep
from tools.loggerUI import log
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

"""
selenium基类
本文件存放了selenium基类的封装方法
"""
class WebPage(object):
    """selenium基类"""

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)

    def find_elements(self, locator):
        """查找多个相同的元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        log.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def readonly_input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_element(locator)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", ele)
        ele.clear()
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def is_click(self, locator, choice=None):
        """点击"""
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            log.info(Npath)
            self.find_element(Npath).click()
            log.info("下拉选择：{}".format(Npath))
        else:
            self.find_element(locator).click()
            # sleep()
            log.info("点击元素：{}".format(locator))

    def edituser_tab_click(self, locator, choice=None, pane=None):
        """编辑用户权限-竖tab切换"""
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            if pane is not None:
                original = "@id='pane-1'"
                pane_str = original.replace('1', str(pane))
                Npath[1] = Npath[1].replace("@id='pane-1'", pane_str)
            self.find_element(Npath).click()
            log.info("设置权限：{}".format(Npath))
        else:
            self.find_element(locator).click()
            # sleep()
            log.info("点击元素：{}".format(locator))

    def click_blank(self, ):
        """点击空白区域，用于取消释法"""
        sleep(10)

    def move_house(self, content):
        """点击空白区域，用于取消释法"""
        ActionChains(content).move_by_offset(700, 700).click().perform()
        sleep(10)

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        log.info("获取文本：{}".format(_text))
        return _text

    def select_state(self, locator):
        """是否被选中"""
        _select = self.find_element(locator).is_selected()
        log.info("获取状态：{}".format(_select))
        return _select

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)

class customPage(object):
    """selenium新增基类"""
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 20
        self.driver = webdriver.

    def custom_find_elements(self, locator):
        """树结构专用查找多个相同的元素"""
        # return self.f
        pass


if __name__ == "__main__":
    pass
