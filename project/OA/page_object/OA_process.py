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
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class OAUserPage(Base):
    """用户类"""

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
        self.is_click_tbm(user['下一步'])

    @allure.step("点击还未装IMWAV或遇到问题？")
    def click_IMWAV(self):
        self.is_click_tbm(user['未装IMWAV'])

    @allure.step("点击通过账号密码登录")
    def click_account_password(self):
        self.is_click_tbm(user['点击通过账号密码'])

    @allure.step("输入账号密码进行登录飞书到应用系统巡检系统")
    def input_account_password(self, name, password):
        self.input_text(user['工号'], name)
        self.input_text(user['密码'], password)

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
        print("111111111111111111", sign)
        print("222", timestamp)
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

    def Messagefeishu(self, text):
        """
        OA流程开发组群聊中机器人调用，推送text消息
        """
        timestamp = round(time.time())
        sign = self.gen_sign(timestamp, "GnJHMFrsFtP4o1IXlEc1Qf")

        post_url = "https://open.feishu.cn/open-apis/bot/v2/hook/d0cf7aae-536e-49d9-80df-2c348c296e4c"
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
        self.input_text(user['签署平台用户名'], variables)

    @allure.step("输入签署平台密码")
    def input_password(self, variables):
        self.input_text(user['签署平台密码'], variables)

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


if __name__ == '__main__':
    pass
