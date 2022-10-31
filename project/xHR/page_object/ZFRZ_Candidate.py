import random

import allure, os
import time
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class Candidate(Base):
    """用户类"""
    @allure.step("查找工号")
    def search_user(self, jobnum=None, name=None):
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

    @allure.step("点击菜单")
    def click_menu(self):
        self.refresh()
        self.is_click(user['xHr'])
        self.is_click(user['中方入职'])
        self.is_click(user['候选人'])

    @allure.step("点击筛选按钮")
    def click_ShaiX(self):
        self.is_click(user['点击筛选按钮'])

    @allure.step("查询数据")
    def input_selectOK(self, type2, txt):
        self.input_text(user['筛选输入筛选文本'], txt, type2)

    @allure.step("点击查询按钮")
    def click_ChaXButton(self):
        self.is_click(user['输入值后点击查询'])

    @allure.step("点击新增候选人按钮")
    def click_NewCandidate(self):
        self.is_click_tbm(user['新增候选人按钮'])

    @allure.step("新增候选人")
    def input_Parameter(self, type1, txt):
        input_type = ['姓名', '出生年份', '电话', '邮箱', '毕业院校', '英文名字']
        select_type = ['国籍', '学历', '招聘渠道']
        HR_type = ['对接HR']
        click_type = ['性别']
        if type1 in input_type:
            self.input_text(user['文本框输入'], txt, type1)
            logging.info('{}输入框输入：{}'.format(type1, txt))
            self.is_click(user['出生年份点击空白'])
        elif type1 in select_type:
            # self.is_click(user['选择下拉框'], type1)
            self.readonly_input_text(user['输入下拉框值'], txt, type1)
            self.is_click(user['选择下拉框值'], txt, type1)
        elif type1 in HR_type:
            self.is_click(user['文本框输入'], type1)
            self.input_text(user['输入对接HR姓名'], txt, type1)
            self.is_click(user['选择人'], type1)
            self.is_click(user['选择HR后点击确定'], type1)
        elif type1 in click_type:
            self.is_click(user['性别'], type1)

    @allure.step("保存候选人")
    def click_SaveCandidate(self):
        self.is_click(user['保存候选人按钮'])

    @allure.step("点击删除")
    def click_DeleteHouxuanren(self, name):
        self.is_click_tbm(user['点击删除'], name)
        self.is_click_tbm(user['确定删除'])

    def Delete_after_data(self):
        phone = self.get_mobile()
        self.click_NewCandidate()
        self.input_Parameter('姓名', '可可子2')
        self.input_Parameter('出生年份', '2000')
        self.input_Parameter('性别', '女')
        self.input_Parameter('电话', phone)
        self.input_Parameter('国籍', '中国')
        self.input_Parameter('邮箱', '1598043326@qq.com')
        self.input_Parameter('毕业院校', '深圳大学')
        self.input_Parameter('对接HR', '李菁豆')
        self.input_Parameter('学历', 'high school高中')
        self.input_Parameter('英文名字', 'Bean')
        self.input_Parameter('招聘渠道', '前程无忧')
        self.click_SaveCandidate()  # 保存按钮
        DomAssert(self.driver).assert_att('新增成功')

    def get_mobile(self):
        mobiles = ['130', '131', '132', '133', '134']
        number = str(int(time.time()))[2:]
        mobile = random.choice(mobiles)+number
        return mobile

    def assert_search(self, header, content):
        DomAssert(self.driver).assert_search_result(user['表格字段'], user['表格内容'], header, content)


if __name__ == '__main__':
    pass
