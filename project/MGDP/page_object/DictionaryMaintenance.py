# -*- coding: utf-8 -*-
# @Time    : 2022-08-02 17:15
# @Author  : wuqi
# @Email   : qi.wu@transsion.com
# @File    : BasicInfo_BoardParametersSetting.py
# @Software: PyCharm
import logging
import os
import time

import allure
from ..test_case.conftest import *
from libs.common.read_element import Element
from public.base.basics import Base

object_name = os.path.basename(__file__).split('.')[0]
basic = Element(pro_name, object_name)


class BoardParametersSetting(Base):
    """看板参数配置"""

    @allure.step("选择工段")
    def choice_workshop_section(self, content):
        self.is_click(basic["工段下拉选择框"])
        self.is_click(basic["下拉选项"], content)


