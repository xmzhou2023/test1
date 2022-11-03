import logging

from libs.common.read_element import Element
from libs.common.time_ui import sleep
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AttendanceRulesPage(Base):

    @allure.step("Attendance Rules页面,点击Add新增考勤规则按钮")
    def click_add(self):
        self.is_click(user['Add AttendanceRules'])
        sleep(1)

    def click_add_brand1(self, context1):
        self.presence_sleep_dcr(user['Add Brand'])
        self.is_click(user['Add Brand'])
        sleep(0.5)
        self.is_click(user['品牌输入项选择'], context1)

    def click_add_brand2(self, context1, context2):
        self.presence_sleep_dcr(user['Add Brand'])
        self.is_click(user['Add Brand'])
        sleep(0.5)
        self.is_click(user['品牌输入项选择'], context1)
        self.is_click(user['品牌输入项选择'], context2)

    @allure.step("Add考勤规则页面，点击选择品牌")
    def click_add_brand3(self, context1, context2, context3):
        self.presence_sleep_dcr(user['Add Brand'])
        self.is_click(user['Add Brand'])
        sleep(0.5)
        self.is_click(user['品牌输入项选择'], context1)
        self.is_click(user['品牌输入项选择'], context2)
        self.is_click(user['品牌输入项选择'], context3)

    @allure.step("Add考勤规则页面，输入国家，选中国家")
    def input_add_country(self, country):
        self.is_click(user['国家'])
        self.input_text(user['国家'], country)
        self.is_click(user['国家输入项选择'], country)

    @allure.step("Add考勤规则页面，输入国家，选中国家")
    def input_add_position(self, position):
        self.is_click(user['职位'])
        self.input_text(user['职位输入'], position)
        self.is_click(user['职位输入项选择'], position)

    @allure.step("Add考勤规则页面，点击开始月份，选中指定的月份")
    def click_start_month(self, month):
        self.input_text(user['开始月份'], month)

    @allure.step("Add考勤规则页面，输入remark评论")
    def input_remark(self, context):
        self.input_text(user['Remark'], context)

    @allure.step("Add考勤规则页面，点击Position标签，释放光标")
    def click_position_label(self):
        self.is_click(user['Click Position label'])

    @allure.step("Add考勤规则页面，点击On Work Time标签，释放光标")
    def click_on_work_time_label(self):
        self.is_click(user['Click On Work Time'])

    @allure.step("Add考勤规则页面，输入上班打开时间")
    def input_on_work_time(self, on_work_time):
        self.input_text(user['上班打卡时间1'], on_work_time)

    @allure.step("Add考勤规则页面，输入下班打开时间")
    def input_off_work_time(self, off_work_time):
        self.input_text(user['下班打卡时间1'], off_work_time)

    @allure.step("Add考勤规则页面，勾选检查工作时间复选框")
    def click_check_working_hours(self):
        self.is_click(user['检查工作时间'])

    @allure.step("Add考勤规则页面，点击Save保存按钮")
    def click_save(self):
        self.is_click(user['保存按钮'])
        sleep(0.5)

    @allure.step("Add考勤规则页面，点击Cancel取消保存按钮")
    def click_add_cancel(self):
        self.is_click_dcr(user['取消保存按钮'])
        sleep(1)


    """筛选考勤规则记录，对列表新增的考勤记录进行断言"""
    @allure.step("考勤规则列表页面，点击Start Month lable 释放光标位置")
    def click_start_month_label(self):
        self.is_click(user['Click Start Month lable'])

    @allure.step("考勤规则列表页面，输入country筛选项筛选 考勤规则记录")
    def input_country_query(self, context):
        self.is_click(user['Input Country query'])
        self.input_text(user['Input Country query'], context)
        sleep(0.5)
        self.presence_sleep_dcr(user['Select Country Value'], context)
        self.is_click_dcr(user['Select Country Value'], context)

    @allure.step("考勤规则列表页面，输入Start Month筛选项 筛选考勤规则记录")
    def input_start_month_query(self, context):
        self.input_text(user['Input Start Month query'], context)

    @allure.step("考勤规则列表页面，输入Start Month筛选项筛选考勤规则记录")
    def click_search(self):
        self.is_click(user['Click Search'])
        sleep(2.5)

    @allure.step("Add考勤规则页面，点击Cancel取消按钮")
    def click_cancel(self):
        self.is_click_dcr(user['Add Page Click Cancel'])
        sleep(0.6)

    @allure.step("考勤规则列表页面，获取Start Mounth字段的内容")
    def get_list_start_month(self):
        self.presence_sleep_dcr(user['Get list Start Mounth'])
        get_start_mounth = self.element_text(user['Get list Start Mounth'])
        return get_start_mounth

    @allure.step("考勤规则列表页面，获取Country 字段的内容")
    def get_list_country(self):
        get_country = self.element_text(user['Get list Country'])
        return get_country

    @allure.step("考勤规则列表页面，获取On Work Time字段的内容")
    def get_list_on_work_time(self):
        get_on_work_time = self.element_text(user['Get list On Work Time'])
        get_on_work_time1 = get_on_work_time[0:5]
        return get_on_work_time1

    @allure.step("考勤规则列表页面，获取Off Work Time字段的内容")
    def get_list_off_work_time(self):
        get_off_work_time = self.element_text(user['Get list Off Work Time'])
        get_off_work_time1 = get_off_work_time[0:5]
        return get_off_work_time1

    @allure.step("考勤规则列表页面，获取 Position 字段的内容")
    def get_list_position(self):
        self.scroll_into_view(user['Get list Position'])
        get_position = self.element_text(user['Get list Position'])
        return get_position


    """删除考勤规则记录"""
    @allure.step("考勤规则列表页面，勾选第一个复选框")
    def click_first_checkbox(self):
        self.is_click_dcr(user['勾选第一个复选框'])

    @allure.step("考勤规则列表页面，点击删除按钮，然后点击确认删除按钮")
    def click_delete_confirm(self):
        self.is_click(user['删除按钮'])
        sleep(0.8)
        self.presence_sleep_dcr(user['删除确认按钮'])
        self.is_click(user['删除确认按钮'])


    """编辑考勤规则记录"""
    @allure.step("考勤规则列表页面，点击编辑按钮")
    def click_edit(self):
        self.presence_sleep_dcr(user['编辑按钮'])
        self.is_click_dcr(user['编辑按钮'])
        sleep(1)

    """查询考勤排班记录"""
    @allure.step("考勤排班列表页面，获取Total总条数")
    def get_total(self):
        get_total = self.element_text(user['Get Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("考勤排班列表页面，断言Total分页总条数是否大于0，能查询到数据")
    def assert_total(self, total):
        if int(total) >= 1:
            logging.info("查询考勤排班页面列表，Total分页功能的总条数，大于0：{}".format(total))
        else:
            logging.info("查询考勤排班页面列表，Total分页功能的总条数，无记录：{}".format(total))

    @allure.step("考勤排班列表页面，获取操作列的 编辑按钮")
    def get_operation_edit(self):
        get_edit = self.element_text(user['编辑按钮'])
        return get_edit

    @allure.step("考勤排班列表页面，获取操作列的 删除按钮")
    def get_operation_delete(self):
        get_delete = self.element_text(user['Operation Delete'])
        return get_delete


if __name__ == '__main__':
    pass

