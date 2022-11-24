import allure
import pytest
@allure.feature("迭代一组4_8")  # 迭代名称
class Teststory_1009:
    @allure.story("【接口优化】/api/rest/v1/authorization/employeeShop/getAuthorizingShop")  # 用户故事名称
    @allure.title("测试点_1、StaffAuthorizationUserAuthorizationShop页面的接口/api/rest/v1/authorization/employeeShop/getAuthorizingShop")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4520(self, drivers):
        pass


    @allure.story("【接口优化】/api/rest/v1/authorization/employeeShop/getAuthorizingShop")  # 用户故事名称
    @allure.title("测试点_2、现状授权门店较多的用户，该接口的查询响应会明显较慢。例如印度生产环境，查User为indiaIT的授权店铺时，接口耗时为12s。即特定用户进行单次查询，接口耗时较长。需要优化。接口优化后性能提升50~60")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4521(self, drivers):
        pass


    @allure.story("【接口优化】/api/rest/v1/authorization/employeeShop/getAuthorizingShop")  # 用户故事名称
    @allure.title("测试点_3、页面功能正常使用不受影响（Search、AddAssociation、Import、ExportFiltered、BatchCancelAssociation、EmptyAllAssociation）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_4522(self, drivers):
        pass


@allure.feature("迭代一组4_8")  # 迭代名称
class Teststory_1011:
    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试路径")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5817(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("UI界面样式和需求保持一致，页面不同分辨率展示效果查看正常")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5818(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("查询时间不超过1s这边目前不要求这个，用户反馈页面只是我们自己用")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5819(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Search按钮_1、点击【Search】按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5825(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Search按钮_2、单个筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5826(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Search按钮_3、组合筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5827(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Reset按钮、点击【Reset】按钮，重置筛选项")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5828(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Add按钮、点击【Add】按钮，弹出新增弹窗（Add），可新增不满意原因")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5829(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Delete按钮_1、点击【Delete】按钮，支持批量删除未关联规则的不满意原因")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5830(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Delete按钮_11、如果选中的都是未关联规则的不满意原因，打开二次确认弹窗，内容确定删除？。点击确定删除当前不满意原因；点击取消关闭二次确认弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5831(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Delete按钮_12、如果选中的有已关联规则的不满意原因，报错提示''/'不满意原因XX已关联规则，不能删除'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5832(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表_1、列表最左边为批量选择框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5833(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表_2、列表列宽自适应用户也可以自己手动拉，和excel表格一样操作")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5834(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表排序规则列表以模块、分类进行分组，按创建时间倒序排列")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5835(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_1、Reason（不满意原因）回显不满意原因的中文")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5836(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_11、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5837(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_2、Module（模块）不满意原因归属的模块")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5838(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_21、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5839(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_3、Classify（分类）不满意原因归属的分类")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5840(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_31、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5841(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_4、EN（英语）不满意原因的英语翻译")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5842(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_41、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5843(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_5、FR（法语）不满意原因的法语翻译")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5844(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_51、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5845(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_6、POR（葡萄牙语）不满意原因的葡萄牙翻译")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5846(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_61、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5847(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_7、ES（西班牙语）不满意原因的西班牙语翻译")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5848(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_71、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5849(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_8、THA（泰语）不满意原因的泰语翻译")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5850(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_81、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5851(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_9、Creator（创建人）不满意原因的创建人")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5852(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_91、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5853(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_10、CreateTime（创建时间）不满意原因的创建时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5854(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_101、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5855(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_11、Opration（操作栏）操作栏有两个按钮，【Edit】按钮和【Delete】按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5856(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_111、点击【Edit】按钮，弹出编辑弹窗（Edit），可编辑不满意原因")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5857(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_1111、编辑弹窗，回显不满意原因")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5858(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_1112、编辑后点击确定，根据内容更新当前规则")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5859(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_112、点击【Delete】按钮，单个删除这行不满意原因只支持删除未关联规则的不满意原因")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5860(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_1121、如果选择的是未关联规则的不满意原因，打开二次确认弹窗，内容确定删除？。点击确定删除当前不满意原因；点击取消关闭二次确认弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5861(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_1122、如果选中的是已关联规则的不满意原因，报错提示''/'不满意原因XX已关联规则，不能删除'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5862(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页1、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5863(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页2、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5864(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页3、页面右下角Total统计正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5865(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页4、页面右下角每页显示记录可设置（15，50，100），如果选择15，则每页显示1至15条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5866(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_1、Reason（不满意原因）必填（红色标识），中文内容最多8位，其他语言限制30字符长度")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5867(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_2、Translate（翻译）这边填入EN（英语）、FR（法语）、POR（葡萄牙语）、ES（西班牙语）、THA（泰语），英文必填（红色标识），其他不限制，不限制位数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5868(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_3、Classify（分类）显示业务系统已有的分类。非必选，单选，单选框内提示'PleaseSelect'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5869(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_31、点击单选框右侧的维护分类按钮【MaintainClassify】，打开维护分类弹窗（MaintainClassify）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5870(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_311、维护分类弹窗上部分是AddClassify（新增分类）栏")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5871(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_3111、未填写分类名称，添加按钮【Add】置灰")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5872(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_3112、在ClassifyName（分类名称）后面的输入框中填入分类名称后点击添加按钮【Add】，将分类与业务系统绑定并保存到中台，添加的分类会展示在下方的（已有分类）栏，添加成功提示语''")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5873(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_312、维护分类弹窗下部分是ExistingClassify（已有分类）栏这一栏只有已有分类时才会展现下面的分类内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5874(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_3121、已有分类按创建时间进行排序，已添加的分类标签右上角出现删除按钮，点击删除按钮，将分类从业务系统中删除。删除成功提示语''")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5875(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_313、添加分类弹窗点击【X】按钮，关闭当前弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5876(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_314、分类翻译由机器自动翻译")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5877(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_4、【Confirm】按钮有必填项未填写时，确定按钮置灰")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5878(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_41、业务系统已存在相同的不满意原因时，提示''/'XX原因已存在'这个提示只有中文吗？")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5879(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_42、未存在以上异常，保存当前不满意原因。弹窗关闭，新增的不满意原因写入列表")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5880(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_43、不满意原因默认作用于系统所有模块")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5881(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_5、新增弹窗点击【Cancel】按钮或者【X】按钮，关闭当前弹窗，不记录本次填写的内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5882(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试路径")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5887(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("UI界面样式和需求保持一致，页面不同分辨率展示效果查看正常")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5889(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("查询时间不超过1s这边目前不要求这个，用户反馈页面只是我们自己用")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5891(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_1、InsertorNot（是否接入）下拉选择，选项内容是（Yes）、否（No）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5893(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_11、筛选InsertorNot，筛选出的数据正确查询接入状态等于选中内容的模块")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5896(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Search按钮、点击【Search】按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5898(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Reset按钮、点击【Reset】按钮，重置筛选项")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5900(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Add按钮、点击【Add】按钮，弹出新增弹窗（Add），可新增模块")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5902(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Delete按钮_1、点击【Delete】按钮，支持批量删除未关联规则的模块")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5904(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Delete按钮_11、如果选中的都是未关联规则的模块，打开二次确认弹窗，内容确定删除？。点击确定删除当前模块；点击取消关闭二次确认弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5906(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Delete按钮_12、如果选中的有已关联规则的模块，报错提示''/'模块XX已关联规则，不能删除'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5907(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表_1、列表最左边为批量选择框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5908(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表_2、列表列宽自适应用户也可以自己手动拉，和excel表格一样操作")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5909(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表排序规则按创建时间倒序排列")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5910(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_1、Key（Key）业务系统模块Key")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5911(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_11、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5912(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_2、Module（模块）业务系统模块名称")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5913(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_21、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5914(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_3、Rules（接入规则）业务系统模块接入规则")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5915(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_31、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5916(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_4、InsertorNot（是否接入）业务系统模块接入状态")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5917(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_41、若模块接入状态为已接入，页面按钮为已接入样式（按钮样式，按钮呈打开状态）。反之为未接入样式（按钮样式，按钮呈关闭状态）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5918(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_42、点击接入状态按钮，将模块的状态设置为另一个状态（接入→未接入、未接入→接入）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5919(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_43、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5920(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_5、Opration（操作栏）操作栏展示【Delete】按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5921(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_51、点击【Delete】按钮，单个删除这行模块只支持删除未关联规则的模块")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5922(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_511、如果选择的是未关联规则的模块，打开二次确认弹窗，内容确定删除？。点击确定删除当前模块；点击取消关闭二次确认弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5923(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_512、如果选中的是已关联规则的模块，报错提示''/'模块XX已关联规则，不能删除'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5924(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页1、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5925(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页2、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5926(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页3、页面右下角Total统计正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5927(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页4、页面右下角每页显示记录可设置（15，50，100），如果选择15，则每页显示1至15条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5928(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_1、Module（模块）支持中文、英文、数字输入，必填（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5929(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_2、Key（Key）支持英文、数字输入，最多输入8位，必填（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5930(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_3、InsertorNot（是否接入）下拉选择项，选项内容是、否。默认选中否，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5931(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_4、Rules（接入规则）最多输入200，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5932(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_5、【Confirm】按钮有必填项未填写时，确定按钮置灰")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5933(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_51、业务系统已存在相同的模块时，提示''/'XX模块已存在'这个提示只有中文吗？")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5934(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_52、未存在以上异常，将业务系统的模块内容保存到中台。弹窗关闭，新增的模块写入列表")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5935(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_6、新增弹窗点击【Cancel】按钮或者【X】按钮，关闭当前弹窗，不记录本次填写的内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5936(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试路径")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5951(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("UI界面样式和需求保持一致，页面不同分辨率展示效果查看正常")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5952(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("查询时间不超过1s这边目前不要求这个，用户反馈页面只是我们自己用")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5953(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_1、Module（模块）下拉多选，查询业务系统包含选中模块的规则")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5954(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_11、选项内容模块接入表状态为已接入的模块")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5955(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_12、筛选Module，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5956(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_2、Country（国家）下拉多选，模糊匹配，查询业务系统包含选中国家的规则")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5957(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_21、选项内容从系统国家表获取")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5958(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_22、筛选Country，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5959(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_3、Status（状态）下拉选择框，查询业务系统包含选中状态的规则")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5960(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_31、选项内容Pending（待开始）、Processing（进行中）、Cloesd（已结束）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5961(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_32、筛选Status，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5962(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Search按钮_1、点击Search按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5963(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Search按钮_2、单个筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5964(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Search按钮_3、组合筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5965(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Reset按钮、点击Reset按钮，重置筛选项")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5966(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Add按钮、点击【Add】按钮，弹出新增弹窗（Add），可新增用户反馈规则")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5967(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Stop按钮、点击【Stop】按钮，支持批量停止用户反馈规则")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5968(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Enable按钮、点击【Enable】按钮，支持批量启用用户反馈规则")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5969(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表_1、列表最左边为批量选择框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5970(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表_2、列表列宽自适应用户也可以自己手动拉，和excel表格一样操作")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5971(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表排序规则列表以模块分组，创建时间倒序排列")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5972(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_1、ID（规则ID）用户反馈规则ID。规则ID格式为FB年月日4位编码")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5973(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_11、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5974(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_2、Module（模块）用户反馈规则关联的模块")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5975(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_21、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5976(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_3、Country（国家）用户反馈规则关联的国家数量合计")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5977(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_31、可点击，点击后出现国家浮窗显示所关联的国家")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5978(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_32、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5979(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_4、CollectionTime（收集时间）用户反馈规则设定的收集时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5980(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_41、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5981(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_5、Status（状态）用户反馈规则状态")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5982(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_51、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5983(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_6、Creator（创建人）用户反馈规则创建人。显示为用户名称用户ID")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5984(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_61、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5985(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_7、CreateTime（创建时间）用户反馈规则创建时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5986(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_71、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5987(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_8、Opration（操作栏）操作栏根据规则的状态显示对应按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5988(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_81、Pending（待开始）【View】、【Edit】、【Enable】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5989(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_82、Processing（进行中）【View】、【Stop】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5990(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_83、Cloesd（已结束）【View】、【Enable】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5991(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_84、点击【View】按钮，打开查看弹窗，将规则内容回显并置灰，隐藏【Confirm】、【Cancel】按钮")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5992(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_841、点击【X】按钮，关闭查看弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5993(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_85、点击【Edit】按钮，打开编辑弹窗（Edit），根据规则回显内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5994(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_851、编辑后点击【Confirm】按钮，根据内容更新当前规则")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5995(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_8511、收集时间的开始时间大于当天，规则状态变更为待开始。开始时间等于当天，规则状态变更为进行中")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5996(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_852、点击【Cancel】按钮或者【X】按钮，关闭编辑弹窗，选中规则不做任何修改")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5997(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_86、点击【Enable】按钮，打开设置收集时间弹窗（SelectCollectionTime）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5998(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_861、CollectionTime（收集时间）必填（红色标识），日期具体到天。开始时间只能选择当天及以后日期，结束时间不能小于开始日期")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5999(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_862、点击【Confirm】按钮，更新选中规则的收集时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6000(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_8621、判断开始时间等于当天，规则状态为进行中，规则时间大于当天，规则状态为待开始")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6001(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_863、点击【Cancel】按钮或者【X】按钮，关闭设置收集时间弹窗，选中规则不做任何修改")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6002(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_87、点击【Stop】按钮，出现二次确认弹窗，内容''/'确定停用当前规则？'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6003(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_871、点击【Confirm】按钮，将选中规则状态变更为已结束并关闭二次确认弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6004(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_872、点击【Cancel】按钮，关闭二次确认弹窗，选中规则不做任何修改")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6005(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页1、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6006(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页2、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6007(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页3、页面右下角Total统计正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6008(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页4、页面右下角每页显示记录可设置（15，50，100），如果选择15，则每页显示1至15条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6009(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_1、CollectionTime（收集时间）必填（红色标识），日期具体到天。开始时间只能选择当天及以后日期，结束时间不能小于开始日期")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6010(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_2、EvaluationMethod（评价方式）必填（红色标识），默认选中评分制（星级），不可取消")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6011(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_3、Country（收集国家）必填（红色标识），下拉多选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6012(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_31、选项内容从系统国家表获取")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6013(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_4、Module（模块）必填（红色标识），多选。若只有一个模块，该模块为选中状态且不可取消")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6014(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_41、选项内容模块接入表状态为已接入的模块")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6015(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_42、业务系统的模块接入表没有状态为已接入的模块，弹窗页面提示''/'系统暂未接入服务'。【Confirm】按钮置灰")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6016(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_5、Reason（不满意原因）必填（红色标识），多选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6017(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_51、选项内容业务系统的不满意原因列表中添加的不满意原因。按原因序号进行排序")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6018(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_52、业务系统的不满意原因列表没有数据，弹窗页面提示''/'未设置不满意原因'。【Confirm】按钮置灰")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6019(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_6、PopupRules（弹窗规则）必填（红色标识），单选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6020(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_61、Whenusercompletestheevaluation，popupruleis（用户完成评价，弹窗）可选择不再弹出，或者编辑天弹出")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6021(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_611、编辑天弹出时天数只能输入正整数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6022(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_62、Whenuserclosed，popupruleis（用户直接关闭，弹窗）可选择不再弹出，或者编辑天弹出")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6023(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_621、编辑天弹出时天数只能输入正整数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6024(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_7、【Confirm】按钮有必填项未填写时，确定按钮置灰")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6025(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_71、判断已选国家在选中模块已生成规则，提示'XX模块已配置XX国家规则'这个提示只有中文吗？")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6026(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_72、根据选中模块与国家保存规则")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6027(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_73、判断开始时间等于当天，规则状态为进行中，规则时间大于当天，规则状态为待开始")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6028(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("新增弹窗_8、新增弹窗点击【Confirm】按钮或者【X】按钮，关闭当前弹窗，不记录本次填写的内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6029(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试路径")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6030(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("UI界面样式和需求保持一致，页面不同分辨率展示效果查看正常")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6031(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("查询时间不超过1s这边目前不要求这个，用户反馈页面只是我们自己用")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6032(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_1、Module（模块）文本输入框，支持模糊查询，查询业务系统模块字段包含输入关键字的评价内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6033(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_11、筛选Module，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6034(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_2、Country（国家）下拉多选，模糊匹配，查询业务系统国家字段包含选中内容的评价内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6035(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_21、选项内容从系统国家表获取")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6036(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_22、筛选Country，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6037(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_3、FeedbackTime（评价日期）日期选择器，查询业务系统评价时间在选中时间段范围内的评价内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6038(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("筛选项_31、筛选FeedbackTime，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6039(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Search按钮_1、点击Search按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6040(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Search按钮_2、单个筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6041(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Search按钮_3、组合筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6042(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Reset按钮、点击Reset按钮，重置筛选项")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6043(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Export按钮、点击Export按钮，导出当前筛选出的全部数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6044(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Export导出_1、导出文件名为菜单名流水号")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6045(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Export导出_2、导出的报表字段名、字段顺序、数据内容和列表一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6046(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Export导出_3、导出的报表表头需要12号字紫色，不做自适应。导出的报表字段宽度为16个字符宽度")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6047(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Export导出_4、筛选后导出的报表数据和筛选的数据保持一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6048(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Export导出_41、单个筛选，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6049(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Export导出_411、筛选Module，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6050(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Export导出_412、筛选Position，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6051(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Export导出_413、筛选Country，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6052(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Export导出_414、筛选FeedbackTime，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6053(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("Export导出_42、组合筛选，导出的报表数据内容和列表数据内容一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6054(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表_1、列表最左边为批量选择框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6055(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表_2、列表列宽自适应用户也可以自己手动拉，和excel表格一样操作")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6056(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表排序规则显示APP用户提交的反馈内容，按评价时间倒序进行显示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6057(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_1、Module（模块）用户反馈来源的模块")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6058(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_11、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6059(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_2、Evaluate（评价等级）用户评价等级")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6060(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_21、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6061(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_3、Reason（不满意原因）用户选择13星时，选择的不满意原因")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6062(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_31、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6063(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_4、Feedback（反馈意见）用户填写的反馈意见")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6064(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_41、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6065(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_5、UserID（用户编码）用户ID")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6066(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_51、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6067(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_6、UserName（用户名称）用户名称")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6068(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_61、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6069(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_7、Position（职位）用户职位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6070(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_71、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6071(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_8、Country（国家）用户资料的国家")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6072(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_81、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6073(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_9、FeedbackTime（评价时间）用户提交反馈的时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6074(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("列表字段_91、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6075(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页1、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6076(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页2、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6077(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页3、页面右下角Total统计正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6078(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("翻页4、页面右下角每页显示记录可设置（15，50，100），如果选择15，则每页显示1至15条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6079(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_1、业务系统模块接入服务，需配置接口触发规则。业务系统接口后，用户反馈中台需记录已接入服务的业务系统及对应模块")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6080(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_11、APP模块在达成触发规则后，可根据规则打开弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6081(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_2、DCR用户反馈弹窗触发应用及规则")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6082(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_21、销量上报点击提交按钮，有网状态下服务器校验提交内容且全部通过")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6083(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_211、没网时转跳到其他页面提示继续上传，有网且校验成功是提示succesfully。只有在提示succesfully的时候才打开弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6084(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_22、库存上报点击提交按钮，有网状态下服务器校验提交内容且全部通过")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6085(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_221、没网时转跳到其他页面提示继续上传，有网且校验成功是提示succesfully。只有在提示succesfully的时候才打开弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6086(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_23、考勤点击打卡按钮，打卡状态提示succesfully。在当前页面打开用户反馈弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6087(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_24、巡店VisitingDetails页面，点击提交按钮返回巡店首页，有网且校验成功时打开用户反馈弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6088(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_25、用户操作满足触发规则，调用服务，若接口响应时长小于3S")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6089(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_251、销量上报不显示原弹窗/toast提示，在当前页面打开用户反馈弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6090(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_252、库存上报不显示原弹窗/toast提示，在当前页面打开用户反馈弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6091(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_253、考勤在当前页面打开用户反馈弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6092(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_254、巡店返回巡店首页并打开用户反馈弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6093(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_26、用户操作满足触发规则，调用服务，若接口响应时长大于3S")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6094(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_261、销量上报按原逻辑处理，不打开用户反馈弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6095(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_262、库存上报按原逻辑处理，不打开用户反馈弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6096(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_263、考勤按原逻辑处理，不打开用户反馈弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6097(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("测试点_264、巡店按原逻辑处理，不打开用户反馈弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6098(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_1、点击弹窗外的区域，不关闭弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6099(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_2、弹窗上方提示'Yourcommentswillmakeusdobetter'/'您的评价将使我们做得更好。'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6100(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_3、评分为5颗星，默认都未点亮。此时【Submit】按钮置灰不可点击")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6101(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_4、如果用户点亮的是45星，不显示不满意原因及反馈意见")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6102(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_41、此时【Submit】按钮是可点击的，点击后调用接口保存用户反馈")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6103(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_5、如果用户点亮的是13星，显示不满意原因及反馈意见")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6104(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_51、如果业务系统未配置不满意原因，则隐藏不满意原因栏目，只显示反馈意见栏目")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6105(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_52、未选择原因且未填写意见反馈时，【Submit】按钮置灰不可点击")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6106(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_53、用户已选择不满意原因或已填写反馈意见，【Submit】按钮可点击")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6107(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_531、点击【Submit】按钮，调用接口保存用户反馈")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6108(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_6、'Yourfeedback'/'您的反馈意见'下方先展示分类选择，分类比较多的时候可左右划动进行选择")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6109(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_61、判断当前模块关联的所有不满意原因所属分类")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6110(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_611、均为空时，不显示分类页签")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6111(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_612、均为相同分类时，不显示分类页签")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6112(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_613、存在分类为空的不满意原因时，前端显示'Other'/'其他'页签，将分类为空的不满意原因统一归纳到'Other'tab页签")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6113(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_7、分类下方展示对应的不满意原因，根据业务系统调用对应的不满意原因")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6114(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_71、切换分类时不满意原因相应变化")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6115(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_8、不满意原因下方显示输入框，输入框内默认提示'Pleasewritedownyourvaluablecomments...'/'请写下您的宝贵意见。。。'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6116(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_81、格式不做限制，最大长度300个字符，超过不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6117(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_9、假设用户选中了分类一下面的三个不满意原因后又选中了分类二下面的三个不满意原因，这时候点击【Submit】按钮，会将这6个不满意原因都一起保存")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6118(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_10、点击【X】按钮，关闭当前弹窗，不记录本次填写的内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6119(self, drivers):
        pass


    @allure.story("用户反馈前后端联调")  # 用户故事名称
    @allure.title("用户反馈弹窗_11、用户关闭弹窗或进行评价后需记录用户操作，并结合规则判断用户再次满足触发规则时，是否再次打开弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_6120(self, drivers):
        pass


@allure.feature("迭代一组4_8")  # 迭代名称
class Teststory_825:
    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB测试点_1、印度环境新增页面UserManagementIndia")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7127(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB测试点_11、UserManagementIndia是在全球版页面UserManagement的基础上新增计划注册信息。新增字段都排序在原来UserManagement页面字段的后面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7128(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB测试点_2、Web端根据角色可配置（RoleDefinitionPermissionSetting）在原来的按钮权限（Table、Add、Edit、Import、Export、Enable、ResetPassword、Quit、SensitivefieldQuery）上新增1个按钮权限Approve")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7129(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB测试点_3、新增字段的加密字段权限配置在SensitivefieldQuery里面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7130(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB测试点_4、权限控制同全球版页面UserManagement的权限控制")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7131(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB筛选项新增_1、筛选项新增AuditStatus（审核状态），放在最后面。下拉单选，可选择All，Pending，True，Untrue，。默认选中All")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7132(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB筛选项新增_11、代表审核状态为空，查询所有审核状态为空的数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7133(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB筛选项新增_12、筛选AuditStatus，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7134(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB筛选项新增_2、筛选项新增SchemeRegistration（计划注册），放在AuditStatus后面。下拉单选，可选择All，Yes，No。默认选中All")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7135(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB筛选项新增_21、筛选SchemeRegistration，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7136(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB按钮新增_1、新增审核按钮【Approve】，位置放在哪里？")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7137(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB按钮新增_2、选择一条或多条记录后，点击审核按钮，打开审核弹窗，提示'Confirmtheselectedemployeeinformationiscorrect?'。根据审核结果，改变用户审核状态")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7138(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB按钮新增_21、如果选择Untrue，状态为【待审核】的用户审核状态会变更为【不通过】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7139(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB按钮新增_211、选择Untrue，状态为【已通过】/【空】的用户审核状态不会发生变更")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7140(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB按钮新增_22、如果选择True，状态为【待审核】的用户审核状态变更为【已审核】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7141(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB按钮新增_221、选择True，状态为【已通过】/【空】的用户审核状态不会发生变更")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7142(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_0、列表新增字段都排序在原来UserManagement字段的后面。新增字段为加密字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7143(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_01、若用户没有加密字段权限，字段显示为加密内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7144(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_02、若用户有加密字段权限，字段内容正常显示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7145(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_1、字段1AuditStatus（审核状态）用户的审核状态。为Pending/True/Untrue/")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7146(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_11、审核状态不影响用户对系统的使用")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7147(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_12、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7148(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_2、字段2SchemeRegistration（计划注册）用户选择的计划注册状态，Yes/No")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7149(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_21、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7150(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_3、字段3PayTMRegisteredNumber（PayTM注册号码）用户在PersonalDetail部分填写的PayTM注册号码")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7151(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_31、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7152(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_4、字段4WhatsAppNumber（WhatsApp号码）用户在PersonalDetail部分填写的WhatsApp号码")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7153(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_41、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7154(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_5、字段5PANNumber（PAN号码）用户在PersonalDetail部分填写的PAN号码")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7155(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_51、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7156(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_6、字段6AadhaarNumber（Aadhaar号码）用户在PersonalDetail部分填写的Aadhaar号码")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7157(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_61、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7158(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_7、字段7CopyofPANcardattachment（PAN卡附件复印件）用户在PersonalDetail部分添加的PAN卡附件复印件。点击可查看图片附件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7159(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_71、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7160(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_8、字段8CopyofAadhaarcardattachment（Aadhaar卡附件复印件）用户在PersonalDetail部分添加的Aadhaar卡附件复印件。点击可查看图片附件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7161(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_81、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7162(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_9、字段9UPIID（UPIID）用户在BankDetail部分填写的UPIID")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7163(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_91、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7164(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_10、字段10BankName（银行名称）用户在BankDetail部分填写的银行名称")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7165(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_101、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7166(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_11、字段11AccountHolderName（账户持有人姓名）用户在BankDetail部分填写的账户持有人姓名")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7167(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_111、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7168(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_12、字段12AccountNumber（账户）用户在BankDetail部分填写的账户")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7169(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_121、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7170(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_13、字段13BranchName（分支机构名称）用户在BankDetail部分填写的分支机构名称")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7171(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_131、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7172(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_14、字段14IFSCCode（IFSC代码）用户在BankDetail部分填写的IFSC代码")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7173(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_141、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7174(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_15、字段15CopyofBankPassbook/CancelChequeAttachment（银行存折副本/取消支票附件）用户在BankDetail部分填写的。点击可查看图片附件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7175(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB列表新增字段_151、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7176(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_0、点击Export导出员工数据时，新增字段都排序在原来UserManagement导出字段的后面。新增字段为加密字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7179(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_01、若用户没有加密字段权限，导出时字段显示为加密内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7180(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_02、若用户有加密字段权限，导出时字段内容正常显示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7181(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_1、字段1AuditStatus（审核状态）用户的审核状态。为Pending/True/Untrue/")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7182(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_11、审核状态不影响用户对系统的使用")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7183(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_12、核对导出值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7184(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_2、字段2SchemeRegistration（计划注册）用户选择的计划注册状态，Yes/No")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7185(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_21、核对导出值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7186(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_3、字段3PayTMRegisteredNumber（PayTM注册号码）用户在PersonalDetail部分填写的PayTM注册号码")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7187(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_31、核对导出值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7188(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_4、字段4WhatsAppNumber（WhatsApp号码）用户在PersonalDetail部分填写的WhatsApp号码")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7189(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_41、核对导出值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7190(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_5、字段5PANNumber（PAN号码）用户在PersonalDetail部分填写的PAN号码")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7191(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_51、核对导出值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7192(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_6、字段6AadhaarNumber（Aadhaar号码）用户在PersonalDetail部分填写的Aadhaar号码")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7193(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_61、核对导出值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7194(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_7、字段7UPIID（UPIID）用户在BankDetail部分填写的UPIID")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7195(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_71、核对导出值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7196(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_8、字段8BankName（银行名称）用户在BankDetail部分填写的银行名称")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7197(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_81、核对导出值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7198(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_9、字段9AccountHolderName（账户持有人姓名）用户在BankDetail部分填写的账户持有人姓名")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7199(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_91、核对导出值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7200(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_10、字段10AccountNumber（账户）用户在BankDetail部分填写的账户")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7201(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_101、核对导出值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7202(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_11、字段11BranchName（分支机构名称）用户在BankDetail部分填写的分支机构名称")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7203(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_111、核对导出值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7204(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_12、字段12IFSCCode（IFSC代码）用户在BankDetail部分填写的IFSC代码")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7205(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB导出新增字段_121、核对导出值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7206(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_0、点击Add创建员工时，在PersonalInformation下方新增SchemeRegistration块内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7207(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_01、选项内容Yes，No。RadioBox单选按钮，必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7208(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_02、默认选中No，不显示PersonalDetail与BankDetail栏目下所有新增字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7209(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_021、创建员工成功后，该员工的AuditStatus（审核状态）为空")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7210(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_03、用户选择Yes后，显示PersonalDetail与BankDetail栏目下所有新增字段，提交时新增校验逻辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7211(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_031、创建员工成功后，该员工的AuditStatus（审核状态）为待审核")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7212(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_1、字段1PayTMRegisteredNumber（PayTM注册号码）文本输入框。仅支持数字输入，最大长度128字符，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7213(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_11、如果未填写，提示'PleasefillinPayTMRegisteredNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7214(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_12、如果输入非数字或小数等，提示'PayTMRegisteredNumber、WhatsAppnumber，Onlynumbersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7215(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_13、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7216(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_2、字段2WhatsAppNumber（WhatsApp号码）文本输入框。仅支持数字输入，最大长度128字符，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7217(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_21、如果未填写，提示'PleasefillinWhatsAppNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7218(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_22、如果输入非数字或小数等，提示'PayTMRegisteredNumber、WhatsAppnumber，Onlynumbersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7219(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_23、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7220(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_3、字段3PANNumber（PAN号码）文本输入框。支持数字与英文输入，最大长度128字符，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7221(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_31、如果未填写，提示'PleasefillinPANNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7222(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_32、如果输入非数字或字符等，提示'PANNumber、AadhaarNumber，Onlynumbersandcharactersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7223(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_33、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7224(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_4、字段4AadhaarNumber（Aadhaar号码）文本输入框。支持数字与英文输入，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7225(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_41、如果输入非数字或字符等，提示'PANNumber、AadhaarNumber，Onlynumbersandcharactersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7226(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_42、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7227(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_5、字段5CopyofPANcardattachment（PAN卡附件复印件）图片上传器。支持jpg/jpeg/png格式，最大支持6M，最多支持5张图片，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7228(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_51、如果未填写，提示'PleasefillinCopyofPANcardattachment'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7229(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_6、字段6CopyofAadhaarcardattachment（Aadhaar卡附件复印件）图片上传器。支持jpg/jpeg/png格式，最大支持6M，最多支持5张图片，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7230(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_PersonalDetail栏_61、如果未填写，提示'PleasefillinCopyofAadhaarcardattachment'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7231(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_BankDetail栏_1、字段1UPIID（UPIID）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7232(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_BankDetail栏_11、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7233(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_BankDetail栏_2、字段2BankName（银行名称）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7234(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_BankDetail栏_21、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7235(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_BankDetail栏_3、字段3AccountHolderName（账户持有人姓名）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7236(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_BankDetail栏_31、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7237(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_BankDetail栏_4、字段4AccountNumber（账户）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7238(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_BankDetail栏_41、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7239(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_BankDetail栏_5、字段5BranchName（分支机构名称）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7240(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_BankDetail栏_51、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7241(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_BankDetail栏_6、字段6IFSCCode（IFSC代码）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7242(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_BankDetail栏_61、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7243(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_BankDetail栏_7、字段7CopyofBankPassbook/CancelChequeAttachment（银行存折副本/取消支票附件）图片上传器。支持jpg/jpeg/png格式，最大支持6M，最多支持5张图片，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7244(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB创建员工新增字段_BankDetail栏_71、如果未填写，提示'PleasefillinCopyofBankPassbook/CancelChequeAttachment'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7245(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_0、点击Import的AddUpload批导创建员工时，新增字段都排序在原来UserManagement的批导模板的字段后面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7246(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_1、字段1SchemeRegistration（计划注册）用户选择的计划注册状态，下拉单选，可选择Yes/No，默认选中No，必填项（字段名颜色红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7247(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_11、如果选中No，批导创建员工成功后，这些员工的AuditStatus（审核状态）为空")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7248(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_12、如果选中Yes，批导创建员工成功后，这些员工的AuditStatus（审核状态）为待审核")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7249(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_2、字段2PayTMRegisteredNumber（PayTM注册号码）仅支持数字输入，最大长度128字符，必填项（字段名颜色红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7250(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_21、如果未填写，提示'PleasefillinPayTMRegisteredNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7251(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_22、如果输入非数字或小数等，提示'PayTMRegisteredNumber、WhatsAppnumber，Onlynumbersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7252(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_23、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7253(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_3、字段3WhatsAppNumber（WhatsApp号码）文本输入框。仅支持数字输入，最大长度128字符，必填项（字段名颜色红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7254(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_31、如果未填写，提示'PleasefillinWhatsAppNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7255(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_32、如果输入非数字或小数等，提示'PayTMRegisteredNumber、WhatsAppnumber，Onlynumbersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7256(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_33、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7257(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_4、字段4PANNumber（PAN号码）文本输入框。支持数字与英文输入，最大长度128字符，必填项（字段名颜色红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7258(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_41、如果未填写，提示'PleasefillinPANNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7259(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_42、如果输入非数字或字符等，提示'PANNumber、AadhaarNumber，Onlynumbersandcharactersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7260(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_43、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7261(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_5、字段5AadhaarNumber（Aadhaar号码）文本输入框。支持数字与英文输入，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7262(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_51、如果输入非数字或字符等，提示'PANNumber、AadhaarNumber，Onlynumbersandcharactersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7263(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_52、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7264(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_6、字段6UPIID（UPIID）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7265(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_61、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7266(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_7、字段7BankName（银行名称）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7267(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_71、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7268(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_8、字段8AccountHolderName（账户持有人姓名）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7269(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_81、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7270(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_9、字段9AccountNumber（账户）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7271(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_91、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7272(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_10、字段10BranchName（分支机构名称）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7273(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_101、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7274(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_11、字段11IFSCCode（IFSC代码）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7275(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导创建员工新增字段_111、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7276(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_0、点击Edit编辑员工时，在PersonalInformation下方新增SchemeRegistration块内容，并回显之前填入的用户数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7278(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_1、用户根据权限，判断加密字段显示内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7279(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_11、若用户没有加密字段权限，回显时显示为加密内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7280(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_12、若用户有加密字段权限，回显时字段内容正常显示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7281(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_2、选项内容Yes，No。RadioBox单选按钮，必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7282(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_21、如果选中No，不显示PersonalDetail与BankDetail栏目下所有新增字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7283(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_22、如果选择Yes，显示PersonalDetail与BankDetail栏目下所有新增字段，提交时新增校验逻辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7284(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_3、编辑完成后提交时，SchemeRegistration内容等于Yes时，新增校验逻辑。根据AuditStatus（审核状态）执行不同逻辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7285(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_31、AuditStatus（审核状态）为【已通过】时，判断PersonalDetail与BankDetail栏目下所有字段内容与原内容是否一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7286(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_311、如果与原内容不一致，提交后该员工的AuditStatus（审核状态）从【已通过】变更为【待审核】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7287(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_312、如果与原内容一致，提交后该员工的AuditStatus（审核状态）维持不变，仍为【已通过】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7288(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_32、AuditStatus（审核状态）为【待审核】时，提交后该员工的AuditStatus（审核状态）维持不变，仍为【待审核】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7289(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_33、AuditStatus（审核状态）为【不通过】时，提交后该员工的AuditStatus（审核状态）从【不通过】变更为【待审核】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7290(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_4、编辑完成后提交时，SchemeRegistration内容等于No时，审核状态变更为空。不清空原来的PersonalDetail与BankDetail字段内容（原来的内容在后台保存）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7291(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_1、字段1PayTMRegisteredNumber（PayTM注册号码）文本输入框。仅支持数字输入，最大长度128字符，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7292(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_11、如果未填写，提示'PleasefillinPayTMRegisteredNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7293(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_12、如果输入非数字或小数等，提示'PayTMRegisteredNumber、WhatsAppnumber，Onlynumbersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7294(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_13、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7295(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_2、字段2WhatsAppNumber（WhatsApp号码）文本输入框。仅支持数字输入，最大长度128字符，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7296(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_21、如果未填写，提示'PleasefillinWhatsAppNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7297(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_22、如果输入非数字或小数等，提示'PayTMRegisteredNumber、WhatsAppnumber，Onlynumbersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7298(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_23、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7299(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_3、字段3PANNumber（PAN号码）文本输入框。支持数字与英文输入，最大长度128字符，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7300(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_31、如果未填写，提示'PleasefillinPANNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7301(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_32、如果输入非数字或字符等，提示'PANNumber、AadhaarNumber，Onlynumbersandcharactersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7302(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_33、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7303(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_4、字段4AadhaarNumber（Aadhaar号码）文本输入框。支持数字与英文输入，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7304(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_41、如果输入非数字或字符等，提示'PANNumber、AadhaarNumber，Onlynumbersandcharactersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7305(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_42、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7306(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_5、字段5CopyofPANcardattachment（PAN卡附件复印件）图片上传器。支持jpg/jpeg/png格式，最大支持6M，最多支持5张图片，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7307(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_51、如果未填写，提示'PleasefillinCopyofPANcardattachment'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7308(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_6、字段6CopyofAadhaarcardattachment（Aadhaar卡附件复印件）图片上传器。支持jpg/jpeg/png格式，最大支持6M，最多支持5张图片，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7309(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_PersonalDetail栏_61、如果未填写，提示'PleasefillinCopyofAadhaarcardattachment'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7310(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_BankDetail栏_1、字段1UPIID（UPIID）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7311(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_BankDetail栏_11、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7312(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_BankDetail栏_2、字段2BankName（银行名称）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7313(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_BankDetail栏_21、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7314(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_BankDetail栏_3、字段3AccountHolderName（账户持有人姓名）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7315(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_BankDetail栏_31、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7316(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_BankDetail栏_4、字段4AccountNumber（账户）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7317(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_BankDetail栏_41、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7318(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_BankDetail栏_5、字段5BranchName（分支机构名称）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7319(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_BankDetail栏_51、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7320(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_BankDetail栏_6、字段6IFSCCode（IFSC代码）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7321(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_BankDetail栏_61、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7322(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_BankDetail栏_7、字段7CopyofBankPassbook/CancelChequeAttachment（银行存折副本/取消支票附件）图片上传器。支持jpg/jpeg/png格式，最大支持6M，最多支持5张图片，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7323(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB编辑员工新增字段_BankDetail栏_71、如果未填写，提示'PleasefillinCopyofBankPassbook/CancelChequeAttachment'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7324(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_0、点击Import的EditUpload批导编辑员工时，执行web端编辑提交逻辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7325(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_1、编辑完成后提交时，SchemeRegistration内容等于Yes时，新增校验逻辑。根据AuditStatus（审核状态）执行不同逻辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7326(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_11、AuditStatus（审核状态）为【已通过】时，判断PersonalDetail与BankDetail栏目下所有字段内容与原内容是否一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7327(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_111、如果与原内容不一致，提交后该员工的AuditStatus（审核状态）从【已通过】变更为【待审核】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7328(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_112、如果与原内容一致，提交后该员工的AuditStatus（审核状态）维持不变，仍为【已通过】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7329(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_12、AuditStatus（审核状态）为【待审核】时，提交后该员工的AuditStatus（审核状态）维持不变，仍为【待审核】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7330(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_13、AuditStatus（审核状态）为【不通过】时，提交后该员工的AuditStatus（审核状态）从【不通过】变更为【待审核】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7331(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_2、编辑完成后提交时，SchemeRegistration内容等于No时，审核状态变更为空。不清空原来的PersonalDetail与BankDetail字段内容（原来的内容在后台保存）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7332(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_1、字段1PayTMRegisteredNumber（PayTM注册号码）仅支持数字输入，最大长度128字符，必填项（字段名颜色红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7333(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_11、如果未填写，提示'PleasefillinPayTMRegisteredNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7334(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_12、如果输入非数字或小数等，提示'PayTMRegisteredNumber、WhatsAppnumber，Onlynumbersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7335(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_13、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7336(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_2、字段2WhatsAppNumber（WhatsApp号码）文本输入框。仅支持数字输入，最大长度128字符，必填项（字段名颜色红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7337(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_21、如果未填写，提示'PleasefillinWhatsAppNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7338(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_22、如果输入非数字或小数等，提示'PayTMRegisteredNumber、WhatsAppnumber，Onlynumbersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7339(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_23、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7340(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_3、字段3PANNumber（PAN号码）文本输入框。支持数字与英文输入，最大长度128字符，必填项（字段名颜色红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7341(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_31、如果未填写，提示'PleasefillinPANNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7343(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_32、如果输入非数字或字符等，提示'PANNumber、AadhaarNumber，Onlynumbersandcharactersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7344(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_33、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7345(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_4、字段4AadhaarNumber（Aadhaar号码）文本输入框。支持数字与英文输入，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7346(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_41、如果输入非数字或字符等，提示'PANNumber、AadhaarNumber，Onlynumbersandcharactersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7347(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_42、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7348(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_5、字段5UPIID（UPIID）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7349(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_51、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7350(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_6、字段6BankName（银行名称）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7351(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_61、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7352(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_7、字段7AccountHolderName（账户持有人姓名）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7353(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_71、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7354(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_8、字段8AccountNumber（账户）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7355(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_81、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7356(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_9、字段9BranchName（分支机构名称）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7357(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_91、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7358(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_10、字段10IFSCCode（IFSC代码）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7359(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("WEB批导编辑员工提交逻辑_字段校验_101、超过长度提示'Themaximumfieldlengthis128'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7360(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP测试点_1、APP端根据角色可配置（RoleDefinitionPermissionSetting）新增2个按钮权限计划注册权限和加密字段权限这个权限菜单放在哪里？")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7361(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP测试点_11、如果用户未配置APP的计划注册权限，在APP的个人中心部分的Personalinformation部分，不显示SchemeRegistration、PersonalDetail与BankDetail栏目下所有新增字段及提交按钮【Submit】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7362(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP测试点_12、如果用户配置了APP的计划注册权限，在APP的个人中心部分的Personalinformation部分新增SchemeRegistration块内容，展示在下面，并回显之前填入的用户数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7363(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_1、用户根据权限，判断加密字段显示内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7364(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_11、若用户没有加密字段权限，回显时显示为加密内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7365(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_12、若用户有加密字段权限，回显时字段内容正常显示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7366(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_2、选项内容Yes，No。RadioBox单选按钮，必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7367(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_21、如果选中No，不显示PersonalDetail与BankDetail栏目下所有新增字段")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7368(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_22、如果选择Yes，显示PersonalDetail与BankDetail栏目下所有新增字段，提交时新增校验逻辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7369(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_3、编辑完成后提交时，SchemeRegistration内容等于Yes时，新增校验逻辑。根据AuditStatus（审核状态）执行不同逻辑")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7370(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_31、AuditStatus（审核状态）为【已通过】时，判断PersonalDetail与BankDetail栏目下所有字段内容与原内容是否一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7371(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_311、如果与原内容不一致，提交后该员工的AuditStatus（审核状态）从【已通过】变更为【待审核】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7372(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_312、如果与原内容一致，提交后该员工的AuditStatus（审核状态）维持不变，仍为【已通过】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7373(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_32、AuditStatus（审核状态）为【待审核】时，提交后该员工的AuditStatus（审核状态）维持不变，仍为【待审核】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7374(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_33、AuditStatus（审核状态）为【不通过】时，提交后该员工的AuditStatus（审核状态）从【不通过】变更为【待审核】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7375(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_4、编辑完成后提交时，SchemeRegistration内容等于No时，审核状态变更为空。不清空原来的PersonalDetail与BankDetail字段内容（原来的内容在后台保存）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7376(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_5、未提交页面内容返回上一页，再进入当前页面，不记录上次操作信息")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7377(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_6、提交按钮【Submit】为悬浮按钮，悬浮在最下面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7378(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_1、字段1PayTMRegisteredNumber（PayTM注册号码）文本输入框。仅支持数字输入，最大长度128字符，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7379(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_11、如果未填写，提示'PleasefillinPayTMRegisteredNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7380(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_12、如果输入非数字或小数等，提示'PayTMRegisteredNumber、WhatsAppnumber，Onlynumbersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7381(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_13、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7382(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_2、字段2WhatsAppNumber（WhatsApp号码）文本输入框。仅支持数字输入，最大长度128字符，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7383(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_21、如果未填写，提示'PleasefillinWhatsAppNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7384(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_22、如果输入非数字或小数等，提示'PayTMRegisteredNumber、WhatsAppnumber，Onlynumbersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7385(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_23、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7386(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_3、字段3PANNumber（PAN号码）文本输入框。支持数字与英文输入，最大长度128字符，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7387(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_31、如果未填写，提示'PleasefillinPANNumber'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7388(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_32、如果输入非数字或字符等，提示'PANNumber、AadhaarNumber，Onlynumbersandcharactersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7389(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_33、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7390(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_4、字段4AadhaarNumber（Aadhaar号码）文本输入框。支持数字与英文输入，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7391(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_41、如果输入非数字或字符等，提示'PANNumber、AadhaarNumber，Onlynumbersandcharactersaresupported'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7392(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_42、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7393(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_5、字段5CopyofPANcardattachment（PAN卡附件复印件）图片上传器。支持jpg/jpeg/png格式，最大支持6M，最多支持5张图片，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7394(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_51、如果未填写，提示'PleasefillinCopyofPANcardattachment'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7395(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_6、字段6CopyofAadhaarcardattachment（Aadhaar卡附件复印件）图片上传器。支持jpg/jpeg/png格式，最大支持6M，最多支持5张图片，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7396(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_PersonalDetail栏_61、如果未填写，提示'PleasefillinCopyofAadhaarcardattachment'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7397(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_BankDetail栏_1、字段1UPIID（UPIID）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7398(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_BankDetail栏_11、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7399(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_BankDetail栏_2、字段2BankName（银行名称）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7400(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_BankDetail栏_21、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7401(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_BankDetail栏_3、字段3AccountHolderName（账户持有人姓名）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7402(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_BankDetail栏_31、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7403(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_BankDetail栏_4、字段4AccountNumber（账户）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7404(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_BankDetail栏_41、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7405(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_BankDetail栏_5、字段5BranchName（分支机构名称）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7406(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_BankDetail栏_51、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7407(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_BankDetail栏_6、字段6IFSCCode（IFSC代码）文本输入框。格式不限制，最大长度128字符，非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7408(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_BankDetail栏_61、超过长度的输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7409(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_BankDetail栏_7、字段7CopyofBankPassbook/CancelChequeAttachment（银行存折副本/取消支票附件）图片上传器。支持jpg/jpeg/png格式，最大支持6M，最多支持5张图片，必填项（红色标识）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7410(self, drivers):
        pass


    @allure.story("印度员工信息新增计划注册")  # 用户故事名称
    @allure.title("APP个人中心新增字段_BankDetail栏_71、如果未填写，提示'PleasefillinCopyofBankPassbook/CancelChequeAttachment'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7411(self, drivers):
        pass


@allure.feature("迭代一组4_8")  # 迭代名称
class Teststory_827:
    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("测试路径RebateAchievementStaffAchievement")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7959(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_1、新增打开自定义计算规则列表按钮（按钮名称【】），在页面呈收起状态。点击【More】按钮弹出")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7960(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_11、【More】按钮中包括打开自定义计算规则列表按钮【】和删除目标按钮【Delete】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7961(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_12、【More】按钮前面按钮从左到右依次为【EditTarget】、【Import】、【Export】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7962(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_13、Web端根据角色可配置（RoleDefinitionPermissionSetting）ShopAchievement菜单下新增【】按钮权限")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7963(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_14、Web端根据角色可配置（RoleDefinitionPermissionSetting）ShopAchievement菜单下新增''/'自定义计算规则列表'页面权限")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7964(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_141、''/'自定义计算规则列表'页面下配置按钮权限【Table】、【Add】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7965(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_2、员工达成新增逻辑根据员工ID，判断员工是否有关联的自定义计算规则")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7966(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_21、如果有关联的自定义计算规则，根据执行语句，计算员工达成数据")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7967(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_211、职位类型等于'渠道'时")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7968(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_2111、ValidSales、MidHighActivated、KeyModelActivated没有数据且不可点击")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7969(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_2112、TotalSales、MidHighSales、KeyModelSales字段的数据从ShopPurchaseQuery取数，并且点击后转跳至ShopPurchaseQuery")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7970(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_2113、跳转的ShopPurchaseQuery页面查询条件有InboundDate/Brand/Shop/Status/Model/Item")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7971(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_21131、【InboundDate】写入自定义计算规则的时间范围TotalSales、MidHighSales、KeyModelSales字段的跳转都会写入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7972(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_211311、自定义计算规则时间范围的结束时间大于当前系统时间，则入库日期查询条件的结束时间等于当前系统时间（举例说明假设自定义计算规则时间范围是126号，今天是20220916，查询条件那边写入20220901~20220916）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7973(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_21132、【Brand】点击达成记录的品牌TotalSales、MidHighSales、KeyModelSales字段的跳转都会写入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7974(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_21133、【Shop】员工关联的所有与点击达成记录品牌一致的门店TotalSales、MidHighSales、KeyModelSales字段的跳转都会写入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7975(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_21134、【Status】查询状态为Committed的记录TotalSales、MidHighSales、KeyModelSales字段的跳转都会写入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7976(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_21135、【Model】品牌关联的中高端机型仅MidHighSales字段的跳转才会写入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7977(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_21136、【Item】品牌关联的重点机型仅KeyModelSales字段的跳转才会写入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7978(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_212、职位类型等于'零售'时，TotalSales、ValidSales、MidHighSales、MidHighActivated、KeyModelSales、KeyModelActivated的计算逻辑和字段跳转与原有逻辑一致（按照原来的从ShopSalesQuery取数，跳转也跳转到ShopSalesQuery页面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7979(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_22、如果没有关联的自定义计算规则，TotalSales、ValidSales、MidHighSales、MidHighActivated、KeyModelSales、KeyModelActivated的计算逻辑和字段跳转与原有逻辑一致（按照原来的从ShopSalesQuery取数，跳转也跳转到ShopSalesQuery页面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7980(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("优化点_221、功能回归正常")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7981(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("点击添加规则按钮【】，进入自定义计算规则列表页面（另外打开的新页面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7982(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("筛选项_1、Position（职位）下拉多选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7983(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("筛选项_11、选项内容系统中所有职位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7984(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("筛选项_12、筛选Position，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7985(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("Search按钮、点击【Search】按钮，根据筛选项查询，列表展示筛选结果")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7986(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("Reset按钮、点击【Reset】按钮，重置筛选项")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7987(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("Add按钮、点击【Add】按钮，打开添加规则弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7988(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表1、列表最左边为批量选择框")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7989(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表2、列表列宽自适应用户也可以自己手动拉，和excel表格一样操作")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7990(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表排序规则创建时间倒序排列")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7991(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_1、Position（职位）自定义计算规则选择的职位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7992(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_11、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7993(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_2、PositionType（职位类型）自定义计算规则选择的职位类型")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7994(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_21、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7995(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_3、TimeRange（时间范围）自定义计算规则选择的时间范围。格式开始日期结束日期")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7996(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_31、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7997(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_4、ReleaseRange（发布范围）自定义计算规则选择的发布范围。以品牌为维度，格式品牌国家、国家")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7998(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_41、例InfinixMorocco,Indonesia")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_7999(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_42、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8000(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_5、Remark（备注）自定义计算规则的备注")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8001(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_51、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8002(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_6、Updater（更新人）自定义计算规则的更新人")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8003(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_61、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8004(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_7、UpdateDate（更新时间）自定义计算规则的更新时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8005(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_71、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8006(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_8、Creator（创建人）自定义计算规则的创建人")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8007(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_81、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8008(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_9、CreateDate（创建时间）自定义计算规则的创建时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8009(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_91、核对列表值为正确（与后台一致）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8010(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_10、Operation（操作栏）操作栏有两个按钮，【Edit】和【Delete】")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8011(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_101、点击【Edit】按钮，弹出编辑规则弹窗，可编辑规则")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8012(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_1011、编辑弹窗，回显选中规则内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8013(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_1012、编辑保存逻辑与新增保存一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8014(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_1013、需记录操作日志")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8015(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_102、点击【Delete】按钮，单个删除这行规则")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8016(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_1021、打开二次确认弹窗，内容确定删除？。点击确定删除当前自定义计算规则；点击取消关闭二次确认弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8017(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("列表字段_1022、需记录操作日志")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8018(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("翻页1、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8019(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("翻页2、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8020(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("翻页3、页面右下角totalrecords统计正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8021(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("翻页4、页面右下角每页显示记录可设置（15，50，100），如果选择15，则每页显示1至15条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8022(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("【Cancel】按钮、点击【Cancel】按钮即关闭当前页面回到StaffAchievement页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8023(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_1、Position（职位）必填（红色标识），下拉单选，默认为空？")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8024(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_11、选项内容系统中所有职位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8025(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_2、PositionType（职位类型）必填（红色标识），下拉单选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8026(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_21、选项内容渠道、零售。这边是默认选中哪个选项呢？还是默认为空呢？")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8027(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_3、SQL（执行语句）必填（红色标识），sql语句，需要做关键字屏蔽，如delete、insert等")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8028(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_31、如果填入的SQL语句错误，报错提示什么？")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8029(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_4、TimeRange（时间范围）必填（红色标识），日期选择器")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8030(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_41、选项内容131，交互逻辑参考DCR门店销量查询销量日期查询条件")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8031(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_5、ReleaseRange（发布范围）必填（红色标识），品牌和国家都多选，和功能配置那边交互一样")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8032(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_51、列出系统所有品牌，在品牌维度下列出所有国家")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8033(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_6、Remark（备注）非必填，最多支持100个字符输入，超过输入框不让输入")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8034(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_7、【Save】按钮有必填项未填写时，保存按钮置灰")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8035(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_71、有必填项未填写时，点击【Save】按钮后必填项下方提示'Thisfieldisrequired'/'此字段必填'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8036(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_72、所选职位在已选发布范围内，打开Tips提示弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8037(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_721、固定提示语（灰色字体显示）'当前职位已在下列品牌国家配置规则'/'Thecurrentpositionhasbeenconfiguredinthefollowingbrandcountries'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8038(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_722、以品牌为维度列出冲突的国家（红色字体显示）。例如InfinixAngola这边品牌和国家换行展示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8039(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_723、点击【OK】按钮或者【X】按钮，关闭Tips提示弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8040(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_73、无以上异常，保存自定义计算规则并关闭添加规则弹窗。数据展示在列表")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8041(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_8、添加规则弹窗点击【Confirm】按钮或者【X】按钮，关闭添加规则弹窗，不记录本次填写的内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8042(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("测试路径APP人员达成维度")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8043(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("测试点_1、这边要考虑如果有关联的自定义计算规则且职位类型等于'渠道'时，APP这边数据的展示是否受影响")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8044(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("测试点_2、人员达成维度功能回归正常")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8045(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_32、输入框下方显示按钮【】/【使用已有SQL】，点击弹出''/'选择SQL'弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8055(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_321、Position（职位）之前新增过的规则的职位")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8056(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_322、SQL之前新增过的规则的职位所对应的SQL")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8057(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_323、单元格行高根据字段内容自适应")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8058(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_324、选项内容规则执行语句表中所有sql语句。单选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8059(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_325、未选择记录，确定按钮【Confirm】置灰")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8060(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_326、选择任一记录点击确定后，将选中sql回写至执行语句输入框并关闭当前弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8061(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_327、选择SQL弹窗点击取消按钮【Cancel】或者【X】按钮，关闭选择SQL弹窗，不记录本次选择的内容")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8062(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_328、页面右下角操作翻页功能正常")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8063(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_3281、页面右下角Goto''输入页数后操作Enter键，页面跳转到所输入的页数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8064(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_3282、页面右下角totalrecords统计正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8065(self, drivers):
        pass


    @allure.story("渠道员工达成")  # 用户故事名称
    @allure.title("添加规则弹窗_3283、页面右下角每页显示记录可设置（15，50，100），如果选择15，则每页显示1至15条记录，左边提示'total'，展示总记录条数")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8066(self, drivers):
        pass


@allure.feature("迭代一组4_8")  # 迭代名称
class Teststory_1282:
    @allure.story("APP查看隐私协议新增填写工号判断")  # 用户故事名称
    @allure.title("1、点击隐私协议时，判断是否输入UserID")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8791(self, drivers):
        pass


    @allure.story("APP查看隐私协议新增填写工号判断")  # 用户故事名称
    @allure.title("11、未输入toast提示请先输入工号")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8792(self, drivers):
        pass


    @allure.story("APP查看隐私协议新增填写工号判断")  # 用户故事名称
    @allure.title("12、输入正确的工号根据选择站点跳转隐私协议详情页，显示对应的隐私协议")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8793(self, drivers):
        pass


    @allure.story("APP查看隐私协议新增填写工号判断")  # 用户故事名称
    @allure.title("121、选择香港站点，跳转全球版隐私协议详情页")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8794(self, drivers):
        pass


    @allure.story("APP查看隐私协议新增填写工号判断")  # 用户故事名称
    @allure.title("122、选择印度站点，跳转印度版隐私协议详情页（目前法文未提供印度版协议）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8795(self, drivers):
        pass


    @allure.story("APP查看隐私协议新增填写工号判断")  # 用户故事名称
    @allure.title("13、输入错误的功能，不能查看隐私协议，提示未获取到用户路由信息（401），请联系您的上级")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8796(self, drivers):
        pass


    @allure.story("APP查看隐私协议新增填写工号判断")  # 用户故事名称
    @allure.title("2、用户首次使用DCRAPP时，不再打开DCRAPP隐私条款弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8797(self, drivers):
        pass


    @allure.story("APP查看隐私协议新增填写工号判断")  # 用户故事名称
    @allure.title("3、使用相机、访问相册、获取定位等需用户授权的手机功能，授权弹窗不在用户首次打开APP时弹出，用户使用过程中用到需授权的手机功能时，再打开授权弹窗")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8798(self, drivers):
        pass


    @allure.story("APP查看隐私协议新增填写工号判断")  # 用户故事名称
    @allure.title("4、用户登录成功后，生成隐私协议日志记录用户授权行为，日志规则与现有逻辑一致（用户登录一次记录一次，勾选了隐私协议则认为是同意）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_8799(self, drivers):
        pass


if __name__ == '__main__':
      pass
