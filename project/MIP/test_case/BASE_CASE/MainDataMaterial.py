import allure
import pytest

from public.base.assert_ui import *
from project.MIP.page_object.Center_Component import NavPage
from project.MIP.page_object.MainDataMaterial import MainDataMaterial


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往 主数据-物料主数据 页面")
    menu = NavPage(drivers)
    menu.click_gotonav("主数据","物料主数据")
    dom = DomAssert(drivers)
    dom.assert_url("/main-data/material")
    yield
    logging.info("后置条件:返回 首页 页面")
    menu.back_homepage()
    dom.assert_url("/dashboard")


@allure.feature("主数据-物料主数据")
class TestQueryItemData:
    @allure.story("查询功能验证")
    @allure.title("输入物料编码范围，查询物料主数据结果正确")
    @allure.description("输入查询条件 '物料编码'范围，查询物料主数据结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        data = MainDataMaterial(drivers)
        data.input_itemCode(itemL="41500100693", itemR="41500201922")
        data.button_query()
        lisNum = data.get_listNum()
        sqlNum = data.get_sqlResult("select count(mat_code) from bb_mara where brand_code <> 0 and enable_flag=1 and "
                                    "mat_code BETWEEN  '41500100693' and  '41500201922'")
        ValueAssert.value_assert_equal(lisNum,sqlNum)
        data.button_empty()

    @allure.story("查询功能验证")
    @allure.title("单一物料查询物料编码，查询物料主数据结果正确")
    @allure.description("输入查询条件 '物料编码'单一物料查询，查询物料主数据结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        data = MainDataMaterial(drivers)
        data.input_itemCode(itemL="41500100693",scene="单一物料查询")
        data.button_query()
        lisNum = data.get_listNum()
        sqlNum = data.get_sqlResult("select count(mat_code) from bb_mara where brand_code <> 0 and enable_flag=1 and "
                                    "mat_code ='41500100693'")
        ValueAssert.value_assert_equal(lisNum,sqlNum)
        data.button_empty()

    @allure.story("查询功能验证")
    @allure.title("查询物料编码到某一物料截止，查询物料主数据结果正确")
    @allure.description("输入查询条件 '物料编码'到某一物料截止，查询物料主数据结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_003(self, drivers):
        data = MainDataMaterial(drivers)
        data.input_itemCode(itemR="41500100693",scene="到某一物料截止")
        data.button_query()
        lisNum = data.get_listNum()
        sqlNum = data.get_sqlResult("select count(mat_code) from bb_mara where brand_code <> 0 and enable_flag=1 and "
                                    "mat_code BETWEEN  '0' and  '41500100693'")
        ValueAssert.value_assert_equal(lisNum,sqlNum)
        data.button_empty()

    @allure.story("查询功能验证")
    @allure.title("查询一级类目，查询物料主数据结果正确")
    @allure.description("查询一级类目 '物料编码'到某一物料截止，查询物料主数据结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_004(self, drivers):
        data = MainDataMaterial(drivers)
        data.choice_category(level1="电子产品",level2="手机配件")
        data.button_query()
        lisNum = data.get_listNum()
        sqlNum = data.get_sqlResult("select count(mat_code) from bb_mara where brand_code <> 0 and category_id = '20001'")
        ValueAssert.value_assert_equal(lisNum,sqlNum)
        data.button_empty()

    @allure.story("查询功能验证")
    @allure.title("[异常]未选择一级类目，二级类目无数据展示")
    @allure.description("不选择一级类目，展开二级类目下拉，无数据展示")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_005(self, drivers):
        data = MainDataMaterial(drivers)
        data.choice_category(level2="手机配件")
        data.button_query()
        data.button_empty()

    @allure.story("查询功能验证")
    @allure.title("输入旧物料编码范围，查询物料主数据结果正确")
    @allure.description("输入查询条件 '旧物料编码'范围，查询物料主数据结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_006(self, drivers):
        data = MainDataMaterial(drivers)
        data.button_spread()
        data.input_oldItemCode("CPM00012","CPM00020")
        data.button_query()
        lisNum = data.get_listNum()
        sqlNum = data.get_sqlResult("select count(old_mat_code) from bb_mara where brand_code <> 0 and old_mat_code BETWEEN  'CPM00012' and  'CPM00020' and enable_flag=1;")
        ValueAssert.value_assert_equal(lisNum,sqlNum)
        data.button_spread()
        data.button_empty()

    @allure.story("查询功能验证")
    @allure.title("输入单一旧物料查询，查询物料主数据结果正确")
    @allure.description("输入查询条件 '旧物料编码'，查询物料主数据结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_007(self, drivers):
        data = MainDataMaterial(drivers)
        data.button_spread()
        data.input_oldItemCode(oldItemCodeL="CPM00012",scene="单一物料查询")
        data.button_query()
        lisNum = data.get_listNum()
        sqlNum = data.get_sqlResult("select count(old_mat_code) from bb_mara where brand_code <> 0 and old_mat_code= 'CPM00012' and enable_flag=1;")
        ValueAssert.value_assert_equal(lisNum,sqlNum)
        data.button_spread()
        data.button_empty()

    @allure.story("查询功能验证")
    @allure.title("输入到某一旧物料截止，查询物料主数据结果正确")
    @allure.description("输入查询条件 '旧物料编码'，查询物料主数据结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_008(self, drivers):
        data = MainDataMaterial(drivers)
        data.button_spread()
        data.input_oldItemCode(oldItemCodeR="CPM00012",scene="到某一物料截止")
        data.button_query()
        lisNum = data.get_listNum()
        sqlNum = data.get_sqlResult("select count(old_mat_code) from bb_mara where brand_code <> 0 and old_mat_code BETWEEN  '' and  'CPM00012' and enable_flag=1;")
        ValueAssert.value_assert_equal(lisNum,sqlNum)
        data.button_spread()
        data.button_empty()

    @allure.story("查询功能验证")
    @allure.title("选择创建日期范围，查询物料主数据结果正确")
    @allure.description("选择创建日期范围，查询物料主数据结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_009(self, drivers):
        data = MainDataMaterial(drivers)
        data.button_spread()
        data.input_createTime("2018-九月-8","2032-九月-22")
        data.button_query()
        lisNum = data.get_listNum()
        sqlNum = data.get_sqlResult("select count(mat_code)  from bb_mara where  brand_code >='00' and creation_time BETWEEN  '2018-09-08' and  '2032-09-22' and enable_flag=1;")
        ValueAssert.value_assert_equal(lisNum,sqlNum)
        data.button_spread()
        data.button_empty()

    @allure.story("查询功能验证")
    @allure.title("选择某一创建日期，查询物料主数据结果正确")
    @allure.description("选择某一创建日期，查询物料主数据结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_010(self, drivers):
        data = MainDataMaterial(drivers)
        data.button_spread()
        data.input_createTime(createTimeL="2018-九月-8",scene="单一日期查询")
        data.button_query()
        lisNum = data.get_listNum()
        sqlNum = data.get_sqlResult("select count(mat_code)  from bb_mara where  brand_code <> 0 and creation_time =  '2018-09-08'  and enable_flag=1;")
        ValueAssert.value_assert_equal(lisNum,sqlNum)
        data.button_spread()
        data.button_empty()

    @allure.story("查询功能验证")
    @allure.title("选择截止到某一创建日期，查询物料主数据结果正确")
    @allure.description("选择截止到某一创建日期，查询物料主数据结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_011(self, drivers):
        data = MainDataMaterial(drivers)
        data.button_spread()
        data.input_createTime(createTimeR="2018-九月-8",scene="到某一日期截止")
        data.button_query()
        lisNum = data.get_listNum()
        sqlNum = data.get_sqlResult("select count(mat_code)  from bb_mara where  brand_code <> 0 and brand_code <> '3CHUB'  and creation_time BETWEEN  '' and  '2018-09-08' and enable_flag=1;")
        ValueAssert.value_assert_equal(lisNum,sqlNum)
        data.button_spread()
        data.button_empty()

    @allure.story("查询功能验证")
    @allure.title("合法维护查询条件，查询物料主数据结果正确")
    @allure.description("合法维护查询条件，查询物料主数据结果正确")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_012(self, drivers):
        data = MainDataMaterial(drivers)
        data.input_itemCode("41500201900","41500201999")
        data.choice_category("电子产品","手机配件")
        data.choice_brand("INFINIX")
        data.choice_statue("已上架")
        data.button_spread()
        data.input_itemDescribe("Infinix_灯箱靠墙配件高柜_V3.1_灯箱布_NOTE7")
        data.input_itemType("4150")
        data.input_itemModel("NOTE7")
        data.input_createTime(createTimeL="2020-九月-22",scene="单一日期查询")
        data.button_query()
        lisNum = data.get_listNum()
        sqlNum = data.get_sqlResult("select count(mat_code)  from bb_mara where  mat_code BETWEEN  '41500201900' and  '41500201999' "
                                    "and brand_code = '02' and pick_up_flag = '1' and matkl = '4150' and model = "
                                    "'NOTE7' and category_id ='20001'and creation_time = '2020-09-22' and "
                                    "enable_flag=1;")
        ValueAssert.value_assert_equal(lisNum,sqlNum)
        data.button_spread()
        data.button_empty()

    @allure.story("查询功能验证")
    @allure.title("[异常]列表无满足条件数据，列表无数据显示")
    @allure.description("列表无满足条件数据，列表无数据显示")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_013(self, drivers):
        data = MainDataMaterial(drivers)
        data.input_itemCode("41500201900", "41500201999")
        data.choice_category("电子产品", "手机配件")
        data.choice_brand("INFINIX")
        data.choice_statue("已上架")
        data.button_spread()
        data.input_itemDescribe("Infinix_灯箱靠墙配件高柜_V3.1_灯箱布_NOTE7")
        data.input_itemType("4150")
        data.input_itemModel("NOTE8")
        data.input_createTime(createTimeL="2020-九月-22", scene="单一日期查询")
        data.button_query()
        lisNum = data.get_listNum()
        sqlNum = data.get_sqlResult(
                "select count(mat_code) from bb_mara where  mat_code BETWEEN  '41500201900' and  '41500201999' "
                "and brand_code = '02' and pick_up_flag = '1' and matkl = '4150' and model = "
                "'NOTE8' and category_id ='20001'and creation_time = '2020-09-22' and "
                "enable_flag=1;")
        ValueAssert.value_assert_equal(lisNum, sqlNum)
        txt = data.return_txt()
        ValueAssert.value_assert_equal(txt,"暂无数据")
        data.button_spread()
        data.button_empty()

    @allure.story("查询功能验证")
    @allure.title("点击物料编码，跳转至物料主数据详情页面")
    @allure.description("点击物料编码，跳转至物料主数据详情页面")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_014(self, drivers):
        data = MainDataMaterial(drivers)
        data.input_itemCode(itemL="41500201922", scene="单一物料查询")
        data.button_query()
        data.click_itemCode("41500201922")
        dom = DomAssert(drivers)
        dom.assert_url("/main-data/matDetail")
        data.return_itemPage()

@allure.feature("主数据-物料主数据")
class TestEditItemData:
    @allure.story("编辑功能验证")
    @allure.title("点击指定行编辑按钮，跳转至对应商品明细页")
    @allure.description("点击指定行编辑按钮，跳转至对应商品明细页")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        data = MainDataMaterial(drivers)
        data.input_itemCode(itemL="41500201922", scene="单一物料查询")
        data.button_query()
        data.button_edit()
        data.checkout_newWindow()
        dom = DomAssert(drivers)
        dom.assert_url("/purchase/detail/edit/41500201922")
        data.close_newWindow()

    @allure.story("编辑功能验证")
    @allure.title("点击指定行预览按钮，跳转至对应商品明细页")
    @allure.description("点击指定行预览按钮，跳转至对应商品明细页")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_002(self, drivers):
        data = MainDataMaterial(drivers)
        data.input_itemCode(itemL="41500201922", scene="单一物料查询")
        data.button_query()
        data.button_preview()
        data.checkout_newWindow()
        dom = DomAssert(drivers)
        dom.assert_url("/purchase/detail/preview/41500201922")
        data.close_newWindow()


@allure.feature("主数据-物料主数据")
class TestPutawayItemData:
    @allure.story("上/下架功能验证")
    @allure.title("勾选指定主数据，点击上架/下架按钮，更新上/下架状态")
    @allure.description("勾选指定主数据，点击上架/下架按钮，更新上/下架状态")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_001(self, drivers):
        data = MainDataMaterial(drivers)
        data.input_itemCode(itemL="41500201922", scene="单一物料查询")
        data.button_query()
        data.select_itemData()
        data.on_off_Shelves()

    @allure.story("上/下架功能验证")
    @allure.title("全选主数据，点击上架/下架按钮，更新上/下架状态")
    @allure.description("全选主数据，点击上架/下架按钮，更新上/下架状态")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_002(self, drivers):
        data = MainDataMaterial(drivers)
        data.input_itemCode("41500201900", "41500201999")
        data.button_query()
        data.select_itemData("全选")
        data.on_off_Shelves()


if __name__ == '__main__':
    pytest.main(['project/MIP/testcase/MainDataMaterial.py'])
