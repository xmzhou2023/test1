from public.base.Basics import Base, sleep
from libs.common.read_element import Element

nav = Element('center_Component')

class NavPage(Base):
    """Nav类"""

    def click_gotonav(self, *content):
        """前往菜单"""
        level = []
        navstr = ""
        for i in range(len(content)):
            navstr = navstr + '->' + content[i]
            level.append(navstr[2:])
        for i in range(len(content)):
            self.is_click(nav[level[i]])
        sleep(5)

if __name__ == '__main__':
    pass
