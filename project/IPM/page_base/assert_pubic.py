
'''
#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/5/18 16:00
# @Author : 李小素
# @File : test_area_cfg.py
# @Software: PyCharm
# @title:个人中心
'''
import logging

from libs.common.logger_ui import log
from public.base.assert_ui import *
from project.IPM.page_base.basics_IPM import *
from project.IPM.page_base.db_mysql import *




#断言
class AssertMode(PubicMethod):

    @allure.step("断言")
    def assert_toast(self,element, content=None):
        # att = self.element_text(user['toast提示'])
        try:
            att = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.filelist.yaml_read(element)))).text
            self.base_get_img()
            logging.info('获取toast提示语：{}'.format(att))
            try:
                if content is None:
                    assert '请求成功' in att or '审核通过' in att or '操作成功' in att or '处理成功' in att
                    logging.info('断言成功，toast提示为：{}'.format(att))
                else:
                    assert content in att
                    logging.info('断言成功，toast提示为：{}'.format(att))
            except:
                logging.error('断言失败，实际提示为：{}'.format(att))
                raise
        except:
            logging.error('断言失败，未获取到toast提示语/toast提示语错误')
            raise


    @allure.step("断言")
    def assert_toast_not(self, element,content=None):
        # att = self.element_text(user['toast提示'])
        try:
            att = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.filelist.yaml_read(element)))).text
            self.base_get_img()
            logging.info('获取toast提示语：{}'.format(att))
            try:
                if content is None:
                    assert '请求成功' not in att or '审核通过' not in att or '操作成功' not in att or '处理成功' not in att
                    logging.info('断言成功，toast提示为：{}'.format(att))
                else:
                    assert content not in att
                    logging.info('断言成功，toast提示为：{}'.format(att))
            except:
                logging.error('断言失败，实际提示为：{}'.format(att))
                raise
        except:
            logging.error('断言失败，未获取到toast提示语/toast提示语错误')
            raise

    @allure.step("断言")
    def assert_IPM(self,att, content=None):

        try:
            if content is None:
                assert '请求成功' in att or '审核通过' in att or '操作成功' in att or '处理成功' in att
                logging.info('断言成功，toast提示为：{}'.format(att))
            else:
                assert content in att
                logging.info('断言成功，toast提示为：{}'.format(att))
        except:
            logging.error('断言失败，实际提示为：{}'.format(att))
            raise

    def element_not_found(self,locator,result=False):
        '''
        locator：元素
        test:断言元素不存在
        '''
        control = Base(self.driver).element_exist(locator)
        try:
            assert  control is result,logging.warning(f'断言失败，元素：{locator}存在结果与期望结果：{result}不符')
            logging.info((f'断崖成功，元素：{locator}存在结果为：{result}'))

        except Exception as e:
            logging.info(e)
            raise




if __name__ == '__main__':
    pass