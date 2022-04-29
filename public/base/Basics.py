from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from libs.config.conf import LOCATE_MODE
from libs.common.time_ui import sleep
from libs.common.logger_ui import log
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

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

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(LOCATE_MODE[name], value)

    def find_element(self, locator, choice=None):
        """寻找单个元素"""
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            log.info("查找元素：{}".format(Npath))
            return Base.element_locator(lambda *args: self.wait.until(
                EC.presence_of_element_located(args)), Npath)
        else:
            log.info("查找元素：{}".format(locator))
            return Base.element_locator(lambda *args: self.wait.until(
                EC.presence_of_element_located(args)), locator)

    def find_elements(self, locator):
        """查找多个相同的元素"""
        return Base.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        log.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def readonly_input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_element(locator)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", ele)
        ele.clear()
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def scroll_into_view(self, locator, choice=None):
        """滑动至出现"""
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            ele = self.find_element(Npath)
            self.driver.execute_script("arguments[0].scrollIntoView()", ele)
            log.info("滚动条至：{}".format(Npath))
        else:
            ele = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView()", ele)
            log.info("滚动条至：{}".format(locator))

    def is_click(self, locator, choice=None):
        """点击"""
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            self.find_element(Npath).click()
            log.info("下拉选择：{}".format(Npath))
        else:
            self.find_element(locator).click()
            # sleep()
            log.info("点击元素：{}".format(locator))

    def force_click(self, xpath, force=False):
        """
        关键字：click

        自定等待元素，然后进行点击
        :param xpath: 元素定位表达式
        :param force: 是否强制点击
        :return:
        """

        ele = self.find_element(xpath)

        if force:  # 使用js强制点击
            self.driver.execute_script("argumnets[0].click()", ele)
        else:
            ele.click()

    def alert_ok(self):
        """
        关键字：alert_ok
        为alert点击确定
        :return:
        """
        alert = self.wait.until(EC.alert_is_present())

        alert.accept()

    def frame_enter(self, xpath):
        """
        关键字 ：frame_enter
        进入到指定的frame

        :param xpath: 元素定位表达式
        :return:
        """
        ele = self.find_element(xpath)
        assert ele.tag_name == "iframe"

        self.driver.switch_to.frame(ele)

    def frame_exit(self):
        """
        关键字 ：frame_exit
        退出当前的frame

        :return:
        """

        self.driver.switch_to.parent_frame()  # 返回上一层

    def frame_top(self):
        """
        关键字 ：frame_top
        返回顶层frame

        :return:
        """

        self.driver.switch_to.default_content()  # 返回到顶层

    def edituser_tab_click(self, locator, choice=None, pane=None):
        """编辑用户权限-竖tab切换"""
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
            log.info("设置权限：{}".format(Npath))
        else:
            self.find_element(locator).click()
            # sleep()
            log.info("点击元素：{}".format(locator))

    def checkbox_init(self,locator, pane=None):
        """编辑用户权限-清除勾选框（组织、品牌用）"""
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
            log.info("清除权限：{}".format(Npath))
        else:
            log.info("清除权限: 未勾选任何权限")

    def tree_init(self, locator, choice=None):
        """编辑用户权限-初孡化勾选框"""
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            self.find_element(Npath).click()
            self.find_element(Npath).click()
            log.info("清除树勾选框状态：{}".format(Npath))
        else:
            self.find_element(locator).click()
            self.find_element(locator).click()
            # sleep()
            log.info("清除树勾选框状态：{}".format(locator))

    def click_blank(self, ):
        """点击空白区域，用于取消释法"""
        sleep(10)

    def move_house(self, content):
        """点击空白区域，用于取消释法"""
        ActionChains(content).move_by_offset(700, 700).click().perform()
        sleep(10)

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        log.info("获取文本：{}".format(_text))
        return _text

    def select_state(self, locator):
        """是否被选中"""
        _select = self.find_element(locator).is_selected()
        log.info("获取状态：{}".format(_select))
        return _select

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)

    def switch_window(self, n):
        """窗口切换"""
        self.driver.switch_to.window(self.driver.window_handles[n])

    def close_switch(self, n):
        """关闭页签"""
        self.driver.switch_to.window(self.driver.window_handles[n])  # 切换到新页签
        self.driver.close()  # 关闭新页签
        self.driver.switch_to.window(self.driver.window_handles[0])  # 然后切换回原始页签

    def hover(self,locator):
        """鼠标悬停"""
        element = self.find_element(locator)
        # 创建Action对象
        actions = ActionChains(self.driver)
        actions.move_to_element(element)

    @classmethod
    def all_keyword(cls):
        """
        列出所有可用的关键字：

        1. key_开头
        2. 可调用的
        :return:
        """

        _all_keyword = []  # 所有可以用关键字

        for attr in dir(cls):  # 遍历自己的所有成员
            if attr.startswith("key_"):  # 关键字前缀
                method = getattr(cls, attr)
                if callable(method):  # 如果是可调用的
                    _all_keyword.append(attr[4:])

        return _all_keyword

    def custom_find_elements(self,locator):
        """树结构专用查找多个相同的元素"""
        return self.driver.find_elements(By.XPATH, locator[1])



if __name__ == "__main__":
    pass
