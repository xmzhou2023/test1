import logging
import os
import allure
from libs.common.read_config import ReadConfig
from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
pro_env = 'prod' # 需要手动配置测试环境
user = Element(pro_name, object_name)
ini = ReadConfig(pro_name, pro_env)


class LoginPage(Base):
    """DCR登录类"""
    def input_account(self, content):
        """输入工号"""
        self.input_text(user['工号输入框'], txt=content)

    def input_passwd(self, content):
        """输入密码"""
        self.input_text(user['密码输入框'], txt=content)

    def switch_lanuage(self, content):
        """语言切换"""
        self.is_click(user['语言切换'])
        self.is_click(user['选择英文'], content)

    def click_check_box(self):
        """判断是否被选中"""
        self.is_click(user['隐私保护勾选'])

    def get_check_box_class(self):
        """获取复选框对应的 Class属性是否包含is-checked"""
        ss = self.find_element(user['隐私保护勾选'])
        get_check_state = ss.get_attribute('class')
        return get_check_state

    def check_box(self):
        """判断是否被选中"""
        checkbox = self.select_state(user['隐私保护勾选'])
        return checkbox

    def click_loginsubmit(self):
        """点击帐号密码登录"""
        self.is_click(user['登录'])
        sleep(6)

    def click_loginOut(self):
        """点击退出登录"""
        sleep(2)
        self.is_click(user['退出登录'])
        sleep(2)

    def get_home_page_text(self):
        Base.presence_sleep_dcr(self, user['get Home Page Customer text'])
        homepage = self.element_text(user['get Home Page Customer text'])
        return homepage

    @allure.step("获取当前打开状态的菜单class值")
    def get_open_menu_class(self):
        ss = self.find_element(user['打开状态的菜单'])
        get_menu_class = ss.get_attribute('class')
        return get_menu_class

    @allure.step("关闭当天打开状态的菜单")
    def click_close_open_menu(self):
        self.is_click(user['关闭当前打开的菜单'])

    @allure.step("登录方法")
    def dcr_login(self, drivers, account, passwd):
        #user = LoginPageDCR(drivers)
        self.get_url(ini.url)
        sleep(3)
        self.input_account(account)
        self.input_passwd(passwd)
        sleep(1.5)
        get_check_class = self.get_check_box_class()
        if "is-checked" not in str(get_check_class):
            self.click_check_box()
        self.click_loginsubmit()


    @allure.step("点击菜单")
    def click_gotomenu(self, *content):
        """前往左侧菜单栏"""
        self.refresh()
        self.is_click(user['菜单栏'])
        self.refresh()
        level = []
        navstr = ""
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        for i in range(len(content)):
            logging.info(user[level[i]])
            sleep(3.5)
            self.scroll_into_view(user[level[i]])
            sleep(4)
            self.is_click(user[level[i]])
        self.element_exist(user['Loading'])

    @allure.step("查找菜单")
    def click_menu(self, *content):
        self.refresh()
        self.is_click_tbm(user['菜单栏'])
        self.refresh()
        for i in range(len(content)):
            self.is_click_tbm(user[f'菜单{i + 1}'], content[i])
            logging.info('点击菜单：{}'.format(content[i]))
        self.refresh()
        self.element_exist(user['Loading'])

    @allure.step("获得Record指定内容")
    def get_Record_info(self, menu, name, header):
        """
        :param menu: 菜单名
        :param name: 输入文件名
        :param header: 需要获取的指定字段
        """
        for i in range(20):
            ac_menu = self.element_text(user['当前菜单'])
            if ac_menu != menu:
                self.click_menu('Basic Data Management', menu)
            column = self.get_table_info(user['表格字段'], header, h_element=user['表头文本'])
            content = self.element_text(user['表格指定列内容'], name, column)
            logging.info(f'获得 {menu} 页面 {name} 文件 {header} 字段内容 {content}')
            return content

    @allure.step("断言：导入导出Record结果")
    def assert_Record_result(self, menu, name, header, result=None):
        """
        :param menu: 菜单
        :param name: 输入文件名
        :param header: 需要获取的指定字段
        :param result: 需要断言的值 比如状态，数量，时间
        """
        ac_result = self.get_Record_info(menu, name, header)
        if header == 'File Size':
            ValueAssert.value_assert_IsNot(ac_result, '0B')
        else:
            ValueAssert.value_assert_In(result, ac_result)

if __name__ == '__main__':
    pass
