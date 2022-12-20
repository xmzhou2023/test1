import time
import random
import allure
from public.base.basics import Base, sleep
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from libs.config.conf import BASE_DIR
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class CustomerManagementPage(Base):
    @allure.step("点击新增Add按钮")
    def click_add(self):
        self.is_click(user['Add'])

    @allure.step("随机生成客户名称")
    def cus_name_random(self):
        num = str(random.randint(100, 999))
        cus_name = 'C_test' + num
        return cus_name

    @allure.step("随机生成邮箱地址")
    def email_random(self):
        num = str(random.randint(100, 999))
        email = str("lhm" + num + "qq.com")
        return email

    @allure.step("随机生成联系人")
    def contact_name_random(self):
        num = str(random.randint(100, 999))
        contact_name = str("test_lhm" + num)
        return contact_name

    @allure.step("随机生成联系电话")
    def contact_no_random(self):
        num = str(random.randint(100, 999))
        contact_no = str("13873245" + num)
        return contact_no


    @allure.step("新增表单")
    def input_form_basic_info(self, flag, brand1, brand2, cname, region, sapid=None):
        """选择点击客户类型属性"""
        self.is_click(user['Customer Type'])
        self.is_click(user['Customer Type Select'], flag)
        """选择点击品牌属性"""
        self.is_click(user['Brand'])
        self.is_click(user['Brand Select'], brand1)
        self.is_click(user['Brand Select'], brand2)
        self.is_click(user['Brand finish'])
        self.is_click(user['Brand finish'])
        """输入客户名称属性"""
        self.is_click(user['Customer Name'])
        self.input_text(user['Customer Name'], cname)
        """输入销售区域属性"""
        self.is_click(user['Sales Region'])
        self.input_text(user['Sales Region'], region)
        sleep(2)
        self.is_click(user['Sales Region Select'], region)
        """如果客户类型为Distributor,则输入SAP Customer ID参数，否则为空 """
        if flag == 'Distributor':
            self.input_text(user['SAP Customer ID'], sapid)
        """点击客户等级属性"""
        self.is_click(user['Customer Grade'])
        self.is_click(user['Customer Grade Select'], 'B')
        sleep(0.8)
        """选择销售业务类型属性"""
        self.is_click(user['Business Type'])
        sleep(1.5)
        self.is_click(user['Business Type Selecte'], 'Retail&Wholesale')

    @allure.step("新增表单")
    def input_form_contact_info(self, contact_name, contact_no, email, country, addresss):
        self.input_text(user['Contact Name'], contact_name)
        self.input_text(user['Contact No'], contact_no)
        self.input_text(user['Email'], email)
        self.is_click(user['Country'])
        self.input_text(user['Country'], country)
        sleep(1)
        self.is_click(user['Country Select'], country)
        self.input_text(user['Customer Address'], addresss)
        self.is_click(user['Add Submit'])
        sleep(1)


    @allure.step("客户列表页面，根据客户ID条件筛选客户信息")
    def input_customer_query(self, customer_id):
        self.is_click_dcr(user['筛选Customer'])
        self.input_text_dcr(user['筛选Customer'], customer_id)
        sleep(2.5)
        self.presence_sleep_dcr(user['筛选Customer Select'], customer_id)
        self.is_click(user['筛选Customer Select'], customer_id)

    @allure.step("客户列表页面，点击Search 查询按钮")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(3)

    @allure.step("客户列表页面，点击Reset 重置按钮")
    def click_reset(self):
        self.is_click(user['Reset'])
        sleep(4.5)

    @allure.step("获取新增客户ID")
    def get_customer_id(self):
        self.presence_sleep_dcr(user['Get list Customer Id'])
        c_id = self.element_text(user['Get list Customer Id'])
        return c_id

    @allure.step("获取新增客户Name")
    def get_customer_name(self):
        c_name = self.element_text(user['Get list Customer Name'])
        return c_name

    @allure.step("获取新增客户Brand")
    def get_list_new_brand(self):
        c_brand = self.element_text(user['Get list New Brand'], 'Infinix,TECNO')
        return c_brand

    @allure.step("获取新增客户类型")
    def get_customer_type(self, type1):
        customer_type = self.element_text(user['Get Customer Type'], type1)
        return customer_type


    @allure.step("获取客户管理列表的，字段文本")
    def get_list_field(self, flag):
        get_field = self.element_text(user[flag])
        return get_field

    @allure.step("获取客户管理列表的，Total总页数")
    def get_list_total(self):
        get_total = self.element_text(user['Get Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("断言分页总数是否存在数据")
    def assert_total1(self, total):
        if int(total) >= 1:
            logging.info("查看客户管理列表，分页总条数大于等于1，能查询到客户信息Total：{}".format(total))
        else:
            logging.info("查看客户管理列表，分页总条数为Total：{}".format(total))

    @allure.step("断言分页总数是否存在数据")
    def assert_total2(self, total):
        if int(total) > 1000:
            logging.info("查看客户管理列表，分页总条数大于1000，能查询到客户信息Total：{}".format(total))
        else:
            logging.info("查看客户管理列表，分页总条数为Total：{}".format(total))

    @allure.step("获取新增客户的Contact Name")
    def get_contact_name(self):
        sleep(1.5)
        self.scroll_into_view(user['Get Contact Name'])
        contact_name = self.element_text(user['Get Contact Name'])
        return contact_name

    @allure.step("获取新增客户的Contact No")
    def get_contact_no(self):
        contact_no = self.element_text(user['Get Contact No'])
        return contact_no

    @allure.step("关闭客户管理菜单")
    def click_close_customer_mgt(self):
        self.is_click(user['关闭客户管理菜单'])

    @allure.step("修改编辑二代表单,客户名称、联系人、联系电话")
    def edit_form_info(self, edit_c_name, edit_contact_name, edit_contact_no):
        self.is_click_dcr(user['Edit'])
        sleep(1.5)
        self.presence_sleep_dcr(user['Customer Name'], edit_c_name)
        self.input_text(user['Customer Name'], edit_c_name)
        self.input_text(user['Contact Name'], edit_contact_name)
        self.input_text(user['Contact No'], edit_contact_no)
        self.is_click(user['Edit Submit'])
        sleep(4)

    @allure.step("删除新建的客户")
    def delete_customer(self):
        self.is_click_dcr(user['CheckBox'])
        self.is_click(user['More Options'])
        sleep(2)
        self.presence_sleep_dcr(user['Delete'])
        self.is_click(user['Delete'])
        sleep(1.5)
        self.presence_sleep_dcr(user['Delete Confirm'])
        self.is_click(user['Delete Confirm'])

    @allure.step("删除有绑定订单数据的客户不能被删除")
    def delete_have_records_customer(self):
        self.is_click_dcr(user['CheckBox'])
        self.is_click(user['More Options'])
        sleep(1.7)
        self.presence_sleep_dcr(user['Delete'])
        self.is_click(user['Delete'])
        sleep(1.5)
        self.presence_sleep_dcr(user['Delete Confirm'])
        self.is_click(user['Delete Confirm'])
        sleep(2)
        DomAssert(self.driver).assert_att("The following customers have delivery or receipt records and cannot be deleted!")
        self.is_click_dcr(user['Delete Tips Close'])


    @allure.step("关闭导出记录菜单")
    def click_close_export_record(self):
        self.is_click(user['关闭导出记录菜单'])


    @allure.step("点击启用按钮")
    def click_more_option_enable(self):
        sleep(1)
        self.is_click_dcr(user['CheckBox'])
        self.is_click(user['More Options'])
        sleep(2)
        self.is_click(user['Enable'])
        sleep(1.5)
        self.presence_sleep_dcr(user['Enable Confirm'])
        self.is_click(user['Enable Confirm'])

    @allure.step("点击禁用按钮")
    def click_more_option_disable(self):
        sleep(1)
        self.is_click_dcr(user['CheckBox'])
        self.is_click(user['More Options'])
        sleep(2)
        self.is_click(user['Disable'])
        sleep(1.5)
        self.presence_sleep_dcr(user['Disable Yes'])
        self.is_click_dcr(user['Disable Yes'])

    @allure.step("客户列表，获取列表状态字段内容")
    def get_list_status(self, status):
        sleep(2)
        self.scroll_into_view(user['Get list Status'], status)
        get_status = self.element_text(user['Get list Status'], status)
        return get_status


    """导入用户操作"""
    @allure.step("Customer Management页面，点击Import 按钮")
    def click_import(self):
        self.is_click(user['Import Button'])
        sleep(1.5)

    @allure.step("Customer Management页面，点击Import Save 按钮")
    def click_import_save(self):
        self.is_click(user['Import Save'])

    @allure.step("Customer Management页面，点击Import 导入功能")
    def click_import_upload_save(self, file1):
        self.is_click(user['Add Upload'])
        sleep(4)
        ele = self.driver.find_element('xpath', "//button//..//input[@name='file']")
        ele.send_keys(file1)
        sleep(1.5)
        self.is_click(user['Import Save'])
        sleep(2)
        self.presence_sleep_dcr(user['Upload Confirm'])
        self.is_click(user['Upload Confirm'])
        sleep(1)

    @allure.step("导入客户模板-上传正确的文件")
    def upload_true_file(self, file1):
        path1 = os.path.join(BASE_DIR, 'project', 'DCR', 'data', file1)
        logging.info("打印上传的客户模块文件path：{}".format(path1))
        self.click_import_upload_save(path1)

    @allure.step("Import Record页面，点击Search 查询按钮")
    def click_import_record_search(self):
        self.is_click(user['Search'])
        sleep(1.7)


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

    @allure.step("Customer Management页面，获取列表 Brand字段文本")
    def get_list_brand(self):
        self.presence_sleep_dcr(user['Get list Brand'])
        get_brand = self.element_text(user['Get list Brand'])
        return get_brand


    """导出客户记录"""
    @allure.step("Customer Management页面，点击导出按钮")
    def click_export(self):
        self.is_click(user['Export'])
        sleep(2)

    @allure.step("Customer Management页面，导出操作后，点击右上角下载图标,点击右上角more...")
    def click_download_more(self):
        self.mouse_hover_click(user['Download Icon'])
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        sleep(2)


    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], txt=content)
        sleep(0.5)
        self.is_click_dcr(user['Task Name value'], content)

    @allure.step("循环点击查询，直到获取到下载状态为COMPLETE")
    def click_export_search(self):
        download_status = self.export_download_status(user['Export Record Search'], user['获取下载状态文本'])
        return download_status

    @allure.step("导出记录页面，获取列表 Download Status文本")
    def get_download_status_text(self):
        status = self.find_element(user['获取下载状态文本'])
        while status != "COMPLETE":
            status = self.element_text(user['获取下载状态文本'])
            sleep(1)
        return status

    @allure.step("导出记录页面，获取列表 Task Name文本")
    def get_task_name_text(self):
        task_name = self.element_text(user['获取任务名称文本'])
        return task_name

    @allure.step("导出记录页面，获取列表 Task Name文本")
    def get_file_size_text(self):
        file_size = self.element_text(user['获取文件大小文本'])
        file_size1 = file_size[0:1]
        return file_size1

    @allure.step("导出记录页面，获取列表 User ID文本")
    def get_task_user_id_text(self):
        user_id = self.element_text(user['获取用户ID文本'])
        return user_id

    @allure.step("导出记录页面，获取列表 Create Date文本")
    def get_create_date_text(self):
        self.scroll_into_view(user['获取创建日期文本'])
        create_date = self.element_text(user['获取创建日期文本'])
        create_date1 = create_date[0:10]
        return create_date1

    @allure.step("导出记录页面，获取列表Complete Date文本")
    def get_complete_date_text(self):
        self.scroll_into_view(user['获取完成日期文本'])
        complete_date = self.element_text(user['获取完成日期文本'])
        complete_date1 = complete_date[0:10]
        return complete_date1

    @allure.step("导出记录页面，获取列表 Operation文本")
    def get_operation_text(self):
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    @allure.step("导出记录页面，获取列表导出时间文本")
    def get_export_time_text(self):
        self.scroll_into_view(user['获取导出时间'])
        export_time = self.element_text(user['获取导出时间'])
        export_time1 = export_time[0:1]
        return export_time1

    @allure.step("断言分页总数是否存在数据")
    def assert_total(self, total):
        if int(total) > 0:
            logging.info("筛选考勤记录列表，分页总条数大于0，能查询到考勤记录数Total:{}".format(total))
        else:
            logging.info("筛选考勤记录列表，分页总条数为0，未查询到考勤记录数Total:{}:".format(total))

    @allure.step("断言分页总数是否存在数据")
    def assert_total2(self, total):
        if int(total) > 1000:
            logging.info("查看考勤记录列表，分页总条数大于1000，能查询到考勤记录Total：{}".format(total))
        else:
            logging.info("查看考勤记录列表，分页总条数为1000，未查询到考勤记录Total：{}".format(total))

    @allure.step("断言文件或导出时间是否有数据")
    def assert_file_time_size(self, file_size, export_time):
        if int(file_size) > 0:
            logging.info("Attendance Records导出成功，File Size导出文件大于M:{}".format(file_size))
        else:
            logging.info("Attendance Records导出失败，File Size导出文件小于M:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("Attendance Records导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("Attendance Records导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))

if __name__ == '__main__':
    pass
