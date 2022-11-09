from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from libs.config.conf import BASE_DIR
from ..test_case.conftest import *
import random

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class UserManagementPage(Base):
    """UserManagementPage 页面元素类"""

    @allure.step("user management页面，点击Add新增按钮")
    def click_add_user(self):
        self.is_click(user['Add'])
        sleep(2.5)

    @allure.step("进入Add user页面， 选择传音员工类型")
    def click_staff_type_value(self, type1):
        self.presence_sleep_dcr(user['Staff Type'])
        self.is_click(user['Staff Type'])
        sleep(1)
        self.is_click(user['Transsion Staff'], type1)

    @allure.step("Add user页面， 输入user ID字段")
    def input_user_id(self, content):
        self.is_click(user['User ID'])
        self.input_text_dcr(user['User ID'], txt=content)

    @allure.step("Add user页面， 输入user Name字段")
    def input_user_name(self, content):
        self.presence_sleep_dcr(user['User Name'])
        self.is_click(user['User Name'])
        self.input_text(user['User Name'], txt=content)

    @allure.step("Add user页面，点击user Name属性，释放光标")
    def click_user_name(self):
        self.is_click(user['User Name'])

    @allure.step("Add user页面， 输入销售区域，然后选中输入的销售区域")
    def input_sales_region(self, content):
        self.is_click(user['Sales Region'])
        self.input_text(user['Sales Region'], txt=content)
        sleep(2)
        self.is_click(user['Sales Region Value'])

    @allure.step("Add user页面， 输入国家城市，然后选中输入的国家城市")
    def input_country_city(self, content):
        self.is_click(user['Country City'])
        self.input_text(user['Country City'], txt=content)
        sleep(2)
        self.is_click(user['Country City Value'])

    @allure.step("Add user页面，选择点击品牌")
    def click_select_brand(self):
        self.is_click(user['Add Select Brand'])
        sleep(1)
        self.presence_sleep_dcr(user['Select Brand Value'], 'Infinix')
        self.is_click(user['Select Brand Value'], 'Infinix')
        self.is_click(user['Select Brand Value'], 'TECNO')
        self.is_click(user['Select Brand Value'], 'itel')


    @allure.step("关闭User Management菜单")
    def click_close_user_mgt(self):
        self.is_click(user['关闭用户管理菜单'])
        sleep(1)

    @allure.step("Edit user页面，选择点击品牌")
    def click_edit_trans_brand(self):
        self.is_click(user['Edit Select Brand'])
        sleep(1)
        self.presence_sleep_dcr(user['Select Brand Value'], 'oraimo')
        self.is_click(user['Select Brand Value'], 'oraimo')

    @allure.step("Edit user页面，选择点击品牌")
    def click_edit_dealer_brand(self):
        self.is_click(user['Edit Select Brand'])
        sleep(1)
        self.presence_sleep_dcr(user['Select Brand Value'], 'Infinix')
        self.is_click(user['Select Brand Value'], 'Infinix')

    @allure.step("Add user页面，输入职位，选中输入的职位")
    def input_position_transsion(self, content):
        self.is_click(user['Position'])
        self.input_text(user['Position'], txt=content)
        sleep(1)
        self.presence_sleep_dcr(user['Position Value Transsion'], content)
        self.is_click(user['Position Value Transsion'], content)

    @allure.step("Add user页面，输入上级领导，选中输入的上级领导")
    def input_superior(self, content):
        self.is_click(user['Superior'])
        self.input_text(user['Superior'], txt=content)
        sleep(2.5)
        self.presence_sleep_dcr(user['Superior Value'], "lhmadmin lhmadmin")
        self.is_click(user['Superior Value'], "lhmadmin lhmadmin")

    @allure.step("Add user页面，输入邮箱")
    def input_email(self, content):
        self.is_click(user['Email'])
        self.input_text(user['Email'], txt=content)

    @allure.step("Add user页面，输入联系电话")
    def input_contact_no(self, content):
        self.input_text(user['Contact No'], txt=content)

    @allure.step("Add user页面，选择性别")
    def click_gender_female(self, context):
        self.is_click(user['Gender'])
        sleep(1)
        self.presence_sleep_dcr(user['Gender Female'], context)
        self.is_click(user['Gender Female'], context)

    @allure.step("Add user页面，点击Submit提交按钮")
    def click_add_user_submit(self):
        self.is_click(user['Add User Submit'])
        sleep(1.5)

    @allure.step("获取列表User ID文本内容")
    def get_text_user_id(self):
        sleep(1.5)
        userid = self.element_text(user['获取列表文本User ID'])
        return userid

    @allure.step("'获取列表User Name文本内容")
    def get_text_user_name(self):
        username = self.element_text(user['获取列表文本User Name'])
        return username

    @allure.step("点击搜索功能")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(4)

    @allure.step("点击重置按钮")
    def click_reset(self):
        self.is_click(user['Reset'])
        sleep(3)


    """编辑用户时，筛选用户"""
    @allure.step("用户管理列表页面，筛选User，进行编辑或者删除")
    def input_query_User(self, userid):
        self.is_click_dcr(user['点击筛选用户输入框'])
        self.input_text_dcr(user['点击筛选用户输入框'], userid)
        sleep(3)
        self.is_click(user['Input User ID Value'], userid)

    @allure.step("点击编辑功能")
    def click_edit(self):
        self.presence_sleep_dcr(user['修改第一个Edit'])
        self.is_click_dcr(user['修改第一个Edit'])
        sleep(2)

    @allure.step("点击第一个checkbox,对用户进行辞职操作")
    def click_first_checkbox(self):
        self.is_click_dcr(user['勾选第一个复选框'])

    @allure.step("编辑用户提交成功提示语")
    def get_set_up_successfully(self):
        set_up_success = self.element_text(user['Set Up Successfully'])
        return set_up_success

    @allure.step("点击更多操作,点击离职功能")
    def click_more_option_quit(self):
        self.is_click(user['More Option'])
        sleep(2)
        self.presence_sleep_dcr(user['Quit'])
        self.is_click(user['Quit'])
        sleep(2)
        self.is_click_dcr(user['确认删除Yes'])

    @allure.step("获取无数据文本")
    def get_text_nodata(self):
        nodata = self.element_text(user['No Data'])
        return nodata

    @allure.step("获取删除成功提示语文本内容")
    def get_text_delete_success(self):
        del_success = self.element_text(user['Disabled Successfully'])
        return del_success


    @allure.step("进入Add user页面， 输入客户ID")
    def input_belong_to_cust(self, content):
        self.is_click(user['Belong To Customer'])
        self.input_text(user['Belong To Customer'], txt=content)
        sleep(2)
        self.is_click(user['Belong To Customer Value'], "UG4019912")

    @allure.step("随机生成userid")
    def user_id_random(self):
        num = str(random.randint(100, 999))
        userid = '19851' + num
        return userid

    @allure.step("随机生成username")
    def user_name_random(self):
        num = str(random.randint(100, 999))
        username = "user_test" + num
        return username

    @allure.step("随机生成电话号码尾号")
    def number_radom(self):
        num = str(random.randint(100, 999))
        return num

    @allure.step("Add user页面，输入职位，选中输入的职位")
    def input_position_dealer(self, content):
        self.is_click(user['Position'])
        self.input_text(user['Position'], txt=content)
        sleep(1)
        self.is_click(user['Position Value Dealer'], content)


    """查询列表用户"""
    @allure.step("用户管理页面，获取列表文本内容方法")
    def input_get_data(self, data):
        self.presence_sleep_dcr(user[data])
        get_data = self.element_text(user[data])
        return get_data

    @allure.step("用户管理页面，获取列表Total分页总数")
    def get_total(self):
        get_total = self.element_text(user['Get Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("断言分页总数是否存在数据")
    def assert_total(self, total):
        if int(total) > 1000:
            logging.info("查看用户管理列表，分页总条数大于1000，用户总记录Total：{}".format(total))
        else:
            logging.info("查看用户管理列表，分页总条数小于1000，用户总记录Total：{}".format(total))


    """用户重置密码"""
    @allure.step("点击重置密码及重置密码确认功能")
    def click_more_reset_password(self):
        self.is_click(user['More Option'])
        sleep(2)
        self.presence_sleep_dcr(user['Reset Password'])
        self.is_click(user['Reset Password'])
        sleep(1.4)
        self.presence_sleep_dcr(user['Reset Password Yes'])
        self.is_click(user['Reset Password Yes'])

    @allure.step("登录时，弹出设置新密码窗口，获取New Password 标签")
    def get_new_password_label(self):
        get_new_password = self.element_text(user['Get New Password'])
        return get_new_password


    @allure.step("重置密码成功后，该用户登录时，弹出设置新密码窗口，输入新密码与确认新密码，并点击保存按钮")
    def input_new_password_save(self, new_password):
        self.is_click(user['Input New Password'])
        self.input_text(user['Input New Password'], txt=new_password)
        sleep(1)
        self.is_click(user['Input Confirm Password'])
        self.input_text(user['Input Confirm Password'], txt=new_password)
        sleep(0.5)
        self.is_click(user['New Password Save'])

    @allure.step("输入新密码登录，点击OK")
    def click_save_successfully_ok(self):
        self.is_click(user['Save successfully OK'])
        sleep(2)

    @allure.step("登录页面，输入新设置的密码")
    def input_login_password(self, password):
        self.is_click(user['login Input Password'])
        self.input_text(user['login Input Password'], txt=password)

    @allure.step("登录页面，点击Login登录按钮")
    def click_login(self):
        self.is_click(user['Click Login'])
        sleep(3.5)


    """导入用户操作"""
    @allure.step("User Management页面，点击Import 按钮")
    def click_import(self):
        self.is_click(user['Import Button'])
        sleep(1.5)

    @allure.step("User Management页面，点击Import Save 按钮")
    def click_import_save(self):
        self.is_click(user['Import Save'])

    @allure.step("User Management页面，点击Import 导入功能")
    def click_import_upload_save(self, file1):
        self.is_click(user['Add Upload'])
        sleep(4)
        ele = self.driver.find_element('xpath', "//button//..//input[@name='file']")
        ele.send_keys(file1)
        sleep(3)
        self.is_click(user['Import Save'])
        sleep(2)
        self.presence_sleep_dcr(user['Upload Confirm'])
        self.is_click(user['Upload Confirm'])


    @allure.step("User Management页面，获取Total分页总条数")
    def get_list_total(self):
        self.presence_sleep_dcr(user['Get Total'])
        get_total = self.element_text(user['Get Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("User Management页面，导入前获取列表筛选的User ID，如果能筛选到1条记录，先删除已存在的用户")
    def delete_repetitive_user(self):
        sql1 = SQL('DCR', 'test')
        try:
            varsql1 = "select USER_CODE from t_user where USER_CODE ='smarttest102'"
            varsql2 = "select EMP_CODE from t_employee where EMP_CODE ='smarttest102'"
            result_user = sql1.query_db(varsql1)
            result_emp = sql1.query_db(varsql2)
            user_code = result_user[0].get("USER_CODE")
            emp_code = result_emp[0].get("EMP_CODE")
            if user_code == 'smarttest102':
                """ 在数据库表中，删除导入的用户 """
                sql1.delete_db(
                    "delete from t_user where USER_CODE ='smarttest102'")
            elif emp_code == 'smarttest102':
                sql1.delete_db(
                    "delete from t_employee where EMP_CODE ='smarttest102'")
            else:
                logging.info("获取User Management页面user_code与emp_code字段内容：{}".format(user_code, emp_code))
        except Exception as e:
            logging.info("如有异常打印日志{}".format(e))


    @allure.step("导入用户模板-上传正确的文件")
    def upload_true_file(self, file1):
        path1 = os.path.join(BASE_DIR, 'project', 'DCR', 'data', file1)
        logging.info("打印上传的用户模板文件path：{}".format(path1))
        self.click_import_upload_save(path1)

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

    @allure.step("User Management页面页面，获取列表Brand字段内容")
    def get_list_brand(self):
        get_brand = self.element_text(user['Get list Brand'])
        return get_brand

    @allure.step("User Management页面页面，获取列表 Country字段内容")
    def get_list_country(self):
        sleep(1.5)
        self.scroll_into_view(user['Get list Country'])
        get_country = self.element_text(user['Get list Country'])
        return get_country

    @allure.step("User Management页面页面，获取列表 Position字段内容")
    def get_list_position(self):
        sleep(1.5)
        self.scroll_into_view(user['Get list Position'])
        get_position = self.element_text(user['Get list Position'])
        return get_position

    @allure.step("User Management页面页面，获取列表 Staff Status字段内容")
    def get_list_staff_status(self):
        get_staff_status = self.element_text(user['Get list Staff Status'])
        return get_staff_status

    """导出用户"""
    @allure.step("User Management页面，点击Export 导出用户记录")
    def click_export(self):
        self.is_click(user['Export'])
        sleep(1.5)

    @allure.step("User Management页面，导出操作后，点击右上角下载图标,点击右上角more...")
    def click_download_more(self):
        self.is_click(user['Download Icon'])
        sleep(2)
        self.presence_sleep_dcr(user['More'])
        self.is_click(user['More'])
        sleep(3)

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], txt=content)
        sleep(2)
        self.is_click(user['Task Name value'], content)

    @allure.step("循环点击查询，直到获取到下载状态为COMPLETE")
    def click_export_search(self):
        download_status = self.export_download_status(user['Export Record Search'], user['获取下载状态文本'])
        return download_status

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
        complete_date = self.element_text(user['获取完成日期文本'])
        complete_date1 = complete_date[0:10]
        return complete_date1

    @allure.step("导出记录页面，获取列表 Operation文本")
    def get_operation_text(self):
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    @allure.step("导出记录页面，获取列表导出时间文本")
    def get_export_time_text(self):
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
        sleep(1)

    @allure.step("关闭导出记录菜单")
    def click_close_export_record(self):
        """关闭导出记录菜单"""
        self.is_click(user['关闭导出记录菜单'])
        sleep(1)


if __name__ == '__main__':
    pass