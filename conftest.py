#!/usr/bin/env python3
# -*- coding:utf-8 -*-
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
def drivers(request):
    global driver
    if driver is None:
        option = webdriver.ChromeOptions()
        # 防止打印一些无用的日志
        option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        driver = webdriver.Chrome(options=option)
        # driver = webdriver.Chrome()
        driver.maximize_window()
        # inspect_element() # page_element YMAL文件自检

    def fn():
        sleep(10)
        driver.quit()

    request.addfinalizer(fn)
    return driver

@pytest.fixture(scope='session', autouse=True)
def login(drivers):
    """统一认证"""
    user = LoginPage(drivers)
    user.get_url(ini.url)
    user.click_accountlogin()
    user.input_account(eval(ini.usernum))
    user.input_passwd('jf3249JFL')
    if not user.check_box():
        user.click_checkbox()
    user.click_loginsubmit()
    # user.click_loginsubmit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="" alt="screenshot" style="width:1024px;height:768px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


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
