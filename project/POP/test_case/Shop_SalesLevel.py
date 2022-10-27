import allure
import pytest
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Shop_SalesLevel import AddSalesLevel
from libs.common.read_element import Element
from project.POP.test_case.conftest import *
from public.base.basics import read_excel

object_name = os.path.basename(__file__).split('.')[0]   # 获取当前的文件是xxx.py文件，以.分割返回为[”xxx”,"py"]取第一个字符即文件名
user = Element(pro_name, object_name)

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP门店-门店销售等级”页面")
    nav = NavPage(drivers)
    nav.click_gotonav("门店","门店销售等级")

@allure.feature("门店") # 模块名称
class TestAddSalesLevel:
    @allure.story("门店销售等级") # 场景名称
    @allure.title("新增门店销量等级")  # 用例名称
    @allure.description("点击新增，输入必填项，增加门店销量等级")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = AddSalesLevel(drivers)
        users.click_add()
        users.switch_organization("oraimo")
        users.switch_region("test3")
        users.add_saleslevel()
        users.switch_level("S")
        users.input_salesdata(10000,20000)
        users.click_preservation()
        sleep(1)
        # 断言--保存提示
        test = users.element_text(user['新增成功提示'])
        ValueAssert.value_assert_equal(test,"SUCCESS")

        # 数据处理--删除新增的数据
        users.delete_data()

    @allure.story("门店销售等级")  # 场景名称
    @allure.title("删除门店销量等级")  # 用例名称
    @allure.description("点击新增，输入必填项，增加门店销量等级")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self,drivers):
        users = AddSalesLevel(drivers)
        users.click_add()
        users.switch_organization("oraimo")
        users.switch_region("test3")
        users.add_saleslevel()
        users.switch_level("S")
        users.input_salesdata(10000, 20000)
        users.click_preservation()
        sleep(1)
        users.delete_data()
        sleep(0.5)
        # 断言--删除提示
        test = users.element_text(user['删除提示'])
        ValueAssert.value_assert_equal(test,"操作成功")


if __name__ == '__main__':
    pytest.main(['Shop_SalesLevel.py'])
