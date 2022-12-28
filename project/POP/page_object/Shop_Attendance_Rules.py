import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *
from project.POP.page_object.Center_Component import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AddAttendanceRule(Base):
    """考勤规则类"""

    @allure.step("点击新增")
    def click_add(self):
        self.is_click_tbm(user['新增按钮'])

    @allure.step("输入考勤信息")
    def attendance_information(self,division,country,role,month,remarks,worktime1,closingtime1):
        # 选择组织
        self.is_click_tbm(user['组织选择框'])
        self.input_text(user['组织选择框'],division)
        self.is_click_tbm(user['组织'],division)
        # 选择国家
        self.is_click_tbm(user['国家选择框'])
        self.input_text(user['国家选择框'],country)
        self.is_click_tbm(user['国家'],country)
        # 选择角色
        self.is_click_tbm(user['角色选择框'])
        self.input_text(user['角色选择框'],role)
        self.is_click_tbm(user['角色'],role)
        # 选择月份
        self.is_click_tbm(user['月份选择框'])
        self.is_click_tbm(user['月份'],month)
        # 输入备注
        self.input_text(user['备注'],remarks)
        # 选择上班时间
        self.input_text(user['上班时间1'],worktime1)
        # 选择下班时间
        self.input_text(user['下班时间1'],closingtime1)

    @allure.step("点击确定")
    def click_sure(self):
        self.is_click_tbm(user['确定按钮'])

class Queryattdendancerule(Page_Operation,General_button):
    """查询考勤规则类"""
    select_list = {"考勤规则-组织框":"考勤规则-组织","考勤规则-国家框":"考勤规则-国家","考勤规则-开始月份框":"考勤规则-开始月份"}

    def queryattendancerule(self,select,content,content1=None):
        if select in self.select_list:
            self.frame_enter(user['iframe弹窗'])
            self.single_condition_input_boxquery(select, self.select_list[select], content)
            sleep()
            self.query()
        else:
            logging.error("系统检测没有此筛选项，请检查后重新输入")

if __name__ == '__main__':
    pass
