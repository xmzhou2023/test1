import random
from public.base.basics import random_list
from libs.common.read_element import Element
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name, object_name)


class InboundOrder(Base):
    """用户类"""

    def input_text(self, locator, txt, *choice):
        """输入文本"""
        sleep(0.5)
        ele = self.find_element(locator, *choice)
        ele.clear()
        ele.send_keys(txt)
        logging.info("输入文本：{}".format(txt))

    @allure.step("查找菜单")
    def click_menu(self, *content):
        self.refresh()
        self.is_click_tbm(user['菜单栏'])
        self.refresh()
        for i in range(len(content)):
            self.is_click_tbm(user['菜单'], content[i])
            logging.info('点击菜单：{}'.format(content[i]))
        self.refresh()
        self.element_exist(user['Loading'])

    @allure.step("点击Unfold 展开筛选项")
    def click_unfold(self):
        self.is_click(user['Unfold'])
        logging.info('点击Unfold 展开筛选项')

    @allure.step("user management页面，输入查询条件")
    def input_search(self, header, content):
        """
        @header： 输入框名称
        @content： 输入内容
        """
        textarea_list = []
        input_list = ['Inbound ID', 'Order ID', 'Delivery Order ID', 'Material ID']
        country_list = ['Seller Region', 'Buyer Region']
        Date_list = ['Inbound Date', 'Delivery Date']
        fuzzySelect_list = ['Buyer', 'Seller']
        exactSelect_list = ['Type', 'Buyer Type', 'Seller Type', 'Upload Type']
        inputSelect_list = ['Brand', 'Buyer Category', 'Model', 'Market Name', 'Buyer Country', 'Seller Country']
        inputSelect_list2 = ['Warehouse']
        self.element_exist(user['Loading'])
        logging.info(f'输入查询条件： {header} ，内容： {content}')
        if content != '':
            if header in textarea_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框3'], content, header)
            elif header in input_list:
                self.input_text(user['输入框'], content, header)
            elif header in exactSelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
            elif header in fuzzySelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框2'], content, header)
                self.is_click_tbm(user['输入结果模糊选择'], content)
            elif header in country_list:
                country = content.split('_')
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], country[2], header)
                self.is_click_tbm(user['地区选择框'], country[0], country[1], country[2])
            elif header in inputSelect_list:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框4'], content, header)
                self.is_click_tbm(user['输入结果精确选择'], content)
                self.is_click_tbm(user['输入框名称'], header)
            elif header in inputSelect_list2:
                self.is_click_tbm(user['输入框'], header)
                self.input_text(user['输入框'], content, header)
                self.is_click_tbm(user['输入结果模糊选择'], content)
            elif header in Date_list:
                createDate = content.split('To')
                for i in range(len(createDate)):
                    self.input_text(user['时间输入框'], createDate[i], header, i + 1)
                    self.is_click_tbm(user['输入框名称'], header)
            else:
                logging.error('请输入正确的查询条件')
                raise ValueError('请输入正确的查询条件')

    @allure.step("点击搜索功能")
    def click_search(self):
        self.is_click(user['Search'])
        self.element_exist(user['Loading'])

    @allure.step("判断空值")
    def assert_None(self, result):
        try:
            assert result == '', logging.warning("断言失败: 该值不为None | x:{}".format(result))
            logging.info("断言成功: 该值为None | x:{}".format(result))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("断言：页面查询结果")
    def assert_Query_result(self, header, content):
        logging.info('开始断言：页面查询结果')
        DomAssert(self.driver).assert_search_contains_result(user['menu表格字段'], user['表格内容'], header, content,
                                                             sc_element=user['滚动条'], h_element=user['表头文本'])

    @allure.step("断言：页面查询结果")
    def assert_search_result(self, header, content):
        if content != '':
            logging.info(f'开始断言：页面查询：{header} 结果 ：{content}')
            id_list = ['Buyer', 'Seller', 'Warehouse']
            Date_list = ['Inbound Date', 'Delivery Date']
            region_list = ['Seller Region', 'Buyer Region']
            if header in id_list:
                self.assert_Query_result(f'{header} ID', content)
            elif header == 'Order ID':
                self.assert_Query_result(f'Sales {header}', content)
            elif header in region_list:
                country = content.split('_')
                for i in range(3):
                    assert_result = False
                    column = self.get_table_info(user['menu表格字段'], f'{header} {3 - i}', sc_element=user['滚动条'],
                                                 h_element=user['表头文本'])
                    contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
                    for j in contents:
                        if ''.join(j.split()) != '':
                            ValueAssert.value_assert_equal(j, country[2])
                            assert_result = True
                        else:
                            logging.info(f'{header} {3 - i} 区域为空，继续比对上级区域')
                            break
                    if assert_result:
                        logging.info('断言结束')
                        break
            elif header in Date_list:
                column = self.get_table_info(user['menu表格字段'], header, sc_element=user['滚动条'],
                                             h_element=user['表头文本'])
                contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
                createDate = content.split('To')
                for i in contents:
                    # timeArray = time.strptime(i, "%Y-%m-%d %H:%M:%S")
                    # a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.mktime(timeArray) + 28800))
                    logging.info(f'实际时间：{i}')
                    # logging.info(f'修正时区后时间：{a}')
                    try:
                        assert createDate[0] <= i <= createDate[1] + ' 23:59:59'
                        logging.info(f'断言成功：创建时间：{i} 在筛选时间 {content} 区间')
                    except:
                        logging.info(f'断言失败：创建时间：{i} 与筛选时间 {content} 不符')
                        raise
            elif header == 'Upload Type':
                column = self.get_table_info(user['menu表格字段'], header, sc_element=user['滚动条'],
                                             h_element=user['表头文本'])
                contents = self.get_row_info(user['表格内容'], column, user['滚动条'])
                for i in contents:
                    if content.lower() in i.lower():
                        logging.info("断言成功，结果: {} 包含指定内容:{}".format(i, content))
            else:
                self.assert_Query_result(header, content)

    @allure.step("组合查询 组合方法")
    def random_Query_Method(self, kwargs):
        list_query = []
        num = random.randint(3, 8)
        for i in kwargs:
            list_query.append(i)
        logging.info(f'输入框：{list_query}')
        list_random = random_list(list_query, num)
        logging.info(f'随机组合：输入框：{list_random}')
        for i in list_random:
            logging.info(f'随机组合：{i} 输入框输入内容：{kwargs[i]}')
            self.input_search(i, kwargs[i])
        self.click_search()
        for i in list_random:
            self.assert_search_result(i, kwargs[i])

    @allure.step("点击Export按钮")
    def click_export(self):
        self.is_click(user['Export'])
        logging.info('点击Export按钮')

    @allure.step("点击ExportDetails按钮")
    def click_export_Details(self):
        self.is_click(user['ExportDetails'])
        logging.info('点击ExportDetails按钮')

    @allure.step("点击弹框Export按钮")
    def click_DialogExport(self):
        self.is_click(user['dialogExport'])
        logging.info('点击弹框Export按钮')

    @allure.step("点击Order IMEI按钮")
    def click_Order_IMEI(self):
        self.is_click(user['OrderIMEI'])
        logging.info('点击Order IMEI按钮')
        self.element_exist(user['弹窗Loading'])

    @allure.step("点击首行Scaned IMEI按钮")
    def click_First_ScanedIMEI(self):
        self.is_click(user['首行ScanedIMEI'])
        logging.info('点击首行Scaned IMEI按钮')
        self.element_exist(user['弹窗Loading'])

    def get_Record_info(self, menu, name, header):
        """
        :param menu: 输入菜单名
        :param name: 输入文件名
        :param header: 需要获取的指定字段
        """
        for i in range(20):
            ac_menu = self.element_text(user['当前菜单'])
            if ac_menu != menu:
                self.click_menu('Basic Data Management', menu)
            column = self.get_table_info(user['Record表格字段'], header, h_element=user['表头文本'])
            content = self.element_text(user['表格指定列内容'], name, column)
            logging.info(f'获得 {menu} 页面 {name} 文件 {header} 字段内容 {content}')
            return content

    @allure.step("断言：Record导入结果")
    def assert_Record_result(self, menu, name, header, result=None):
        """
        :param menu: 菜单
        :param name: 输入文件名
        :param header: 需要获取的指定字段
        :param result: 需要断言的值 比如状态，数量，时间
        """
        logging.info(f'开始断言：{menu} Record导入结果')
        ac_result = self.get_Record_info(menu, name, header)
        if header == 'File Size':
            ValueAssert.value_assert_IsNot(ac_result, '0B')
        else:
            ValueAssert.value_assert_In(result, ac_result)

    @allure.step("获得首行指定内容")
    def get_FirstRow_info(self, header):
        """
        :param header: 需要获取的指定字段
        """
        column = self.get_table_info(user['menu表格字段'], header, h_element=user['表头文本'])
        content = self.inner_text(user['表格首行指定内容'], column)
        content_list = []
        if '|' in content:
            for i in content.split('|'):
                content_list.append(i)
            logging.info('获取首行 {} 内容：{}'.format(header, content_list))
            return content_list
        else:
            logging.info('获取首行 {} 内容：{}'.format(header, content))
            return content

    @allure.step("点击首行复选框")
    def get_FirstRow_checkbox(self):
        self.is_click_tbm(user['首行复选框'])
        logging.info('点击首行复选框')

    @allure.step("断言：Order IMEI页面内容正确")
    def assert_Order_IMEI_result(self, num):
        """
        :param num: 数量
        """
        logging.info('开始断言：Order IMEI页面内容正确')
        total_text = self.element_text(user['dialogTotal'])
        total = total_text[total_text.index(' ') + 1:]
        logging.info(f'页面合计数：{total}')
        if isinstance(num, list):
            num_sum = 0
            for i in num:
                num_sum += int(i)
            num = str(num_sum)
        logging.info(f'首行合计数：{num}')
        ValueAssert.value_assert_equal(total, num)


if __name__ == '__main__':
    pass
