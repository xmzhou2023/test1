import logging
from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AttendanceStatistics(Base):
    @allure.step("Attendance Statistics页面，输入User筛选考勤统计记录")
    def input_user_query(self, user1):
        self.is_click(user['筛选用户'])
        self.input_text(user['输入筛选用户'], user1)
        sleep(2)
        self.presence_sleep_dcr(user['选中筛选用户'], user1)
        self.is_click(user['选中筛选用户'], user1)

    @allure.step("Attendance Statistics页面，输入Position 筛选考勤统计记录")
    def input_position_query(self, position):
        self.is_click(user['筛选职位'])
        self.input_text_dcr(user['输入筛选职位'], position)
        sleep(2)
        self.presence_sleep_dcr(user['选中筛选职位'], position)
        self.is_click(user['选中筛选职位'], position)
        self.click_position_label()

    @allure.step("Attendance Statistics页面，根据用户和职位筛选 考勤统计记录")
    def query_attendance_statistics(self, user1, position):
        self.input_user_query(user1)
        self.input_position_query(position)
        self.click_search()


    @allure.step("Attendance Statistics页面，点击Search查询按钮")
    def click_search(self):
        self.is_click(user['考勤统计Search'])
        sleep(2.5)

    @allure.step("Attendance Statistics页面，点击position 标签释放光标")
    def click_position_label(self):
        self.is_click(user['Click Position Label'])

    @allure.step("Attendance Statistics页面，获取列表 Brand字段文本")
    def get_list_brand(self):
        get_brand = self.element_text(user['Get list Brand'])
        return get_brand

    @allure.step("Attendance Statistics页面，获取列表 User ID字段文本")
    def get_list_user_id(self):
        get_user_id = self.element_text(user['Get list User ID'])
        return get_user_id

    @allure.step("Attendance Statistics页面，获取列表 User Name字段文本")
    def get_list_user_name(self):
        get_user_name = self.element_text(user['Get list User Name'])
        return get_user_name

    @allure.step("Attendance Statistics页面，获取列表 Position字段文本")
    def get_list_position(self):
        get_position = self.element_text(user['Get list Position'])
        return get_position

    @allure.step("Attendance Statistics页面，获取列表 Normal字段文本")
    def get_list_normal(self):
        get_normal = self.element_text(user['Get list Normal'])
        return get_normal

    @allure.step("Attendance Statistics页面，获取列表 Absence字段文本")
    def get_list_absence(self):
        get_absence = self.element_text(user['Get list Absence'])
        return get_absence

    @allure.step("Attendance Statistics页面，获取列表 Late字段文本")
    def get_list_late(self):
        get_late = self.element_text(user['Get list Late'])
        return get_late

    @allure.step("Attendance Statistics页面，获取列表 Leave early字段文本")
    def get_list_leave_early(self):
        get_leave_early = self.element_text(user['Get list Leave early'])
        return get_leave_early

    @allure.step("Attendance Statistics页面，获取Total分页总条数文本")
    def get_total_text(self):
        get_total = self.element_text(user['Get Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("断言获取分页功能的总条数是否大于0条")
    def assert_total(self, total):
        if int(total) > 0:
            logging.info("Attendance Statistics页面，获取分页功能Total总条数:{}".format(total))
        else:
            logging.info("Attendance Statistics页面，获取分页功能Total总条数:{}".format(total))


if __name__ == '__main__':
    pass
