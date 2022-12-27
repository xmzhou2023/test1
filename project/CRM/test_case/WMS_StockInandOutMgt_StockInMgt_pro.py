import logging

import allure
import pytest

import conftest
from public.base.assert_ui import *
from project.CRM.page_object.Center_Component import NavPage
from project.CRM.page_object.WMS_StockInandOutMgt_StockInMgt_pro import *
# from conftest import *
"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@pytest.fixture(scope='module',autouse=True)
def module_fixture(drivers):
    logging.info("前置条件:进入入库单管理页")
    user = NavPage(drivers)
    user.refresh_page()
    user.list_search(content='Stock In Mgt')
    yield
    logging.info("后置条件:合起菜单")
    user = NavPage(drivers)
    user.click_gotonav("WMS")



@allure.feature("WMS-Stock in&out Mgt-Stock in-pro")
class TestStockInSearch:
    @allure.story("查询当月各个业务类型的入库单数据")  # 场景名称
    @allure.title("根据type和时间筛选值进行查询")  # 用例名称
    @allure.description("type选择各种业务类型,时间默认为当前月，其余条件为空进行查询")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    # @pytest.mark.parametrize("type", ["Purchase In", "JobSheet In", "Verification In", "Allocation In"])
    def test_001_001(self, drivers, __init__):  # 用例名称取名规范'test+场景编号+用例编号'
        num = StockInSearch(drivers)
        num.stockinsearch()
        logging.info("pro_env的值为:{}".format(__init__))
        num = DomAssert(drivers)
        if "pro_hk" == __init__:
            num.assert_point_att(1, 3, 'PKSTI202209301371')
        elif "pro_fra" == __init__:
            num.assert_point_att(1, 3, 'RWSTI20220930109')
        elif "pro_9s" == __init__:
            num.assert_point_att(1, 3, 'NGSTI20220930007')













if __name__ == '__main__':
    pass

