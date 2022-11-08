from libs.common.read_element import Element
from libs.common.time_ui import sleep
from ..test_case.conftest import *
from libs.config.conf import BASE_DIR

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class AssetDefinitionPage(Base):

    @allure.step("Asset Definition页面，点击Add按钮")
    def click_add_asset(self):
        self.is_click(user['Add Asset Definition'])
        sleep(1)


    @allure.step("Asset Add页面, 新增资产定义")
    def add_asset(self, brand, design_by, category, asset_name_en, asset_name_cn, version):
        #Asset Add页面，选择Brand
        self.is_click(user['Brand Select'])
        self.is_click(user['Brand Select Value'], brand)
        #Asset Add页面，选择Design By
        self.is_click(user['Design By'], design_by)
        #选择资产分类
        self.is_click(user['Asset Category'])
        self.is_click(user['Asset Category Value'], category)
        #输入资产英文名称
        self.input_text(user['Asset Name EN'], asset_name_en)
        # 输入资产中文名称
        self.input_text(user['Asset Name CN'], asset_name_cn)
        self.input_text(user['Version'], version)
        self.is_click(user['Has ASN'])
        self.is_click(user['Has ASN Yes'])
        #选中国家 启用状态
        self.scroll_into_view(user['Bangladesh Lable'])
        self.is_click(user['Status Bangladesh Enable'], 'Bangladesh')
        self.is_click(user['Status China Enable'], 'China')
        self.is_click(user['Status Canada Enable'], 'Canada')

    @allure.step("Asset Add页面, 点击Picture上传图片按钮")
    def click_upload_picture(self, picture):
        #滚动到 picture位置
        self.scroll_into_view(user['Upload Picture'])
        path1 = os.path.join(BASE_DIR, 'project', 'DCR', 'data', picture)
        logging.info("打印上传的文件path：{}".format(path1))
        self.click_upload_payslip(path1)

    @allure.step("Asset Add页面,上传图片")
    def click_upload_payslip(self, file):
        self.is_click(user['Upload Picture'])
        sleep(2)
        ele = self.driver.find_element('xpath', "//div/..//input[@name='files']")
        ele.send_keys(file)
        sleep(2)

    @allure.step("Asset Add页面, 点击Submit按钮")
    def click_add_submit(self):
        self.is_click(user['Submit'])

    @allure.step("Asset Definition列表, 筛选当天的日期，查看资产信息")
    def query_create_date(self, start_date):
        self.is_click(user['Create Start Date'])
        self.input_text(user['Create Start Date'], start_date)
        self.is_click(user['Create End Date'])
        self.input_text(user['Create End Date'], start_date)

    @allure.step("Asset Definition列表, 筛选Category")
    def query_category(self, category):
        self.is_click(user['Cagegory Query'])
        self.is_click(user['Asset Category Value'],category)

    @allure.step("Asset Definition列表, 点击Search")
    def click_search(self):
        self.is_click(user['Search'])
        sleep(1.5)

    @allure.step("Asset Definition列表, 或者列表字段内容")
    def get_list_field_content(self, field):
        field = self.element_text(user[field])
        return field



if __name__ == '__main__':
    pass
