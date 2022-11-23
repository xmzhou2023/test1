import allure
import pytest
@allure.feature("迭代二组V4_10")  # 迭代名称
class Teststory_2090:
    @allure.story("礼品返利，增加礼品价值金额字段")  # 用户故事名称
    @allure.title("选择礼品返利时，增加礼品单价金额字段GiftUnitPrice（本地币，例如PKR）非必填项")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10827(self, drivers):
        pass


    @allure.story("礼品返利，增加礼品价值金额字段")  # 用户故事名称
    @allure.title("单价金额只允许正整数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10828(self, drivers):
        pass


    @allure.story("礼品返利，增加礼品价值金额字段")  # 用户故事名称
    @allure.title("仅支持9个9")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10829(self, drivers):
        pass


    @allure.story("礼品返利，增加礼品价值金额字段")  # 用户故事名称
    @allure.title("保留两位小数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10830(self, drivers):
        pass


    @allure.story("礼品返利，增加礼品价值金额字段")  # 用户故事名称
    @allure.title("返利管理总表和返利reportUser维度（total表），需要加上礼品总金额GiftAmount（LocalCurrency），GiftAmount（）.导出同步增加")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10831(self, drivers):
        pass


    @allure.story("礼品返利，增加礼品价值金额字段")  # 用户故事名称
    @allure.title("返利reportUser维度（3个维度子表）,在gift字段右边增加GiftAmount（LocalCurrency），GiftAmount（），显示该对象获得礼品价值金额。导出同步增加。")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10832(self, drivers):
        pass


    @allure.story("礼品返利，增加礼品价值金额字段")  # 用户故事名称
    @allure.title("返利reportitem维度，在gift字段右边增加GiftAmount（LocalCurrency），GiftAmount（），显示礼品机型对应的分摊礼品金额。导出同步增加。")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10833(self, drivers):
        pass


    @allure.story("礼品返利，增加礼品价值金额字段")  # 用户故事名称
    @allure.title("礼品金额返利计算组合回归")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10834(self, drivers):
        pass


    @allure.story("礼品返利，增加礼品价值金额字段")  # 用户故事名称
    @allure.title("金额推送fol成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10835(self, drivers):
        pass


@allure.feature("迭代二组V4_10")  # 迭代名称
class Teststory_2091:
    @allure.story("返利对象（人员、客户、门店），去掉启用和禁用状态校验")  # 用户故事名称
    @allure.title("返利参与者人员、对象和门店均不校验状态")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10836(self, drivers):
        pass


    @allure.story("返利对象（人员、客户、门店），去掉启用和禁用状态校验")  # 用户故事名称
    @allure.title("回归所有计算场景")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10837(self, drivers):
        pass


@allure.feature("迭代二组V4_10")  # 迭代名称
class Teststory_2092:
    @allure.story("返利ReportitemCustomer优化，按国包维度拆分机型。")  # 用户故事名称
    @allure.title("item报表Custome维度，列表增加国包Customeid和Customename字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11084(self, drivers):
        pass


    @allure.story("返利ReportitemCustomer优化，按国包维度拆分机型。")  # 用户故事名称
    @allure.title("根据当前返利对应机型，从哪个国包拿货就显示该国包信息。对应的机型数量，多个国包，多行显示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11085(self, drivers):
        pass


    @allure.story("返利ReportitemCustomer优化，按国包维度拆分机型。")  # 用户故事名称
    @allure.title("导出同步增加")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11086(self, drivers):
        pass


    @allure.story("返利ReportitemCustomer优化，按国包维度拆分机型。")  # 用户故事名称
    @allure.title("列表的拆分逻辑由之前的机型维度，改为国包机型维度")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11087(self, drivers):
        pass


    @allure.story("返利ReportitemCustomer优化，按国包维度拆分机型。")  # 用户故事名称
    @allure.title("推送fol对应国包才会有数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11088(self, drivers):
        pass


    @allure.story("返利ReportitemCustomer优化，按国包维度拆分机型。")  # 用户故事名称
    @allure.title("回归与fol对接流程")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11089(self, drivers):
        pass


@allure.feature("迭代二组V4_10")  # 迭代名称
class Teststory_2093:
    @allure.story("新增返利政策，增加国家选择框")  # 用户故事名称
    @allure.title("国家为必填字段，销售区域为非必填字段；")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11102(self, drivers):
        pass


    @allure.story("新增返利政策，增加国家选择框")  # 用户故事名称
    @allure.title("国家字段增加在销售区域上")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11103(self, drivers):
        pass


    @allure.story("新增返利政策，增加国家选择框")  # 用户故事名称
    @allure.title("国家的选项，仅展示账户授权的国家（根据销售区域授权下的国家展示）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11104(self, drivers):
        pass


    @allure.story("新增返利政策，增加国家选择框")  # 用户故事名称
    @allure.title("如果国家选中，销售区域默认显示选中的国家以下的销售区域")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11105(self, drivers):
        pass


    @allure.story("新增返利政策，增加国家选择框")  # 用户故事名称
    @allure.title("通过国家控制销售区域")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11106(self, drivers):
        pass


    @allure.story("新增返利政策，增加国家选择框")  # 用户故事名称
    @allure.title("先选择销售区域再选择国家如果不一致时系统提示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11107(self, drivers):
        pass


    @allure.story("新增返利政策，增加国家选择框")  # 用户故事名称
    @allure.title("销售区域和国家同时选中取最小层级")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11108(self, drivers):
        pass


@allure.feature("迭代二组V4_10")  # 迭代名称
class Teststory_1712:
    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("未配置菜单权限时页面不展示改功能页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11171(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("报表的数据权限为品牌门店的数据权限")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11253(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("门店运营分析报表的UI与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11254(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("门店运营分析报表进入默认展示门店指标维度的报表数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11255(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("点击search按钮可以查询出对应的筛选条件的数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11256(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("点击Reset按钮可以清空对应的筛选条件的数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11257(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("点击Export按钮可以导出对应的查询维度的列表数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11258(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("导出为异步导出")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11259(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("导出的数据与筛选查询字段一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11260(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("大数据量的情况下的导出性能支持")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11261(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("导出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11262(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("报表的维度可任意切换、切换对应的报表字段的数据与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11263(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("页签切回时保留上次的操作状态，含条件筛选、字段勾选、查询状态等")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11264(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("tab页的切换及跳转")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11265(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("点击Fold/Unfold可以展开收缩对应的查询条件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11266(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表UI显示与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11267(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表报表筛选字段与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11268(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表报表时间字段筛选条件为时间筛选框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11269(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表报表时间筛选终止时间不能小于起始时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11270(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表shop字段筛选支持门店编码及门店名称模糊搜索")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11271(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表shop筛选字段支持复制粘贴")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11272(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表门店状态来源于DCR门店状态")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11273(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表门店状态下拉选择显示Pending、Rejected、Enabled、Disabled状态")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11274(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表门店状态选择对应的状态可搜索出对应的查询数据信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11275(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表Brand数据来源于DCR的品牌数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11276(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表Brand下拉多选、支持模糊搜索/精确搜索")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11277(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表Country数据来源于DCR国家数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11278(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表Country下拉选择支持单选及多选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11279(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表Country支持模糊搜索/精确搜索")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11280(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表salesRegion数据来源于DCR系统")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11281(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表salesRegion下拉选择支持模糊搜索/精确搜索")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11282(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表ShopInfo字段筛选下拉单选最新和历史")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11283(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表选择对应的查询条件可以筛选出对应的查询条件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11284(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表默认显示维度字段的数据信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11285(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表点击切换维度时指标时对应的字段切换")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11286(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表点击字段的筛选弹框弹出页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11287(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表弹框页面的数据字段与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11288(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表默认勾选的必选字段与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11289(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表取消勾选后列表随之取消该字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11290(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表选择该字段后列表随之增加该字段数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11291(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表取消/勾选的字段在固定的栏位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11292(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表必选字段不可取消勾选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11293(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表点击切换指标")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11294(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表展示指标字段与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11295(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表指标取消勾选后列表随之取消该字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11296(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表指标选择该字段后列表增加该字段数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11297(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表指标取消/勾选的字段在固定的栏位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11298(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("shop报表指标取消/勾选的字段在固定的栏位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11299(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("SalesUploader报表UI显示与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11301(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("SalesUploader报表筛选字段与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11302(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("SalesUploader报表时间字段筛选条件为时间筛选框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11304(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("SalesUploader报表时间筛选终止时间不能小于起始时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11305(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("SalesUploader报表筛选字段与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11306(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("SalesUploader报表筛选字段可筛选出对应的数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11307(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表UI显示与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11308(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表筛选字段与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11309(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表时间字段筛选条件为时间筛选框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11310(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表时间筛选终止时间不能小于起始时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11311(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表Brand数据来源于DCR的品牌数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11312(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表Brand下拉多选、支持模糊搜索/精确搜索")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11313(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表Country数据来源于DCR国家数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11314(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表Country下拉选择支持单选及多选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11315(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表Country支持模糊搜索/精确搜索")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11316(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表shop字段筛选支持门店编码及门店名称模糊搜索")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11317(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表shop筛选字段支持复制粘贴")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11318(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表门店状态来源于DCR门店状态")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11319(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表门店状态下拉选择显示Pending、Rejected、Enabled、Disabled状态")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11320(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表门店状态选择对应的状态可搜索出对应的查询数据信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11321(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表salesRegion数据来源于DCR系统")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11322(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表salesRegion下拉选择支持模糊搜索/精确搜索")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11323(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表Modl支持复制粘贴")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11324(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表Modl支持模糊筛选、多选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11325(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表MarketName支持复制粘贴查询")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11326(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表SP/FP字段支持模糊搜索")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11327(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表SP/FP字段支持复制粘贴")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11328(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("Model报表ShopInfo可选择查询")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11329(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("UploaderModel报表UI显示与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11330(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("UploaderModel报表筛选字段与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11331(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("UploaderModel报表时间字段筛选条件为时间筛选框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11332(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("UploaderModel报表时间筛选终止时间不能小于起始时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11333(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("UploaderModel报表筛选字段与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11334(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("UploaderModel报表选择对应的筛选条件可查看对应的数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11335(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("筛选条件支持单个条件查询")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11336(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("筛选条件是否支持多个组合条件查询")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11337(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("quot点击ColumnConfiguration时弹框弹出选择条件的字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11338(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("切换不同的维度时点击ColumnConfiguration对应的列表字段与需求一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11340(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("ColumnConfiguration页面的必选字段置灰显示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11341(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("取消勾选后列表随之取消该字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11342(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("选择该字段后列表随之增加该字段数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11343(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("取消/勾选的字段在固定的栏位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11344(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("必选字段不可取消勾选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11345(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("选择最新时默认展示当天列表维度最新的数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11346(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("选择历史时默认显示当天之前的数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11347(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("列表数据展示的字段与下方勾选的字段一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11348(self, drivers):
        pass


    @allure.story("门店运营分析报表")  # 用户故事名称
    @allure.title("展示的维度字段与需求字段一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_11349(self, drivers):
        pass


@allure.feature("迭代二组V4_10")  # 迭代名称
class Teststory_2089:
    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("Import按钮根据菜单权限配置")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12025(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("点击Import弹框弹出导入页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12026(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("点击Template可以下载导入的模版")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12027(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("导入模版名称VisitShopPlanTemplate")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12028(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("点击Upload可选择Excel文件上传")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12029(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("只支持Excel表格上传")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12030(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("点击ImportRecord可跳转到对应的页面查看对应的上传信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12031(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("未选择数据点击save时系统给出对应的提示信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12032(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("点击Cancel关闭导入页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12033(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("点击右上角的X可以关闭页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12034(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("选择文件点击Save文件上传成功且给出对应的提示信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12035(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("成功后点击弹框提示信息可跳转至对应的上传文件页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12036(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("WEB列表增加字段SourceType【来源类型】、VisitorUser、VisitorUserName")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12037(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("SourceType字段显示类型有APPAdd、WEBImport")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12038(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("导出字段同列表一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12039(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("PlanVisitDate为必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12040(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("填写过去的时间日期时失败系统提示PlanVisitDatecanonlybeenteredfortodayorfuturedates.")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12041(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("中文巡店日期只能输入今天或未来的日期。")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12042(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("巡店日期未规范的时间填写系统提示日期错误提示Pleaseentercorrectdateformat，Forexample20221001.请输入正确的日期格式，例如20221001.")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12043(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("PlanVisitUserID为必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12044(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("PlanVisitUserID导入的人员ID需为DCR的账户数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12045(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("非法填写导入失败提示PlanVisitorUserIDisincorrect,pleasereenter.中文巡店者编号不正确，请重新输入。")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12046(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("导入的人员ID需要有对应的权限信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12047(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("导入的人员ID需要有对应的权限信息导入失败的提示YouarenotauthorizedtocreatevisitplanforthisuserID，Pleasecontacttheadmin.中文您无权为此用户创建巡店计划，请联系管理员。")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12048(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("PlanVisitShopID为必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12049(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("PlanVisitShopID导入的门店ID需为DCR的门店ID数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12050(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("非法填写导入失败提示PlanVisitorShopIDisincorrect,pleasereenter.中文巡店的门店编号不正确，请重新输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12051(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("导入的门店ID需要导入的巡店人员ID有对应的权限信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12052(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("导入需要有对应的权限信息提示YouarenotauthorizedtocreatevisitplanforthisshopID，Pleasecontacttheadmin.中文您无权为此门店创建巡店计划，请联系管理员。")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12053(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("已导入的数据再次导入时导入失败")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12054(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("quot同一个用户当天已创建巡店计划后再次导入当天的计划时导入失败提示ThePlanVisitDate,thisuserhasalreadycreatedavisitplan，noneedcreateitagain.")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12055(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("中文该巡店日期，用户已经创建了一个巡店计划，无需重复创建。quot")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12056(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("同一个用户有对应的不同的门店信息时可导入不同的计划")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12057(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("导入未来的时间的巡店模版导入成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12058(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("APP端已新有巡店记录时导入失败")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12059(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("任意必填项未填写时导入失败时产生对应的提示信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12060(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("导入模版含空格时导入时系统自动去除空格信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12061(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("同个Excel表中导入不同的数据填写符合信息导入成功")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12062(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("同个Excel表中导入数据中不符合的导入失败符合的导入成功失败的给出对应的提示信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12063(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("APP端由现在的判断=创建者mine，改为判断巡店执行者")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12064(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("WEB导入的VisitorUser为APP端的巡店执行者")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12065(self, drivers):
        pass


    @allure.story("WEB巡店计划增加导入功能")  # 用户故事名称
    @allure.title("WEB导入的执行计划APP端不可关闭，Close按钮隐藏")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12066(self, drivers):
        pass


@allure.feature("迭代二组V4_10")  # 迭代名称
class Teststory_2098:
    @allure.story("【APP】门店绩效达成优化")  # 用户故事名称
    @allure.title("销售区域对应二级、三级、四级区域")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12112(self, drivers):
        pass


    @allure.story("【APP】门店绩效达成优化")  # 用户故事名称
    @allure.title("sold字段修改为ValidAchieved")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12113(self, drivers):
        pass


    @allure.story("【APP】门店绩效达成优化")  # 用户故事名称
    @allure.title("app字段ValidAchieved字段取web端SalesRegionAchievement报表ValidSales字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12114(self, drivers):
        pass


    @allure.story("【APP】门店绩效达成优化")  # 用户故事名称
    @allure.title("ValidAch取web端SalesRegionAchievement报表ValidSalesAch字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12115(self, drivers):
        pass


    @allure.story("【APP】门店绩效达成优化")  # 用户故事名称
    @allure.title("筛选项对全局数据生效")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12116(self, drivers):
        pass


    @allure.story("【APP】门店绩效达成优化")  # 用户故事名称
    @allure.title("app端数据与web端数据保持一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12117(self, drivers):
        pass


    @allure.story("【APP】门店绩效达成优化")  # 用户故事名称
    @allure.title("原Target字段文案调整为MyMyTarget。取值不变")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12118(self, drivers):
        pass


    @allure.story("【APP】门店绩效达成优化")  # 用户故事名称
    @allure.title("ValidAchValidAchieved/MyTarget")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12119(self, drivers):
        pass


    @allure.story("【APP】门店绩效达成优化")  # 用户故事名称
    @allure.title("新增UploadSales当前销售区域的上报销量")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12120(self, drivers):
        pass


    @allure.story("【APP】门店绩效达成优化")  # 用户故事名称
    @allure.title("新增UploadAchUploadSales/MyTarget")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12121(self, drivers):
        pass


    @allure.story("【APP】门店绩效达成优化")  # 用户故事名称
    @allure.title("原有的上报销量取值更改为当前销售区域的有效销量")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12122(self, drivers):
        pass


    @allure.story("【APP】门店绩效达成优化")  # 用户故事名称
    @allure.title("达成进度图ValidAchieved/MyTarget")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12123(self, drivers):
        pass


@allure.feature("迭代二组V4_10")  # 迭代名称
class Teststory_2088:
    @allure.story("巡店模板增加复制、拖动调整顺序、修改中文翻译")  # 用户故事名称
    @allure.title("中文模式下的店内基本检查优化为巡店模版设置")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12190(self, drivers):
        pass


    @allure.story("巡店模板增加复制、拖动调整顺序、修改中文翻译")  # 用户故事名称
    @allure.title("菜单权限增加Copy按钮权限")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12191(self, drivers):
        pass


    @allure.story("巡店模板增加复制、拖动调整顺序、修改中文翻译")  # 用户故事名称
    @allure.title("未选择数据时点击Copy时系统给出对应的提示信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12192(self, drivers):
        pass


    @allure.story("巡店模板增加复制、拖动调整顺序、修改中文翻译")  # 用户故事名称
    @allure.title("选择多条数据点击Copy时系统给出对应的提示信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12193(self, drivers):
        pass


    @allure.story("巡店模板增加复制、拖动调整顺序、修改中文翻译")  # 用户故事名称
    @allure.title("Copy只支持单条数据Copy")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12194(self, drivers):
        pass


    @allure.story("巡店模板增加复制、拖动调整顺序、修改中文翻译")  # 用户故事名称
    @allure.title("Copy只能CP对应的权限的数据模版")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12195(self, drivers):
        pass


    @allure.story("巡店模板增加复制、拖动调整顺序、修改中文翻译")  # 用户故事名称
    @allure.title("组内支持顺序调整")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12196(self, drivers):
        pass


    @allure.story("巡店模板增加复制、拖动调整顺序、修改中文翻译")  # 用户故事名称
    @allure.title("整个模版支持整个组调顺序")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12197(self, drivers):
        pass


    @allure.story("巡店模板增加复制、拖动调整顺序、修改中文翻译")  # 用户故事名称
    @allure.title("组调顺序时对应的组内的顺序不改变")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12198(self, drivers):
        pass


    @allure.story("巡店模板增加复制、拖动调整顺序、修改中文翻译")  # 用户故事名称
    @allure.title("组调顺序时整个组顺序一起变动")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12199(self, drivers):
        pass


    @allure.story("巡店模板增加复制、拖动调整顺序、修改中文翻译")  # 用户故事名称
    @allure.title("顺序的调整支持Copy、编辑、新增")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12200(self, drivers):
        pass


    @allure.story("巡店模板增加复制、拖动调整顺序、修改中文翻译")  # 用户故事名称
    @allure.title("当顺序变动时APP端的巡店模版顺序对应的做变动")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_12201(self, drivers):
        pass


@allure.feature("迭代二组V4_10")  # 迭代名称
class Teststory_2100:
    @allure.story("新增样机下样无限制配置")  # 用户故事名称
    @allure.title("APP1、新增DemoPhoneRetiredRestriction配置项")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13092(self, drivers):
        pass


    @allure.story("新增样机下样无限制配置")  # 用户故事名称
    @allure.title("web11、Value等于1时，发布范围内的零售商关联门店可直接对类型为Branddemodevice、Commonowner的样机直接下样，无需判断上样时间是否小于等于90天")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13093(self, drivers):
        pass


    @allure.story("新增样机下样无限制配置")  # 用户故事名称
    @allure.title("APP2、样机类型为Branddemodevice、Commonowner的样机，判断上样时间小于等于90天且门店关联零售商无关联Value等于1的DemoPhoneRetiredRestriction配置项，下样（Retired）按钮置灰，页面出现提示语")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13094(self, drivers):
        pass


    @allure.story("新增样机下样无限制配置")  # 用户故事名称
    @allure.title("APP21、提示语此设备的上样时间小于为90天，不能下样，支持多语言")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13095(self, drivers):
        pass


    @allure.story("新增样机下样无限制配置")  # 用户故事名称
    @allure.title("APP4、下样后的imei可以重新上样")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13096(self, drivers):
        pass


    @allure.story("新增样机下样无限制配置")  # 用户故事名称
    @allure.title("零售商多品牌的情况下，通过品牌国家客户类型配置，门店的品牌和配置项品牌一样才生效")  # 用例名称
    @allure.description("零售商idPK4500203")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13729(self, drivers):
        pass


@allure.feature("迭代二组V4_10")  # 迭代名称
class Teststory_1713:
    @allure.story("移动端门店编码获取优化")  # 用户故事名称
    @allure.title("当门店数据出现修改时APP取最新修改的门店数据信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14366(self, drivers):
        pass


    @allure.story("移动端门店编码获取优化")  # 用户故事名称
    @allure.title("WEB更改编码后APP端实时获取")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14367(self, drivers):
        pass


    @allure.story("移动端门店编码获取优化")  # 用户故事名称
    @allure.title("APP端登录后只能查看到对应的一条门店的数信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14368(self, drivers):
        pass


    @allure.story("移动端门店编码获取优化")  # 用户故事名称
    @allure.title("禁用的状态下转启用后登录查看对应的门店是否只有一条门店的数据信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14369(self, drivers):
        pass


    @allure.story("移动端门店编码获取优化")  # 用户故事名称
    @allure.title("禁用的状态下转启用后登录查看对应的门店是否只有一条门店的数据信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14370(self, drivers):
        pass


    @allure.story("移动端门店编码获取优化")  # 用户故事名称
    @allure.title("授权多个门店时登录是否可查看到对应的门店数据信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14371(self, drivers):
        pass


    @allure.story("移动端门店编码获取优化")  # 用户故事名称
    @allure.title("已授权的门店解除授权后登录查看对应的门店信息是否不可查看")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14372(self, drivers):
        pass


    @allure.story("移动端门店编码获取优化")  # 用户故事名称
    @allure.title("单个品牌的门店扩展多个品牌时查看对应的门店是否增加")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14373(self, drivers):
        pass


    @allure.story("移动端门店编码获取优化")  # 用户故事名称
    @allure.title("门店品牌删除后对应的数据信息是否不可查看")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14374(self, drivers):
        pass


if __name__ == '__main__':
      pass
