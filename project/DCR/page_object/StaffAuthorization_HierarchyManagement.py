import random
from public.base.basics import random_list
from libs.common.read_element import Element
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class HierarchyManagement(Base):
    """用户类"""

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
        input_list = ['Employee Name']
        country_list = ['Country/City']
        fuzzySelect_list = ['Superior']
        exactSelect_list = ['Staff Status', 'Gender', 'Have Superior or Not', 'Have Shop or Not', 'Staff Type']
        inputSelect_list = ['Brand', 'Position', 'Country']
        inputSelect_list2 = ['User Name']
        self.element_exist(user['Loading'])
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if content != '':
            if header == 'User ID':
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框3'], content, header)
            elif header in input_list:
                self.input_text(user['输入框'], content, header)
            elif header in exactSelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
            elif header in fuzzySelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框2'], content, header)
                self.is_click_tbm(user['输入结果模糊选择'], content)
            elif header in country_list:
                country = content.split('_')
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], country[2], header)
                self.is_click_tbm(user['地区选择框'], country[0], country[1], country[2])
            elif header in inputSelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框4'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
            elif header in inputSelect_list2:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], content, header)
                self.is_click_tbm(user['输入结果模糊选择'], content)
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

    @allure.step("点击Unfold 展开筛选项")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        logging.info('点击Unfold 展开筛选项')

    @allure.step("判断空值")
    def assert_None(self, result):
        try:
            assert result == '', logging.warning("断言失败: 该值不为None | x:{}".format(result))
            logging.info("断言成功: 该值为None | x:{}".format(result))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("断言：页面查询结果")
    def assert_search_result(self, header, content):
        logging.info(f'开始断言：页面查询：{header} 结果 ：{content}')
        if header == 'Country/City':
            country = content.split('_')
            self.assert_Query_result(f'City', country[2])
        elif header == 'Have Superior or Not':
            column = self.get_table_info(user['menu表格字段'], f"{header.split(' ')[1]} ID", sc_element=user['滚动条'],
                                         h_element=user['表头文本'])
            contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
            if content == 'Yes':
                for i in contents:
                    ValueAssert.value_assert_IsNoneNot(i)
            elif content == 'No':
                for i in contents:
                    self.assert_None(''.join(i.split()))
        elif header == 'Have Shop or Not':
            column = self.get_table_info(user['menu表格字段'], f"{header.split(' ')[1]} Code", sc_element=user['滚动条'],
                                         h_element=user['表头文本'])
            contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
            if content == 'Yes':
                for i in contents:
                    ValueAssert.value_assert_IsNoneNot(i)
            elif content == 'No':
                for i in contents:
                    self.assert_None(''.join(i.split()))
        elif header == 'Employee Name':
            self.assert_Query_result('User Name', content)
        elif header == 'Superior':
            self.assert_Query_result(f'{header} ID', content)
        else:
            self.assert_Query_result(header, content)

    @allure.step("组合查询 组合方法")
    def random_Query_Method(self, kwargs):
        list_query = []
        num = random.randint(3, 8)
        for i in kwargs:
            list_query.append(i)
        logging.info(f'输入框：{list_query}')
        list_random = random_list(list_query, num)
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
        :param function: 需要点击的功能按钮，具体如下：
        Export, Staff Hierarchy, Add The Subordinate, Delete The Subordinate
        """
        logging.info(f'点击功能按钮： {function}')
        self.is_click(user['功能按钮'], function)
        if function == 'Add The Subordinate' or function == 'Delete The Subordinate':
            self.element_exist(user['弹窗Loading'])

    @allure.step("断言：存在上下级关系树")
    def assert_Hierarchy_exist(self, name):
        """
        :param name: 需要断言的名称
        """
        logging.info(f'开始断言：存在上下级关系树: {name}')
        self.input_text(user['关系输入框'], name)
        DomAssert(self.driver).assert_control(user['关系人'], name)

    @allure.step("点击复选框")
    def click_checkbox(self, name):
        """
        :param name: userid
        """
        col = self.get_table_info(user['menu表格字段'], 'User ID')
        self.is_click_tbm(user['复选框'], col, name)
        logging.info(f'点击 {name} 复选框')
        sleep(1)

    @allure.step("输入弹框查询条件")
    def input_dialog_search(self, header, content):
        """
        :param header: 输入框
        :param content: 内容
        """
        input_list = ['User ID', 'Employee Name']
        country_list = ['Country/City']
        exactSelect_list = ['Division', 'Position', 'Have Superior or Not', 'Staff Status', 'Gender']
        logging.info(f'输入弹框查询条件： {header} ，内容： {content}')
        if content != '':
            if header in input_list:
                self.input_text(user['弹窗输入框'], content, header)
            elif header in exactSelect_list:
                self.is_click_tbm(user['弹窗输入框'], header)
                self.input_text(user['弹窗输入框'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
            elif header in country_list:
                country = content.split('_')
                self.is_click_tbm(user['输弹窗输入框入框'], header)
                self.input_text(user['弹窗输入框'], country[2], header)
                self.is_click_tbm(user['地区选择框'], country[0], country[1], country[2])
            else:
                logging.error('请输入正确的弹框查询条件')
                raise ValueError('请输入正确的弹框查询条件')

    @allure.step("点击Unfold 展开筛选项")
    def click_dialog_unfold(self):
        self.is_click(user['弹窗Unfold'])
        logging.info('点击弹窗Unfold按钮')

    @allure.step("点击Search 查询按钮")
    def click_dialog_search(self):
        self.is_click(user['弹窗Search'])
        logging.info('点击弹窗Search按钮')
        self.element_exist(user['弹窗Loading'])

    @allure.step("点击Save")
    def click_dialog_save(self, style=None):
        """
        :param style: 保存类型，如果是删除保存，需要点击弹框删除，故需要传入变量delete
        """
        self.is_click(user['弹窗Save'])
        logging.info('点击弹窗Save按钮')
        self.element_exist(user['Loading'])
        if style == 'delete':
            DomAssert(self.driver).assert_att('You will delete the records!')
            self.is_click_tbm(user['Delete'])
            logging.info('点击弹窗Delete按钮')

    @allure.step("点击指定行功能按钮")
    def click_row_function(self, uid, function):
        """
        :param uid: 指定User ID
        :param function: 需要点击的功能按钮，具体如下：
        Subordinate, Operation
        """
        col = self.get_table_info(user['menu表格字段'], function)
        self.is_click(user['指定行按钮'], uid, col)
        self.element_exist(user['弹窗Loading'])
        logging.info(f'点击指定行 {uid} 功能按钮: {function}')

    @allure.step("断言：弹窗页面查询结果")
    def assert_dialog_Query_result(self, header, content):
        """
        :param header: 需要获取的指定字段
        :param content: 需要断言的值
        """
        logging.info('开始断言：页面查询结果')
        DomAssert(self.driver).assert_search_result(user['弹窗menu表格字段'], user['表格内容'], header, content)

    @allure.step("断言：查询结果为空")
    def assert_NoData(self):
        logging.info('开始断言：查询结果为空')
        DomAssert(self.driver).assert_control(user['NoData'])

    @allure.step("断言：点击导出有进度条")
    def assert_export_success(self):
        logging.info('开始断言：点击导出存在进度条')
        DomAssert(self.driver).assert_control(user['导出进度条'])

    @allure.step("点击弹框复选框")
    def click_dialog_checkbox(self, name):
        """
        :param name: userid
        """
        col = self.get_table_info(user['弹窗menu表格字段'], 'User ID')
        self.is_click_tbm(user['复选框'], col, name)
        logging.info(f'点击 {name} 弹框复选框')
        sleep(1)
if __name__ == '__main__':
    pass
