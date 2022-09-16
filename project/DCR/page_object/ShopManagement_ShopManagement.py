from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
import random
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class ShopManagementPage(Base):
    """ShopManagementPage 页面元素类"""
    @allure.step("点击Add新建门店按钮")
    def click_add(self):
        self.presence_sleep_dcr(user['Add'])
        self.is_click(user['Add'])
        sleep(3)

    @allure.step("新建门店，输入门店名称")
    def input_shop_name(self, content):
        self.presence_sleep_dcr(user['Shop Name'])
        self.input_text(user['Shop Name'], txt=content)

    @allure.step("新建门店，输入联系人")
    def input_contact_name(self, content):
        self.input_text(user['Contact Name'], txt=content)

    @allure.step("新建门店，输入联系人电话")
    def input_contact_no(self, content):
        self.input_text(user['Contact No'], txt=content)

    @allure.step("新建门店时，输入国家城市")
    def input_country_city(self, content):
        self.is_click(user['Country City'])
        self.input_text(user['Country City'], txt=content)
        sleep(1)
        self.is_click(user['Country City value'])

    @allure.step("新建门店时，输入地址")
    def input_address(self, content):
        self.input_text(user['Address'], txt=content)

    @allure.step("新建门店时，选择品牌")
    def click_brand(self):
        self.is_click(user['Brand'])
        sleep(1)
        self.is_click(user['TECNO'], "TECNO")

    @allure.step("新建门店时，输入销售区域")
    def input_sales_region(self, content):
        self.scroll_into_view(user['Sales Region'])
        self.is_click(user['Sales Region'])
        self.input_text(user['Sales Region'], txt=content)
        sleep(1)
        self.is_click(user['Sales Region value'], "Barisal itel")
        #sleep(1)

    @allure.step("新建门店时，选择门店等级")
    def click_shop_grade(self):
        self.is_click(user['Shop Grade'])
        sleep(2)
        self.is_click(user['Shop Grade Value'], "B 0-50 ")

    @allure.step("新建门店时，选择门店类型")
    def click_shop_type(self):
        self.is_click(user['Shop Type'])
        sleep(1)
        self.is_click(user['Shop Type GRT value'], "GRT")

    @allure.step("新建门店时，选择门店形象类型")
    def click_image_type(self):
        self.scroll_into_view(user['Image Type'])
        self.is_click(user['Image Type'])
        sleep(1)
        self.is_click(user['Zone Shop Value'], "Zone Shop")

    @allure.step("新建门店时，选择上传方式")
    def click_upload_mode(self):
        self.is_click(user['Inventory Upload mode'])
        sleep(1)
        self.is_click(user['Freedom value'], "Freedom")

    @allure.step("新建门店时，选择NO，输入门店关联的零售商ID")
    def input_retailer_account(self, content):
        self.is_click(user['点击No'])
        sleep(1)
        self.is_click(user['输入零售商'])
        self.input_text(user['输入零售商'], txt=content)
        sleep(2)
        self.is_click(user['选中零售商'], "SN455338 lhmRetailer005 ")

    @allure.step("新建门店时，选择商业区域")
    def click_commercial_area_tag(self):
        self.is_click(user['Commercial Area Tag'])
        sleep(1)
        self.is_click(user['Commercial Area value'], "IR")

    @allure.step("新建或者编辑门店时，点击提交")
    def click_submit(self):
        self.is_click_dcr(user['Submit'], "Submit")
        sleep(2)

    @allure.step("新建门店时，门店名称后缀随机生成")
    def shop_random(self):
        num = str(random.randint(100, 999))
        return num

    @allure.step("根据门店名称查询，最近新建的门店ID")
    def input_query_shop_name(self, content):
        self.presence_sleep_dcr(user['点击门店输入框'])
        self.is_click_dcr(user['点击门店输入框'])
        self.input_text(user['门店输入框输入'], txt=content)
        sleep(3)
        self.presence_sleep_dcr(user['选中门店值1'], content)
        self.is_click(user['选中门店值1'], content)

    @allure.step("根据门店名称查询，最近扩展门店品牌的的门店ID")
    def extend_query_shop_name(self, content):
        self.is_click(user['点击门店输入框'])
        self.input_text_dcr(user['点击门店输入框'], txt=content)
        sleep(2)
        self.presence_sleep_dcr(user['选中门店值1'], content)
        self.is_click(user['选中门店值1'], content)

    @allure.step("点击Search查询门店信息")
    def click_query_search(self):
        self.is_click(user['Search'])
        sleep(4)

    @allure.step("筛选最近新建的门店ID后，勾线第一个复选框")
    def click_first_checkbox(self):
        self.presence_sleep_dcr(user['勾选第一个复选框'])
        self.is_click(user['勾选第一个复选框'])

    @allure.step("勾选第二个复选框")
    def click_second_checkbox(self):
        self.is_click(user['勾选第二个复选框'])

    @allure.step("点击More Option更多操作按钮")
    def click_more_option(self):
        self.is_click(user['More Option'])
        sleep(1.7)

    @allure.step("点击delete 删除按钮")
    def click_delete(self):
        self.presence_sleep_dcr(user['Delete'])
        self.is_click(user['Delete'])
        sleep(1)

    @allure.step("点击Confirm 确认删除按钮")
    def click_confirm_delete(self):
        self.is_click(user['Delete Confirm'])
        sleep(1)

    @allure.step("删除门店成功后，获取列表 successfully文本内容")
    def get_text_edit_success(self):
        success = self.element_text(user['Edited Successfully'])
        return success

    @allure.step("删除门店成功后，获取列表 successfully文本内容")
    def get_text_del_success(self):
        success = self.element_text(user['delete successfully'])
        return success

    @allure.step("删除门店成功后，获取列表 No Data文本内容")
    def get_text_nodata(self):
        nodata = self.element_text(user['No Data'])
        return nodata

    @allure.step("获取列表Shop ID文本")
    def get_shop_id_text(self):
        sleep(5)
        self.presence_sleep_dcr(user['获取ShopID文本'])
        get_shop_id = self.element_text(user['获取ShopID文本'])
        return get_shop_id

    @allure.step("获取列表Shop ID文本")
    def get_extend_shop_id_text(self):
        self.presence_sleep_dcr(user['获取ShopID文本'])
        get_shop_id = self.element_text(user['获取ShopID文本'])
        return get_shop_id

    @allure.step("获取列表Shop Name文本")
    def get_shop_name_text(self):
        self.presence_sleep_dcr(user['获取ShopName文本'])
        get_shop_name = self.element_text(user['获取ShopName文本'])
        return get_shop_name

    @allure.step("获取列表brand文本")
    def get_shop_brand_text(self):
        sleep(1)
        get_brand = self.element_text(user['获取Brand文本'])
        return get_brand

    @allure.step("获取列表Status文本")
    def get_shop_status_text(self):
        self.presence_sleep_dcr(user['获取Status文本'])
        get_status = self.element_text(user['获取Status文本'])
        return get_status

    @allure.step("获取列表public文本")
    def get_shop_public(self):
        get_public = self.element_text(user['获取Public ID文本'])
        get_public1 = get_public[1:]
        return get_public1

    @allure.step("点击Reset重置按钮")
    def click_reset(self):
        self.is_click(user['Reset'])
        sleep(4)


    """门店扩展品牌"""
    @allure.step("点击More Option->Extend Brand扩展品牌按钮")
    def click_extend_brand(self):
        self.presence_sleep_dcr(user['Extend Brand'])
        self.is_click(user['Extend Brand'])
        sleep(1)

    @allure.step("点击选择扩展品牌的输入框，然后选择扩展的品牌itel")
    def select_extend_brand(self, content):
        self.is_click(user['下拉选择扩展品牌'])
        self.input_text(user['下拉选择扩展品牌'], txt=content)
        sleep(2)
        self.is_click(user['选中扩展的品牌'], content)

    @allure.step("点击增加扩展品牌时，弹出窗口选择品牌后，点击Save")
    def extend_brand_save(self):
        self.is_click(user['Extend Brand Save'])
        sleep(5)

    @allure.step("编辑门店，增加扩展品牌时，输入销售区域并选择销售区域")
    def input_extend_sales_region(self, content):
        self.scroll_into_view(user['Extend Sales Region'])
        sleep(3)
        self.is_click(user['Extend Sales Region'])
        self.input_text(user['Extend Sales Region'], txt=content)
        sleep(3.5)
        self.is_click(user['Extend Sales Region Value'], content)
        sleep(1)

    @allure.step("扩展门店等级属性")
    def click_extend_shop_grade(self):
        self.scroll_into_view(user['Extend Shop Grade'])
        sleep(1)
        self.is_click(user['Extend Shop Grade'])
        sleep(2.5)
        self.is_click(user['Extend Shop Grade Value'], "A 10-20 ")

    @allure.step("扩展门店类型属性")
    def click_extend_shop_type(self):
        self.is_click(user['Extend Shop Type'])
        sleep(1.5)
        self.is_click(user['Extend Shop Type Value'], "CHIN")

    @allure.step("扩展门店形象属性")
    def click_extend_image_type(self):
        self.is_click(user['Extend Image Type'])
        sleep(1.5)
        self.is_click_dcr(user['Extend Zone Shop Value'], "Zone Shop")
        sleep(1)

    @allure.step("扩展零售商客户属性")
    def extend_retail_customer(self, content):
        self.is_click(user['扩展品牌输入零售商'])
        self.input_text(user['扩展品牌输入零售商'], txt=content)
        sleep(3)
        self.is_click_dcr(user['扩展品牌选中零售商'], content)

    @allure.step("扩展商业区域属性")
    def extend_commercial_area(self):
        self.is_click(user['Extend Commercial Area'])
        sleep(1.5)
        self.is_click_dcr(user['Extend Commercial Value'], "KA")

    @allure.step("关闭门店管理菜单")
    def click_close_shop_management(self):
        self.is_click(user['关闭门店管理菜单'])
        sleep(1)

    @allure.step("关闭导出记录菜单")
    def click_close_export_record(self):
        """关闭导出记录菜单"""
        self.is_click(user['关闭导出记录菜单'])
        sleep(1)

    """禁用门店"""
    @allure.step("点击禁用门店按钮")
    def click_disable_confirm(self):
        self.presence_sleep_dcr(user['Disable'])
        self.is_click(user['Disable'])
        sleep(1.5)
        self.presence_sleep_dcr(user['Disable Confirm'])
        self.is_click(user['Disable Confirm'])
        sleep(1)


    """启用门店Disabled"""
    @allure.step("点击启用门店按钮")
    def click_enable_confirm(self):
        self.presence_sleep_dcr(user['Enable'])
        self.is_click(user['Enable'])
        sleep(1.5)
        self.presence_sleep_dcr(user['Enable Confirm'])
        self.is_click(user['Enable Confirm'])
        sleep(1)

    @allure.step("Status筛选项，筛选禁用或启用状态")
    def click_status_filter(self, status):
        self.is_click(user['门店列表筛选状态'])
        sleep(1)
        self.presence_sleep_dcr(user['筛选后选中禁用值'], status)
        self.is_click(user['筛选后选中禁用值'], status)

    @allure.step("点击Status筛选项后，点击Status属性名称，释放光标位置")
    def click_status_attribute(self):
        self.is_click(user['Click Status Attribute'])
        sleep(1)


    """View查看门店"""
    @allure.step("门店管理页面，点击View查看门店详情")
    def click_view_shop(self):
        self.is_click(user['View Shop'])
        sleep(3.5)

    @allure.step("门店管理页面，获取列表Shop ID段内容")
    def get_list_shop_id_text(self):
        self.presence_sleep_dcr(user['Get list Shop ID Text'])
        list_shop_id = self.element_text(user['Get list Shop ID Text'])
        return list_shop_id

    @allure.step("门店管理页面，获取列表Shop Name字段内容")
    def get_list_shop_name_text(self):
        self.presence_sleep_dcr(user['Get list Shop Name Text'])
        list_shop_name1 = self.element_text(user['Get list Shop Name Text'])
        return list_shop_name1

    @allure.step("门店管理页面，获取列表Contact Name字段内容")
    def get_list_public_id_text(self):
        self.scroll_into_view(user['Get list Public ID Text'])
        contact_name = self.element_text(user['Get list Public ID Text'])
        return contact_name

    @allure.step("门店管理页面，获取列表Contact Name字段内容")
    def get_list_contact_name_text(self):
        self.scroll_into_view(user['Get list Public ID Text'])
        contact_name = self.element_text(user['Get list Contact Name Text'])
        return contact_name

    @allure.step("门店管理页面，获取列表Contact no字段内容")
    def get_list_contact_no_text(self):
        contact_no = self.element_text(user['Get list Contact No Text'])
        return contact_no

    @allure.step("View详情页，获取Shop ID字段内容")
    def get_view_shop_id_text(self):
        self.scroll_into_view(user['Get view Shop ID Text'])
        view_shop_id = self.element_input_text(user['Get view Shop ID Text'])
        return view_shop_id

    @allure.step("View详情页，获取Shop Name字段内容")
    def get_view_shop_name_text(self):
        view_shop_name = self.element_input_text(user['Get View Shop Name Text'])
        return view_shop_name

    @allure.step("View详情页，获取Contact Name字段内容")
    def get_view_contact_name_text(self):
        view_contact_name = self.element_input_text(user['Get View Contact Name Text'])
        return view_contact_name

    @allure.step("View详情页，获取Contact No字段内容")
    def get_view_contact_no_text(self):
        view_contact_no = self.element_input_text(user['Get View Contact No Text'])
        return view_contact_no

    @allure.step("View详情页，获取Public ID字段内容")
    def get_view_public_id_text(self):
        view_public_id = self.element_input_text(user['Get View Public ID Text'])
        return view_public_id

    @allure.step("View详情页面，关闭门店View页面")
    def click_close_shop_view(self):
        self.is_click(user['Close Shop View'])
        sleep(3)


    """查询门店信息"""
    @allure.step("点击Unfold 展开筛选项")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        sleep(2)

    @allure.step("点击Fold收起筛选项")
    def click_fold(self):
        self.is_click(user['Fold'])

    @allure.step("输入Create Date开始日期与截止日期")
    def input_create_date(self, context, context1):
        self.is_click(user['Create Start Date'])
        self.input_text(user['Create Start Date'], txt=context)
        sleep(0.5)
        self.is_click(user['Create End Date'])
        self.input_text(user['Create End Date'], txt=context1)

    @allure.step("获取Total分页总数")
    def get_total_text(self):
        total = self.element_text(user['Get Total'])
        total1 = total[6:]
        return total1

    @allure.step("断言分页总数是否存在数据")
    def assert_total(self, total):
        if int(total) > 1:
            logging.info("筛选考勤记录列表，分页总条数大于1，能查询到考勤记录数Total:{}".format(total))
        else:
            logging.info("筛选考勤记录列表，分页总条数为1，未查询到考勤记录数Total:{}:".format(total))

    @allure.step("获取列表品牌字段内容")
    def get_list_brand_text(self):
        get_list_brand = self.element_text(user['Get list Brand Text'])
        return get_list_brand


    """编辑门店信息"""
    @allure.step("门店列表页面，点击编辑门店功能")
    def click_edit_shop(self):
        self.presence_sleep_dcr(user['Edit Shop'])
        self.is_click(user['Edit Shop'])
        sleep(2)


    """导出门店功能"""
    @allure.step("门店列表页面，点击Export 导出考勤记录")
    def click_export(self):
        self.is_click(user['Export'])
        sleep(2)

    @allure.step("门店列表页面，导出操作后，点击右上角下载图标,点击右上角more...")
    def click_download_more(self):
        self.is_click(user['Download Icon'])
        sleep(1)
        self.presence_sleep_dcr(user['More'])
        self.is_click(user['More'])
        sleep(6)

    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], txt=content)
        sleep(2)
        self.is_click(user['Task Name value'], content)

    @allure.step("循环点击查询，直到获取到下载状态为COMPLETE")
    def click_export_search(self):
        download_status = self.export_download_status(user['Export Record Search'], user['获取下载状态文本'])
        return download_status

    @allure.step("导出记录页面，获取列表 Download Status文本")
    def get_download_status_text(self):
        status = self.find_element(user['获取下载状态文本'])
        while status != "COMPLETE":
            status = self.element_text(user['获取下载状态文本'])
            sleep(1)
        return status

    @allure.step("导出记录页面，获取列表 Task Name文本")
    def get_task_name_text(self):
        task_name = self.element_text(user['获取任务名称文本'])
        return task_name

    @allure.step("导出记录页面，获取列表 Task Name文本")
    def get_file_size_text(self):
        file_size = self.element_text(user['获取文件大小文本'])
        file_size1 = file_size[0:1]
        return file_size1

    @allure.step("导出记录页面，获取列表 User ID文本")
    def get_task_user_id_text(self):
        user_id = self.element_text(user['获取用户ID文本'])
        return user_id

    @allure.step("导出记录页面，获取列表 Create Date文本")
    def get_create_date_text(self):
        self.scroll_into_view(user['获取创建日期文本'])
        create_date = self.element_text(user['获取创建日期文本'])
        create_date1 = create_date[0:10]
        return create_date1

    @allure.step("导出记录页面，获取列表Complete Date文本")
    def get_complete_date_text(self):
        complete_date = self.element_text(user['获取完成日期文本'])
        complete_date1 = complete_date[0:10]
        return complete_date1

    @allure.step("导出记录页面，获取列表 Operation文本")
    def get_operation_text(self):
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    @allure.step("导出记录页面，获取列表导出时间文本")
    def get_export_time_text(self):
        export_time = self.element_text(user['获取导出时间'])
        export_time1 = export_time[0:1]
        return export_time1

    @allure.step("断言分页总数是否存在数据")
    def assert_total(self, total):
        if int(total) > 0:
            logging.info("筛选考勤记录列表，分页总条数大于0，能查询到考勤记录数Total:{}".format(total))
        else:
            logging.info("筛选考勤记录列表，分页总条数为0，未查询到考勤记录数Total:{}:".format(total))

    @allure.step("断言分页总数是否存在数据")
    def assert_total2(self, total):
        if int(total) > 1000:
            logging.info("查看考勤记录列表，分页总条数大于1000，能查询到考勤记录Total：{}".format(total))
        else:
            logging.info("查看考勤记录列表，分页总条数为1000，未查询到考勤记录Total：{}".format(total))

    @allure.step("断言文件或导出时间是否有数据")
    def assert_file_time_size(self, file_size, export_time):
        if int(file_size) > 0:
            logging.info("Attendance Records导出成功，File Size导出文件大于M:{}".format(file_size))
        else:
            logging.info("Attendance Records导出失败，File Size导出文件小于M:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("Attendance Records导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("Attendance Records导出失败，Export Time(s)导出时间小于0s:{}".format(export_time))
        sleep(1)


if __name__ == '__main__':
    pass