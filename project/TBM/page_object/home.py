#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging

import logging
from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class HomePage(Base):
    """登录类"""
    def click_menu(self, metatitle, nestmenu):
        """点击菜单"""
        ele = self.element_text(user['当前菜单']).strip()
        if ele != nestmenu:
            try:
                self.is_click_tbm(user['meta-title'], metatitle)
                logging.info(f'点击一级菜单:{metatitle}')
                sleep(1)
                self.is_click_tbm(user['nest-menu'], nestmenu)
                logging.info(f'点击二级菜单:{nestmenu}')
                sleep(2)
                self.refresh()
            except Exception as e:
                logging.error(e)
                self.base_get_img()
                self.refresh()
                self.is_click_tbm(user['meta-title'], metatitle)
                logging.info(f'点击一级菜单:{metatitle}')
                sleep(1)
                self.is_click_tbm(user['nest-menu'], nestmenu)
                logging.info(f'点击二级菜单:{nestmenu}')
                sleep(2)
                self.refresh()


if __name__ == '__main__':
    pass
