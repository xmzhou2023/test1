import allure
import pytest
@allure.feature("售后需求")  # 迭代名称
class Teststory_320:
    @allure.story("【售后】自营网点OSC售后工单接口增加字段")  # 用户故事名称
    @allure.title("OSC售后工单接口增加外部发票号码physicalinvoice")  # 用例名称
    @allure.description("外部发票号码为空==外部号码为合法值")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_870(self, drivers):
        pass


@allure.feature("售后需求")  # 迭代名称
class Teststory_368:
    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("页面数据列表字段检查")  # 用例名称
    @allure.description("检查页面数据列表字段是否与需求一致==检查页面字段对应数据显示格式是否与需求一致")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1070(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("页面字段可以缩放自适应")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1071(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("查询条件为空查询所有数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1072(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("填单人查询")  # 用例名称
    @allure.description("填单人输入'45'==填单人输入'李'==选择单个填单人，点击查询==选择多个填单人，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1073(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("单据编号查询")  # 用例名称
    @allure.description("输入部分单据编号，点击查询==输入完整单据编号，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1074(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("收银单号查询")  # 用例名称
    @allure.description("输入部分收银单号，点击查询==输入完整收银单号，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1075(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("收/退款单号查询")  # 用例名称
    @allure.description("输入部分收/退款单号，点击查询==输入完整收/退款单号，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1076(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("国家查询")  # 用例名称
    @allure.description("输入国家名称'乌'==选择单个国家，点击查询==选择多个国家，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1077(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("网点编码查询")  # 用例名称
    @allure.description("输入部分网点编码，点击查询==输入完整网点编码，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1078(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("收款方式查询")  # 用例名称
    @allure.description("点击收款方式文本框==选择单个收款方式，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1079(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("单据日期查询")  # 用例名称
    @allure.description("选择单据日期期间为一天查询==选择单据日期期间超过一月查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1080(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("工单单号查询")  # 用例名称
    @allure.description("输入部分工单单号，点击查询==输入完整工单单号，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1081(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("存现单号查询")  # 用例名称
    @allure.description("输入部分存现单号，点击查询==输入完整存现单号，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1082(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("审批状态查询")  # 用例名称
    @allure.description("点击审批状态文本框==选择单个审批状态，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1083(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("逐步选择查询条件查询")  # 用例名称
    @allure.description("选择填单人和输入单据编号查询==填单人、单据编号、收银单号查询==填单人、单据编号、收银单号、收/退款单号查询==填单人、单据编号、收银单号、收/退款单号、国家查询==填单人、单据编号、收银单号、收/退款单号、国家、网点编码查询==填单人、单据编号、收银单号、收/退款单号、国家、网点编码、收款方式查询==填单人、单据编号、收银单号、收/退款单号、国家、网点编码、收款方式、单据日期查询==填单人、单据编号、收银单号、收/退款单号、国家、网点编码、收款方式、单据日期、工单单号查询==填单人、单据编号、收银单号、收/退款单号、国家、网点编码、收款方式、单据日期、工单单号、存现单号查询==填单人、单据编号、收银单号、收/退款单号、国家、网点编码、收款方式、单据日期、工单单号、存现单号、审批状态查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1084(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("没有公司数据权限，查询数据为空")  # 用例名称
    @allure.description("逐步选择查询条件查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1085(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("有对应公司权限，只能查询对应公司数据")  # 用例名称
    @allure.description("逐步选择查询条件查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1086(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("管理员权限，可以查询所有公司数据")  # 用例名称
    @allure.description("登录账号只有管理员权限==登录账号有管理员权限和对应公司权限==登录账号只有管理员权限==逐步选择查询条件查询==登录账号有管理员权限和对应公司权限==逐步选择查询条件查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1087(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("费用会计权限，可以查询所有公司数据")  # 用例名称
    @allure.description("登录账号只有费用会计权限==登录账号有费用会计权限和对应公司权限")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1088(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("填单人查询，导出查询出数据")  # 用例名称
    @allure.description("选择单个填单人查询，点击导出==选择多个填单人查询，点击导出")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1089(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("单据编号查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1090(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("收银单号查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1091(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("收/退款单号查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1092(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("国家查询，导出查询出数据")  # 用例名称
    @allure.description("选择单个国家查询，点击导出==选择多个国家查询，点击导出")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1093(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("网点编码查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1094(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("收款方式查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1095(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("单据日期查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1096(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("工单单号查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1097(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("存现单号查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1098(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("审批状态查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1099(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】售后收退款单报表")  # 用户故事名称
    @allure.title("查询条件为空查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1205(self, drivers):
        pass


@allure.feature("售后需求")  # 迭代名称
class Teststory_378:
    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("页面数据列表字段检查")  # 用例名称
    @allure.description("检查页面数据列表字段是否与需求一致==检查页面字段对应数据显示格式是否与需求一致")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1206(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("页面字段可以缩放自适应")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1207(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("查询条件为空查询所有数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1208(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("填单人查询")  # 用例名称
    @allure.description("填单人输入'45'==填单人输入'李'==选择单个填单人，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1209(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("单据编号查询")  # 用例名称
    @allure.description("输入部分单据编号，点击查询==输入完整单据编号，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1210(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("工单单号查询")  # 用例名称
    @allure.description("输入部分工单单号，点击查询==输入完整工单单号，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1211(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("国家查询")  # 用例名称
    @allure.description("输入国家名称'乌'==选择单个国家，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1212(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("网点查询")  # 用例名称
    @allure.description("输入部分网点，点击查询==输入完整网点，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1213(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("网点编码查询")  # 用例名称
    @allure.description("输入部分网点编码，点击查询==输入完整网点编码，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1214(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("业务类型查询")  # 用例名称
    @allure.description("点击业务类型文本框==选择单个业务类型，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1215(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("账套查询")  # 用例名称
    @allure.description("账套输入'63'==账套输入'深圳'==选择单个填单人，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1216(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("审批状态查询")  # 用例名称
    @allure.description("点击审批状态文本框==选择单个审批状态，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1217(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("逐步选择查询条件查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1218(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("没有公司数据权限，查询数据为空")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1219(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("有对应公司权限，只能查询对应公司数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1220(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("管理员权限，可以查询所有公司数据")  # 用例名称
    @allure.description("登录账号只有管理员权限==登录账号有管理员权限和对应公司权限")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1221(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("费用会计权限，可以查询所有公司数据")  # 用例名称
    @allure.description("登录账号只有费用会计权限==登录账号有费用会计权限和对应公司权限")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1222(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("填单人查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1223(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("单据编号查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1224(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("工单单号查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1225(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("国家查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1226(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("网点查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1227(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("网点编码查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1228(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("业务类型查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1229(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("账套查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1230(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("审批状态查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1231(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】OSC工单报表")  # 用户故事名称
    @allure.title("查询条件为空查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1232(self, drivers):
        pass


@allure.feature("售后需求")  # 迭代名称
class Teststory_379:
    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("页面数据列表字段检查")  # 用例名称
    @allure.description("检查页面数据列表字段是否与需求一致==检查页面字段对应数据显示格式是否与需求一致")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1233(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("页面字段可以缩放自适应")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1234(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("查询条件为空查询所有数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1235(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("单据编号查询")  # 用例名称
    @allure.description("输入部分单据编号，点击查询==输入完整单据编号，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1236(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("工单单号查询")  # 用例名称
    @allure.description("输入部分工单单号，点击查询==输入完整工单单号，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1237(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("账套查询")  # 用例名称
    @allure.description("账套输入'63'==账套输入'深圳'==选择单个填单人，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1238(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("国家查询")  # 用例名称
    @allure.description("输入国家名称'乌'==选择单个国家，点击查询==选择多个国家，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1239(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("网点查询")  # 用例名称
    @allure.description("输入部分网点，点击查询==输入完整网点，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1240(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("网点编码查询")  # 用例名称
    @allure.description("输入部分网点编码，点击查询==输入完整网点编码，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1241(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("业务类型查询")  # 用例名称
    @allure.description("点击业务类型文本框==选择单个业务类型，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1242(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("结算类型查询")  # 用例名称
    @allure.description("点击结算类型文本框==选择单个结算类型，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1243(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("审批状态查询")  # 用例名称
    @allure.description("点击审批状态文本框==选择单个审批状态，点击查询")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1244(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("逐步选择查询条件查询")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1245(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("没有公司数据权限，查询数据为空")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1246(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("有对应公司权限，只能查询对应公司数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1247(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("管理员权限，可以查询所有公司数据")  # 用例名称
    @allure.description("登录账号只有管理员权限==登录账号有管理员权限和对应公司权限")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1248(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("费用会计权限，可以查询所有公司数据")  # 用例名称
    @allure.description("登录账号只有费用会计权限==登录账号有费用会计权限和对应公司权限")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1249(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("单据编号查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1250(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("工单单号查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1251(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("国家查询，导出查询出数据")  # 用例名称
    @allure.description("选择单个国家查询，点击导出==选择多个国家查询，点击导出")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1252(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("网点查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1253(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("网点编码查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1254(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("业务类型查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1255(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("结算类型查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1256(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("账套查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1257(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("审批状态查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1258(self, drivers):
        pass


    @allure.story("【售后】售后报表/【售后】ASC工单报表")  # 用户故事名称
    @allure.title("查询条件为空查询，导出查询出数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1259(self, drivers):
        pass


if __name__ == '__main__':
    pass
