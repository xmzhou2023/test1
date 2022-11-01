import allure,logging
import pytest,random,time
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.Good_Management import AddGood,ExportGood
from public.base.assert_ui import *
from project.POP.test_case.conftest import *
from libs.common.read_element import Element
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP商品-商品管理”页面")
    user = NavPage(drivers)
    user.click_gotonav("商品","商品管理")

@allure.feature("商品-商品管理") # 模块名称
class TestAddGood:
    @allure.story("商品管理") # 场景名称
    @allure.title("商品新增")  # 用例名称
    @allure.description("输入必填项新增商品成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = AddGood(drivers)
        user.click_add()
        content = "zwq新增测试商品" + str(int(time.time()))
        user.input_productname(content)
        user.switch_category('qwz')
        user.switch_region('China')
        user.switch_brand('TECNO')
        user.switch_imei('否')
        user.add_goodinfo()
        user.click_preserve()
        sleep(0.5)
        # 断言--新增后页面返回商品管理页面判定页面是否存在商品管理字段
        DomAssert(drivers).assert_exact_att('商品管理')

@allure.feature("商品-商品管理") # 模块名称
class TestExportGood:
    @allure.story("商品管理") # 场景名称
    @allure.title("商品管理导出")  # 用例名称
    @allure.description("点击导出，商品管理列表导出成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_002_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = ExportGood(drivers)
        users.click_export()
        sleep(0.5)
        #断言-导出成功提示
        test = users.element_text(user['导出成功提示'])
        ValueAssert.value_assert_equal(test,"创建导出任务成功！")


if __name__ == '__main__':
    pytest.main(['Good_Management.py'])
