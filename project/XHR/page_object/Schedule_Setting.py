import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ScheduleSetting(Base):
    """用户类"""

    @allure.step("查找工号")
    def search_user(self, jobnum=None,name=None):
        if jobnum is not None:
            self.readonly_input_text(user['用户管理-工号输入框'], txt=jobnum)
            sleep(2)
            self.is_click(user['用户管理-工号下拉列表'], jobnum)
        if name is not None:
            self.readonly_input_text(user['用户管理-姓名输入框'], txt=name)
            sleep(2)
            self.is_click(user['用户管理-姓名下拉列表'], name)
        self.is_click(user['用户管理-查询'])
        sleep()

    @allure.step("点击班次设置")
    def schedule_setting(self):
        self.refresh()
        self.hover(user['悬停xHR'])
        sleep(1)
        self.is_click(user['考勤管理'])
        self.is_click(user['班次设置'])

    @allure.step("点击新增")
    def click_add(self):
        self.is_click(user['新增'])

    @allure.step("输入班次名称")
    def input_name(self, name):
        self.input_text(user['班次名称'], name)

    @allure.step("选择适用公司")
    def click_selectcompany(self,companyname):
        self.is_click(user['适用公司'])
        self.is_click(user['公司架构树'])
        self.is_click(user['选择适用公司选项'],companyname)
        self.click_blank()

    @allure.step("点击空白处")
    def click_blank(self):
        self.is_click(user['点击_班次新增'])

    @allure.step("输入考勤开始时间")
    def input_atstime(self, type, starttime, endtime):
        self.input_text(user['开始时间'], starttime, type)
        self.input_text(user['结束时间'], endtime, type)
        self.is_click(user['点击_班次新增'])

    @allure.step("输入上班取卡提前时间")
    def input_ClockTime(self, type1, Earliest):
        dict1 = {'上班最早取卡时间提前':'startCard','下班最晚取卡时间延后':'endCard'}
        self.input_text(user['取卡时间'], Earliest, dict1[type1])

    @allure.step("确定")
    def click_sure(self):
        self.is_click(user['确定'])

    @allure.step
    def input_alltime(self):
        self.click_selectcompany('Transsion_SN(XD)')
        self.input_atstime('考勤时间', '09:00', '18:00')
        self.input_atstime('休息时间', '12:00', '13:00')
        self.input_ClockTime('上班最早取卡时间提前', '120')
        self.input_ClockTime('下班最晚取卡时间延后', '120')
        self.click_sure()

    @allure.step("查询")
    def click_searchitem(self):
        self.is_click(user['查询抽屉'])

    @allure.step("输入筛选条件")
    def input_condition(self, name):
        self.input_text(user['名称输入'], name)

    @allure.step("点击查询按钮")
    def click_searchbutton(self):
        self.is_click(user['查询按钮'])

    @allure.step("点击关闭按钮")
    def click_closebutton(self):
        self.is_click(user['关闭按钮'])

    @allure.step("删除筛选结果")
    def delete_banci(self,name):
        self.is_click(user['删除'],name)

    @allure.step("确认删除")
    def sure_del(self):
        self.is_click(user['二次确定按钮'])




if __name__ == '__main__':
    pass
