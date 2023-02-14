import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class StaffAuthorizedList(Base):
    """用户类"""

    @allure.step("关闭不同页面菜单")
    def click_close_menu(self,content):
        self.is_click(user['关闭页面菜单'],content)

    @allure.step("关闭Role弹窗页面菜单")
    def click_close_role(self):
        self.is_click(user['关闭Role弹窗页面'])

    @allure.step("点击user输入框")
    def click_user(self):
        self.is_click(user['User点击'])


    @allure.step("输入文本,进行筛选")
    def select_content(self, type, content):
        if type == 'User ID':
            self.is_click(user['User点击'])
            self.input_text(user['User输入'], txt=content)
            self.is_click(user['User选择'],content)
        elif type == 'Brand':
            self.is_click(user['Brand点击'])
            self.is_click(user['Brand_Position_Country_Role_Staff选择'], content)
            self.is_click(user['User点击'])
        elif type == 'Position':
            self.is_click(user['Position点击'])
            self.input_text(user['Position输入'], txt=content)
            self.is_click(user['Brand_Position_Country_Role_Staff选择'], content)
            self.is_click(user['不活跃天数'])
        elif type == 'Country':
            self.is_click(user['Country点击'])
            self.input_text(user['Country输入'], txt=content)
            self.is_click(user['Brand_Position_Country_Role_Staff选择'], content)
            self.is_click(user['不活跃天数'])
        elif type == 'Role':
            self.is_click(user['Role点击输入'])
            self.input_text(user['Role点击输入'], txt=content)
            self.is_click(user['Brand_Position_Country_Role_Staff选择'], content)
        elif type == 'Customer':
            self.is_click(user['是否有customer'])
            self.is_click(user['是否有customer_销售区域选择'], content)
        elif type == 'Warehouse':
            self.is_click(user['是否有仓库点击'])
            self.is_click(user['是否有customer_销售区域选择'], content)
        elif type == 'Staff Type':
            self.is_click(user['StaffType点击'])
            self.is_click(user['Brand_Position_Country_Role_Staff选择'], content)
        elif type == 'Shop':
            self.is_click(user['是否有店铺点击'])
            self.is_click(user['是否有customer_销售区域选择'], content)
        elif type == 'Authorized Sales Region':
            self.is_click(user['是否有销售区域点击'])
            self.is_click(user['是否有customer_销售区域选择'], content)
        elif type == 'Inactive Day(No Login)':
            self.is_click(user['不活跃天数'])
            self.input_text(user['不活跃天数'], txt=content)
        elif type == 'Last Login Date':
            self.input_text(user['最后登录日期开始'], txt=content)
            self.input_text(user['最后登录日期结束'], txt=content)
            self.is_click(user['不活跃天数'])
        else:
            logging.info('type is wrong,pls check')
        sleep()

    @allure.step("根据表头获取列的class值")
    def get_table_column(self, header):
        attribute = self.get_table_info(user['表头字段'], header, attr='class', sc_element=user['滑动条'])
        logging.info('列元素的属性是%s' % attribute)
        # number=int(attribute[4:])
        return attribute

    @allure.step("获取下载进度值")
    def get_download_value(self):
        attribute = self.get_table_info(user['下载进度条'], attr='aria-valuenow')
        logging.info('下载进度值是%s' % attribute)
        # number=int(attribute[4:])
        return int(attribute)

    @allure.step("获取表格文本")
    def get_table_content(self, content):
        txt = self.element_text(user['表格具体字段'], content)
        return txt

    @allure.step("获取表格文本可点击字段的值")
    def get_text_content(self, content):
        txt = self.element_text(user['表格文本可点击字段'], content)
        return txt

    @allure.step("点击文本可点击字段跳转")
    def click_table_text(self, content):
        self.is_click(user['表格文本可点击字段'], content)

    @allure.step("获取表格数值字段文本值")
    def get_table_column_number(self, content):
        txt = self.element_text(user['表格数值字段'], content)
        return txt

    @allure.step("点击表格数值字段跳转")
    def click_table_column_number(self, content):
        self.is_click(user['表格数值字段'], content)

    @allure.step("获取弹窗页面标题文本")
    def get_pop_windows_content(self):
        txt = self.element_text(user['Role弹窗页面'])
        logging.info('the total txt is %s'%txt)
        return txt[11:]

    @allure.step("获取Total数值文本")
    def get_total_content(self):
        txt = self.element_text(user['Total结果'])
        logging.info('the total txt is %s'%txt)
        return txt[6:]

    @allure.step("获取跳转页Total数值文本")
    def get_total_jump(self):
        txt = self.element_text(user['跳转页面total'])
        logging.info('the total txt is %s'%txt)
        return txt[6:]

    @allure.step("获取页面标题文本")
    def get_page_title(self):
        sleep(3)
        txt = self.element_text(user['活动页面'])
        logging.info('the page txt is %s'%txt)
        return txt

    @allure.step("点击Unfold展开筛选项按钮")
    def click_button(self, txt):
        self.is_click(user['Export_Unfold_Search_Reset按钮'], txt)
        if txt=='Search':
            self.element_exist(user['Loading'])
        elif txt == 'Reset':
            self.element_exist(user['Loading'])
        else:
            sleep()



if __name__ == '__main__':
    pass
