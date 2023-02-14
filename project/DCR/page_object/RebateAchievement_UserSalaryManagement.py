import logging
from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from public.base.assert_ui import ValueAssert, DomAssert

from ..test_case.conftest import *
from libs.config.conf import BASE_DIR

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class UserSalaryManagement(Base):
    @allure.step("User Salary Management页面，输入Country筛选，点击Search按钮查询")
    def input_country_query_search(self, country):
        self.is_click(user['筛选国家'])
        self.input_text_dcr(user['输入筛选国家'], country)
        sleep(1.5)
        self.is_click(user['选中筛选国家'], country)
        self.click_search()

    @allure.step("User Salary Management页面，输入User筛选，点击Search按钮查询")
    def input_user_query_search(self, userid):
        self.presence_sleep_dcr(user['筛选用户'])
        self.is_click(user['筛选用户'])
        self.input_text(user['输入筛选用户'], userid)
        sleep(2)
        self.presence_sleep_dcr(user['选中筛选用户'], userid)
        self.is_click(user['选中筛选用户'], userid)
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    @allure.step("User Salary Management页面，点击Import 导入功能")
    def click_import_upload_save(self, file):
        self.is_click(user['Import Upload'])
        sleep(1.5)
        ele = self.driver.find_element('xpath', "//button/..//input[@name='file']")
        ele.send_keys(file)
        sleep(1)
        self.is_click(user['Import Save'])
        sleep(1)
        self.presence_sleep_dcr(user['Upload Confirm'])
        self.is_click(user['Upload Confirm'])


    @allure.step("User Salary Management页面，点击Import Payslip 导入工资明细单功能")
    def click_import_payslip_upload_save(self, file):
        self.is_click(user['Import Upload'])
        sleep(2)
        ele = self.driver.find_element('xpath', "//button/..//input[@name='file']")
        ele.send_keys(file)
        sleep(1)
        self.is_click(user['Import Save'])
        sleep(2)
        self.presence_sleep_dcr(user['Upload Confirm'])
        self.is_click(user['Upload Confirm'])
        sleep(1)

    @allure.step("导入员工工资模板-上传正确的文件")
    def upload_true_file(self, file1):
        path1 = os.path.join(BASE_DIR, 'project', 'DCR', 'data', file1)
        logging.info("打印上传的文件path：{}".format(path1))
        if file1 == 'PaySlipTemplate.xlsx':
            self.click_import_payslip_upload_save(path1)
        elif file1 == 'StaffSalaryTemplate.xlsx':
            self.click_import_upload_save(path1)
        else:
            self.click_import_upload_save(path1)

    @allure.step("导入员工工资模板-上传错误文件")
    def upload_wrong_file(self, wrong_file):
        path3 = os.path.join(BASE_DIR, 'project', 'DCR', 'data', wrong_file)
        if wrong_file == 'CustomerTemplate1.xlsx':
            self.click_import_upload_save(path3)
        elif wrong_file == 'CustomerTemplate2.xlsx':
            self.click_import_payslip_upload_save(path3)
        else:
            self.click_import_upload_save(path3)

    @allure.step("User Salary Management页面，点击Import 按钮")
    def click_import(self):
        self.is_click(user['Import Button'])
        sleep(1.5)

    @allure.step("User Salary Management页面，点击Import Payslip按钮")
    def click_import_payslip(self):
        self.is_click(user['Import Payslip Button'])
        sleep(1.5)

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
    def click_first_checkbox1(self):
        self.presence_sleep_dcr(user['勾选第一条复选框'])
        self.is_click_dcr(user['勾选第一条复选框'])

    @allure.step("User Salary Management页面，勾选第一个和第二个复选框")
    def click_first_checkbox2(self):
        self.presence_sleep_dcr(user['勾选第一条复选框'])
        self.is_click_dcr(user['勾选第一条复选框'])
        self.is_click_dcr(user['勾选第二条复选框'])

    @allure.step("Import Record页面，点击Search 查询按钮")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    @allure.step("Import Record页面，点击Reset 重置按钮")
    def click_reset(self):
        self.is_click(user['Reset'])
        self.element_exist(user['Loading'])

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


    """获取User Salary Management页面，是否加载导入成功的数据"""
    @allure.step("User Salary Management页面，获取 User Name字段文本")
    def get_list_user_name(self):
        self.presence_sleep_dcr(user['Get list User Name'])
        get_user_name = self.element_text(user['Get list User Name'])
        return get_user_name

    @allure.step("User Salary Management页面，获取 User ID字段文本")
    def get_list_user_id(self):
        self.presence_sleep_dcr(user['Get list User ID'])
        get_user_id = self.element_text(user['Get list User ID'])
        return get_user_id

    @allure.step("User Salary Management页面，获取 YYYY MM字段文本")
    def get_list_yyyy_mm(self):
        get_yyyy_mm = self.element_text(user['Get list YYYY MM'])
        return get_yyyy_mm

    @allure.step("User Salary Management页面，获取 Position字段文本")
    def get_list_position(self):
        get_position = self.element_text(user['Get list Position'])
        return get_position

    @allure.step("User Salary Management页面，获取 Basic Salary字段文本")
    def get_list_basic_salary(self):
        self.scroll_into_view(user['Get list Basic Salary'])
        get_basic_salary = self.element_text(user['Get list Basic Salary'])
        return get_basic_salary

    @allure.step("User Salary Management页面，获取 Basic Salary字段文本")
    def get_list_bonus_incentive(self):
        self.scroll_into_view(user['Get list Bonus Incentive'])
        get_incentive = self.element_text(user['Get list Bonus Incentive'])
        return get_incentive

    @allure.step("User Salary Management页面，获取Total分页总条数")
    def get_list_total(self):
        self.presence_sleep_dcr(user['Get list Total'])
        get_total = self.element_text(user['Get list Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("User Salary Management页面，导入前获取列表总条数，如果大于2条以上记录，先删除已存在的工资单")
    def delete_repetitive_salary(self, total):
        logging.info("获取User Salary Management页面Total分页总条数：{}".format(total))
        if int(total) == 4:
            self.click_first_checkbox2()
            self.click_delete()
            DomAssert(self.driver).assert_att('Deleted Successfully')
        elif int(total) == 3:
            self.click_first_checkbox1()
            self.click_delete()
            DomAssert(self.driver).assert_att('Deleted Successfully')
        else:
            logging.info("获取User Salary Management页面Total分页总条数：{}".format(total))


    @allure.step("User Salary Management页面，断言 Total分页总条数是否有数据")
    def assert_total(self, total):
        if int(total) > 1:
            logging.info("筛选User Salary Management页面，加载分页总条数Total:{}".format(total))
        else:
            logging.info("筛选User Salary Management页面，加载分页总条数Total:{}:".format(total))

    @allure.step("User Salary Management页面，获取 Country字段文本")
    def get_list_country(self):
        self.scroll_into_view(user['Get list Country'])
        sleep(1.5)
        get_country = self.element_text(user['Get list Country'])
        return get_country

    """编辑工资"""
    @allure.step("User Salary Management页面，点击Edit编辑功能")
    def click_edit(self):
        self.is_click(user['Edit'])
        sleep(0.5)

    @allure.step("User Salary Management页面，编辑基本工资字段")
    def input_edit_basic_salary(self, salary1, salary2):
        self.presence_sleep_dcr(user['Edit Basic Salary1'])
        self.is_click(user['Edit Basic Salary1'])
        self.input_text(user['Edit Basic Salary1'], salary1)
        self.is_click(user['Edit Basic Salary2'])
        self.input_text(user['Edit Basic Salary2'], salary2)


if __name__ == '__main__':
    pass
