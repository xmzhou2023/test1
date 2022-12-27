import allure
import pytest
@allure.feature("信贷自动化FOL改造")  # 迭代名称
class Teststory_410:
    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【收款确认单】点击认领按钮时，将信贷明细表的字段从主表中默认拷贝到信贷明细中")  # 用例名称
    @allure.description("选中此笔收款确认单，点击收款认领==查看信贷明细表的字段是否从主表中默认拷贝到信贷明细中")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5696(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【公司信贷档案】增加'事业部'、'信贷范围默认值标识'维度")  # 用例名称
    @allure.description("查看公司信贷档案，是否增加以上几个维度")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17009(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【客户加款单】有默认唯一标识的信贷范围，默认选中")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目不为'客户转款'==必填项维护==查看是否默认选中唯一标识的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17010(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【客户减款单】有默认唯一标识的信贷范围，默认选中")  # 用例名称
    @allure.description("新增一笔客户减款单==必填项维护==查看是否默认选中唯一标识的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17032(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【客户减款单】匹配到唯一的信贷范围无论是否有默认标识都自动默认选中")  # 用例名称
    @allure.description("新增一笔客户减款单==必填项维护==查看是否默认选中唯一的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17033(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【客户减款单】匹配到多个信贷范围，可选中任意一条除默认唯一标识以外的信贷范围")  # 用例名称
    @allure.description("新增一笔客户减款单==必填项维护==查看是否可以选中任意一条除默认唯一标识以外的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17034(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【客户减款单】匹配到多个信贷范围没有默认标识，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔客户减款单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17035(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【客户减款单】匹配到默认标识的信贷范围，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔客户减款单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17036(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【客户减款单】有默认唯一标识的信贷范围，默认选中")  # 用例名称
    @allure.description("新增一笔客户减款单==必填项维护==查看是否默认选中唯一标识的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17037(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【客户减款单】匹配到唯一的信贷范围无论是否有默认标识都自动默认选中")  # 用例名称
    @allure.description("新增一笔客户减款单==必填项维护==查看是否默认选中唯一的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17038(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【客户减款单】匹配到多个信贷范围，可选中任意一条除默认唯一标识以外的信贷范围")  # 用例名称
    @allure.description("新增一笔客户减款单==必填项维护==查看是否可以选中任意一条除默认唯一标识以外的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17039(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【客户减款单】匹配到多个信贷范围没有默认标识，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔客户减款单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17040(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【客户减款单】匹配到默认标识的信贷范围，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔客户减款单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17041(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【退款申请单】有默认唯一标识的信贷范围，默认选中")  # 用例名称
    @allure.description("新增一笔退款申请单==必填项维护==查看是否默认选中唯一标识的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17042(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【退款申请单】匹配到唯一的信贷范围无论是否有默认标识都自动默认选中")  # 用例名称
    @allure.description("新增一笔退款申请单==必填项维护==查看是否默认选中唯一的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17043(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【退款申请单】匹配到多个信贷范围，可选中任意一条除默认唯一标识以外的信贷范围")  # 用例名称
    @allure.description("新增一笔退款申请单==必填项维护==查看是否可以选中任意一条除默认唯一标识以外的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17044(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【退款申请单】匹配到多个信贷范围没有默认标识，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔退款申请单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17045(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【退款申请单】匹配到默认标识的信贷范围，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔退款申请单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17046(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【退款申请单】有默认唯一标识的信贷范围，默认选中")  # 用例名称
    @allure.description("新增一笔退款申请单==必填项维护==查看是否默认选中唯一标识的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17047(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【退款申请单】匹配到唯一的信贷范围无论是否有默认标识都自动默认选中")  # 用例名称
    @allure.description("新增一笔退款申请单==必填项维护==查看是否默认选中唯一的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17048(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【退款申请单】匹配到多个信贷范围，可选中任意一条除默认唯一标识以外的信贷范围")  # 用例名称
    @allure.description("新增一笔退款申请单==必填项维护==查看是否可以选中任意一条除默认唯一标识以外的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17049(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【退款申请单】匹配到多个信贷范围没有默认标识，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔退款申请单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17050(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【退款申请单】匹配到默认标识的信贷范围，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔退款申请单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17051(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】有默认唯一标识的信贷范围，默认选中")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否默认选中唯一标识的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17052(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到唯一的信贷范围无论是否有默认标识都自动默认选中")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否默认选中唯一的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17053(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到多个信贷范围，可选中任意一条除默认唯一标识以外的信贷范围")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否可以选中任意一条除默认唯一标识以外的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17054(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到多个信贷范围没有默认标识，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17055(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到默认标识的信贷范围，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17056(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】有默认唯一标识的信贷范围，默认选中")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否默认选中唯一标识的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17057(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到唯一的信贷范围无论是否有默认标识都自动默认选中")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否默认选中唯一的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17058(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到多个信贷范围，可选中任意一条除默认唯一标识以外的信贷范围")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否可以选中任意一条除默认唯一标识以外的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17059(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到多个信贷范围没有默认标识，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17060(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到默认标识的信贷范围，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17061(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】有默认唯一标识的信贷范围，默认选中")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否默认选中唯一标识的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17062(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到唯一的信贷范围无论是否有默认标识都自动默认选中")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否默认选中唯一的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17063(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到多个信贷范围，可选中任意一条除默认唯一标识以外的信贷范围")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否可以选中任意一条除默认唯一标识以外的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17064(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到多个信贷范围没有默认标识，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17065(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到默认标识的信贷范围，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17066(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】有默认唯一标识的信贷范围，默认选中")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否默认选中唯一标识的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17067(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到唯一的信贷范围无论是否有默认标识都自动默认选中")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否默认选中唯一的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17068(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到多个信贷范围，可选中任意一条除默认唯一标识以外的信贷范围")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否可以选中任意一条除默认唯一标识以外的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17069(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到多个信贷范围没有默认标识，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17070(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】匹配到默认标识的信贷范围，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔返利执行单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17071(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【返利执行单】第三方代付，无信贷控制范围")  # 用例名称
    @allure.description("新增一条返利执行单==选择第三方代付，其他必填项维护==验证是否无信贷控制范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17072(self, drivers):
        pass


@allure.feature("信贷自动化FOL改造")  # 迭代名称
class Teststory_407:
    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到唯一的信贷范围无论是否有默认标识都自动默认选中")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目不为'客户转款'==必填项维护==查看是否默认选中唯一的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17011(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到多个信贷范围，可选中任意一条除默认唯一标识以外的信贷范围")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目不为'客户转款'==必填项维护==查看是否可以选中任意一条除默认唯一标识以外的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17012(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到多个信贷范围没有默认标识，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目不为'客户转款'==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17013(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到默认标识的信贷范围，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目不为'客户转款'==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17014(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】有默认唯一标识的信贷范围，默认选中")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目不为'客户转款'==必填项维护==查看是否默认选中唯一标识的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17015(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到唯一的信贷范围无论是否有默认标识都自动默认选中")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目不为'客户转款'==必填项维护==查看是否默认选中唯一的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17016(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到多个信贷范围，可选中任意一条除默认唯一标识以外的信贷范围")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目不为'客户转款'==必填项维护==查看是否可以选中任意一条除默认唯一标识以外的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17017(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到多个信贷范围没有默认标识，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目不为'客户转款'==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17018(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到默认标识的信贷范围，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目不为'客户转款'==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17019(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】新增转出事业部字段")  # 用例名称
    @allure.description("查看是否新增转出事业部字段==验证转出事业部字段是否为必填")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17020(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】副项目不为客户转款，不显示转出事业部字段")  # 用例名称
    @allure.description("验证副项目不为客户转款时，是否不显示转出事业部字段")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17021(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】有默认唯一标识的信贷范围，默认选中")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目为客户转款==必填项维护==查看是否默认选中唯一标识的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17022(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到唯一的信贷范围无论是否有默认标识都自动默认选中")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目为客户转款==必填项维护==查看是否默认选中唯一的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17023(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到多个信贷范围，可选中任意一条除默认唯一标识以外的信贷范围")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目为客户转款==必填项维护==查看是否可以选中任意一条除默认唯一标识以外的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17024(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到多个信贷范围没有默认标识，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目为客户转款==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17025(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到默认标识的信贷范围，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目为客户转款==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17026(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】有默认唯一标识的信贷范围，默认选中")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目为客户转款==必填项维护==查看是否默认选中唯一标识的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17027(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到唯一的信贷范围无论是否有默认标识都自动默认选中")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目为客户转款==必填项维护==查看是否默认选中唯一的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17028(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到多个信贷范围，可选中任意一条除默认唯一标识以外的信贷范围")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目为客户转款==必填项维护==查看是否可以选中任意一条除默认唯一标识以外的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17029(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到多个信贷范围没有默认标识，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目为客户转款==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17030(self, drivers):
        pass


    @allure.story("【信贷自动化】/【信贷自动化】FOL改造加款单针对转款场景，除了支持原有客户间转款，也需要支持同客户内部不同信贷范围进行转款操作")  # 用户故事名称
    @allure.title("【客户加款单】匹配到默认标识的信贷范围，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔客户加款单，副项目为客户转款==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17031(self, drivers):
        pass


@allure.feature("信贷自动化FOL改造")  # 迭代名称
class Teststory_411:
    @allure.story("【信贷自动化】/收款确认单针对一笔款项针对不同信贷范围进行认领")  # 用户故事名称
    @allure.title("【收款确认单】有默认唯一标识的信贷范围，默认选中")  # 用例名称
    @allure.description("新增一笔收款确认单==必填项维护==查看是否默认选中唯一标识的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17073(self, drivers):
        pass


    @allure.story("【信贷自动化】/收款确认单针对一笔款项针对不同信贷范围进行认领")  # 用户故事名称
    @allure.title("【收款确认单】匹配到唯一的信贷范围无论是否有默认标识都自动默认选中")  # 用例名称
    @allure.description("新增一笔收款确认单==必填项维护==查看是否默认选中唯一的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17074(self, drivers):
        pass


    @allure.story("【信贷自动化】/收款确认单针对一笔款项针对不同信贷范围进行认领")  # 用户故事名称
    @allure.title("【收款确认单】匹配到多个信贷范围，可选中任意一条除默认唯一标识以外的信贷范围")  # 用例名称
    @allure.description("新增一笔收款确认单==必填项维护==查看是否可以选中任意一条除默认唯一标识以外的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17075(self, drivers):
        pass


    @allure.story("【信贷自动化】/收款确认单针对一笔款项针对不同信贷范围进行认领")  # 用户故事名称
    @allure.title("【收款确认单】匹配到多个信贷范围没有默认标识，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔收款确认单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17076(self, drivers):
        pass


    @allure.story("【信贷自动化】/收款确认单针对一笔款项针对不同信贷范围进行认领")  # 用户故事名称
    @allure.title("【收款确认单】匹配到默认标识的信贷范围，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔收款确认单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17077(self, drivers):
        pass


    @allure.story("【信贷自动化】/收款确认单针对一笔款项针对不同信贷范围进行认领")  # 用户故事名称
    @allure.title("【收款确认单】有默认唯一标识的信贷范围，默认选中")  # 用例名称
    @allure.description("新增一笔收款确认单==必填项维护==查看是否默认选中唯一标识的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17078(self, drivers):
        pass


    @allure.story("【信贷自动化】/收款确认单针对一笔款项针对不同信贷范围进行认领")  # 用户故事名称
    @allure.title("【收款确认单】匹配到唯一的信贷范围无论是否有默认标识都自动默认选中")  # 用例名称
    @allure.description("新增一笔收款确认单==必填项维护==查看是否默认选中唯一的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17079(self, drivers):
        pass


    @allure.story("【信贷自动化】/收款确认单针对一笔款项针对不同信贷范围进行认领")  # 用户故事名称
    @allure.title("【收款确认单】匹配到多个信贷范围，可选中任意一条除默认唯一标识以外的信贷范围")  # 用例名称
    @allure.description("新增一笔收款确认单==必填项维护==查看是否可以选中任意一条除默认唯一标识以外的信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17080(self, drivers):
        pass


    @allure.story("【信贷自动化】/收款确认单针对一笔款项针对不同信贷范围进行认领")  # 用户故事名称
    @allure.title("【收款确认单】匹配到多个信贷范围没有默认标识，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔收款确认单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17081(self, drivers):
        pass


    @allure.story("【信贷自动化】/收款确认单针对一笔款项针对不同信贷范围进行认领")  # 用户故事名称
    @allure.title("【收款确认单】匹配到默认标识的信贷范围，可选中任意一条信贷范围")  # 用例名称
    @allure.description("新增一笔收款确认单==必填项维护==查看是否可选中任意一条信贷范围")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_17082(self, drivers):
        pass


if __name__ == '__main__':
    pass
