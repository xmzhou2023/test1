#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

import pytest
from py._xmlgen import html
from selenium import webdriver
from common.inspect import inspect_element
from time import sleep

from tools.loggerUI import log
from common.readconfig import ini
from page_object.loginpage import LoginPage

driver = None

@pytest.fixture(scope='session', autouse=True)
def drivers(request, no_ui=False):
    global driver
    if driver is None:
        if 'linux' in sys.platform:
            option = webdriver.ChromeOptions()
            option.add_argument('no-sandbox')  # 以最高权限运行
            option.add_argument('--start-maximized')  # 最大化运行（全屏窗口）设置元素定位比较准确
            option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            # # option.add_argument('--window-size=1920,1080')  # 设置浏览器分辨率（窗口大小）
            driver = webdriver.Remote("http://10.250.101.58:5555/wd/hub", options=option)
            # driver = webdriver.Chrome(options=option)
            # # inspect_element() # page_element YMAL文件自检
        else:
            if no_ui:
                '''win系统下界面模式'''
                option = webdriver.ChromeOptions()
                option.add_argument('headless')  # 浏览器不提供可视化页面
                option.add_argument('--start-maximized')  # 最大化运行（全屏窗口）设置元素定位比较准确
                driver = webdriver.Chrome(chrome_options=option)
                # inspect_element() # page_element YMAL文件自检
            else:
                option = webdriver.ChromeOptions()
                # 防止打印一些无用的日志
                option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
                driver = webdriver.Chrome(options=option)
                driver.maximize_window()
                # inspect_element() # page_element YMAL文件自检
    def fn():
        sleep(10)
        driver.quit()

    # 终结函数
    request.addfinalizer(fn)
    return driver

@pytest.fixture(scope='session', autouse=True)
def login(drivers):
    """统一认证"""
    user = LoginPage(drivers)
    user.get_url(ini.url)
    user.click_accountlogin()
    user.input_account(eval(ini.usernum))
    user.input_passwd(eval(ini.passwd))
    if not user.check_box():
        user.click_checkbox()
    user.click_loginsubmit()

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             screen_img = _capture_screenshot()
#             if file_name:
#                 html = '<div><img src="" alt="screenshot" style="width:1024px;height:768px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#         report.description = str(item.function.__doc__)
#         report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例名称'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)


@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))


def _capture_screenshot():
    '''
    截图保存为base64
    :return:
    '''
    return driver.get_screenshot_as_base64()
