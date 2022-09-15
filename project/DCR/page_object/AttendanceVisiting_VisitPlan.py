import logging
from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class VisitPlan(Base):
    @allure.step("Visit Plan页面，输入User筛选，点击Search按钮查询")
    def input_shop_query_search(self, shop):
        self.presence_sleep_dcr(user['筛选门店'])
        self.is_click(user['筛选门店'])
        self.input_text(user['输入筛选用户'], shop)
        sleep(1.5)
        self.is_click(user['Search'])
        sleep(2.5)

    @allure.step("Visit Plan页面，点击 Unfold按钮")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        sleep(1.7)

    @allure.step("Visit Plan页面，点击 Fold按钮")
    def click_fold(self):
        self.is_click(user['Fold'])

    @allure.step("Visit Plan页面，获取列表Plan No文本内容")
    def get_plan_no(self):
        get_plan_no = self.element_text(user['Get list Plan No'])
        return get_plan_no

    @allure.step("Visit Plan页面，获取列表Shop Name文本内容")
    def get_list_shop_name(self):
        self.scroll_into_view(user['Get list Shop Name'])
        get_shop_name = self.element_text(user['Get list Shop Name'])
        return get_shop_name

    @allure.step("Visit Plan页面，获取列表Shop ID文本内容")
    def get_list_shop_id(self):
        self.scroll_into_view(user['Get list Shop ID'])
        get_shop_id = self.element_text(user['Get list Shop ID'])
        return get_shop_id

    @allure.step("Visit Plan页面，获取列表Status文本内容")
    def get_list_status(self):
        self.scroll_into_view(user['Get list Status'])
        get_status = self.element_text(user['Get list Status'])
        return get_status

    @allure.step("Visit Plan页面，获取列表Upload User文本内容")
    def get_list_upload_user(self):
        self.scroll_into_view(user['Get list Upload User'])
        get_upload_user = self.element_text(user['Get list Upload User'])
        return get_upload_user

    @allure.step("Visit Plan页面，获取列表 User Name文本内容")
    def get_list_user_name(self):
        self.scroll_into_view(user['Get list User Name'])
        get_user_name = self.element_text(user['Get list User Name'])
        return get_user_name

    @allure.step("Visit Plan页面，获取列表 Position文本内容")
    def get_list_position(self):
        self.scroll_into_view(user['Get list Position'])
        get_position = self.element_text(user['Get list Position'])
        return get_position

    @allure.step("Visit Plan页面，获取Total分页总条数文本")
    def get_total_text(self):
        get_total = self.element_text(user['Get list Total'])
        get_total1 = get_total[6:]
        return get_total1

    @allure.step("断言获取分页功能的总条数是否大于0条")
    def assert_total(self, total):
        if int(total) > 0:
            logging.info("Visit Plan页面,获取分页功能Total总条数:{}".format(total))
        else:
            logging.info("Visit Plan页面,获取分页功能Total总条数:{}".format(total))


if __name__ == '__main__':
    pass
