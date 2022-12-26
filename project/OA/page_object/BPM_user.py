import time
import json
import requests
from libs.common.read_element import Element
from project.OA.page_object.OA_login import OAdnluPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from public.libs.unified_login.login import Login
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class BPM_user_Page(Base):
    """
    BPM用户端操作界面
    """

    @allure.step("判断一及导航的个人中心目录是否成功")
    def ismodeling_Log(self):
        itexis = self.element_exist(user["一级导航"], "个人中心")
        return itexis

    @allure.step("点击流程中心下的【一级导航】按钮")
    def click_one(self, variables):
        self.is_click_tbm(user['一级导航'], variables)

    @allure.step("点击流程中心下的【二级导航】按钮")
    def click_two(self, variables):
        self.is_click_tbm(user['二级导航'], variables)

    @allure.step("新建流程下_搜索输入框输入查询内容")
    def input_enter(self, content):
        self.input_text(user['流程概览的搜索输入框'], txt=content)

    @allure.step("新建流程下_点击搜索输入框后面查询按钮")
    def click_Inquire(self):
        self.is_click_tbm(user['流程概览的搜索按钮'])

    @allure.step("新建流程下_查询后点击第一条流程")
    def click_tick(self):
        self.is_click_tbm(user['查询出来的第一条数据'])

    @allure.step("判断流程列表字段存在的值")
    def ismodeling_release(self):
        itexisA = self.element_exist(user["流程字段"], "字段一")
        itexisB = self.element_exist(user["流程字段"], "字段二")
        itexisC = self.element_exist(user["流程字段"], "字段三")
        itexisD = self.element_exist(user["流程字段"], "你好哦")
        itexisE = self.element_exist(user["流程字段"], "附件字段")
        itexisF = self.element_exist(user["流程字段"], "吃饭了吗")
        if itexisA and itexisB and itexisC and itexisD and itexisE and itexisF:
            return True
        else:
            return False

    @allure.step("点击流程启动_审批表单下_底部的流程处理按钮")
    def click_button(self, variables):
        self.is_click_tbm(user['流程启动_审批表单下底部的流程处理按钮'], variables)

    @allure.step("判断流程提交是否成功")
    def ismodeling_submit(self):
        itexis = self.element_exist(user["提交流程成功提示"])
        return itexis

    @allure.step("获取提交成功后流程的流程编号")
    def get_Numbering(self):
        text = self.get_element_attribute(user["流程编号"], attribute="textContent")
        return text

    @allure.step("当前用户退出登录")
    def click_quit(self):
        self.is_click_tbm(user['右上角登录名'])
        self.is_click_tbm(user['右上角弹出菜单栏'], "退出登录")
        self.is_click_tbm(user['退出系统提示_确定_取消按钮'])

    @allure.step("点击我的待办导航")
    def click_Upcoming(self):
        self.is_click_tbm(user['我的待办导航'])

    @allure.step("我的待办下界面下，输入流程编号进行搜索查询，点击进入流程详情界面")
    def input_click_process(self, content):
        self.input_text(user['我的待办_搜索输入框'], txt=content)
        self.is_click_tbm(user['我的待办_搜索查询按钮'])
        self.is_click_tbm(user['待办列表第一条标题'])

    @allure.step("流程审批同意弹窗下的_审批意见。输入审批意见")
    def input_Opinion(self, content):
        self.input_text(user['审批同意_输入框'], content)

    @allure.step("点击流程审批同意弹窗下的_确定/取消按钮")
    def click_yes_no(self, variables):
        self.is_click_tbm(user['审批同意_确定_取消_按钮'], variables)

    @allure.step("判断审批流程，同意审批提交是否成功")
    def ismodeling_consent_process(self):
        itexis = self.element_exist(user["同意流程成功提示"])
        return itexis

    @allure.step("点击我的已办导航")
    def click_done(self):
        self.is_click_tbm(user['我的已办导航'])

    @allure.step("我的已办下界面下，输入流程编号进行搜索查询，点击标题进入流程详情界面")
    def input_click_done(self, content):
        self.input_text(user['我的已办_搜索输入框'], txt=content)
        self.is_click_tbm(user['我的已办_搜索查询按钮'])
        self.is_click_tbm(user['已办列表第一条标题'])
        # self.is_click_tbm(user['已办列表第一条标题'])

    @allure.step("判断流程的最终状态是不是已归档状态")
    def ismodeling_state(self):
        itexis = self.element_exist(user["已归档状态"])
        return itexis

    #
    # @allure.step("PC表单设计_点击方框一行名称文")
    # def click_name(self):
    #     self.is_click_tbm(user['PC表单_选择方框一行名称文'])
    #
    # @allure.step("PC表单设计_发布按钮")
    # def click_release(self):
    #     self.is_click_tbm(user['PC表单设计_发布'])
    #
