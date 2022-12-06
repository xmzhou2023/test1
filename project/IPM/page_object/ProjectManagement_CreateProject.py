'''创建项目'''

from project.IPM.page_base.basics_IPM import PubicMethod
from libs.common.time_ui import *
from project.IPM.page_base.assert_pubic import *
now_times = strftime('%Y-%m-%d%H:%M:%S')
now_t = strftime('%Y-%m-%d')
time_ipm=f'ipm自动化{now_times}'
class CreateProject(PubicMethod):

    def __init__(self,driver,element_yaml='ProjectManagement_CreateProject',expect='ProjectManagement_CreateProject.yaml'):
        super().__init__(driver, element_yaml,expect=expect)

    def get_url_project(self):
        self.get_url("http://ipm-uat.transsion.com/#/project-manage")
        sleep(2)
    def click_project(self):
        '''
        点击项目管理
        '''
        self.click_IPM('项目管理')
        sleep(2)

    def click_add(self):
        '''点击新增'''
        self.click_IPM('新增')
        sleep(2)

    def Select_Template(self,choice):
        '''
        选择模板
        :param choice：模板名字（IT项目模板，IT需求项目模板等）
        '''
        self.click_IPM('选择模板',choice=choice)
        sleep(2)

    def projecy_name(self,nametext):
        '''项目名字'''
        self.input_text_IPM('项目名称',nametext)
        sleep(2)

    def projecy_Description(self,Descriptiontext=None):
        '''项目描述'''
        self.input_text_IPM('项目描述',text=Descriptiontext)
        sleep(2)

    def projecy_preservation(self):
        '''保存'''
        self.click_IPM('保存')


    def projecy_cancel(self):
        '''取消'''
        self.click_IPM('取消')

    def click_project_entrance(self,projectname):
        '''进入项目'''
        self.click_IPM('进入项目',projectname)

    def click_edit(self):
        '''编辑'''
        self.click_IPM('编辑')


    def element_get_attribute(self,element_name):
        ele_text=self.form_element_ipm(element_name)
        return ele_text.get_attribute('innerText')

    def Create_project(self, Save_or_Cancel, templatename=None, nametext=None, Descriptiontext=None):
        """
        创建项目
        :param templatename: 选择对应的项目模板名字
        :param nametext: 项目名称
        :param Descriptiontext: 项目描述
        :param Save_or_Cancel: 保存还是取消
        """

        self.click_project()
        self.click_add()
        if templatename != None:
            self.Select_Template(templatename)
        if nametext != None:
            self.projecy_name(nametext)
        if Descriptiontext != None:
            self.projecy_Description(Descriptiontext)
        if Save_or_Cancel == '保存':
            self.projecy_preservation()
        else:
            self.projecy_cancel()

    def project_entrance(self,projectname):
        self.click_project_entrance(projectname)
        self.click_edit()



#断言
class Assert_result(AssertMode):
    def __init__(self,driver,element_yaml='ProjectManagement_CreateProject', expect='ProjectManagement_CreateProject.yaml'):
        super().__init__(driver, element_yaml,expect=expect)

    def assert_Create_project(self,actual,Expected):
        self.assert_element_equal(actual,Expected)


    @allure.step("断言")
    def assert_toast(self, content=None):
        # att = self.element_text(user['toast提示'])
        try:
            att = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, "//div[@role='alert']/p"))).text
            self.base_get_img()
            logging.info('获取toast提示语：{}'.format(att))
            try:
                if content is None:
                    assert '请求成功' in att or '审核通过' in att or '操作成功' in att or '处理成功' in att
                    logging.info('断言成功，toast提示为：{}'.format(att))
                else:
                    assert content in att
                    logging.info('断言成功，toast提示为：{}'.format(att))
            except:
                logging.error('断言失败，实际提示为：{}'.format(att))
                raise
        except:
            logging.error('断言失败，未获取到toast提示语/toast提示语错误')
            raise


    @allure.step("断言")
    def assert_toast_not(self, content=None):
        # att = self.element_text(user['toast提示'])
        try:
            att = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/main/section/div[1]/section/div[1]/div/div[1]/div[1]'))).text
            self.base_get_img()
            logging.info('获取toast提示语：{}'.format(att))
            try:
                if content is None:
                    assert '请求成功' not in att or '审核通过' not in att or '操作成功' not in att or '处理成功' not in att
                    logging.info('断言成功，toast提示为：{}'.format(att))
                else:
                    assert content not in att
                    logging.info('断言成功，toast提示为：{}'.format(att))
            except:
                logging.error('断言失败，实际提示为：{}'.format(att))
                raise
        except:
            logging.error('断言失败，未获取到toast提示语/toast提示语错误')
            raise
