from time import sleep

import allure
import pytest
import logging

from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Organazition_Region import Region
from project.POP.test_case.conftest import *
from libs.common.read_element import Element

"""
funciton 每一个函数或方法都会调用
class 每一个类调用一次，一个类可以有多个方法
module 每一个.py文件调用一次，该文件内又有多个function和class
session 每个session只运行一次，在自动化测试时，登录步骤可以使用该session
"""

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


@pytest.fixture(scope='function', autouse=True)
def setup_module(drivers):
    logging.info("前置条件：进入’组织-区域‘页面")
    nav = NavPage(drivers)
    nav.click_gotonav("组织", "区域")


@allure.feature("组织")    # 模块名
class TestExportRegion:
    @allure.story("区域")
    @allure.title("Region")
    @allure.description("根据筛选条件导出区域列表")
    @allure.severity("normal")
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        users = Region(drivers)
        users.click_dropdown('国家', 'China')
        users.click_search('查询')
        sleep()
        users.click_button('导出')
        test = users.element_text(user['断言'])
        ValueAssert.value_assert_equal(test, '创建导出任务成功！')


if __name__ == '__main__':
    pytest.main(['Organazition_Region.py'])
