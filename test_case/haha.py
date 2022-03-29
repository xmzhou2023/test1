# coding=utf-8
from selenium import webdriver
import os

# chrome_driver = os.path.abspath(r"/opt/webDriver/chromedriver")
# os.environ["webdriver.chrome.driver"] = chrome_driver
# chrome_capabilities = {
#     "browserName": "chrome",
#     "version": "",
#     "platform": "ANY",
#     "javascriptEnabled": True,
#     "webdriver.chrome.driver": chrome_driver
# }

from selenium.webdriver.chrome.options import Options
chrome_options = Options()

chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless')

browser = webdriver.Remote("http://10.250.101.58:5555/wd/hub",options=chrome_options)
browser.get("http://www.163.com")
print(browser.title)
browser.get_screenshot_as_file(r"\chrome.png")
browser.quit()