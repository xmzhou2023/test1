from time import sleep

import allure
import pytest
import logging

from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Organazition_Region import Region
from project.POP.test_case.conftest import *
from libs.common.read_element import Element

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


@pytest.fixture(scope='function', autouse=True)
def setup_module(drivers):
    logging.info("前置条件：进入’组织-区域‘页面")
    nav = NavPage(drivers)
    nav.click_gotonav("组织", "区域")


@allure.feature("组织-区域")    #模块名
class TestExportRegion:
    @allure.story("导出区域")
    @allure.title("导出筛选区域")
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
