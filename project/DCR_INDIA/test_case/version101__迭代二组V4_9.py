import allure
import pytest
@allure.feature("迭代二组V4_9")  # 迭代名称
class Teststory_1686:
    @allure.story("推送FoL的时候处理一下功能机的item")  # 用户故事名称
    @allure.title("功能机参与返利政策后端代码对功能机的机型推送的内存做处理")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8479(self, drivers):
        pass


    @allure.story("推送FoL的时候处理一下功能机的item")  # 用户故事名称
    @allure.title("推送返利给fol要兼容上传的附件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8480(self, drivers):
        pass


@allure.feature("迭代二组V4_9")  # 迭代名称
class Teststory_1138:
    @allure.story("返利预览页，增加税费填写项和计算逻辑。")  # 用户故事名称
    @allure.title("预览页面增加填写税费框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8481(self, drivers):
        pass


    @allure.story("返利预览页，增加税费填写项和计算逻辑。")  # 用户故事名称
    @allure.title("默认不选中")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8482(self, drivers):
        pass


    @allure.story("返利预览页，增加税费填写项和计算逻辑。")  # 用户故事名称
    @allure.title("点击yes，填写对应税率")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8483(self, drivers):
        pass


    @allure.story("返利预览页，增加税费填写项和计算逻辑。")  # 用户故事名称
    @allure.title("点击no，默认原有逻辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8484(self, drivers):
        pass


    @allure.story("返利预览页，增加税费填写项和计算逻辑。")  # 用户故事名称
    @allure.title("税率仅支持数字")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8485(self, drivers):
        pass


    @allure.story("返利预览页，增加税费填写项和计算逻辑。")  # 用户故事名称
    @allure.title("税率数字支持9位数，2位小数")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8486(self, drivers):
        pass


    @allure.story("返利预览页，增加税费填写项和计算逻辑。")  # 用户故事名称
    @allure.title("通用机型的结果金额，计入返利总金额里面。并且在report（4个子栏目）item表显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8487(self, drivers):
        pass


    @allure.story("返利预览页，增加税费填写项和计算逻辑。")  # 用户故事名称
    @allure.title("按品牌的通用机型，算金额")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8488(self, drivers):
        pass


    @allure.story("返利预览页，增加税费填写项和计算逻辑。")  # 用户故事名称
    @allure.title("通用机型的返利金额=本次返利总金额输入的费用率，例如=5165600元2=1033112")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8489(self, drivers):
        pass


    @allure.story("返利预览页，增加税费填写项和计算逻辑。")  # 用户故事名称
    @allure.title("本次返利的总发钱的机型总销售量=通用机型的总销量=18648台")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8490(self, drivers):
        pass


    @allure.story("返利预览页，增加税费填写项和计算逻辑。")  # 用户故事名称
    @allure.title("通用机型翻台返利金额=1033112元/18648台=55.45元")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8491(self, drivers):
        pass


    @allure.story("返利预览页，增加税费填写项和计算逻辑。")  # 用户故事名称
    @allure.title("报表数据一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8492(self, drivers):
        pass


@allure.feature("迭代二组V4_9")  # 迭代名称
class Teststory_1142:
    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("1、配置项角色菜单增加返利政策手工执行操作按钮，")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8528(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("11、配置手工操作按钮后勾选政策点击可以触发推送返利政策数据到FOL")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8529(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("12、未勾选按钮时点击推送按钮系统给出对应的提示数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8530(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("13、未配置该角色的权限按钮不可查看及操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8531(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("14、已推送的数据再次点击推送时给出对应的提示信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8532(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("15、推送消息或推送FOL成功后都不允许禁用和删除系统提示Therebatepolicyhasbeenimplementedtocompletionandisnotallowedtobedisabledordeleted.")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8533(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("16、推送失败的单据都可执行操作和删除按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8691(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("17、数据未推送之前禁用后不可执行推送操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8692(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("18、删除的数据页面不在显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8693(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("19、禁用/启用后对应的状态生成显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8694(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("110、禁用后再次启用的政策执行单可正常进行推送操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8695(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("111、操作按钮对应的提示信息正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8696(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("2、Web端，返利政策所有的按钮增加到Moreoption内，页面只留copy和导出")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8697(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("3、返利增加人工执行按钮ManualExecution")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8802(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("31、在配置项角色菜单当中增加ManualExecution按钮权限")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8803(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("32、ManualExecution按钮受角色菜单权限控制")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8804(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("321、未选择数据时点击ManualExecution按钮系统给出对应的提示信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8805(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("322、ManualExecution只针对一条数据进行推送")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8806(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("323、当选择多条数据点击ManualExecution按钮时系统给出对应的提示信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8807(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("324、选择一条数据点击ManualExecution按钮时推送返回对应的数据执行状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8808(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("325、点击ManualExecution按钮时实时执行该操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8809(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("4、执行状态中增加Failed状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8810(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("41、DCR的返利执行状态ExecutionStatus增加Failed状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8811(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("411、ExecutionStatus选择Failed状态时能筛选到对应的查询状态的数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8812(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("421、ApproveStatus选择对应的状态时能筛选到对应的查询状态的数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8814(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("431、SettleStatus选择对应状态时能筛选到对应的查询状态的数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8816(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("44、三个状态的筛选条件存在对应的筛选值能筛选出有对应状态的数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8817(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("441、当三个状态的筛选条件无数据时返回为空")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8818(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("5、原功能回归组合条件筛选查询时可查询出对应的数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8819(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("6、列表增加推送字段PolicyPushFOLornot")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8820(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("61、PolicyPushFOLornot状态显示推送成功=Successful、未推送=NO、推送失败=Failed")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8821(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("62、PolicyPushFOLornot字段无筛选条件")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8822(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("63、PolicyPushFOLornot导出同列表一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8823(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("66、已成功推送的返利政策再次点击推送时系统提示TherebatepolicyhasbeenpushedtoFOL.")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8824(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("67、推送失败的返利政策可再次点击推送按钮操作推送")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8825(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("68、推送失败的返利政策可执行再此编辑价格")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8826(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("610、推送第二次成功确认后的状态不可再次编辑")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8828(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("611、PolicyPushFOLornot列表的状态只针对第一次的状态显示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8829(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("612、第一次的推送无论成功与否PolicyPushFOLornot的状态都是未推送状态")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8830(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("613、第一次推送失败的状态PolicyPushFOLornot的状态为推送失败")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8831(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("614、第一次推送成功PolicyPushFOLornot的状态为推送成功")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8832(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("7、条件大于小于符号都加上等于符号")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8883(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("71、条件对应的符号校验")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8884(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("8、二次重选机型页面左侧的搜索由原来的精准搜索变成可批量黏贴搜索")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8885(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("81、批量黏贴可搜索出对应的数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8886(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("82、精确搜索可搜索出对应的数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8887(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("9、右侧已选择的机型增加搜索选择框")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8888(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("91、右侧搜索可精准搜索可批量黏贴搜索")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8889(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("93、搜索出的数据与搜索框一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8890(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("10、增加按钮PushFOLRebatePolicy")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8891(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("101、PushFOLRebatePolicy按钮受权限控制")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8892(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("1012、PushFOLRebatePolicy在角色菜单中配置按钮")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8893(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("1011、在推送第一次FOL后对应的推送状态产生")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8894(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("102、推送第一次fol失败时不可执行第二次的按钮推送")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8895(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("103、推送第一次按钮成功的状态下才可执行第二次的推送")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8896(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("104、推送第二次按钮推送状态成功后不可在执行操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8897(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("105、第二次推送失败时可执行任意操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8898(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("106、第一次推送政策成功后不可执行任何操作")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8899(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("1、判断逻辑已推送FOL政策状态点击edit提示PushedFOL,cannotedit.")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9774(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("2、判断逻辑已推送FOL金额状态点击edit提示PushedFOL,cannotedit.")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9775(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("3、判断逻辑导入的数据点击edit提示Importedrebatedatacannotbeedited")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9776(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("4、判断逻辑已推送的FOL政策的返利再次点击PushFOLRebatePolicy提示Pushed，cannotduplicatepush.")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9777(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("5、判断逻辑已推送的FOL金额的返利再次点击PushFOLRebatePolicy提示Pushed，cannotduplicatepush.")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9778(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("7、判断逻辑导入的数据点击PushPushFOLRebatePolicy提示ImportedrebatedatacannotbepushedFOLsystem")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9779(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("7、判断逻辑导入的数据点击PushPushFOLRebateAmount提示ImportedrebatedatacannotbepushedFOLsystem")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9780(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("8、判断逻辑已推送的FOL金额的返利再次点击PushPushFOLRebateAmount提示Pushed，cannotduplicatepush.")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9781(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("9、判断逻辑已推送的FOL政策点击ManualExecution按钮提示AlreadypushedFOLsystemandcannotbeexecutedmanually")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9782(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("10、判断逻辑已推送的FOL金额点击ManualExecution按钮提示AlreadypushedFOLsystemandcannotbeexecutedmanually")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9783(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("11、判断逻辑导入的数据点击ManualExecution按钮提示Importedrebatedatacannotbeexecutedmanually")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9784(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("12、判断逻辑已推送的FOL政策点击Disable按钮提示AlreadypushedFOLsystemandcannotdisable")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9785(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("13、判断逻辑已推送的FOL金额点击Disable按钮提示AlreadypushedFOLsystemandcannotbedisable")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9786(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("14、判断逻辑已推送的FOL政策点击Delete按钮提示AlreadypushedFOLsystemandcannotdisable")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9787(self, drivers):
        pass


    @allure.story("返利Web端按钮优化后端配合")  # 用户故事名称
    @allure.title("15、判断逻辑已推送的FOL金额点击Disable按钮提示AlreadypushedFOLsystemandcannotbedisable")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9788(self, drivers):
        pass


@allure.feature("迭代二组V4_9")  # 迭代名称
class Teststory_1711:
    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("代理员工只能所属代理品牌授权的国包数据（登录账号仅支持国包代理员工）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8540(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("传音员工根据客户授权品牌查看授权国包的数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8541(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("ASM角色为AreaSalesManager的人员授权国包品牌（传音员工）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8542(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("菜单权限控制Region、ASM、Customer、Model四个维度的页签展示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8543(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("日期默认显示当前月份")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8544(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("支持跨日、月、年筛选不做任何限制")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8545(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("TotalPurchase取Purchase的指标数据的汇总（指标数据会通过点击标签实时变化）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8546(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("TotalActivated取Activated的指标数据的汇总（指标数据会通过点击标签实时变化）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8547(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("TotalSales取Sales的指标数据的汇总（指标数据会通过点击标签实时变化）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8548(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("TotalSalesupload取Salesupload的指标数据的汇总（指标数据会通过点击标签实时变化）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8549(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("销售区域取web端PST报表根据PrimaryBuyerID匹配客户管理中的SAPid确定客户编码和名字")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8550(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("销售区域显示区域路径根据当前登录人授权的国包客户所属父级往上的区域显示（目前仅支持销售区域是印度）下面区域显示该区域的子区域，区域路径可以点击")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8551(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("Purchase取web端PST报表根据PrimaryCreateDate统计一段时间内国包的数量汇总")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8552(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("Sales取web端PST报表根据DeliveryDate统计一段时间内国包的数量汇总")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8553(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("Activated取web端PST报表根据TertiaryActivationDate统计一段时间内国包的数量")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8554(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("Salesupload取web端PST报表根据SalesCreateDate统计一段时间内国包的数量")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8555(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("品牌筛选默认选择全部，仅支持授权品牌展示（切换品牌对应数据会实时变化）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8556(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("点击下面销售区域的子区域则下面销售区域展示对应当前点击的子区域下的子区域数据会实时变化")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8557(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("点击各个标签数据会实时变化")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8558(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("点击ASM跳转到新页面客户维度查看显示AMS授权的国包客户数据（点击切换销售区域，显示对应销售区域下的AMS授权的国包客户数据）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8559(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("点击Custiomer页面按照国包客户展示数据点击某个国包页面跳转到新页面机型机型维度查看（市场名内存）（点击切换销售区域，显示对应销售区域下的AMS授权的国包客户数据）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8560(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("点击机型维度，则按照机型维度展示对应数据市场名内存（点击切换销售区域，显示对应销售区域下的AMS授权的国包客户数据）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8561(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("分页处理每页展示10条数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8562(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("选择对应的筛选条件可以查出对应的数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8563(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("点击重置筛选条件清空")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8564(self, drivers):
        pass


    @allure.story("新增印度APP端PST报表")  # 用户故事名称
    @allure.title("数据校验与web端数据一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8565(self, drivers):
        pass


@allure.feature("迭代二组V4_9")  # 迭代名称
class Teststory_1145:
    @allure.story("优化返利导入的预览和下载")  # 用户故事名称
    @allure.title("1、导入的字段与预览页显示的字段一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8900(self, drivers):
        pass


    @allure.story("优化返利导入的预览和下载")  # 用户故事名称
    @allure.title("2、预览页面的字段与PDF字段一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8901(self, drivers):
        pass


    @allure.story("优化返利导入的预览和下载")  # 用户故事名称
    @allure.title("3、预览页面数据与导入的数据的数量一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8902(self, drivers):
        pass


    @allure.story("优化返利导入的预览和下载")  # 用户故事名称
    @allure.title("4、数量大的情况下增加滚动条拖动预览页面的数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8903(self, drivers):
        pass


    @allure.story("优化返利导入的预览和下载")  # 用户故事名称
    @allure.title("5、导入的数据在对应的导入记录表生成对应的数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8904(self, drivers):
        pass


    @allure.story("优化返利导入的预览和下载")  # 用户故事名称
    @allure.title("6、PDF下载的数据在对应的下载记录表生成对应的数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8905(self, drivers):
        pass


    @allure.story("优化返利导入的预览和下载")  # 用户故事名称
    @allure.title("7、其余正常新增/编辑/CP预览页保持原功能一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8906(self, drivers):
        pass


@allure.feature("迭代二组V4_9")  # 迭代名称
class Teststory_1143:
    @allure.story("返利report和item，需要增加异步导出，在ExportRecord能看到数据。")  # 用户故事名称
    @allure.title("1、Item表原导出功能改为异步导出")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8907(self, drivers):
        pass


    @allure.story("返利report和item，需要增加异步导出，在ExportRecord能看到数据。")  # 用户故事名称
    @allure.title("11、item表的user维度的导出为异步导出")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8908(self, drivers):
        pass


    @allure.story("返利report和item，需要增加异步导出，在ExportRecord能看到数据。")  # 用户故事名称
    @allure.title("111、item表的user维度的导出的数据与页面筛选查询条件列表字段一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8909(self, drivers):
        pass


    @allure.story("返利report和item，需要增加异步导出，在ExportRecord能看到数据。")  # 用户故事名称
    @allure.title("112、item表的user维度的导出成功在对应的下载记录表中产生对应的导出数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8910(self, drivers):
        pass


    @allure.story("返利report和item，需要增加异步导出，在ExportRecord能看到数据。")  # 用户故事名称
    @allure.title("12、item表的customer维度的导出为异步导出")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8911(self, drivers):
        pass


    @allure.story("返利report和item，需要增加异步导出，在ExportRecord能看到数据。")  # 用户故事名称
    @allure.title("121、item表的customer维度的导出的数据与页面筛选查询条件列表字段一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8912(self, drivers):
        pass


    @allure.story("返利report和item，需要增加异步导出，在ExportRecord能看到数据。")  # 用户故事名称
    @allure.title("122、item表的customer维度的导出成功在对应的下载记录表中产生对应的导出数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8913(self, drivers):
        pass


    @allure.story("返利report和item，需要增加异步导出，在ExportRecord能看到数据。")  # 用户故事名称
    @allure.title("13、item表的shopr维度的导出为异步导出")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8914(self, drivers):
        pass


    @allure.story("返利report和item，需要增加异步导出，在ExportRecord能看到数据。")  # 用户故事名称
    @allure.title("131、item表的shop维度的导出的数据与页面筛选查询条件列表字段一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8915(self, drivers):
        pass


    @allure.story("返利report和item，需要增加异步导出，在ExportRecord能看到数据。")  # 用户故事名称
    @allure.title("132、item表的shop维度的导出成功在对应的下载记录表中产生对应的导出数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8916(self, drivers):
        pass


    @allure.story("返利report和item，需要增加异步导出，在ExportRecord能看到数据。")  # 用户故事名称
    @allure.title("2、Report表原导出功能改为异步导出")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8917(self, drivers):
        pass


    @allure.story("返利report和item，需要增加异步导出，在ExportRecord能看到数据。")  # 用户故事名称
    @allure.title("21、导出的数据与页面筛选查询条件列表字段一致")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8918(self, drivers):
        pass


    @allure.story("返利report和item，需要增加异步导出，在ExportRecord能看到数据。")  # 用户故事名称
    @allure.title("22、导出成功/失败在对应的下载记录表中产生对应的导出数据信息")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8919(self, drivers):
        pass


@allure.feature("迭代二组V4_9")  # 迭代名称
class Teststory_1687:
    @allure.story("返利执行单，MD客户类型返利，推送FOL，增加拆分新逻辑")  # 用户故事名称
    @allure.title("此场景仅针对客户维度的二代采购")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9208(self, drivers):
        pass


    @allure.story("返利执行单，MD客户类型返利，推送FOL，增加拆分新逻辑")  # 用户故事名称
    @allure.title("二代客户的返利通过对应的上游国包商拿货量拆分返利金额和机型数据推送给fol")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9209(self, drivers):
        pass


    @allure.story("返利执行单，MD客户类型返利，推送FOL，增加拆分新逻辑")  # 用户故事名称
    @allure.title("二代对应的国包商的拿货量取CustomerSalesReport表的buyer=本次返利的目标二代ID，取ActualSales字段数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9210(self, drivers):
        pass


    @allure.story("返利执行单，MD客户类型返利，推送FOL，增加拆分新逻辑")  # 用户故事名称
    @allure.title("国包商的返利额通过计算单台返利额拿货量")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9211(self, drivers):
        pass


    @allure.story("返利执行单，MD客户类型返利，推送FOL，增加拆分新逻辑")  # 用户故事名称
    @allure.title("MD对应多个国包商推送成功，FOL会回传多个执行单号，需要记录多个单号")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9212(self, drivers):
        pass


    @allure.story("返利执行单，MD客户类型返利，推送FOL，增加拆分新逻辑")  # 用户故事名称
    @allure.title("多个执行单发放任意一笔执行单或者是全部执行单的返利额回传到dcr的状态均是Pushed")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9213(self, drivers):
        pass


    @allure.story("返利执行单，MD客户类型返利，推送FOL，增加拆分新逻辑")  # 用户故事名称
    @allure.title("推送FOL，拆分的执行支付单，需要备注国包编号，FOL的业务说明字段，返利备注（原需求）国包编号（本次需求）")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9214(self, drivers):
        pass


@allure.feature("迭代二组V4_9")  # 迭代名称
class Teststory_1695:
    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("1.App端的UploadSales中的CustomerName/Phone/Email更改为ConsumerName/Phone/Email顾客姓名/手机/邮箱")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9665(self, drivers):
        pass


    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("11、顾客对应多语言同步修改，对照需求")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9666(self, drivers):
        pass


    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("12、Web端的ShopSalesQuery中，CustomerName/CustomerPhone/CustomerEmail中的Customer相关文字也一并更改")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9667(self, drivers):
        pass


    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("13、导入/导出文件相关字段也一并更改")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9668(self, drivers):
        pass


    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("2、门店销量表单增加中高低端，价位字段")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9669(self, drivers):
        pass


    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("21、去除Country/City筛选项")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9670(self, drivers):
        pass


    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("22、新增中高端机型，价位字段")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9671(self, drivers):
        pass


    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("23、中高端机型（MidHigh）列表和导出文件都增加；加在Model之后")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9672(self, drivers):
        pass


    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("23、建议零售商售价（SuggestedRP）列表和导出文件都增加；加在BookingActivityId之后")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9673(self, drivers):
        pass


    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("3、MidHigh取值逻辑判断上报国家Country字段在ModelEdit页面的Plan中是否有配置")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9674(self, drivers):
        pass


    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("31、ModelEdit页面的Plan中有配置，取对应的Plan中ModelType的值若ModelType中的值为空，则取值为空")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9675(self, drivers):
        pass


    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("32、ModelEdit页面的Plan中没有配置，取Default中的值")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9676(self, drivers):
        pass


    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("4、SuggestedRP取值逻辑取对应的Plan中SuggestedRP的值若SuggestedRP中的值为空，则取值为空")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9677(self, drivers):
        pass


    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("33、Plan中有配置为HighEnds、MidEnds，MidHigh显示为Yes，配置为其他则为No，为配置则为空")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9919(self, drivers):
        pass


    @allure.story("【Web/APP】销量上报客户名称翻译修正和增加中高端机,价格字段")  # 用户故事名称
    @allure.title("新增筛选项MidHigh位置在Model后面，下拉单选。默认不选")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_9946(self, drivers):
        pass


@allure.feature("迭代二组V4_9")  # 迭代名称
class Teststory_1696:
    @allure.story("ShopInventoryIMEIQuery查询接口优化")  # 用户故事名称
    @allure.title("ShopInventoryIMEIQuery页面查询获取字段正常")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10231(self, drivers):
        pass


    @allure.story("ShopInventoryIMEIQuery查询接口优化")  # 用户故事名称
    @allure.title("ShopInventoryIMEIQuery筛选项功能正常，筛选结果准确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10232(self, drivers):
        pass


    @allure.story("ShopInventoryIMEIQuery查询接口优化")  # 用户故事名称
    @allure.title("ShopInventoryIMEIQuery导出功能正常，导出数据正确")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10233(self, drivers):
        pass


    @allure.story("ShopInventoryIMEIQuery查询接口优化")  # 用户故事名称
    @allure.title("ShopInventoryIMEIQuery查询接口优化后性能提升5060")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_10234(self, drivers):
        pass


if __name__ == '__main__':
      pass
