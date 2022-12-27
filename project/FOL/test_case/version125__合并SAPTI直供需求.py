import allure
import pytest
@allure.feature("合并SAPTI直供需求")  # 迭代名称
class Teststory_1431:
    @allure.story("【TI直供系统】修改功能点网银付款结果回传SAP逻辑")  # 用户故事名称
    @allure.title("【TI直供系统】网银付款结果回传SAP执行成功")  # 用例名称
    @allure.description("新增一笔供应商材料类付款申请，选择票到付款的付款类型==审批通过生成共享付款申请单==付款单完成付款后，单据运行时列表里面看下流程控制网银付款结果回传SAP是否有执行成功==如果执行成功selectfromlog_sap_pj_return_interfacewherebillidlike039bcb1b989efdc4f419308da59c6d4543e039andLogCode=039sapPayReturn039中的data看下新增的这几个字段有没有在里面传过去SAP，{quotIT_PAYquot[{quotZZISTGRquotquotB14quot,quotPAYAMOUNTquotquot60229.00quot,quotZZKJGHquotquot18647020quot,quotPAYNOquotquot200000000000062128quot,quotSTATUSquotquotPAYEDquot,quotZPAYIDquotquot165940624382848883quot,quotFSSCBILLNOquotquotGN282208020249quot,quotPAYDATEquotquot20220804quot,quotBATCHquotquot100000000000008531quot,quotZPAYTYPEquotquotTTquot,quotZPJHquotquot,quotZPAYHKONTquotquot0010020146quot}]}")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10012(self, drivers):
        pass


@allure.feature("合并SAPTI直供需求")  # 迭代名称
class Teststory_1434:
    @allure.story("【凭证接口】行分录增加字段事务类型其他货币")  # 用户故事名称
    @allure.title("【凭证接口】新增'事务类型其他货币TransactionType2")  # 用例名称
    @allure.description("查看是否新增'事务类型其他货币")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10013(self, drivers):
        pass


    @allure.story("【凭证接口】行分录增加字段事务类型其他货币")  # 用户故事名称
    @allure.title("【凭证接口】预制凭证逻辑正确，且过账成功")  # 用例名称
    @allure.description("点击生成凭证补给单，借方这里，事务类型其他货币字段选择Z开头的一个==审批过账==验证能否正常过账")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10014(self, drivers):
        pass


    @allure.story("【凭证接口】行分录增加字段事务类型其他货币")  # 用户故事名称
    @allure.title("【凭证接口】匹配正确事务类型编码（Transactioncode）传给SAP")  # 用例名称
    @allure.description("进入表eb_TransactionBase==根据TransactionID查询Transactioncode==查看是否传正确的Transactioncode给SAP")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10015(self, drivers):
        pass


    @allure.story("【凭证接口】行分录增加字段事务类型其他货币")  # 用户故事名称
    @allure.title("【凭证接口】新增'业务地点'（BUPLA）")  # 用例名称
    @allure.description("查看是否新增'业务地点'")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10016(self, drivers):
        pass


    @allure.story("【凭证接口】行分录增加字段事务类型其他货币")  # 用户故事名称
    @allure.title("【凭证接口】预制凭证逻辑正确，且过账成功")  # 用例名称
    @allure.description("点击生成凭证补给单==审批过账==验证能否正常过账")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10017(self, drivers):
        pass


    @allure.story("【凭证接口】行分录增加字段事务类型其他货币")  # 用户故事名称
    @allure.title("【凭证接口】匹配正确业务地点编码（sapbuplacode）传给SAP")  # 用例名称
    @allure.description("进入表eb_sapbuplaBase==根据sapbuplaID查询Transactioncode==查看是否传正确的sapbuplacode给SAP")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10018(self, drivers):
        pass


    @allure.story("【凭证接口】行分录增加字段事务类型其他货币")  # 用户故事名称
    @allure.title("【凭证接口】新增'集团货币金额'")  # 用例名称
    @allure.description("查看是否新增'集团货币金额'")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10019(self, drivers):
        pass


    @allure.story("【凭证接口】行分录增加字段事务类型其他货币")  # 用户故事名称
    @allure.title("【凭证接口】预制凭证逻辑正确")  # 用例名称
    @allure.description("点击生成凭证==进入凭证中间表==进入凭证模板主表==验证此凭证中间表'集团货币金额'（Groupmoney）的取值是否正确")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10020(self, drivers):
        pass


    @allure.story("【凭证接口】行分录增加字段事务类型其他货币")  # 用户故事名称
    @allure.title("【凭证接口】取正确的集团货币金额字段传给值给SAP")  # 用例名称
    @allure.description("查看是否取正确的集团货币金额字段传给值给SAP")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10021(self, drivers):
        pass


@allure.feature("合并SAPTI直供需求")  # 迭代名称
class Teststory_1680:
    @allure.story("【收款及扣款确认】收款和扣款零星认领逻辑修改")  # 用户故事名称
    @allure.title("【收款确认类型】将'收款确认类型'界面的字段写入'收款确认单（待认领）'单据里")  # 用例名称
    @allure.description("字段有值时，查看是否把收款确认类型里的业务小类（名称）、业务大类（名称）、凭证类型、客户名称、供应商、交易类型、抬头文本、行文本、贷方会计科目、内部订单号、借方原因代码写入收款确认单（待认领）单据里==字段无值时，不做更新")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10022(self, drivers):
        pass


    @allure.story("【收款及扣款确认】收款和扣款零星认领逻辑修改")  # 用户故事名称
    @allure.title("【收款确认类型】将'收款确认类型'界面的字段写入'收款确认单（待认领）'数据表里")  # 用例名称
    @allure.description("字段有值时，查看是否把收款确认类型里的业务小类（名称）、业务大类（名称）、凭证类型、客户名称、供应商、交易类型、抬头文本、行文本、贷方会计科目、内部订单号、借方原因代码写入收款确认单（待认领）数据表里==字段无值时，不做更新")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10023(self, drivers):
        pass


    @allure.story("【收款及扣款确认】收款和扣款零星认领逻辑修改")  # 用户故事名称
    @allure.title("【确认被动扣款类型】将确认被动扣款类型界面的字段写入到银行被动扣款待认领单据里")  # 用例名称
    @allure.description("字段有值时，查看是否将借方供应商、交易类型、凭证类型、借方会计科目、内部订单号、借方原因代码、是否需要补票、补票人、补票单借方科目写入到银行被动扣款待认领单据里==字段无值时，不做更新")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10024(self, drivers):
        pass


    @allure.story("【收款及扣款确认】收款和扣款零星认领逻辑修改")  # 用户故事名称
    @allure.title("【收款确认类型】将确认被动扣款类型界面的字段写入到银行被动扣款待认领数据表里")  # 用例名称
    @allure.description("字段有值时，查看是否将借方供应商、交易类型、凭证类型、借方会计科目、内部订单号、借方原因代码、是否需要补票、补票人、补票单借方科目写入到银行被动扣款待认领数据表里==字段无值时，不做更新")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10025(self, drivers):
        pass


if __name__ == '__main__':
    pass
