Selenium使用手册

导航
# 打开网站
driver.get("https://transsion.com")

# 后退
driver.back()

# 前进
driver.forward()

# 刷新
driver.refresh()

# 获取标题
driver.title

# 获取URL地址
driver.current_url

Alerts 警告框
# 等待警报显示，并将其存储在变量中
alert = wait.until(expected_conditions.alert_is_present())

# 将警报文本存储在变量中
text = alert.text

# 点击确定按钮
alert.accept()

# 点击取消按钮
alert.dimiss()

Confirm 确认框
# 等待警报显示
wait.until(expected_conditions.alert_is_present())

# 将警报存储在变量中以供重用
alert = driver.switch_to.alert

# 将警报文本存储在变量中
text = alert.text

# 点击取消按钮
alert.dismiss()

Prompt 提示框
# 等待警报显示
wait.until(expected_conditions.alert_is_present())

# 将警报存储在变量中以供重用
alert = Alert(driver)

# 输入你的信息
alert.send_keys("Selenium")

# 点击确认按钮
alert.accept()

Cookie
# 添加cookie
driver.add_cookie({"name": "key", "value": "value"})

# 获取cookie
driver.get_cookie("foo")

# 获取全部cookie
driver.get_cookies()

# 删除cookie
driver.delete_cookie("test1")

# 删除所有cookie
driver.delete_all_cookies()

iFrame & frameset
# 存储网页元素
iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")

# 切换到选择的 iframe
driver.switch_to.frame(iframe)

# 单击按钮
driver.find_element(By.TAG_NAME, 'button').click()

# 通过 id 切换框架
driver.switch_to.frame('buttonframe')

# 单击按钮
driver.find_element(By.TAG_NAME, 'button').click()

# 基于索引切换到第 2 个 iframe
iframe = driver.find_elements_by_tag_name('iframe')[1]

# 切换到选择的 iframe
driver.switch_to.frame(iframe)

# 切回到默认内容
driver.switch_to.default_content()

窗口和标签页
# 查看当前窗口句柄
driver.current_window_handle

# 打开新标签页并切换到新标签页
driver.switch_to.new_window('tab')

# 关闭标签页或窗口
driver.close()

# 切回到之前的标签页或窗口
driver.switch_to.window(original_window)

# 关闭浏览器
driver.quit()

# 分别获取窗口大小每个尺寸
width = driver.get_window_size().get("width")
height = driver.get_window_size().get("height")

# 或者存储尺寸并在以后查询它们
size = driver.get_window_size()
width1 = size.get("width")
height1 = size.get("height")

# 设置窗口大小
driver.set_window_size(1024, 768)

# 分别获取每个尺寸
x = driver.get_window_position().get('x')
y = driver.get_window_position().get('y')

# 将窗口移动到主显示器的左上角
driver.set_window_position(0, 0)

# 最大化窗口
driver.maximize_window()

# 最小化窗口
driver.minimize_window()

# 全屏窗口
driver.fullscreen_window()

# 屏幕截图
driver.save_screenshot('./image.png')

# 元素屏幕截图
ele = driver.find_element(By.CSS_SELECTOR, 'h1')
ele.screenshot('./image.png')

# 执行js脚本
header = driver.find_element(By.CSS_SELECTOR, "h1")
driver.execute_script('return arguments[0].innerText', header)

# 打印页面
from selenium.webdriver.common.print_page_options import PrintOptions

    print_options = PrintOptions()
    print_options.page_ranges = ['1-2']

    driver.get("printPage.html")

    base64code = driver.print_page(print_options)

元素
交互
发送键位
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()

    # Navigate to url
driver.get("http://www.google.com")

    # Enter "webdriver" text and perform "ENTER" keyboard action
driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)

清除
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

    # Navigate to url
driver.get("http://www.google.com")
    # Store 'SearchInput' element
SearchInput = driver.find_element(By.NAME, "q")
SearchInput.send_keys("selenium")
    # Clears the entered text
SearchInput.clear()

