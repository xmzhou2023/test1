from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
import sys
import allure
import logging
from selenium.webdriver.support.select import Select
from libs.common.time_ui import sleep
from libs.common.connect_sql import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from public.base.basics import Base

"""     值校验的各种方法     """

class ValueAssert(object):

    @allure.step("两值相等断言")
    def value_assert_equal(a, b):
        try:
            assert a == b, logging.warning("断言失败: 两值不等 | a:{} b:{}".format(a, b))
            logging.info("断言成功: 两值相等 | a:{} b:{}".format(a, b))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("两值不等断言")
    def value_assert_Notequal(a, b):
        try:
            assert a != b, logging.warning("断言失败: 两值相等 | a:{} b:{}".format(a, b))
            logging.info("断言成功: 两值不等 | a:{} b:{}".format(a, b))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("值为True值断言")
    def value_assert_True(x):
        try:
            assert bool(x) is True, logging.warning("断言失败: 该值不为True值 | x:{}".format(x))
            logging.info("断言成功: 该值为True值 | x:{}".format(x))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("值为False值断言")
    def value_assert_False(x):
        try:
            assert bool(x) is False, logging.warning("断言失败: 该值不为False值 | x:{}".format(x))
            logging.info("断言成功: 该值为False值 | x:{}".format(x))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("是本身断言")
    def value_assert_Is(a, b):
        try:
            assert a is b, logging.warning("断言失败:  a 不是 b | a:{} b:{}".format(a, b))
            logging.info("断言成功: a 是 b | a:{} b:{}".format(a, b))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("不是本身断言")
    def value_assert_IsNot(a, b):
        try:
            assert a is not b, logging.warning("断言失败: a 是 b | a:{} b:{}".format(a, b))
            logging.info("断言成功: a 不是 b | a:{} b:{}".format(a, b))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("值为None值断言")
    def value_assert_IsNone(x):
        try:
            assert x is None, logging.warning("断言失败: 该值不为None | x:{}".format(x))
            logging.info("断言成功: 该值为None | x:{}".format(x))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("值不为None值断言")
    def value_assert_IsNoneNot(x):
        try:
            assert x is not None, logging.warning("断言失败: 该值为None | x:{}".format(x))
            logging.info("断言成功: 该值不为None | x:{}".format(x))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("是包含断言")
    def value_assert_In(a, b):
        try:
            assert a in b, logging.warning("断言失败: a 不包含 b | a:{} b:{}".format(a, b))
            logging.info("断言成功: a 包含 b | a:{} b:{}".format(a, b))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("不是包含断言")
    def value_assert_InNot(a, b):
        try:
            assert a not in b, logging.warning("断言失败: a 包含 b | a: {} b:{}".format(a, b))
            logging.info("断言成功: a 不包含 b | a: {} b: {}".format(a, b))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("判断值为指定类型断言")
    def value_assert_Instance(a, b):
        try:
            assert isinstance(a, b), logging.warning("断言失败: a: {} 类型：{}".format(a, b))
            logging.info("断言成功: a: {} 类型： {}".format(a, b))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("判断值不是指定类型断言")
    def value_assert_IsInstanceNot(a, b):
        try:
            assert not isinstance(a, b), logging.warning("断言失败: a: {} 类型：{}".format(a, b))
            logging.info("断言成功: a: {} 类型：{}".format(a, b))
        except Exception as e:
            logging.error(e)
            raise


