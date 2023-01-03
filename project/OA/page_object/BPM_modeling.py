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


class BPM_modeling_Page(Base):

    @allure.step("点击导航首页一级")
    def click_level_one(self, variables):
        self.is_click_tbm(user['导航首页一级'], variables)

    @allure.step("点击导航首页二级")
    def click_level_two(self, variables):
        self.is_click_tbm(user['导航首页二级'], variables)

    @allure.step("导航首页三级")
    def click_level_three(self, variables):
        self.is_click_tbm(user['导航首页三级'], variables)

    @allure.step("点击：添加_设置分类_删除 按钮")
    def click_buttons(self, variables):
        self.is_click_tbm(user['添加_设置分类_删除按钮'], variables)

    @allure.step("输入业务建模下的模型描述输入框输入文字")
    def input_modeling_name(self, content):
        self.input_text(user['模型描述输入框'], txt=content)

    @allure.step("点击添加实体按钮")
    def click_physical_button(self):
        self.is_click_tbm(user['添加实体按钮'])

    @allure.step("输入主实体描述输入框输入文字")
    def input_master_entity(self, content):
        self.input_text(user['主实体描述输入框'], txt=content)

    # @allure.step("点击6次添加字段按钮")
    # def click_from_button(self):
    #     self.is_click_tbm(user['添加字段按钮'])
    #     self.is_click_tbm(user['添加字段按钮'])
    #     self.is_click_tbm(user['添加字段按钮'])
    #     self.is_click_tbm(user['添加字段按钮'])
    #     self.is_click_tbm(user['添加字段按钮'])
    #     self.is_click_tbm(user['添加字段按钮'])

    @allure.step("添加字段，连续输入1，2，3，4，5，6的主实体注释字段")
    def input_note(self):
        self.is_click_tbm(user['添加字段按钮'])
        self.input_text(user['字段列表1行注释'], txt="字段一")
        self.input_text(user['字段列表1行名称'], txt="zdy")
        self.is_click_tbm(user['添加字段按钮'])
        self.input_text(user['字段列表2行注释'], txt="字段二")
        self.input_text(user['字段列表2行名称'], txt="zder")
        self.is_click_tbm(user['添加字段按钮'])
        self.input_text(user['字段列表3行注释'], txt="字段三")
        self.input_text(user['字段列表3行名称'], txt="zdsan")
        self.is_click_tbm(user['添加字段按钮'])
        self.input_text(user['字段列表4行注释'], txt="你好哦")
        self.input_text(user['字段列表4行名称'], txt="inhao")
        self.is_click_tbm(user['添加字段按钮'])
        self.input_text(user['字段列表5行注释'], txt="附件字段")
        self.input_text(user['字段列表5行名称'], txt="ziduanwu")
        self.is_click_tbm(user['添加字段按钮'])
        self.input_text(user['字段列表6行注释'], txt="吃饭了吗")
        self.input_text(user['字段列表6行名称'], txt="ziduanliu")

    @allure.step("建模下点击业务建模_保存按钮")
    def click_save(self):
        self.is_click_tbm(user['业务建模_保存'])

    @allure.step("判断业务建模保存是否成功")
    def ismodeling_success(self):
        itexis = self.element_exist(user["业务建模_保存成功弹窗提示语"])
        return itexis

    @allure.step("数据建模下的搜索框进行搜索")
    def input_modelingA(self, content):
        self.input_text(user['输入别名搜索输入框'], txt=content)

    @allure.step("数据建模下的搜索框进行搜索__点击搜索按钮_点击选择方框一行描述进入详情界面")
    def click_modeling_search(self):
        self.is_click_tbm(user['别名搜索按钮'])
        sleep(5)
        self.is_click_tbm(user['选择方框一行描述文'])

    @allure.step("建模下点击业务建模_发布按钮")
    def click_release(self):
        self.is_click_tbm(user['业务建模_发布'])

    @allure.step("判断业务建模发布是否成功")
    def ismodeling_srelease(self):
        itexis = self.element_exist(user["业务建模_发布_创建表单成功弹窗提示语"])
        return itexis

    @allure.step("判断BPM是否登录成功，设计中心导航界面是否存在")
    def ismodeling_login(self):
        sleep(3)
        itexis = self.element_exist(user['导航首页一级'], "设计中心")
        return itexis




