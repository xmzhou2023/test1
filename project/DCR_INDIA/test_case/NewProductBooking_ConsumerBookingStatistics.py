import allure
import pytest

from project.DCR_INDIA.page_object.NewProductBooking_ConsumerBookingStatistics import ConsumerBookingStatistics

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("新品预订-顾客预订报表") # 模块名称
class TestSearch:
    @allure.story("页面查询") # 场景名称
    @allure.title("组合查询")  # 用例名称
    @allure.description("组合查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):
        """变量"""
        query_dict = {
            # 'Booking Date': '2022-06-01To2022-12-26',
            'Order Status': 'Pending Delivery',
            'Model': 'AD9',
            'Brand': 'TECNO',
            'Market Name': 'PHANTOM X2 Pro',
            'Shop': 'IN002046',
            'IMEI': '',
            # 'Activated Status': 'No',
            'Delivered Date': '',
            'Activated Date': '',
            'Activity Template': 'TEM2212200002',
            'Booking Order ID': 'BO221221000001',
            'Country/City': 'India_Maharashtra_Mumbai',
            'Sales Region': 'India District_India-TECNO_Alternate Channel'
        }
        add = ConsumerBookingStatistics(drivers)
        add.click_menu("New Product Booking", "Consumer Booking Statistics")
        add.click_unfold()
        add.random_Query_Method(query_dict)

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
