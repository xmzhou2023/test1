# chrome.exe --remote-debugging-port=9527 --user-data-dir="D:\selenium\AutomationProfile"


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:9527")
driver = webdriver.Chrome(options=options)
# driver.get("http://10.250.112.166:9000/#/systemManage/userManage")
# driver.find_element(By.XPATH,"//div[@class='el-tabs__nav is-left']//div[contains(text(),'品牌')]").click()
# driver.find_element(By.XPATH,"xpath==//div[@id='pane-1']//span[@class='el-checkbox__label'][contains(text(),'Infinix事业部')]").click()
driver.find_element(By.XPATH, "xpath==//div[@class='rowCheckBox']//span[@class='el-checkbox__label'][contains(text(),'Infinix事业部')").click()

if __name__ == '__main__':
    pass