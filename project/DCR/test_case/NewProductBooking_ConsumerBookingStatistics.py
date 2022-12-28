import allure
import pytest

from project.DCR.page_object.NewProductBooking_ConsumerBookingStatistics import ConsumerBookingStatistics

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
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        """变量"""
        query_dict = {
            # 'Booking Date': '2020-11-13To2022-12-26',
            'Order Status': 'Finished',
            'Model': 'KE5',
            'Brand': 'TECNO',
            # 'Market Name': 'SPARK Go 2021',
            'Shop': 'BD020213',
            'IMEI': '350120813065408',
            'Activated Status': 'Yes',
            'Delivered Date': '2022-04-01To2022-04-30',
            'Activated Date': '2021-08-15To2021-08-15',
            'Activity Template': 'TEM2204240001',
            'Booking Order ID': 'BO220424000011',
            'Country/City': 'Bangladesh_Bandarban_Bandarban',
            'Sales Region': 'Bangladesh District_Bangladesh_Barisal-测试'
        }
        add = ConsumerBookingStatistics(drivers)
        add.click_menu("New Product Booking", "Consumer Booking Statistics")
        add.click_unfold()
        add.random_Query_Method(query_dict)

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
