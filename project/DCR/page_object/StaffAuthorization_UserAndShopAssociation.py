from libs.common.read_element import Element
from public.base.basics import Base
from libs.common.time_ui import sleep
from ..test_case.conftest import *
from public.base.basics import Base, random_list
import random
from libs.config.conf import BASE_DIR

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)

class UserShopAssociaPage(Base):
    """ User and Shop Association 菜单定位元素类"""
    @allure.step("进入User and Shop Association页面，根据User或 Shop条件筛选品牌、客户等数据")
    def input_user_or_shop_query(self, label, content):
        self.is_click(user['点击输入框'], label)
        self.input_text(user['输入输入框'], label, content)
        self.presence_sleep_dcr(user['输入结果模糊选择'], content)
        self.is_click(user['输入结果模糊选择'], content)

    @allure.step("进入User and Shop Association页面，点击Unfold 或 Fold展开收起筛选项")
    def click_unfold_or_fold(self, operation):
        self.is_click(user['Click Unfold or Fold'], operation)
        sleep(1.5)

    @allure.step("点击Search按钮筛选数据")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_text(user['Loading'])

    @allure.step("获取分页总条数文本")
    def get_total_text(self):
        get_total = self.element_text(user['Get Total Text'])
        total1 = get_total[6:]
        return total1

    @allure.step("获取列表User ID文本")
    def get_list_user_id(self):
        self.presence_sleep_dcr(user['Get list User ID'])
        get_userid = self.element_text(user['Get list User ID'])
        return get_userid

    @allure.step("获取列表User Name文本")
    def get_list_user_name(self):
        get_username = self.element_text(user['Get list User Name'])
        return get_username

    @allure.step("获取列表Position文本")
    def get_list_position(self):
        get_position = self.element_text(user['Get list Position'])
        return get_position

    @allure.step("获取列表Shop ID文本")
    def get_list_shop_id(self):
        shop_id = self.element_text(user['Get list Shop ID'])
        return shop_id

    @allure.step("获取列表Shop Name文本")
    def get_list_shop_name(self):
        shop_name = self.element_text(user['Get list Shop Name'])
        return shop_name

    @allure.step("点击关闭导出记录菜单")
    def click_close_export_record(self):
        self.is_click(user['关闭导出记录菜单'])

    @allure.step("点击关闭用户与门店关系菜单")
    def click_close_user_shop_assoc(self):
        self.is_click(user['关闭用户与门店关系菜单'])


    # User and Shop Association列表数据筛选后，导出操作成功后验证
    @allure.step("点击Export导出按钮")
    def click_export(self):
        self.is_click(user['Export'])
        sleep(2)

    @allure.step("点击下载Download Icon按钮，点击more更多按钮")
    def click_download_more(self):
        self.mouse_hover_click(user['Download Icon'])
        Base.presence_sleep_dcr(self, user['More'])
        self.is_click(user['More'])
        sleep(3)


    @allure.step("输入Task Name筛选该任务的导出记录")
    def input_task_name(self, content):
        self.is_click(user['Input Task Name'])
        self.input_text(user['Input Task Name'], txt=content)
        sleep(0.5)
        self.is_click(user['Task Name value'], content)

    @allure.step("导出页面，点击Search按钮")
    def click_export_search(self):
        down_status = self.export_download_status(user['Export Record Search'], user['获取下载状态文本'])
        return down_status

    @allure.step("导出记录页面，获取列表 Download Status文本")
    def get_download_status_text(self):
        status = self.element_text(user['获取下载状态文本'])
        return status

    @allure.step("导出记录页面，获取列表 Task Name文本")
    def get_task_name_text(self):
        self.presence_sleep_dcr(user['获取任务名称文本'])
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
    def get_export_operation_text(self):
        operation = self.element_text(user['获取操作按钮文本'])
        return operation

    @allure.step("导出记录页面，获取列表导出时间文本")
    def get_export_time_text(self):
        export_time = self.element_text(user['获取导出时间'])
        export_time1 = export_time[0:1]
        return export_time1


    @allure.step("断言判读分页总条数，是否能查询到数据且大于1条")
    def assert_total(self, total):
        if int(total) >= 1000:
            logging.info("查看User and Shop Association列表，加载筛选的数据正常，分页总条数Total：{}".format(total))
        else:
            logging.info("查看User and Shop Association列表，加载筛选的数据正常，分页总条数Total：{}".format(total))

    @allure.step("断言判读分页总条数，是否能查询到数据且大于1条")
    def assert_total2(self, total2):
        if int(total2) >= 1:
            logging.info("查看User and Shop Association列表，加载筛选的数据正常，分页总条数Total：{}".format(total2))
        else:
            logging.info("查看User and Shop Association列表，加载筛选的数据正常，分页总条数Total：{}".format(total2))

    @allure.step("断言导出后的文件大小与导出时间是否大于0")
    def assert_file_time_size(self, file_size, export_time):
        if int(file_size) > 0:
            logging.info("User and Shop Association导出成功，File Size 导出文件大于1KB:{}".format(file_size))
        else:
            logging.info("User and Shop Association导出失败，File Size 导出文件小于1KB:{}".format(file_size))

        if int(export_time) > 0:
            logging.info("User and Shop Association导出成功，Export Time(s)导出时间大于0s:{}".format(export_time))
        else:
            logging.info("User and Shop Association导出成功，Export Time(s)导出时间等于0s:{}".format(export_time))


    @allure.step("断言精确查询结果 user and shop Association 列表，字段列、字段内容是否与预期的字段内容值一致，有滚动条")
    def assert_user_and_shop_assoc_field(self, header, content):
        DomAssert(self.driver).assert_search_result(user['表格字段'], user['表格指定列内容'], header, content,
                                                    sc_element=user['水平滚动条'])

    @allure.step("断言模糊查询结果 user and shop Association 列表，字段列、字段内容是否与预期的字段内容值一致，有滚动条")
    def assert_contains_user_and_shop_assoc_field(self, header, content):
        DomAssert(self.driver).assert_search_contains_result(user['表格字段'], user['表格指定列内容'], header, content,
                                                             sc_element=user['水平滚动条'])


    #导入用户和门店关系
    @allure.step("user and shop Association 页面，点击导入按钮")
    def click_import(self):
        self.is_click(user['Click Import'])
        sleep(1)
        """未上传文件时，先点击Save，弹出提示：请上传文件"""
        self.presence_sleep_dcr(user['Click Upload Save'])
        self.is_click(user['Click Upload Save'])
        DomAssert(self.driver).assert_att('Please upload first.')

    @allure.step("user and shop Association 页面，点击Upload上传文件")
    def click_upload_save(self, file1):
        path1 = os.path.join(BASE_DIR, 'project', 'DCR', 'data', file1)
        logging.info("打印上传的用户模板文件path：{}".format(path1))
        self.is_click(user['Click Upload'])
        sleep(3)
        ele = self.driver.find_element('xpath', "//div/..//button/..//input[@name='file']")
        ele.send_keys(file1)
        sleep(3)
        self.is_click(user['Import Save'])
        self.presence_sleep_dcr(user['Upload Confirm'])
        self.is_click(user['Upload Confirm'])

    @allure.step("导入记录页面，根据Import Date条件筛选导入开始日期")
    def import_record_import_date_query(self, start_date):
        self.is_click(user['Query Import Start Date'])
        self.input_text(user['Query Import Start Date'], start_date)

    @allure.step("循环点击查询，直到获取到导入记录状态为Upload Successfully")
    def click_import_status_search(self):
        import_status = self.import_record_status(user['Search'], user['Get Import Record Status'])
        return import_status


    #删除用户和门店关系数据
    # def input_shop_id_query(self):
    #     self.is_click(user['Shop输入框'])
    #     self.input_text(user['Input Shop输入框'])
    #     self.presence_sleep_dcr(user[''])
    #     self.is_click(user[''])
    @allure.step("根据User ID与 Shop ID条件进行搜索待删除的数据")
    def user_and_shop_query(self, unfold):
        self.click_unfold_or_fold(unfold)
        self.input_user_or_shop_query('lhmdianzhang', 'User')
        self.input_user_or_shop_query('EG000706', 'Shop')
        self.click_search()

    @allure.step("点击删除操作")
    def click_delete_operation(self, unfold):
        self.click_unfold_or_fold('Fold')
        self.is_click(user['勾选第一个复选框'])
        self.is_click(user['Delete'])
        self.is_click(user['Confirm Delete'])


    @allure.step("断言：页面查询结果")
    def assert_User_Exist(self, header, content):
        logging.info('开始断言：页面查询结果')
        DomAssert(self.driver).assert_search_contains_result(user['表格指定列内容'], header, content, sc_element=user['水平滚动条'], h_element=user['表头文本'])

    @allure.step("判断空值")
    def assert_None(self, result):
        try:
            assert result == '', logging.warning("断言失败: 该值不为None | x:{}".format(result))
            logging.info("断言成功: 该值为None | x:{}".format(result))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("user management页面，输入查询条件")
    def input_search(self, header, content):
        """
        @header： 输入框名称
        @content： 输入内容
        """
        click_input_list = ['Return Order ID', 'Delivery/DN Order ID']
        input_select_list = ['Brand']
        input_select_all_list1 = ['Status', 'Return Type']
        input_select_all_list22 = ['Model', 'Market Name', 'Seller Country']
        return_date_list = ['Return Date']
        seller_list = ['Seller', 'Buyer']
        warehouse_list = ['Buyer Warehouse Region', 'Seller Warehouse Region']
        imei_list = ['IMEI']
        self.element_exist(user['Loading'])
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if header in click_input_list:
            self.is_click_dcr(user['输入框'], header)
            self.input_text(user['输入框'], content, header)
        elif header in input_select_list:
            self.is_click_dcr(user['输入框'], header)
            self.is_click(user['输入结果精确选择'], content, header)
            self.is_click(user['点击label标签'], header)
        elif header in input_select_all_list1:
            self.is_click(user['输入框'], header)
            self.input_text(user['输入框2'], content, header)
            self.is_click(user['输入结果精确选择'], content)
        elif header in input_select_all_list22:
            self.is_click_dcr(user['输入框'], header)
            self.input_text(user['输入框1'], content, header)
            sleep(1.8)
            self.is_click(user['输入结果精确选择1'], header, content)
            self.is_click(user['点击label标签'], header)
        elif header in return_date_list:
            self.is_click(user['Input Return Start Date'], header)
            self.input_text(user['Input Return Start Date'], content, header)
            """弹出日历空间后，点击日历标签释法"""
            self.is_click(user['点击label标签'], header)
        elif header in seller_list:
            self.is_click(user['输入框'], header)
            self.input_text(user['输入框2'], content, header)
            sleep(0.8)
            self.is_click(user['输入结果模糊选择'], content)
        elif header in warehouse_list:
            self.is_click(user['输入框'], header)
            self.input_text(user['输入框'], content, header)
            sleep(0.8)
            self.is_click(user['输入仓库区域精确选择'], header, content)
        elif header in imei_list:
            self.is_click(user['输入框'], header)
            self.input_text(user['输入框IMEI'], content, header)
        else:
            logging.error('请输入正确的查询条件')
            raise ValueError('请输入正确的查询条件')


    @allure.step("断言：页面查询结果")
    def assert_search_result(self, header, content):
        logging.info(f'开始断言：页面查询：{header} 结果 ：{content}')
        if header == 'Return Order ID' or header == 'Delivery/DN Order ID':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Return Date':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Status':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Return Type':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Brand':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Model':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Market Name':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Seller':
            self.assert_User_Exist(f'{header} ID', content)
        elif header == 'Seller Country':
            self.assert_User_Exist(f'{header}', content)
        elif header == 'Buyer':
            self.assert_User_Exist(f'{header} ID', content)
        elif header == 'Buyer Warehouse Region' or header == 'Seller Warehouse Region':
            self.assert_User_Exist(f'{header}1', content)
        elif header == 'IMEI':
            self.is_click(user['点击IMEI Detail按钮'])
            sleep(0.5)
            self.assert_User_Exist(f'{header}', content)
            self.is_click(user['关闭IMEI Detail窗口'])
        else:
            self.assert_User_Exist(header, content)


    @allure.step("组合查询 组合方法")
    def random_Query_Method(self, kwargs):
        list_query = []
        num = random.randint(3, 9)
        for i in kwargs:
            list_query.append(i)
        logging.info(f'输入框：{list_query}')
        list_random = random_list(list_query, num)
        logging.info(f'随机组合：输入框：{list_random}')
        for i in list_random:
            logging.info(f'随机组合：输入内容：{kwargs[i]}')
            self.input_search(i, kwargs[i])
        self.click_search()
        for i in list_random:
            self.assert_search_result(i, kwargs[i])





if __name__ == '__main__':
    pass