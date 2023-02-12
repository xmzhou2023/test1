import allure
import pytest

from project.DCR_GLOBAL.page_object.NewProductBooking_ConsumerBookingStatistics import ConsumerBookingStatistics

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("新品预订-顾客预订报表") # 模块名称
class TestConsumerBookingStatistics:
    @allure.story("顾客预订报表") # 场景名称
    @allure.title("组合查询")  # 用例名称
    @allure.description("组合查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):
        """变量"""
        query_dict = {
            # 'Booking Date': '2022-06-01To2022-12-26',
            'Order Status': 'Pending Delivery',
            'Model': 'X672',
            'Brand': 'Infinix',
            'Market Name': 'NOTE 12 VIP',
            'Shop': 'PK410266',
            'IMEI': '',
            'Activated Status': 'No',
            'Delivered Date': '',
            'Activated Date': '',
            'Activity Template': 'TEM2206300001',
            'Booking Order ID': 'BO220630000001',
            'Country/City': 'Pakistan_Punjab_Lahore',
            'Sales Region': 'New Market_Pakistan-Infinix_C1'
        }
        add = ConsumerBookingStatistics(drivers)
        add.click_menu("New Product Booking", "Consumer Booking Statistics")
        add.click_unfold()
        add.random_Query_Method(query_dict)

    @allure.story("顾客预订报表")
    @allure.title("逻辑冲突的查询条件查询结果为空：是否激活&激活时间")
    @allure.description("逻辑冲突的查询条件查询结果为空：是否激活&激活时间")
    @allure.severity("critical")  # 分别为3种类型等级：critical\normal\minor
    def test_001_002(self, drivers):
        user = ConsumerBookingStatistics(drivers)
        user.click_menu("New Product Booking", "Consumer Booking Statistics")
        user.click_unfold()
        user.input_search('Activated Status', 'No')
        user.input_search('Booking Date', '2019-01-01To2023-12-31')
        user.input_search('Activated Date', '2019-01-01To2023-12-31')
        user.click_search()
        user.assert_NoData()


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
