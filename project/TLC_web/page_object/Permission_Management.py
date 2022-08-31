import allure
from public.base.basics import Base
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import logging
from project.TLC_web.test_case.conftest import *
pro_env = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, pro_env)
class Permission(Base):
    """权限管理"""

    @allure.step("点击权限管理页面")
    def click_roletab(self):
        self.is_click(user['权限管理页面点击'])
        logging.info("定位在权限管理页面")
        sleep(1)
# 新增角色
    @allure.step("点击添加角色按钮")
    def add_role(self):
        self.is_click(user['添加角色图标'])
        logging.info("打开新增角色弹窗")
        sleep(1)

    @allure.step("新增角色弹框 输入角色名称")
    def input_rolename(self, input_rolename=None):
        self.readonly_input_text(user['角色输入框'], input_rolename)
        sleep(1)


    @allure.step("新增弹窗 新增保存")
    def save_button(self, t):
        self.is_click(user['角色添加按钮'])
        if t == "角色新增反例":
            a = self.element_text(user['角色名称必填项'])
            if a == '角色名不能为空':
                self.is_click(user['新增角色弹框关闭'])
                logging.info("角色名称为必填项,新增失败")
        else:
            # TODO
            ...

    @allure.step("关闭新建弹窗")
    def close_button(self):
        self.is_click(user['新增角色弹框关闭'])
        logging.info("新增角色弹框关闭")
        sleep(2)

    @allure.step("取消角色新增")
    def cancel_button(self):
        self.is_click(user['角色取消按钮'])
        logging.info("取消新增操作")
        sleep(2)


if __name__ == '__main__':
        pass

