import allure
import pytest,time
from project.POP.page_object.Center_Component import SpecialNavPage
from project.POP.page_object.Role_Management import *
from libs.common.read_element import Element
from project.POP.test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP组织-角色管理”页面")
    nav = SpecialNavPage(drivers)
    nav.click_gotonav("组织","角色管理")

@allure.feature("组织-角色管理") # 模块名称
class TestAddRole:
    @allure.story("角色管理") # 场景名称
    @allure.title("点击新增角色")  # 用例名称
    @allure.description("点击新增角色")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self,drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = AddRole(drivers)
        users.click_add()
        name = "张文强测试角色" + str(int(time.time()))
        users.input_rolename(name)
        users.switch_role("Promoter")
        users.input_remarks("测试专用")
        users.click_submit()
        sleep(0.5)
        # 断言-查询卖家编码与输入编码一致
        test = users.element_text(user['提交成功按钮'])
        ValueAssert.value_assert_equal(test,"新增成功")

        # 数据处理删除新增角色
        users.delete_data()

if __name__ == '__main__':
    pytest.main(['Role_Management.py'])