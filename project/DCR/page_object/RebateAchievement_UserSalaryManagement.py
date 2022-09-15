import logging
from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *
from libs.config.conf import BASE_DIR

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class UserSalaryManagement(Base):
    @allure.step("User Salary Management页面，输入User筛选，点击Search按钮查询")
    def input_user_query_search(self, userid):
        self.presence_sleep_dcr(user['筛选用户'])
        self.is_click(user['筛选用户'])
        self.input_text(user['输入筛选用户'], userid)
        sleep(2)
        self.presence_sleep_dcr(user['选中筛选用户'], userid)
        self.is_click(user['选中筛选用户'], userid)
        self.is_click(user['Search'])
        sleep(3)

    @allure.step("User Salary Management页面，点击Import 导入功能")
    def click_import_upload_save(self, file):
        self.is_click(user['Import Upload'])
        ele = self.driver.find_element('xpath', "//input[@name='file']")
        ele.send_keys(file)
        sleep(1)
        self.is_click(user['Import Save'])
        sleep(1)
        self.presence_sleep_dcr(user['Upload Confirm'])
        self.is_click(user['Upload Confirm'])


    @allure.step("导入员工工资模板-上传正确的文件")
    def upload_true_file(self):
        path1 = os.path.join(BASE_DIR, 'project', 'DCR', 'data', 'StaffSalaryTemplate.xlsx')
        self.click_import_upload_save(path1)

    @allure.step("导入员工工资模板-上传错误文件")
    def upload_wrong_file(self):
        path1 = os.path.join(BASE_DIR, 'project', 'DCR', 'data', 'CustomerTemplate.xlsx')
        self.click_import_upload_save(path1)

    @allure.step("User Salary Management页面，点击Import 按钮")
    def click_import(self):
        self.is_click(user['Import Button'])

    @allure.step("User Salary Management页面，点击Import Save 按钮")
    def click_import_save(self):
        self.is_click(user['Import Save'])


    """删除功能"""
    @allure.step("User Salary Management页面，点击Delete,点击确认删除按钮")
    def click_delete(self):
        self.is_click(user['Delete'])
        sleep(1)
        self.presence_sleep_dcr(user['Confirm Delete Yes'])
        self.is_click(user['Confirm Delete Yes'])

    @allure.step("User Salary Management页面，勾选第一个和第二个复选框")
    def click_first_checkbox(self):
        self.presence_sleep_dcr(user['勾选第一条复选'])
        self.is_click_dcr(user['勾选第一条复选'])
        self.is_click_dcr(user['勾选第二条复选'])

    @allure.step("Import Record页面，点击Search 查询按钮")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(1.5)

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



if __name__ == '__main__':
    pass
