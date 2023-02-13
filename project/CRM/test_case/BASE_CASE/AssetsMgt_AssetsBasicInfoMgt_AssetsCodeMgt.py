import allure
import pytest
from project.CRM.page_object.OperationMgt_PolicyAndProfits_ProfitsTypeMgt import *
from project.CRM.page_object.Center_Component import *
from public.base.assert_ui import *
import logging
from project.CRM.page_object.AssetsMgt_AssetsBasicInfoMgt_AssetsCodeMgt import *


"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@pytest.fixture(scope='module' , autouse=True) # 模块名称
def module_fixture(drivers):
    logging.info("模块前置条件，前往AssetsMgt页面")
    user = NavPage(drivers)
    user.refresh_page()
    user.click_gotonav_CRM("AssetsMgt", "AssetsBasicInfoMgt", "AssetsCodeMgt")  # 点击菜单
    user= DomAssert(drivers)
    sleep(1)
    user.assert_url("assetsMgt/assetsBasicInfoMgt/assetsCodeMgt")
    yield
    logging.info("后置条件：收起菜单")
    user = NavPage(drivers)
    user.click_gotonav("AssetsMgt")


@allure.feature("AssetsBasicInfoMgt") # 模块名称
class TestAssetsCode:
    @allure.story("AssetsBasicInfoMgt_AssetsCode") # 场景名称
    @allure.title("AssetsCode页firstType筛选")  # 用例名称
    @allure.description("对国家查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.parametrize("status, FT",
                             [("Repair Tools", "FT002"), ("Office Equipment", "FT001"), ("Publicity Materials", "FT003"), ("Warehouse Materials", "FT004")])
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers, status, FT):   # 用例名称取名规范'test+场景编号+用例编号'
        user = AssetsMgtPage(drivers)
        user.Get_search(status, choice="firstType")
        user = NavPage(drivers)
        total_assets = user.get_total()
        user = SQL("CRM", "test")
        s_ser = user.query_db('SELECT COUNT(*) FROM crm_wms_assets_code_application WHERE first_type = "{}"'.format(FT))
        sql_total = s_ser[0].get("COUNT(*)")
        ValueAssert.value_assert_equal(sql_total, int(total_assets))

    @allure.story("AssetsBasicInfoMgt_AssetsCode") # 场景名称
    @allure.title("AssetsCode页approved status筛选")  # 用例名称
    @allure.description("对国家查询")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.parametrize("status, code",
                             [("Draft", 0), ("Submitted", 1), ("In Approval", 2), ("Approved", 3), ("Failed", 4)])
    @pytest.mark.smoke # 用例标记
    def test_001_002(self, drivers, status, code):   # 用例名称取名规范'test+场景编号+用例编号'
        user = AssetsMgtPage(drivers)
        user.Get_search(status, choice="approveStatus")
        user = NavPage(drivers)
        get_total = user.get_total()
        user = SQL("CRM", "test")
        s_ser = user.query_db('SELECT COUNT(*) FROM crm_wms_assets_code_application WHERE approve_status = "{}" AND is_deleted = 0'.format(code))
        logging.info("获取到sql数据：".format(s_ser))
        sql_qty = s_ser[0].get("COUNT(*)")
        ValueAssert.value_assert_equal(sql_qty, int(get_total))

    @allure.story("AssetsBasicInfoMgt_AssetsCode") # 场景名称
    @allure.title("AssetsCode页新增数据")  # 用例名称
    @allure.description("新增一条assets code")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_003(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        file_path = os.path.join(BASE_DIR, "project", "CRM", "data", "附件.png")
        user = AssetsMgtPage(drivers)
        user.assets_add()
        user.Add_input(txt="AAA", price="221.1", file=file_path, unit="%(V)", choice=1)
        user.assets_button("Save")  # 点击保存，并校验页面返回列表页
        user = DomAssert(drivers)
        user.assert_exact_att("Search Criteria:")

    @allure.story("AssetsBasicInfoMgt_AssetsCode") # 场景名称
    @allure.title("AssetsCode页编辑数据")  # 用例名称
    @allure.description("编辑assets code数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_004(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        file_path = os.path.join(BASE_DIR, "project", "CRM", "data", "附件.png")
        user = AssetsMgtPage(drivers)
        user.Get_search(status="Draft", choice="approveStatus")
        user.assets_edit(operate="Edit")
        user.Add_input(txt="AAA", price="133.2", file=file_path, unit="%(V)", choice=2)  # 编辑页修改purchase type
        user.assets_button("Save")
        user = DomAssert(drivers)
        user.assert_exact_att("Search Criteria:")
        user = AssetsMgtPage(drivers)
        user.Get_search(status="Draft", choice="approveStatus")
        user.assets_edit(operate="Edit")  # 校验编辑页修改的purchase type成功
        purchasetype = user.assets_get_text()
        logging.info("purchasetype是：{}".format(purchasetype))
        get_type = "Purchase from HQ"
        logging.info("get_type文本是:{}".format(get_type))
        ValueAssert.value_assert_equal(get_type, purchasetype)
        sleep(1)
        user = AssetsMgtPage(drivers)
        user.assets_scroll()
        user.assets_button("Cancel")  # 关闭编辑页

    @allure.story("AssetsBasicInfoMgt_AssetsCode") # 场景名称
    @allure.title("AssetsCode页新增数据")  # 用例名称
    @allure.description("新增一条assets code并submit")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_005(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        file_path = os.path.join(BASE_DIR, "project", "CRM", "data", "附件.png")
        user = AssetsMgtPage(drivers)
        user.assets_add()
        user.Add_input(txt="AAA", price="221.1", file=file_path, unit="%(V)", choice=1)
        user.assets_button("Submit")  # 点击submit，并校验页面approve状态显示正确
        approve = user.assets_get_status()
        ValueAssert.value_assert_equal(approve, "Submitted")

    @allure.story("AssetsBasicInfoMgt_AssetsCode") # 场景名称
    @allure.title("AssetsCode页新增校验必填项")  # 用例名称
    @allure.description("新增校验必填项")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_006(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        file_path = os.path.join(BASE_DIR, "project", "CRM", "data", "附件.png")
        user = AssetsMgtPage(drivers)
        user.assets_add()
        user.Add_input(txt="", price="221.1", file=file_path, unit="%(V)", choice=1)
        user.assets_button("Save")  # 点击submit，并校验页面approve状态显示正确
        user = DomAssert(drivers)
        user.assert_exact_att("nameChinese is required")
        user = AssetsMgtPage(drivers)
        user.assets_button("Cancel")  # 关闭编辑页

    @allure.story("AssetsBasicInfoMgt_AssetsCode") # 场景名称
    @allure.title("AssetsCode页编辑点击提交")  # 用例名称
    @allure.description("assets code编辑页点击submit")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_007(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = AssetsMgtPage(drivers)
        user.Get_search(status="Draft", choice="approveStatus")
        user.assets_edit(operate="Edit")
        user = AssetsMgtPage(drivers)
        user.assets_scroll()
        user.assets_button("Submit")  # 点击submit，并校验页面approve状态显示正确
        approve = user.assets_get_status()
        ValueAssert.value_assert_equal(approve, "Submitted")

if __name__ == '__main__':
    pytest.main(['project/CRM/test_case/OperationMgt_PolicyAndProfits_ProfitsTypeMgt.py'])
