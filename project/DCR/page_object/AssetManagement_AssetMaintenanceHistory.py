import logging

from libs.common.read_element import Element
from libs.common.time_ui import sleep
from ..test_case.conftest import *
from libs.config.conf import BASE_DIR
import random

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AssetMaintenanceHistoryPage(Base):
    @allure.step("Asset Maintenance History页面, 按Brand,Country,Statistical Date条件查询")
    def query_asset_maintenance_history(self, country, brand, status):
        self.is_click(user['Unfold'])
        sleep(1)
        #选择品牌筛选
        self.is_click(user['Query Country'])
        sleep(0.4)
        self.input_text(user['Query Country'], country)
        self.is_click(user['Query Country Value'], country)

        self.is_click(user['Query Brand'])
        self.is_click(user['Query Brand Value'], brand)
        self.is_click(user['Query Status'])
        self.is_click(user['Query Status Value'], status)



    @allure.step("Asset Maintenance History页面, 点击查询按钮")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(2)

    @allure.step("Inventory Shortage Report页面, 获取列表字段内容")
    def get_list_field_content(self, field):
        self.scroll_into_view(user[field])
        field = self.element_text(user[field])
        return field

    @allure.step("Asset Maintenance History页面, 获取列表分页总条数")
    def get_total(self):
        get_total = self.element_text(user['Get list Total'])
        total1 = int(get_total[6:])
        return total1

    @allure.step("断言分页总数是否存在数据")
    def assert_total(self, total):
        if int(total) >= 1:
            logging.info("库存不足报告列表，分页总条数大于0，能查询到考勤记录数Total:{}".format(total))
        else:
            logging.info("库存不足报告列表，分页总条数为0，未查询到考勤记录数Total:{}:".format(total))



if __name__ == '__main__':
    pass
