'''
进行excel数据驱动,excel数据驱动类底层代码
'''
import openpyxl
from openpyxl.styles import Font,colors,Alignment
from libs.common.logger_ui import log
# from Common.WebKey import WebKey

# 读取excel
log.info('正在读取Excel文件')
excel = openpyxl.load_workbook('../../project/DRP/workflow/TestCase.xls')
# 获取sheet页
sheets = excel.sheetnames
# 遍历sheet页
for sheet in sheets:
    log.info('正在读取表格{0}'.format(sheet))
    sheet_temp = excel[sheet]
    # 判断该表格是否为测试用例：根据表格sheet名是否含有testcase
    if 'testcase' in sheet:
        log.info('正在执行{}'.format(sheet_temp['A1'].value))
        # 遍历sheet页单元格
        for values in sheet_temp.values:
            # 判断用例是否已经执行过,有执行结果的代表，用例已经执行过了
            if 'Pass' or 'Fail' not in values[8]:
                # 读取用例执行部分内容
                if type(values[0]) is int:
                    log.info('操作描述：{}'.format(values[6]))
                    # print(values)
                    # 定义字典
                    data = {}
                    # 元素定位方法
                    data['name']=values[2]
                    # 元素定位路径
                    data['value']=values[3]
                    # 元素变量
                    data['variable']=values[4]
                    # 输入的文本值
                    data['txt']=values[5]
                    # print(data)
                    # 优化数据,删除为None的数据
                    for key in list(data.keys()):
                        if data[key] is None:
                            del data[key]
                    # print(data)
                    # 调用关键字执行不同操作
                    if values[1] == 'open_browser':
                        wt = WebKey(values[5])
                     # 如果是断言，需要写入，判断断言是否成功，成功True,失败False
                    elif 'assert' in values[1]:
                        # 断言函数有返回
                        status = getattr(wt ,values[1])(**data)
                        if status:
                            sheet_temp.cell(row=values[0] +2,column=8).value ='Pass'
                            # sheet_temp.cell(row=values[0] +2, column=8).fill = PatternFill("solid", fgColor="#00FA9A")
                            sheet_temp.cell(row=values[0] +2, column=8).font =Font(color=colors.BLUE,bold=True)
                            sheet_temp.cell(row=values[0] +2, column=8).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
                        else:
                            sheet_temp.cell(row=values[0] +2,column=8).value ='Fail'
                            # sheet_temp.cell(row=values[0] +2,column=8).fill = PatternFill("solid", fgColor="#FF0000")
                            sheet_temp.cell(row=values[0] +2, column=8).font = Font(color='#A52A2A',bold=True)
                            sheet_temp.cell(row=values[0] +2, column=8).alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
                    else:
                        getattr(wt,values[1])(**data)
            else:
                break
    else:
        log.info('该表格内容不是测试用例')
# 写入后进行保存
log.info('自动化用例执行完毕')
excel.save('../workflow/TestCase.xls')