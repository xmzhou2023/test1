import allure
import pytest
@allure.feature("MES_CSR秘钥上传google")  # 迭代名称
class Teststory_2201:
    @allure.story("MES后台创建动态表，保存TPS上传的结构化数据")  # 用户故事名称
    @allure.title("CSR未审核项目审核组装项目后，自动创建CSR数据表")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13613(self, drivers):
        pass


    @allure.story("MES后台创建动态表，保存TPS上传的结构化数据")  # 用户故事名称
    @allure.title("CSR已审核项目手动创建CSR数据表成功")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13614(self, drivers):
        pass


    @allure.story("MES后台创建动态表，保存TPS上传的结构化数据")  # 用户故事名称
    @allure.title("CSRTPS上传数据后，对应机型表正确存储各字段数据")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13615(self, drivers):
        pass


@allure.feature("MES_CSR秘钥上传google")  # 迭代名称
class Teststory_2202:
    @allure.story("获取工具上传CSRS结构化数据接口")  # 用户故事名称
    @allure.title("工具上传CSR数据MD5错误时，拦截并提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13693(self, drivers):
        pass


    @allure.story("获取工具上传CSRS结构化数据接口")  # 用户故事名称
    @allure.title("工具上传CSR数据任一字段缺失/为空时，拦截并提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13697(self, drivers):
        pass


    @allure.story("获取工具上传CSRS结构化数据接口")  # 用户故事名称
    @allure.title("工具上传CSR数据SNIMEI1chipid已存在对应表时，，拦截并提示")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13699(self, drivers):
        pass


    @allure.story("获取工具上传CSRS结构化数据接口")  # 用户故事名称
    @allure.title("工具上传CSR数据数据正确，上传成功")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13701(self, drivers):
        pass


@allure.feature("MES_CSR秘钥上传google")  # 迭代名称
class Teststory_2203:
    @allure.story("工厂库定时同步csrs结构化数据到中转库")  # 用户故事名称
    @allure.title("定时任务执行后，工厂中各机型的CSR表数据正确同步到中转库中，工厂机型CSR表中正确记录同步时间及同步标识")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_13862(self, drivers):
        pass


@allure.feature("MES_CSR秘钥上传google")  # 迭代名称
class Teststory_2204:
    @allure.story("中转库定时同步CSRS结构化数据到MES总部接口")  # 用户故事名称
    @allure.title("定时任务执行后，中转库中记录的CSR数据正确同步到总部库，中转库中正确记录同步时间及同步标识")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14235(self, drivers):
        pass


@allure.feature("MES_CSR秘钥上传google")  # 迭代名称
class Teststory_2205:
    @allure.story("增加CSRS结构化上传日志查询报表")  # 用户故事名称
    @allure.title("CSR上传日志查询查询条件检查")  # 用例名称
    @allure.description("检查查询条件")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14244(self, drivers):
        pass


    @allure.story("增加CSRS结构化上传日志查询报表")  # 用户故事名称
    @allure.title("CSR上传日志查询查询结果表单字段检查")  # 用例名称
    @allure.description("检查列表字段")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14303(self, drivers):
        pass


    @allure.story("增加CSRS结构化上传日志查询报表")  # 用户故事名称
    @allure.title("CSR上传日志查询查询条件功能校验")  # 用例名称
    @allure.description("各条件单独查询==条件组合查询")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14318(self, drivers):
        pass


    @allure.story("增加CSRS结构化上传日志查询报表")  # 用户故事名称
    @allure.title("CSR上传日志查询查询/翻页组合场景校验")  # 用例名称
    @allure.description("查询后翻页==翻页后查询")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14319(self, drivers):
        pass


    @allure.story("增加CSRS结构化上传日志查询报表")  # 用户故事名称
    @allure.title("CSR上传日志查询列表内容正确展示")  # 用例名称
    @allure.description("检查列表内容")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14320(self, drivers):
        pass


    @allure.story("增加CSRS结构化上传日志查询报表")  # 用户故事名称
    @allure.title("CSR上传日志查询页面功能按钮检查")  # 用例名称
    @allure.description("检查页面功能按钮")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14321(self, drivers):
        pass


    @allure.story("增加CSRS结构化上传日志查询报表")  # 用户故事名称
    @allure.title("CSR上传日志查询页面数据默认为空")  # 用例名称
    @allure.description("进入页面")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14322(self, drivers):
        pass


    @allure.story("增加CSRS结构化上传日志查询报表")  # 用户故事名称
    @allure.title("CSR上传日志查询重置按钮功能校验")  # 用例名称
    @allure.description("查询后点击【重置】按钮")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14323(self, drivers):
        pass


    @allure.story("增加CSRS结构化上传日志查询报表")  # 用户故事名称
    @allure.title("CSR上传日志查询导出功能校验")  # 用例名称
    @allure.description("查询后导出==查询后导出==检查导出数据内容")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14324(self, drivers):
        pass


    @allure.story("增加CSRS结构化上传日志查询报表")  # 用户故事名称
    @allure.title("CSR上传日志查询工厂数据成上传到总部后，状态及上传时间正确")  # 用例名称
    @allure.description("工厂→中转库→总部成功，")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14346(self, drivers):
        pass


    @allure.story("增加CSRS结构化上传日志查询报表")  # 用户故事名称
    @allure.title("CSR上传日志查询同步失败时，上传状态应为未上传")  # 用例名称
    @allure.description("工厂→中转库（失败）==工厂→中转库（成功），中转库→总部（失败）")  # 用例描述
    @allure.severity("critical")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14377(self, drivers):
        pass


    @allure.story("增加CSRS结构化上传日志查询报表")  # 用户故事名称
    @allure.title("CSR上传日志查询列表创建时间检查")  # 用例名称
    @allure.description("检查数据创建时间")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14378(self, drivers):
        pass


@allure.feature("MES_CSR秘钥上传google")  # 迭代名称
class Teststory_2206:
    @allure.story("接收工厂推送CSRS结构化数据接口")  # 用户故事名称
    @allure.title("CSR接收工厂推送CSRS结构化数据成功后，数据正确存储到总部数据库")  # 用例名称
    @allure.description("")  # 用例描述
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_14380(self, drivers):
        pass


if __name__ == '__main__':
      pass
