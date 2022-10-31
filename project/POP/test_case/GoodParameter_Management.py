import allure,logging
import pytest,time
from project.POP.page_object.Center_Component import NavPage
from project.POP.page_object.GoodParameter_Management import *
from public.base.assert_ui import *

@pytest.fixture(scope='function', autouse=True)
def setup_class(drivers):
    logging.info("模块前置条件：前往“POP商品-商品参数”页面")
    user = NavPage(drivers)
    user.click_gotonav("商品","商品参数")

@allure.feature("商品-商品参数") # 模块名称
class TestAddGoodParam:
    @allure.story("商品参数") # 场景名称
    @allure.title("商品参数新增")  # 用例名称
    @allure.description("输入必填项新增商品参数")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    @pytest.mark.skip(reason="暂时跳过")
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user= AddGoodParam(drivers)
        user.click_add()
        content = '测试新增参数' + str(int(time.time()))
        user.input_paramname(content)
        user.switch_category()
        user.switch_display_form("单选框")
        user.switch_order("1")
        user.input_parameters("参数值1","参数值2","参数值3")
        user.click_submit()
        sleep(0.5)
        # 断言根据商品参数名数据库查询该参数并计数，判定返回值=1
        sql = f"SELECT count(*) FROM `pop_data_db`.`goods_parameter_config` WHERE parameter_name='{content}';"
        SQLAssert('POP', 'test').assert_sql_count(1, sql)

@allure.feature("商品-商品参数") # 模块名称
class TestQueryDetail:
    @allure.story("商品参数") # 场景名称
    @allure.title("商品参数详情查看")  # 用例名称
    @allure.description("点击商品参数列表详情，正常查看参数详情页")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_002_001(self,drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        users = Query_GoodDetail(drivers)
        users.click_detail()
        sleep(0.5)
        # 断言
        test = users.element_text(user['参数详情'])
        ValueAssert.value_assert_equal(test,'参数详情')
        users.refresh()
        sleep(3)
@allure.feature("商品-商品参数")
class TestExportGoodParam:
    @allure.story("商品参数")
    @allure.title("商品参数导出")
    @allure.description("点击导出，商品参数列表导出")
    @allure.severity("normal")
    @pytest.mark.smoke # 用例标记
    def test_003_001(self,drivers):
        users = ExportGoodParam(drivers)
        users.click_export()
        sleep(0.5)
        # 断言
        test = users.element_text(user['导出成功提示'])
        ValueAssert.value_assert_equal(test,"创建导出任务成功！")
if __name__ == '__main__':
    pytest.main(['GoodParameter_Management.py'])
