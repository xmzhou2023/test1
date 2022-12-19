import random
from public.base.basics import random_list
from libs.common.read_element import Element
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class UserManagementPage(Base):
    """用户类"""

    @allure.step("查找菜单")
    def click_menu(self, *content):
        self.refresh()
        self.is_click_tbm(user['菜单栏'])
        self.refresh()
        for i in range(len(content)):
            self.is_click_tbm(user['菜单'], content[i])
            logging.info('点击菜单：{}'.format(content[i]))
        self.refresh()
        self.element_exist(user['Loading'])

    @allure.step("点击Unfold 展开筛选项")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        logging.info('点击Unfold 展开筛选项')

    @allure.step("user management页面，输入查询条件")
    def input_search(self, header, content):
        """
        @header： 输入框名称
        @content： 输入内容
        """
        user_list = ['User']
        country_list = ['Sales Region', 'Country/City']
        fuzzySelect_list = ['Belong To Customer', 'Superior']
        exactSelect_list = ['Staff Status', 'Have Superior or Not', 'Have Shop or Not', 'Staff Type']
        inputSelect_list = ['Brand', 'Position', 'Role']
        self.element_exist(user['Loading'])
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if header in user_list:
            self.is_click_tbm(user['输入框'], header)
            self.input_text(user['输入框2'], content, header)
        elif header == 'User Name':
            self.is_click_tbm(user['输入框'], header)
            self.input_text(user['输入框'], content, header)
            self.is_click_tbm(user['输入结果模糊选择'], content)
        elif header in exactSelect_list:
            self.is_click_tbm(user['输入框'], header)
            self.is_click_tbm(user['输入结果精确选择'], content)
        elif header in fuzzySelect_list:
            if content != '':
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框2'], content, header)
                self.is_click_tbm(user['输入结果模糊选择'], content)
        elif header in country_list:
            self.is_click_tbm(user['输入框'], header)
            self.input_text(user['输入框'], content, header)
            self.is_click_tbm(user['地区选择框'], content)
        elif header in inputSelect_list:
            self.is_click_tbm(user['输入框'], header)
            self.input_text(user['输入框4'], content, header)
            self.is_click_tbm(user['输入结果精确选择'], content)
        else:
            logging.error('请输入正确的查询条件')
            raise ValueError('请输入正确的查询条件')

    @allure.step("点击搜索功能")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    @allure.step("判断空值")
    def assert_None(self, result):
        try:
            assert result == '', logging.warning("断言失败: 该值不为None | x:{}".format(result))
            logging.info("断言成功: 该值为None | x:{}".format(result))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("断言：页面查询结果")
    def assert_User_Exist(self, header, content):
        logging.info('开始断言：页面查询结果')
        DomAssert(self.driver).assert_search_contains_result(user['menu表格字段'], user['表格内容'], header, content, sc_element=user['滚动条'], h_element=user['表头文本'])

    @allure.step("断言：页面查询结果")
    def assert_search_result(self, header, content):
        logging.info(f'开始断言：页面查询：{header} 结果 ：{content}')
        if header == 'Superior' or header == 'Belong To Customer' or header == 'User':
            if content == '':
                column = self.get_table_info(user['menu表格字段'], f'{header} ID', sc_element=user['滚动条'],
                                             h_element=user['表头文本'])
                contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
                for i in contents:
                    self.assert_None(i)
            else:
                self.assert_User_Exist(f'{header} ID', content)
        elif header == 'Have Superior or Not' or header == 'Have Shop or Not':
            column = self.get_table_info(user['menu表格字段'], 'Superior ID', sc_element=user['滚动条'], h_element=user['表头文本'])
            contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
            if content == 'Yes':
                for i in contents:
                    ValueAssert.value_assert_IsNoneNot(i)
            else:
                for i in contents:
                    self.assert_None(i)
        elif header == 'Sales Region':
            self.assert_User_Exist(f'{header}5', content)
        elif header == 'Country/City':
            self.assert_User_Exist(f'City', content)
        elif header == 'Staff Type':
            column = self.get_table_info(user['menu表格字段'], 'Belong To Customer ID', sc_element=user['滚动条'], h_element=user['表头文本'])
            contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
            if content == 'Dealer Staff':
                for i in contents:
                    ValueAssert.value_assert_IsNoneNot(i)
            elif header == 'Dealer Staff':
                for i in contents:
                    self.assert_None(i)
        else:
            self.assert_User_Exist(header, content)

    @allure.step("组合查询 组合方法")
    def random_Query_Method(self, kwargs):
        list_query = []
        num = random.randint(3, 8)
        for i in kwargs:
            list_query.append(i)
        logging.info(f'输入框：{list_query}')
        list_random = random_list(list_query, num)
        logging.info(f'随机组合：输入框：{list_random}')
        for i in list_query:
            logging.info(f'随机组合：输入内容：{kwargs[i]}')
            self.input_search(i, kwargs[i])
        self.click_search()
        for i in list_query:
            self.assert_search_result(i, kwargs[i])


if __name__ == '__main__':
    pass
