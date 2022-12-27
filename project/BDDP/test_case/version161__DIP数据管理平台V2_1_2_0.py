import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from libs.common.action import KeyWord
import allure
@allure.feature("DIP数据管理平台V2_1_2_0")  # 迭代名称
class Teststory_2499:
    @allure.story("角色管理负责对所有的报表进行授权管理")  # 用户故事名称
    @allure.title("公开报表说明栏501字以内新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域输入业务域==输入业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型总部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_28877(self, drivers):
        pass


if __name__ == '__main__':
    pass
