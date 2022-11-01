import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AssessmentType(Base):
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

    @allure.step("点击测评类型")
    def assess_type(self):
        self.refresh()
        self.hover_click(user['悬停xHR'])
        sleep(1)
        self.is_click_tbm(user['测评中心'])
        self.is_click_tbm(user['测评类型'])

    @allure.step("筛选")
    def assess_search(self):
        self.is_click(user['筛选按钮'])

    @allure.step("输入筛选条件")
    def assess_inputinfo(self,name):
        self.input_text(user['测评类型筛选项'], name)

    @allure.step("点击查询按钮")
    def click_searchbutton(self):
        self.is_click_tbm(user['查询按钮'])
        self.is_click_tbm(user['关闭按钮'])



    @allure.step("断言查询结果")
    def assert_search(self, header, content):
        DomAssert(self.driver).assert_search_result(user['表格字段'], user['表格内容'], header, content)




if __name__ == '__main__':
    pass
