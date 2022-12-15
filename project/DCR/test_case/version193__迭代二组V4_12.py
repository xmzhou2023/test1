import allure
import pytest
@allure.feature("迭代二组V4_12")  # 迭代名称
class Teststory_3120:
    @allure.story("考勤统计页导出优化为异步导出")  # 用户故事名称
    @allure.title("1、点击Web端考勤统计页面，导出按钮，调用DCR异步导出方式")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19825(self, drivers):
        pass


    @allure.story("考勤统计页导出优化为异步导出")  # 用户故事名称
    @allure.title("2、导出列表列宽25，其他样式为DCR异步导出通用样式。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19826(self, drivers):
        pass


    @allure.story("考勤统计页导出优化为异步导出")  # 用户故事名称
    @allure.title("3、导出列表内容与web显示一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19827(self, drivers):
        pass


    @allure.story("考勤统计页导出优化为异步导出")  # 用户故事名称
    @allure.title("31、筛选项，组合条件查询出结果，点击导出，导出内容与web查询结果一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19828(self, drivers):
        pass


    @allure.story("考勤统计页导出优化为异步导出")  # 用户故事名称
    @allure.title("32、筛选项，单条件查询出结果，点击导出，导出内容与web查询结果一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19829(self, drivers):
        pass


    @allure.story("考勤统计页导出优化为异步导出")  # 用户故事名称
    @allure.title("冒烟考勤统计页面导出功能正常，不报错")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19830(self, drivers):
        pass


@allure.feature("迭代二组V4_12")  # 迭代名称
class Teststory_3150:
    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("APP销量上报页面底部添加Gender,Age选择题")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19842(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("消费者性别的选项（下拉弹框显示男、女）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19843(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("消费者年龄的选项（下拉弹框显示017、1824、2534、3544、4554、55）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19844(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("web销量上报页面列表字段POSID后添加ConsumerGender、ConsumerAge字段")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19845(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("导出增加ConsumerGender、ConsumerAge字段")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19846(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("角色菜单配置内CustomerInfo更改为ConsumerInfo")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19847(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("CustomerCollect_Mandatory更改为ConsumerCollect_Mandatory")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19848(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("CustomerCollect_Nonmandatory更改为ConsumerCollect_Mandatory")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19849(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("列表ConsumerAge字段后新增供应商字段SupplierID和SupplierName")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19850(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("导出增加SupplierID和SupplierName")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19851(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("供应商取值逻辑门店的所属零售商为Buyer的出库单中的Seller。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19852(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("不做任何渠道流转数据情况下直接销量上报则供应商字段为空")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19853(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("Supplier新增筛选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19854(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("支持模糊搜索")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19855(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("支持批量粘贴")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19856(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("销量上报列表字段MidHigh更改为ModelType")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19857(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("新增ModelType筛选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19858(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("下拉框展示全量数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19859(self, drivers):
        pass


    @allure.story("【APPWeb】销量上报添加消费者性别，年龄段、供应商字段")  # 用户故事名称
    @allure.title("支持模糊搜索")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19860(self, drivers):
        pass


@allure.feature("迭代二组V4_12")  # 迭代名称
class Teststory_3121:
    @allure.story("门店管理更新经纬度接口优化为取大数据聚合的经纬度结果值")  # 用户故事名称
    @allure.title("ShopLongitude取大数据集合经纬度数据，大数据有更新时，需要同步更新到DCR")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19861(self, drivers):
        pass


    @allure.story("门店管理更新经纬度接口优化为取大数据聚合的经纬度结果值")  # 用户故事名称
    @allure.title("ShopLatitude取大数据集合经纬度数据，大数据有更新时，需要同步更新到DCR")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19862(self, drivers):
        pass


    @allure.story("门店管理更新经纬度接口优化为取大数据聚合的经纬度结果值")  # 用户故事名称
    @allure.title("ShopLongitude取大数据集合经纬度数据，大数据有更新时，需要同步更新到DCR")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23485(self, drivers):
        pass


    @allure.story("门店管理更新经纬度接口优化为取大数据聚合的经纬度结果值")  # 用户故事名称
    @allure.title("ShopLatitude取大数据集合经纬度数据，大数据有更新时，需要同步更新到DCR")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23486(self, drivers):
        pass


@allure.feature("迭代二组V4_12")  # 迭代名称
class Teststory_2959:
    @allure.story("客户激活PSI库存逻辑更改")  # 用户故事名称
    @allure.title("库存改为取库存指标未激活的库存")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19863(self, drivers):
        pass


    @allure.story("客户激活PSI库存逻辑更改")  # 用户故事名称
    @allure.title("psi库存数据与CustomerInventoryQuery报表InactiveInventory字段数据一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19864(self, drivers):
        pass


    @allure.story("客户激活PSI库存逻辑更改")  # 用户故事名称
    @allure.title("DOS按最新的库存逻辑计算库存/7天平均销量")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19865(self, drivers):
        pass


    @allure.story("客户激活PSI库存逻辑更改")  # 用户故事名称
    @allure.title("库存改为取库存指标未激活的库存")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21734(self, drivers):
        pass


    @allure.story("客户激活PSI库存逻辑更改")  # 用户故事名称
    @allure.title("psi库存数据与CustomerInventoryQuery报表InactiveInventory字段数据一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21735(self, drivers):
        pass


    @allure.story("客户激活PSI库存逻辑更改")  # 用户故事名称
    @allure.title("DOS按最新的库存逻辑计算库存/7天平均销量")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21736(self, drivers):
        pass


@allure.feature("迭代二组V4_12")  # 迭代名称
class Teststory_3146:
    @allure.story("APP全局缓存")  # 用户故事名称
    @allure.title("冒烟用户进入到考勤应用，基础数据加载正常，不报错")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19866(self, drivers):
        pass


    @allure.story("APP全局缓存")  # 用户故事名称
    @allure.title("1、APP考勤门店接口从离线获取缓存，pakistan_channel/api/rest/v1/baseAppAuth/getAppAuthForAttendanceManagement")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19867(self, drivers):
        pass


    @allure.story("APP全局缓存")  # 用户故事名称
    @allure.title("2、APP考勤门店列表显示；仅保留ShopName、ShopID、Brand，同时考勤里的门店搜索界面去掉地址信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19868(self, drivers):
        pass


    @allure.story("APP全局缓存")  # 用户故事名称
    @allure.title("3、APP考勤门店列表数据显示正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19869(self, drivers):
        pass


    @allure.story("APP全局缓存")  # 用户故事名称
    @allure.title("31、APP考勤已授权的门店，被禁用后，门店列表实时更新门店状态，不显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19870(self, drivers):
        pass


    @allure.story("APP全局缓存")  # 用户故事名称
    @allure.title("app考勤门店列表页，查询门店功能正常，查询结果正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20712(self, drivers):
        pass


@allure.feature("迭代二组V4_12")  # 迭代名称
class Teststory_3148:
    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("purchaseorder模块进入首页显示客户")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19871(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("当前登录人的客户只有一个时跳过客户首页自动选择唯一客户进入采购页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19872(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("页面默认最多显示10个上游客户不能下拉自动加载")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19873(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("显示最上方一条客户信息为最近采购的客户")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19874(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("在页面底部显示提示Displayuptotencustomers,pleasesearch；（最多显示十个客户，请搜索）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19875(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("客户首页筛选项支持客户编码名称精确搜索及模糊搜索")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19876(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("客户首页筛选项权限代理员工根据当前登录人授权客户所属的上游客户")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19877(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("客户首页筛选项权限传音员工根据当前登录人授权客户所属的上游客户")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19878(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("页面客户的信息包括客户名称、品牌、客户编码、客户地址（国家省城市地址）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19879(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("选择客户后进入下一页商品选择页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19880(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("采购页面页面UI最上方显示选择的客户名称")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19881(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("采购页面页面显示的产品为客户库存中有过记录的产品")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19882(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("采购页面显示的产品为客户库存中有过记录的产品")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19883(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("采购页面包含有库存和无库存的")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19884(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("采购页面客户上游无库存无采购记录的产品不显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19885(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("采购页面已禁用的产品不显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19886(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("当选择产品，加入购物车时，如果没有库存，则弹框确认提示英文Outofstocknowwhileyoucansubmitthedemandandwewillrestocksoon")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19887(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("当选择产品，加入购物车时，如果没有库存，则弹框确认提示中文现在缺货，但您可以提交需求，我们将很快补充库存")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19888(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("弹框点击确认，则加入购物车")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19889(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("弹框点击取消，则不加入购物车")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19890(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("采购页面Model筛选框，model显示为市场名（机型）内存")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19891(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("商品详情页面添加商品时购物车对应添加")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19892(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("原功能测试回归")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19893(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("我要采购原功能回归")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21543(self, drivers):
        pass


    @allure.story("我要采购模块优化")  # 用户故事名称
    @allure.title("客户首页在页面底部显示提示Displayuptotencustomers,pleasesearch")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_21544(self, drivers):
        pass


@allure.feature("迭代二组V4_12")  # 迭代名称
class Teststory_3167:
    @allure.story("隐私协议APP弹窗")  # 用户故事名称
    @allure.title("冒烟设置好一个最新版本的隐私协议，用户第一次登录，弹出隐私弹框，点同意后，隐私协议系统中的隐私日志会有一条记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19969(self, drivers):
        pass


    @allure.story("隐私协议APP弹窗")  # 用户故事名称
    @allure.title("1、业务系统登录页勾选状态首次使用APP、用户退出登录，隐私协议默认不勾选")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19970(self, drivers):
        pass


    @allure.story("隐私协议APP弹窗")  # 用户故事名称
    @allure.title("2、登录成功后根据业务系统，用户账号未授权最新版本的隐私协议，弹出隐私协议弹窗")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19971(self, drivers):
        pass


    @allure.story("隐私协议APP弹窗")  # 用户故事名称
    @allure.title("21、点击，同意并开启服务关闭APP隐私协议弹窗，进入业务系统首页。隐私系统生成用户授权当前版本号信息记录，显示在隐私日志页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19972(self, drivers):
        pass


    @allure.story("隐私协议APP弹窗")  # 用户故事名称
    @allure.title("22、不同意退出登录并返回业务系统登录页")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19973(self, drivers):
        pass


    @allure.story("隐私协议APP弹窗")  # 用户故事名称
    @allure.title("3、登录成功后根据业务系统，，用户账号已授权最新的隐私协议，APP不会再次弹")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19974(self, drivers):
        pass


    @allure.story("隐私协议APP弹窗")  # 用户故事名称
    @allure.title("31、web端登录同意过之后，APP不会再次弹，反之APP同意之后，web端不会再弹框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19975(self, drivers):
        pass


    @allure.story("隐私协议APP弹窗")  # 用户故事名称
    @allure.title("4、根据系统语言显示隐私协议语言，若系统语言不在隐私协议语言之中，隐私协议语言顺序英、中、法")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19976(self, drivers):
        pass


    @allure.story("隐私协议APP弹窗")  # 用户故事名称
    @allure.title("41、目前隐私系统只有三种语言，中英法，若只有中文的隐私协议，全部随意切换语言均显示中文隐私协议")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19977(self, drivers):
        pass


    @allure.story("隐私协议APP弹窗")  # 用户故事名称
    @allure.title("42、若有中英两种语言，则中文系统显示中文的隐私协议，其他语言均显示英文的")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19978(self, drivers):
        pass


    @allure.story("隐私协议APP弹窗")  # 用户故事名称
    @allure.title("43、若有中法两种语言，则法文系统显示法文的隐私协议，其他语言均显示中文的")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19979(self, drivers):
        pass


    @allure.story("隐私协议APP弹窗")  # 用户故事名称
    @allure.title("5、APP隐私协议弹窗需求一致，内容显示正常，UI风格与系统保存一直")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19980(self, drivers):
        pass


    @allure.story("隐私协议APP弹窗")  # 用户故事名称
    @allure.title("51，隐私弹框中，红色部分业务系统对应隐私协议表单的隐私协议系统名")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19981(self, drivers):
        pass


    @allure.story("隐私协议APP弹窗")  # 用户故事名称
    @allure.title("蓝色部分52、蓝色部分根据业务系统，显示对应语言版本的隐私协议，点击后，打开对应语言版本的APP隐私协议预览页")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19982(self, drivers):
        pass


@allure.feature("迭代二组V4_12")  # 迭代名称
class Teststory_3158:
    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("冒烟用例WEB新增一个自定义模版可以成功")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19983(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("冒烟用例WEB端新增自定义模版在APP端可正常显示巡店")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19984(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("冒烟用例WEB端新增自定义模版已有国家和品牌时新增失败且给出对应的提示信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19985(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("冒烟用例WEB端新增自定义模版支持复制编辑拖动")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19986(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("冒烟用例APP端使用的新增自定义模版巡店成功后对应的页面有数据生成记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19987(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("数据权限品牌加门店")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19988(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("自定义模版的UI与需求显示一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19989(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("自定义模版View时与新建的模版一致且不可操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19990(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("模板类型切换巡店/门店自检放置在筛选条件作为下拉单选")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19991(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("选择对应的巡店模版时显示对应的模版界面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19992(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("切换shopselfinspection时页面与原功能一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19993(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("BaslcInformation同原功能保持一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19994(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("默认显示Visittask页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19995(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("新旧模板之间来回切换时保留切换前的编辑内容，切换回来依旧可以继续编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19996(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("点击Submit时只保留当前页面编辑的巡店模版")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19997(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("点击Reset清空当前编辑页面的模版数据恢复初始化页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19998(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("控件页面显示基本类型与DCR数据类型两种题型")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19999(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Fillin【填空】可任意输入问题及问题描述")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20000(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Fillin【填空】是否必填为单选")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20001(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Fillin【填空】是否必填打开时该填空题为必填项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20002(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Fillin【填空】是否必填关闭时该填空题为非必填项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20003(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Fillin【填空】是否保留记录打开时APP巡店时自动保留该题目数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20004(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Fillin【填空】是否保留记录关闭时APP巡店时不会保留该题目数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20005(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型MultipieChoice【多选】为多项选择题")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20006(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型MultipieChoice【多选】多项选择只保留一个选项时系统提示quot至少需要2个选项quot")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20007(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型MultipieChoice【多选】删除选项只剩余一个提交时系统提示至少需要2个选项quot")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20008(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型MultipieChoice【多选】当选项只有一个提交时系统给出对应的提示信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20009(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型MultipieChoice【多选】多选题目选项支持20个以内否则提示quot最多支持20选项quot")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20010(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型MultipieChoice【多选】是否必填打开时该填空题为必填项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20011(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型MultipieChoice【多选】是否必填关闭时该填空题为非必填项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20012(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型MultipieChoice【多选】是否保留记录打开时APP巡店时自动保留该题目数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20013(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型MultipieChoice【多选】是否保留记录关闭时APP巡店时不会保留该题目数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20014(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型MultipieChoice【多选】打开是否需要备注时页面显示备注框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20015(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型MultipieChoice【多选】关闭是否需要备注时页面无显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20016(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型MultipieChoice【多选】多选页面交互APP端为框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20017(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型SingelChoice【单选】不支持多选")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20018(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型SingelChoice【单选】是否需要备注校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20019(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型SingelChoice【单选】是否保留记录操作校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20020(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型SingelChoice【单选】是否必填操作校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20021(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型SingelChoice【单选】APP页面单选为圈")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20022(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Picture【图片题】只支持4张")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20023(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Picture【图片题】是否必填校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20024(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Picture【图片题】是否保留记录校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20025(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Quantity只支持数字输入")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20026(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Quantity是否必填校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20027(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Quantity是否保留记录校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20028(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Location【定位】获取当前用户的位置信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20029(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Location【定位】是否必填校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20030(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Location【定位】当弱网环境无网时返回默认值0")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20031(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Date日期选择")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20032(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Date时间选择为前后一年")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20033(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Grade【评分】是否必填校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20034(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Grade【评分】是否保留记录校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20035(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Judge【判断题】单选按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20036(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Judge【判断题】是否必填校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20037(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型Judge【判断题】是否保留记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20038(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型ScanCode是否允许手动输入打开时页面文本输入框支持手动输入及扫码")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20039(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型ScanCode扫码内容与扫描内容一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20040(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型ScanCode是否保留记录校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20041(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类型ScanCode是否必填校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20042(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型ShopPerformance【门店达成】")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20043(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型PSICollect机型下拉选择")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20044(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型PSICollect支持模糊搜索及精确搜索")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20045(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型PSICollect支持多选")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20046(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型PSICollect是否必填校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20047(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型PSICollect是否保留记录校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20048(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型SalesRegion下拉树选择")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20049(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型SalesRegion权限过滤当前登录用户的授权销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20050(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型SalesRegion是否必填")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20051(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型SalesRegion是否保留记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20052(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型Country/State/City显示DCR系统中国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20053(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型Country/State/City权限过滤当前登录用户授权的国家")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20054(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型Country/State/City是否必填校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20055(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型Country/State/City是否保留记录校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20056(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型ShopOpen【门店状态】用户选择关闭时后续题目不在显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20057(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型ShopOpen顺序永远在ShopPerformance下保持第二个排序")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20058(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型ShopOpen【门店状态】默认第二位且只能有一个唯一能删除操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20059(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型MarketName【市场名】是否必填校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20060(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型MarketName【市场名】是否保留记录校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20061(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型AssociatedUser/Customer/Shop为多选题")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20062(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型AssociatedUser/Customer/Shop当选择对象时自动过滤当前登录的用户权限过滤")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20063(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型AssociatedUser/Customer/Shop是否必填校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20064(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("DCR数据类型AssociatedUser/Customer/Shop是否保留记录校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20065(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("控件属性页面属性编辑中控件类型下拉单选")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20066(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("控件属性页面属性编辑中控件类型可任意切换")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20067(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("控件属性页面属性编辑中标题为文本输入框可任意填写")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20068(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("控件属性页面属性编辑中问题描述为文本输入框可任意填写")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20069(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("控件属性页面设置放在选项内容下")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20070(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("控件属性页面设置中是否必填操作选择")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20071(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("控件属性页面设置中是否保留记录操作选择")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20072(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("控件模块的页面校验所有题目置灰显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20073(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("控件模块的页面校验点击控件类的题目后属性编辑页面随着点击的题目切换")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20074(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("控件模块的页面校验可重复点击该题目")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20075(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("控件模块的页面校验只允许存在一个ShopOpen，用户点击弹框提示ShopOpencanonlyhaveone")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20076(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("属性编辑页面的校验点击控件页面的题目后控件属性显示当前题目")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20077(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("属性编辑页面的校验点击控件页面的题目控件属性显示当前题目后可再次下拉框选择其他类型题目")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20078(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("属性编辑页面的校验增加题目时UI界面显示对应操作信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20079(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("属性编辑页面的校验可重复添加同一问题的题目")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20080(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("属性编辑页面的校验编辑页面的必填项显示对应的标识")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20081(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("属性编辑页面的校验点击类型切换时属性编辑页不用校验必填项是否必填")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20082(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("属性编辑页面的校验当属性编辑页面的题目存在必填项未填写时页面标红给出对应的提示信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20083(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("属性编辑页面的校验所有文本输入框均限制255，到达255输入则在输入框下方红色小字提示Theinputistoolong")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20084(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("属性编辑页面的校验多选/单选题目的选项后点击X时可删除该题目内的选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20085(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("属性编辑页面的校验多选的题目的选项只保留一个点击切换控件类型时页面校验提示当前题目为多选不可只保留一个选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20086(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("属性编辑页面的校验是否必填为选择按钮默认显示否")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20087(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("属性编辑页面的校验当选择为是时，题目在UI界面有对应的必填项的标识")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20088(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("属性编辑页面的校验当选择为否时，题目在UI界面无任何标识")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20089(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("UI页面页面文本输入框，可填写本次巡店目标非必填,默认为空，填写的内容置灰显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20090(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("UI页面UI界面同步显示当前编辑的问题内容背景颜色为淡蓝色")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20091(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("UI页面题目的数据变动随着属性编辑页面的操作变动")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20092(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("UI页面点击题目后可回显到属性编辑页面进行编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20093(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("UI页面自定义巡店模板中进入后默认显示ShopPerformance")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20094(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("UI页面自定义巡店模板中进入后默认显示ShopPerformance不可删除不可移动")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20095(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("UI页面shopOpen不可移动，位置始终保持在默认的ShopPerformance下可删除")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20096(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("空模版时点击Submit时系统给出对应的提示信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20097(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("当属性编辑页面有题目正在编辑时点击Submit时系统给出对应的提示信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20098(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("当所有数据信息有对应的数据时点击submit时提交成功")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20099(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("UI页面题目后点击删除时可选择YES/NO")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20100(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("UI页面题目后点击删除时选择YES删除成功")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20101(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("UI页面题目后点击删除时选择NO删除失败")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20102(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("UI页面题目后点击删除时点击空白处数据保留")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20103(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("点击cancel关闭当前页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20104(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("用户可以在UI界面按住问题前面的标识即可拖动调换顺序")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20105(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("基本类的题目与DCR数据类题目不能相互移动")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20106(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("只能在同一类题目中组内题目移动")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20107(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("只能在同一类题目中组内顺序题目移动")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20108(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("自定义模版支持复制及编辑操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20109(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("APP端巡店模版的展示UI与WEB端保存最新的模版一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20110(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("APP优化当前的巡店填写页面置顶按钮下移")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20111(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("APP端原功能回归")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20112(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("APP端题目的类型操作与WEB端一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20113(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("APP端当必填项未填点击提交时则对应的题目标红提示quotXXisrequirequot")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20114(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("APP端当非必填未填写时点击提交可以提交成功")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20115(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("APP端当提交成功一条巡店记录后WEB端记录页面新增一条记录，图片页面新增一条图片信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20116(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("APP端巡店Shopopen关闭时记录页面保持一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20118(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("模版的拖拉移动ShopPerformance默认有且一号位不可移动，不可删除")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22108(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("ShopOpen默认有且二号位不可移动，可删除，删除后再次添加自动移动至二号位")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22109(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("PSICollect不可以与其他题目组成一组，只能单独一组")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22110(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("控件库新增控件/切换控件时控件配置的输入框标红，且右侧弹窗提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22111(self, drivers):
        pass


    @allure.story("自定义模板")  # 用户故事名称
    @allure.title("自定义模版UI界面底部有Add按钮，用户点击后可以新增空白组")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22112(self, drivers):
        pass


@allure.feature("迭代二组V4_12")  # 迭代名称
class Teststory_3147:
    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("点击上传按钮批量上传成功后提示quot成功上传//AllVisitingRecordsUploadSuccessfullyquot")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20122(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("无上传任务时点击提示quot你的巡店任务已经全部上传//Allyourshopvisitshavebeenuploadedquot")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20123(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("人员显示逻辑优化进入页面默认显示Mine及相关数据当前默认是All")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20124(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("巡店卡片优化增加巡店人员信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20125(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("地址前增加门店地址图标")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20126(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("非本人Mine的巡店记录去掉Visit/Close按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20127(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("数据后页面增加END标识")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20128(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("数据显示计划所属的人员当前绑定的门店数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20129(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("将原本下一页的NewPlan按钮与StartVisit按钮放在首页点击可进入不同页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20130(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("点击Newplan进入新建计划页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20131(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("没有模板的门店在ShopName后增加文本标识标识NoTemplate且没有选择框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20132(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("没有模版用户点击门店时，弹窗提示quotNotemplate,Pleasecontactyoursupervisor")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20133(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("支持多选多选标识为圈，用户选择门店后，点击submit即可提交")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20134(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("选择门店点击StartVisit可直接开始巡店")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20135(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("没有模板的门店在ShopName后增加标识")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20136(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("没有模版用户点击门店时，弹窗提示quotNotemplate,Pleasecontactyoursupervisor")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20137(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("没有模板的门店在ShopName后增加标识")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20138(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("StartVisit为单选")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20139(self, drivers):
        pass


    @allure.story("APP巡店优化")  # 用户故事名称
    @allure.title("巡店计划原功能回归")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20140(self, drivers):
        pass


@allure.feature("迭代二组V4_12")  # 迭代名称
class Teststory_3152:
    @allure.story("APP报错提示优化")  # 用户故事名称
    @allure.title("1、在用户点击首次应用按钮后，加载时进行校验涉及菜单所有")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22566(self, drivers):
        pass


    @allure.story("APP报错提示优化")  # 用户故事名称
    @allure.title("2、用户网络错误判断用户是否打开网络，如果没有，弹窗提示如下，用户点击OK退出微应用")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22567(self, drivers):
        pass


    @allure.story("APP报错提示优化")  # 用户故事名称
    @allure.title("21、弹框提示Pleasecheckyournetworkandtryagain，支持多语言")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22568(self, drivers):
        pass


    @allure.story("APP报错提示优化")  # 用户故事名称
    @allure.title("3、链接网络错误判断用户设备是否正常连接到服务器，如果没有，弹窗提示如下，")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22569(self, drivers):
        pass


    @allure.story("APP报错提示优化")  # 用户故事名称
    @allure.title("31.、用户点击NetworkDetection跳转到DCR的网络诊断页面")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22570(self, drivers):
        pass


    @allure.story("APP报错提示优化")  # 用户故事名称
    @allure.title("32、用户点击OK退出微应用")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22571(self, drivers):
        pass


    @allure.story("APP报错提示优化")  # 用户故事名称
    @allure.title("33/弹框内容Thenetworkabnormal,pleasecheckthenetworkstatus")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_22572(self, drivers):
        pass


@allure.feature("迭代二组V4_12")  # 迭代名称
class Teststory_3149:
    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("FTPSetting中新增退货配置字段Retumdate、IMEI、Dir、RetumFiag字段")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23399(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("退货字段中只要填写任意一个字段其他字段都为必填字段")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23400(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("退货字段任意一个字段未填写时提交系统提示Thereturnfieldisnotcompleted")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23401(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("退货的文件取数逻辑与出库单的一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23402(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("RetumFiag字段的标识为1时自动识别文件中的退货IMEI")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23403(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("退货成功的excel文件在ReturnOrder生成一条单据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23404(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("退货的模版与需求一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23405(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("当RetumFiag字段有退货的标识且Dir目录不一致时配置失败")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23406(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("FTP配置校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23407(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("FTPFileQuery增加ImportType字段")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23408(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("ImportType字段数据显示ReturnImport和DeliveryImport")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23409(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("退货的FTP配置成功时ImportType字段数据显示ReturnImpor")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23410(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("出库单的FTP配置成功时ImportType字段数据显示DeliveryImport")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23411(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("FTPFileQuery页面增加ReUpload按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23412(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("选择失败单个文件点击ReUpload按钮时可以重新上传且对应的状态转变为执行中")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23413(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("ReUpload按钮可针对多个失败的文件批量上传处理")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23414(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("失败的文件再次点击选择失败单个文件点击ReUpload按钮时可在次重新操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23415(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("上传成功的Total数量对应的增多Failed的数量减少")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23416(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("退货只支持Excel文件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23417(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("文件中当必填项为空时导入失败提示错误的数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23418(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("当IMEI必填项为空时导入失败提示错误的数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23419(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("当IMEI非法数据时导入失败提示错误的数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23420(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("当ReturnDate必填项为空时导入失败提示错误的数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23421(self, drivers):
        pass


    @allure.story("FTP识别增加退货数据")  # 用户故事名称
    @allure.title("ReturnDate的时间格式为yyyymmdd")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23422(self, drivers):
        pass


if __name__ == '__main__':
      pass
