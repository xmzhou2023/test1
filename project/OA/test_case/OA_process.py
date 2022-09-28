import allure
import pytest
import base64
import pytest, logging

from project.OA.page_object.OA_login import OAdnluPage
from public.data.unified_login.unified import *
from public.base.assert_ui import *
from public.libs.unified_login.login import Login
from libs.common.read_config import *

pro_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from project.OA.page_object.OA_process import OAUserPage

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""


@allure.feature("OA应用系统巡检")  # 模块名称
class TestUtil:

    @allure.story("二级标题：OA应用系统巡检")  # 场景名称
    @allure.title("三级标题：OA自动巡检登录功能，提交系统巡检报告，调用飞书机器消息推送结果")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OA = OAUserPage(drivers)
        OA.refresh()  # 刷新当前界面
        sleep(30)
        itexis = OA.islogin()
        OA.open_url("https://wenjuan.feishu.cn/m/cfm?t=spxJpHryzfxi-qnnu")  # 打开应用系统巡检地址
        # 绕过【应用系统巡检】扫码登录
        OA.click_toggle()
        OA.click_read()
        OA.click_SSO()
        OA.input_company_name("transsioner")
        OA.click_Next()
        OA.click_IMWAV()
        OA.click_account_password()
        OA.input_account_password('0', '1')
        OA.click_Login()
        # 提交系统巡检报告
        OA.click_Inspection("深圳")
        OA.click_Inspection("OA")
        OA.input_personnel("机器人【刘艳】")
        OA.click_date()
        if itexis:
            OA.click_Inspection("系统登陆正常")
            # OA.Messagefeishu("OA自动巡检通知\n今天OA系统登陆正常！已提交系统巡检报告", "1")
            assert True
        else:
            OA.click_Inspection("系统登陆异常")
            OA.input_reason("OA机器人巡检，生产环境登录OA异常。登录OA地址[https://oa.transsion.com/wui/main.jsp]")
            OA.Messagefeishu("【重要信息】OA机器人自动巡检通知,发现系统登陆异常,请相关人员及时排查问题！已提交系统巡检报告！", "1")
            assert False
        OA.click_sumbmit()

    @allure.story("二级标题：深圳传音控股电子签署平台巡检")  # 场景名称
    @allure.title("三级标题：深圳传音控股电子签署平台登录功能， 调用飞书机器消息推送结果")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OA = OAUserPage(drivers)
        OA.open_url("https://seal.transsion.com:9180/contractlist?pageNo=1")  # 打开应用系统巡检地址
        OA.input_username(2)
        OA.input_password(3)
        OA.click_button()
        itexis = OA.issign_login()

        if itexis:
            # OA.Messagefeishu("契约锁自动巡检通知\n系统登陆正常!", "1")
            assert True
        else:
            OA.Messagefeishu("【重要信息】OA机器人自动巡检通知,生产环境深圳传音控股电子签署平台登录异常,请相关人员及时排查问题!", "1")
            assert False

    # @allure.story("二级标题：禅道平台登录巡检")  # 场景名称
    # @allure.title("三级标题：禅道平台登录巡检， 调用飞书机器消息推送结果")  # 用例名称
    # @allure.description("用例描述")
    # @allure.severity("normal")  # 用例等级
    # @pytest.mark.smoke  # 用例标记
    # def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
    #     a = SQL("OA", "test")
    #     ie = a.query_db(
    #         "select count(gdzt) from uf_gdcs where lcid in (select  requestid from workflow_requestbase where  "
    #         "currentnodetype ='3'  and requestid in(select lcid from uf_gdcs )) and gdzt !='0'")
    #     print(ie)


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
    #     pytest .\project\OA\test_case\OA_process.py
