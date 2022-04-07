# cd C:\Program Files\Google\Chrome\Application
# chrome.exe --remote-debugging-port=9527 --user-data-dir="D:\selenium\AutomationProfile"
# http://10.250.112.166:9000/#/systemManage/userManage

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
# from page_base.webpage import WebPage
from common.unit_assert import DomAssert

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = webdriver.Chrome(options=options)
driver.get("http://www.google.com")
print(driver.title)
# print(driver.find_element(By.ID, "kw").send_keys("guxiaofei"))
# driver.find_element(By.NAME, "wd").send_keys("guxiaofei")
driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("guxiaofei")
# print(driver.find_element(By.CLASS_NAME, 's_ipt').send_keys("11111"))
print(driver.find_element(By.XPATH, '//*[@id="su"]').text)
# print(driver.find_element(By.PARTIAL_LINK_TEXT, "扫码登录").text)
# print(driver.find_element(By.LINK_TEXT, " 移动端扫码登录").text)
# print(driver.find_elements(By.XPATH, "//div[contains(text(),'扫码')]")[0].text)

# option = webdriver.ChromeOptions()
# # option.add_argument('--headless')  # 浏览器不提供可视化页面
# option.add_argument('--no-sandbox')  # 以最高权限运行
# option.add_argument('--lang=zh-CN')  # 以最高权限运行
# option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
# option.add_argument('--start-maximized')  # 最大化运行（全屏窗口）设置元素定位比较准确
# option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
# # option.add_argument('--window-size=1366,768')  # 设置浏览器分辨率（窗口大小）
# driver = webdriver.Remote("http://10.250.101.58:5555/wd/hub", options=option)
# driver.get("http://www.baidu.com")
# driver.get("http://www.qq.com")

# driver = WebPage(driver)
# //*[@id="app"]/div/div/section/div/header/div/div[2]/div/text()
# driver.get("http://10.250.112.166:9000/#/systemManage/userManage")
# print(driver.find_element(By.ID, "tab-account").click())
# print(driver.find_element(By.XPATH, "//li[contains(text(),'variable')]").click())
# driver.find_element(By.XPATH,"xpath==//div[@id='pane-1']//span[@class='el-checkbox__label'][contains(text(),'Infinix事业部')]").click()
# driver.find_element(By.XPATH, "//div[@id='pane-1']//span[@class='el-checkbox__label'][contains(text(),'TECNO')]").click()
# driver.find_element(By.XPATH, "//div[@id='pane-3']//div[@id='pane-Infinix']//span[@class='el-tree-node__label'][contains(text(),'全部区域')]").click()
# driver.find_element(By.XPATH, "//div[@id='pane-3']//div[@id='pane-Infinix']//span[@class='el-tree-node__label'][contains(text(),'全部区域')]").click()
# list = driver.find_elements(By.XPATH, "//div[@id='pane-3']//div[@id='pane-itel']//span[@class='el-tree-node__expand-icon el-icon-caret-right']")
# a = driver.find_elements(By.XPATH, "//div[@id='pane-2']//label[@class='el-checkbox is-checked']//span[@class='el-checkbox__inner']")
#
# for i in range(len(a)):
#     if a == []:
#         print(a)
#     else:
#         driver.find_element(By.XPATH, "//div[@id='pane-2']//label[@class='el-checkbox is-checked']//span[@class='el-checkbox__inner']").click()
# if a == []:
#     driver.find_element(By.XPATH,"//div[@id='pane-2']//label[@class='el-checkbox is-checked']//span")
#     a = driver.find_elements(By.XPATH, "//div[@id='pane-2']//label[@class='el-checkbox is-checked']//span")

# left_list=driver.find_elements(By.XPATH, path)
# print(len(left_list))
# for i in range(len(left_list)):
#     driver.find_element(By.XPATH, path).click()
#     sleep(1)

# while 1:
#     path = "//div[@id='pane-3']//div[@id='pane-Infinix']//span[@class='el-tree-node__expand-icon el-icon-caret-right']"
#     left_list = len(driver.find_elements(By.XPATH, path))
#     print(left_list)
#     if left_list != 0:
#         ele = driver.find_element(By.XPATH, path)
#         driver.execute_script("arguments[0].scrollIntoView()", ele)
#         driver.find_element(By.XPATH, path).click()
#         sleep(1)
#     else:
#         break

# driver.find_element(By.XPATH, "//div[@id='pane-3']//div[@id='pane-TECNO']//span[@class='el-tree-node__label'][contains(text(),'尼日利亚')]").click()
# driver.find_element(By.XPATH, "//div[@role='group']//div[@role='group']//div[@role='group']//span[@class='el-tree-node__label'][contains(text(),'纳米比亚')]/preceding-sibling::label").click()
# driver.find_element(By.XPATH, "//div[@role='group']//div[@role='group']//div[@role='group']//span[@class='el-tree-node__label'][contains(text(),'事业部备料')]/preceding-sibling::label").click()
#
# dict = { 'chinese', 'english',  'french'}
# dict = { 0:['中文版','英文版', '法文版'],1:['chinese','english', 'french'],2:['chinois', 'anglais', 'français']}
# a = '中文版'
# b = 'englist'
# for i,k in dict.items():
#      dict[i].index(a))
#

if __name__ == '__main__':
    pass
