#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:huangqin
# @time:2022/3/10 11:15

from selenium.webdriver.common.by import By




homepageBy8 = (By.ID, "TANGRAM__PSP_11__submit")

homepageBy7 = (By.XPATH, '//*[@id="s-top-username"]/span[2]')

homepageBy6 = (By.LINK_TEXT,  "link text")

homepageBy5 = (By.PARTIAL_LINK_TEXT, "partial link text")

homepageBy4 = (By.NAME, "name")

homepageBy3 = (By.TAG_NAME, "tag name")

homepageBy2 = (By.CLASS_NAME, "class name")

homepageBy1 = (By.CSS_SELECTOR, '#kw')