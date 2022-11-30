from libs.common.read_element import Element
from libs.common.time_ui import sleep
from ..test_case.conftest import *
from libs.config.conf import BASE_DIR
import random


object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AssetCountingPage(Base):
    @allure.step("Asset Counting页面, 根据国家、品牌、状态、人力资源条件筛选资产统计数据")
    def query_asset_counting(self, country, brand, status, manpower):
        self.is_click(user['Unfold'])
        sleep(1)
        self.is_click(user['Query Country'])
        self.input_text(user['Query Country'], country)
        sleep(0.5)
        self.is_click(user['Query Country Value'])

        self.is_click(user['Query Brand'])
        self.is_click(user['Query Brand Value'], brand)

        self.is_click(user['Query Status'])
        self.is_click(user['Query Status Value'], status)

        self.is_click(user['Manpower Type'])
        self.is_click(user['Manpower Type Value'], manpower)
        self.is_click(user['Fold'])


    @allure.step("Asset Counting页面, 点击查询按钮")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(2)

    @allure.step("Asset Counting页面, 获取列表字段内容")
    def get_list_field_content(self, field):
        self.scroll_into_view(user[field])
        field = self.element_text(user[field])
        return field

    @allure.step("Asset Counting页面, 获取列表分页总条数")
    def get_total(self):
        get_total = self.element_text(user['Get list Total'])
        total1 = int(get_total[6:])
        return total1

    @allure.step("Asset Counting页面, 点击picture打开图片")
    def click_picture(self):
        self.is_click(user['Get list Picture'])
        sleep(2)

    @allure.step("Asset Counting页面, 关闭弹出的Asset Photo页面")
    def close_asset_photo(self):
        self.is_click(user['Close Asset Photo'])

if __name__ == '__main__':
    pass
