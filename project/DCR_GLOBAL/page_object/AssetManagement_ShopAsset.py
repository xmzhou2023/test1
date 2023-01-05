from libs.common.read_element import Element
from libs.common.time_ui import sleep
from ..test_case.conftest import *
from libs.config.conf import BASE_DIR
from public.base.basics import Base, random_list
import random

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ShopAssetPage(Base):
    @allure.step("Shop Asset页面，点击Search按钮")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(2)

    @allure.step("Shop Asset页面，点击Unfold展开筛选条件")
    def click_unfold_fold(self, content):
        self.is_click(user['Unfold_Fold'], content)

    @allure.step("断言：页面查询结果")
    def assert_User_Exist(self, header, content):
        logging.info('开始断言：页面查询结果')
        DomAssert(self.driver).assert_search_contains_result(user['menu表格字段'], user['表格内容'], header, content, sc_element=user['滚动条'], h_element=user['表头文本'])

    @allure.step("判断空值")
    def assert_None(self, result):
        try:
            assert result == '', logging.warning("断言失败: 该值不为None | x:{}".format(result))
            logging.info("断言成功: 该值为None | x:{}".format(result))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("user management页面，输入查询条件")
    def input_search(self, header, content):
        """
        @header： 输入框名称
        @content： 输入内容
        """
        input_select_list = ['Country', 'Brand', 'Category']
        input_select_all_list1 = ['Has ASN', 'Status', 'Design By']
        create_date_list = ['Create Date']
        click_input_list = ['Asset Name']
        shop_list = ['Shop']
        sales_region_list = ['Sales Region']
        manpower_type_list = ['Manpower Type']
        self.element_exist(user['Loading'])
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if header in input_select_list:
            self.is_click(user['输入框'], header)
            self.input_text(user['输入框2'], content, header)
            self.is_click(user['输入结果精确选择'], content)
        elif header in input_select_all_list1:
            self.is_click(user['输入框'], header)
            self.is_click(user['输入结果精确选择'], content)
        elif header in create_date_list:
            self.is_click(user['Create Start Date'])
            self.input_text(user['Create Start Date'], content)
            self.is_click(user['Create End Date'])
            self.input_text(user['Create End Date'], content)
            """弹出日历空间后，点击日历标签释法"""
            self.is_click(user['点击label标签'], header)
        elif header in click_input_list:
            self.is_click(user['输入框'], header)
            self.input_text(user['输入框'], content, header)
        elif header in shop_list:
            self.is_click(user['输入框'], header)
            self.input_text(user['输入框2'], content, header)
            sleep(1)
            self.is_click(user['输入结果模糊选择'], content)
        elif header in sales_region_list:
            self.is_click(user['输入框'], header)
            self.input_text(user['输入框'], content, header)
            sleep(0.8)
            self.is_click(user['输入区域精确选择'], header, content)
        elif header in manpower_type_list:
            self.is_click_dcr(user['输入框2'], header)
            self.input_text(user['输入框1'], content, header)
            self.is_click(user['输入结果精确选择'], content)
        else:
            logging.error('请输入正确的查询条件')
            raise ValueError('请输入正确的查询条件')


    @allure.step("断言：页面查询结果")
    def assert_search_result(self, header, content):
        logging.info(f'开始断言：页面查询：{header} 结果 ：{content}')
        if header == 'Brand':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Country':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Shop':
            self.assert_User_Exist(f'{header} ID', content)
        elif header == 'Manpower Type':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Design By':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Sales Region':
            self.assert_User_Exist(f'{header} 1', content)
        elif header == 'Category':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Asset Name':
            self.assert_User_Exist(f'{header}(CN)', content)
        elif header == 'Status':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Has ASN':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Create Date':
            self.assert_User_Exist(f'{header}', content)
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
        for i in list_random:
            logging.info(f'随机组合：输入内容：{kwargs[i]}')
            self.input_search(i, kwargs[i])
        self.click_search()
        for i in list_random:
            self.assert_search_result(i, kwargs[i])


if __name__ == '__main__':
    pass