import allure
import pytest
@allure.feature("2022年末需求计划")  # 迭代名称
class Teststory_2760:
    @allure.story(""高级搜索优化"")  # 用户故事名称
    @allure.title("自动化测试跑流程")  # 用例名称
    @allure.description("登录==创建项目")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_18778(self, drivers):
        pass


    @allure.story(""高级搜索优化"")  # 用户故事名称
    @allure.title("IPM流程测试")  # 用例名称
    @allure.description("发起==流程审批==断言")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_19625(self, drivers):
        pass


@allure.feature("2022年末需求计划")  # 迭代名称
class Teststory_2966:
    @allure.story("1.5.3视图amp描述输入条件，更改数据后条件丢失了")  # 用户故事名称
    @allure.title('视图配置条件查询用户输入搜索条件，选中之一数据做编辑，编辑完成后，要保存搜索条件，除非用户重置或者清空')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20854(self, drivers):
        pass


    @allure.story("1.5.3视图amp描述输入条件，更改数据后条件丢失了")  # 用户故事名称
    @allure.title('编码规则条件查询用户输入搜索条件，选中之一数据做编辑，编辑完成后，要保存搜索条件，除非用户重置或者清空')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20855(self, drivers):
        pass


    @allure.story("1.5.3视图amp描述输入条件，更改数据后条件丢失了")  # 用户故事名称
    @allure.title('对象管理/对象数用户输入搜索条件，选中之一数据做编辑，编辑完成后，对象数层级维持更改过后的现状，不做任何刷新处理')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20856(self, drivers):
        pass


