import allure
import pytest
import base64
import pytest, logging

from project.OA.page_object.BPM_modeling import BPM_modeling_Page
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

    @allure.story("OA应用系统巡检")  # 场景名称
    @allure.title("三级标题：OA自动巡检登录功能，提交系统巡检报告，调用飞书机器消息推送结果")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OA = OAUserPage(drivers)
        OA.refresh()  # 刷新当前界面
        sleep(5)
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
        OA.OAlog()
        # 提交系统巡检报告
        OA.click_Inspection("深圳")
        OA.click_Inspection("OA")
        OA.input_personnel("机器人【刘艳】")
        OA.click_date()
        if itexis:
            OA.click_Inspection("系统登陆正常")
            # OA.Messagefeishu("OA自动巡检通知\n今天OA系统登陆正常！已提交系统巡检报告", "1")
            # OA.Messagefeishu("1用例ok", "1")
            assert True
        else:
            OA.click_Inspection("系统登陆异常")
            OA.input_reason("OA机器人巡检，生产环境登录OA异常。登录OA地址[https://oa.transsion.com/wui/main.jsp]")
            OA.Messagefeishu("【重要信息】OA机器人自动巡检通知,发现系统登陆异常,请相关人员及时排查问题！已提交系统巡检报告！", "1")
            assert False
        OA.click_sumbmit()

    @allure.story("OA应用系统巡检")  # 场景名称
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
            # OA.Messagefeishu("2用例ok", "1")
            assert True
        else:
            OA.Messagefeishu("【重要信息】OA机器人自动巡检通知,生产环境深圳传音控股电子签署平台登录异常,请相关人员及时排查问题!", "1")
            assert False

    @allure.story("OA应用系统巡检")  # 场景名称
    @allure.title("三级标题：合同归档催收数据监控，飞书推送消息给吴军")  # 用例名称
    @allure.description("合同归档催收数据监控，数据库查询结果大于0异常，等于0正常")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OA = OAUserPage(drivers)
        a = SQL("OA", "test")
        result = a.query_db(
            "select count(gdzt) from ECOLOGY.uf_gdcs where lcid in (select requestid from "
            "ECOLOGY.workflow_requestbase where currentnodetype ='3'  and requestid in(select lcid from "
            "ECOLOGY.uf_gdcs )) and gdzt !='0'")

        count = result[0].get("count(gdzt)")
        if count > 0:
            OA.Messagefeishu("@吴军\n合同归档催收数据同步异常,异常个数共计：{}".format(count), "1")
            # OA.Messagefeishu("3用例ok", "1")
            assert False
        elif count == 0:
            # OA.Messagefeishu("@吴军\n合同归档催收数据同步正常", "1")
            assert True

    @allure.story("OA应用系统巡检")  # 场景名称
    @allure.title("三级标题：档案管理系统巡检，飞书推送消息到OA测试群")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OA = OAdnluPage(drivers)
        OB = OAUserPage(drivers)
        OA.open_url("http://10.248.39.80/AmsHome")  # 打开应用系统巡检地址
        OB.OAlogB()
        itexis = OA.isfile_login()
        if itexis:
            # OB.Messagefeishu("4用例ok", "1")
            # OB.Messagefeishu("档案管理系统巡检通知\n系统登陆正常!", "1")
            assert True
        else:
            OB.Messagefeishu("【重要信息】OA机器人自动巡检通知,生产环境档案管理系统登录异常,请相关人员及时排查问题!", "1")
            assert False

    # @allure.story("OA应用系统巡检")  # 场景名称
    # @allure.title("三级标题：传音知识产权管理系统巡检，飞书推送消息到OA测试群")  # 用例名称
    # @allure.description("用例描述")
    # @allure.severity("normal")  # 用例等级
    # @pytest.mark.smoke  # 用例标记
    # def test_001_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
    #     OA = OAdnluPage(drivers)
    #     OB = OAUserPage(drivers)
    #     OA.open_url("https://ipr.transsion.com:8060/login.html")  # 打开应用系统巡检地址
    #     # OA.click_accountuser()
    #     # OA.click_accountlogin()  # 点击帐户密码登录
    #     OB.OAlogB()
    #     # OA.input_account_password_log('0', '1')
    #     #
    #     # OA.input_imgcode()  # 输入验证码
    #     # OA.click_checkbox()
    #     # OA.click_checkbox()
    #     # OA.click_loginsubmit()
    #     itexis = OA.ispatent_login()
    #     if itexis:
    #         # OB.Messagefeishu("5用例ok", "1")
    #         # OB.Messagefeishu("传音知识产权管理系统巡检通知\n系统登陆正常!", "1")
    #         assert True
    #     else:
    #         OB.Messagefeishu("【重要信息】OA机器人自动巡检通知,生产环境传音知识产权管理系统登录异常,请相关人员及时排查问题!", "1")
    #         assert False

    @allure.story("OA应用系统巡检")  # 场景名称
    @allure.title("三级标题：BPM开发环境管理端登录")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_006(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OB = OAUserPage(drivers)
        OA = OAdnluPage(drivers)
        OA.BPMlog(options=3)
        bmmA = BPM_modeling_Page(drivers)
        itexis = bmmA.ismodeling_login()
        if itexis:
            # OB.Messagefeishu("BPM开发环境管理端登录成功", "4")
            assert True
        else:
            OB.Messagefeishu("BPM开发环境管理端登录失败", "4")
            assert False

    @allure.story("OA应用系统巡检")  # 场景名称
    @allure.title("三级标题：BPM测试环境管理端登录")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_007(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OB = OAUserPage(drivers)
        OA = OAdnluPage(drivers)
        OA.BPMlog(options=1)
        bmmA = BPM_modeling_Page(drivers)
        itexis = bmmA.ismodeling_login()
        if itexis:
            # OB.Messagefeishu("BPM测试环境管理端登录成功", "4")
            assert True
        else:
            OB.Messagefeishu("BPM测试环境管理端登录失败", "4")
            assert False

    @allure.story("OA应用系统巡检")  # 场景名称
    @allure.title("三级标题：BPM—UAT环境管理端登录")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_008(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OB = OAUserPage(drivers)
        OA = OAdnluPage(drivers)
        OA.BPMlog(options=2)
        bmmA = BPM_modeling_Page(drivers)
        itexis = bmmA.ismodeling_login()
        if itexis:
            # OB.Messagefeishu("BPM—UAT环境管理端登录成功", "4")
            assert True
        else:
            OB.Messagefeishu("BPM—UAT环境管理端登录失败", "4")
            assert False

    @allure.story("OA应用系统巡检")  # 场景名称
    @allure.title("三级标题：BPM—生产环境管理端登录")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_009(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OB = OAUserPage(drivers)
        OA = OAdnluPage(drivers)
        OA.open_url("https://bpm.transsion.com/mvue/")
        OB.OAlogB()
        bmmA = BPM_modeling_Page(drivers)
        itexis = bmmA.ismodeling_login()
        if itexis:
            # OB.Messagefeishu("BPM—生产环境管理端登录成功", "4")
            assert True
        else:
            OB.Messagefeishu("BPM—生产环境管理端登录失败", "4")
            assert False

    @allure.story("OA应用系统巡检")  # 场景名称
    @allure.title("三级标题：BPM【制造中心的生产环境】端登录")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_010(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OB = OAUserPage(drivers)
        OA = OAdnluPage(drivers)
        OA.open_url("http://10.129.2.246:9081/mvue/")  # 打开应用系统巡检地址
        OB.OAlogB()
        bmmA = BPM_modeling_Page(drivers)
        itexis = bmmA.ismodeling_login()
        if itexis:
            # OB.Messagefeishu("BPM【制造中心的生产环境】端登录成功", "4")
            assert True
        else:
            OB.Messagefeishu("BPM【制造中心的生产环境】端登录失败", "4")
            assert False


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
    #     pytest .\project\OA\test_case\OA_process.py
