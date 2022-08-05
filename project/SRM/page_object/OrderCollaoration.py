from libs.common.read_element import Element
from public.base.basics import Base
import time
import os
from ..test_case.conftest import *


object_name = os.path.basename(__file__).split('.')[0]
order= Element(pro_name, object_name)

class OrderCollaboration(Base):
    
    @allure.step("进入订单协同页面")
    def switch_ordercollbaration_page(self):
        self.find_element(order['订单协同按钮']).click()
        return self.find_element(order['订单协同页面标题头']).text

    def switch_order_manage_page(self):
        self.frame_enter(order['订单协同iframe'])
        self.find_element(order['订单管理菜单按钮']).click()
        return self.find_element(order['订单管理tab标题']).text

    def switch_ordermanage_iframe(self):
        self.frame_enter(order['订单管理iframe'])

    def get_ordermanage_search_text(self):
        return self.find_element(order['订单管理查询栏']).text

    def click_ordermanage_morebutton(self):
        self.find_element(order['订单管理更多按钮']).click()

    def get_ordermanage_more_search_text(self):
        return self.find_element(order['订单管理更多查询栏']).text

    def click_ordermanage_purchaseorderstatus(self):
        self.find_element(order['订单管理-查询条件-采购订单状态下拉按钮']).click()

    def get_ordermanage_purchaseorderstatus(self):
        return self.find_element(order['订单管理-查询条件-采购订单状态选项框']).text

    def click_ordermanage_ordersendstatus(self):
        self.find_element(order['订单管理-查询条件-订单发送状态下拉按钮']).click()

    def get_ordermanage_ordersendstatus(self):
        return self.find_element(order['订单管理-查询条件-订单发送状态选项框']).text

    def click_ordermanage_approval_status(self):
        self.find_element(order['订单管理-查询条件-审批状态下拉按钮']).click()

    def get_ordermanage_approval_status(self):
        return self.find_element(order['订单管理-查询条件-审批状态选项框']).text

    def order_manage_search_by_purchase_orderstatus(self,condition):
        self.click_ordermanage_purchaseorderstatus()
        self.find_element(order['订单管理-查询条件-采购订单状态{0}选项'.format(condition)]).click()
        self.find_element(order['订单管理查询按钮']).click()
        time.sleep(5)

    def get_order_manage_search_result(self):
        return self.find_element(order['订单管理-查询结果']).text
