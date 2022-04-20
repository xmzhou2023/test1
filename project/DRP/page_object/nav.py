from public.public_base.Basics import Base, sleep
from libs.common.read_element import Element
from libs.common.logger_ui import log

nav = Element('nav')

class NavPage(Base):
    """Nav类"""

    def click_gotonav(self, *content):
        """前往菜单"""
        level = []
        navstr = ""
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        log.info(level)
        for i in range(len(content)):
            log.info(nav[level[i]])
            self.is_click(nav[level[i]])
        sleep(10)

if __name__ == '__main__':
    pass
