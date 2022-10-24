import allure
import pytest

from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.SystemMgmt_RegionMgmt import AreaPage


@pytest.fixture(scope='module', autouse=True)
def module_setup_fixture(drivers):
    logging.info("模块前置条件：前往 DRP数据管理-机型库 页面")
    user = NavPage(drivers)
    user.click_gotonav("系统管理", "区域管理")
    dom = DomAssert(drivers)
    dom.assert_url("/systemManage/areaManage")
    yield
    logging.info("后置条件:关闭 DRP数据管理-机型库 页面")
    user.close_page()
    dom.assert_url("/dashboard")


@allure.feature("系统管理-区域管理")
class TestSearchArea:

    @allure.story("查询区域")
    @allure.title("前往一级区域")
    @allure.description("点击‘TECNO事业部’前往一级区域‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_001(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('TECNO事业部')
        user.assert_area('管理维度','TECNO事业部','市场划分')

    @allure.story("查询区域")
    @allure.title("前往二级区域")
    @allure.description("点击‘非洲区’前往二级区域")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('TECNO事业部', '非洲区')
        user.assert_area('市场划分','非洲区', '区域')

    @allure.story("查询区域")
    @allure.title("前往三级区域")
    @allure.description("点击‘东非地区’前往三级区域")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_003(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('TECNO事业部', '非洲区', '东非地区')
        user.assert_area('区域','东非地区', '大区')

    @allure.story("查询区域")
    @allure.title("前往四级区域")
    @allure.description("点击‘东非一区’前往四级区域‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_004(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('TECNO事业部', '非洲区', '东非地区', '东非一区')
        user.assert_area('大区', '东非一区', '国家')

    @allure.story("查询区域")
    @allure.title("前往五级区域")
    @allure.description("点击‘孟加拉’前往五级区域‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_005(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('TECNO事业部', '非洲区', '东非地区', '东非一区', '卢旺达')
        user.assert_area('国家', '卢旺达')

    @allure.story("查询区域")
    @allure.title("精确搜索区域")
    @allure.description("区域搜索框，输入‘卢旺达’，可查到该区域")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_006(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('TECNO事业部')
        user.search_area("卢旺达")
        allist = user.goto_tree()
        user.check_tree("卢旺达", allist)

    @allure.story("查询区域")
    @allure.title("模糊搜索区域")
    @allure.description("区域搜索框，输入‘卢旺’，可查到该区域")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_007(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('TECNO事业部')
        user.search_area("卢旺")
        allist = user.goto_tree('Itel事业部')
        user.check_tree("卢旺", allist)


@allure.feature("系统管理-区域管理")
class TestAppendArea:
    @allure.story("新增区域")
    @allure.title("新增二级区域")
    @allure.description("前往‘Infinix事业部‘一级区域，新增‘其他’二级区域成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部')
        user.add_button()  # 点击新增按钮
        user.add_area('其他')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        # 删除测试数据
        user.del_list(2, '其他')  # 点击删除按钮

    @allure.story("新增区域")
    @allure.title("新增三级区域")
    @allure.description("前往‘新市场’二级区域，新增‘其他’三级区域成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_002(self, drivers):
        user = AreaPage(drivers)
        user.precondition(drivers,2)
        user.goto_tree('Infinix事业部', '其他')
        user.add_button()  # 点击新增按钮
        user.add_area('其他')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        # 删除测试数据
        user.del_list(2, '其他')  # 点击删除按钮
        user.goto_tree('Infinix事业部')
        user.del_list(2, '其他')  # 点击删除按钮

    @allure.story("新增区域")
    @allure.title("新增四级区域")
    @allure.description("前往‘Xpark区‘四级区域，新增四级区域‘其他’成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_003(self, drivers):
        user = AreaPage(drivers)
        user.precondition(drivers,3)
        user.goto_tree('Infinix事业部','其他','其他')
        user.add_button()  # 点击新增按钮
        user.add_area('迪拜')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        # 删除测试数据
        user.del_list(2, '迪拜')  # 点击删除按钮
        user.goto_tree('Infinix事业部', '其他')
        user.del_list(2, '其他')  # 点击删除按钮
        user.goto_tree('Infinix事业部')
        user.del_list(2, '其他')  # 点击删除按钮

    @allure.story("新增区域")
    @allure.title("新增五级区域（国家）")
    @allure.description("前往‘摩洛哥’四级区域，新增国家'贝宁'成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_004(self, drivers):
        user = AreaPage(drivers)
        user.precondition(drivers,4)
        user.goto_tree('Infinix事业部','其他','其他', '迪拜')
        user.add_button()  # 点击新增按钮
        user.add_area('贝宁')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        # 删除测试数据
        user.clear_testdata()

    @allure.story("新增区域")
    @allure.title("新增国家信息")
    @allure.description("前往‘贝宁’五级区域，新增国家国家信息成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_005(self, drivers):
        user = AreaPage(drivers)
        user.precondition(drivers,5)
        user.goto_tree('Infinix事业部','其他','其他', '迪拜','贝宁')
        user.add_button()  # 点击新增按钮
        user.add_area('Infinix','品牌')  # 选择品牌
        user.add_area('公开市场','市场分类')  # 选择市场分类
        user.add_area('Infinix事业部','组织')  # 选择组织
        user.add_area('Infinix事业部','部门')  # 选择部门
        user.add_area('Infinix事业部','事业部')  # 选择事业部
        user.save_button()  # 点击保存按钮
        # 删除测试数据
        user.clear_testdata()

    @allure.story("新增区域")
    @allure.title("[异常]重复新增二级区域，新增失败")
    @allure.description("前往 Infinix事业部 ，重复新增 二级区域-其他，新增失败")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_006(self, drivers):
        user = AreaPage(drivers)
        user.precondition(drivers,2)
        user.add_button()  # 点击新增按钮
        user.add_area('其他')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        user.assert_add()
        # 删除测试数据
        user.clear_testdata()

    @allure.story("新增区域")
    @allure.title("[异常]重复新增三级区域，新增失败")
    @allure.description("前往 二级区域 ，重复新增 三级区域-其他，新增失败")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_007(self, drivers):
        user = AreaPage(drivers)
        user.precondition(drivers,3)
        user.add_button()  # 点击新增按钮
        user.add_area('其他')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        user.assert_add()
        # 删除测试数据
        user.clear_testdata()

    @allure.story("新增区域")
    @allure.title("[异常]重复新增四级区域，新增失败")
    @allure.description("前往 三级区域 ，重复新增 四级区域-摩洛哥，新增失败")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_008(self, drivers):
        user = AreaPage(drivers)
        user.precondition(drivers,4)
        user.add_button()  # 点击新增按钮
        user.add_area('迪拜')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        user.assert_add()
        # 删除测试数据
        user.clear_testdata()

    @allure.story("新增区域")
    @allure.title("[异常]重复新增国家，新增失败")
    @allure.description("前往‘摩洛哥’四级区域，重复新增国家-贝宁 新增失败")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_009(self, drivers):
        user = AreaPage(drivers)
        user.precondition(drivers,5)
        user.add_button()  # 点击新增按钮
        user.add_area('贝宁')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        user.assert_add()
        # 删除测试数据
        user.clear_testdata()


@allure.feature("系统管理-区域管理")
class TestDeleteArea:

    @allure.story("删除区域")
    @allure.title("删除二级区域")
    @allure.description("前往‘Infinix事业部’，删除二级区域-其他 删除成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_001(self, drivers):
        user = AreaPage(drivers)
        user.precondition(drivers,2)
        user.del_list(2,'其他')

    @allure.story("删除区域")
    @allure.title("删除三级区域")
    @allure.description("前往 二级区域，删除三级区域-其他 删除成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_002(self, drivers):
        user = AreaPage(drivers)
        user.precondition(drivers,3)
        user.del_list(2,'其他')
        # 删除测试数据
        user.clear_testdata()

    @allure.story("删除区域")
    @allure.title("删除四级区域失败")
    @allure.description("前往 三级区域，删除四级区域-摩洛哥 删除成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_003(self, drivers):
        user = AreaPage(drivers)
        user.precondition(drivers,4)
        user.del_list(2,'迪拜')
        # 删除测试数据
        user.clear_testdata()

    @allure.story("删除区域")
    @allure.title("[异常] 已关联国家的四级区域，删除失败")
    @allure.description("四级区域-摩洛哥，已关联国家-贝宁，删除摩洛哥失败")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_004(self, drivers):
        user = AreaPage(drivers)
        user.precondition(drivers,5)
        user.goto_tree('Infinix事业部','其他','其他')
        user.del_list(2,'迪拜')
        user.del_assert()
        # 删除测试数据
        user.clear_testdata()


@allure.feature("系统管理-区域管理")
class TestEditArea:
    @allure.story("编辑国家信息")
    @allure.title("编辑国家信息")
    @allure.description("前往国家-贝宁，编辑国家信息，编辑成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_001(self, drivers):
        user = AreaPage(drivers)
        user.precondition(drivers,5)  # 前置条件-新增国家完成
        user.precondition_contry(drivers)  # 前置条件-维护国家信息完成
        user.edit_list(1,"Infinix")
        user.add_area('定制市场','市场分类')  # 选择市场分类
        user.save_button()  # 点击保存按钮
        user.edit_assert(2,'定制市场')
        # 删除测试数据
        user.clear_testdata()

@allure.feature("系统管理-区域管理")
class TestMoveArea:
    @allure.story("移动功能")
    @allure.title("移动国家至其他大区部")
    @allure.description("前往大区部，编辑国家信息，编辑成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_005_001(self, drivers):
        user = AreaPage(drivers)
        user.precondition1(drivers)  # 前置条件-新增目标大区完成
        user.precondition(drivers,5)  # 前置条件-新增国家完成
        user.move_button(3,'贝宁')
        user.choice_target('新市场','东非地区','东非一区')
        user.move_affirm(3,'贝宁')
        user.goto_tree('Infinix事业部','新市场','东非地区','东非一区')
        user.edit_assert(3,'贝宁')
        # 删除测试数据
        user.clear_testdata()

    @allure.story("移动功能")
    @allure.title("批量移动")
    @allure.description("批量移动国家至某大区 移动成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_005_002(self, drivers):
        user = AreaPage(drivers)
        user.precondition1(drivers)  # 前置条件-新增目标大区完成
        user.precondition(drivers,5)  # 前置条件-新增国家完成
        user.precondition2(drivers)  # 前置条件-新增其他国家完成
        user.choice_country(3,'贝宁')
        user.choice_country(3,'孟加拉')
        user.bulk_operation()
        user.choice_target('新市场','东非地区','东非一区')
        user.move_affirm(3,'贝宁')
        user.goto_tree('Infinix事业部','新市场','东非地区','东非一区')
        assertValue1 = user.edit_assert(3,'贝宁')
        logging.info("列表数据：{}".format(assertValue1))
        # 删除测试数据
        user.clear_testdata()

    @allure.story("移动功能")
    @allure.title("全选批量移动")
    @allure.description("全选批量移动国家至某大区 移动成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_005_003(self, drivers):
        user = AreaPage(drivers)
        user.precondition1(drivers)  # 前置条件-新增目标大区完成
        user.precondition(drivers,5)  # 前置条件-新增国家完成
        user.precondition2(drivers)  # 前置条件-新增其他国家完成
        user.choice_all()
        user.bulk_operation()
        user.choice_target('新市场','东非地区','东非一区')
        user.move_affirm(3,'贝宁')
        user.goto_tree('Infinix事业部','新市场','东非地区','东非一区')
        assertValue1 = user.edit_assert(3,'贝宁')
        logging.info("列表数据：{}".format(assertValue1))
        # 删除测试数据
        user.clear_testdata()



if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/SystemMgmt_RegionMgmt.py'])
