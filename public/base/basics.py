import datetime
import time
import openpyxl
import xlrd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from libs.config.conf import LOCATE_MODE, DOWNLOAD_PATH, IMAGE_PATH, BASE_DIR
from libs.common.time_ui import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import logging
import allure
import datetime
import ddddocr
from selenium.webdriver.chrome.options import Options


import warnings
from PIL import Image

"""git
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
    def all_keyword(cls):
        """遍历所有可用关键字函数"""
        _all_keyword = []  # 所有可以用关键字

        for attr in dir(cls):  # 遍历自己的所有成员
            if attr.startswith("key_"):  # 关键字前缀
                method = getattr(cls, attr)
                if callable(method):  # 如果是可调用的
                    _all_keyword.append(attr[4:])
        return _all_keyword

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

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

    def get_graphical_code(self, locator):
        """获取图形验证码"""
        # 验证码下载路径
        html_path = os.path.join(DOWNLOAD_PATH, 'driver_html.png')
        code_path = os.path.join(DOWNLOAD_PATH, 'code.png')
        time.sleep(3)  # 定个缓冲时间

        self.driver.save_screenshot(html_path)  # 截取整个网页
        location = self.find_element(locator)  # 获取需要识别的元素对象
        size = location.size  # 获取需要识别的元素尺寸

        # 获取验证码图片的坐标大小
        rangle = (int(location.location['x']), int(location.location['y']), int(location.location['x'] + size['width']),
                  int(location.location['y'] + size['height']))

        # 打开保存的网页图片并截取验证码区域并保存
        Image.open(html_path).crop(rangle).save(code_path)

        # 识别截图内容验证码
        ocr = ddddocr.DdddOcr()

        with open(code_path, "rb") as f:
            img_bytes = f.read()

        res = ocr.classification(img_bytes)

        return res

    def send_enter(self):  # 夏小珍新增 2022-9-2
        """回车"""
        ActionChains(self).send_keys(Keys.ENTER)

    def is_click(self, locator, *args, **kwargs):
        """点击元素"""
        if args and args is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            for i in range(len(args)):
                Npath[1] = Npath[1].replace('variable', str(args[i]), 1)
            sleep(2)
            self.find_element(Npath).click()
            logging.info("选择点击：{}".format(Npath))

        elif kwargs and kwargs is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', str(kwargs['choice']))
            logging.info(Npath)
            sleep(2)
            self.find_element(Npath).click()
            logging.info("选择点击：{}".format(Npath))

        else:
            self.find_element(locator).click()
            logging.info("点击元素：{}".format(locator))
            sleep(0.5)

    def find_element(self, locator, *args, **kwargs):
        """寻找单个元素"""
        if args and args is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            for i in range(len(args)):
                Npath[1] = Npath[1].replace('variable',str(args[i]),1)
            logging.info("查找元素：{}".format(Npath))
            return Base.element_locator(lambda *args: self.wait.until(
                EC.presence_of_element_located(args)), Npath)

        elif kwargs and kwargs is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', str(kwargs['choice']))
            logging.info("查找元素：{}".format(Npath))
            return Base.element_locator(lambda *args: self.wait.until(
                EC.presence_of_element_located(args)), Npath)
        else:
            logging.info("查找元素：{}".format(locator))
            return Base.element_locator(lambda *args: self.wait.until(
                EC.presence_of_element_located(args)), locator)

    def find_elements(self, locator, *args, **kwargs):
        """寻找多个相同的元素"""
        if args and args is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            for i in range(len(args)):
                Npath[1] = Npath[1].replace('variable', str(args[i]), 1)
            logging.info("查找元素：{}".format(Npath))
            return Base.element_locator(lambda *args: self.wait.until(
                EC.presence_of_all_elements_located(args)), Npath)
        elif kwargs and kwargs is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', str(kwargs['choice']))
            logging.info("查找元素：{}".format(Npath))
            return Base.element_locator(lambda *args: self.wait.until(
                EC.presence_of_all_elements_located(args)), Npath)
        else:
            return Base.element_locator(lambda *args: self.wait.until(
                EC.presence_of_all_elements_located(args)), locator)

    def elements_num(self, locator):
        """获取相同元素个数"""
        number = len(self.find_elements(locator))
        logging.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt, choice=None):
        """输入文本"""
        if choice is None:
            sleep(0.5)
            ele = self.find_element(locator)
            ele.clear()
            ele.clear()
            ele.send_keys(txt)
            logging.info("输入文本：{}".format(txt))
        else:
            """输入(输入前先清空)"""
            sleep(0.5)
            ele = self.find_element(locator, choice)
            ele.clear()
            ele.clear()
            ele.send_keys(txt)
            logging.info("输入文本：{}".format(txt))

    def clear_code(self, locator):
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.clear()
        return ele


    def readonly_input_text(self, locator, txt, *choice):
        """去除只读属性后输入"""
        if choice is None:
            sleep(0.5)
            ele = self.find_element(locator)
            self.driver.execute_script("arguments[0].removeAttribute('readonly')", ele)
            ele.clear()
            ele.clear()
            ele.send_keys(txt)
            logging.info("输入文本：{}".format(txt))
        else:
            sleep(0.5)
            ele = self.find_element(locator, *choice)
            self.driver.execute_script("arguments[0].removeAttribute('readonly')", ele)
            ele.clear()
            ele.clear()
            ele.send_keys(txt)
            logging.info("输入文本：{}".format(txt))

    def scroll_into_view(self, locator, *args, **kwargs):
        """滑动至出现元素"""
        ele = self.find_element(locator, *args, **kwargs)
        self.driver.execute_script("arguments[0].scrollIntoView()", ele)
        logging.info("滚动条至：{}".format(locator, *args, **kwargs))

    def scroll_into_view_CRM(self, locator, choice=None):
        """滑动至出现元素"""
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            ele = self.find_element(Npath).click()
            self.driver.execute_script("arguments[0].scrollIntoView()", ele)
            logging.info("滚动条至：{}".format(Npath))
        else:
            ele = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView()", ele)
            self.find_element(locator).click()
            logging.info("滚动条至：{}".format(locator))

    def force_click(self, xpath, force=False, xpath_js=None):
        """点击元素(用js)"""
        if xpath_js == None:
            ele = self.find_element(xpath)
            if force:  # 使用js强制点击
                self.driver.execute_script("argumnets[0].click()", ele)
            else:
                ele.click()
        else:
            self.driver.execute_script('document.evaluate("{}",document).iterateNext().click()'.format(xpath))


    def alert_ok(self):
        """确认弹窗"""
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def frame_enter(self, xpath):
        """切换frame"""
        ele = self.find_element(xpath)
        assert ele.tag_name == "iframe"
        self.driver.switch_to.frame(ele)

    def frame_back(self):
        """返回frame"""
        self.driver.switch_to.parent_frame()  # 返回上一层

    def frame_exit(self):
        """去顶层frame"""
        self.driver.switch_to.default_content()  # 返回到顶层

    def edituser_tab_click(self, locator, choice=None, pane=None):
        """编辑用户权限-竖tab切换(DRP专用)"""
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

    def checkbox_init(self,locator, pane=None):
        """编辑用户权限-清除勾选框(DRP组织、品牌专用)"""
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

    def tree_init(self, locator, choice=None):
        """编辑用户权限-初孡化勾选框(DRP专用)"""
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


    def export_download_status(self, click_search, get_status):
        """DCR通用的导出，等待下载状态更新(DRP专用)"""
        self.is_click(click_search)
        status = self.element_text(get_status)
        logging.info("循环前Download Status{}".format(status))
        for i in range(20):
            if status != "COMPLETE":
                self.is_click(click_search)
                status = self.element_text(get_status)
                logging.info("循环后Download Status{}".format(status))
                sleep(1)
                i += 1
                logging.info("打印循环执行查询次数{}".format(i))
        return status

    def import_record_status(self, click_search, get_status):
        """DCR通用的导出，等待导入状态更新(DRP专用)"""
        self.is_click(click_search)
        status = self.element_text(get_status)
        logging.info("循环前Download Status{}".format(status))
        for i in range(10):
            if status != "Upload Successfully":
                self.is_click(click_search)
                status = self.element_text(get_status)
                logging.info("循环后Import Status{}".format(status))
                sleep(1)
                i += 1
                logging.info("打印循环执行查询次数{}".format(i))
        return status

    def move_house(self, content):
        """点击空白区域，用于取消释法"""
        ActionChains(content).move_by_offset(700, 700).click().perform()
        sleep(10)

    def element_text(self, locator, *args, **kwargs):
        """获取元素的文本"""
        if args and args is not None:
            ele = self.find_element(locator, *args)
            _text = ele.text.replace("\n", "|")
            logging.info("获取文本：{}".format(_text))
            return _text
        elif kwargs and kwargs is not None:
            ele = self.find_element(locator, *kwargs)
            _text = ele.text.replace("\n", "|")
            logging.info("获取文本：{}".format(_text))
            return _text
        else:
            _text = self.find_element(locator).text.replace("\n", "|")
            logging.info("获取文本：{}".format(_text))
            return _text


    def select_state(self, locator):
        """获取元素的选中状态"""
        _select = self.find_element(locator).is_selected()
        logging.info("获取状态：{}".format(_select))
        return _select

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)
        logging.info('刷新页面')

    def switch_window(self, n):
        """切换窗口"""
        self.driver.switch_to.window(self.driver.window_handles[n])

    def close_switch(self, n):
        """关闭窗口"""
        self.driver.switch_to.window(self.driver.window_handles[n])  # 切换到新页签
        self.driver.close()  # 关闭新页签
        self.driver.switch_to.window(self.driver.window_handles[0])  # 然后切换回原始页签

    def hover(self,locator, choice=None):
        """鼠标悬停"""
        if choice is None:
            sleep(1)
            element = self.find_element(locator)
            # 创建Action对象
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            sleep(1)
        else:
            sleep(1)
            element = self.find_element(locator, choice)
            # 创建Action对象
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            sleep(1)

    def clear_download(self):
        """清空下载路径"""
        for file in os.listdir(DOWNLOAD_PATH):
            if len(file) > 0:
                os.remove(DOWNLOAD_PATH + r"/" + file)

    def download_file(self, filename, load=1):
        """下载到指定路径"""
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

    def check_download(self, locator, content):
        """下载并断言文件名是否符合预期"""
        self.clear_download()
        self.find_element(locator).click()
        assert self.download_file(filename=content, load=3), logging.warning("断言失败: 下载该附件失败 | {} ".format(content))
        logging.info("断言成功: 下载该附件成功 | {} ".format(content))

    def custom_find_elements(self,locator):
        """树结构专用查找多个相同的元素(原生)"""
        return self.driver.find_elements(By.XPATH, locator[1])

    def input_text_dcr(self, locator, txt):
        """输入文本(DCR专用)"""
        sleep(1)
        ele = self.find_elements_dcr(locator)
        ele[0].clear()
        ele[0].send_keys(txt)
        logging.info("输入文本：{}".format(txt))

    def is_click_dcr(self, locator, choice=None):
        """点击元素(DCR专用)"""
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

    def find_elements_dcr(self, locator):
        """查找相同元素(DCR专用)"""
        return Base.element_locator(lambda *args: self.wait.until(
            EC.visibility_of_any_elements_located(args)), locator)

    def presence_sleep_dcr(self, locator, *args, **kwargs):
        """通用的加载数据等待方法(DCR专用)"""
        txt = None
        if args and args is not None:
            for i in range(10):
                if txt is None:
                    txt = self.find_element(locator, args[0])
                    sleep(1)
                    i += 1
                    logging.info("循环查找元素次数:{}".format(i))
                else:
                    break
        elif kwargs and kwargs is not None:
            for i in range(10):
                if txt is None:
                    txt = self.find_element(locator, kwargs['choice'])
                    sleep(1)
                    i += 1
                    logging.info("循环查找元素次数:{}".format(i))
                else:
                    break
        else:
            for i in range(10):
                if txt is None:
                    txt = self.find_element(locator)
                    sleep(1)
                    i += 1
                    logging.info("循环查找元素次数:{}".format(i))
                else:
                    break


    def get_datetime_today(self):
        """获取当天日期(DCR专用)"""
        today = datetime.date.today()
        today1 = str(today)
        return today1

    def base_get_img(self, name='err'):
        """截图方法"""
        imgname = IMAGE_PATH + '\\' + "{}.png".format(name)
        # 保存截图 error日志
        logging.error("正在截图...")
        self.driver.get_screenshot_as_file(imgname)
        # 写入报告
        self.__base_write_img(imgname)

    def __base_write_img(self, imgname):
        """读图片"""
        logging.error("日志正在附加截图...")
        with open(imgname, 'rb') as f:
            # 附加报告
            allure.attach(f.read(), "断言截图:", allure.attachment_type.PNG)
        logging.error("日志附加截图成功")

    def read_excel(self, path, path_list):
        """"""
        wb = openpyxl.load_workbook(r'{}\{}'.format(path, path_list))
        sheets = wb.sheetnames
        ws = wb[sheets[0]]
        info_list = []
        for i in list(ws.rows)[1:]:
            info = []
            for cell in i:
                info.append(str(cell.value))
            info_list.append(info)
        logging.info('excel表格内容：{}'.format(info_list))
        return info_list

    def delete_excel(self, path, path_list):
        """删除excel"""
        os.remove(r'{}\{}'.format(path, path_list))
        logging.info('删除文件成功')

    def read_excel_flow(self):
        """读Excel"""
        try:
            path = DOWNLOAD_PATH
            path_list = os.listdir(path)
            logging.info(path)
            logging.info('download文件夹内有文件：{}'.format(path_list))
            assert len(path_list) != 0
        except:
            path = os.path.join(BASE_DIR)
            path_list = os.listdir(DOWNLOAD_PATH)
            logging.info(path)
            logging.info('download文件夹内有文件：{}'.format(path_list))
        try:
            return self.read_excel(path, path_list[-1])
        except Exception as e:
            logging.error(e)
            raise
        # finally:
            # self.delete_excel(path, path_list[-1])

    def element_exist(self, locator, *choice):
        """校验元素是否存在"""
        self.base_get_img()
        try:
            self.find_element(locator, *choice)
        except:
            logging.error('{}元素不存在'.format(locator))
            self.base_get_img()
            return False
        else:
            logging.info('存在元素：{}'.format(locator))
            self.base_get_img()
            return True

    def upload_file(self,locator,file, *choice):
        """上传"""
        sleep(0.5)
        ele = self.find_element(locator,*choice)
        ele.send_keys(file)
        logging.info("上传文件：{}".format(file))

    def get_element_attribute(self, locator, attribute, *choice):
        """获取元素属性值"""
        sleep(0.5)
        ele = self.find_element(locator, *choice)
        attribute_value = ele.get_attribute('{}'.format(attribute))
        logging.info("获取元素属性：{}，属性值为：{}".format(attribute, attribute_value))
        return attribute_value

    def change_attribute_value(self, locator, choice=None, type='style', content='display: none;'):
        """获取元素属性值"""
        ele = self.find_element(locator, choice)
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", ele, type, content)
        logging.info("使用JS脚本修改属性")

    def find_elements_tbm(self, locator, choice=None):
        """查找多个相同的元素（TBM专用）"""
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            logging.info("正在查找元素：{}".format(Npath))
            return Base.element_locator(lambda *args: self.wait.until(
                EC.visibility_of_all_elements_located(args)), Npath)
        else:
            return Base.element_locator(lambda *args: self.wait.until(
                EC.visibility_of_all_elements_located(args)), locator)

    def is_click_tbm(self, locator, *choice):
        """点击（TBM专用）"""
        try:
            ele = self.find_element(locator, *choice)
            try:
                ele.click()
                sleep(0.5)
            except:
                self.driver.execute_script("arguments[0].click();", ele)
                sleep(0.5)
        except:
            ele = self.find_element(locator, *choice)
            self.driver.execute_script("arguments[0].scrollIntoView()", ele)
            try:
                ele.click()
                sleep(0.5)
            except:
                self.driver.execute_script("arguments[0].click();", ele)
                sleep(0.5)
        logging.info("点击元素：{}{}".format(locator, choice))

    def element_input_text(self, locator, *choice):
        """获取输入框当前的text"""
        ele = self.find_element(locator, *choice)
        _text = ele.get_attribute('value')
        logging.info("获取文本：{}".format(_text))
        return _text

    def mouse_click(self,locator):
        """鼠标点击"""
        element = self.find_element(locator)
        # 创建Action对象
        actions = ActionChains(self.driver)
        actions.click(element).perform()

    def mouse_double_click(self, locator, *args, **kwargs):
        """鼠标双击"""
        element = self.find_element(locator, *args, **kwargs)
        # 创建Action对象
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()


    def mouse_right_click(self, locator, *args, **kwargs):
        """鼠标右击"""
        if args and args is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            for i in range(len(args)):
                Npath[1] = Npath[1].replace('variable', args[i], 1)
            sleep(0.5)
            element = self.find_element(Npath)
            actions = ActionChains(self.driver)
            actions.context_click(element).perform()
            logging.info("选择点击：{}".format(Npath))
        elif kwargs and kwargs is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', str(kwargs['choice']))
            sleep(0.5)
            element = self.find_element(Npath)
            actions = ActionChains(self.driver)
            actions.context_click(element).perform()
            logging.info("选择点击：{}".format(Npath))
        else:
            element = self.find_element(locator)
            actions = ActionChains(self.driver)
            actions.context_click(element).perform()
            logging.info("点击元素：{}".format(locator))
            sleep(0.5)

    def mouse_hover(self, locator, choice=None):
        """TLC专用鼠标悬停"""
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            sleep(0.5)
            element = self.find_element(Npath)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            logging.info("hover元素：{}".format(Npath))
        else:
            element = self.find_element(locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            logging.info("hover元素：{}".format(locator))
            sleep(0.5)
    def clear_input(self, xpath):
        # 清除文本框输入，srm使用
        ele = self.find_element(xpath)
        ele.clear()

    def hover_click(self, locator):
        # 鼠标悬停后点击
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions.click(element).perform()

    def keyboard_enter(self, locator):
        # 键盘回车
        element = self.find_element(locator)
        element.send_keys(Keys.ENTER)

    def keyboard_backspace(self, locator):
        # 键盘删除键
        element = self.find_element(locator)
        element.send_keys(Keys.BACK_SPACE)

    def get_table_info(self, locator, *choice, attr='class', index='0'):
        """
        获取指定定位的属性值，可用于获取表格每列内容，做查询断言，如：el-table_3_column_45
        :param attr: 需要获取到的属性，默认是class
        :param index: 需要获取到的属性索引位置，默认是0
        """
        header_class = self.get_element_attribute(locator, attr, *choice)
        column_class = header_class.split(' ')[int(index)]
        logging.info('获取定位属性：{}的第{}个属性值：{}'.format(attr, index, column_class))
        return column_class

    # POP输入框输入文本按enter键专用方法
    def input_enter(self,locator,content=None,choice=None):
        """
            POP项目中输入框输入内容点击Enter键
        :param locator: 定位元素-固定格式=>xx['']
        :param content: 参数值，例如输入框需要输入的内容
        :param choice: 元素定位传入“variable”参数值
        :return: 无
        """
        if choice is None:
            sleep(0.5)
            ele = self.find_element(locator,choice)
            ele.clear()
            ele.send_keys(content + Keys.ENTER)
            logging.info("输入文本：{}".format(content))
        else:
            """输入(输入前先清空)"""
            sleep(0.5)
            ele = self.find_element(locator,choice)
            ele.clear()
            ele.send_keys(content + Keys.ENTER)
            logging.info("输入文本：{}".format(content))


    def DivRolling(self, locator, direction='left', num=1000):
        '''
        内嵌div上下左右滑动
        :param locator: 内嵌div
        :param direction: 滚动条滚动方向
        :param num: 内边距
        '''
        try:
            ele = self.find_element(locator)
            if direction == 'top':
                self.driver.execute_script("arguments[0].scrollTop={}".format(num), ele)
                logging.info('滚动条向下滑动：{}'.format(num))
            elif direction == 'left':
                self.driver.execute_script("arguments[0].scrollLeft={}".format(num), ele)
                logging.info('滚动条向右滑动：{}'.format(num))
            else:
                logging.error('请输入direction参数：left or top')
        except Exception as e:
            raise e

def read_excel(file_path,sheet_name,data_num=7,expect_num=8):
    """
        读取excel表测试数据
    @param file_path: 测试数据文件保存地址
    @param sheet_name: 测试数据表对应sheet名称
    @param data_num: 测试参数的数据所在测试数据表格的列数，以索引计算，起始数字为0
    @param expect_num: 测试预期结果的数据所在测试数据表格的列数，以索引计算，起始数字为0
    @return: 测试数据值--列表套元组
    """
    # 打开文件
    workbook = xlrd.open_workbook(file_path)
    # 读取第一张表
    sheet = workbook.sheet_by_name(sheet_name)
    # 获取行数
    row = sheet.nrows
    # 声明一个空列表用于保存处理后需要的数据
    li = []
    # 获取每行数据--从第三行开始的所以数据（0--对应第一行，1--对应第二行）
    for i in range(1, row):
        # 获取每行数据
        each_row = sheet.row_values(i)
        print(each_row)
        # 定位到测试步骤参数列，并以\n换行隔开返回为列表
        data = each_row[data_num].split("\n")
        # 将预期结果列添加到data表格中
        data.append(each_row[expect_num])
        # 在家data列表添加到li列表形成二维列表--[[]]
        li.append(tuple(data))
    return li


def data_drive_excel(file_path, sheet_name, mode, rows=0, cols=0, start_col=0, end_col=None, start_row=0, end_row=None):
    """
    按行/列读取EXCEL数据
    file_path:文件路径（XLS格式文件）
    sheet_name：需要读取数据的sheet
    mode：取值方式（row:按行  column：按列）
    rows:按行读取数据时，起始行
    cols:按列读取数据时，起始列
    start_row、end_row：按列读取数据时，数据读取起止行
    start_col、end_col：按行读取数据时，数据读取起止列
    return:
        values：读取的值，根据mode传参，按行/列返回，返回数据格式为列表中嵌套元组
    """
    data_excel = xlrd.open_workbook(file_path)
    table = data_excel.sheet_by_name(sheet_name)
    values = []
    if mode == "row":
        for i in range(table.nrows):
            if i < rows:
                pass
            else:
                values.append(tuple(table.row_values(i, start_col, end_col)))
    elif mode == "column":
        for i in range(table.ncols):
            if i < cols:
                pass
            else:
                values.append(tuple(table.col_values(i, start_row, end_row)))
    else:
        logging.info("excel取值方式错误")
    return values

if __name__ == "__main__":
    print(read_excel(r"C:\Users\wenqiang.zhang5\PycharmProjects\untitled\UIPOMTest\project\POP\data\test_data.xls","测试用例数据"))
