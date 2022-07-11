from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class RoleDefinitionPage(Base):
    """RoleDefinitionPage 定位元素类"""

    def input_role_query(self, content):
        """进入角色设置页面，根据Role角色筛选数据"""
        self.is_click(user['Click Role'])
        self.input_text(user['Input Role'], txt=content)
        sleep(2)
        self.is_click(user['Click Role value'])

    def click_search(self):
        """进入角色设置页面，点击查询按钮"""
        self.is_click(user['Search'])
        sleep(2.5)

    def click_first_checkbox(self):
        """进入角色设置页面，筛选角色后，点击第一个复选框"""
        self.is_click(user['第一个复选框'])

    def click_permission_setting(self):
        """点击Permission Setting权限设置按钮"""
        self.is_click(user['Permission Setting'])
        sleep(3)

    def basic_data_mgt_status(self):
        """点击 basic_data_management菜单复选框"""
        status = self.select_state(user['Basic Data Management'])
        return status

    def click_basic_data_mgt(self):
        """点击 basic_data_management菜单复选框"""
        self.is_click(user['Basic Data Management'])

    def click_save(self):
        """点击Save保存按钮 """
        self.is_click_dcr(user['Save'])
        sleep(1)

    def get_save_successfully(self):
        """获取Save Successfully保存成功提示语"""
        success = self.element_text(user['Get Save Successfully Text'])
        return success

    def click_confirm(self):
        """点击Confirm确认保存按钮 """
        self.is_click(user['Confirm'])
        sleep(1.5)

    def get_sale_region_mgt_text(self):
        text = self.element_text(user['Sales Region Management'])
        return text


if __name__ == '__main__':
    pass