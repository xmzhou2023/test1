import allure
import pytest

from project.XHR.page_object.ZFRZ_Candidate import Candidate
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""


@allure.feature("中方入职-候选人")  # 模块名称
class TestSearch:
    @allure.story("查询候选人")  # 场景名称
    @allure.title("查询多条件字段")  # 用例名称
    @allure.description("查询候选人编号、姓名、电话字段成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        a = Candidate(drivers)
        # 进入菜单
        a.click_menu()
        # 筛选按钮
        a.click_ShaiX()
        # 筛选数据
        a.input_selectOK('候选人编号', '202207280002')
        a.input_selectOK('姓名', '登记表2')
        a.input_selectOK('电话', '14400000005')
        # 点击查询
        a.click_ChaXButton()
        a.assert_search('候选人编号', '202207280002')

@allure.feature("中方入职-候选人")  # 模块名称
class TestAdd:
    @allure.story("新增候选人")  # 场景名称
    @allure.title("新增一条候选人")  # 用例名称
    @allure.description("新增候选人姓名、出生年份、性别、电话、国籍、农业院校、对接HR、学历、英文名字、招聘渠道必填字段")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_002_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        a = Candidate(drivers)
        # 新增数据
        a.click_menu()
        a.click_NewCandidate()
        phone = a.get_mobile()
        a.input_Parameter('姓名', '可可子2')
        a.input_Parameter('出生年份', '2000')
        a.input_Parameter('性别', '女')
        a.input_Parameter('电话', phone)
        a.input_Parameter('国籍', '中国')
        a.input_Parameter('邮箱', '1598043326@qq.com')
        a.input_Parameter('毕业院校', '深圳大学')
        a.input_Parameter('对接HR', '李菁豆')
        a.input_Parameter('学历', 'high school高中')
        a.input_Parameter('英文名字', 'Bean')
        a.input_Parameter('招聘渠道', '前程无忧')
        a.click_SaveCandidate()  # 保存按钮
        DomAssert(drivers).assert_att('新增成功')
        # 查询
        # 筛选按钮
        a.click_ShaiX()
        # 筛选数据
        a.input_selectOK('电话', phone)
        # 点击查询
        a.click_ChaXButton()
        # 结果
        a.assert_search('电话', phone)
        a.assert_search('对接HR', '李菁豆')
        a.assert_search('性别', '女')
        a.assert_search('姓名', '可可子2')
        a.click_DeleteHouxuanren('可可子2')

@allure.feature("中方入职-候选人")  # 模块名称
class TestDelete:
    @allure.story("删除候选人")  # 场景名称
    @allure.title("测试删除候选人成功")  # 用例名称
    @allure.description("指定删除候选人")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        a = Candidate(drivers)
        a.click_menu()  # 删除按钮
        a.Delete_after_data()  # 新增数据后删除
        a.click_DeleteHouxuanren('可可子2')
        DomAssert(drivers).assert_att('删除成功')


if __name__ == '__main__':
    pytest.main(['project/xHR1/testcase/run_code.py'])
