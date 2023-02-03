import time

import allure
import pytest
from project.xHR.page_object.Assessment_Field import AssessField
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("测评中心") # 模块名称
class TestAdd:
    @allure.story("测评设置") # 场景名称
    @allure.title("测评领域")  # 用例名称
    @allure.description("新增测评领域")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        a = AssessField(drivers)
        a.assess_field()
        a.Field_add()
        name = str(time.time())
        a.input_fieldname(name)
        a.click_save()
        DomAssert(drivers).assert_att('新增成功')
        a.assess_search()
        a.assess_inputinfo(name)
        a.click_searchbutton()
        a.assert_search('测评领域',name)
        a.check_box(name)
        a.delete()
        DomAssert(drivers).assert_att('删除成功')

    @allure.story("测评设置")  # 场景名称
    @allure.title("测评领域")  # 用例名称
    @allure.description("测评领域名称非空校验")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        a = AssessField(drivers)
        a.assess_field()
        a.Field_add()
        a.input_fieldname('')
        a.click_save()
        DomAssert(drivers).assert_att('不能为空')


@allure.feature("测评中心") # 模块名称
class TestEdit:
    @allure.story("测评设置") # 场景名称
    @allure.title("测评领域")  # 用例名称
    @allure.description("编辑测评领域")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_002_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        a = AssessField(drivers)
        a.assess_field()
        a.assess_search()
        a.assess_inputinfo('HR-TEST-AUTO(勿删)')
        a.click_searchbutton()
        a.assert_search('测评领域','HR-TEST-AUTO(勿删)')
        a.disable_field()
        DomAssert(drivers).assert_att('停用成功')
        a.enable_field()
        DomAssert(drivers).assert_att('启用成功')


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
