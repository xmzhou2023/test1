import pywinauto
from pywinauto.keyboard import send_keys
from libs.common.time_ui import *

def Improt_File_n(pathDIR,path_filename):
    '''

    :param pathDIR: 导入的文件路径
    :param path_filename: 文件名
    :param mumo_lis: 异常备注
    :return:
    '''
    try:
        # 打开文件选择框
        # 创建操作桌面的对象
        app = pywinauto.Desktop()
        # 获取弹窗的窗口标题
        dlg = app["打开"]
        # 打印窗口的所有控件信息
        # dlg.print_ctrl_ids()

        # 选择文件地址输入控件
        dlg["Toolbar3"].click()
        send_keys(pathDIR)
        send_keys("{VK_RETURN}")
        sleep(2)

        # 输入文件名
        dlg["文件名(&N):Edit"].type_keys(path_filename)
        send_keys("{VK_RETURN}")
        sleep(2)
    except Exception as e:
        print('文件导入失败')
        raise Exception(e)




if __name__ == '__main__':
    pass
