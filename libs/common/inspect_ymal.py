import os
import sys

import yaml
from libs.common.time_ui import timestamp
from libs.config.conf import PEROJECT_PATH, LOCATE_MODE

def get_FolderName(filepath):
    pro_list = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s' % (allDir))
        pro_list.append(child)
    return pro_list

def inspect_element():
    """审查所有的元素是否正确"""
    print("【开始】请稍候，元素定位库文件自检程序开始！" )
    start_time = timestamp()
    pro_list = get_FolderName(PEROJECT_PATH)

    for pro in pro_list:
        ELEMENT_PATH = os.path.join(PEROJECT_PATH, pro, 'page_element')
        for i in os.listdir(ELEMENT_PATH):
            _path = os.path.join(ELEMENT_PATH, i)
            if os.path.isfile(_path):
                with open(_path, encoding='utf-8') as f:
                    data = yaml.safe_load(f)

                    assert data.values is None, '【提示】【%s】项目【%s】模块格式不符，亲再检查下格式哦！' % (pro, i)

                    for k in data.values():
                        assert '==' in k, '【提示】【%s】项目【%s】模块中【%s]元素xpath格式不符，亲再检查下格式哦！' % (pro, i, k)

                        pattern, value = k.split('==')

                        if pattern not in LOCATE_MODE:
                            raise AttributeError('【提示】【%s】项目【%s】模块中【%s]元素没有指定类型，亲再检查下格式哦！' % (pro, i, k))
                        if pattern == 'xpath':
                            assert '/' in value, '【提示】【%s】项目【%s】模块中【%s]元素xpath类型与值不配，亲再检查下格式哦！' % (pro, i, k)
                        if pattern == 'css':
                            assert '/' not in value, '【%s】项目【%s】模块中【%s]元素css类型与值不配' % (pro, i, k)
                        if pattern in ('id', 'name', 'class'):
                            assert value, '【提示】【%s】项目【%s】模块中【%s]元素类型与值不匹配，亲再检查下格式哦！' % (pro, i, k)

    end_time = timestamp()
    print("【结束】恭喜您，元素库文件自检程序完成！用时%.3f秒！" % (end_time - start_time))


if __name__ == '__main__':
    # print(get_FolderName(PEROJECT_PATH))
    inspect_element()