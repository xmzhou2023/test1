#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:huangqin
# @time:2022/3/10 16:58
'''
selenium元素操作行为：常规篇
1.访问url,点击，输入，close与quit,元素定位
'''
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# 启动chromedriver.exe,并驱动浏览器的生成
driver = webdriver.Chrome()
# 访问url
driver.get('http://www.baidu.com')
# 元素定位find_element_*的函数在selenium4版本中已经被弃用
input_txt = driver.find_element()
# 输入文本：send_keys只运用于input标签
input_txt.send_keys('qwe')

# 点击
driver.find_element('id', '').click()

# 文件上传
driver.find_element('xpath', '').click()
time.sleep(4)
# 文件上传也通过send_keys函数，输入文件的完整路径及文件名称及后缀名，只限于input标签可以使用;非input标签来上传, 则需要应用到autoIT的库来实现
driver.find_element('xpath', '').send_keys(r'D:/kjkjk/kk.jpg')

# 关闭浏览器，并释放后台进程
driver.quit()
# 对于close,是关闭当前标签页，而非浏览器，而且不会释放后台进程
driver.close()


'''
特定的元素操作行为
1.句柄(控制标签页)：句柄的操作一定要注意最多保留2个标签页，特殊情况不要超过3个
2.句柄的切换并不是固定不变的，要根据业务考量
3.iframe的处理(内嵌窗体)
'''

# 句柄的获取与切换
handles = driver.window_handles
# 关闭当前标签页
driver.close()
# 句柄的切换
driver.switch_to.window(handles[1])
print('切换后')
print(driver.title)

# 切换后的操作
driver.find_element('link text', '首页').click()

'''
iframe窗体中的元素如果要获取，则需要切换到iframe之中，再去操作
'''
# 切换iframe,可通过元素，下表，
el = driver.find_element('xpath', '')
driver.switch_to.frame(el)
# 可以操作iframe中的元素，注意：只能够操作iframe的元素
# 操作完iframe之后，需要切换到默认窗体
driver.switch_to.default_content()

'''
selenium4更新：
1、常态化的元素操作行为的优化
2、新增一部分操作行为
3、针对浏览器新增一些行为
4、更新了selenium分布式架构技术的体系内容
'''

# 页面加载策略
options = webdriver.ChromeOptions()
options.page_load_strategy = 'none', 'normal', 'eager'  # none可提升加载速度，none是页面未加载完成就可以操作
drivers = webdriver.Chrome(options=options)


# 相对定位器
'''
传统定位是基于八大元素定位法则进行的元素定位
相对定位器是基于人的方向认知进行的元素定位---没什么用：在UI元素密集的情况下，相对定位器极大概率会返回多个不同的元素，无法精准定位
'''
from selenium.webdriver.support.relative_locator import locate_with
# 1、定位一个元素
el = driver.find_element('xpath', '')
# 2、基于已有的元素进行相对定位，方向为上下左右附近，共五种方法
driver.find_element(locate_with(By.TAG_NAME, 'input').to_left_of(el))
driver.find_element(locate_with(By.TAG_NAME, 'input').to_right_of(el))
driver.find_element(locate_with(By.TAG_NAME, 'input').above(el))
driver.find_element(locate_with(By.TAG_NAME, 'input').below(el))
driver.find_element(locate_with(By.TAG_NAME, 'input').near(el))



# 解决特殊场景的应用：多端的特殊场景的应用，生成并切换句柄
driver.switch_to.new_window('window') # 新增一个浏览器页面
driver.switch_to.new_window('tab') # 新增一个标签页面


'''
selenium grid:分布式框架部署：增加event bus,session queue,异步处理机制的优化，hub端的节点管理优化。。。可用于提升自动化效率
'''
# 

