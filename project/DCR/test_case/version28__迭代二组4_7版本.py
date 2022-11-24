import allure
import pytest
@allure.feature("迭代二组4_7版本")  # 迭代名称
class Teststory_429:
    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("APP优化点_1、列表根据授权门店做区分，如果大权限的走报表服务，利用ADB查询；如果小权限的化继续调本地接口")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_694(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_1、VisitingTemplate页面，点击列表操作栏的Edit对模板进行编辑时，Reset按钮在编辑状态下重置无效，需要改为有效（不论用户是否删除后提交了再编辑）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_695(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_2、VisitRecord页面，筛选项Position支持下拉多选")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_696(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_21、筛选Position，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_697(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_3、VisitRecord页面，巡店记录下载后，在Export和ExportDetails导出后的Excel里，加上Operation字段（位置放在SubmitTime后面）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_698(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_31、在Visittask选项卡，点击Export导出后的Excel里，点击Operation里的链接后，跳到DCRWeb端该被检查的用户的巡店记录详情页面中，可查看他的巡店图片（前提是用户已登录。若用户未登录，则需要登录，登录后再进入被检查人的巡店记录详情中）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_699(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_311、在Visittask选项卡，点击ExportDetails导出后的Excel里，点击Operation里的链接后，跳到DCRWeb端该被检查的用户的巡店记录详情页面中，可查看他的巡店图片（前提是用户已登录。若用户未登录，则需要登录，登录后再进入被检查人的巡店记录详情中）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_700(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_32、在Shopselfinspection选项卡，点击Export导出后的Excel里，点击Operation里的链接后，跳到DCRWeb端该被检查的用户的促销员自检记录详情页面中，可查看他的促销员自检图片（前提是用户已登录。若用户未登录，则需要登录，登录后再进入被检查人的促销员自检记录详情中）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_701(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_321、在Shopselfinspection选项卡，点击ExportDetails导出后的Excel里，点击Operation里的链接后，跳到DCRWeb端该被检查的用户的促销员自检记录详情页面中，可查看他的促销员自检图片（前提是用户已登录。若用户未登录，则需要登录，登录后再进入被检查人的促销员自检记录详情中）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_702(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_4、VisitRecord页面，新增ImageType的筛选项，交互和门店管理的一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_703(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_41、ImageType（门店形象等级）筛选门店形象等级（来源ShopMgt）。下拉单选，默认为空（框中提示Select）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_704(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_411、ImageType对应的数据来源于数据字典")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_705(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_412、筛选ImageType，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_706(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_5、VisitRecord页面，新增Country/City的筛选项，交互和门店管理的一致")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_707(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_51、Country/City（国家/城市）筛选国家/城市，下拉展示国家树，单选，默认为空")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_708(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_511、筛选Country/City，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_709(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_6、VisitRecord页面，列表展示新增State（省份）、City（城市）字段，位置在Country（国家）字段之后")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_710(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_61、点击Export导出新增State（省份）、City（城市）字段，位置在Country（国家）字段之后")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_711(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_62、点击ExportDetail导出新增State（省份）、City（城市）字段，位置在Country（国家）字段之后")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_712(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_63、State（省份）取门店所在省份，City（城市）取门店所在城市来源ShopMgt这个是不是实时取呀？")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_713(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_7、VisitRecord页面，UploadUser的筛选项，支持输入多个搜索（不需要模糊）")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_714(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_71、UploadUser（更新人）APP上提交巡店记录的人员ID。UserIDUserName的组合（来源UserMgt）。默认为空（框中提示All），输入框点击时提示'Batchinputcontent'")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_715(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_711、支持多条输入（即批量粘贴）支持UserID批量粘贴搜索/UserID无特殊符号的UserName的组合批量粘贴搜索现在去掉批量粘贴了")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_716(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_712、输入模糊搜索（单选）支持UserID搜索/无特殊符号的UserName的搜索")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_717(self, drivers):
        pass


    @allure.story("巡店优化2")  # 用户故事名称
    @allure.title("WEB优化点_713、筛选UploadUser，筛选出的数据正确")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_718(self, drivers):
        pass


@allure.feature("迭代二组4_7版本")  # 迭代名称
class Teststory_134:
    @allure.story("门店自检查看历史和督导检查门店自检")  # 用户故事名称
    @allure.title("1、权限配置Shopselfinspection，配置后显示的是促销员自检门店的页面")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1662(self, drivers):
        pass


@allure.feature("迭代二组4_7版本")  # 迭代名称
class Teststory_88:
    @allure.story("返利条件增加时间重选功能")  # 用户故事名称
    @allure.title("1、涉及User维度")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1725(self, drivers):
        pass


@allure.feature("迭代二组4_7版本")  # 迭代名称
class Teststory_403:
    @allure.story("巡店优化1")  # 用户故事名称
    @allure.title("1、巡店App端的ProductDisplay题，MarketName的筛选需要变更为MarketNameModel，支持模糊搜索，选择后只保存市场名")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1798(self, drivers):
        pass


    @allure.story("巡店优化1")  # 用户故事名称
    @allure.title("3、巡店模板中ShopStatus、ProductDisplay、POSMSetting下的Comments都改为默认非必填")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1801(self, drivers):
        pass


    @allure.story("巡店优化1")  # 用户故事名称
    @allure.title("4、自检和巡店APP显示的提交时间是上传人国家的本地时间")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_1803(self, drivers):
        pass


@allure.feature("迭代二组4_7版本")  # 迭代名称
class Teststory_363:
    @allure.story("APP销售出库选择买方限制展示50条")  # 用户故事名称
    @allure.title("1、APP销售出库选择买方买家限制显示，不需要分页，展示50条；")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_2853(self, drivers):
        pass


@allure.feature("迭代二组4_7版本")  # 迭代名称
class Teststory_364:
    @allure.story("APP端返利金额和返利机型数据更新逻辑")  # 用户故事名称
    @allure.title("1、我的返利页面分三部分展示整体返利数据汇总、本月及上月的返利数据对应的政策展示和历史返利数据对应的政策展示")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3340(self, drivers):
        pass


@allure.feature("迭代二组4_7版本")  # 迭代名称
class Teststory_289:
    @allure.story("TotalQuantity允许重选机型")  # 用户故事名称
    @allure.title("1、涉及customer维度的TotalQuantity、TotalAch的Rebate")  # 用例名称
    @allure.description("None")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_3970(self, drivers):
        pass


if __name__ == '__main__':
      pass
