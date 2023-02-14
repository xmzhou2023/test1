from libs.common.read_element import Element
from libs.common.time_ui import sleep
from ..test_case.conftest import *
from libs.config.conf import BASE_DIR
from public.base.basics import Base, random_list
import random

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ShopAssetPage(Base):

    @allure.step("Shop Asset页面，点击Import按钮")
    def click_import(self):
        self.is_click(user['Import'])
        sleep(1)

    @allure.step("Shop Asset页面，点击Import Save保存按钮")
    def click_import_save(self):
        self.is_click(user['Import Save'])

    @allure.step("导Shop Asset模板-上传正确的模板文件")
    def upload_true_file(self, file1):
        path1 = os.path.join(BASE_DIR, 'project', 'DCR', 'data', file1)
        logging.info("打印上传的用户模板文件path：{}".format(path1))
        self.click_import_upload_save(path1)

    @allure.step("导Shop Asset模板-上传错误的模板文件")
    def upload_error_file(self, file1):
        path1 = os.path.join(BASE_DIR, 'project', 'DCR', 'data', file1)
        logging.info("打印上传的用户模板文件path：{}".format(path1))
        self.click_import_upload_save(path1)

    @allure.step("Shop Asset页面，点击Import 导入功能上传文件")
    def click_import_upload_save(self, file1):
        self.is_click(user['Import Upload'])
        sleep(3.5)
        ele = self.driver.find_element('xpath', "//button/..//input[@name='file']")
        ele.send_keys(file1)
        sleep(3)
        self.is_click(user['Import Save'])
        sleep(1.5)
        self.presence_sleep_dcr(user['Upload Confirm'])
        self.is_click(user['Upload Confirm'])


    @allure.step("循环点击查询，直到获取到导入记录状态为Upload Successfully")
    def click_import_status_search(self):
        import_status = self.import_record_status(user['Import Search'], user['Get Import Record Status'])
        return import_status

    """导入记录页面，获取列表字段断言是否导入成功"""
    @allure.step("Import Record页面，获取File Name字段文本")
    def get_import_file_name(self):
        get_file_name = self.element_text(user['Get Import Record File Name'])
        return get_file_name

    @allure.step("Import Record页面，获取Status字段文本")
    def get_import_status(self):
        get_status = self.element_text(user['Get Import Record Status'])
        return get_status

    @allure.step("Import Record页面，获取Total字段文本")
    def get_import_total(self):
        get_total = self.element_text(user['Get Import Record Total'])
        return get_total

    @allure.step("Import Record页面，获取Total字段文本")
    def get_import_success(self):
        get_success = self.element_text(user['Get Import Record Success'])
        return get_success

    @allure.step("Import Record页面，获取Failed字段文本")
    def get_import_failed(self):
        get_failed = self.element_text(user['Get Import Record Failed'])
        return get_failed

    @allure.step("Import Record页面，获取 Fail Data字段文本")
    def get_import_fail_data(self):
        self.scroll_into_view(user['Get Import Fail Data'])
        get_fail_data = self.element_text(user['Get Import Fail Data'])
        return get_fail_data

    @allure.step("Import Record页面，获取 Import Date字段文本")
    def get_import_import_date(self):
        self.scroll_into_view(user['Get Import Import Date'])
        get_import_date = self.element_text(user['Get Import Import Date'])
        get_import_date1 = get_import_date[0:10]
        return get_import_date1


    @allure.step("Shop Asset页面，点击Delete按钮")
    def click_delete(self):
        self.is_click(user['Delete'])

    @allure.step("Shop Asset页面，勾选第一条复选框")
    def click_checkbox(self):
        self.is_click_dcr(user['勾选第复选框'])

    @allure.step("Shop Asset页面，输入创建时间与结束时间")
    def input_create_date_query(self, start_date, end_date):
        self.is_click(user['Create start Date'])
        self.input_text(user['Create start Date'], start_date)
        self.is_click(user['Create end Date'])
        self.input_text(user['Create end Date'], end_date)

    @allure.step("Shop Asset页面，根据状态查询门店资产数据")
    def click_status_query(self, content):
        self.is_click(user['query Status'])
        self.is_click(user['query Status Value'], content)

    @allure.step("Shop Asset页面，点击Unfold展开筛选条件")
    def click_unfold_fold(self, content):
        self.is_click(user['Unfold_Fold'], content)

    @allure.step("Shop Asset页面，点击Search按钮")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    @allure.step("Shop Asset列表, 获取列表字段内容")
    def get_list_field_content(self, field):
        self.scroll_into_view(user[field])
        field = self.element_text(user[field])
        return field

    @allure.step("Asset Definition页面, 获取列表Total总条数")
    def get_list_total(self):
        total = self.element_text(user['Get list Total'])
        total1 = int(total[6:])
        return total1

    @allure.step("断言分页总数是否存在数据")
    def assert_total(self, total):
        if int(total) >= 1:
            logging.info("门店资产列表，分页总条数大于0，能查询到考勤记录数Total:{}".format(total))
        else:
            logging.info("门店资产列表，分页总条数为0，未查询到考勤记录数Total:{}:".format(total))



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
            self.assert_User_Exist(f'{header} 3', content)
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
