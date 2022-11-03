import allure
import pytest
from project.xHR.page_object.Assessment_Type import AssessmentType
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("测评设置") # 模块名称
class TestSearch:
    @allure.story("测评类型") # 场景名称
    @allure.title("查询")  # 用例名称
    @allure.description("查询测评类型")
    @allure.severity("trivial")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        a = AssessmentType(drivers)
        a.assess_type()
        a.assess_search()
        a.assess_inputinfo('LX202106010001')
        a.click_searchbutton()
        a.assert_search('测评类型编码', 'LX202106010001')




if __name__ == '__main__':
    pytest.main(['project/XHR/testcase/run_code.py'])