@allure.feature("2022年末需求计划")  # 迭代名称
class Teststory_2965:
    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('路径选择需要编辑的类型，选择需要一键设置的属性，点击后面的'一键设置'按钮未作更改')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20857(self, drivers):
        pass


    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('视图批量设置功能属性批量编辑页面增加了【事件方法】【显示名】【编码规则】的设置')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20858(self, drivers):
        pass


    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('批量编辑/事件方法批量勾选所需编辑的视图，点击批量编辑按钮，弹出批量编辑弹框，在视图属性中选中事件方法后，属性值按照事件方法联动选择值，点击确定，选中的所有视图批量更新事件方法，在查询结果栏页面中显示当前视图属性绑定的所有事件方法')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20859(self, drivers):
        pass


    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('批量编辑/事件方法批量选中编辑的视图中已有事件方法在视图属性中选中事件方法后，属性值默认显示第一条视图数据的【事件配置】数据，在当前页面进行事件方法的新增及编辑')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20860(self, drivers):
        pass


    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('批量编辑/事件方法当前勾选的视图中，默认获取第一个视图的事件方法，第一个视图与其他视图的事件方法数量不一致时，默认按照第一个视图设置批量刷新')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20861(self, drivers):
        pass


    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('批量编辑/显示名批量勾选所需编辑的视图，点击批量编辑按钮，弹出批量编辑弹框，在视图属性中选中显示名后，属性值按输入对应的显示名后，点击确定，选中的所有视图批量更新显示名，在查询结果栏页面中显示当前视图属性设置的显示名')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20862(self, drivers):
        pass


    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('批量编辑/编码规则批量勾选所需编辑的视图，点击批量编辑按钮，弹出批量编辑弹框，在视图属性中选中编码规则后，属性值输入对应的编码规则后，点击确定，选中的所有视图批量更新编码规则，在查询结果栏页面中显示当前视图属性设置的编码规则')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20863(self, drivers):
        pass


    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('视图批量设置/编辑单个编辑不增加【事件方法】【显示名】【编码规则】的设置')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20864(self, drivers):
        pass


    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('视图批量设置查询增加【显示名】【编码规则】的查询条件')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20865(self, drivers):
        pass


    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('显示名/查询模糊匹配查询，输入显示名部分字段，在结果栏展示字段相关的所有显示名的数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20866(self, drivers):
        pass


    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('显示名/查询准确输入显示名，在结果栏展示显示名的字段数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20867(self, drivers):
        pass


    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('编码规则/查询模糊匹配查询，输入编码规则部分数据，在结果栏展示字段相关的所有编码规则的数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20868(self, drivers):
        pass


    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('编码规则/查询准确输入编码规则，在结果栏展示编码规则的字段数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20869(self, drivers):
        pass


    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('视图批量设置结果栏增加【事件方法】【显示名】【编码规则】的数据在结果栏中显示')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20870(self, drivers):
        pass


    @allure.story("1.5.3对象中属性一键设置功能增加事件方法")  # 用户故事名称
    @allure.title('视图批量设置结果栏【事件方法】显示当前视图属性绑定的所有事件方法')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20871(self, drivers):
        pass


@allure.feature("2022年末需求计划")  # 迭代名称
class Teststory_2961:
    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('新增对象选中根节点，点击新增子对象操作在菜单上直接点击悬浮的''标识，树型菜单中增加一个节点')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20872(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('新增子对象选中对象，点击''标识，树型菜单中选中的对象增加一个子节点')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20873(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('删除对象若对象未启用，且无子对象或子对象全部未启用，可删除选中的对象及其子对象，提示'请确定删除选定的对象及子对象'；否者不显示删除按钮')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20874(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('删除对象选中的对象无子对象且未启用，点击'删除'标识，可删除选中的对象')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20875(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('删除对象选中的对象或子对象有启用或禁用的状态，点击'删除'标识，不能删除，并提示')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20876(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('搜索支持模糊查询对象名称')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20877(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('上移同一个父对象节点下，同一层级，可上移')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20878(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('上移不同父节点下，不可上移')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20879(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('上移不同层级，不可上移')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20880(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('下移同一个父对象节点下，同一层级，可下移位置')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20881(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('下移不同父节点下，不可下移')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20882(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('下移不同层级，不可下移')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20883(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('展开')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20884(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('针对父对象下的子对象进行展开')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20885(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('收缩')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20886(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('针对父对象下的子对象进行收缩')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20887(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('进入对象管理页面，系统初始加载了所有基类的对象（基类对象提前定义），可对基类对象进行检出编辑')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20888(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('对象基本属性/对象图标可更换图标')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20889(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('对象基本属性/对象编码50char，新增自动生成；不可编辑')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20890(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('对象基本属性/对象名称50char，可编辑')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20891(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('对象基本属性/父对象显示父对象的值不可编辑，根据父对象的名称实时变化')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20892(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('对象基本属性/状态/未启用创建对象时可选择'未启用'及'启用'状态，一旦对象设置为'启用'或'禁用'状态，'未启用'状态不显示')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20893(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('对象基本属性/状态/未启用'未启用'状态的对象可删除，若存在'启用'或'禁用'的子对象，不可删除；')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20894(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('对象基本属性/状态/未启用'未启用'状态的对象无法创建对象实例。')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20895(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('对象基本属性/状态/启用创建对象时可选择'未启用'及'启用'状态；')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20896(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('对象基本属性/状态/启用'启用'状态的对象可创建对象实例；')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20897(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('对象基本属性/状态/禁用'禁用'状态的对象无法创建对象实例；')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20898(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('对象基本属性/是否管控版本对象上增加属性【是否管控版本】')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20899(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('对象基本属性/是否管控版本默认不勾选，勾选，则在对象实例数据上管控版本')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20900(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('对象基本属性/是否管控版本不勾选，则在对象实例数据上不管控版本')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20901(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('属性及约束/新增属性新增属性没有变化，按照之前的逻辑')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20902(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('属性及约束/编辑属性基础属性和继承属性都可自定义修改配置')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20903(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('属性及约束/编辑属性/innername编辑属性的innername权限只有系统管理员才可编辑')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20904(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('生命周期若生命周期未自定义，显示父类的生命周期，可以在本对象中进行自定义，点击自定义，生命周期的表单才可编辑')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20905(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('权限默认继承父类对象，继承的对象不能进行编辑')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20906(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('权限检出状态才能新增')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20907(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('权限/操作/保存继承的权限‘保存’操作默认置灰，不能编辑')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20908(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('权限/操作/删除对新增自定义的权限可以进行删除，继承的权限没有删除操作')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20909(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('检出选择对象，鼠标右键选择检出')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20910(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('检出子对象检出编辑后，当前对象整个树上锁，同级对象不上锁')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20911(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('检出多个同级对象检出后，对应统一的父对象需显示被检出对象')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20912(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('检出对象被别人检出后，当前看到的对象是未被检入的版本')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20913(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('检出对象被别人检出后，不能删除对象，对象名称不能编辑')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20914(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('检出只要操作检出，根节点就会锁住，在锁住的状态下，管理员只能操作一个节点，节点操作检入后才能操作其他节点')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20915(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('检出检出标识上显示被检出人与检出对象')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20916(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('检入用户点击【检入】，弹出对话框，用户点击确定，升级版本，且所有的子对象同步升级版本，并解锁；')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20917(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('检入用户点击【检入】，弹出对话框，用户点击取消，保存当前对象实例数据，但当前对象实例仍为检出状态')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20918(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('撤销检出用户点击撤销检出，弹出对话框；点击确定，检出编辑页面被删除，锁定取消')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20919(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('暂存点击暂存，被检出对象的数据暂时保存为草稿')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20920(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('暂存从其他对象切换到被暂存的对象上时，需加载暂时保存为草稿的数据')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20921(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('暂存暂存为草稿的数据，点击撤销检出后，暂存对象数据恢复成被检出的状态，且草稿数据删除')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20922(self, drivers):
        pass


    @allure.story("1.5.3对象类型改造点")  # 用户故事名称
    @allure.title('暂存暂存状态，退出界面后，再次进入默认为编辑状态')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_20923(self, drivers):
        pass


@allure.feature("2022年末需求计划")  # 迭代名称
class Teststory_2963:
    @allure.story("1.5.3数据组节点英文导入")  # 用户故事名称
    @allure.title('物料申请，主数据审核节点进入我的待办，点开任务任务详情页中增加导入的按钮，所有包含主数据审核节点的物料类型申请流程均要查看')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23288(self, drivers):
        pass


    @allure.story("1.5.3数据组节点英文导入")  # 用户故事名称
    @allure.title('点击导入，弹出导入的页面，可以下载模板')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23289(self, drivers):
        pass


    @allure.story("1.5.3数据组节点英文导入")  # 用户故事名称
    @allure.title('点击下载模板，导入模板包含对象类型、物料名称、物料描述CN、物料描述EN、物料长描述、物料长描述EN、工厂、颜色、颜色EN')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('blocker')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23290(self, drivers):
        pass


    @allure.story("1.5.3数据组节点英文导入")  # 用户故事名称
    @allure.title('导出的模板清单在一个sheet页中显示页面上所有的物料实例，属性包含【对象类型】【物料名称】【物料描述CN】【物料描述EN】【物料长描述】【物料长描述EN】【颜色】【颜色EN】，仅有【颜色EN】可以进行编辑')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23291(self, drivers):
        pass


    @allure.story("1.5.3数据组节点英文导入")  # 用户故事名称
    @allure.title('对【【对象类型】【物料名称】【物料描述CN】【物料描述EN】【物料长描述】【物料长描述EN】【颜色】】字段尝试进行修改，修改失败，无法编辑')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23292(self, drivers):
        pass


    @allure.story("1.5.3数据组节点英文导入")  # 用户故事名称
    @allure.title('点击应用，系统中【颜色EN】更改，其他的联动属性同步更改，如【物料描述EN】【物料长描述EN】，物料描述和物料长描述需要修改吗，如原【颜色EN】为red，将【颜色EN】修改为blue，导入应用后，任务详情中的【颜色EN】显示【blue】，物料描述EN】【物料长描述EN】的颜色也随之更换显示为blue')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23293(self, drivers):
        pass


    @allure.story("1.5.3数据组节点英文导入")  # 用户故事名称
    @allure.title('物料描述EN绑定的是颜色但取值是颜色的key值，物料描述EN关联的颜色值不跟着联动更改')  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity('normal')  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_23294(self, drivers):
        pass


if __name__ == '__main__':
    pass
