'''
#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/5/18 15:00
# @Author : 李小素
# @File : test_area_cfg.py
# @Software: PyCharm
'''

from project.IPM.login.login import *


class ProcessHome(Base):

    def __init__(self,driver,filename):
        super(ProcessHome, self).__init__(driver)
        self.chome = Element('IPM',filename)


    '''项目管理'''
    def click_home(self,public,title=None):
        '''点击查询按钮'''
        self.is_click(self.chome[public],title)
        sleep(2)

    def click_process(self,process):
        '''选择流程'''
        self.switch_window(0)
        self.is_click(self.chome[process])
        sleep(3)
