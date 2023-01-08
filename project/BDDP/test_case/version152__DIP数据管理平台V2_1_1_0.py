import allure
import pytest
@allure.feature("DIP数据管理平台V2_1_1_0")  # 迭代名称
class Teststory_2492:
    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("移动端报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30876(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("PC端报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型pc端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==输入访问地址==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30877(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("大屏端报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型大屏端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==输入访问地址==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30878(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("自助分析端报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型自助分析==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==输入访问地址==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30879(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无首页差异化报表外部引入类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择外部引入==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30880(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无首页差异化报表定制卡片类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择定制==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==选择私有卡片==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30881(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无首页差异化报表定制外部引入类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择定制==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30882(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无首页差异化报表定制卡片、外部引入组合类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择定制==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==选择私有卡片、输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30883(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合总部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30884(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合地区部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型地区部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30885(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型事业部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30886(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合国家类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型国家==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30887(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合地区部_事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型地区部_事业部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30888(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合总部、地区部_事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源卡片组合==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型地区部_事业部==选择卡片来源财务销售事业分析部==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30889(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入总部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择外部引入==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30890(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入地区部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择外部引入==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型地区部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30891(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择外部引入==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型事业部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30892(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入国家类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择外部引入==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型国家部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30893(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入地区部_事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择外部引入==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型地区事业部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30894(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入总部、地区部_事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择外部引入==选择报表首页差异化是==进入角色管理中心进行数据授权==选择报表类型总部、地区部==输入外部链接==选择指标财务销售事业分析部==说明销售事业公析==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30895(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制总部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型总部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30896(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制地区部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型地区部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30897(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型事业部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30898(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制国家类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型国家==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30899(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制地区部_事业部类报表新建验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择页面来源定制==选择报表首页差异化是==选择报表类型地区部_事业部==进入角色管理中心进行数据授权==来源卡片财务销售事业分析部（私有化卡片）==访问地址输入外部地址==选择指标财务销售事业分析部==说明销售事业公析")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30900(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化卡片组合类报表修改功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击编辑==修改报表名称==修改主题域==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改报表类型卡片组合==修改是否差异化是、修改报表类型国家==修改卡片来源==修改分析指标选择2项指标==修改说明18字==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30901(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化外部引入类报表修改功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击编辑==修改报表名称==修改主题域==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改报表类型外部引入==修改是否差异化是、修改报表类型国家==修改外部链接==修改分析指标选择2项指标==修改说明18字==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30902(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("有报表差异化定制类报表修改功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击编辑==修改报表名称==修改主题域==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改报表类型定制==修改是否差异化是、修改报表类型国家==修改卡片来源、外部链接==修改分析指标选择2项指标==修改说明18字==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30903(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无报表差异化卡片组合类报表修改功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击编辑==修改报表名称==修改主题域==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改报表类型卡片组合==修改是否差异化否、==修改卡片来源==修改分析指标选择2项指标==修改说明18字==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30904(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无报表差异化外部引入类报表修改功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击编辑==修改报表名称==修改主题域==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改报表类型外部引入==修改是否差异化否==修改外部链接==修改分析指标选择2项指标==修改说明18字==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30905(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("无报表差异化定制类报表修改功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击编辑==修改报表名称==修改主题域==修改需求提出人==修改业务负责人.业务组织、IT负责人==修改报表类型定制==修改是否差异化否==修改卡片来源、外部链接==修改分析指标选择2项指标==修改说明18字==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30906(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表启用功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击启用==输入申请原因==点击保存")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30907(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表查看功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击查看")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30908(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表停用功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==选择已新建成功的报表==点击停用")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30909(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表已启用的报表删除功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理选择已启用的报表==修改报表名称、应用类型移动端==输入主题域选择业务域==修改业务负责人.业务组织、IT负责人==修改页面来源卡片组合==修改报表首页差异化是==进入角色管理中心进行数据授权==修改报表类型总部==修改卡片来源财务销售事业分析部==修改指标财务销售事业分析部==修改说明销售事业公析==点击保存后再点击删除")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30910(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表类型全部选择功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击首页==选择全部")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30911(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表类型已启用选择功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击首页==选择已启用")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30912(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表类型已停用选择功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击首页==选择已停用")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30913(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("新建报表卡片来源卡片搜索功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表管理新建==选择报表名称、应用类型移动端==输入主题域选择业务域==选择业务负责人.业务组织、IT负责人==选择报表组件分享==选择是否公开公开==选择首页报表池是==搜索下钻报表财务销售经营分析、供应链库存金额")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30914(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表类型搜索功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击报表搜索框==选择报表名称、应用类型移动端==点击搜索")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30915(self, drivers):
        pass


    @allure.story("报表管理新增定制化报表和首页差异化报表属性")  # 用户故事名称
    @allure.title("报表模糊搜索功能验证")  # 用例名称
    @allure.description("登录PC端后台管理系统==点击模糊搜索框==输入模糊报表名称、应用类型移动==点击搜索")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_30916(self, drivers):
        pass


if __name__ == '__main__':
    pass
