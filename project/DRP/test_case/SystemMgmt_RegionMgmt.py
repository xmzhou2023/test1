import allure
import pytest
from public.base.assert_ui import DomAssert, ValueAssert
from project.DRP.page_object.center_Component import NavPage
from project.DRP.page_object.SystemMgmt_RegionMgmt import AreaPage


@allure.feature("系统管理-区域管理")
class TestSearchArea:

    @allure.story("前往区域")
    @allure.title("前往主菜单")
    @allure.description("前往主菜单‘itel事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_001_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('itel事业部')

    @pytest.mark.RT
    @allure.story("前往区域")
    @allure.title("前往二级菜单")
    @allure.description("前往二级菜单‘itel事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    def test_001_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('itel事业部', 'itel事业部')

    @allure.story("前往区域")
    @allure.title("前往三级菜单")
    @allure.description("前往三级菜单‘itel事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=3)
    def test_001_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('itel事业部', 'itel事业部', 'itel事业部')

    @allure.story("前往区域")
    @allure.title("前往四级菜单")
    @allure.description("前往四级菜单‘事业部备料‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=4)
    def test_001_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('itel事业部', 'itel事业部', 'itel事业部', '事业部备料')

    @allure.story("区域搜索")
    @allure.title("精确搜索区域")
    @allure.description("前往主菜单‘itel事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=5)
    def test_001_005(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('itel事业部')
        user.search_area("巴基斯坦")
        allist = user.goto_tree()
        res = user.check_tree("巴基斯坦", allist)
        user = ValueAssert()
        user.value_assert_equal(res)

    @allure.story("区域搜索")
    @allure.title("模糊搜索区域")
    @allure.description("前往主菜单‘itel事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=6)
    def test_001_006(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('itel事业部')
        user.search_area("巴基")
        allist = user.goto_tree()
        res = user.check_tree("巴基", allist)
        user = ValueAssert()
        user.value_assert_equal(res)

    @allure.story("清空区域搜索框")
    @allure.title("点击按钮，清空搜索框内容")
    @allure.description("前往主菜单‘itel事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=7)
    def test_001_007(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('itel事业部')
        user.search_area("加纳")
        allist = user.goto_tree()
        res = user.check_tree("加纳", allist)
        user = ValueAssert()
        user.value_assert_equal(res)
        user = AreaPage(drivers)
        user.clear_tree()


@allure.feature("系统管理-区域管理")
class TestExportArea:

    @allure.story("导出区域")
    @allure.title("导出区域数据")
    @allure.description("导出区域数据‘itel事业部’")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=8)
    def test_002_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('itel事业部')
        user.download_area(content="drp_dept_export_TECNO")


@allure.feature("系统管理-区域管理")
class TestAppendArea:

    @allure.story("新增区域")
    @allure.title("新增一级区域（地区部）")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=9)
    def test_003_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部')
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='lj测试01', nameEn='ljtest01')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮

    @allure.story("新增区域")
    @allure.title("新增二级区域（大区）")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=12)
    def test_003_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区')
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='lj测试001', nameEn='ljtest001')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮


    @allure.story("新增区域")
    @allure.title("新增三级区域（国家）")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=15)
    def test_003_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.add_button()  # 点击新增按钮
        user.add_area(country='中国')  # 输入国家并搜索
        user.add_list(area_name='中国')  # 点击添加国家按钮
        user.save_country_button()  # 点击保存按钮

    @allure.story("新增区域")
    @allure.title("配置市场-市场分类配置")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=16)
    def test_003_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区', '中国')
        user.update_market()  # 点击编辑
        user.market_class(market='印度')  # 选择市场分类
        user.save_market()  # 保存

    @allure.story("新增区域")
    @allure.title("配置市场-市场划分配置")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=18)
    def test_003_005(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区', '中国')
        user.cut_market(cut='国家市场划分配置')  # 切换市场划分配置
        user.update_market()  # 点击编辑按钮
        user.market_class(market1='SSA')  # 选择市场
        user.save_market()  # 保存


@allure.feature("系统管理-区域管理")
class TestUpdateArea:

    @allure.story("编辑区域")
    @allure.title("编辑二级区域（地区部）")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=10)
    def test_004_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部')
        user.update_list('lj测试01')  # 点击编辑按钮
        user.update_area(nameZh='lj测试02', nameEn='ljtest02')  # 编辑 替换内容
        user.save_button()  # 保存

    @allure.story("编辑区域")
    @allure.title("编辑三级区域（大区）")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=13)
    def test_004_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区')
        user.update_list('lj测试001')  # 点击编辑按钮
        user.update_area(nameZh='lj测试002', nameEn='ljtest002')  # 编辑 替换内容
        user.save_button()  # 保存

    @allure.story("编辑区域")
    @allure.title("编辑市场分类配置")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=17)
    def test_004_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区', '中国')
        user.update_market()  # 点击编辑
        user.market_class(market='孟加拉')  # 选择市场分类
        user.save_market()  # 保存

    @allure.story("编辑区域")
    @allure.title("编辑市场划分配置")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=19)
    def test_004_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区', '中国')
        user.cut_market(cut='国家市场划分配置')  # 切换市场划分配置
        user.update_market()  # 点击编辑按钮
        user.market_class(market1='印度')  # 选择市场
        user.save_market()  # 保存


