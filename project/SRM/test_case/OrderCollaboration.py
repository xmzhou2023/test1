import pytest
import allure
from project.SRM.page_object.OrderCollaoration import OrderCollaboration

@allure.feature("订单协同")
class TestOrderCollaboration:

    @allure.story("订单协同界面")
    @allure.title("进入订单协同界面")
    @allure.description("点击‘订单协同按钮‘，前往订单协同界面")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    def test_switch_to_order_collaborationpage(self, drivers):
        order = OrderCollaboration(drivers)
        title = order.switch_ordercollbaration_page()
        assert '订单协同' in title, '进入订单协同页面失败'

