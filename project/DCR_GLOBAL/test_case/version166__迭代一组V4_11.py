import allure
import pytest
@allure.feature("迭代一组V4_11")  # 迭代名称
class Teststory_2704:
    @allure.story("国包收货新增流通国家逻辑")  # 用户故事名称
    @allure.title("新增设置交货国家按钮，检查角色按钮权限配置,配置角色生效，展示按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16276(self, drivers):
        pass


    @allure.story("国包收货新增流通国家逻辑")  # 用户故事名称
    @allure.title("新增设置交货国家按钮，检查角色按钮权限配置,配置角色不生效，不展示按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16277(self, drivers):
        pass


    @allure.story("国包收货新增流通国家逻辑")  # 用户故事名称
    @allure.title("选择没有交货国家的一条DN，点击设置交货国家按钮,弹出设置交货国家弹窗")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16278(self, drivers):
        pass


    @allure.story("国包收货新增流通国家逻辑")  # 用户故事名称
    @allure.title("选择没有交货国家的一条DN，点击设置交货国家按钮,交货国家为下拉选项，内容国包收货国家（单选）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16279(self, drivers):
        pass


    @allure.story("国包收货新增流通国家逻辑")  # 用户故事名称
    @allure.title("选择没有交货国家的一条DN，点击设置交货国家按钮,点击提交必填项校验，成功设置交货国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16280(self, drivers):
        pass


    @allure.story("国包收货新增流通国家逻辑")  # 用户故事名称
    @allure.title("选择没有交货国家的一条DN，点击设置交货国家按钮,点击导出自动同步列表字段内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16281(self, drivers):
        pass


    @allure.story("国包收货新增流通国家逻辑")  # 用户故事名称
    @allure.title("选择没有交货国家的一条DN，点击设置交货国家按钮,设置过交货国家后收货")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16282(self, drivers):
        pass


    @allure.story("国包收货新增流通国家逻辑")  # 用户故事名称
    @allure.title("选择没有交货国家的一条DN，点击设置交货国家按钮,点击关闭弹窗")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16283(self, drivers):
        pass


    @allure.story("国包收货新增流通国家逻辑")  # 用户故事名称
    @allure.title("选择多条没有交货国家的DN，统一设置相同的交货国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16284(self, drivers):
        pass


    @allure.story("国包收货新增流通国家逻辑")  # 用户故事名称
    @allure.title("选择一条有交货国家的DN，点击设置交货国家按钮,提示选中DN已设置交货国家（SelectedDNordershavebeensetupDeliveryCountry）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16285(self, drivers):
        pass


    @allure.story("国包收货新增流通国家逻辑")  # 用户故事名称
    @allure.title("选择多条DN其中含有交货国家字段不为空的，过滤该条DN不显示在设置弹窗的列表中")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16286(self, drivers):
        pass


    @allure.story("国包收货新增流通国家逻辑")  # 用户故事名称
    @allure.title("选择多条DN的交货国家字段都不为空时，提示选中DN已设置交货国家（SelectedDNordershavebeensetupDeliveryCountry）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16287(self, drivers):
        pass


@allure.feature("迭代一组V4_11")  # 迭代名称
class Teststory_2703:
    @allure.story("用户反馈新增未评价记录显示与评价等级查询条件")  # 用户故事名称
    @allure.title("测试点_1、测试路径FeedBackFeedBack")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16430(self, drivers):
        pass


    @allure.story("用户反馈新增未评价记录显示与评价等级查询条件")  # 用户故事名称
    @allure.title("测试点_2、用户关闭APP反馈弹窗，生成评价记录并记录用户评价等级为未评价")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16431(self, drivers):
        pass


    @allure.story("用户反馈新增未评价记录显示与评价等级查询条件")  # 用户故事名称
    @allure.title("测试点_3、新增筛选项Evaluate（评价等级），下拉选择框，多选，根据选中等级，查询对应的评价记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16432(self, drivers):
        pass


    @allure.story("用户反馈新增未评价记录显示与评价等级查询条件")  # 用户故事名称
    @allure.title("测试点_31、选项内容1~5、未评价")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16433(self, drivers):
        pass


    @allure.story("用户反馈新增未评价记录显示与评价等级查询条件")  # 用户故事名称
    @allure.title("测试点_32、筛选Evaluate，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16434(self, drivers):
        pass


@allure.feature("迭代一组V4_11")  # 迭代名称
class Teststory_2645:
    @allure.story("返利SchemeType增加TotalAmountAch")  # 用户故事名称
    @allure.title("返利SchemeType增加TotalAmountAch")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16883(self, drivers):
        pass


    @allure.story("返利SchemeType增加TotalAmountAch")  # 用户故事名称
    @allure.title("取数逻辑=CustomerAchievement里面的PurchaseAmountAch的达成率结果。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16884(self, drivers):
        pass


    @allure.story("返利SchemeType增加TotalAmountAch")  # 用户故事名称
    @allure.title("customerPurchaseTotalAmountAchUnitRebateAmount")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16885(self, drivers):
        pass


    @allure.story("返利SchemeType增加TotalAmountAch")  # 用户故事名称
    @allure.title("customerPurchaseTotalAmountAchTotalRebateAmount")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16886(self, drivers):
        pass


    @allure.story("返利SchemeType增加TotalAmountAch")  # 用户故事名称
    @allure.title("customerPurchaseTotalAmountAchRebate")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16887(self, drivers):
        pass


    @allure.story("返利SchemeType增加TotalAmountAch")  # 用户故事名称
    @allure.title("customerPurchaseTotalAmountAchUnitRebateAmount条件6种")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16888(self, drivers):
        pass


    @allure.story("返利SchemeType增加TotalAmountAch")  # 用户故事名称
    @allure.title("customerPurchaseTotalAmountAchTotalRebateAmount条件6种")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16889(self, drivers):
        pass


    @allure.story("返利SchemeType增加TotalAmountAch")  # 用户故事名称
    @allure.title("customerPurchaseTotalAmountAchRebate条件6种")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16890(self, drivers):
        pass


    @allure.story("返利SchemeType增加TotalAmountAch")  # 用户故事名称
    @allure.title("校验各个组合执行返利数据一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16891(self, drivers):
        pass


@allure.feature("迭代一组V4_11")  # 迭代名称
class Teststory_2706:
    @allure.story("salesregion支持上级编辑")  # 用户故事名称
    @allure.title("区域等级是1的销售区域不支持编辑父级，即SalesRegion")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17242(self, drivers):
        pass


    @allure.story("salesregion支持上级编辑")  # 用户故事名称
    @allure.title("编辑区域等级时25的销售区域，编辑其父级	父级区域为下拉选项树，内容所有销售区域SalesRegion1~4级节点，单选")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17243(self, drivers):
        pass


    @allure.story("salesregion支持上级编辑")  # 用户故事名称
    @allure.title("编辑区域等级时25的销售区域，编辑其父级	当前节点及下级节点等级之和移动的目标节点等级小于等于5，可以成功修改当前节点的父节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17244(self, drivers):
        pass


    @allure.story("salesregion支持上级编辑")  # 用户故事名称
    @allure.title("编辑区域等级时25的销售区域，编辑其父级	当前节点及下级节点等级之和移动的目标节点等级大于5，提示目标父级区域为4级销售区域，只支持选择X级以上的销售区域（X=5当前节点及下级等级之和）修改失败")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17245(self, drivers):
        pass


    @allure.story("salesregion支持上级编辑")  # 用户故事名称
    @allure.title("编辑区域等级时25的销售区域，编辑其父级	修改到SalesRegion节点，目标父节点按0计算，理论上都可以修改成功")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17246(self, drivers):
        pass


    @allure.story("salesregion支持上级编辑")  # 用户故事名称
    @allure.title("编辑区域等级时25的销售区域，编辑其父级	修改5级节点，可以修改到任何节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17247(self, drivers):
        pass


    @allure.story("salesregion支持上级编辑")  # 用户故事名称
    @allure.title("编辑区域等级时25的销售区域，编辑其父级	跨级向上修改父节点，理论上可以修改成功")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17248(self, drivers):
        pass


    @allure.story("salesregion支持上级编辑")  # 用户故事名称
    @allure.title("编辑区域等级时25的销售区域，编辑其父级	跨级向下修改父节点，验证是否通过")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17249(self, drivers):
        pass


    @allure.story("salesregion支持上级编辑")  # 用户故事名称
    @allure.title("保存修改的父节点	必填项校验，未选择父级给与提示Thisfiledisrequired")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17250(self, drivers):
        pass


    @allure.story("salesregion支持上级编辑")  # 用户故事名称
    @allure.title("保存修改的父节点	提交更新销售区域树")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17251(self, drivers):
        pass


    @allure.story("salesregion支持上级编辑")  # 用户故事名称
    @allure.title("保存修改的父节点	检查销售区域列表数据更新、人员、客户、门店销售区域树是否更新")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17252(self, drivers):
        pass


    @allure.story("salesregion支持上级编辑")  # 用户故事名称
    @allure.title("保存修改的父节点	未授权当前节点，但是目标父节点已授权的销售区域人员需新增授权当前节点及下级节点的人、商、店进行自动授权")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17253(self, drivers):
        pass


@allure.feature("迭代一组V4_11")  # 迭代名称
class Teststory_2768:
    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_0、测试路径ShopManagementShopGrade")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17636(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_新增_1、新增门店等级时，在打开的弹窗中新增字段StatisticalDimension（统计维度），选项内容Month（月）、Quarter（季）。单选位置放在Brand筛选项下方")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17637(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_新增_2、ShopGradeList部分，MonthlySalesRange变更为QuarterlySalesRange（季度销售范围）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17638(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_新增_3、'Doyouagreetoautomaticallycalculatetheshopgradeonthe2ndofeverymonth,basedonthelastmonth039ssales?'提示语变更为")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17639(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_新增_4、其他地方维持不变，新增成功后手动触发一次更新")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17640(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_新增_5、月度文案维持原样不变")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17641(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_编辑_1、编辑门店等级时，在打开的弹窗中新增字段StatisticalDimension（统计维度），选项内容Month（月）、Quarter（季）。单选位置放在Brand筛选项下方")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17642(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_编辑_2、ShopGradeList部分，MonthlySalesRange变更为QuarterlySalesRange（季度销售范围）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17643(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_编辑_3、'Doyouagreetoautomaticallycalculatetheshopgradeonthe2ndofeverymonth,basedonthelastmonth039ssales?'提示语变更为")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17644(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_编辑_4、其他地方维持不变，编辑成功后手动触发一次更新")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17645(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_编辑_41、如果是从月度变更为季度，门店管理那边的门店等级相应变更为季度的展示（上期销量同步变更）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17646(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_编辑_42、如果是从季度变更为月度，门店管理那边的门店等级相应变更为月度的展示（上期销量同步变更）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17647(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_编辑_5、月度文案维持原样不变")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17648(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_列表_1、门店等级列表，新增字段StatisticalDimension（统计维度），根据统计维度的内容，将等级销售范围数据显示在SalesRange（销售范围）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17649(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_列表_2、字段MonthlySalesRange（月度销售范围）变更为SalesRange（销售范围）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17650(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_列表_3、新增按季度计算门店等级逻辑根据门店所在国家、品牌，获取关联的门店等级记录。若统计维度为季，根据门店ID、品牌、上季度日期范围（对应销售日期）作为查询条件，查询ShopSalesQuery的状态为Committed的记录，根据门店销售数据匹配季度等级范围，更新门店等级")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17651(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_列表_4、门店等级更新日期及上季度日期范围")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17652(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_列表_41、更新日期0102。上季度日期范围1001~1231")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17653(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_列表_42、更新日期0402。上季度日期范围0101~0331")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17654(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_列表_43、更新日期0702。上季度日期范围0401~0630")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17655(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_列表_44、更新日期1002。上季度日期范围0701~0930")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17656(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_导出_1、新增StatisticalDimension（统计维度）字段，位置与取值与列表页一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17657(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopGrade_测试点_导出_2、字段MonthlySalesRange（月度销售范围）变更为SalesRange（销售范围）。取值与列表页一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17658(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_0、测试路径ShopManagementShopManagementglobal")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17659(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_列表_1、ShopGrade字段提示语根据门店统计维度，做不同显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17660(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_列表_11、月度维持不变，仍为'Thecountrieswhereshopgradeareautomaticallycalculatedbysalesvolume,thisgradeiscalculatedbylastmonthsalesvolume.'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17661(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_列表_12、季度'Thecountrieswhereshopgradeareautomaticallycalculatedbysalesvolume,thisgradeiscalculatedbylastquartersalesvolume.'/'商店等级的国家是按销售量自动计算的。这个等级是按上一季度的销售量计算的。'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17662(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_列表_2、新增字段StatisticalDimension（统计维度），显示门店统计维度，位置在AutoCaculateorNot字段之后，显示具体的天数范围。例Month（10.01~10.31）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17663(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_列表_21、月度上月1号到最后一天")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17664(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_列表_22、季度上季度日期范围")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17665(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_列表_3、新增字段PreviousSales（上期销量），字段位置在StatisticalDimension（统计维度）之后。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17666(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_列表_31、根据门店ID、品牌、统计维度时间范围（对应销售日期）作为查询条件，查询ShopSalesQuery的所有销售日期包含在统计维度时间范围内的状态为Committed的记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17667(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_列表_311、月度统计维度时间范围等于上月1号~最后一天")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17668(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_列表_312、季度统计维度时间范围与按季度计算门店等级的上季度日期范围一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17669(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_列表_32、上期销量为快照数据，更新门店等级时记录的数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17670(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_列表_321、若品牌国家未设置自动更新门店等级，则该字段为空")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17671(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_列表_33、字段后新增提示语'Ifthebrandcountryisnotsettoautomaticallycalculatetheshoplevel,theshopwillnotcountthesalesofthepreviousperiod'/'如果品牌国家没有设置自动计算门店等级，门店不会统计上期销量'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17672(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_导出_1、新增StatisticalDimension（统计维度）字段，位置与取值与列表页一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17673(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（全球版）_测试点_导出_2、新增PreviousSales（上期销量）字段，位置与取值与列表页一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17674(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_0、测试路径ShopManagementShopManagementindia")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17675(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_列表_1、ShopGrade字段提示语根据门店统计维度，做不同显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17676(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_列表_11、月度维持不变，仍为'Thecountrieswhereshopgradeareautomaticallycalculatedbysalesvolume,thisgradeiscalculatedbylastmonthsalesvolume.'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17677(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_列表_12、季度'Thecountrieswhereshopgradeareautomaticallycalculatedbysalesvolume,thisgradeiscalculatedbylastquartersalesvolume.'/'商店等级的国家是按销售量自动计算的。这个等级是按上一季度的销售量计算的。'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17678(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_列表_2、新增字段StatisticalDimension（统计维度），显示门店统计维度，位置在AutoCaculateorNot字段之后，显示具体的天数范围。例Month（10.01~10.31）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17679(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_列表_21、月度上月1号到最后一天")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17680(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_列表_22、季度上季度日期范围")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17681(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_列表_3、新增字段PreviousSales（上期销量），字段位置在StatisticalDimension（统计维度）之后。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17682(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_列表_31、根据门店ID、品牌、统计维度时间范围（对应销售日期）作为查询条件，查询ShopSalesQuery的所有销售日期包含在统计维度时间范围内的状态为Committed的记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17683(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_列表_311、月度统计维度时间范围等于上月1号~最后一天")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17684(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_列表_312、季度统计维度时间范围与按季度计算门店等级的上季度日期范围一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17685(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_列表_32、上期销量为快照数据，更新门店等级时记录的数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17686(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_列表_321、若品牌国家未设置自动更新门店等级，则该字段为空")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17687(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_列表_33、字段后新增提示语'Ifthebrandcountryisnotsettoautomaticallycalculatetheshoplevel,theshopwillnotcountthesalesofthepreviousperiod'/'如果品牌国家没有设置自动计算门店等级，门店不会统计上期销量'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17688(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_导出_1、新增StatisticalDimension（统计维度）字段，位置与取值与列表页一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17689(self, drivers):
        pass


    @allure.story("门店等级按季度配置")  # 用户故事名称
    @allure.title("ShopMgt（印度版）_测试点_导出_2、新增PreviousSales（上期销量）字段，位置与取值与列表页一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17690(self, drivers):
        pass


@allure.feature("迭代一组V4_11")  # 迭代名称
class Teststory_2721:
    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_0、测试路径APP的ShopManagement（门店管理）应用")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18089(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_1、APP消息中心增加一个类型，ShopMonitoring（门店预警）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18090(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_2、消息推送到APP时，按配置的模板展示消息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18091(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_3、点击消息跳转到ShopManagement（门店管理）应用")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18092(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_新增筛选_0、ShopList选项卡中，RegionFilter右侧增加过滤条件（过滤图标展示？还是【Filter】按钮展示？），点击过滤图标是从右向左整屏显示筛选页Filter")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18093(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_新增筛选_01、未点击筛选时，【Filter】按钮的颜色是灰色。点击筛选项进行筛选后，【Filter】按钮的颜色才会是蓝色")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18094(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_新增筛选_02、点击筛选页Filter的【OK】按钮收起筛选页并根据选择的筛选项进行筛选，列表数据相应变化")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18095(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_新增筛选_03、点击筛选页Filter的重置按钮【Reset】重置筛选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18096(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_新增筛选_04、点击筛选页Filter的【lt】按钮收起筛选页")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18097(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_新增筛选_1、ManpowerType（人力类型）支持多选。有促无促，默认为All")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18098(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_新增筛选_11、可选择Manned（门店员工都是促销员），MannedFlexi（门店有员工是临时促销员），Unmanned（无促门店）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18099(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_新增筛选_111、统一规则门店有员工是促销员且是临时促销员时，ManpowerType是MannedFlexi")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18100(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_新增筛选_2、Brand（品牌）只支持单选，默认为All")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18101(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_新增筛选_21、内容源取DCR品牌管理表，受限于账户品牌权限")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18102(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_新增筛选_3、ShopType（门店类型）默认只有All，当选择品牌后，才会显示具体门店类型的可选项这边是单选？还是多选？")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18103(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_新增筛选_31、内容源取自数据字典定义")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18104(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店异常类型_1、ShopList选项卡中，RegionFilter下方增加门店异常类型展示（补货）、（达成率低）、（考勤定位）、（巡店定位）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18105(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店异常类型_11、并统计各异常的门店数量，标在后面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18106(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店异常类型_2、需要根据查询条件过滤统计")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18107(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店异常类型_3、点击（补货）/（达成率低）/（考勤定位）/（巡店定位），把对应的门店筛选出来")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18108(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店异常类型_4、如果管理的门店都没有异常，则不显示这一项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18109(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_列表门店信息展示_1、ShopList选项卡中，门店在现有的基础上增加显示以下信息ManpowerType（人力类型）、ShopType（门店类型）、ShopGrade（门店等级）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18110(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_列表门店信息展示_11、这三个信息跟在品牌后面，像小围标显示在一起")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18111(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_列表门店信息展示_12、这三个信息取值正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18112(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_1、ShopList选项卡中，点击门店进入的门店详情页面（ShopView）中，门店基础信息部分作如下优化")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18113(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_11、将ShopType（门店类型）、Grade（门店等级）作为小图标移到上面，展示在ManpowerType（人力类型）后面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18114(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_12、增加区域显示，从二级区域开始显示，以点隔开位置在ShopID下面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18115(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_121、格式为RegionWest.Malaysia")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18116(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_13、增加促销员的显示，如果没有则不显示。如果有多个，逗号隔开，最多显示两行位置在Region下面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18117(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_131、格式为PromoterPromoterNamePromoterID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18118(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_14、增加门店上级显示。如果有多个，逗号隔开，最多显示两行位置在Promoter下面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18119(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_141、格式为SuperiorSuperiorNameSuperiorID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18120(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_15、ShopAddress、ContactName、ContactNo位置往后移")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18121(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_2、ShopList选项卡中，点击门店进入的门店详情页面（ShopView）中，门店基础信息部分下方的内容归为页签Overview（概览）含MonthlySales、Inventory、Assets、DemoPhone、VisitingRecords")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18122(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3、ShopList选项卡中，点击门店进入的门店详情页面（ShopView）中，门店基础信息部分下方新增页签Warning（预警）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18123(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_31、预警显示该门店的异常信息每一个卡片为一个异常信息，由后台决定是否显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18124(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_311、卡片里的内容，包括标题也由后台确定")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18125(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_32、如果有异常，页签Warning（预警）上显示小红点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18126(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_33、目前有五种异常卡片信息Replenishment（补货）、ModelSalesAch（机型达成）、ShopSalesAch（门店达成）、Attendance（考勤）、Visit（巡店）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18127(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_331、Replenishment（补货）表格形式展示4列信息，分别是Model、Inventory、Dos、Replenishment（Replenishment列的数据标红显示）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18128(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3311、Model大数据推送过来的补货异常的Model")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18129(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3312、Inventory大数据推送过来的补货异常的Model所对应的Inventory")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18130(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3313、Dos大数据推送过来的补货异常的Model所对应的DOS")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18131(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3314、Replenishment大数据推送过来的补货异常的Model所对应的Replenishment")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18132(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_332、ModelSalesAch（机型达成）表格形式展示4列信息，分别是Model、Sales、Target、Ach（Ach列的数据标红显示）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18133(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3321、Model大数据推送过来的机型达成异常的Model")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18134(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3322、Sales大数据推送过来的机型达成异常的Model所对应的Sales")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18135(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3323、Target大数据推送过来的机型达成异常的Model所对应的Target")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18136(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3324、Ach大数据推送过来的机型达成异常的Model所对应的Ach")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18137(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_333、ShopSalesAch（门店达成）表格形式展示3列信息，分别是Sales、Target、Ach（Ach列的数据标红显示）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18138(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3331、Sales大数据推送过来的门店达成异常的门店所对应的Sales")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18139(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3332、Target大数据推送过来的门店达成异常的门店所对应的Target")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18140(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3333、Ach大数据推送过来的门店达成异常的门店所对应的Ach")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18141(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_334、Attendance（考勤）表格形式展示3列信息，分别是Staff、Date、Distance（Distance列的数据标红显示）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18142(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3341、Staff大数据推送过来的考勤定位距离异常的考勤所对应的用户信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18143(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3342、Date大数据推送过来的考勤定位距离异常的考勤所对应的打卡时间")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18144(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3343、Distance大数据推送过来的考勤定位距离异常的考勤所对应的考勤定位距离")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18145(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_335、Visit（巡店）表格形式展示3列信息，分别是Staff、Date、Distance（Distance列的数据标红显示）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18146(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3351、Staff大数据推送过来的巡店定位距离异常的巡店所对应的用户信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18147(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3352、Date大数据推送过来的巡店定位距离异常的巡店所对应的打卡时间")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18148(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3353、Distance大数据推送过来的巡店定位距离异常的巡店所对应的巡店定位距离")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18149(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_34、五个异常卡片信息下方显示Feedback（反馈）输入框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18150(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_341、可以填写内容，提交反馈，最大填写512字")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18151(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_342、填写后点击【Submit】按钮提交的内容，需要记录以下信息门店ID、反馈时间、反馈内容、反馈人")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18152(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_3421、内容在WEB端的零售运营分析报表（ReportAnalysisRetailOperationAnalysis）的门店维度查看")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18153(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_343、如果没有异常信息，则不显示该反馈输入框不展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18154(self, drivers):
        pass


    @allure.story("门店运营异常推送/APP门店异常指标查看并反馈")  # 用户故事名称
    @allure.title("测试点_ShopMgt_门店详情_344、每个人、每个店只能提交一次。如果提交过，这边把内容显示出来，不可编辑，隐藏提交按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18155(self, drivers):
        pass


@allure.feature("迭代一组V4_11")  # 迭代名称
class Teststory_2719:
    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_MonitoringTemplate_0、测试路径GTMManagementMonitoringTemplate")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18195(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_MonitoringTemplate_1、在点击【Add】按钮打开的MonitoringTemplateAdd页面，增加门店异常推送的模板")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18196(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_MonitoringTemplate_11、MonitorType筛选项那边增加门店异常推送的类型ShopMonitoring（门店预警）原来只有SaleMonitor、InventoryMonitor两个选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18197(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_MonitoringTemplate_12、选择'ShopMonitoring'后，Item、ShopType、ImageType、ManpowerType为非必填选择SaleMonitor/InventoryMonitor时全部都为必填项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18198(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_MonitoringTemplate_13、新增门店异常推送正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18199(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_MonitoringTemplate_14、配置好预警监控模板后，大数据那边就会按模板的规则进行消息推送")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18200(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_MonitoringTemplate_15、配置好预警监控模板后又进行了模板修改操作，大数据那边以最新的模板规则进行消息推送")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18201(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_PushSetting_0、测试路径BasicDataManagementPushData，点击Setpush进入的PushSetting页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18202(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_PushSetting_1、在消息推送设置中，添加门店预警推送内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18203(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_PushSetting_2、Messagetype增加一个类型，ShopMonitoring")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18204(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_PushSetting_3、推送内容Title（标题）ShopMonitoringTask")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18205(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_PushSetting_4、推送内容Statement（内容）''/'有家门店的指标存在异常，请及时查看，并给出反馈'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18206(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_PushSetting_5、新增门店预警推送消息正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18207(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_PushSetting_6、PushData页面同步新增ShopMonitoring类型")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18208(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_PushSetting_7、PushData页面查询正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18209(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_PushSetting_8、PushData页面导出正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18210(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_PushSetting_9、推送规则的模板和消息模板都配置好后，系统就会按规则，查找零售运营分析报表中有异常的门店（从大数据推送过来的），如果有符合的门店，就会给用户推送消息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18211(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_PushSetting_91、用户收到的推送消息正常记录在PushData页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18212(self, drivers):
        pass


    @allure.story("门店运营异常推送/门店异常指标消息推送")  # 用户故事名称
    @allure.title("测试点_PushSetting_92、用户收到的推送消息正常记录在PushRecord页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18213(self, drivers):
        pass


@allure.feature("迭代一组V4_11")  # 迭代名称
class Teststory_2718:
    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_0、测试路径ReportAnalysisRetailOperationAnalysis")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18224(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_1、需要跟踪的异常指标有五个门店达成率（在门店维度中增加）、机型达成率（在机型维度中增加）、门店补货（在机型、门店维度中增加）、考勤距离（在人员维度中增加）、巡店距离（在人员维度中增加）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18225(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_11、数据来源于大数据推送")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18226(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_2、需要增加APP反馈的内容反馈内容、反馈人、反馈时间（在门店维度中增加）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18227(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_21、取值逻辑根据日期和门店关联APP反馈内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18228(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_211、如果一天有多个反馈，只显示最新的")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18229(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_3、四个维度查询正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18230(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_4、四个维度导出正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18231(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_5、100万数据，20并发，3s响应这个要压测吗？")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18232(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_Shop维度_1、（MTD月达成率）在门店维度中增加字段'MTD月达成率'，位置放在Target（目标销量）后面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18233(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_Shop维度_11、MTD月达成率=MTD销量/（目标销量本月已过天数/本月总天数）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18234(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_Shop维度_2、Replenishment（建议补货量）在门店维度中增加字段'Replenishment'，位置放在InfiltrationSales（上报窜货数量）后面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18235(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_Shop维度_21、每日快照数据。根据DCR补货报表中各机型补货量的汇总")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18236(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_Shop维度_3、Feedback（反馈内容）在门店维度中增加字段'Feedback'，位置放在Replenishment（建议补货量）后面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18237(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_Shop维度_31、APP提交的反馈内容")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18238(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_Shop维度_4、Submitter（反馈人）在门店维度中增加字段'Submitter'，位置放在Feedback（反馈内容）后面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18239(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_Shop维度_41、APP提交反馈内容的用户")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18240(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_Shop维度_5、FeedbackDate（反馈时间）在门店维度中增加字段'FeedbackDate'，位置放在Submitter（反馈人）后面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18241(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_Shop维度_51、APP提交的反馈内容的时间")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18242(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_Model维度_1、（MTD月达成率）在机型维度中增加字段'MTD月达成率'，位置放在YTDTarget（YTD目标销量）后面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18243(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_Model维度_11、MTD月达成率=MTD销量/（目标销量本月已过天数/本月总天数）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18244(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_Model维度_2、Replenishment（建议补货量）在机型维度中增加字段'Replenishment'，位置放在DOS28（28天DOS）后面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18245(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_Model维度_21、每日快照数据。根据DCR补货报表中各机型补货量的汇总")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18246(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_SalesUploader维度_1、AttendanceDistance（考勤距离）在销量上报人维度中增加字段'AttendanceDistance'，位置放在TotalAttendances（考勤次数）后面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18247(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_SalesUploader维度_11、多个距离用逗号隔开")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18248(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_SalesUploader维度_2、TotalVisits（巡店次数）在销量上报人维度中增加字段'TotalVisits'，位置放在AttendanceDistance（考勤距离）后面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18249(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_SalesUploader维度_21、按天统计人员的巡店次数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18250(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_SalesUploader维度_3、VisitDistance（巡店距离）在销量上报人维度中增加字段'VisitDistance'，位置放在TotalVisits（巡店次数）后面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18251(self, drivers):
        pass


    @allure.story("门店运营异常推送/零售运营报表增加异常指标")  # 用户故事名称
    @allure.title("测试点_SalesUploader维度_31、多个距离用逗号隔开")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18252(self, drivers):
        pass


@allure.feature("迭代一组V4_11")  # 迭代名称
class Teststory_2720:
    @allure.story("门店运营异常推送/设置门店异常指标的标准值")  # 用户故事名称
    @allure.title("测试点_0、测试路径SystemManagementFunctionSetting")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18262(self, drivers):
        pass


    @allure.story("门店运营异常推送/设置门店异常指标的标准值")  # 用户故事名称
    @allure.title("测试点_1、增加两个配置项，来配置考勤定位距离、巡店定位距离的标准值")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18263(self, drivers):
        pass


    @allure.story("门店运营异常推送/设置门店异常指标的标准值")  # 用户故事名称
    @allure.title("测试点_2、Attendancelocationdistancewarningvalue（考勤定位距离预警值）支持按门店的国家、品牌配置")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18264(self, drivers):
        pass


    @allure.story("门店运营异常推送/设置门店异常指标的标准值")  # 用户故事名称
    @allure.title("测试点_3、Visitinglocationdistancewarningvalue（巡店定位距离预警值）支持按门店的国家、品牌配置")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18265(self, drivers):
        pass


    @allure.story("门店运营异常推送/设置门店异常指标的标准值")  # 用户故事名称
    @allure.title("测试点_4、可正常配置考勤定位距离预警值和巡店定位距离预警值")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18266(self, drivers):
        pass


    @allure.story("门店运营异常推送/设置门店异常指标的标准值")  # 用户故事名称
    @allure.title("测试点_5、大数据读取这里的配置项，来计算考勤定位、巡店定位是否异常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18267(self, drivers):
        pass


if __name__ == '__main__':
    pass
