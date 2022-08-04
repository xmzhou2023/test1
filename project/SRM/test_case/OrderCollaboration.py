import pytest
import allure
from project.SRM.page_object.OrderCollaoration import OrderCollaboration

@allure.feature("订单协同")
class TestOrderCollaboration:

    @allure.story("订单协同界面")
    @allure.title("进入订单协同界面")
    @allure.description("点击‘订单协同按钮‘，前往订单协同界面")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_switch_to_order_collaborationpage(self, drivers):
        order = OrderCollaboration(drivers)
        title = order.switch_ordercollbaration_page()
        assert '订单协同' in title, '进入订单协同页面失败'

@allure.feature("订单协同")
class TestOrderManage:

    @allure.story("订单管理")
    @allure.title("进入订单管理")
    @allure.description("点击‘订单管理‘，前往订单管理界面")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_check_switch_to_order_managepage(self, drivers):
        order = OrderCollaboration(drivers)
        OrderManageTabTitle = order.switch_order_manage_page()
        assert '订单管理' in OrderManageTabTitle, '进入订单管理页面失败'

    @allure.story("订单管理")
    @allure.title("检查是否有按供应商erp号条件进行搜索")
    @allure.description("检查是否有按供应商erp号条件进行搜索")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    def test_check_order_manage_search_erptitle(self, drivers):
        order = OrderCollaboration(drivers)
        order.switch_ordermanage_iframe()
        OrderManageErpTitle = order.get_ordermanage_search_text()
        assert '供应商erp号' in OrderManageErpTitle, '搜索条件缺少供应商erp号'