"""     页面元素校验的方法     """
class DomAssert(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)


    @allure.step("值为True值断言")
    def assert_platform(self, word):
        try:
            value = sys.platform
            assert (word in value), logging.warning("断言失败：运行系统与预期不一致 |  当前系统: {}".format(value))
            logging.info("断言成功：运行系统与预期一致 | 当前系统: {}".format(value))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("存在某文字断言")
    def assert_att(self, word):
        """页面是否存在某文字"""
        try:
            Base(self.driver).base_get_img('result')
            att = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'{}')]".format(word)))).text
            assert word in att, logging.warning("断言失败：页面不存在该标识 | 当前页面关键字: {}".format(att.replace("\n", "|")))
            logging.info("断言成功：页面存在该标识 | 当前页面关键字: {}".format(att.replace("\n", "|")))
        except Exception as e:
            logging.error(e)
            raise

    def assert_exact_att(self, word):
        """精确匹配：页面是否存在某文字"""
        try:
            Base(self.driver).base_get_img('result')
            att = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[normalize-space(text())='{}']".format(word)))).text
            assert word in att, logging.warning("断言失败：页面不存在该标识{} | 关键字:{}".format(att, word))
            logging.info("断言成功：页面存在该标识{} | 关键字:{}".format(att, word))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("具体某行某列存在某内容断言")
    def assert_point_att(self, variable1, variable2, word, press='Search'):
        """精确匹配：某行某列是否存在某文字"""
        """查询结果和需要的值不一致时，最多循环5次等待查询，在5次内结果一致即跳出循环，进行断言。超过5次结果还是不一样也一样跳出循环，进行断言"""
        n = 1
        while n < 6:
            attr = self.driver.find_element(By.XPATH, "//tr[{0}]/td[{1}]//*".format(variable1, variable2)).text
            if attr == word:
                logging.info("断言成功：页面存在该标识{} | 关键字:{}".format(attr, word))
                break
            else:
                logging.info("继续查询{}值".format(word))
                sleep(5)
                # print("//button//span[contains(text(),'{}')]".format(press))
                self.driver.find_element(By.XPATH, "//button//span[contains(text(),'{}')]".format(press)).click()
                n += 1
                continue
        try:
            Base(self.driver).base_get_img('result')
            att = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//tr[{0}]/td[{1}]//*[normalize-space(text())='{2}']".format(variable1, variable2, word))), message='你要的值未找到').text
            assert word in att, logging.warning("断言失败：页面不存在该标识{} | 关键字:'{}'".format(att, word))
            logging.info("断言成功：页面存在该标识'{}' | 关键字:'{}'".format(att, word))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("值为True值断言")
    def assert_title(self, word):
        """当前页面标题是否是指定title"""
        try:
            att = self.driver.switch_to.window(self.driver.window_handles[-1])
            assert word in att.title, logging.warning("断言失败：标题为预期不符 | 标题: {}".format(att.title))
            logging.info("断言成功：标题为预期一致 | 标题: {}".format(att.title))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("值为True值断言")
    def assert_url(self, word):
        """当前页面是不是指定url"""
        try:
            att = self.driver.current_url
            assert word in att, logging.warning("断言失败：URL为预期不一致 | URL: {}".format(att))
            logging.info("断言成功：URL为预期一致 | URL: {}".format(att))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("值为True值断言")
    def assert_page_source(self, word):
        """当前断言页面不包含not found"""
        try:
            value = self.driver.page_source
            assert word not in value, logging.warning("断言失败：页面包含此标识 | 标识: {}".format(value))
            logging.info("断言成功：页面不包含此标识| 标识: {}".format(value))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("值为True值断言")
    def assert_select(self, element, word):
        """断言当前下拉选择值是否符合预期"""
        try:
            elements = self.driver.find_element(By.XPATH, element)
            select_object = Select(elements)
            value = select_object.first_selected_option.text
            assert word == value, logging.warning("断言失败：下拉选择框不是该值 | 当前值: {}".format(value))
            logging.info("断言成功：下拉选择框是该值| 当前值: {}".format(value))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("值为True值断言")
    def assert_filename(self, element, word):
        """断言当前下文件上传是否符合预期"""
        try:
            elements = self.driver.find_elements(By.XPATH, element)
            value = elements[0].get_attribute('value')

            assert word in value, logging.warning("断言失败：选择上传不是该文件 | 当前文件: {}".format(value))
            logging.info("断言成功：选择上传是该文件| 当前文件: {}".format(value))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("值为True值断言")
    def assert_domcolor(self, element, color):
        """断言当前颜色是否符合预期"""
        try:
            elements = self.driver.find_elements(By.XPATH, element)
            value = elements[0].value_of_css_property('color')
            logging.info(value)

            assert color == value, logging.warning("断言失败：颜色不符合预期 | 当前元素颜色: {}".format(value))
            logging.info("断言成功：颜色符合预期| 当前元素颜色: {}".format(value))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("值为True值断言")
    def assert_alerttext(self, element, content):
        """断言当前下文件上传是否符合预期"""
        try:
            self.driver.find_element(By.XPATH, element).click()
            alert = self.driver.switch_to.alert
            value = alert.text

            assert content == value, logging.warning("断言失败：弹窗内容不符合预期 | 当前弹窗内容: {}".format(value))
            logging.info("断言成功：弹窗内容符合预期 | 当前弹窗内容: {}".format(value))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("值为True值断言")
    def assert_control(self, element, result=True):
        """
        断言：页面是否存在控件
        @element：元素定位
        @result：断言结果，True表示断言存在； False表示断言不存在
        @choice：元素定位
        """
        control = Base(self.driver).element_exist(element)
        try:
            assert control is result, logging.warning('断言失败，元素：{}存在结果与期望结果：{}不符'.format(element, result))
            logging.info('断言成功，元素：{}存在结果为：{}'.format(element, result))
        except Exception as e:
            logging.error(e)
            raise


    """     数据库断言     """
class SQLAssert(object):
    def __init__(self, name, env, ini_name=None, values=None):  # 此处可以加入这个类中需要定义的参数
        self.name = name
        self.env = env
        self.ini_name = ini_name
        self.values = values

    @allure.step("值为True值断言")
    def assert_sql(self, word, sql):
        """页面是否存在某文字"""
        database = SQL(self.name, self.env, self.ini_name, self.values)
        sql_list = database.query_db(sql)
        sql_colum = []
        for i in sql_list:
            sql_colum.append(str(list(i.values())[0]))
        try:
            assert word in sql_colum, logging.warning("断言失败: 该内容不存在数据列表中 | word:{}".format(word))
            logging.info("断言成功: 该内容存在数据列表中 | word:{}".format(word))
        except Exception as e:
            logging.error(e)
            raise

    @allure.step("值为True值断言")
    def assert_sql_count(self, count, sql):
        """数据库查询结果条数"""
        database = SQL(self.name, self.env)
        sql_list = database.query_db(sql)
        # result = sql_list[0]["count(*)"]
        result = list(sql_list[0].values())[0]
        try:
            assert int(result) == count, logging.warning("断言失败: 数据库查询结果为{}行，页面查询结果为{}行".format(result, count))
            logging.info("断言成功: 数据库查询结果条数与页面查询结果一致")
        except Exception as e:
            logging.error(e)
            raise


if __name__ == "__main__":
    # print(value_assert_equal(1,2))
    # print(value_assert_Notequal(1,2))
    # print(value_assert_True(0))
    # print(value_assert_False(1))
    # print(value_assert_Is(2, 2))
    # print(value_assert_IsNot(2,2))
    # print(value_assert_IsNone(None))
    # print(value_assert_IsNoneNot(1))
    # print(value_assert_In(3, {3,2}))
    # print(value_assert_InNot(3, {3,2}))
    # print(value_assert_Instance("abc",str))
    # print(value_assert_IsInstanceNot(2,int))
    a = SQLAssert('DRP', 'test')
    print(a.assert_sql(word='刘勇', sql='select name_zh from uc_user where enable_flag=1'))
