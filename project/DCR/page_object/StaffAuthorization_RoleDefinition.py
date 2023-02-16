import random

from libs.common.read_element import Element
from public.base.basics import Base, random_list
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


    @allure.step("进入角色设置页面，筛选角色后，点击第一个复选框")
    def click_first_checkbox(self):
        self.is_click_dcr(user['第一个复选框'])

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

    @allure.step("点击Confirm确认保存按钮 ")
    def click_confirm(self):
        self.is_click(user['dialogConfirm'])
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

    def input_text(self, locator, txt, *choice):
        """输入文本"""
        sleep(0.5)
        ele = self.find_element(locator, *choice)
        ele.clear()
        ele.send_keys(txt)
        logging.info("输入文本：{}".format(txt))

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

    @allure.step("输入查询条件")
    def input_search(self, header, content):
        input_list = ['Creator', 'Updater']
        exactSelect_list = ['Enable or Not', 'Menu Type']
        inputSelect_list = ['Role']
        self.element_exist(user['Loading'])
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if content != '':
            if header in input_list:
                self.input_text(user['输入框'], content, header)
            elif header in exactSelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
            elif header in inputSelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框4'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
                self.is_click_tbm(user['输入框名称'], header)
            else:
                logging.error('请输入正确的查询条件')
                raise ValueError('请输入正确的查询条件')

    @allure.step("断言：页面查询结果")
    def assert_Query_result(self, header, content):
        """
        :param header: 需要获取的指定字段
        :param content: 需要断言的值
        """
        logging.info('开始断言：页面查询结果')
        DomAssert(self.driver).assert_search_result(user['menu表格字段'], user['表格内容'], header, content,
                                                    sc_element=user['滚动条'], h_element=user['表头文本'])

    @allure.step("点击Search 查询按钮")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])
        logging.info('点击Search查询按钮')

    @allure.step("点击Unfold 展开筛选项")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        logging.info('点击Unfold 展开筛选项')

    @allure.step("断言：页面查询结果")
    def assert_search_result(self, header, content):
        logging.info(f'开始断言：页面查询：{header} 结果 ：{content}')
        if header == 'Enable or Not':
            if content == 'Enable':
                self.assert_Query_result(header, 'Yes')
            else:
                self.assert_Query_result(header, 'No')
        else:
            self.assert_Query_result(header, content)

    @allure.step("组合查询 组合方法")
    def All_Query_Method(self, kwargs):
        list_query = []
        for i in kwargs:
            list_query.append(i)
        logging.info(f'输入框：{list_query}')
        for i in list_query:
            logging.info(f'随机组合：{i} 输入框输入内容：{kwargs[i]}')
            self.input_search(i, kwargs[i])
        self.click_search()
        for i in list_query:
            self.assert_search_result(i, kwargs[i])

    @allure.step("组合查询 组合方法")
    def random_Query_Method(self, kwargs):
        list_query = []
        for i in kwargs:
            list_query.append(i)
        logging.info(f'输入框：{list_query}')
        list_random = random_list(list_query, 1)
        logging.info(f'随机组合：输入框：{list_random}')
        for i in list_random:
            logging.info(f'随机组合：{i} 输入框输入内容：{kwargs[i]}')
            self.input_search(i, kwargs[i])
        self.click_search()
        for i in list_random:
            self.assert_search_result(i, kwargs[i])

    @allure.step("点击功能按钮")
    def click_function_button(self, function):
        """
        @function： 需要点击的功能按钮，具体如下：
        Add, Export Permission, Permission Setting, More Option,
        Delete, configCountry
        """
        logging.info(f'点击功能按钮： {function}')
        MoreOptionList = ['Delete', 'configCountry']
        if function in MoreOptionList:
            self.is_click_tbm(user['功能按钮'], 'More Option')
            self.is_click_tbm(user['功能按钮2'], function)
            if function == 'Delete':
                self.is_click_tbm(user['dialogConfirm'])
        else:
            self.is_click_tbm(user['功能按钮'], function)

    @allure.step("输入角色定义内容")
    def input_role_content(self, header, content):
        self.input_text(user['AddRole'], content, header)
        logging.info(f'输入角色内容 {header} : {content}')

    @allure.step("点击保存")
    def click_AddSave(self):
        self.is_click_tbm(user['AddSave'])
        logging.info('点击保存')

    @allure.step("点击复选框")
    def click_checkbox(self, UID, header='Role'):
        """
        @UID： UID 默认传入userid，username或其他唯一内容也可以传
        """
        column = self.get_table_info(user['menu表格字段'], header, h_element=user['表头文本'])
        self.is_click_tbm(user['指定复选框'], column, UID)
        logging.info(f'点击 {UID} 复选框')

    @allure.step("点击指定行编辑")
    def click_edit(self, role):
        """
        :param role: 指定role
        """
        col = self.get_table_info(user['menu表格字段'], 'Operation')
        self.is_click(user['指定行按钮'], role, col)
        logging.info(f'点击指定行 {role} 编辑按钮')

    @allure.step("断言：查询结果为空")
    def assert_NoData(self):
        logging.info('开始断言：查询结果为空')
        DomAssert(self.driver).assert_control(user['NoData'])

    @allure.step("断言：点击导出有进度条")
    def assert_export_success(self):
        logging.info('开始断言：点击导出存在进度条')
        DomAssert(self.driver).assert_control(user['导出进度条'])

    @allure.step("点击指定菜单复选框")
    def click_menu_checkbox(self, menu):
        """
        :param menu: 指定菜单
        """
        self.is_click(user['菜单复选框'], menu)
        logging.info(f'点击指定菜单 {menu} 复选框')

    @allure.step("点击指定菜单管理页")
    def click_menu_management(self, menu):
        """
        :param menu: 指定菜单
        """
        if menu.lower() == 'app':
            self.is_click(user['菜单管理页'], 'App Menu Management')
            logging.info(f'点击指定菜单 {menu} 复选框')
        elif menu.lower() == 'web':
            self.is_click(user['菜单管理页'], 'WEB Menu Management')
            logging.info(f'点击指定菜单 {menu} 复选框')
        else:
            logging.error('请输入正确的菜单名')
            raise ValueError('请输入正确的菜单名')

    @allure.step("点击保存")
    def click_permissionSave(self):
        self.is_click_tbm(user['permissionSave'])
        logging.info('点击保存')

    @allure.step("点击确定")
    def click_dialog_Confirm(self):
        self.is_click_tbm(user['dialogConfirm'])
        logging.info('点击确定')


if __name__ == '__main__':
    pass