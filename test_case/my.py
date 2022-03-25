from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1920,1080")
chrome_options.add_argument("--no-sandbox")
prefs = {"profile.managed_default_content_settings.images":2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

url = "https://www.baidu.com"
driver.get(url)
print(driver.page_source) ## 打印加载后的源码

