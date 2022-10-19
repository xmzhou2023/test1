from libs.common.read_element import Element
from project.TBM.page_object.Center_Component import CenterComponent
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class KeyComponentsSearch(CenterComponent, APIRequest):
    """关键器件_关键器件查询"""

    @allure.step("初始化页面")
    def refresh_webpage_click_menu(self):
        self.refresh_webpage()
        self.click_menu("关键器件", "关键器件查询")

    @allure.step("点击操作")
    def click_operate(self, item, operate):
        """
        关键器件查询 点击操作 ： 查看/修订/封板
        @param item:项目
        @param operate:操作
        """
        self.is_click_tbm(user['项目操作'], item, operate)

    @allure.step("点击修订关键器件复选框")
    def click_key(self, key):
        """
        关键器件查询 点击修订关键器件复选框
        @param key:指定器件分类
        """
        self.is_click_tbm(user['修订关键器件-复选框'], key)

    @allure.step("点击修订关键器件确定")
    def click_revise_comfirm(self):
        self.is_click_tbm(user['修订关键器件-确定'])

    @allure.step("断言：进入关键器件修订发起页面，查看关键器件-业务审核-维护关键器件显示是否正确")
    def assert_review(self, review, result=True):
        DomAssert(self.driver).assert_control(user['修订关键器件-业务审核'], review, result=result)


if __name__ == '__main__':
    pass
