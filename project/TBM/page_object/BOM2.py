import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class UserPage(Base):
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

    @allure.step("点击菜单")
    def click_menu(self, metatitle, nestmenu):
        self.is_click_tbm(user['一级菜单'], metatitle)
        logging.info(f'点击一级菜单：{metatitle}')
        self.is_click_tbm(user['二级菜单'], nestmenu)
        logging.info(f'点击二级菜单：{nestmenu}')
        sleep(1)
        self.refresh()

    @allure.step("点击新增")
    def click_add(self):
        self.is_click_tbm(user["新增"])
        sleep(2)

    @allure.step("Bom信息填写", )
    def click_Bom(self, message, select):
        if message == '机型':
            self.readonly_input_text(user['Bom信息填写'], select, message)
            self.is_click_tbm(user['Bom机型选择'], select)
            sleep()
        else:
            self.is_click_tbm(user['Bom信息填写'], message)
            self.is_click_tbm(user['Bom信息选择'], select)
            sleep()

    @allure.step("点击新增BOM")
    def click_add_bom(self):
        self.is_click_tbm(user["新增Bom"])
        self.is_click_tbm(user["新增Bom-编辑"])
        sleep(1)

    @allure.step("Bom Tree")
    def click_bom_tree(self, message, choice):
        dict1 = {'BOM状态': '2', '物料编码': '5', '用量': '8'}
        if message == '物料编码':
            self.readonly_input_text(user['新增Bom类型'], choice, dict1[message])
            self.is_click_tbm(user['新增Bom物料编码'], choice)
        elif message == '用量':
            self.readonly_input_text(user['新增Bom类型'], choice, dict1[message])
        else:
            self.is_click_tbm(user['新增Bom类型'], dict1[message])
            self.is_click_tbm(user['新增Bom信息'], choice)

    @allure.step("点击确定")
    def click_qd(self):
        self.is_click_tbm(user["新增Bom-确定"])
        sleep(1)


    @allure.step("审核人设置")
    def click_shr(self,message,member,number):
        self.is_click_tbm(user["审核人设置"],message)
        self.input_text(user["审核人设置-成员列表输入"],txt=member)
        self.is_click_tbm(user["审核人设置-工号"],number)
        self.is_click_tbm(user["审核人设置-确定"])
        sleep(1)

    @allure.step("点击提交")
    def click_submit(self):
        self.is_click_tbm(user["提交"])
        sleep(1)

    @allure.step("查询")
    def click_search(self):
        self.is_click_tbm(user['查询'])

    @allure.step("流程编码")
    def get_code(self, x):
        code = self.element_text(user['流程编码'], x)
        return code

    @allure.step("点击列表")
    def click_menu1(self, metatitle, nestmenu):
        self.is_click_tbm(user['待办列表'], metatitle)
        logging.info(f'点击待办列表：{metatitle}')
        self.is_click_tbm(user['我申请的'], nestmenu)
        logging.info(f'点击我申请的：{nestmenu}')
        sleep(1)
        self.refresh()
        self.frame_enter(user['iframe'])

    @allure.step("点击查看详情")
    def click_xq(self, code):
        self.is_click_tbm(user["查看详情"], code)
        self.switch_window(1)
        sleep(2)

    @allure.step("撤回")
    def click_ch(self):
        self.is_click_tbm(user["撤回"])
        self.is_click_tbm(user["撤回确定"])
        self.close_switch(1)
        sleep(1)

    @allure.step("删除")
    def click_delete(self, code):
        self.is_click_tbm(user['查询'])
        self.is_click_tbm(user['删除'], code)
        self.is_click_tbm(user['撤回确定'])
if __name__ == '__main__':
    pass
