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

    error_list = []
    for pro in pro_list:
        ELEMENT_PATH = os.path.join(PEROJECT_PATH, pro, 'page_element')
        for i in os.listdir(ELEMENT_PATH):
            _path = os.path.join(ELEMENT_PATH, i)
            if os.path.isfile(_path):
                with open(_path, encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    try:
                        if data is None:
                            error_list.append('【%s】项目【%s】模块格式不符' % (pro, i))

                        for k in data.values():
                            if '==' not in k:
                                error_list.append('【%s】项目【%s】模块【%s】元素xpath格式不符' % (pro, i, k))

                            pattern, value = k.split('==')


                            if pattern not in LOCATE_MODE:
                                error_list.append('【%s】项目【%s】模块【%s】元素没有指定类型' % (pro, i, k))

                            if pattern in ('id', 'name', 'css', 'class', 'text', 'partial-link', 'tag'):
                                continue

                            if pattern == 'xpath':
                                if '/' not in value:
                                    error_list.append('【%s】项目【%s】模块【%s】元素xpath类型与值不配！' % (pro, i, k))

                            # if pattern == 'css':
                            #     if '/' not in value:
                            #         print('【提示】【%s】项目【%s】模块【%s】元素css类型与值不配' % (pro, i, k))
                            #         error_list += 1

                            # if pattern == 'id':
                            #     if '/' not in value:
                            #         print('【提示】【%s】项目【%s】模块【%s】元素css类型与值不配' % (pro, i, k))
                            #         error_list += 1
                    except:
                        continue


    end_time = timestamp()
    print("【结束】恭喜您，元素库文件自检程序完成！用时%.3f秒！" % (end_time - start_time))
    if len(error_list) != 0:
        raise AttributeError('\n%s\n【提示】请尽快检查并修改自己的用例，如有异议，请尽快联系我们，谢谢！' % error_list)

if __name__ == '__main__':
    # print(get_FolderName(PEROJECT_PATH))
    inspect_element()