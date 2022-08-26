import allure
import pytest

from public.base.assert_ui import *
from project.DRP.page_object.Center_Component import NavPage
from project.DRP.page_object.SystemMgmt_RegionMgmt import AreaPage


@pytest.fixture(scope='module', autouse=True)
def setup_module(drivers):
    logging.info("模块前置条件：前往“系统管理-区域管理”页面")
    user = NavPage(drivers)
    user.click_gotonav("系统管理", "区域管理")
    user = DomAssert(drivers)
    user.assert_url("/systemManage/areaManage")


@allure.feature("系统管理-区域管理")
class TestSearchArea:

    @allure.story("查询区域")
    @allure.title("前往一级区域")
    @allure.description("点击‘itel事业部’前往一级区域‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_001_001(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('itel事业部')

    @allure.story("查询区域")
    @allure.title("前往二级区域")
    @allure.description("点击‘itel事业部’前往二级区域")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_002(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('itel事业部', 'itel事业部')

    @allure.story("查询区域")
    @allure.title("前往三级区域")
    @allure.description("点击‘itel事业部’前往三级区域")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_003(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('itel事业部', 'itel事业部', 'itel事业部')

    @allure.story("查询区域")
    @allure.title("前往四级区域")
    @allure.description("点击‘事业部备料’前往四级区域‘")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    @pytest.mark.run(order=4)
    def test_001_004(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('itel事业部', 'itel事业部', 'itel事业部', '事业部备料')

    @allure.story("查询区域")
    @allure.title("精确搜索区域")
    @allure.description("区域搜索框，输入‘巴基斯坦’，可查到该区域")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_005(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('itel事业部')
        user.search_area("巴基斯坦")
        allist = user.goto_tree()
        res = user.check_tree("巴基斯坦", allist)
        user = ValueAssert()
        user.value_assert_equal(res)

    @allure.story("查询区域")
    @allure.title("模糊搜索区域")
    @allure.description("区域搜索框，输入‘巴基’，可查到该区域")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_006(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('itel事业部')
        user.search_area("巴基")
        allist = user.goto_tree()
        res = user.check_tree("巴基", allist)
        user = ValueAssert()
        user.value_assert_equal(res)

    @allure.story("查询区域")
    @allure.title("清空搜索框内容")
    @allure.description("区域搜索框输入‘加纳’，再点击清除按钮，搜索框被清空")
    @allure.severity("trivial")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_001_007(self, drivers):
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
    @allure.description("前往‘itel事业部’一级区域，点击导出按钮，区域数据导出成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_002_001(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('itel事业部')
        user.download_area(content="drp_dept_export_itel")


@allure.feature("系统管理-区域管理")
class TestAppendArea:

    @allure.story("新增区域")
    @allure.title("新增二级区域（地区部）")
    @allure.description("前往‘Infinix事业部‘一级区域，新增‘lj测试01’地区部成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_001(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部')
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='lj测试01', nameEn='ljtest01')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        # 删除测试数据
        user.del_list(2, 'lj测试01')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("新增区域")
    @allure.title("新增三级区域（大区）")
    @allure.description("前往‘Xpark业务区’二级区域，新增‘lj测试001’大区成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_002(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区')
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='lj测试001', nameEn='ljtest001')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        # 删除测试数据
        user.del_list(2, 'lj测试001')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("新增区域")
    @allure.title("新增四级区域（国家）")
    @allure.description("前往‘Xpark区‘三级区域，新增国家‘中国’成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_003(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.add_button()  # 点击新增按钮
        user.add_area(country='中国')  # 输入国家并搜索
        user.add_list(2, '中国')  # 点击添加国家按钮
        user.save_country_button()  # 点击保存按钮
        # 删除测试数据
        user.del_list(2, '中国')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("新增区域")
    @allure.title("新配置市场-市场分类配置")
    @allure.description("前往‘中国’四级区域，配置市场分类为‘印度’成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_004(self, drivers):
        user = AreaPage(drivers)
        # 新增国家“中国”
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.add_button()  # 点击新增按钮
        user.add_area(country='中国')  # 输入国家并搜索
        user.add_list(2, '中国')  # 点击添加国家按钮
        user.save_country_button()  # 点击保存按钮
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区', '中国')
        user.update_market()  # 点击编辑
        user.market_class(market='印度')  # 选择市场分类
        user.save_market()  # 保存

        # 删除测试数据
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.del_list(2, '中国')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("新增区域")
    @allure.title("新配置市场-市场划分配置")
    @allure.description("前往‘中国’四级区域，配置市场划分为‘SSA’成功")
    @allure.severity("blocker")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_005(self, drivers):
        user = AreaPage(drivers)
        # 新增国家“中国”
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.add_button()  # 点击新增按钮
        user.add_area(country='中国')  # 输入国家并搜索
        user.add_list(2, '中国')  # 点击添加国家按钮
        user.save_country_button()  # 点击保存按钮
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区', '中国')
        user.cut_market(cut='国家市场划分配置')  # 切换市场划分配置
        user.update_market()  # 点击编辑按钮
        user.market_class(market1='SSA')  # 选择市场
        user.save_market()  # 保存
        # 删除测试数据
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.del_list(2, '中国')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("新增区域")
    @allure.title("[异常]重复新增二级区域（地区部）保存失败")
    @allure.description("前往‘Infinix事业部‘，重复新增地区部‘lj测试01’失败")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_006(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部')
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='lj测试01', nameEn='ljtest01')  # 新增地区部名称并保存
        user.save_button()
        user.add_button()
        user.add_area(nameZh='lj测试01', nameEn='ljtest01')  # 再次新增相同的地区部名称 保存失败
        user.save_button()
        # 删除测试数据
        user.del_list(2, 'lj测试01')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("新增区域")
    @allure.title("[异常]重复新增三级区域（大区）保存失败")
    @allure.description("前往‘Xpark业务区‘，重复新增大区‘lj测试01’失败")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_007(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区')
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='lj测试01', nameEn='ljtest01')  # 新增大区名称并保存
        user.save_button()  # 保存
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='lj测试01', nameEn='ljtest01')  # 再次新增相同的大区名称 保存失败
        user.save_button()  # 保存
        # 删除测试数据
        user.del_list(2, 'lj测试01')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("新增区域")
    @allure.title("[异常]重复添加四级区域（国家）保存失败")
    @allure.description("前往‘Xpark区‘，重复添加国家‘中国’失败")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_008(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.add_button()  # 点击新增按钮
        user.add_area(country='中国')  # 输入国家并搜索
        user.add_list(2, '中国')  # 点击添加国家按钮
        user.save_country_button()  # 保存国家
        user.add_button()  # 点击新增按钮
        user.add_area(country='中国')  # 输入国家并搜索
        user.add_list(2, '中国')  # 点击添加国家按钮
        user.save_country_button()  # 保存国家 失败
        # 删除测试数据
        user.del_list(2, '中国')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("新增区域")
    @allure.title("[异常]添加其他组织已存在的国家 保存失败")
    @allure.description("前往‘Xpark区‘ 添加其他组织已存在的国家‘阿联酋’失败")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_009(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.add_button()  # 点击新增按钮
        user.add_area(country='阿联酋')  # 添加国家
        user.add_list(2, '阿联酋')  # 点击添加国家按钮
        user.save_country_button()  # 同一品牌同一国家不能重复维护到不同的组织下面 保存失败

    @allure.story("新增区域")
    @allure.title("[异常]中/英文名称为空，保存失败")
    @allure.description("前往‘Infinix事业部‘，点击新增按钮，不输入中/英文名称，新增保存失败")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_003_010(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部')
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='', nameEn='')  # 不维护中/英文名称 保存失败
        user.save_button()


@allure.feature("系统管理-区域管理")
class TestUpdateArea:

    @allure.story("编辑区域")
    @allure.title("编辑二级区域（地区部）")
    @allure.description("前往‘Infinix事业部‘一级区域，将地区部’lj测试01‘修改为‘lj测试02’成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_001(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部')
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='lj测试01', nameEn='ljtest01')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        user.update_list(2, 'lj测试01')  # 点击编辑按钮
        user.update_area(nameZh='lj测试02', nameEn='ljtest02')  # 编辑 替换内容
        user.save_button()  # 保存
        # 删除测试数据
        user.del_list(2, 'lj测试02')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("编辑区域")
    @allure.title("编辑三级区域（大区）")
    @allure.description("前往‘Xpark业务区’二级区域，将‘lj测试001’修改为‘ljtest002’成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_002(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区')
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='lj测试001', nameEn='lj测试001')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        user.update_list(2, 'lj测试001')  # 点击编辑按钮
        user.update_area(nameZh='lj测试002', nameEn='ljtest002')  # 编辑 替换内容
        user.save_button()  # 保存
        # 删除测试数据
        user.del_list(2, 'lj测试002')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("编辑区域")
    @allure.title("编辑市场分类配置")
    @allure.description("前往四级区域‘中国’，将市场分类‘印度’修改为‘孟加拉’成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_003(self, drivers):
        user = AreaPage(drivers)
        # 新增国家“中国”
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.add_button()  # 点击新增按钮
        user.add_area(country='中国')  # 输入国家并搜索
        user.add_list(2, '中国')  # 点击添加国家按钮
        user.save_country_button()  # 点击保存按钮
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区', '中国')
        user.update_market()  # 点击编辑按钮
        user.market_class(market='印度')  # 选择市场
        user.save_market()  # 保存
        user.update_market()  # 点击编辑
        user.market_class(market='孟加拉')  # 选择市场分类
        user.save_market()  # 保存
        # 删除测试数据
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.del_list(2, '中国')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("编辑区域")
    @allure.title("编辑市场划分配置")
    @allure.description("前往四级区域‘中国’，将市场分类‘SSA’修改为‘印度’成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_004_004(self, drivers):
        user = AreaPage(drivers)
        # 新增国家“中国”
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.add_button()  # 点击新增按钮
        user.add_area(country='中国')  # 输入国家并搜索
        user.add_list(2, '中国')  # 点击添加国家按钮
        user.save_country_button()  # 点击保存按钮
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区', '中国')
        user.cut_market(cut='国家市场划分配置')  # 切换市场划分配置
        user.update_market()  # 点击编辑按钮
        user.market_class(market1='SSA')  # 选择市场
        user.save_market()  # 保存
        user.update_market()  # 点击编辑按钮
        user.market_class(market1='印度')  # 选择市场
        user.save_market()  # 保存
        # 删除测试数据
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.del_list(2, '中国')  # 点击删除按钮
        user.delete_area()  # 删除确认


@allure.feature("系统管理-区域管理")
class TestDeleteArea:

    @allure.story("删除区域")
    @allure.title("删除四级区域")
    @allure.description("前往‘Xpark区’，删除国家‘中国’成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_005_001(self, drivers):
        user = AreaPage(drivers)
        # 新增国家“中国”
        user.goto_tree('Infinix事业部', 'Xpark业务区', 'Xpark区')
        user.add_button()  # 点击新增按钮
        user.add_area(country='中国')  # 输入国家并搜索
        user.add_list(2, '中国')  # 点击添加国家按钮
        user.save_country_button()  # 点击保存按钮
        user.del_list(2, '中国')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("删除区域")
    @allure.title("删除三级区域")
    @allure.description("前往‘Xpark业务区’，删除大区‘lj测试002’成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_005_002(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部', 'Xpark业务区')
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='lj测试001', nameEn='ljtest001')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        user.del_list(2, 'lj测试001')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("删除区域")
    @allure.title("删除二级区域")
    @allure.description("前往‘Infinix事业部‘，删除地区部‘lj测试02’成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_005_003(self, drivers):
        user = AreaPage(drivers)
        user.goto_tree('Infinix事业部')
        user.add_button()  # 点击新增按钮
        user.add_area(nameZh='lj测试01', nameEn='ljtest01')  # 输入地区中英文名称
        user.save_button()  # 点击保存按钮
        user.goto_tree('Infinix事业部')
        user.del_list(2, 'lj测试01')  # 点击删除按钮
        user.delete_area()  # 删除确认

    @allure.story("删除区域")
    @allure.title("删除二级区域，分支下的区域都被删除")
    @allure.description("新建二级区域‘lj测试01’，再新建下阶区域‘lj测试001’，删除地区部‘lj测试01’，下阶区域‘lj测试001’也被删除")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    @pytest.mark.smoke
    def test_005_004(self, drivers):
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
        user.del_list(2, 'lj测试01')  # 点击删除按钮
        user.delete_area()  # 删除地区部，且大区也被删除



if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/SystemMgmt_RegionMgmt.py'])
