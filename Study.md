### action - 浏览器操作

导航：
# 打开网站
driver.get("https://selenium.dev")
# 后退
driver.back()
# 前进
driver.forward()
# 刷新
driver.refresh()

Alerts 警告框：
# 等待警报显示，并将其存储在变量中
alert = wait.until(expected_conditions.alert_is_present())
# 将警报文本存储在变量中
text = alert.text
# 点击确定按钮
alert.accept()

Confirm 确认框:
# 等待警报显示
wait.until(expected_conditions.alert_is_present())
# 将警报存储在变量中以供重用
alert = driver.switch_to.alert
# 将警报文本存储在变量中
text = alert.text
# 点击取消按钮
alert.dismiss()

Prompt 提示框：
# 等待警报显示
wait.until(expected_conditions.alert_is_present())

# 将警报存储在变量中以供重用
alert = Alert(driver)

# 输入你的信息
alert.send_keys("Selenium")

# 点击确认按钮
alert.accept()

Cookie :
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

# 创建新窗口(或)新标签页并且切换
```
    # 打开新标签页并切换到新标签页
driver.switch_to.new_window('tab')

    # 打开一个新窗口并切换到新窗口
driver.switch_to.new_window('window')
```
#关闭标签页或窗口
driver.close()

#切回到之前的标签页或窗口
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

