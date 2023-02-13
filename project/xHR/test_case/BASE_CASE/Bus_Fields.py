import allure
import pytest

from project.xHR.page_object.Bus_Fields import Busfields
from public.base.assert_ui import DomAssert

"""
    用例等级说明:
        blocker级别:中断缺陷(客户端程序无响应，无法执行下一步操作)
        critical级别: 临界缺陷(功能点缺失)
        normal级别:普通缺陷(数值计算错误)
        minor级别: 次要缺陷(界面错误与UI需求不符)
        trivial级别:轻微缺陷(必输项无提示， 或者提示不规范)
"""


@allure.feature("中方入职-业务字段")  # 模块名称
class TestUtil1add:
    @allure.story("新增成功场景")  # 场景名称
    @allure.title("在业务字段页面新增薪资比例模板")  # 用例名称
    @allure.description("在业务字段页面，点击新增薪资比例模板，新增后断言提示:'新增成功',之后操作删除，提示：删除成功")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_001_001(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        a = Busfields(drivers)  # 添加类
        a.click_menu()  # 进入菜单
        a.click_NewCandidate()  # 点击新增
        a.input_Proportion('月固', '60')
        a.input_Proportion('月浮', '30')
        a.input_Proportion('季度', '10')
        a.input_Proportion('年度', '0')
        a.input_Adding()  # 新增保存按钮
        DomAssert(drivers).assert_att('新增成功')
        a.input_Deactivate('60%')  # 点击停用
        DomAssert(drivers).assert_att('保存成功')
        a.input_Deleteing('60%')  # 点击删除按钮确定删除
        DomAssert(drivers).assert_att('删除成功')


@allure.feature("中方入职-业务字段")  # 模块名称
class TestUtil2Deit:
    @allure.story("新增编辑成功场景")  # 场景名称
    @allure.title("在业务字段页面编辑数据停用后删除")  # 用例名称
    @allure.description("在业务字段页面，新增数据后，点击编辑，修改数据后成功，提示'更新成功'，操作停用提示'保存成功',操作删除提示'删除成功'")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_002_002(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        a = Busfields(drivers)  # 添加类
        a.click_menu()  # 进入菜单
        a.click_NewCandidate()  # 点击新增
        a.input_Proportion('月固', '12')
        a.input_Proportion('月浮', '18')
        a.input_Proportion('季度', '10')
        a.input_Proportion('年度', '60')
        a.input_Adding()  # 新增保存按钮
        DomAssert(drivers).assert_att('新增成功')
        a.input_Deiting('12%')  # 点击编辑
        a.input_Proportion('月固', '1')
        a.input_Proportion('月浮', '8')
        a.input_Proportion('季度', '91')
        a.input_Proportion('年度', '0')
        a.input_Adding()  # 新增保存按钮
        DomAssert(drivers).assert_att('更新成功')
        a.input_Deactivate('1%')  # 点击停用
        DomAssert(drivers).assert_att('保存成功')
        a.input_Deleteing('1%')  # 点击删除按钮确定删除
        DomAssert(drivers).assert_att('删除成功')


@allure.feature("中方入职-业务字段")  # 模块名称
class TestUtil3Delete:
    @allure.story("当状态是启用时，删除失败场景")  # 场景名称
    @allure.title("在业务字段页面新增薪资比例模板后删除")  # 用例名称
    @allure.description("在业务字段页面，点击新增薪资比例模板，新增后断言提示:新增成功,然后操作删除此数据，提示:当前为启用状态，不可删除!之后操作停用删除")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_003_003(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        a = Busfields(drivers)  # 添加类
        a.click_menu()  # 进入菜单
        a.click_NewCandidate()  # 点击新增
        a.input_Proportion('月固', '10')
        a.input_Proportion('月浮', '10')
        a.input_Proportion('季度', '10')
        a.input_Proportion('年度', '70')
        a.input_Adding()  # 新增保存按钮
        DomAssert(drivers).assert_att('新增成功')
        a.input_Deleteing2('10%')  # 点击删除按钮
        DomAssert(drivers).assert_att('当前为启用状态，不可删除！')
        a.input_Deactivate('10%')  # 点击停用
        DomAssert(drivers).assert_att('保存成功')
        a.input_Deleteing('10%')  # 继续点击删除按钮确定删除
        DomAssert(drivers).assert_att('删除成功')


@allure.feature("中方入职-业务字段")  # 模块名称
class TestUtil4Add2:
    @allure.story("新增失败场景")  # 场景名称
    @allure.title("在业务字段页面新增重复比例模板")  # 用例名称
    @allure.description("在业务字段页面，点击新增重复薪资比例模板，新增后断言提示:'已存在相同数据，请勿重复提交！'")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_004_004(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        a = Busfields(drivers)  # 添加类
        a.click_menu()  # 进入菜单
        a.click_NewCandidate()  # 点击新增
        a.input_Proportion('月固', '75')
        a.input_Proportion('月浮', '12.5')
        a.input_Proportion('季度', '0')
        a.input_Proportion('年度', '12.5')
        a.input_Adding()  # 新增保存按钮
        DomAssert(drivers).assert_att('已存在相同数据，请勿重复提交！')
        a.input_Quing()  # 取消按钮


@allure.feature("中方入职-业务字段")  # 模块名称
class TestUtil5Deit2:
    @allure.story("编辑失败场景")  # 场景名称
    @allure.title("在业务字段页面编辑异常数据后又正确编辑数据")  # 用例名称
    @allure.description("在业务字段页面，点击编辑，修改数据不正确，提示'薪资比例有误，请检查。'并取消编辑，再次编辑新增正常数据")
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke # 用例标记
    def test_005_005(self, drivers):  # 用例名称取名规范'test+场景编号+用例编号'
        a = Busfields(drivers)  # 添加类
        a.click_menu()  # 进入菜单
        a.click_NewCandidate()  # 点击新增
        a.input_Proportion('月固', '12')
        a.input_Proportion('月浮', '18')
        a.input_Proportion('季度', '20')
        a.input_Proportion('年度', '50')
        a.input_Adding()  # 新增保存按钮
        a.input_Deiting('12%')  # 点击编辑
        a.input_Proportion('月固', '1')
        a.input_Proportion('月浮', '8')
        a.input_Proportion('季度', '9')
        a.input_Proportion('年度', '99')
        a.input_Adding()  # 新增保存按钮
        DomAssert(drivers).assert_att('薪资比例有误，请检查。')
        a.input_Quing()  # 取消按钮
        a.input_Deactivate('12%')  # 点击停用
        DomAssert(drivers).assert_att('保存成功')
        a.input_Deleteing('12%')  # 继续点击删除按钮确定删除
        DomAssert(drivers).assert_att('删除成功')


if __name__ == '__main__':
    pytest.main(['project/xHR1/testcase/run_code.py'])
