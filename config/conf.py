#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from selenium.webdriver.common.by import By

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件
INI_PATH = os.path.join(BASE_DIR, 'env', 'test', 'config.ini')

# 页面元素目录
ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'log')

# 报告目录
REPORT_PATH = os.path.join(BASE_DIR, 'report', 'report.html')

# 元素定位的类型
LOCATE_MODE = {
    'id': By.ID,
    'name': By.NAME,
    'css': By.CSS_SELECTOR,
    'class': By.CLASS_NAME,
    'text': By.LINK_TEXT,
    'partial-link': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'xpath': By.XPATH,
}

# 邮件信息
EMAIL_INFO = {
    'username': '756978382@qq.com',  # 切换成你自己的地址
    'password': 'QQ邮箱授权码',
    'smtp_host': 'smtp.qq.com',
    'smtp_port': 465
}

# 收件人
ADDRESSEE = [
    'yong.liu7@transsion.com',
]

if __name__ == '__main__':
    print(BASE_DIR)