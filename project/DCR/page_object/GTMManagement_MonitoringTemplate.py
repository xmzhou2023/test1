from libs.common.read_element import Element
from libs.common.time_ui import sleep
from ..test_case.conftest import *
from libs.config.conf import BASE_DIR
import random

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class MonitoringTemplatePage(Base):
    @allure.step("Monitoring Template Add页面，点击Add按钮")
    def click_add_monitoring(self):
        self.is_click(user['Add Monitoring Template'])
        sleep(1.5)

    @allure.step("Monitoring Template Add页面，填写预警模板基本信息")
    def add_basic_information(self, title_name, brand, country, monitory_type, quantity, item, start_date, end_date, shop_type, image_type, manpower, frequency, position):
        self.presence_sleep_dcr(user['Title'])
        self.input_text(user['Title'], title_name)
        self.is_click(user['Brand'])
        self.is_click(user['Select Brand Value'], brand)
        self.is_click(user['Country'])
        self.input_text(user['Country'], country)
        sleep(0.5)
        self.is_click_dcr(user['Select Country Value'], country)

        """若monitory type选择Sale Monitor类型，出现Sale Quantity字段；若monitory type选择Inventory Monitory类型，出现Inventory Quantity字段"""
        if "Sale Monitor" == monitory_type:
            self.is_click(user['Monitory Type'])
            self.is_click(user['Select Monitory Type'], monitory_type)
            sleep(0.5)
            self.input_text(user['Sale Quantity'], quantity)
        elif "Inventory Monitor" == monitory_type:
            self.is_click(user['Monitory Type'])
            self.is_click(user['Select Monitory Type'], monitory_type)
            sleep(0.5)
            self.input_text(user['Inventory Quantity'], quantity)

        self.is_click_dcr(user['Item'])
        self.input_text_dcr(user['Item'], item)
        sleep(0.5)
        self.is_click(user['Select Item Value'], item)

        self.is_click(user['Enable Start Date'])
        self.input_text(user['Enable Start Date'], start_date)
        self.is_click(user['Enable End Date'])
        self.input_text(user['Enable End Date'], end_date)

        self.is_click_dcr(user['Shop Type'])
        self.input_text_dcr(user['Shop Type'], shop_type)
        sleep(0.5)
        self.is_click(user['Select Shop Type'], shop_type)

        self.is_click_dcr(user['Image Type'])
        self.is_click(user['Select Image Type'], image_type)

        self.is_click_dcr(user['Manpower Type'])
        self.is_click(user['Select Manpower Type'], manpower)
        self.is_click(user['Frequency'])
        self.is_click(user['Select Frequency Value'], frequency)

        self.is_click_dcr(user['Monitor Position'])
        self.input_text_dcr(user['Monitor Position'], position)
        sleep(0.5)
        self.is_click(user['Select Monitor Position'], position)


    @allure.step("新增预警模板时，点击提交按钮")
    def click_add_submit(self):
        self.is_click(user['Add Submit'])

    @allure.step("新增预警模板时，字段增加随机数")
    def asset_random(self):
        num = str(random.randint(100, 999))
        return num

    @allure.step("Monitoring Template列表, 获取列表字段内容")
    def get_list_field_content(self, field):
        self.scroll_into_view(user[field])
        field = self.element_text(user[field])
        return field

    @allure.step("Monitoring Template 列表, 获取列表字段内容")
    def query_title(self, title):
        self.input_text(user['Query Title'], title)

    @allure.step("Monitoring Template 列表, 点击Search按钮")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(2)

    @allure.step("Monitoring Template Edit页面, 点击编辑按钮")
    def click_edit(self):
        self.is_click_dcr(user['Operation Edit'])
        sleep(1)

    @allure.step("Monitoring Template Edit页面, 编辑预警模板基本信息")
    def edit_basic_information(self, title, shop_type, image_type, manpower):
        self.input_text(user['Title'], title)
        self.is_click_dcr(user['Shop Type'])
        self.input_text_dcr(user['Shop Type'], shop_type)
        sleep(0.5)
        self.is_click(user['Select Shop Type'], shop_type)

        self.is_click_dcr(user['Image Type'])
        self.is_click(user['Select Image Type'], image_type)

        self.is_click_dcr(user['Manpower Type'])
        self.is_click(user['Select Manpower Type'], manpower)

    @allure.step("Monitoring Template列表, 勾选第一个复选框")
    def click_check_box(self):
        self.is_click_dcr(user['勾选复选框'])

    @allure.step("Monitoring Template列表, 点击Disable按钮")
    def click_disable_button(self):
        self.is_click(user['Disable Button'])
        sleep(0.5)
        self.presence_sleep_dcr(user['Disable Yes'])
        self.is_click(user['Disable Yes'])

    def query_title_status(self, title, status):
        self.is_click(user['Unfold'])
        self.input_text(user['Query Title'], title)
        self.is_click(user['Query Status'])
        self.is_click(user['Select Query Status Value'], status)
        self.is_click(user['Fold'])


if __name__ == '__main__':
    pass
