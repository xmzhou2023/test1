import csv
import os
from libs.config.conf import PUBLIC_DATA_PATH

path = os.path.join(PUBLIC_DATA_PATH, 'account.csv')

def readCsv(path):
    """列表的读取方式，读取csv的文件内容"""
    lists = []
    with open(path, encoding='utf-8') as f:
        reader = csv.reader(f)
        for item in reader:  # 加到列表用append方法。
            lists.append(item)
    return lists  # 每读取完一行就返回整个列表


def readCsvList(path):
    """列表的读取方式，读取csv的文件内容"""
    lists = []
    with open(path, encoding='utf-8') as f:
        reader = csv.reader(f)
        # 不读取data.csv文件的第一行
        next(reader)  # 循环列表
        for item in reader:  # 加到列表用append方法。
            lists.append(item)
        # return lists #读取完第一行，返回第一行。
    return lists  # 每读取完一行就返回整个列表


def readCsvDict(path):
    """字典的读取方式，读取csv的文件内容"""
    lists = []  # 读取的文件中有时候会出现 "\ufeff" 非法字符，这个时候需要改变编码方式 'UTF-8'为 'UTF-8-sig'
    with open(path, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for item in reader:
            lists.append(dict(item))
            # return lists #读取完第一行，返回第一行。
    return lists  # 每读取完一行就返回整个列表


if __name__ == '__main__':
    # 直接输出，检查代码是否能正常运行
    print(readCsv(path))
    print(readCsvList(path))
    print(readCsvDict(path))
    print(readCsvDict(path)[0])