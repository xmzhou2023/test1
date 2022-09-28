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


@allure.feature("禅道应用系统巡检")  # 模块名称
class TestZenUtil:

    @allure.story("二级标题：禅道平台登录巡检")  # 场景名称
    @allure.title("三级标题：禅道平台登录巡检， 调用飞书机器消息推送结果")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        OB = OAUserPage(drivers)
        OA = OAdnluPage(drivers)
        OA.open_url("http://zentao.transsion.com:9090")  # 打开禅道地址
        OA.input_Zenuser(0, 1)
        OA.click_Zencheckbox()
        OA.click_Zensubmit()
        sleep(10)
        itexis = OA.isZenlogin()
        if itexis:
            # OB.Messagefeishu("巡检通知\n禅道登录正常", "3")
            assert True
        else:
            OB.Messagefeishu("巡检通知\n禅道登录异常", "3")
            assert False


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
    #     pytest .\project\OA\test_case\OA_login.py
