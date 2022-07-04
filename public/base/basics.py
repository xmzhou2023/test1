from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from libs.config.conf import LOCATE_MODE,DOWNLOAD_PATH
from libs.common.time_ui import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import os
import logging
import allure
"""
selenium基类
本文件存放了selenium基类的封装方法
"""
class Base(object):
    """selenium基类"""

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(LOCATE_MODE[name], value)

    @classmethod
    @allure.step("遍历所有可用关键字函数")
    def all_keyword(cls):
        _all_keyword = []  # 所有可以用关键字

        for attr in dir(cls):  # 遍历自己的所有成员
            if attr.startswith("key_"):  # 关键字前缀
                method = getattr(cls, attr)
                if callable(method):  # 如果是可调用的
                    _all_keyword.append(attr[4:])
        return _all_keyword

    @property
    @allure.step("获取页面源代码")
    def get_source(self):
        return self.driver.page_source

    @allure.step("打开网址并验证")
    def get_url(self, url):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            logging.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @allure.step("寻找单个元素")
    def find_element(self, locator, choice=None):
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            logging.info("查找元素：{}".format(Npath))
            return Base.element_locator(lambda *args: self.wait.until(
                EC.presence_of_element_located(args)), Npath)
        else:
            logging.info("查找元素：{}".format(locator))
            return Base.element_locator(lambda *args: self.wait.until(
                EC.presence_of_element_located(args)), locator)

    @allure.step("寻找多个相同的元素")
    def find_elements(self, locator):
        return Base.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    @allure.step("获取相同元素个数")
    def elements_num(self, locator):
        number = len(self.find_elements(locator))
        logging.info("相同元素：{}".format((locator, number)))
        return number

    @allure.step("输入文本")
    def input_text(self, locator, txt):
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        logging.info("输入文本：{}".format(txt))

    @allure.step("去除只读属性后输入")
    def readonly_input_text(self, locator, txt):
        sleep(0.5)
        ele = self.find_element(locator)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", ele)
        ele.clear()
        ele.send_keys(txt)
        logging.info("输入文本：{}".format(txt))

    @allure.step("滑动至出现元素")
    def scroll_into_view(self, locator, choice=None):
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            ele = self.find_element(Npath)
            self.driver.execute_script("arguments[0].scrollIntoView()", ele)
            logging.info("滚动条至：{}".format(Npath))
        else:
            ele = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView()", ele)
            logging.info("滚动条至：{}".format(locator))

    @allure.step("点击元素")
    def is_click(self, locator, choice=None):
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            sleep(2)
            self.find_element(Npath).click()
            logging.info("选择点击：{}".format(Npath))
        else:
            self.find_element(locator).click()
            logging.info("点击元素：{}".format(locator))

    @allure.step("点击元素(用js)")
    def force_click(self, xpath, force=False):
        ele = self.find_element(xpath)
        if force:  # 使用js强制点击
            self.driver.execute_script("argumnets[0].click()", ele)
        else:
            ele.click()

    @allure.step("确认弹窗")
    def alert_ok(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    @allure.step("切换frame")
    def frame_enter(self, xpath):
        ele = self.find_element(xpath)
        assert ele.tag_name == "iframe"
        self.driver.switch_to.frame(ele)

    @allure.step("返回frame")
    def frame_exit(self):
        self.driver.switch_to.parent_frame()  # 返回上一层

    @allure.step("去顶层frame")
    def frame_top(self):
        self.driver.switch_to.default_content()  # 返回到顶层

    @allure.step("编辑用户权限-竖tab切换(DRP专用)")
    def edituser_tab_click(self, locator, choice=None, pane=None):
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            if pane is not None:
                original = "@id='pane-1'"
                pane_str = original.replace('1', str(pane))
                Npath[1] = Npath[1].replace("@id='pane-1'", pane_str)
            self.find_element(Npath).click()
            logging.info("设置权限：{}".format(Npath))
        else:
            self.find_element(locator).click()
            # sleep()
            logging.info("点击元素：{}".format(locator))

    @allure.step("编辑用户权限-清除勾选框(DRP组织、品牌专用)")
    def checkbox_init(self,locator, pane=None):
        """"""
        Npath = []
        Npath.append(locator[0])
        Npath.append(locator[1])
        original = "@id='pane-num'"
        pane_str = original.replace('num', str(pane))
        Npath[1] = Npath[1].replace("@id='pane-num'", pane_str)
        element = len(self.driver.find_elements(By.XPATH, Npath[1]))
        if element != 0:
            elements = self.find_elements(Npath)
            for i in range(len(elements)):
                if elements:
                    self.find_element(Npath).click()
                else:
                    break
            logging.info("清除权限：{}".format(Npath))
        else:
            logging.info("清除权限: 未勾选任何权限")

    @allure.step("编辑用户权限-初孡化勾选框(DRP专用)")
    def tree_init(self, locator, choice=None):
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            self.find_element(Npath).click()
            self.find_element(Npath).click()
            logging.info("清除树勾选框状态：{}".format(Npath))
        else:
            self.find_element(locator).click()
            self.find_element(locator).click()
            # sleep()
            logging.info("清除树勾选框状态：{}".format(locator))

    @allure.step("点击空白区域，用于取消释法")
    def move_house(self, content):
        """点击空白区域，用于取消释法"""
        ActionChains(content).move_by_offset(700, 700).click().perform()
        sleep(10)

    @allure.step("获取元素的文本")
    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        logging.info("获取文本：{}".format(_text))
        return _text

    @allure.step("获取元素的选中状态")
    def select_state(self, locator):
        _select = self.find_element(locator).is_selected()
        logging.info("获取状态：{}".format(_select))
        return _select

    @allure.step("刷新页面F5")
    def refresh(self):
        self.driver.refresh()
        self.driver.implicitly_wait(30)

    @allure.step("切换窗口")
    def switch_window(self, n):
        self.driver.switch_to.window(self.driver.window_handles[n])

    @allure.step("关闭窗口")
    def close_switch(self, n):
        self.driver.switch_to.window(self.driver.window_handles[n])  # 切换到新页签
        self.driver.close()  # 关闭新页签
        self.driver.switch_to.window(self.driver.window_handles[0])  # 然后切换回原始页签

    @allure.step("鼠标悬停")
    def hover(self,locator):
        element = self.find_element(locator)
        # 创建Action对象
        actions = ActionChains(self.driver)
        actions.move_to_element(element)

    @allure.step("清空下载路径")
    def clear_download(self):
        for file in os.listdir(DOWNLOAD_PATH):
            if len(file) > 0:
                os.remove(DOWNLOAD_PATH + r"/" + file)

    @allure.step("下载到指定路径")
    def download_file(self, filename, load=1):
        try:
            if os.path.exists(DOWNLOAD_PATH):
                logging.info("指定下载路径: {}".format(DOWNLOAD_PATH))
                sleep(int(load))
                logging.info(os.listdir(DOWNLOAD_PATH))
                for file in os.listdir(DOWNLOAD_PATH):
                    if filename in file:
                        return True
                    return False
        except Exception:
            return

    @allure.step("下载并断言文件名是否符合预期")
    def check_download(self, locator, content):
        self.clear_download()
        self.find_element(locator).click()
        assert self.download_file(filename=content, load=3), logging.warning("断言失败: 下载该附件失败 | {} ".format(content))
        logging.info("断言成功: 下载该附件成功 | {} ".format(content))

    @allure.step("树结构专用查找多个相同的元素(原生)")
    def custom_find_elements(self,locator):
        return self.driver.find_elements(By.XPATH, locator[1])

    @allure.step("输入文本(DCR专用)")
    def input_text_dcr(self, locator, txt):
        """ """
        sleep(1)
        ele = self.find_elements_dcr(locator)
        ele[0].clear()
        ele[0].send_keys(txt)
        logging.info("输入文本：{}".format(txt))

    @allure.step("点击元素(DCR专用)")
    def is_click_dcr(self, locator, choice=None):
        if choice is not None:
            logging.info(locator)
            logging.info(choice)
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            self.find_elements_dcr(Npath)[0].click()
            logging.info("下拉选择：{}".format(Npath))
        else:
            self.find_elements_dcr(locator)[0].click()
            logging.info("点击元素：{}".format(locator))

    @allure.step("查找相同元素(DCR专用)")
    def find_elements_dcr(self, locator):
        return Base.element_locator(lambda *args: self.wait.until(
            EC.visibility_of_any_elements_located(args)), locator)


if __name__ == "__main__":
    pass
