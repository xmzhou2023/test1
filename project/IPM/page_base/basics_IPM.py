from public.base.basics import *
from libs.common.read_element import Element
from project.IPM.page_base.yamlbase import YamlRead
from libs.common.logger_ui import log
class PubicMethod(Base):
    def __init__(self, driver,element_yaml,expect=None,project='IPM'):
        super().__init__(driver)
        self.chome = Element( project=project, name=element_yaml)
        self.filelist = YamlRead(expect)

    # def find_element_IPM(self, locator, choice=None,choices=None):
    #     """寻找元素,并传入多个变量"""
    #     if choice is not None:
    #         Npath = []
    #         Npath.append(locator[0])
    #         Npath.append(locator[1])
    #         Npath[1] = Npath[1].replace('variable', choice)
    #         logging.info("查找元素：{}".format(Npath))
    #         if choices is not None:
    #             Npath[1] = Npath[1].replace('variabls', choices)
    #             logging.info("查找元素：{}".format(Npath))
    #         return Base.element_locator(lambda *args: self.wait.until(
    #             EC.presence_of_element_located(args)), Npath)
    #     else:
    #         logging.info("查找元素：{}".format(locator))
    #         return Base.element_locator(lambda *args: self.wait.until(
    #             EC.presence_of_element_located(args)), locator)

    def scroll_into_view_IPM(self, locator, choice1=None,choice2=None):
        """滑动至出现元素,并传入多个变量"""

        ele = self.find_element(locator, choice1, choice2)
        self.driver.execute_script("arguments[0].scrollIntoView()", ele)
        logging.info("滚动条至：{}".format(locator))


    def is_click_IPM(self, locator, choice=None, choices=None):
        """点击元素"""

        ele=self.find_element(locator, choice, choices)
        try:
            ele.click()
        except:
            self.driver.execute_script("arguments[0].click();", ele)
            sleep(0.5)
        logging.info("点击元素：{} {}".format(locator, choice))
        sleep(0.5)
    def mouse_hover_IPM(self,element,choice=None):
        '''鼠标悬停'''
        self.mouse_hover(self.chome[element], choice=choice)

    def element_exist_IPM(self,element,choice=None,choice1=None,choice2=None,choice3=None):
        """校验元素是否存在"""
        return  self.element_exist(self.chome[element],choice,choice1,choice2,choice3)

    def mouse_right_click_ipm(self,element,choice=None):
        '''鼠标右击'''
        return self.mouse_right_click(self.chome[element],choice)

    def find_element_IPM_yaml(self,element, choice=None, choices=None):
        return self.find_element(self.chome[element], choice=choice, choices=choices)

    def find_elemens_ipm_yaml_get_attribute(self,element, choice=None,get_attribute="innerText"):
        ele=self.find_elements(self.chome[element], choice=choice)
        elelist=[]
        for i in ele:
            res=i.get_attribute(get_attribute)
            elelist.append(res)
        return elelist

    def drag_and_drop_ipm(self,element,start_choice,end_choice):
        '''拖拽元素'''
        #这是鼠标需要进行的元素
        start_location = self.find_element(self.chome[element], choice=start_choice)
        #这是鼠标需要停留的元素
        end_location = self.find_element(self.chome[element], choice=end_choice)
        ActionChains(self.driver).drag_and_drop(start_location,end_location).perform()

    def refresh_webpage(self):
        logging.info("初始化浏览器")
        self.refresh()
        self.driver.switch_to.default_content()
        handles = self.driver.window_handles
        logging.info('当前窗口：{}'.format(handles))
        if len(handles) != 1:
            for i in range(1, len(handles)):
                self.close_switch(1)
        else:
            self.switch_window(0)
    def mouse_double_click_ipm(self,element,choice=None):
        '''双击'''
        return self.mouse_double_click(self.chome[element], choice=choice)

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
        sleep(0.5)

    def upload_file_ipm(self,elements,text,choice=None):
        self.upload_file(self.chome[elements],text,choice)


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