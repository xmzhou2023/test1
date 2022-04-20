from libs.common import read_excel
from libs.common import action
from libs.config.conf import TESTCASE_PATH

def key_func():
    key_word = action.KeyWord()
    for step in read_excel.excel(TESTCASE_PATH):
        print(step)
        if step['步骤名'] is None:
            continue
        else:
            步骤名 = step['步骤名'] # 变量名可以是unicode,包括中文
            关键字 = step['关键字']
            参数 = step['参数']
            print(f"{步骤名}...", end='') # 取消换行

            # 面向对象中: 反射
            # - 反射
            # - 鸭子类型
            f = getattr(key_word, f"key_{关键字}") # 关键字变为python函数
            f(*参数) # 参数是打包后的，传递时需要先解包
            # 函数后面加括号，表示对函数的调用

            print("OK") # 取消换行,表求步骤结束

if __name__ == '__main__':
    key_func()