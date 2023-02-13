import allure, os
from public.base.basics import Base, sleep
import hashlib
import base64
import hmac
import time
import json
import requests
from libs.common.read_element import Element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging
from public.libs.unified_login.login import Login
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class OAUserPage(Base):
    """用户类"""

    def input_text_oa(self, locator, txt, *choice):
        """输入文本"""
        sleep(0.5)
        ele = self.find_element(locator, *choice)
        ele.clear()
        pwd_list = self.password()
        pwd_str = str(pwd_list[int(txt)]).lstrip("b'").rstrip("'")
        ele.send_keys(pwd_str)

    @allure.step("判断OA是否登录成功，到home页面")
    def islogin(self):
        itexis = self.element_exist(user["OA登录成功界面"])
        return itexis

    @allure.step("打开应用系统巡检地址")
    def open_url(self, url):
        self.get_url(url)

    @allure.step("点击飞书登录切账号登录")
    def click_toggle(self):
        self.is_click_tbm(user['飞书登录切账号登录'])

    @allure.step("勾选飞书登录已阅同意")
    def click_read(self):
        self.is_click_tbm(user['飞书登录已阅同意'])

    @allure.step("点击sso登录")
    def click_SSO(self):
        self.is_click_tbm(user['sso登录'])

    @allure.step("输入企业名")
    def input_company_name(self, variables):
        self.input_text(user['输入企业名'], variables)

    @allure.step("点击下一步")
    def click_Next(self):
        element = self.find_elements(user['下一步'])
        element[len(element) - 1].click()

    @allure.step("点击还未装IMWAV或遇到问题？")
    def click_IMWAV(self):
        self.is_click_tbm(user['未装IMWAV'])

    @allure.step("点击通过账号密码登录")
    def click_account_password(self):
        self.is_click_tbm(user['点击通过账号密码'])


    @allure.step("输入账号密码进行登录飞书到应用系统巡检系统")
    def input_account_password(self, name, password):
        sleep(10)
        self.input_text_oa(user['工号'], name)
        self.input_text_oa(user['密码'], password)

    @allure.step("点击登录")
    def click_Login(self):
        self.is_click_tbm(user['登录'])

    @allure.step("点击巡检区域加模块加巡检")
    def click_Inspection(self, variables):
        self.is_click_tbm(user['巡检区域加模块加巡检'], variables)

    @allure.step("输入巡检人员")
    def input_personnel(self, variables):
        self.input_text(user['巡检人员'], variables)

    @allure.step("点击巡检日期，确认")
    def click_date(self):
        self.is_click_tbm(user['巡检日期'])
        self.is_click_tbm(user['巡检日期确认'])

    @allure.step("点击巡检日期，确认")
    def click_sumbmit(self):
        self.is_click_tbm(user['提交按钮'])
        # 异常原因

    @allure.step("输入系统登陆异常原因")
    def input_reason(self, variables):
        self.input_text(user['异常原因'], variables)

    def gen_sign(self, timestamp, secret):
        "获得签名和时间戳后，调用飞书机器人，发送消息"
        # 拼接timestamp和secret
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()

        # 对结果进行base64处理
        sign = base64.b64encode(hmac_code).decode('utf-8')
        return sign

    def request_post(self, url, param):
        """调用飞书消息接口"""
        fails = 0
        while True:
            try:
                if fails >= 20:
                    break

                headers = {'content-type': 'application/json'}
                ret = requests.post(url, json=param, headers=headers, timeout=10)

                if ret.status_code == 200:
                    text = json.loads(ret.text)
                else:
                    continue
            except:
                fails += 1
                print('网络连接出现问题, 正在尝试再次请求: ', fails)
            else:
                break
        return text

    def Messagefeishu(self, text, choose):
        """
        OA流程开发组群聊中机器人调用，推送text消息,
        OA开发大群：SGtaWNm59KG22fKyFRFIu  https://open.feishu.cn/open-apis/bot/v2/hook/17490e59-2cdd-40cc-98da-edd949b4508e
        OA测试群：wc1EQGbcebUVGmZMBPhbUe  https://open.feishu.cn/open-apis/bot/v2/hook/ca9f9bbc-6bc0-4c15-b0b0-66f82f17f8d9
        禅道大群： TI382IhVUAI6FtxqAWb3Vh   https://open.feishu.cn/open-apis/bot/v2/hook/5e74a61c-b59c-4fa3-bad5-c87db5eefe49

        """
        timestamp = round(time.time())
        if choose == "1":  # OA测试群
            sign = self.gen_sign(timestamp, "wc1EQGbcebUVGmZMBPhbUe")
            post_url = "https://open.feishu.cn/open-apis/bot/v2/hook/ca9f9bbc-6bc0-4c15-b0b0-66f82f17f8d9"
        elif choose == "2":  # 禁用 OA开发大群
            sign = self.gen_sign(timestamp, "SGtaWNm59KG22fKyFRFIu")
            post_url = "https://open.feishu.cn/open-apis/bot/v2/hook/17490e59-2cdd-40cc-98da-edd949b4508e"
        elif choose == "3":  # 禁用 禅道大群
            sign = self.gen_sign(timestamp, "TI382IhVUAI6FtxqAWb3Vh")
            post_url = "https://open.feishu.cn/open-apis/bot/v2/hook/5e74a61c-b59c-4fa3-bad5-c87db5eefe49"
        elif choose == "4":  # 禁用 BPM测试群
            sign = self.gen_sign(timestamp, "RdwWixnXElNrzkL7K0uPBh")
            post_url = "https://open.feishu.cn/open-apis/bot/v2/hook/df935d46-60cb-4b07-8e62-af9d067c44b5"


        request_param = {
            "timestamp": timestamp,
            "sign": sign,
            "msg_type": "text",
            "content": {
                "text": text
            }
        }
        a = self.request_post(post_url, request_param)
        print(a)

    #
    @allure.step("输入签署平台用户名")
    def input_username(self, variables):
        self.input_text_oa(user['签署平台用户名'], variables)

    @allure.step("输入签署平台密码")
    def input_password(self, variables):
        self.input_text_oa(user['签署平台密码'], variables)

    @allure.step("点击签署平台-登录按钮")
    def click_button(self):
        self.is_click_tbm(user['签署平台登录'])

    @allure.step("判断签署平台是否登录成功到home页面")
    def issign_login(self):
        itexis = self.element_exist(user["签署平台首页"])
        return itexis

    def password(self):
        aa = base64.decodebytes(bytes("MTg2NDcyMjA=\n", 'utf-8'))
        pa = base64.decodebytes(bytes("dGVkZHlAMjg2Mw==\n", 'utf-8'))
        cc = base64.decodebytes(bytes("MTg2NjQzMzMyNDM=\n", 'utf-8'))
        dd = base64.decodebytes(bytes("MzI0OTIyQHd1\n==\n", 'utf-8'))
        return aa, pa, cc, dd

    @allure.step("登录OA正式环境")
    def OAlog(self, options=1, Job="18647220"):
        self.frame_enter(user["iframe"])
        if options == 1:
            self.input_newaccount(Job)  # 默认使用刘艳的号登录BPM
            self.input_newpasswd("teddy@2863")
            aa = 0
            count = 0
            # 如果a=1 就跳出循环
            while aa == 0 and count < 10:
                count += 1
                self.input_newimgcode()
                self.click_newloginsubmit()
                itexis = self.element_exist(user["新登录按钮"])
                if itexis:
                    aa = 0
                else:
                    aa = 1

    @allure.step("登录OA正式环境,不用重新获取iframe")
    def OAlogB(self, options=1, Job="18647220"):
        if options == 1:
            self.input_newaccount(Job)  # 默认使用刘艳的号登录BPM
            self.input_newpasswd("teddy@2863")
            aa = 0
            count = 0
            # 如果a=1 就跳出循环
            while aa == 0 and count < 10:
                count += 1
                self.input_newimgcode()
                self.click_newloginsubmit()
                itexis = self.element_exist(user["新登录按钮"])
                if itexis:
                    aa = 0
                else:
                    aa = 1

    def input_newaccount(self, content):
        """输入工号"""
        self.input_text(user['新账号名'], txt=content)

    def input_newpasswd(self, content):
        """输入密码"""
        self.input_text(user['新密码'], txt=content)

    def click_newloginsubmit(self):
        """点击帐号密码登录"""
        self.is_click(user['新登录按钮'])

    def input_newimgcode(self):
        """识别图形验证码，输入验证码"""
        imgcode = self.get_graphical_code(user['图形验证码'])
        self.input_text(user['图形验证码输入框输入'], imgcode)


if __name__ == '__main__':
    pass