@allure.feature("系统管理-区域管理")
class TestDeleteArea:

    @allure.story("删除区域")
    @allure.title("删除国家")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=20)
    def test_005_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.del_list('中国')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("删除区域")
    @allure.title("删除大区")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=14)
    def test_005_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区')
        user.del_list('lj测试002')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("删除区域")
    @allure.title("删除地区部")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=11)
    def test_005_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部')
        user.del_list('lj测试02')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("删除区域")
    @allure.title("删除地区部，下级区域都被删除")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_005_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部')  # 进入一级菜单
        user.add_button()
        user.add_area(nameZh='lj测试01', nameEn='ljtest01')  # 新增地区部
        user.save_button()
        user.goto_tree('Infinix事业部', 'lj测试01')  # 切换到地区部层级
        user.add_button()
        user.add_area(nameZh='lj测试001', nameEn='ljtest001')  # 新增大区
        user.save_button()
        user.goto_tree('Infinix事业部')  # 切到一级菜单
        user.del_list('lj测试01')  # 点击删除按钮
        user.delete_area()  # 删除地区部，且大区也被删除


@allure.feature("系统管理-区域管理")
class TestCloseArea:

    @allure.story("关闭区域管理窗口")
    @allure.title("关闭区域管理窗口")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_006_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.close_window(window_name='区域管理')  # 关闭区域管理窗口


@allure.feature("系统管理-区域管理")
class TestCounterExample:

    @allure.story("重复新增")
    @allure.title("重复新增 一级区域（地区部）保存失败")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_007_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部')
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='lj测试01', nameEn='ljtest01')  # 新增地区部名称并保存
        user.save_button()
        user.add_button()
        user.add_area(nameZh='lj测试01', nameEn='ljtest01')  # 再次新增相同的地区部名称 保存失败
        user.save_button()

    @allure.story("重复新增")
    @allure.title("重复新增 二级区域（大区）保存失败")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_007_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区')
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='lj测试01', nameEn='ljtest01')  # 新增大区名称并保存
        user.save_button()  # 保存
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='lj测试01', nameEn='ljtest01')  # 再次新增相同的大区名称 保存失败
        user.save_button()  # 保存

    @allure.story("重复新增")
    @allure.title("重复新增 三级区域（国家）保存失败")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_007_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.add_button()  # 点击新增按钮
        user.add_area(country='中国')  # 输入国家并搜索
        user.add_list(area_name='中国')  # 点击添加国家按钮
        user.save_country_button()  # 保存国家
        user.add_button()  # 点击新增按钮
        user.add_area(country='中国')  # 输入国家并搜索
        user.add_list(area_name='中国')  # 点击添加国家按钮
        user.save_country_button()  # 保存国家 失败

    @allure.story("重复新增")
    @allure.title("重复新增 同一品牌同一国家不能重复维护到不同的组织下面")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_007_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.add_button()  # 点击新增按钮
        user.add_area(country='阿联酋')  # 添加国家
        user.add_list(area_name='阿联酋')  # 点击添加国家按钮
        user.save_country_button()  # 同一品牌同一国家不能重复维护到不同的组织下面 保存失败

    @allure.story("新增失败")
    @allure.title("中/英文名称为空，保存失败")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_007_005(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', )
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='', nameEn='')  # 不维护中/英文名称 保存失败
        user.save_button()


class TestClearData:
    @allure.story("删除测试遗留数据")
    @allure.title("删除测试遗留数据")
    @allure.description("前往主菜单‘Infinix事业部‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_008_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("系统管理", "区域管理")
        user = DomAssert(drivers)
        user.assert_url("/systemManage/areaManage")
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部')
        user.del_list('lj测试01')  # 点击删除按钮
        user.delete_area()  # 删除确认
        user.goto_tree('Infinix事业部', 'Xpark业务区')
        user.del_list('lj测试01')  # 点击删除按钮
        user.delete_area()  # 删除确认
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.del_list('中国')  # 点击删除按钮
        user.delete_area()  # 删除确认


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/SystemMgmt_RegionMgmt.py'])
