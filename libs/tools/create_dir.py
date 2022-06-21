from libs.common.read_csv import *
from libs.config.conf import PEROJECT_PATH
from libs.common.logger_ui import log
import csv
import os
# 创建文件依据
path = os.path.join('template/modle_name.csv')

# 引用模板位置
CASE_TEMPLATE_PATH = os.path.join('template/case_template.py')
OBJECT_TEMPLATE_PATH = os.path.join('template/object_template.py')
ELEMENT_TEMPLATE_PATH = os.path.join('template/element_template.yaml')

# 文件下载路径
CASE_PATH = os.path.join(PEROJECT_PATH, 'test_case/')
OBJECT_PATH = os.path.join(PEROJECT_PATH, 'page_object/')
ELEMENT_PATH = os.path.join(PEROJECT_PATH, 'page_element/')

def read_file(filepaxh):
    with open(filepaxh, 'r', encoding='utf-8') as file:
        txt = file.read()
        file.close()
    return txt

def text_create(name, type="case"):
    if type == "element":
        desktop_path = ELEMENT_PATH
        full_path = desktop_path + name + '.yaml'   # 创建元素定位库yaml文件
        msg = read_file(ELEMENT_TEMPLATE_PATH)
    elif type == "object":
        desktop_path = OBJECT_PATH
        full_path = desktop_path + name + '.py'     # 创建页面对象
        msg = read_file(OBJECT_TEMPLATE_PATH)
    else:
        desktop_path = CASE_PATH  # 新创建的txt文件的存放路径
        full_path = desktop_path + name + '.py'
        msg = read_file(CASE_TEMPLATE_PATH)

    if not os.path.exists(full_path) :
        file = open(full_path, 'w', encoding='utf-8')    # w 的含义为可进行读写
        file.write(msg)        #file.write()为写入指令
        file.close()
        log.info("生成成功: 模块文件名为 | {} ".format(name))

def generate_module(file_type):
        list = readCsv(path)
        for i in range(len(list)):
            text_create(name=list[i][0],type=file_type)

if __name__ == '__main__':
    generate_module("element")



