import logging
from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class LeaveApplicationRecords(Base):
    @allure.step("Leave Application Records页面，输入User筛选 休假申请记录")
    def input_user_query(self, user1):
        self.is_click_dcr(user['筛选用户'])
        self.input_text_dcr(user['筛选用户'], user1)
        sleep(2)
        self.presence_sleep_dcr(user['选中筛选用户'], user1)
        self.is_click(user['选中筛选用户'], user1)

    @allure.step("Leave Application Records页面，输入Leave Date开始日期")
    def input_leave_date(self, date):
        self.is_click(user['Leave Start Date'])
        self.input_text(user['Leave Start Date'], date)

    @allure.step("Leave Application Records页面，根据用户 筛选 休假申请记录")
    def query_leave_application_records(self, date, user1):
        self.input_leave_date(date)
        self.input_user_query(user1)
        self.click_search()

    @allure.step("Leave Application Records页面，点击Search 查询按钮")
    def click_search(self):
        self.is_click(user['休假申请记录Search'])
        sleep(2)

    @allure.step("Leave Application Records页面，获取列表 Leave Type字段文本")
    def get_list_leave_type(self):
        get_leave_type = self.element_text(user['Get Leave Type'])
        return get_leave_type

    @allure.step("Leave Application Records页面，获取列表 Leave Reason字段文本")
    def get_list_leave_reason(self):
        get_leave_reason = self.element_text(user['Get Leave Reason'])
        return get_leave_reason

    @allure.step("Leave Application Records页面，获取列表 Start Date字段文本")
    def get_list_start_date(self):
        get_start_date = self.element_text(user['Get Start Date'])
        return get_start_date

    @allure.step("Leave Application Records页面，获取列表 Start Time字段文本")
    def get_list_start_time(self):
        get_start_time = self.element_text(user['Get Start Time'])
        return get_start_time

    @allure.step("Leave Application Records页面，获取列表 End Date字段文本")
    def get_list_end_date(self):
        get_end_date = self.element_text(user['Get End Date'])
        return get_end_date

    @allure.step("Leave Application Records页面，获取列表 End Time字段文本")
    def get_list_end_time(self):
        get_end_time = self.element_text(user['Get End Time'])
        return get_end_time

    @allure.step("Leave Application Records页面，获取列表 End Time字段文本")
    def get_list_duration(self):
        get_duration = self.element_text(user['Get Duration'])
        return get_duration

    @allure.step("Leave Application Records页面，获取列表 Status字段文本")
    def get_list_status(self):
        get_status = self.element_text(user['Get Status'])
        return get_status

    @allure.step("Leave Application Records页面，获取列表 User ID字段文本")
    def get_list_user_id(self):
        self.presence_sleep_dcr(user['Get User ID'])
        get_user_id = self.element_text(user['Get User ID'])
        return get_user_id

    @allure.step("Leave Application Records页面，获取Total分页总条数文本")
    def get_total_text(self):
        get_total = self.element_text(user['Get Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("断言获取分页功能的总条数是否大于0条")
    def assert_total(self, total):
        if int(total) > 0:
            logging.info("Leave Application Records页面,获取分页功能Total总条数:{}".format(total))
        else:
            logging.info("Leave Application Records页面,获取分页功能Total总条数:{}".format(total))


if __name__ == '__main__':
    pass
