import datetime

import allure
import pytest

from project.xHR.page_object.PayrollManagement_PayrollConfigure import PayrollConfigure
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("薪酬管理-薪酬配置") # 模块名称
class TestUtil:
    @allure.story("添加集团方案") # 场景名称
    @allure.title("进入集团方案页面，新增，输入已存在的编码，添加方案")  # 用例名称
    @allure.description("进入集团方案页面，新增，输入已存在的编码，其他信息正常填写，添加方案，断言判断是否弹出提示’编码已存在‘")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        # 打开薪酬配置页面
        user = PayrollConfigure(drivers)
        user.click_menus('薪酬管理','薪酬配置')
        # 打开集团方案页面
        user.click_slalary_setting('集团方案')

        # 点击新增
        user.click_add()
        # 输入新增的信息
        #user.input_code('X001'+str(random.randint(1,999)))
        user.input_code('X001')
        user.input_name('大诗人')
        date_now=datetime.datetime.now().strftime('%Y-%m-%d')   #获取当前日期
        user.input_efftivedate(date_now)
        user.input_status('启用')
        # 确定添加
        user.click_sure('确定')
        DomAssert(drivers).assert_att('编码已存在')

    @allure.story("新增集团方案")  # 场景名称
    @allure.title("薪酬配置界面，新增集团方案")  # 用例名称
    @allure.description("薪酬配置界面进入集团方案，点击新增")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 新增集团方案
        user = PayrollConfigure(drivers)
        user.click_menus('薪酬管理','薪酬配置')
        user.click_slalary_setting('集团方案')  # 点击集团方案
        user.click_add()
        user.input_code('6911t')  # 输入集团方案编码
        user.click_sure('确定')
        DomAssert(drivers).assert_att('请输入4位方案编码，由数字、字母组成')

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
