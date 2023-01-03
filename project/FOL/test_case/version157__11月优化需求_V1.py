import allure
import pytest
@allure.feature("11月优化需求_V1")  # 迭代名称
class Teststory_2533:
    @allure.story("费用计提冲销增加冲销人/凭证制单人查询报表增加单据跳转链接")  # 用户故事名称
    @allure.title("【费用计提冲销】列表新增凭证制单人、冲销人")  # 用例名称
    @allure.description("查看费用计提冲销列表是否新增凭证制单人和冲销人字段")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16403(self, drivers):
        pass


    @allure.story("费用计提冲销增加冲销人/凭证制单人查询报表增加单据跳转链接")  # 用户故事名称
    @allure.title("【费用计提冲销】查询新增凭证制单人、冲销人")  # 用例名称
    @allure.description("查看费用计提冲销查询是否新增凭证制单人和冲销人字段")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16404(self, drivers):
        pass


    @allure.story("费用计提冲销增加冲销人/凭证制单人查询报表增加单据跳转链接")  # 用户故事名称
    @allure.title("【费用计提冲销】查询凭证制单人，弹框选择")  # 用例名称
    @allure.description("验证凭证制单人是否弹框选择")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16405(self, drivers):
        pass


    @allure.story("费用计提冲销增加冲销人/凭证制单人查询报表增加单据跳转链接")  # 用户故事名称
    @allure.title("【费用计提冲销】查询凭证制单人，模糊查询选择后精确搜索，支持工号、姓名")  # 用例名称
    @allure.description("验证凭证制单人是否可模糊查询==验证凭证制单人是否可支持工号、姓名")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16406(self, drivers):
        pass


    @allure.story("费用计提冲销增加冲销人/凭证制单人查询报表增加单据跳转链接")  # 用户故事名称
    @allure.title("【费用计提冲销】查询冲销人，弹框选择")  # 用例名称
    @allure.description("验证冲销人是否弹框选择")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16407(self, drivers):
        pass


    @allure.story("费用计提冲销增加冲销人/凭证制单人查询报表增加单据跳转链接")  # 用户故事名称
    @allure.title("【费用计提冲销】查询冲销人，模糊查询，支持工号、姓名")  # 用例名称
    @allure.description("验证冲销人是否可模糊查询==验证冲销人是否可支持工号、姓名")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16408(self, drivers):
        pass


    @allure.story("费用计提冲销增加冲销人/凭证制单人查询报表增加单据跳转链接")  # 用户故事名称
    @allure.title("【费用计提报表】单据编号，点击后跳转至费用计提单据详情页面")  # 用例名称
    @allure.description("验证点击单据编号，是否跳转至费用计提单据详情页面")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16409(self, drivers):
        pass


    @allure.story("费用计提冲销增加冲销人/凭证制单人查询报表增加单据跳转链接")  # 用户故事名称
    @allure.title("【费用计提报表】可查看审批流程情况和共享审批情况")  # 用例名称
    @allure.description("点击单据编号==跳转至费用计提单据详情页面==验证是否能查看审批流程情况和共享审批情况")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16410(self, drivers):
        pass


    @allure.story("费用计提冲销增加冲销人/凭证制单人查询报表增加单据跳转链接")  # 用户故事名称
    @allure.title("【费用计提冲销】英文界面，凭证制单人、冲销人翻译正确")  # 用例名称
    @allure.description("进入英文系统==查看凭证制单人是否翻译为VoucherCreator==查看冲销人是否翻译为ReversalPerson")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16411(self, drivers):
        pass


@allure.feature("11月优化需求_V1")  # 迭代名称
class Teststory_2425:
    @allure.story("返利执行单除迪拜保税区返利外，其他的返利类型'利润中心'、'返利类型'字段，由前端政策自动带出且不允许除了共享财务外的其他节点修改（特别注意迪拜保税区保持现状，可以修改）")  # 用户故事名称
    @allure.title("【返利执行单】选择返利政策单号后，默认带出'返利类型'和'利润中心'")  # 用例名称
    @allure.description("新增一笔返利执行单==选中一笔返利政策单==验证'返利类型'和'利润中心'是否默认带出")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16412(self, drivers):
        pass


    @allure.story("返利执行单除迪拜保税区返利外，其他的返利类型'利润中心'、'返利类型'字段，由前端政策自动带出且不允许除了共享财务外的其他节点修改（特别注意迪拜保税区保持现状，可以修改）")  # 用户故事名称
    @allure.title("【返利执行单】选择返利政策单号后，'返利类型'和'利润中心'为只读状态")  # 用例名称
    @allure.description("新增一笔返利执行单==选中一笔返利政策单==验证'返利类型'和'利润中心'是否为只读状态")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16413(self, drivers):
        pass


    @allure.story("返利执行单除迪拜保税区返利外，其他的返利类型'利润中心'、'返利类型'字段，由前端政策自动带出且不允许除了共享财务外的其他节点修改（特别注意迪拜保税区保持现状，可以修改）")  # 用户故事名称
    @allure.title("【返利执行单】清空返利政策单号，则'返利类型'和'利润中心'可编辑")  # 用例名称
    @allure.description("新增一笔返利执行单==选中一笔返利政策单，再清空这笔返利政策单==验证'返利类型'和'利润中心'是否可编辑")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16414(self, drivers):
        pass


    @allure.story("返利执行单除迪拜保税区返利外，其他的返利类型'利润中心'、'返利类型'字段，由前端政策自动带出且不允许除了共享财务外的其他节点修改（特别注意迪拜保税区保持现状，可以修改）")  # 用户故事名称
    @allure.title("【返利执行单】共享财务节点，可修改'返利类型'和'利润中心'")  # 用例名称
    @allure.description("验证共享财务节点是否可修改'返利类型'和'利润中心'")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16415(self, drivers):
        pass


    @allure.story("返利执行单除迪拜保税区返利外，其他的返利类型'利润中心'、'返利类型'字段，由前端政策自动带出且不允许除了共享财务外的其他节点修改（特别注意迪拜保税区保持现状，可以修改）")  # 用户故事名称
    @allure.title("【返利执行单】迪拜保税区，可编辑'返利类型'和'利润中心'")  # 用例名称
    @allure.description("新增一笔返利执行单==选中一笔返利政策单==查看'返利类型'和'利润中心'是否可编辑==新增一笔返利执行单==查看'返利类型'和'利润中心'是否可编辑")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16416(self, drivers):
        pass


    @allure.story("返利执行单除迪拜保税区返利外，其他的返利类型'利润中心'、'返利类型'字段，由前端政策自动带出且不允许除了共享财务外的其他节点修改（特别注意迪拜保税区保持现状，可以修改）")  # 用户故事名称
    @allure.title("【返利执行单】返利类型为其他返利，返利类型备注就为必填")  # 用例名称
    @allure.description("验证返利类型为其他返利，返利类型备注是否为必填")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_16417(self, drivers):
        pass


if __name__ == '__main__':
    pass
