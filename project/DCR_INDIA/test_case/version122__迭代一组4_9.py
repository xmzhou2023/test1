import allure
import pytest
@allure.feature("迭代一组4_9")  # 迭代名称
class Teststory_1702:
    @allure.story("/api/rest/v1/dealer/association/findBuyerByNameOrCodeAndDSR接口优化")  # 用户故事名称
    @allure.title("创建销售单/出库单功能回归，buyer查询接口响应时间测试")  # 用例名称
    @allure.description("创建销售单，未选择seller时选择buyer==创建出库单，未选择seller选择buyer")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8616(self, drivers):
        pass


@allure.feature("迭代一组4_9")  # 迭代名称
class Teststory_1698:
    @allure.story("客户信息更新同步仓库、门店")  # 用户故事名称
    @allure.title("客户更新销售区域（全球和印度），唯一仓库，关联仓库同步更新销售区域，刷新用户授权的销售区域的客户和仓库权限")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8623(self, drivers):
        pass


    @allure.story("客户信息更新同步仓库、门店")  # 用户故事名称
    @allure.title("客户更新销售区域（全球和印度）客户有多个仓库时，仓库不同步更新销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8624(self, drivers):
        pass


    @allure.story("客户信息更新同步仓库、门店")  # 用户故事名称
    @allure.title("客户更新销售区域（全球和印度）批导更新客户销售区域，同步更新唯一仓库的销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8625(self, drivers):
        pass


    @allure.story("客户信息更新同步仓库、门店")  # 用户故事名称
    @allure.title("更新客户关联唯一仓库的销售区域，不会同步更新客户的销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8626(self, drivers):
        pass


    @allure.story("客户信息更新同步仓库、门店")  # 用户故事名称
    @allure.title("零售商类客户编辑信息（全球和印度）唯一仓库，关联仓库同步更新销售区域")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8627(self, drivers):
        pass


    @allure.story("客户信息更新同步仓库、门店")  # 用户故事名称
    @allure.title("零售商类客户编辑信息（全球和印度）,有且只有一个PublicID关联唯一零售商的门店，同步更新门店的ContactName、ContactNo、CustomerName、CustomerAddress、Country/City、SalesRegion同步更新")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8628(self, drivers):
        pass


    @allure.story("客户信息更新同步仓库、门店")  # 用户故事名称
    @allure.title("零售商类客户编辑信息（全球和印度），批导更新客户的如上字段信息，同步更新门店的各字段信息，刷新用户授权销售区域的客户和门店权限")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8629(self, drivers):
        pass


    @allure.story("客户信息更新同步仓库、门店")  # 用户故事名称
    @allure.title("更新门店信息，同步更新关联零售商的ContactName、ContactNo、CustomerName、CustomerAddress、Country/City字段信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8630(self, drivers):
        pass


    @allure.story("客户信息更新同步仓库、门店")  # 用户故事名称
    @allure.title("更新门店信息，批导编辑更新门店的如上字段信息，不同步更新零售商的信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8631(self, drivers):
        pass


    @allure.story("客户信息更新同步仓库、门店")  # 用户故事名称
    @allure.title("更新门店信息，编辑更新门店的销售区域不更新零售商的销售区域，检查用户授权销售区域的门店授权")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8632(self, drivers):
        pass


    @allure.story("客户信息更新同步仓库、门店")  # 用户故事名称
    @allure.title("客户管理，隐藏删除按钮，全球和印度版都隐藏")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8633(self, drivers):
        pass


    @allure.story("客户信息更新同步仓库、门店")  # 用户故事名称
    @allure.title("零售商类客户编辑信息（全球和印度）,零售商关联多个publicID的门店，更新如上字段后不同步更新门店字段信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9291(self, drivers):
        pass


    @allure.story("客户信息更新同步仓库、门店")  # 用户故事名称
    @allure.title("零售商类客户编辑信息（全球和印度）,零售商关联一个PublicID的多门店，门店有关联其他零售商时，更新如上字段后不同步更新门店字段信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9292(self, drivers):
        pass


@allure.feature("迭代一组4_9")  # 迭代名称
class Teststory_1701:
    @allure.story("客户管理页面优化")  # 用户故事名称
    @allure.title("进入零售商客户的编辑页，有关联门店，编辑页顶部显示提示该零售商不允许更改客户类型，如需更改联系管理员（目前只有中英）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8634(self, drivers):
        pass


    @allure.story("客户管理页面优化")  # 用户故事名称
    @allure.title("进入零售商客户的编辑页，客户类型置灰为不可编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8635(self, drivers):
        pass


    @allure.story("客户管理页面优化")  # 用户故事名称
    @allure.title("批导编辑零售商客户类型，有关联门店，该条记录导入失败提示TheCustomertypeofthisretailerisnotallowedtochange")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8636(self, drivers):
        pass


    @allure.story("客户管理页面优化")  # 用户故事名称
    @allure.title("页面/批导编辑无关联门店的零售商客户类型，没有不可编辑提示，可以更改客户类型")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8637(self, drivers):
        pass


    @allure.story("客户管理页面优化")  # 用户故事名称
    @allure.title("验证全球和印度版编辑有关联门店的零售商场景提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8638(self, drivers):
        pass


    @allure.story("客户管理页面优化")  # 用户故事名称
    @allure.title("客户编辑页，ChannelSalesManager字段数据显示，查看编辑页字段显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8639(self, drivers):
        pass


    @allure.story("客户管理页面优化")  # 用户故事名称
    @allure.title("客户编辑页，ChannelSalesManager字段数据显示，编辑/清空提交保存查看字段是否显示正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8640(self, drivers):
        pass


    @allure.story("客户管理页面优化")  # 用户故事名称
    @allure.title("客户编辑页，ChannelSalesManager字段数据显示，验证全球和印度")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8641(self, drivers):
        pass


    @allure.story("客户管理页面优化")  # 用户故事名称
    @allure.title("客户View页面Edit按钮去掉，验证全球和印度都去掉")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8642(self, drivers):
        pass


    @allure.story("客户管理页面优化")  # 用户故事名称
    @allure.title("机型管理编辑页面，修改remark提示文案，为Maximunto500characters（只有英文）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8643(self, drivers):
        pass


    @allure.story("客户管理页面优化")  # 用户故事名称
    @allure.title("门店销量列表字段更新，BookingActivityid改为BookingActivityID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8644(self, drivers):
        pass


    @allure.story("客户管理页面优化")  # 用户故事名称
    @allure.title("门店销量列表字段更新，导出同步更新字段显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8645(self, drivers):
        pass


@allure.feature("迭代一组4_9")  # 迭代名称
class Teststory_1703:
    @allure.story("出库单/二级三级收货新增月度字段")  # 用户故事名称
    @allure.title("DeliveryOrder新增DeliveryMonth字段，格式年月")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8646(self, drivers):
        pass


    @allure.story("出库单/二级三级收货新增月度字段")  # 用户故事名称
    @allure.title("DeliveryOrder新增DeliveryMonth字段，位置BuyerRegion3之后")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8647(self, drivers):
        pass


    @allure.story("出库单/二级三级收货新增月度字段")  # 用户故事名称
    @allure.title("DeliveryOrder新增DeliveryMonth字段，取值DeliveryDate中的年月")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8648(self, drivers):
        pass


    @allure.story("出库单/二级三级收货新增月度字段")  # 用户故事名称
    @allure.title("DeliveryOrder新增DeliveryMonth字段，导出同步增加该字段显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8649(self, drivers):
        pass


    @allure.story("出库单/二级三级收货新增月度字段")  # 用户故事名称
    @allure.title("DeliveryOrder新增DeliveryMonth字段，多语言验证")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8650(self, drivers):
        pass


    @allure.story("出库单/二级三级收货新增月度字段")  # 用户故事名称
    @allure.title("InboundReceipt新增DeliveryMonth字段，格式年月")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8651(self, drivers):
        pass


    @allure.story("出库单/二级三级收货新增月度字段")  # 用户故事名称
    @allure.title("InboundReceipt新增DeliveryMonth字段，位置BuyerRegion3之后")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8652(self, drivers):
        pass


    @allure.story("出库单/二级三级收货新增月度字段")  # 用户故事名称
    @allure.title("InboundReceipt新增DeliveryMonth字段，取值DeliveryDate中的年月")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8653(self, drivers):
        pass


    @allure.story("出库单/二级三级收货新增月度字段")  # 用户故事名称
    @allure.title("InboundReceipt新增DeliveryMonth字段，导出同步增加该字段显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8654(self, drivers):
        pass


    @allure.story("出库单/二级三级收货新增月度字段")  # 用户故事名称
    @allure.title("InboundReceipt新增DeliveryMonth字段，多语言验证")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8655(self, drivers):
        pass


@allure.feature("迭代一组4_9")  # 迭代名称
class Teststory_1705:
    @allure.story("渠道销售统计/退货流水报表增加字段")  # 用户故事名称
    @allure.title("CustomerSalesReport列表新增字段，新增BuyerCountry（多语言检查）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8667(self, drivers):
        pass


    @allure.story("渠道销售统计/退货流水报表增加字段")  # 用户故事名称
    @allure.title("CustomerSalesReport列表新增字段，位置BuyerRegion5之后")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8668(self, drivers):
        pass


    @allure.story("渠道销售统计/退货流水报表增加字段")  # 用户故事名称
    @allure.title("CustomerSalesReport列表新增字段，导出同步新增字段")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8669(self, drivers):
        pass


    @allure.story("渠道销售统计/退货流水报表增加字段")  # 用户故事名称
    @allure.title("CustomerSalesReport添加筛选项，BuyerCountry下拉可多选")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8670(self, drivers):
        pass


    @allure.story("渠道销售统计/退货流水报表增加字段")  # 用户故事名称
    @allure.title("CustomerSalesReport添加筛选项，验证筛选数据和导出结果")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8671(self, drivers):
        pass


    @allure.story("渠道销售统计/退货流水报表增加字段")  # 用户故事名称
    @allure.title("IMEIReturnQuery增加字段，增加退货单中的创建人、创建时间、审核人、审核时间字段")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8672(self, drivers):
        pass


    @allure.story("渠道销售统计/退货流水报表增加字段")  # 用户故事名称
    @allure.title("IMEIReturnQuery增加字段，位置在CreateDate字段之后")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8673(self, drivers):
        pass


    @allure.story("渠道销售统计/退货流水报表增加字段")  # 用户故事名称
    @allure.title("IMEIReturnQuery增加字段，取值ReturnOrder列表的数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8674(self, drivers):
        pass


    @allure.story("渠道销售统计/退货流水报表增加字段")  # 用户故事名称
    @allure.title("IMEIReturnQuery增加字段，检查加字段后查询接口响应时间，目前3万多数据147ms")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8675(self, drivers):
        pass


    @allure.story("渠道销售统计/退货流水报表增加字段")  # 用户故事名称
    @allure.title("IMEIReturnQuery增加字段，导出数据同步增加新增的字段")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8676(self, drivers):
        pass


@allure.feature("迭代一组4_9")  # 迭代名称
class Teststory_1709:
    @allure.story("尼日代理员工自动授权客户")  # 用户故事名称
    @allure.title("新增功能配置项，名称Autoauthorizestheagent039scustomer")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8677(self, drivers):
        pass


    @allure.story("尼日代理员工自动授权客户")  # 用户故事名称
    @allure.title("新增功能配置项，配置卖方客户国家品牌生效")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8678(self, drivers):
        pass


    @allure.story("尼日代理员工自动授权客户")  # 用户故事名称
    @allure.title("新增功能配置项，默认不配置角色")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8679(self, drivers):
        pass


    @allure.story("尼日代理员工自动授权客户")  # 用户故事名称
    @allure.title("新增功能配置项，Value2配置角色名称，英文逗号隔开可配置多个（可测5个）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8680(self, drivers):
        pass


    @allure.story("尼日代理员工自动授权客户")  # 用户故事名称
    @allure.title("新增配置角色，自动授权该角色的用户seller的所有下游客户（品牌、状态过滤），用户授权seller，自动授权下游客户")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8681(self, drivers):
        pass


    @allure.story("尼日代理员工自动授权客户")  # 用户故事名称
    @allure.title("新增配置角色，自动授权该角色的用户seller的所有下游客户（品牌、状态过滤）seller新增buyer，该用户自动授权buyer")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8682(self, drivers):
        pass


    @allure.story("尼日代理员工自动授权客户")  # 用户故事名称
    @allure.title("未配置seller的国家品牌，该角色用户（非主账号）授权seller不会自动授权下游客户")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8683(self, drivers):
        pass


    @allure.story("尼日代理员工自动授权客户")  # 用户故事名称
    @allure.title("未配置seller的国家品牌，该角色如果是主账号，也会自动授权下游客户")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8684(self, drivers):
        pass


    @allure.story("尼日代理员工自动授权客户")  # 用户故事名称
    @allure.title("该角色用户已授权的seller，解除客户的某个buyer上下级关系，该用户自动解除buyer、仓库和关联门店授权")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8685(self, drivers):
        pass


    @allure.story("尼日代理员工自动授权客户")  # 用户故事名称
    @allure.title("该角色用户（非主账号）解除buyer授权，不影响客户上下级关系")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8686(self, drivers):
        pass


    @allure.story("尼日代理员工自动授权客户")  # 用户故事名称
    @allure.title("配置主账号的角色自动授权卖方的下游客户，用户授权解除客户权限会自动解绑客户上下级关系")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8687(self, drivers):
        pass


    @allure.story("尼日代理员工自动授权客户")  # 用户故事名称
    @allure.title("验证代理员工和传音员工各角色的自动授权逻辑，传音员工会自动授权客户仓库和零售商关联品牌一致的门店")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8688(self, drivers):
        pass


    @allure.story("尼日代理员工自动授权客户")  # 用户故事名称
    @allure.title("验证代理员工和传音员工各角色的自动授权逻辑，代理员工根据功能配置是否授权零售商关联的门店")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8689(self, drivers):
        pass


    @allure.story("尼日代理员工自动授权客户")  # 用户故事名称
    @allure.title("未配置的该功能项的角色用户（非主账号），授权seller不会自动授权下游客户")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8690(self, drivers):
        pass


@allure.feature("迭代一组4_9")  # 迭代名称
class Teststory_1707:
    @allure.story("退货单增加卖方国家字段")  # 用户故事名称
    @allure.title("测试路径SalesManagementReturnOrder")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9629(self, drivers):
        pass


    @allure.story("退货单增加卖方国家字段")  # 用户故事名称
    @allure.title("测试点_1、表单添加SellerCountry（卖方国家）字段，取值为CustomerManagement中Seller的国家字段，添加位置在字段SellerName之后")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9630(self, drivers):
        pass


    @allure.story("退货单增加卖方国家字段")  # 用户故事名称
    @allure.title("测试点_11、导出文件也一并增加")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9631(self, drivers):
        pass


    @allure.story("退货单增加卖方国家字段")  # 用户故事名称
    @allure.title("测试点_2、增加筛选项SellerCountry（卖方国家），下拉多选，默认为空（框中提示All）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9632(self, drivers):
        pass


    @allure.story("退货单增加卖方国家字段")  # 用户故事名称
    @allure.title("测试点_21、筛选SellerCountry，筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9633(self, drivers):
        pass


    @allure.story("退货单增加卖方国家字段")  # 用户故事名称
    @allure.title("测试点_22、筛选SellerCountry，筛选后导出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9634(self, drivers):
        pass


@allure.feature("迭代一组4_9")  # 迭代名称
class Teststory_1706:
    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_测试路径BasicDataManagementExportRecord")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9678(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_测试点_1、新增DCR、MKT选择项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9679(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_测试点_2、无论该页面进入路径为点击消息列表的More按钮进入的，还是从BasicDataManagementExportRecord菜单点击进入的。进入的页面都是默认选中DCR")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9680(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_测试点_3、选中DCR，查询未实现中台化模块的当前用户下载记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9681(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_测试点_31、选中DCR时，列表取数逻辑不变")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9682(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_测试点_4、选中MKT，查询已实现中台化模块的当前用户下载记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9683(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_测试点_41、选中MKT时，列表为本次新设计的页面，按照需求设计来")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9684(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_DCR列表回归_1、查询及重置功能回归正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9685(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_DCR列表回归_2、列表展示及翻页功能回归正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9686(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_DCR列表回归_3、操作栏点击【Download】下载导出文件回归正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9687(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_DCR列表回归_4、点击【Delete】删除导出记录回归正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9688(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_筛选项_1、TaskName（任务名称）下拉选择框，下拉单选")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9693(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_筛选项_11、选项内容所有已实现中台化的业务模块（例如用户反馈、多语言组件）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9694(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_筛选项_12、选择MKT，根据选中的任务名称，进行查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9695(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_筛选项_2、DownStatus（下载状态）下拉选择项，选项内容与现有内容一致（Pending/Exporting/Complete/Failed/unknow_task）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9696(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_筛选项_21、选择MKT，根据选中的下载状态，进行查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9697(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_筛选项_3、CreateDate（创建时间）日期选择器，查询所有创建时间包含在选择时间范围内的记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9698(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_筛选项_31、选择MKT，根据选中的创建时间，进行查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9699(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_Search按钮_1、点击Search按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9700(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_Search按钮_2、单个筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9701(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_Search按钮_3、组合筛选出的数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9702(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_Reset按钮、点击Reset按钮，重置筛选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9703(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_Delete按钮、点击Delete按钮，删除选中的导出记录（支持批量删除）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9704(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表_1、列表最左边为批量选择框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9705(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表_2、列表列宽自适应用户也可以自己手动拉，和excel表格一样操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9706(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表排序规则按导出时间倒序排列")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9707(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_1、DownloadStatus（下载状态）导出文件下载状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9708(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_11、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9709(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_2、Reason（原因）文件导出失败原因")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9710(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_21、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9711(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_3、Remark（备注）文件导出失败备注说明")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9712(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_31、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9713(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_4、TaskName（任务名称）导出任务类型")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9714(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_41、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9715(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_5、FileName（文件名）导入文件名称")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9716(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_51、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9717(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_6、FileSize（文件大小）导出文件大小")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9718(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_61、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9719(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_7、UserID（用户ID）下载用户的ID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9720(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_71、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9721(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_8、UserName（用户名）下载用户名称")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9722(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_81、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9723(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_9、CreateDate（创建时间）下载任务创建时间")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9724(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_91、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9725(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_10、CompleteDate（完成时间）下载任务完成时间")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9726(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_101、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9727(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_11、WaitTimes（等待耗时（秒））下载任务在等待处理过程中时间")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9728(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_111、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9729(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_12、ExportTimes（下载耗时（秒））下载任务处理时间")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9730(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_121、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9731(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_13、Operation（操作栏）操作栏展示【Download】按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9732(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_列表字段_131、点击【Download】按钮，下载对应的导出文件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9733(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_翻页1、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9734(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_翻页2、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9735(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_翻页3、页面右下角Total统计正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9736(self, drivers):
        pass


    @allure.story("ExportRecord兼容中台")  # 用户故事名称
    @allure.title("ExportRecord_MKT列表_翻页4、页面右下角每页显示记录可设置（15，50，100），如果选择15，则每页显示1至15条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9737(self, drivers):
        pass


@allure.feature("迭代一组4_9")  # 迭代名称
class Teststory_1714:
    @allure.story("用户反馈支持导出")  # 用户故事名称
    @allure.title("测试路径FeedBackFeedBack")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9738(self, drivers):
        pass


    @allure.story("用户反馈支持导出")  # 用户故事名称
    @allure.title("Export按钮、点击Export按钮，导出当前筛选出的全部数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9739(self, drivers):
        pass


    @allure.story("用户反馈支持导出")  # 用户故事名称
    @allure.title("Export导出_1、导出文件名为菜单名流水号")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9740(self, drivers):
        pass


    @allure.story("用户反馈支持导出")  # 用户故事名称
    @allure.title("Export导出_2、导出的报表字段名、字段顺序、数据内容和列表一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9741(self, drivers):
        pass


    @allure.story("用户反馈支持导出")  # 用户故事名称
    @allure.title("Export导出_3、导出的报表表头需要12号字紫色，不做自适应。导出的报表字段宽度为16个字符宽度")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9742(self, drivers):
        pass


    @allure.story("用户反馈支持导出")  # 用户故事名称
    @allure.title("Export导出_4、筛选后导出的报表数据和筛选的数据保持一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9743(self, drivers):
        pass


    @allure.story("用户反馈支持导出")  # 用户故事名称
    @allure.title("Export导出_41、单个筛选，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9744(self, drivers):
        pass


    @allure.story("用户反馈支持导出")  # 用户故事名称
    @allure.title("Export导出_411、筛选Module，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9745(self, drivers):
        pass


    @allure.story("用户反馈支持导出")  # 用户故事名称
    @allure.title("Export导出_412、筛选Country，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9746(self, drivers):
        pass


    @allure.story("用户反馈支持导出")  # 用户故事名称
    @allure.title("Export导出_413、筛选FeedbackTime，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9747(self, drivers):
        pass


    @allure.story("用户反馈支持导出")  # 用户故事名称
    @allure.title("Export导出_42、组合筛选，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9748(self, drivers):
        pass


@allure.feature("迭代一组4_9")  # 迭代名称
class Teststory_1699:
    @allure.story("移动端图片水印组件化")  # 用户故事名称
    @allure.title("1、巡店拍照生成水印信息正确地理位置、拍照时间（本地时间）、员工（员工名称工号）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10029(self, drivers):
        pass


    @allure.story("移动端图片水印组件化")  # 用户故事名称
    @allure.title("2、巡店VisitingDetalis页面点击图片查看大图")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10030(self, drivers):
        pass


    @allure.story("移动端图片水印组件化")  # 用户故事名称
    @allure.title("3、图片新增保存按钮，点击保存按钮，可将图片保存至本地，保存成功后toast提示'Savedtoalbum'")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10031(self, drivers):
        pass


    @allure.story("移动端图片水印组件化")  # 用户故事名称
    @allure.title("31、Savedtoalbum要做多语言，与需求提个一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10032(self, drivers):
        pass


@allure.feature("迭代一组4_9")  # 迭代名称
class Teststory_1704:
    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_测试路径BasicDataManagementImportRecord")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10052(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_测试点_1、新增DCR、MKT选择项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10053(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_测试点_2、无论该页面是从业务模块导入后自动跳转进入的，还是从BasicDataManagementImportRecord菜单点击进入的。进入的页面都是默认选中DCR")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10054(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_测试点_3、选中DCR，查询未实现中台化模块的当前用户上传记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10055(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_测试点_31、选中DCR时，列表取数逻辑不变")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10056(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_测试点_4、选中MKT，查询已实现中台化模块的当前用户上传记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10057(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_测试点_41、选中MKT时，列表为本次新设计的页面，按照需求设计来")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10058(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_DCR列表回归_1、查询及重置功能回归正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10059(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_DCR列表回归_2、列表展示及翻页功能回归正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10060(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_DCR列表回归_3、FailData栏点击【DownloadFailed】下载报错文件回归正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10061(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_筛选项_1、ImportDate（导入日期）日期选择器，查询所有导入时间包含在选择时间范围内的记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10062(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_筛选项_11、选择MKT，根据选中的导入时间，进行查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10063(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_Search按钮_1、点击Search按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10064(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_Reset按钮、点击Reset按钮，重置筛选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10065(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表_1、列表最左边为批量选择框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10066(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表_2、列表列宽自适应用户也可以自己手动拉，和excel表格一样操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10067(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表排序规则按导入时间倒序排列")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10068(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_1、FileName（文件名）导入文件名称")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10069(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_11、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10070(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_2、Status（状态）导入文件状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10071(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_21、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10072(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_3、Total（总计）导入数据的总行数计（除表头与说明内容所占行数）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10073(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_31、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10074(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_4、Success（成功）导入数据成功行数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10075(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_41、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10076(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_5、Failed（失败的）导入数据失败行数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10077(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_51、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10078(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_6、FailData（失败数据）系统生成导入失败记录。如果导入成功，这边展示为空。如果导入失败，这边展示【DownloadFailed】按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10079(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_61、点击【DownloadFailed】按钮，下载对应的报错文件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10080(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_7、ImportDate（导入日期）文件导入的日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10081(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_71、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10082(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_8、UserID（用户ID）上传用户的ID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10083(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_列表字段_81、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10084(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_翻页1、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10085(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_翻页2、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10086(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_翻页3、页面右下角Total统计正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10087(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("ImportRecord_MKT列表_翻页4、页面右下角每页显示记录可设置（15，50，100），如果选择15，则每页显示1至15条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10088(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_测试路径BasicDataManagementBatchImport")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10089(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_测试点_1、新增DCR、MKT选择项切换DCR/MKT时TaskType这个条件要重置，其他不用")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10090(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_测试点_2、无论该页面是从业务模块导入后自动跳转进入的，还是从BasicDataManagementBatchImport菜单点击进入的。进入的页面都是默认选中DCR")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10091(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_测试点_3、选中DCR，根据查询条件查询未实现中台化模块的上传记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10092(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_测试点_31、选中DCR时，列表取数逻辑不变")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10093(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_测试点_4、选中MKT，根据查询条件查询已实现中台化模块的上传记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10094(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_测试点_41、选中MKT时，列表为本次新设计的页面，按照需求设计来")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10095(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_DCR列表回归_1、查询及重置功能回归正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10096(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_DCR列表回归_2、列表展示及翻页功能回归正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10097(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_DCR列表回归_3、FailData栏点击【DownloadFailed】下载报错文件回归正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10098(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_DCR列表回归_4、操作栏点击【View】弹出弹窗'ResultOfUpload'展示的内容回归正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10099(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_筛选项_1、TaskType（任务类型）下拉选择框，下拉单选")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10100(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_筛选项_11、选项内容所有已实现中台化的业务模块（例如用户反馈、多语言组件）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10101(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_筛选项_12、选择MKT，根据选中的任务类型，进行查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10102(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_筛选项_2、ImportDate（导入日期）日期选择器，查询所有导入时间包含在选择时间范围内的记录")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10103(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_筛选项_21、选择MKT，根据选中的导入时间，进行查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10104(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_筛选项_3、UserID（用户ID）文本输入框，根据输入内容与所选的服务端，进行模糊查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10105(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_筛选项_31、选择MKT，根据选中的用户ID，进行查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10106(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_Search按钮_1、点击Search按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10107(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_Reset按钮、点击Reset按钮，重置筛选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10108(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表_1、列表最左边为批量选择框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10109(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表_2、列表列宽自适应用户也可以自己手动拉，和excel表格一样操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10110(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表排序规则按导入时间倒序排列")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10111(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_1、TaskType（任务类型）导入文件的任务类型")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10112(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_11、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10113(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_2、FileName（文件名）导入文件名称")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10114(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_21、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10115(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_3、UploadPath（上传地址）导入文件的存放路径")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10116(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_31、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10117(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_4、Status（状态）导入文件状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10118(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_41、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10119(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_5、Total（总计）导入数据的总行数计（除表头与说明内容所占行数）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10120(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_51、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10121(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_6、Success（成功）导入数据成功行数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10122(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_61、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10123(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_7、Failed（失败的）导入数据失败行数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10124(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_71、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10125(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_8、FailData（失败数据）系统生成导入失败记录。如果导入成功，这边展示为空。如果导入失败，这边展示【DownloadFailed】按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10126(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_81、点击【DownloadFailed】按钮，下载对应的报错文件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10127(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_9、ImportDate（导入日期）文件导入的日期")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10128(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_91、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10129(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_10、UserID（用户ID）上传用户的ID")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10130(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_101、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10131(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_11、Remark（备注）导入文件校验错误备注")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10132(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_111、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10133(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_列表字段_12、Operation（操作栏）操作栏隐藏【View】按钮，展示为空")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10134(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_翻页1、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10135(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_翻页2、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10136(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_翻页3、页面右下角Total统计正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10137(self, drivers):
        pass


    @allure.story("ImportRecord/BatchImport兼容中台")  # 用户故事名称
    @allure.title("BatchImport_MKT列表_翻页4、页面右下角每页显示记录可设置（15，50，100），如果选择15，则每页显示1至15条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10138(self, drivers):
        pass


@allure.feature("迭代一组4_9")  # 迭代名称
class Teststory_1854:
    @allure.story("客户编码自动生成规则优化")  # 用户故事名称
    @allure.title("1、已存在的客户编码有对应的提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10149(self, drivers):
        pass


    @allure.story("客户编码自动生成规则优化")  # 用户故事名称
    @allure.title("2、编码手动生成任意的时候、再去新增自动生成的编码为最底的编码")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10150(self, drivers):
        pass


    @allure.story("客户编码自动生成规则优化")  # 用户故事名称
    @allure.title("3、编码自动生成A手动添加B再次添加自动生成C")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10151(self, drivers):
        pass


    @allure.story("客户编码自动生成规则优化")  # 用户故事名称
    @allure.title("4、二代手动编码已生成A、手动编码在零售添加A、返回二代自动生成A1、反之返回二代添加零售A系统给出对应的提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10152(self, drivers):
        pass


@allure.feature("迭代一组4_9")  # 迭代名称
class Teststory_1700:
    @allure.story("/api/rest/v1/channel/warehouseStockInitial/checkImei接口优化")  # 用户故事名称
    @allure.title("库存初始化页面功能正常，不报错")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10191(self, drivers):
        pass


    @allure.story("/api/rest/v1/channel/warehouseStockInitial/checkImei接口优化")  # 用户故事名称
    @allure.title("/api/rest/v1/channel/warehouseStockInitial/checkImei接口优化后性能提升5060")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10192(self, drivers):
        pass


if __name__ == '__main__':
      pass
