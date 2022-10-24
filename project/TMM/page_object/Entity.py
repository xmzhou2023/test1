import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class EntityPage(Base):
    """实体"""



    @allure.step("进入实体页面")
    def GotoEntity(self):
        self.is_click(user['业务配置'])
        Entity = self.find_element(user['实体模块']).text
        self.is_click(user['实体模块'])
        self.is_click(user['实体查询按钮'])
        sleep(1)
        return Entity



    @allure.step("实体名称查询")
    def EntityQuery(self, entity_name):
        self.input_text(user['实体名称输入框'], entity_name)
        self.is_click(user['实体查询按钮'])
        sleep(1)


    @allure.step("实体名称重置")
    def EntityReset(self):
        self.is_click(user['实体重置按钮'])
        sleep(1)


    @allure.step("新增实体")
    def AddEntity(self, entity_name, entity_describe):
        entity = self.element_exist(user['实体'], entity_name)
        while entity:
            entity_name = entity_name + '1'
            entity = self.element_exist(user['实体'], entity_name)
        self.is_click(user['实体新增按钮'])
        AddEntity = self.find_element(user['新增页面保存按钮']).text
        self.input_text(user['新增页面实体名称输入框'], entity_name)
        self.input_text(user['新增页面实体描述输入框'], entity_describe)
        self.is_click(user['新增页面保存按钮'])
        sleep(1)
        return AddEntity



    @allure.step("编辑实体")
    def EditEntity(self, entity_name, entity_describe):
        entity = self.element_exist(user['实体'], entity_name)
        while entity:
            entity_name = entity_name + '1'
            entity = self.element_exist(user['实体'], entity_name)
        self.is_click(user['实体编辑按钮'])
        sleep(1)
        EditEntityName = self.find_element(user['编辑页面实体名称title']).text
        self.input_text(user['编辑页面实体名称输入框'], entity_name)
        self.input_text(user['编辑页面实体描述输入框'], entity_describe)
        self.is_click(user['编辑页面保存按钮'])
        sleep(1)
        return EditEntityName


    @allure.step("查看实体")
    def ViewEntity(self):
        self.is_click(user['实体查看按钮'])
        ViewEntity = self.find_element(user['查看实体页面返回按钮']).text
        self.is_click(user['查看实体页面返回按钮'])
        sleep(1)
        return ViewEntity

    # def ViewPageText(self):


if __name__ == '__main__':
    pass
