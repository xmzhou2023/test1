import os
import re

# 项目目录
import pymysql

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 当前项目目录
PEROJECT_PATH = os.path.join(BASE_DIR, 'project')

sql = {'host': '10.250.113.16', 'port': 3306, 'user_name': 'root', 'password': '123456', 'db_name': 'TranDesk',
       'drive': 'mysql'}

def get_db_conn():
    conn = pymysql.connect(
        host=sql['host'],  # 数据库地址
        port=sql['port'],  # 端口（配置文件传入的是字符串格式，所以这里取值的时候，用getint的方法 ）
        user=sql['user_name'],  # 账号
        passwd=str(sql['password']),  # 密码
        db=sql['db_name'],  # 要操作的数据库名
        charset='utf8')  # 指定编码格式
    return conn

# 更改
def change_db(pro_sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    try:
        for sql_excute in pro_sql:
            cur.execute(sql_excute)  # 执行sql
            conn.commit()  # 提交更改
    except Exception as e:
        print(e)
        conn.rollback()  # 回滚
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接0

def get_FolderName(filepath):
    pro_list = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s' % (allDir))
        pro_list.append(child)
    return pro_list

def get_ModuleName(filepath):
    py_list = []
    module = os.listdir(filepath)
    for i in module:
        if i != '__pycache__' and i != 'conftest.py' and i != 'failures':
            py_list.append(i)
    return py_list

def change_pylist_modulelist(py_name):
    module = os.path.splitext(py_name)[0]
    return module


def get_PyClass(filepath):
    class_list = {}
    with open(filepath, "r", encoding='utf-8') as file:
        feature_name = ''  # 初始化模块描述
        for line in file.readlines():
            """获取模块编码(py脚本名)feature"""
            if re.match("@allure.feature\((.*)\)", line):
                feature_name = re.match("@allure.feature\((.*)\)", line)
                feature_name = feature_name.group(1)
                # print(feature_name)

            """获取场景编码(class类名)class"""
            if re.match("class (.*):", line):
                class_name = re.match("class (.*):", line)
                class_name = class_name.group(1)
                if '()' in class_name:
                    class_name = class_name.replace('()','')
                class_list[class_name] = {}
                class_list[class_name]['att'] = {}
                # print(class_name)

            """获取场景中文名class"""
            if re.match("    @allure.story\(\"(.*)\"\)", line):
                story_name = re.match("    @allure.story\(\"(.*)\"\)", line)
                story_name = story_name.group(1)
                class_list[class_name]['att'] = story_name
                mark_name = [] # 初始化mark_name
                # print(story_name)

            """获取用例中文名title"""
            if re.match("    @allure.title\(\"(.*)\"\)", line):
                title_name = re.match("    @allure.title\(\"(.*)\"\)", line)
                title_name = title_name.group(1)
                # print(title_name)

            """获取用例概述description"""
            if re.match("    @allure.description\(\"(.*)\"\)", line):
                description_name = re.match("    @allure.description\(\"(.*)\"\)", line)
                description_name = description_name.group(1)
                # print(description_name)

            """获取用例等级severity"""
            if re.match("    @allure.severity\(\"(.*)\"\)", line):
                severity_name = re.match("    @allure.severity\(\"(.*)\"\)", line)
                severity_name = severity_name.group(1)
                # print(severity_name)

            """获取用例标签mark"""
            if re.match("    @pytest.mark.([^\s]+)", line):
                mark_value = re.match("    @pytest.mark.([^\s]+)", line)
                mark_value = mark_value.group(1)
                if 'run' not in mark_value and 'skip' not in mark_value:
                    mark_name.append(mark_value)
                    # print(mark_name)

            """获取用例中文(def用例名)def"""
            if re.match("    def (.*)\(", line):
                function_name = re.match("    def (.*)\(", line)
                function_name = function_name.group(1)
                # print(function_name)
                try:
                    class_list[class_name]['value'][function_name] = {}
                except KeyError as e:
                    class_list[class_name]['value'] = {}
                    class_list[class_name]['value'][function_name] = {}
                try:
                    class_list[class_name]['value'][function_name]['title'] = title_name
                    class_list[class_name]['value'][function_name]['description'] = description_name
                    class_list[class_name]['value'][function_name]['severity'] = severity_name
                    class_list[class_name]['value'][function_name]['mark'] = mark_name
                except UnboundLocalError as e:
                    print('请检查指定代码格式{}'.format(class_list))
    return class_list, feature_name

def get_Data():
    data_list = {}
    pro_list = get_FolderName(PEROJECT_PATH)
    # print(pro_list)     # 打印项目列表名
    for pro_name in pro_list:
        data_list[pro_name] = {}
        module_path = os.path.join(BASE_DIR, 'project', pro_name, 'test_case')
        py_list = get_ModuleName(module_path)
        # print(module_list)      # 打印模块列表名
        for py_name in py_list:
            data_list[pro_name][change_pylist_modulelist(py_name)] = {}
            py_path = os.path.join(BASE_DIR, 'project', pro_name, 'test_case', py_name)
            data_list[pro_name][change_pylist_modulelist(py_name)]['att'] = {}
            data_list[pro_name][change_pylist_modulelist(py_name)]['value'] = {}
            data_all = get_PyClass(py_path)
            data_list[pro_name][change_pylist_modulelist(py_name)]['value'] = data_all[0]
            data_list[pro_name][change_pylist_modulelist(py_name)]['att'] = data_all[1]
    return data_list  # 封装好的数据

def sync_Data(data_list):
    sql_execute = []
    case_mark = {
        'smoke': 1,
        'RT': 2,
        'UT': 3,
    }

    case_level = {
        'blocker': 1,
        'critical': 2,
        'normal': 3,
        'minor': 4,
        'trivial': 5,
    }

    sql_execute.append("TRUNCATE ts_project")
    sql_execute.append("TRUNCATE ts_module")
    sql_execute.append("TRUNCATE ts_testtype")
    sql_execute.append("TRUNCATE scene")
    sql_execute.append("TRUNCATE ts_case")
    sql_execute.append("TRUNCATE ts_casemark_detail")

    # 项目数据
    for pro_id, pro_code in enumerate(data_list.keys(), 1):
        sql_pro = "INSERT INTO ts_project(project_name,created_by,updated_by,manager_id,project_team,enabled_flag) VALUES ('{}',1,1,1,1,1)".format(pro_code)
        sql_execute.append(sql_pro)

        # 模块数据
        for mod_id, mod_code in enumerate(data_list[pro_code], 1):
            module_zh = data_list[pro_code][mod_code]['att'].replace('\"', '')
            sql_mod = "INSERT INTO ts_module(module_code,module_name,p_id,created_by,updated_by,enabled_flag) VALUES ('{}','{}','{}','自动化平台','自动化平台',1)".format(mod_code,module_zh ,pro_id)
            sql_execute.append(sql_mod)

            # 添加模块分类

            sql_type_FT = "INSERT INTO ts_testtype(testtype_name,testtype_des,m_id,created_by,updated_by,enabled_flag) VALUES ('接口测试','FT',{},'自动化平台','自动化平台',1)".format(mod_id)
            sql_execute.append(sql_type_FT)
            sql_type_ST = "INSERT INTO ts_testtype(testtype_name,testtype_des,m_id,created_by,updated_by,enabled_flag) VALUES ('场景测试','ST',{},'自动化平台','自动化平台',1)".format(mod_id)
            sql_execute.append(sql_type_ST)
            sql_type_UT = "INSERT INTO ts_testtype(testtype_name,testtype_des,m_id,created_by,updated_by,enabled_flag) VALUES ('单元测试','UT',{},'自动化平台','自动化平台',1)".format(mod_id)
            sql_execute.append(sql_type_UT)


            # 场景数据
            for sce_id, sce_code in enumerate(data_list[pro_code][mod_code]['value'], 1):
                sce_zh = data_list[pro_code][mod_code]['value'][sce_code]['att'].replace('\"', '')
                # print(pro_code,mod_code)
                sql_sce = "INSERT INTO scene(scene_code,scene_name,m_id,scene_level,created_by,updated_by,enabled_flag) VALUES('{}','{}',{},1,'自动化平台','自动化平台',1)".format(sce_code, sce_zh, mod_id)
                sql_execute.append(sql_sce)

                # 用例数据
                for case_id, case_code in enumerate(data_list[pro_code][mod_code]['value'][sce_code]['value'], 1):

                    # 添加用例描述
                    case_zh = data_list[pro_code][mod_code]['value'][sce_code]['value'][case_code]['title'].replace('\"', '')
                    case_desc = data_list[pro_code][mod_code]['value'][sce_code]['value'][case_code]['description'].replace('\"', '')
                    case_desc = '123'

                    # 设置用例等级
                    severity_level = data_list[pro_code][mod_code]['value'][sce_code]['value'][case_code]['severity'].replace('\"', '')
                    case_level_id = case_level[severity_level]

                    # 添加用例数据
                    sql_case = "INSERT INTO ts_case(case_code,case_name,case_des,case_status,s_id,case_level,manager_id,created_by,updated_by,enabled_flag,meta_status) VALUES('{}','{}','{}',1,'{}',{},1,'自动化平台','自动化平台',1,'unexecuted')".format(case_code, case_zh, case_desc, sce_id, case_level_id)
                    sql_execute.append(sql_case)

                    # 添加用例等级
                    severity_level = data_list[pro_code][mod_code]['value'][sce_code]['value'][case_code]['mark']
                    for i in severity_level:
                        case_level_id = case_mark[i]
                        sql_severity = "INSERT INTO ts_casemark_detail(case_id,case_mark_id,created_by,updated_by,enabled_flag) VALUES({},{},1,1,1)".format(case_id, case_level_id)
                        sql_execute.append(sql_severity)

    change_db(sql_execute)

if __name__ == '__main__':
    sync_Data(get_Data())
