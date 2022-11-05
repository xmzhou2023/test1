import allure
import pytest
@allure.feature("信贷自动化FOL改造")  # 迭代名称
class Teststory_410:
    @allure.story("【信贷自动化】信贷控制范围的维度精细化管理，细化到付款方式维度客户公司信贷OL改造")  # 用户故事名称
    @allure.title("【收款确认单】点击认领按钮时，将信贷明细表的字段从主表中默认拷贝到信贷明细中")  # 用例名称
    @allure.description("选中此笔收款确认单，点击收款认领==查看信贷明细表的字段是否从主表中默认拷贝到信贷明细中")  # 用例描述
    @allure.severity("normal")  # 用例等级
    @pytest.mark.smoke  # 用例标记
    def test_5696(self, drivers):
        12pass312


if __name__ == '__main__':
      pass
