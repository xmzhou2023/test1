import pytest
from public.base.assert_ui import *
from project.TLC_web.page_object.Center_Component import NavPage
from project.TLC_web.page_object.Card_Label import label

# 卡片中心-卡片属性
@allure.feature("新增分类管理")
class TestAddLabel:
    # 新增标签
    @allure.story("卡片属性新增")
    @allure.title("新增卡片标签")
    @allure.description("‘新增卡片标签’成功操作")
    @allure.severity("critical")  # blocker\critical\normal\minor\trivial
    # @pytest.mark.smoke
    def test_001_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.append_button()
        user.add_label(input_labelName='autozz0829010', input_Description='testssssssauto')
        user.add_save("标签新增正例")
        user = DomAssert(drivers)
        user.assert_exact_att("autozz0829010")



    @allure.story("卡片属性新增")
    @allure.title("【异常】新增标签名称为空")
    @allure.description("‘新增卡片标签’名称必填项校验")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_001_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.append_button()
        user.add_label(input_labelName='', input_Description='testssssssauto')
        user.add_save("标签名称为空")

    @allure.story("卡片属性新增")
    @allure.title("【异常】新增重复标签")
    @allure.description("‘新增卡片标签’重复名称校验")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_001_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.append_button()
        user.add_label(input_labelName='08_19fulltestedit', input_Description='auto')
        user.add_save("标签名称重复")
        user = DomAssert(drivers)
        user.assert_exact_att("卡片组别添加失败")

    @allure.story("卡片属性新增")
    @allure.title("新增弹框关闭场景1")
    @allure.description("‘新增卡片标签’右上角X关闭弹框")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_001_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.append_button()
        user.close_screen()

    @allure.story("卡片属性新增")
    @allure.title("新增弹框关闭场景2")
    @allure.description("‘新增卡片标签’取消按钮关闭弹框")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_001_005(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.append_button()
        user.append_cancel()


@allure.feature("编辑卡片属性")
class TestEditLabel:
    # 编辑标签

    @allure.story("卡片属性编辑")
    @allure.title("编辑卡片属性成功")
    @allure.description("‘编辑卡片属性’编辑修改成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_002_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.edit_button()
        user.edit_label(edit_labelName='zzedit0829005', edit_Description='sssssauto')
        user.edit_save("标签编辑正例")
        user = DomAssert(drivers)
        user.assert_exact_att("zzedit0829005")

    @allure.story("卡片属性编辑")
    @allure.title("【异常】编辑标签名称为空")
    @allure.description("‘编辑卡片属性’卡片名称必填项校验")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_002_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.edit_button()
        user.edit_label(edit_labelName='', edit_Description='sssssauto')
        user.edit_save("编辑标签名称为空")


    @allure.story("卡片属性编辑")
    @allure.title("【异常】编辑标签名称重复")
    @allure.description("‘编辑卡片属性’重复名称校验")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_002_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.edit_button()
        user.edit_label(edit_labelName='08_19fulltestedit', edit_Description='sssssauto')
        user.edit_save("编辑标签名称重复")
        user = DomAssert(drivers)
        user.assert_exact_att("卡片组别修改失败")

    @allure.story("卡片属性编辑")
    @allure.title("编辑弹框关闭场景1")
    @allure.description("‘编辑卡片标签’右上角X关闭弹框")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_002_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.edit_button()
        user.edit_close()

    @allure.story("卡片属性编辑")
    @allure.title("编辑弹框关闭场景2")
    @allure.description("‘编辑卡片标签’取消按钮关闭弹框")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_002_005(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.edit_button()
        user.edit_cancel()


class TestStateLabel:
    # 标签状态切换

    @allure.story("卡片属性状态切换")
    @allure.title("启用卡片标签")
    @allure.description("‘启用卡片属性’成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_004_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.enable_label()

    @allure.story("卡片属性状态切换")
    @allure.title("禁用卡片标签")
    @allure.description("‘禁用卡片属性’成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_004_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.disable_label()

    @allure.story("卡片属性状态切换")
    @allure.title("取消禁用卡片标签")
    @allure.description("‘禁用卡片属性’取消操作")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_004_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.disable_cancel()

    @allure.story("卡片属性状态切换")
    @allure.title("关闭禁用卡片标签弹框")
    @allure.description("‘禁用卡片属性’弹框关闭")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_004_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.disable_close()

@allure.feature("查询卡片属性")
class TestQueryLabel:
    # 标签查询

    @allure.story("卡片属性查询")
    @allure.title("卡片标签启用查询")
    @allure.description("‘卡片属性名称状态查询’启用状态")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_005_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.query_label()
        user.query_labelName(query_labelName='视图')
        user.query_labelState(query_labelState='启用')


    @allure.story("卡片属性查询")
    @allure.title("卡片标签禁用查询")
    @allure.description("‘卡片属性名称状态查询’禁用状态")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_005_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.query_label()
        user.query_labelName(query_labelName='测试')
        user.query_labelState(query_labelState='禁用')


    @allure.story("卡片属性查询")
    @allure.title("卡片标签查询取消按钮")
    @allure.description("‘卡片属性查询取消’取消成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_005_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.query_label()
        user.query_cancel()

    @allure.story("卡片属性查询")
    @allure.title("卡片标签查询弹框关闭")
    @allure.description("‘卡片属性查询弹框关闭’关闭成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_005_004(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.query_label()
        user.query_close()

    @allure.story("卡片属性查询")
    @allure.title("卡片标签查询重置条件")
    @allure.description("‘卡片属性查询重置’重置成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_005_005(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.query_label()
        user.query_reset()

@allure.feature("删除卡片属性")
class TestDelLabel:
    # 删除标签

    @allure.story("卡片属性删除")
    @allure.title("删除卡片属性")
    @allure.description("‘删除卡片属性’成功")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_006_001(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.del_button()
        user.del_save()

    @allure.story("卡片属性删除")
    @allure.title("取消删除卡片属性")
    @allure.description("‘删除卡片属性‘取消删除操作")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_006_002(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.del_button()
        user.del_cancel()



    @allure.story("卡片属性删除")
    @allure.title("关闭删除卡片属性弹框")
    @allure.description("‘删除卡片属性‘关闭删除弹框")
    @allure.severity("normal")  # blocker\critical\normal\minor\trivial
    def test_006_003(self, drivers):
        user = NavPage(drivers)
        user.click_gotonav("卡片中心", "分类管理")
        user = DomAssert(drivers)
        user.assert_url("/card-manage/attribute")
        user = label(drivers)
        user.page_click()
        user.del_button()
        user.del_close()


if __name__ == '__main__':
    pytest.main(['project/TLC_web/test_case/Card_Label.py'])