查询定位元素
vegetable = driver.find_element(By.CLASS_NAME, "tomatoes")
vegetable = driver.find_element(By.CSS_SELECTOR, "tomatoes")
vegetable = driver.find_element(By.ID, "tomatoes")
vegetable = driver.find_element(By.NAME, "tomatoes")
vegetable = driver.find_element(By.LINK_TEXT, "tomatoes")
vegetable = driver.find_element(By.PARTIAL_LINK_TEXT, "tomatoes")
vegetable = driver.find_element(By.TAG_NAME, "tomatoes")
vegetable = driver.find_element(By.XPATH, "tomatoes")

# 找第二个元素
fruits = driver.find_element(By.ID, "fruits")
fruit = fruits.find_elements_by_id("tomatoes")

# CSS选择器
fruit = driver.find_element_by_css_selector("#fruits .tomatoes")

# 多个匹配元素
elements = driver.find_elements(By.TAG_NAME, "li")
# 遍历多个元素
for e in elements:
    print(e.text)

# 获取活动元素
 attr = driver.switch_to.active_element.get_attribute("title")
  print(attr)

获取信息
# 是否选择了元素

value = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']:first-of-type").is_selected()

# 获取元素标签名

attr = driver.find_element(By.CSS_SELECTOR, "h1").tag_name

# 获取元素尺寸坐标

res = driver.find_element(By.CSS_SELECTOR, "h1").rect

# 获取当前浏览上下文中元素的特定计算样式属性的值

cssValue = driver.findElement(By.LINK_TEXT, "More information...").value_of_css_property('color')

# 获取元素文本

text = driver.find_element(By.CSS_SELECTOR, "h1").text

相对定位
# 上
email_locator = locate_with(By.TAG_NAME, "input").above({By.ID: "password"})

# 下
password_locator = locate_with(By.TAG_NAME, "input").below({By.ID: "email"})

# 左
cancel_locator = locate_with(By.TAG_NAME, "button").to_left_of({By.ID: "submit"})

# 右
submit_locator = locate_with(By.TAG_NAME, "button").to_right_of({By.ID: "cancel"})

# 附近
email_locator = locate_with(By.TAG_NAME, "input").near({By.ID: "lbl-email"})

# 相对位置链接
submit_locator = locate_with(By.TAG_NAME, "button").below({By.ID: "email"}).to_right_of({By.ID: "cancel"})

选择框
from selenium.webdriver.support.select import Select

select_element = driver.find_element(By.ID,'selectElementID')
select_object = Select(select_element)

# 根据<Select>元素的内部索引选择<option>
select_object.select_by_index(1)

# 根据其值属性选择一个<option>
select_object.select_by_value('value1')

# 根据文本选择一个<option>
select_object.select_by_visible_text('Bread')

# 返回已选择选项的列表[WebElement]
all_selected_options = select_object.all_selected_options

# 返回一个WebElement，该WebElement引用通过遍历DOM找到的第一个选择选项
first_selected_option = select_object.first_selected_option

# 返回<select>元素包含的选项列表[WebElement]
all_available_options = select_object.options

# 根据<select>元素的内部索引取消选择<option>
select_object.deselect_by_index(1)

# Deselect an <option> based upon its value attribute
select_object.deselect_by_value('value1')

# 根据其值属性取消选择<option>
select_object.deselect_by_visible_text('Bread')

# 取消选择所有选定的<option>元素
select_object.deselect_all()

# 是否允许多选
does_this_allow_multiple_selections = select_object.is_multiple

等待
强制等待
import time
time.sleep(10)  # 强制等待10秒时间

显式等待
1. WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
2. driver：webdriver的驱动程序（ie，firefox，chrome，或远程）
3. timeout：最长超时时间，默认单位s
4. poll_frequency=0.5：休眠时间的间隔时间，默认为0.5秒
5. ignored_exceptions=none：超时后的异常信息，默认情况下抛NoSuchElementException 异常
from selenium.webdriver.support.ui import WebDriverWait

driver.navigate("file:///race_condition.html")
el = WebDriverWait(driver).until(lambda d: d.find_element_by_tag_name("p"))
assert el.text == "Hello from JavaScript!"

WebDriverWait(driver, timeout=3).until(some_condition)

隐式等待
driver = Firefox()
driver.implicitly_wait(10)
driver.get("http://somedomain/url_that_delays_loading")
my_dynamic_element = driver.find_element(By.ID, "myDynamicElement")

