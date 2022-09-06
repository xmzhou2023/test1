import allure
import pytest

from project.TBM.page_object.BOM2 import UserPage
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""

@allure.feature("脚本名称") # 模块名称
class TestUtil:
    @allure.story("二级标题") # 场景名称
    @allure.title("三级标题")  # 用例名称
    @allure.description("用例描述")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):   # 用例名称取名规范'test+场景编号+用例编号'
        user = UserPage(drivers)
        user.click_menu('BOM协作', '单机头BOM协作')
        user.click_add()
        user.click_Bom('制作类型','单机头BOM制作')
        user.click_Bom('品牌','itel')
        user.click_Bom('机型','C6769')
        user.click_Bom('阶段','试产阶段')
        user.click_Bom('市场','孟加拉')
        user.click_Bom('同时做衍生BOM', '否')
        user.click_add_bom()
        user.click_bom_tree('BOM状态','试产')
        user.click_bom_tree('物料编码','12000001')
        user.click_bom_tree('用量','1000')
        user.click_qd()
        user.click_shr('MPM','李小素','18645960')
        user.click_submit()
        DomAssert(drivers).assert_att('创建流程成功')
        user.click_search()
        code = user.get_code('C6769')
        user.click_menu1('待办列表', '我申请的')
        user.click_xq(code)
        user.click_ch()
        user.click_menu('BOM协作', '单机头BOM协作')
        user.click_delete(code)
        DomAssert(drivers).assert_att('删除成功')
        pass

if __name__ == '__main__':
    pytest.main(['project/DRP/testcase/run_code.py'])
