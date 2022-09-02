import logging
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

    error_list = 0
    for pro in pro_list:
        ELEMENT_PATH = os.path.join(PEROJECT_PATH, pro, 'page_element')
        for i in os.listdir(ELEMENT_PATH):
            _path = os.path.join(ELEMENT_PATH, i)
            if os.path.isfile(_path):
                with open(_path, encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    try:
                        if data.values is None:
                            print('【提示】【%s】项目【%s】模块格式不符，亲再检查下格式哦！' % (pro, i))
                            error_list += 1

                        for k in data.values():
                            if '==' not in k:
                                print('【提示】【%s】项目【%s】模块【%s】元素xpath格式不符，亲再检查下格式哦！' % (pro, i, k))
                                error_list += 1

                            pattern, value = k.split('==')

                            if pattern not in LOCATE_MODE:
                                print('【提示】【%s】项目【%s】模块【%s】元素没有指定类型，亲再检查下格式哦！' % (pro, i, k))
                                error_list += 1
                            if pattern == 'xpath':
                                if '/' not in value:
                                    print('【提示】【%s】项目【%s】模块【%s】元素xpath类型与值不配，亲再检查下格式哦！' % (pro, i, k))
                                    error_list += 1
                            if pattern == 'css':
                                if '/' not in value:
                                    print('【提示】【%s】项目【%s】模块【%s】元素css类型与值不配' % (pro, i, k))
                                    error_list += 1
                            if pattern == 'id':
                                if '/' not in value:
                                    print('【提示】【%s】项目【%s】模块【%s】元素css类型与值不配' % (pro, i, k))
                                    error_list += 1
                            if pattern in ('id', 'name', 'css', 'class', 'text', 'partial-link', 'tag'):
                                print('【提示】【%s】项目【%s】模块【%s】元素类型与值不匹配，亲再检查下格式哦！' % (pro, i, k))
                                error_list += 1
                    except:
                        error_list += 1


    end_time = timestamp()
    print("【结束】恭喜您，元素库文件自检程序完成！用时%.3f秒！" % (end_time - start_time))
    if error_list != 0:
        raise AttributeError('【提示】请尽快检查并修改自己的用例，如有异议，请尽快联系我们，谢谢！')

if __name__ == '__main__':
    # print(get_FolderName(PEROJECT_PATH))
    inspect_element()