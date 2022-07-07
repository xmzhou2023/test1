import logging
from libs.common.read_element import Element
from libs.common.time_ui import sleep
from public.base.basics import Base
from ..test_case.conftest import *

object_name = os.path.basename(__file__).split('.')[0]
user = Element(pro_name,object_name)

class MenuPage(Base):
    """MenuPage类"""
    def click_gotomenu(self, *content):
        """前往左侧菜单栏"""
        level = []
        navstr = ""
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        for i in range(len(content)):
            logging.info(user[level[i]])
            sleep(2)
            self.scroll_into_view(user[level[i]])
            sleep(2)
            self.is_click(user[level[i]])
        sleep(4)


if __name__ == '__main__':
    pass