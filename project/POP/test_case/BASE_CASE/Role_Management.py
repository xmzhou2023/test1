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
        # # 断言-编辑成功提示
        test = users.element_text(user['提交成功提示'])
        ValueAssert.value_assert_equal(test,"新增成功")
        sleep(3)
        # for i in range(17,18):
        #     users.click_add()
        #     # name = "zwq_test" + str(int(time.time()))
        #     name = "zwq_test" + str(i)
        #     users.input_rolename(name)
        #     users.switch_role("Promoter")
        #     users.input_remarks("测试专用")
        #     users.click_submit()
        #     # sleep(0.5)
        #     # # 断言-查询卖家编码与输入编码一致
        #     # test = users.element_text(user['提交成功按钮'])
        #     # ValueAssert.value_assert_equal(test,"新增成功")
        #     sleep(3)

        # # 数据处理删除新增角色
        users.delete_data(name)

    @allure.story("角色管理")  # 场景名称
    @allure.title("点击新增禁用后的角色")  # 用例名称
    @allure.description("点击新增禁用后的角色")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):
        users = AddRole(drivers)
        users.click_add()
        name = "zwq_test" + str(int(time.time()))
        users.input_rolename(name)
        users.switch_role("Promoter")
        users.input_remarks("测试专用")
        users.click_submit()
        sleep(3)
        #禁用新增的数据
        users.delete_data(name)
        #再新增刚刚的禁用的数据
        users = AddRole(drivers)
        users.click_add()
        users.input_rolename(name)
        users.switch_role("Promoter")
        users.input_remarks("测试专用")
        users.click_submit()
        sleep(0.5)
        # 断言--重复提交提示
        test = users.element_text(user['重复提交提示'])
        ValueAssert.value_assert_equal(test, "该角色名已存在，请联系系统管理员操作")
        # 关闭弹窗
        users.click_close()
        sleep(3)

@allure.feature("组织-角色管理") # 模块名称
class TestDisableRole:
    @allure.story("角色管理") # 场景名称
    @allure.title("禁用角色")  # 用例名称
    @allure.description("选择角色组禁用角色组")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_002_001(self,drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = DisableRole(drivers)
        users.disable_role("manage")
        sleep(1)
        # 断言--存在人员提示--请先移动人员
        test = users.element_text(user['存在人员禁用提示'])
        ValueAssert.value_assert_equal(test,"请先移除人员")

@allure.feature("组织-角色管理") # 模块名称
class TestEditRole:
    @allure.story("角色管理")  # 场景名称
    @allure.title("编辑角色")  # 用例名称
    @allure.description("选择角色编辑角色组")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_001(self, drivers):
        users = AddRole(drivers)
        users.click_add()
        name = "zwq_test" + str(int(time.time()))
        users.input_rolename(name)
        users.switch_role("Promoter")
        users.input_remarks("测试专用")
        users.click_submit()
        # 编辑新增的角色组
        users1 = EditRole(drivers)
        users1.switch_role(name)
        users1.click_edit()
        editname = "zwq_test" + str(int(time.time()))
        users1.input_rolename(editname)
        users1.click_submit()
        sleep(1)
        # 断言--success
        test = users.element_text(user['编辑成功提示'])
        ValueAssert.value_assert_equal(test, "编辑成功")

        # 数据清理
        users.delete_data(editname)






if __name__ == '__main__':
    pytest.main(['Role_Management.py'])