#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
# from tools.times import sleep
from tools.loggerUI import log
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
import unittest
# from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
"""
    值校验的各种方法
"""

def value_assert_equal(a,b):
    try:
        assert a == b, log.warning("assert equal fail | a:{} b:{}".format(a, b))
        log.info("assert equal success | a:{} b:{}".format(a, b))
    except Exception as e:
        pass

def value_assert_Notequal(a,b):
    try:
        assert a != b, log.warning("assert equal fail | a:{} b:{}".format(a, b))
        log.info("assert equal success | a:{} b:{}".format(a, b))
    except Exception as e:
        pass

def value_assert_True(x):
    try:
        assert bool(x) is True, log.warning("assert True fail | x:{}".format(x))
        log.info("assert True success | x:{}".format(x))
    except Exception as e:
        pass

def value_assert_False(x):
    try:
        assert bool(x) is False, log.warning("assert False fail | x:{}".format(x))
        log.info("assert False success | x:{}".format(x))
    except Exception as e:
        pass

def value_assert_Is(a,b):
    try:
        assert a is b, log.warning("assert Is fail | a:{} b:{}".format(a, b))
        log.info("assert Is success | a:{} b:{}".format(a, b))
    except Exception as e:
        pass

def value_assert_IsNot(a,b):
    try:
        assert a is not b, log.warning("assert IsNot fail | a:{} b:{}".format(a, b))
        log.info("assert IsNot success | a:{} b:{}".format(a, b))
    except Exception as e:
        pass

def value_assert_IsNone(x):
    try:
        assert x is None, log.warning("assert IsNone fail | x:{}".format(x))
        log.info("assert IsNone success | x:{}".format(x))
    except Exception as e:
        pass

def value_assert_IsNoneNot(x):
    try:
        assert x is not None, log.warning("assert IsNoneNot fail | x:{}".format(x))
        log.info("assert IsNoneNot success | x:{}".format(x))
    except Exception as e:
        pass

def value_assert_In(a,b):
    try:
        assert a in b, log.warning("assert In fail | a:{} b:{}".format(a, b))
        log.info("assert In success | a:{} b:{}".format(a, b))
    except Exception as e:
        pass

def value_assert_InNot(a,b):
    try:
        assert a not in b, log.warning("assert InNot fail | a:{} b:{}".format(a, b))
        log.info("assert InNot success | a:{} b:{}".format(a, b))
    except Exception as e:
        pass


def value_assert_Instance(a,b):
    try:
        assert isinstance(a,b), log.warning("assert Instance fail | a:{} {}".format(a, b))
        log.info("assert Instance success | a:{} {}".format(a, b))
    except Exception as e:
        pass

def value_assert_IsInstanceNot(a,b):
    try:
        assert not isinstance(a,b), log.warning("assert IsInstanceNot fail | a:{} {}".format(a, b))
        log.info("assert IsInstanceNot success | a:{} {}".format(a, b))
    except Exception as e:
        pass

"""
    页面元素校验的方法
"""
class DomAssert(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def assert_att(self, word):
        """页面是否存在某文字"""
        try:
            att = self.driver.find_element(By.XPATH,'//*[contains(text(),word)]').text
            assert word in att, log.warning("assert In fail | word:{}".format(word))
            log.info("assert In success | word:{}".format(word))
        except Exception as e:
            return e

"""
    数据库断言
"""
class sqlAssert(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def assert_att(self, word):
        """页面是否存在某文字"""
        try:
            att = self.driver.find_element(By.XPATH,'//*[contains(text(),word)]').text
            assert word in att, log.warning("assert In fail | word:{}".format(word))
            log.info("assert In success | word:{}".format(word))
        except Exception as e:
            return e


if __name__ == "__main__":
   print(value_assert_equal(1,2))
   print(value_assert_Notequal(1,2))
   print(value_assert_True(0))
   print(value_assert_False(1))
   print(value_assert_Is(2, 2))
   print(value_assert_IsNot(2,2))
   print(value_assert_IsNone(None))
   print(value_assert_IsNoneNot(1))
   print(value_assert_In(3, {3,2}))
   print(value_assert_InNot(3, {3,2}))
   print(value_assert_Instance("abc",str))
   print(value_assert_IsInstanceNot(2,int))


