import allure, os
from public.base.basics import Base, sleep
from libs.common.read_element import Element
import logging
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class Inventory_Query(Base):
    """根据门店名称查询库存"""

    @allure.step("输入门店名称筛选条件")
    def click_shop(self,variable):
        # 点击门店输入框，输入仙桃体专店

        self.is_click(user["门店名称输入框"])
        self.input_text(user["门店名称输入框"], variable)
        self.is_click(user["门店"], variable)

    @allure.step("点击查询")
    def click_query(self, expect):
        # 点击查询按钮
        self.is_click(user["查询按钮"])


if __name__ == '__main__':
    pass
