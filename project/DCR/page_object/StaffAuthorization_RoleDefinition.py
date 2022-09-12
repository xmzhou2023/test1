from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class RoleDefinitionPage(Base):
    """RoleDefinitionPage 定位元素类"""

    @allure.step("进入角色设置页面，根据Role角色筛选数据")
    def input_role_query(self, content):
        self.presence_sleep_dcr(user['Click Role'])
        self.is_click(user['Click Role'])
        self.input_text(user['Input Role'], txt=content)
        sleep(2)
        self.presence_sleep_dcr(user['Click Role value'])
        self.is_click(user['Click Role value'])

    @allure.step("进入角色设置页面，点击查询按钮")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(2.5)

    @allure.step("进入角色设置页面，筛选角色后，点击第一个复选框")
    def click_first_checkbox(self):
        self.presence_sleep_dcr(user['第一个复选框'])
        self.is_click(user['第一个复选框'])

    @allure.step("点击Permission Setting权限设置按钮")
    def click_permission_setting(self):
        self.is_click(user['Permission Setting'])
        sleep(3)

    @allure.step("点击 basic_data_management菜单复选框")
    def click_basic_data_mgt(self):
        self.is_click(user['Basic Data Management'])

    @allure.step("点击Save保存按钮 ")
    def click_save(self):
        self.is_click_dcr(user['Save'])
        sleep(1)

    @allure.step("获取Save Successfully保存成功提示语")
    def get_save_successfully(self):
        success = self.element_text(user['Get Save Successfully Text'])
        return success

    @allure.step("点击Confirm确认保存按钮 ")
    def click_confirm(self):
        self.is_click(user['Confirm'])
        sleep(1.5)

    @allure.step("获取Sales Region Management文本内容")
    def get_sale_region_mgt_text(self):
        text = self.element_text(user['Sales Region Management'])
        return text

    @allure.step("获取复选框对应的 Class属性是否包含is-checked")
    def click_check_basic_data_mgt(self):
        self.presence_sleep_dcr(user['Basic Data Management'])
        ss = self.find_element(user['Basic Data Management'])
        get_check_class = ss.get_attribute('class')
        if "is-checked" not in str(get_check_class):
            self.click_basic_data_mgt()
        else:
            self.click_basic_data_mgt()
            self.click_basic_data_mgt()

    @allure.step("关闭角色授权菜单")
    def click_close_role_definition(self):
        self.is_click(user['关闭角色授权菜单'])
        sleep(1)

if __name__ == '__main__':
    pass