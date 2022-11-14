from libs.common.read_element import Element
from libs.common.time_ui import sleep
from ..test_case.conftest import *
from libs.config.conf import BASE_DIR
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

    @allure.step("导Shop Asset模板-上传正确的文件")
    def upload_true_file(self, file1):
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
        sleep(2)

    @allure.step("Shop Asset列表, 获取列表字段内容")
    def get_list_field_content(self, field):
        self.scroll_into_view(user[field])
        field = self.element_text(user[field])
        return field

if __name__ == '__main__':
    pass
