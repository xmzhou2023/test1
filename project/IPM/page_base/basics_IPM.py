from public.base.basics import *
from libs.common.read_element import Element
from project.IPM.page_object.yamlbase import YamlRead
from libs.common.logger_ui import log
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


    def form_elements(self,formheader,choice=None,get_attributs='innerText'):
        """
        读取表头字段
        :param formheader: 获取多个字段的值
        :param choice: 传入元素variable
        :param get_attributs: 获取innerText/value
        """
        form = self.find_elements(self.chome[formheader],choice=choice)
        formlist = []
        for i in form:
            if i.get_attribute('innerText') == '序号' or i.get_attribute('innerText') == '操作' or i.get_attribute('innerText') == '\u3000':
                pass
            else:
                formlist.append(i.get_attribute(get_attributs))
                log.info(f'获取表单字段{formlist}')
        return formlist
    def split_lines(self,s):
        """
        字段读取特殊处理
        :param s:
        """
        return s.split('\n')

    def elements_detail_special(self,formheader,choice=None,get_attributs='innerText'):
        """
        读取元素的内容存储在字典中
        :param formheader: 获取单个字段的值
        :param choice: 传入元素variable
        :param get_attributs: 获取innerText/value
        """
        try:
            form = self.find_elements(self.chome[formheader],choice=choice)
            filelistw = []
            for i in form:
                filelistw.append(i.get_attribute(get_attributs).replace(' ', ''))
            lis = ''.join(filelistw)
            form_list = self.split_lines(lis)
            lists=list(filter(None,form_list))
            log.info(f'获取表单字段{lists}')
            return lists
        except Exception as e:
            log.info(f'找不到{formheader}元素信息,{e}')
            raise e