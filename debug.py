# cd C:\Program Files\Google\Chrome\Application
# chrome.exe --remote-debugging-port=9527 --user-data-dir="D:\selenium\AutomationProfile"
# http://10.250.112.166:9000/#/systemManage/userManage


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = webdriver.Chrome(options=options)
# driver.get("http://10.250.112.166:9000/#/systemManage/userManage")
driver.find_element(By.XPATH, "//div[@class='el-tabs__nav is-left']//div[contains(text(),'区域')]").click()
# driver.find_element(By.XPATH,"xpath==//div[@id='pane-1']//span[@class='el-checkbox__label'][contains(text(),'Infinix事业部')]").click()
# driver.find_element(By.XPATH, "//div[@id='pane-1']//span[@class='el-checkbox__label'][contains(text(),'TECNO')]").click()
# driver.find_element(By.XPATH, "//div[@id='pane-3']//div[@id='pane-Infinix']//span[@class='el-tree-node__label'][contains(text(),'全部区域')]").click()
# driver.find_element(By.XPATH, "//div[@id='pane-3']//div[@id='pane-Infinix']//span[@class='el-tree-node__label'][contains(text(),'全部区域')]").click()
# list = driver.find_elements(By.XPATH, "//div[@id='pane-3']//div[@id='pane-itel']//span[@class='el-tree-node__expand-icon el-icon-caret-right']")


# left_list=driver.find_elements(By.XPATH, path)
# print(len(left_list))
# for i in range(len(left_list)):
#     driver.find_element(By.XPATH, path).click()
#     sleep(1)

while 1:
    # path = "//div[@id='pane-3']//div[@id='pane-TECNO']//span[@class='el-tree-node__expand-icon el-icon-caret-right']"
    path = "//div[@id='pane-3']//div[@id='pane-itel']//span[@class='el-tree-node__expand-icon el-icon-caret-right']"
    left_list = len(driver.find_elements(By.XPATH, path))
    print(left_list)
    if left_list != 0:
        driver.find_element(By.XPATH, path).click()
        sleep(1)
    else:
        break

# driver.find_element(By.XPATH, "//div[@id='pane-3']//div[@id='pane-TECNO']//span[@class='el-tree-node__label'][contains(text(),'尼日利亚')]").click()
# driver.find_element(By.XPATH, "//div[@role='group']//div[@role='group']//div[@role='group']//span[@class='el-tree-node__label'][contains(text(),'纳米比亚')]/preceding-sibling::label").click()
# driver.find_element(By.XPATH, "//div[@role='group']//div[@role='group']//div[@role='group']//span[@class='el-tree-node__label'][contains(text(),'事业部备料')]/preceding-sibling::label").click()
#

if __name__ == '__main__':
    pass