流畅等待
driver = Firefox()
driver.get("http://somedomain/url_that_delays_loading")
wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))

键盘
按下
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

# 输入“webdriver”文本并执行“Enter”键盘操作
driver.find_element(By.ID, "kw").send_keys("webdriver" + Keys.ENTER)

# 输入框中的ctrl+A操作（局部）
driver.find_element(By.ID, 'kw').send_keys(Keys.CONTROL,"a")

# 执行ctrl+A操作（页面全部）
webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()

弹起
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

# 定位输入框位置
search = driver.find_element(By.ID, "kw")

# shift+'qwerty'
webdriver.ActionChains(driver).key_down(Keys.SHIFT).send_keys_to_element(search, "qwerty").perform()

# 输入文本“QWERTYqwerty”（按下qwerty弹起qwert实现大小写输入）
 webdriver.ActionChains(driver).key_down(Keys.SHIFT).send_keys_to_element(search, "qwerty").key_up(Keys.SHIFT).send_keys("qwerty").perform()

Keys()类提供了键盘上几乎所有按键的方法。 前面了解到， send_keys()方法可以用来模拟键
盘输入， 除此 之外， 我们还可以用它来输入键盘上的按键， 甚至是组合键， 如 Ctrl+A、Ctrl+C 等
# 引入 Keys 模块
from selenium.webdriver.common.keys import Keys
以下为常用的键盘操作：
send_keys(Keys.BACK_SPACE)     删除键（BackSpace）
send_keys(Keys.SPACE)          空格键(Space)
send_keys(Keys.TAB)            制表键(Tab)
send_keys(Keys.ESCAPE)         回退键（Esc）
send_keys(Keys.ENTER)          回车键（Enter）
send_keys(Keys.CONTROL,'a')    全选（Ctrl+A）
send_keys(Keys.CONTROL,'c')    复制（Ctrl+C）
send_keys(Keys.CONTROL,'x')    剪切（Ctrl+X）
send_keys(Keys.CONTROL,'v')    粘贴（Ctrl+V）
send_keys(Keys.F1)             键盘 F1
……
send_keys(Keys.F12)            键盘 F12

鼠标
练习地址https://sahitest.com/demo/dragDropMooTools.htm
点击
# 存储“谷歌搜索”按钮web元素
searchBtn = driver.find_element(By.ID, "s-usersetting-top")

# 对图元执行“单击并按住”操作
webdriver.ActionChains(driver).click()

按下
# 存储“谷歌搜索”按钮web元素
searchBtn = driver.find_element(By.ID, "s-usersetting-top")

# 对图元执行“按住”操作
webdriver.ActionChains(driver).click_and_hold(searchBtn).perform()

移动到元素
# 移动到元素位置
webdriver.ActionChains(driver).move_to_element(gmailLink).perform()

施放
webdriver.ActionChains(driver).click_and_hold(sourceEle).move_to_element(targetEle).perform()
webdriver.ActionChains(driver).release().perform()

右击
# 对元素执行“右击”操作
webdriver.ActionChains(driver).context_click(searchBtn).perform()

双击
# 对元素执行“双击”操作
webdriver.ActionChains(driver).double_click(searchBtn).perform()

按偏移量移动
xOffset = 100
yOffset = 100
# 移动到偏移量位置
webdriver.ActionChains(driver).move_by_offset(xOffset,yOffset).perform()

拖放到目标位置
# 拖放地址
sourceEle = driver.find_element(By.ID, "draggable")
# 释放地址
targetEle  = driver.find_element(By.ID, "droppable")
# 执行操作 (https://park.glitch.me/)
webdriver.ActionChains(driver).drag_and_drop(sourceEle,targetEle).perform()

拖放到偏移位置
# 拖放地址
sourceEle = driver.find_element(By.ID, "draggable")
# 释放地址
targetEle  = driver.find_element(By.ID, "droppable")
# 获得释放地址的x,y坐标
targetEleXOffset = targetEle.location.get("x")
targetEleYOffset = targetEle.location.get("y")
# 拖到指定位置施放
webdriver.ActionChains(driver).drag_and_drop_by_offset(sourceEle, targetEleXOffset, targetEleYOffset).perform()

