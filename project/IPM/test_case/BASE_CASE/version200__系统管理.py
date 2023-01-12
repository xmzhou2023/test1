import allure
import pytest
from project.IPM.page_object.system_management import *
from project.IPM.api.api_system_management import *
@allure.feature("系统管理")  # 迭代名称
class Teststory_4488:
    @allure.story("对象管理/对象类型_树形对象左上图标")  # 用户故事名称
    @allure.title("新增对象选中根节点，点击新增子对象操作在菜单上直接点击悬浮的''标识，树型菜单中增加一个节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31245(self, drivers):

        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test=SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称',proname)
        test.system_management_object_newbaseclass('确认')
        ass = Assert_result_system_management(drivers)
        ass.elements_assert(proname,'对象_树结构_对象查询')
        get_object_delete(proname)


    @allure.story("对象管理/对象类型_树形对象左上图标")  # 用户故事名称
    @allure.title("新增子对象选中对象，点击''标识，树型菜单中选中的对象增加一个子节点")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31246(self, drivers):

        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        bjname = f'IPM子对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_all(proname)
        test.system_management_object_upper_function('新建')
        test.system_management_object_editobject(bjname)
        test.system_management_object_functionkeys_confirm_cancel("确定")
        ass = Assert_result_system_management(drivers)
        ass.elements_assert(bjname, '对象_树结构_对象查询')
        get_object_delete(proname)


    @allure.story("对象管理/对象类型_树形对象左上图标")  # 用户故事名称
    @allure.title("删除对象若对象未启用，且无子对象或子对象全部未启用，可删除选中的对象及其子对象，提示'请确定删除选定的对象及子对象'；")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31247(self, drivers):

        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_righ(proname, '删除')
        ass = Assert_result_system_management(drivers)
        ass.assert_toast("对象_删除节点提示", '是否删除该节点?')
        test.system_management_object_functionkeys('确定')


    @allure.story("对象管理/对象类型_树形对象左上图标")  # 用户故事名称
    @allure.title("删除对象若对象启用，则删除提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31248(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_righ(proname, '检出')
        test.system_management_object_checkingin("状态", "确定")
        test.system_management_object_functionkeys('检入')
        test.system_management_object_all(proname)
        test.system_management_object_righ(proname, '删除')
        test.system_management_object_functionkeys('确定')
        ass = Assert_result_system_management(drivers)
        ass.assert_toast("断言提示", '只有未启用的节点才允许删除！')
        get_object_delete(proname)

    @allure.story("对象管理/对象类型_树形对象左上图标")  # 用户故事名称
    @allure.title("删除对象选中的对象无子对象且未启用，点击'删除'标识，可删除选中的对象")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31249(self, drivers):

        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_righ(proname, '检出')
        test.system_management_object_checkingin("状态","确定")
        test.system_management_object_functionkeys('检入')
        test.system_management_object_all(proname)
        test.system_management_object_righ(proname, '删除')
        ass = Assert_result_system_management(drivers)
        ass.assert_toast("对象_删除节点提示", '是否删除该节点?')


    @allure.story("对象管理/对象类型_树形对象左上图标")  # 用户故事名称
    @allure.title("删除对象选中的对象或子对象有启用或禁用的状态，点击'删除'标识，不能删除，并提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31250(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_righ(proname, '检出')
        test.system_management_object_checkingin("状态", "确定")
        test.system_management_object_functionkeys('检入')
        test.system_management_object_upper_function('新建')
        test.system_management_object_editobject('IPM子对象创建')
        test.system_management_object_righ("IPM子对象创建", '检出')
        test.system_management_object_checkingin("状态", "确定")
        test.system_management_object_functionkeys('检入')
        test.system_management_object_all(proname)
        test.system_management_object_righ(proname, '删除')
        ass = Assert_result_system_management(drivers)
        ass.assert_toast("对象_删除节点提示", '是否删除该节点?')
        test.system_management_object_functionkeys('确定')


    @allure.story("对象管理/对象类型_树形对象左上图标")  # 用户故事名称
    @allure.title("搜索支持模糊查询对象名称")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31251(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_upper_function('查询','IPM')
        ass = Assert_result_system_management(drivers)
        ass.assert_toast("对象_获取指定对象的名称", 'IPM')
        test.system_management_object_all(proname)
        test.system_management_object_righ(proname,'删除','确定')


    @allure.story("对象管理/对象类型_树形对象左上图标")  # 用户故事名称
    @allure.title("上移同一个父对象节点下，同一层级，可上移")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31252(self, drivers):

        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_all(proname)
        test.system_management_object_upper_function('新建')
        test.system_management_object_editobject('IPM子对象创建_1')
        test.system_management_object_all(proname)
        test.system_management_object_upper_function('新建')
        test.system_management_object_editobject('IPM子对象创建_2')
        test.system_management_object_all("IPM子对象创建_2")
        test.system_management_object_upper_function('上移')
        ass = Assert_result_system_management(drivers)
        ass.elements_assert("IPM子对象创建_2", '对象_树结构_获取对象下面子对象的第一个对象',proname)
        test.system_management_object_all(proname)
        test.system_management_object_righ(proname,'删除','确定')


    @allure.story("对象管理/对象类型_树形对象左上图标")  # 用户故事名称
    @allure.title("上移不同父节点下，不可上移")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31253(self, drivers):

        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_all(proname)
        test.system_management_object_upper_function('新建')
        test.system_management_object_editobject('IPM子对象创建_1')
        test.system_management_object_all(proname)
        test.system_management_object_upper_function('新建')
        test.system_management_object_editobject('IPM子对象创建_2')
        test.system_management_object_all("IPM子对象创建_1")
        test.system_management_object_upper_function('上移')
        ass = Assert_result_system_management(drivers)
        ass.elements_assert("IPM子对象创建_1", '对象_树结构_获取对象下面子对象的第一个对象',proname)
        test.system_management_object_all(proname)
        test.system_management_object_righ(proname,'删除','确定')


    @allure.story("对象管理/对象类型_树形对象左上图标")  # 用户故事名称
    @allure.title("下移同一个父对象节点下，同一层级，可下移位置")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31254(self, drivers):

        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_all(proname)
        test.system_management_object_upper_function('新建')
        test.system_management_object_editobject('IPM子对象创建_1')
        test.system_management_object_all(proname)
        test.system_management_object_upper_function('新建')
        test.system_management_object_editobject('IPM子对象创建_2')
        test.system_management_object_all("IPM子对象创建_1")
        test.system_management_object_upper_function('下移')
        ass = Assert_result_system_management(drivers)
        ass.elements_assert("IPM子对象创建_2", '对象_树结构_获取对象下面子对象的第一个对象',proname)
        test.system_management_object_all(proname)
        test.system_management_object_righ(proname,'删除','确定')



    @allure.story("对象管理/对象类型_树形对象左上图标")  # 用户故事名称
    @allure.title("下移不同层级，不可下移")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31255(self, drivers):

        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_all(proname)
        test.system_management_object_upper_function('新建')
        test.system_management_object_editobject('IPM子对象创建_1')
        test.system_management_object_all(proname)
        test.system_management_object_upper_function('新建')
        test.system_management_object_editobject('IPM子对象创建_2')
        test.system_management_object_all("IPM子对象创建_2")
        test.system_management_object_upper_function('下移')
        ass = Assert_result_system_management(drivers)
        ass.elements_assert("IPM子对象创建_1", '对象_树结构_获取对象下面子对象的第一个对象',proname)
        ass.elements_assert("IPM子对象创建_2", '对象_树结构_获取对象下面子对象的第二个对象',proname)
        test.system_management_object_all(proname)
        test.system_management_object_righ(proname,'删除','确定')


    @allure.story("对象管理/对象类型_树形对象左上图标")  # 用户故事名称
    @allure.title("展开针对父对象下的子对象进行展开")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31256(self, drivers):

        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_upper_function('展开')
        ass = Assert_result_system_management(drivers)
        ass.element_not_found("对象_树结构_全部展开按钮收缩")


    @allure.story("对象管理/对象类型_树形对象左上图标")  # 用户故事名称
    @allure.title("收缩针对父对象下的子对象进行收缩")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31257(self, drivers):

        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_upper_function('收起')
        ass = Assert_result_system_management(drivers)
        ass.element_not_found("对象_树结构_全部收缩按钮展开")


@allure.feature("系统管理")  # 迭代名称
class Teststory_4489:
    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("进入对象管理页面，系统初始加载了所有基类的对象（基类对象提前定义），可对基类对象进行检出编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31258(self, drivers):

        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.get_url_system_management_object()
        test.system_management_object_all(proname)
        test.system_management_object_functionkeys('检出')
        ass = Assert_result_system_management(drivers)
        ass.elements_assert("检入", '对象_检入检出功能键','检入')
        get_object_delete(proname)


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("对象基本属性/对象图标可更换图标")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31259(self, drivers):

        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.get_url_system_management_object()
        test.system_management_object_all(proname)
        test.system_management_object_functionkeys('检出')
        test.system_management_object_checkingin('选择图标','上传图标',"确定")
        ass = Assert_result_system_management(drivers)
        ass.elements_assert("https://transsion-platform02.oss-cn-shenzhen.aliyuncs.com/avatar/%E4%B8%8A%E4%BC%A0%E5%9B%BE%E6%A0%87.jpeg",
                            '对象_检入中_断言上传图标地址',get_attribute='src')
        test.system_management_object_functionkeys('撤销检出')
        test.system_management_object_functionkeys_confirm_cancel('确定')
        get_object_delete(proname)


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("对象基本属性/对象编码50char，新增自动生成；不可编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31260(self, drivers):

        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.get_url_system_management_object()
        test.system_management_object_all(proname)
        test.system_management_object_functionkeys('检出')
        ass = Assert_result_system_management(drivers)
        ass.element_not_found("对象_检入中_字段不可编辑",True,'BID')
        test.system_management_object_functionkeys('撤销检出')
        test.system_management_object_functionkeys_confirm_cancel('确定')
        get_object_delete(proname)



    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("对象基本属性/对象名称50char，可编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31261(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.get_url_system_management_object()
        test.system_management_object_all(proname)
        test.system_management_object_functionkeys('检出')
        ass = Assert_result_system_management(drivers)
        ass.element_not_found("对象_检入中_字段不可编辑",choice='对象名称')
        test.system_management_object_functionkeys('撤销检出')
        test.system_management_object_functionkeys_confirm_cancel('确定')
        get_object_delete(proname)



    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("对象基本属性/父对象显示父对象的值不可编辑，根据父对象的名称实时变化")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31262(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        objectname= f'IPM子对象测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_all(proname)
        test.system_management_object_functionkeys('新建', proname, '确定', objectname)
        test.get_url_system_management_object()
        test.system_management_object_all(objectname, proname)
        test.system_management_object_all(objectname)
        test.system_management_object_righ(objectname, '检出')
        ass = Assert_result_system_management(drivers)
        ass.element_not_found("对象_检入中_字段不可编辑",True, choice='父对象')
        get_object_delete(proname)



    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("对象基本属性/状态/未启用一旦对象设置为'启用'或'禁用'状态，'未启用'状态不显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31263(self, drivers):

        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_all(proname)
        test.system_management_object_functionkeys('检出')
        test.system_management_object_checkingin("状态","确定")
        ass = Assert_result_system_management(drivers)
        ass.element_not_found("对象_检入中_字段框_启用禁用未启用文本",choice='未启用')
        test.system_management_object_functionkeys('撤销检出')
        test.system_management_object_functionkeys_confirm_cancel('确定')
        get_object_delete(proname)

    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("对象基本属性/状态/未启用'未启用'状态的对象可删除")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31264(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_all(proname)
        test.system_management_object_righ(proname, '删除')
        ass = Assert_result_system_management(drivers)
        ass.assert_toast("对象_删除节点提示", '是否删除该节点?')
        test.system_management_object_functionkeys('确定')
        test.get_url_system_management_object()
        ass.element_not_found("对象_点击对象名称", choice=proname)
        get_object_delete(proname)


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("对象基本属性/状态/未启用'未启用'状态的对象无法创建对象实例。")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31265(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("对象基本属性/状态/启用创建对象时可选择'未启用'及'启用'状态；")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31266(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("对象基本属性/状态/启用'启用'状态的对象可创建对象实例；")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31267(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("对象基本属性/状态/禁用'禁用'状态的对象无法创建对象实例；")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31268(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("对象基本属性/是否管控版本对象上增加属性【是否管控版本】")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31269(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("对象基本属性/是否管控版本默认不勾选，勾选，则在对象实例数据上管控版本")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31270(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("对象基本属性/是否管控版本不勾选，则在对象实例数据上不管控版本")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31271(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("属性及约束/新增属性右键展开新增按钮，点击新增新增成功")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31272(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        objectname= f'测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_all(proname)
        test.system_management_object_righ(proname,'新建',objectname)
        test.get_url_system_management_object()
        test.system_management_object_all(objectname,proname)
        ass = Assert_result_system_management(drivers)
        ass.element_not_found("对象_点击对象名称",result=True, choice=objectname)
        get_object_delete(proname)


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("属性及约束/新增属性点击对象右侧旁边的新增按钮新增成功")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31273(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        objectname= f'测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_all(proname)
        test.system_management_object_functionkeys('新建',proname,'确定',objectname)
        test.get_url_system_management_object()
        test.system_management_object_all(objectname,proname)
        ass = Assert_result_system_management(drivers)
        ass.element_not_found("对象_点击对象名称",result=True, choice=objectname)
        get_object_delete(proname)


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("属性及约束/编辑属性基础属性和继承属性都可自定义修改配置")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31274(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        objectname= f'测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_righ(proname, '检出')
        test.system_management_object_functionkeys("新增")
        test.system_management_object_newattribute("类型","基础组件",'文本')
        test.system_management_object_newattribute("属性名","testname")
        test.system_management_object_newattribute("字段释义","测试名称")
        test.system_management_object_functionkeys_confirm_cancel('确认',"新增属性")
        ass = Assert_result_system_management(drivers)
        ass.element_not_found("对象_属性及约束表单_表单值获取",result=True, choice="测试名称")
        get_object_delete(proname)


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("属性及约束/编辑属性/innername编辑属性的innername权限只有系统管理员才可编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31275(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("生命周期若生命周期未自定义，显示父类的生命周期，可以在本对象中进行自定义，点击自定义，生命周期的表单才可编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31276(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("权限默认继承父类对象，继承的对象不能进行编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31277(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("权限未检出状态可以新增权限")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31278(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        objectname= f'测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_configuration('权限')
        test.system_management_object_functionkeys('新增权限')
        test.system_management_object_permissions_formediting('角色')
        test.system_management_object_selectpermissionrole('物料变更','查询')
        test.system_management_object_selectpermissionrole('物料变更',confirm_or_cancel='确定')
        test.system_management_object_permissions_formediting('保存',1)
        test.get_url_system_management_object()
        test.system_management_object_all(proname)
        test.system_management_object_configuration('权限')
        ass = Assert_result_system_management(drivers)
        ass.element_not_found("span",result=True, choice="物料变更")
        get_object_delete(proname)


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("权限检出状态可以新增权限")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31279(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        objectname= f'测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_righ(proname, '检出')
        test.system_management_object_configuration('权限')
        test.system_management_object_functionkeys('新增权限')
        test.system_management_object_permissions_formediting('角色')
        test.system_management_object_selectpermissionrole('物料变更','查询')
        test.system_management_object_selectpermissionrole('物料变更',confirm_or_cancel='确定')
        test.system_management_object_permissions_formediting('保存',1)
        test.get_url_system_management_object()
        test.system_management_object_all(proname)
        test.system_management_object_configuration('权限')
        ass = Assert_result_system_management(drivers)
        ass.element_not_found("span",result=True, choice="物料变更")
        get_object_delete(proname)


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("权限/操作/保存继承的权限‘保存’操作默认置灰，不能编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31280(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        objectname = f'测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_righ(proname, '检出')
        test.system_management_object_functionkeys("新增")
        test.system_management_object_newattribute("类型", "基础组件", '文本')
        test.system_management_object_newattribute("属性名", "testname")
        test.system_management_object_newattribute("字段释义", f"测试名称{now_times}")
        test.system_management_object_functionkeys_confirm_cancel('确认', "新增属性")
        test.system_management_object_functionkeys('检入')
        test.system_management_object_all(proname)
        test.system_management_object_functionkeys('新建', proname, '确定', objectname)
        test.get_url_system_management_object()
        test.system_management_object_all(objectname, proname)
        test.system_management_object_all(objectname)
        test.system_management_object_righ(objectname, '检出')
        test.system_management_object_functionkeys("新增")
        test.system_management_object_newattribute("类型", "基础组件", '文本')
        test.system_management_object_newattribute("属性名", "testnameobj")
        test.system_management_object_newattribute("字段释义", f"测试子对象{now_times}")
        test.system_management_object_functionkeys_confirm_cancel('确认', "新增属性")
        test.system_management_object_functionkeys('检入')
        ass = Assert_result_system_management(drivers)
        ass.element_not_found("对象_属性及约束表单_表单值获取", result=True, choice=f"测试名称{now_times}")
        ass.element_not_found("对象_属性及约束表单_继承属性不可删除功能键", result=True, choice="1")
        ass.element_not_found("对象_属性及约束表单_表单值获取", result=True, choice=f"测试子对象{now_times}")
        ass.element_not_found("对象_属性及约束表单_删除", result=True, choice="2")
        ass.elements_assert('#icon-no-deletion', '对象_属性及约束表单_删除', '2', 'xlink:href')
        get_object_delete(proname)


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("权限/操作/删除对新增自定义的权限可以进行删除，继承的权限没有删除操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31281(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        objectname = f'测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_righ(proname, '检出')
        test.system_management_object_functionkeys("新增")
        test.system_management_object_newattribute("类型", "基础组件", '文本')
        test.system_management_object_newattribute("属性名", "testname")
        test.system_management_object_newattribute("字段释义", f"测试名称{now_times}")
        test.system_management_object_functionkeys_confirm_cancel('确认', "新增属性")
        test.system_management_object_functionkeys('检入')
        test.system_management_object_all(proname)
        test.system_management_object_functionkeys('新建', proname, '确定', objectname)
        test.get_url_system_management_object()
        test.system_management_object_all(objectname, proname)
        test.system_management_object_all(objectname)
        ass = Assert_result_system_management(drivers)
        ass.elements_assert('#icon-inherit', '对象_属性及约束表单_删除', '1', 'xlink:href')
        get_object_delete(proname)


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("检出选择对象，鼠标右键选择检出")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31282(self, drivers):
        now_times = strftime('%Y-%m-%d%H:%M:%S')
        proname = f'IPM自动化测试对象{now_times}'
        objectname = f'测试对象{now_times}'
        test = SystemManagement(drivers)
        test.get_url_system_management_object()
        test.system_management_object_all('所有对象')
        test.system_management_object_upper_function('新建')
        test.system_management_object_newbaseclass('名称', proname)
        test.system_management_object_newbaseclass('确认')
        test.system_management_object_righ(proname, '检出')
        ass = Assert_result_system_management(drivers)
        ass.elements_assert('检入', '对象_检入检出功能键', '检入')
        test.system_management_object_functionkeys('检入')
        get_object_delete(proname)

    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("检出子对象检出编辑后，当前对象整个树上锁，同级对象不上锁")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31283(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("检出多个同级对象检出后，对应统一的父对象需显示被检出对象")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31284(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("检出对象被别人检出后，当前看到的对象是未被检入的版本")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31285(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("检出对象被别人检出后，不能删除对象，对象名称不能编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31286(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("检出只要操作检出，根节点就会锁住，在锁住的状态下，管理员只能操作当前对象，同级对象也可操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31287(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("检出检出标识上显示被检出人与检出对象")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31288(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("检入用户点击【检入】，弹出对话框，用户点击确定，升级版本，且所有的子对象同步升级版本，并解锁；")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31289(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("检入用户点击【检入】，弹出对话框，用户点击取消，保存当前对象实例数据，但当前对象实例仍为检出状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31290(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("撤销检出用户点击撤销检出，弹出对话框；点击确定，检出编辑页面被删除，锁定取消")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31291(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("暂存点击暂存，被检出对象的数据暂时保存为草稿")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31292(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("暂存从其他对象切换到被暂存的对象上时，需加载暂时保存为草稿的数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31293(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("暂存暂存为草稿的数据，点击撤销检出后，暂存对象数据恢复成被检出的状态，且草稿数据删除")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31294(self, drivers):
        pass


    @allure.story("对象管理/对象类型_对象管理界面")  # 用户故事名称
    @allure.title("暂存暂存状态，退出界面后，再次进入默认为编辑状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_31295(self, drivers):
        pass


if __name__ == '__main__':
    pass
