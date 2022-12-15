from public.base.basics import *
from libs.common.read_element import Element
from project.IPM.page_object.yamlbase import YamlRead

class PubicMethod(Base):
    def __init__(self, driver,element_yaml,expect=None,project='IPM'):
        super().__init__(driver)
        self.chome = Element( project=project, name=element_yaml)
        self.filelist = YamlRead(expect)

    def find_element_IPM(self, locator, choice=None,choices=None):
        """寻找元素,并传入多个变量"""
        if choice is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice)
            logging.info("查找元素：{}".format(Npath))
            if choices is not None:
                Npath[1] = Npath[1].replace('variabls', choices)
                logging.info("查找元素：{}".format(Npath))
            return Base.element_locator(lambda *args: self.wait.until(
                EC.presence_of_element_located(args)), Npath)
        else:
            logging.info("查找元素：{}".format(locator))
            return Base.element_locator(lambda *args: self.wait.until(
                EC.presence_of_element_located(args)), locator)

    def scroll_into_view_IPM(self, locator, choice1=None,choice2=None):
        """滑动至出现元素,并传入多个变量"""
        if choice1 is not None:
            Npath = []
            Npath.append(locator[0])
            Npath.append(locator[1])
            Npath[1] = Npath[1].replace('variable', choice1)
            ele = self.find_element(Npath)
            if choice2 is not None:
                Npath[1] = Npath[1].replace('variabls', choice2)
                ele = self.find_element(Npath)
            self.driver.execute_script("arguments[0].scrollIntoView()", ele)
            logging.info("滚动条至：{}".format(Npath))
        else:
            ele = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView()", ele)
            logging.info("滚动条至：{}".format(locator))


    def is_click_IPM(self, locator, choice=None, choices=None):
        """点击元素"""

        ele=self.find_element_IPM(locator, choice, choices)
        try:
            ele.click()
        except:
            self.driver.execute_script("arguments[0].click();", ele)
            sleep(0.5)
        logging.info("点击元素：{}".format(locator))
        sleep(0.5)


    def click_IPM(self, element, choice=None, choices=None):
        """
        点击元素
        """
        try:
            self.is_click_IPM(self.chome[element], choice=choice, choices=choices)
        except:
            self.scroll_into_view_IPM(self.chome[element], choice1=choice, choice2=choices)
            self.is_click_IPM(self.chome[element], choice=choice, choices=choices)
        sleep(0.5)

    def input_text_IPM(self,elements='currency',text=None,choice=None):
        """
        找到文本框输入文本
        :param elements: 找到文本输入框
        :param text: 输入文本
        :param choice: 传入元素variable
        """
        try:
            self.input_text(locator=self.chome[elements], txt=text, choice=choice)
        except:
            self.scroll_into_view(locator=self.chome[elements],choice=choice)
            self.input_text(locator=self.chome[elements], txt=text,choice=choice)
