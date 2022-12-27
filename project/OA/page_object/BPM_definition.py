import time
import json
import requests
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from public.libs.unified_login.login import Login
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class BPM_definition_Page(Base):
    """
        流程定义界面操作
      """

    @allure.step("点击流程定义下的【新增_导入_导出】按钮")
    def click_add(self, variables):
        self.is_click_tbm(user['新增_导入_导出按钮'], variables)

    @allure.step("进入流程设计界面，点击分类放大镜按钮")
    def click_Classification(self):
        self.is_click_tbm(user['分类放大镜按钮'])

    @allure.step("进入流程设计界面，点击分类_进行选择分类 ")
    def click_Category_selection(self, variables):
        self.is_click_tbm(user['分类_选择分类'], variables)

    @allure.step("进入流程设计界面，进入分类选择界面后点击确定按钮")
    def click_confirm(self):
        self.is_click_tbm(user['分类_确定'])

    @allure.step("流程设计界面下，流程名称输入框输入内容")
    def input_enter(self, content):
        self.input_text(user['流程名称输入框'], txt=content)

    @allure.step("流程设计界面下,点击第一个用户任务")
    def click_userA(self):
        element = self.find_elements(user['用户任务多个通过s取下标'])
        element[0].click()

    @allure.step("流程设计界面下,双击第二个用户任务")
    def click_userB(self):
        element = self.find_elements(user['用户任务多个通过s取下标'])
        actions = ActionChains(self.driver)
        actions.double_click(element[1]).perform()

    @allure.step("进入流程设计界面，添加一个新的用户任务事件")
    def click_Add_user(self):
        self.is_click_tbm(user['用户任务'])

    @allure.step("进入流程设计界面，追加结束事件")
    def click_Finish(self):
        self.is_click_tbm(user['追加结束事件'])

    @allure.step("流程设计界面下，修改流程配置_第二个用户任务的文本")
    def input_userenter(self, content):
        self.input_text(user['流程配置_第二个用户任务的文本'], txt=content)

    @allure.step("进入流程设计界面，点击保存按钮")
    def click_save(self):
        self.is_click_tbm(user['保存按钮'])

    @allure.step("判断流程设计保存是否成功")
    def ismodeling_save(self):
        itexis = self.element_exist(user["保存成功提示语"])
        return itexis

    @allure.step("进入流程设计界面，点击发布按钮")
    def click_release(self):
        self.is_click_tbm(user['发布按钮'])

    @allure.step("判断流程设计发布是否成功")
    def ismodeling_release(self):
        itexis = self.element_exist(user["发布成功提示语"])
        return itexis

    @allure.step("流程定义界面，输入框输入文字查询")
    def input_name(self, content):
        self.input_text(user['流程搜索输入框'], txt=content)

    @allure.step("流程定义界面，点击流程搜索放大镜按钮")
    def click_search(self):
        self.is_click_tbm(user['流程搜索放大镜'])

    @allure.step("流程定义界面，点击列表第一行名称,跳到详情界面")
    def click_name(self):
        self.is_click_tbm(user['列表第一行名称'])

    def move_houseA(self, drivers, x, y):
        """点击空白区域，用于取消释法,参数driver对象，x轴坐标，y轴坐标"""
        ActionChains(drivers).move_by_offset(x, y).click().perform()

    @allure.step("流程编辑界面，点击目录_流程配置")
    def click_Table(self):
        self.is_click_tbm(user['目录_流程配置'])

    @allure.step("给02节点的用户任务1指定节点审批人员“刘艳")
    def click_input_big(self, content):
        self.is_click_tbm(user['流程配置_第二个用户任务的文本B'])
        self.is_click_tbm(user['流程配置_节点审批人员'])
        self.is_click_tbm(user['节点审批人员_新增按钮'])
        self.is_click_tbm(user['用户来自_选择'])
        self.is_click_tbm(user['用户选择_指定用户_圈圈'])
        self.is_click_tbm(user['用户选择_指定用户_选择框'])
        self.input_text(user['选择用户_输入框'], txt=content)
        sleep(2)
        self.is_click_tbm(user['选择用户_放大镜'])
        sleep(3)
        self.is_click_tbm(user['用户列表第一列'])
        self.is_click_tbm(user['选择用户3_确定'])
        self.is_click_tbm(user['用户选择2_确定'])
        self.is_click_tbm(user['用户任务节点人员设置_确定'])

    @allure.step("判断流程编辑，02节点用户任务1有没有成功指定上用户")
    def ismodeling_user(self):
        itexis = self.element_exist(user["流程配置_新增节点人员记录刘艳"])
        return itexis

    @allure.step("流程编辑界面，点击保存配置按钮")
    def click_configuration(self):
        self.is_click_tbm(user['保存配置按钮'])

    @allure.step("判断流程编辑界面，点击保存配置按钮保存成功")
    def ismodeling_configuration(self):
        itexis = self.element_exist(user["保存配置功提示语"])
        return itexis

    @allure.step("流程编辑界面，点击目录_流程设计")
    def click_Design(self):
        self.is_click_tbm(user['目录_流程设计'])

    @allure.step("流程编辑界面，点击流程配置下的_全局设置")
    def click_global(self):
        self.is_click_tbm(user['流程配置_全局设置'])

    @allure.step("流程编辑界面，点击流程配置下的_全局表单_PC端放大镜")
    def click_PC(self):
        self.is_click_tbm(user['全局表单_PC端放大镜'])

    @allure.step("全局表单PC端添加表单")
    def click_input_globalA(self, content):
        self.input_text(user['选择表单_搜索输入框'], txt=content)
        self.is_click_tbm(user['选择表单_查询'])
        self.is_click_tbm(user['选择表单_第一行选项'])
        self.is_click_tbm(user['选择表单_确定'])

    @allure.step("全局表单PC端添加表单")
    def click_input_globalB(self, content):
        element = self.find_elements(user['选择表单_搜索输入框'])
        element[1].clear()
        element[1].send_keys(content)
        logging.info("输入文本：{}".format(content))
        elementB = self.find_elements(user['选择表单_查询'])
        elementB[1].click()
        elementC = self.find_elements(user['选择表单_第一行选项B'])
        elementC[len(elementC) - 1].click()
        self.is_click_tbm(user['选择表单_确定'])

    @allure.step("流程编辑界面，点击流程配置下的_实例表单_PC端放大镜")
    def click_SLPC(self):
        self.is_click_tbm(user['实例表单_PC端放大镜'])

    @allure.step("判断流程编辑，全局设置有没有成功绑定【机器人数据建模】开头的表单")
    def ismodeling_form(self):
        itexis = self.element_exist(user["全局表单绑定表单"])
        return itexis
