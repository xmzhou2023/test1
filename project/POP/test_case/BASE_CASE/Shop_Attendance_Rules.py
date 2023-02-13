import allure
import pytest,time
from project.POP.page_object.Center_Component import *
from project.POP.page_object.Shop_Attendance_Rules import *
from libs.common.read_element import Element
from project.POP.test_case.conftest import *
object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP门店-考勤规则”页面")
    nav = SpecialNavPage(drivers)
    nav.click_gotonav("门店","考勤规则")

@allure.feature("门店-考勤规则") # 模块名称
class TestAddAttendanceRules:
    @allure.story("考勤规则") # 场景名称
    @allure.title("点击新增考勤规则")  # 用例名称
    @allure.description("点击新增单排班考勤规则")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self,drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = AddAttendanceRule(drivers)
        users.click_add()
        users.attendance_information("oraimo","China","xhr_test6","十二月","测试专用","16:00","17:00")
        users.click_sure()
        sleep(1)
        # 断言--新增成功提示
        test = users.element_text(user['新增成功提示'])
        ValueAssert.value_assert_equal(test, "新增成功")

@allure.feature("门店-考勤规则") # 模块名称
class TestQueryAttendanceRules:
    @allure.story("考勤规则")  # 场景名称
    @allure.title("查询考勤规则")  # 用例名称
    @allure.description("输入组织，点击查询对应组织下的考勤规则")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = Queryattdendancerule(drivers)
        users.queryattendancerule("考勤规则-组织框","oraimo")
        sleep(2)
        # 断言--新增成功提示
        test = users.element_text(user['组织断言'])
        ValueAssert.value_assert_equal(test,"oraimo")
        # 退出iframe
        users.frame_back()


    @allure.story("考勤规则")  # 场景名称
    @allure.title("查询考勤规则")  # 用例名称
    @allure.description("输入国家，点击查询对应国家下的考勤规则")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = Queryattdendancerule(drivers)
        users.queryattendancerule("考勤规则-国家框","Uganda")
        sleep(5)
        # 断言--新增成功提示
        test = users.element_text(user['国家断言'])
        ValueAssert.value_assert_equal(test,"Uganda")
        # 退出iframe
        users.frame_back()

    @allure.story("考勤规则")  # 场景名称
    @allure.title("查询考勤规则")  # 用例名称
    @allure.description("输入开始月份，点击查询对应月份下的考勤规则")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        users = Queryattdendancerule(drivers)
        users.queryattendancerule("考勤规则-开始月份框","十一月")
        sleep(5)
        # 断言--新增成功提示
        test = users.element_text(user['开始月份断言'])
        ValueAssert.value_assert_equal(test,"2022-11")
        # 退出iframe
        users.frame_back()



if __name__ == '__main__':
    pytest.main(['Shop_Attendance_Rules.py::TestQueryAttendanceRules'])