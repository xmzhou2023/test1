import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class PayrollConfigure(Base):
    """用户类"""

    @allure.step("点击菜单")
    def click_menus(self, metatitle,nestmenu):
        self.refresh()
        self.hover(user['XHR'])
        self.is_click(user['一级菜单'],metatitle)
        logging.info(f'点击一级菜单：{metatitle}')
        self.is_click(user['二级菜单'], nestmenu)
        logging.info(f'点击二级菜单：{nestmenu}')
        sleep(1)
        self.refresh()

    @allure.step("进入集团方案")
    def click_slalary_setting(self,salaryset):
        self.is_click(user['薪酬配置选项'],salaryset)
        sleep(1)

    @allure.step("点击新增")
    def click_add(self):
        self.is_click(user['集团方案新增'])
        DomAssert(self.driver).assert_att('新增集团方案')

    @allure.step("集团方案编码")
    def input_code(self,info):
        self.input_text(user['集团方案编码'],info)

    @allure.step("集团方案名称")
    def input_name(self, info):
        self.input_text(user['集团方案名称'], info)

    @allure.step("生效日期")
    def input_efftivedate(self,txt):
        self.readonly_input_text(user['生效日期'],txt)
        self.is_click(user['label'])
        #self.is_click(user['生效日期'])
        #self.is_click(user['日期'])

    @allure.step("状态")
    def input_status(self,type):
        self.is_click(user['状态'])
        self.is_click(user['状态选择'],type)


    @allure.step("确定或取消方案")
    def click_sure(self, type):
        self.is_click(user['确定或取消'],type)
        # DomAssert(self.driver).assert_att('编码已存在')

if __name__ == '__main__':
    pass
