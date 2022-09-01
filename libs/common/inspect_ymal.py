import os
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
    start_time = timestamp()
    pro_list = get_FolderName(PEROJECT_PATH)
    for pro in pro_list:
        ELEMENT_PATH = os.path.join(PEROJECT_PATH, pro, 'page_element')
        for i in os.listdir(ELEMENT_PATH):
            _path = os.path.join(ELEMENT_PATH, i)
            if os.path.isfile(_path):
                with open(_path, encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    for k in data.values():
                        assert '==' in k, '【%s】项目【%s】模块中【%s]元素xpath格式不符' % (pro, i, k)

                        pattern, value = k.split('==')

                        if pattern not in LOCATE_MODE:
                            raise AttributeError('【%s】项目【%s】模块中【%s]元素没有指定类型' % (pro, i, k))
                        if pattern == 'xpath':
                            assert '/' in value, '【%s】项目【%s】模块中【%s]元素xpath类型与值不配' % (pro, i, k)
                        # if pattern == 'css':
                        #     assert '/' not in value, '【%s】项目【%s】模块中【%s]元素css类型与值不配' % (pro, i, k)
                        if pattern in ('id', 'name', 'class'):
                            assert value, '【%s】项目【%s】模块中【%s]元素类型与值不匹配' % (pro, i, k)
    end_time = timestamp()
    print("校验元素done！用时%.3f秒！" % (end_time - start_time))


if __name__ == '__main__':
    # print(get_FolderName(PEROJECT_PATH))
    inspect_element()