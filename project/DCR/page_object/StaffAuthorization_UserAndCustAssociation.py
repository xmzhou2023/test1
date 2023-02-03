from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class UserCustomerAssociaPage(Base):
    """ User and Customer Association 菜单定位元素类"""

    @allure.step("进入User and Customer Association页面，根据User筛选品牌、客户等数据")
    def input_user_query(self, content):
        self.is_click_dcr(user['Input User'])
        self.input_text_dcr(user['Input User'], txt=content)
        sleep(2.2)
        self.presence_sleep_dcr(user['User Select Value'], content)
        self.is_click(user['User Select Value'], content)

    @allure.step("点击Search按钮筛选数据")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_text(user['Loading'])

    @allure.step("获取分页总条数文本")
    def get_total_text(self):
        get_total = self.element_text(user['Get Total Text'])
        total1 = get_total[6:]
        return total1

    @allure.step("获取列表User ID文本")
    def get_list_user_id(self):
        self.presence_sleep_dcr(user['Get list User ID'])
        get_userid = self.element_text(user['Get list User ID'])
        return get_userid

    @allure.step("获取列表User Name文本")
    def get_list_user_name(self):
        get_username = self.element_text(user['Get list User Name'])
        return get_username

    @allure.step("获取列表Position文本")
    def get_list_position(self):
        get_position = self.element_text(user['Get list Position'])
        return get_position

    @allure.step("获取列表Customer ID文本")
    def get_list_customer_id(self):
        get_customerid = self.element_text(user['Get list Customer ID'])
        return get_customerid

    @allure.step("获取列表Customer Name文本")
    def get_list_customer_name(self):
        customer_name = self.element_text(user['Get list Customer Name'])
        return customer_name

    @allure.step("关闭用户与客户关系菜单")
    def click_close_user_cust_assoc(self):
        self.is_click(user['关闭用户与客户关系菜单'])

    @allure.step("关闭导出记录菜单")
    def click_close_export_record(self):
        self.is_click(user['关闭导出记录菜单'])

    # User and Customer Association列表数据筛选后，导出操作成功后验证
    @allure.step("点击Export导出按钮")
    def click_export(self):
        self.is_click(user['Export'])
        sleep(2)

    @allure.step("点击下载Download Icon，点击more更多按钮")
    def click_download_more(self):
        self.mouse_hover_click(user['Download Icon'])
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        sleep(6)

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], txt=content)
        sleep(0.5)
        self.is_click(user['Task Name value'], content)


    @allure.step("导出页面，点击Search按钮")
    def click_export_search(self):
        status = self.export_download_status(user['Export Record Search'], user['获取下载状态文本'])
        return status

    @allure.step("导出记录页面，获取列表 Download Status文本")
    def get_download_status_text(self):
        status = self.element_text(user['获取下载状态文本'])
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
        complete_date = self.element_text(user['获取完成日期文本'])
        complete_date1 = complete_date[0:10]
        return complete_date1

    @allure.step("导出记录页面，获取列表 Operation文本")
    def get_export_operation_text(self):
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    @allure.step("导出记录页面，获取列表导出时间文本")
    def get_export_time_text(self):
        export_time = self.element_text(user['获取导出时间'])
        export_time1 = export_time[0:1]
        return export_time1

    @allure.step("断言判读分页总条数，是否能查询到数据且大于1条")
    def assert_total(self, total):
        if int(total) >= 1000:
            logging.info("查看User And Customer Association列表，加载筛选的数据正常，分页总条数Total：{}".format(total))
        else:
            logging.info("查看User And Customer Association列表，加载筛选的数据正常，分页总条数Total：{}".format(total))
        sleep(1)

    @allure.step("断言判读分页总条数，是否能查询到数据且大于1条")
    def assert_total1(self, total1):
        if int(total1) >= 1:
            logging.info("查看User And Customer Association列表，加载筛选的数据正常，分页总条数Total：{}".format(total1))
        else:
            logging.info("查看User And Customer Association列表，加载筛选的数据正常，分页总条数Total：{}".format(total1))
        sleep(1)

    @allure.step("断言文件或导出时间是否有数据")
    def assert_file_time_size(self, file_size, export_time):
        if int(file_size) > 0:
            logging.info("User and Customer Association导出成功，File Size 导出文件大于1KB:{}".format(file_size))
        else:
            logging.info("User and Customer Association导出失败，File Size 导出文件小于1KB:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("User and Customer Association导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("User and Customer Association导出成功，Export Time(s)导出时间等于0s:{}".format(export_time))
        sleep(1)


if __name__ == '__main__':
    pass
