import time

import allure
import pytest
from project.xHR.page_object.Dimension_Scheme import DimensionScheme
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
    @allure.title("维度方案")  # 用例名称
    @allure.description("新增维度方案")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        a = DimensionScheme(drivers)
        a.menu()
        a.dimension_add()
        name = str(time.time())
        a.input_demensionname(name)
        a.select_set('测评类型', '干部领导力360测评[LX202106010001]')
        a.select_set('测评领域', '人事领域[LY202207270001]')
        a.click_save()
        DomAssert(drivers).assert_att('新增成功')
        a.assess_search()
        a.assess_inputinfo(name)
        a.click_searchbutton()
        a.assert_search('维度方案', name)
        a.check_box(name)
        a.delete_dimension()
        DomAssert(drivers).assert_att('删除成功')


if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
