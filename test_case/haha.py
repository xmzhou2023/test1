# coding=utf-8
from selenium import webdriver
import os

chrome_driver = os.path.abspath(r"/opt/webDriver/chromedriver")
os.environ["webdriver.chrome.driver"] = chrome_driver
chrome_capabilities = {
    "browserName": "chrome",
    "version": "",
    "platform": "ANY",
    "javascriptEnabled": True,
    "webdriver.chrome.driver": chrome_driver
}
browser = webdriver.Remote("http://10.250.101.58:5555/wd/hub",options=webdriver.ChromeOptions())
browser.get("http://www.163.com")
print(browser.title)
browser.get_screenshot_as_file(r"\chrome.png")
browser.quit()