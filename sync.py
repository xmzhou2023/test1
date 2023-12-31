# -*- coding=utf-8 -*-
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from time import sleep

# 项目目录
import pymysql

from libs.common.read_config import ReadConfig

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 当前项目目录
PEROJECT_PATH = os.path.join(BASE_DIR, 'project')

sql = ''

def run_env(env_name):
    global sql
    if env_name == 'uat':
        sql = {'host': '10.250.113.16', 'port': 3306, 'user_name': 'root', 'password': '123456', 'db_name': 'TranDesk',
               'drive': 'mysql'}
    else:
        sql = {'host': '10.250.101.58', 'port': 3306, 'user_name': 'root', 'password': '123456', 'db_name': 'TranTest',
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
def change_db(sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    try:
        for sql_excute in sql:
            cur.execute(sql_excute)  # 执行sql
        conn.commit()  # 提交更改
    except Exception as e:
        print(e)
        conn.rollback()  # 回滚
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接0

# 删除
def delete_db(sql):
    conn = get_db_conn()                            # 获取连接
    cur = conn.cursor()                             # 建立游标
    try:
        for sql_excute in sql:
            cur.execute(sql_excute)  # 执行sql
        conn.commit()  # 提交更改                           # 提交更改
    except Exception as e:
        conn.rollback()                             # 回滚
    finally:
        cur.close()                                 # 关闭游标
        conn.close()                                # 关闭连接0

# 查询
def query_db(pro_sql):
    conn = get_db_conn()                                  # 获取连接
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 建立游标
    cur.execute(pro_sql)                                      # 执行sql
    conn.commit()
    result = cur.fetchall()                               # 获取所有查询结果
    cur.close()                                           # 关闭游标
    conn.close()                                          # 关闭连接
    return result                                         # 返回结果


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
        if i != '__pycache__' and i != 'conftest.py' and i != 'failures' and i != 'login.py':
            py_list.append(i)
    return py_list

def get_yamlName(filepath):
    yaml_list = []
    module = os.listdir(filepath)
    for i in module:
        if i != '__pycache__':
            yaml_list.append(i)
    return yaml_list

def change_pylist_modulelist(py_name):
    module = os.path.splitext(py_name)[0]
    return module

def get_YamlTest(filepath):
    try:
        with open(filepath, "r", encoding='utf-8', errors='ignore') as file:
            lines = file.read()
            return lines
    except:
        return None
def get_PyClass(filepath):
    class_list = {}
    with open(filepath, "r", encoding='utf-8', errors='ignore') as file:
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
                story_name = story_name.replace('\\\\', '\\')
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
                if 'run' not in mark_value and 'skip' not in mark_value and 'usefixtures(' not in mark_value and 'parametrize(' not in mark_value and 'xfail' not in mark_value:
                    mark_name.append(mark_value)
                    # print(mark_name)

            """获取用例中文(def用例名)def"""
            if re.match("    def (.*)\(", line):
                function_name = re.match("    def (.*)\(", line)
                function_name = function_name.group(1)
                # print(function_name)
                if '_fixture' in function_name:
                    continue
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
                    class_list[class_name]['value'][function_name]['status'] = 1
                except UnboundLocalError as e:
                    print('请检查指定代码格式{}'.format(class_list))
            """获取用例状态(是否是pass)def"""
            if re.match("        (.*)", line):
                status_name = re.match("        (.*)", line)
                status_name = status_name.group(1)
                if 'pass' == status_name:
                    class_list[class_name]['value'][function_name]['status'] = 0
                if 'robot = KeyWord(drivers)' == status_name:
                    class_list[class_name]['value'][function_name]['status'] = 2

    return class_list, feature_name

def get_env():

    env_list = {}
    pro_list = get_FolderName(PEROJECT_PATH)
    for pro_name in pro_list:
        env_list[pro_name] = {}
        env_path = os.path.join(BASE_DIR, 'project', pro_name, 'env')
        list = os.listdir(env_path)
        for env_name in list:
            # 当前环境目录
            ini = ReadConfig(pro_name, env_name)
            env_list[pro_name][env_name] = ini.url

    return env_list  # 封装好的数据

def get_Data():
    data_list = {}
    pro_list = get_FolderName(PEROJECT_PATH)
    # print(pro_list)     # 打印项目列表名
    for pro_name in pro_list:
        data_list[pro_name] = {}
        iter_path = os.path.join(BASE_DIR, 'project', pro_name, 'test_case')
        for iter_name in get_FolderName(iter_path):
            if iter_name == 'conftest.py' or iter_name == '__pycache__':
                continue
            module_path = os.path.join(iter_path, iter_name)
            yaml_path = os.path.join(BASE_DIR, 'project', pro_name, 'page_element')
            py_list = get_ModuleName(module_path)
            yaml_list = get_yamlName(yaml_path)
            data_list[pro_name][iter_name] = {}
            for py_name in py_list:
                data_list[pro_name][iter_name][change_pylist_modulelist(py_name)] = {}
                py_path = os.path.join(module_path, py_name)
                data_list[pro_name][iter_name][change_pylist_modulelist(py_name)]['att'] = {}
                data_list[pro_name][iter_name][change_pylist_modulelist(py_name)]['yaml'] = {}

                data_all = get_PyClass(py_path)
                data_list[pro_name][iter_name][change_pylist_modulelist(py_name)]['value'] = data_all[0]
                data_list[pro_name][iter_name][change_pylist_modulelist(py_name)]['att'] = data_all[1]
                yaml_text = ''

                for yaml_name in yaml_list:
                    py_name_yaml = py_name[0:py_name.rfind('.')]
                    if iter_name == 'BASE_CASE':
                        py_name_yaml = py_name_yaml[0:py_name_yaml.rfind('')]
                    if py_name_yaml == yaml_name[0:yaml_name.rfind('.')]:
                        yaml_path = os.path.join(BASE_DIR, 'project', pro_name, 'page_element', yaml_name)
                        ori_yaml_text = get_YamlTest(yaml_path)
                        yaml_text = ori_yaml_text.replace('\"', '\\"').replace("\'", "\\'")


                data_list[pro_name][iter_name][change_pylist_modulelist(py_name)]['yaml'] = yaml_text
    return data_list  # 封装好的数据

def sync_AllData(data_list, env_list):
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
    sql_execute.append("TRUNCATE ts_env")
    sql_execute.append("TRUNCATE ts_iteration")
    sql_execute.append("TRUNCATE ts_module")
    sql_execute.append("TRUNCATE ts_yaml")
    sql_execute.append("TRUNCATE ts_testtype")
    sql_execute.append("TRUNCATE scene")
    sql_execute.append("TRUNCATE ts_case")
    sql_execute.append("TRUNCATE ts_casemark_detail")

    # 项目数据
    iter_id = 1
    mod_id = 1
    sce_id = 1
    case_id = 1
    for pro_id, pro_code in enumerate(data_list.keys(), 1):
        sql_pro = "INSERT INTO ts_project(project_name,created_by,updated_by,manager_id,project_team,enabled_flag) VALUES ('{}',1,1,1,1,1)".format(pro_code)
        sql_execute.append(sql_pro)
        for iter_id, iter_code in enumerate(data_list[pro_code].keys(), 1):
            sql_iter = "INSERT INTO ts_iteration(iter_code,iter_name,p_id,enabled_flag) VALUES ('{}','{}',{},1)".format(iter_code, iter_code, pro_id)
            sql_execute.append(sql_iter)
            for mod_index, mod_code in enumerate(data_list[pro_code][iter_code], 1):
                module_zh = data_list[pro_code][iter_code][mod_code]['att'].replace('\"', '').replace("\'", "\\'")
                sql_mod = "INSERT INTO ts_module(module_code,module_name,i_id,created_by,updated_by,enabled_flag) VALUES ('{}','{}','{}','自动化平台','自动化平台',1)".format(mod_code, module_zh, iter_id)
                sql_execute.append(sql_mod)
                # 添加模块分类
                sql_type_FT = "INSERT INTO ts_testtype(testtype_name,testtype_des,m_id,created_by,updated_by,enabled_flag) VALUES ('接口测试','FT',{},'自动化平台','自动化平台',1)".format(mod_id)
                sql_execute.append(sql_type_FT)
                sql_type_ST = "INSERT INTO ts_testtype(testtype_name,testtype_des,m_id,created_by,updated_by,enabled_flag) VALUES ('场景测试','ST',{},'自动化平台','自动化平台',1)".format(mod_id)
                sql_execute.append(sql_type_ST)
                sql_type_UT = "INSERT INTO ts_testtype(testtype_name,testtype_des,m_id,created_by,updated_by,enabled_flag) VALUES ('单元测试','UT',{},'自动化平台','自动化平台',1)".format(mod_id)
                sql_execute.append(sql_type_UT)

                yaml_text = data_list[pro_code][iter_code][mod_code]['yaml']
                sql_yaml = "INSERT INTO ts_yaml(p_id,p_code,i_id,i_code,m_id,m_code,yaml_text,enabled_flag) VALUES ({},'{}',{},'{}',{},'{}','{}',1)".format(pro_id, pro_code, iter_id, iter_code, mod_id, mod_code, yaml_text)
                sql_execute.append(sql_yaml)
                print(sql_yaml)

                # 场景数据
                for sce_index, sce_code in enumerate(data_list[pro_code][iter_code][mod_code]['value'], 1):
                    sce_zh = data_list[pro_code][iter_code][mod_code]['value'][sce_code]['att'].replace('\"', '').replace("\'", "\\'")
                    sql_sce = "INSERT INTO scene(scene_code,scene_name,m_id,scene_level,created_by,updated_by,enabled_flag,scene_type) VALUES('{}','{}',{},1,'自动化平台','自动化平台',1,2)".format(sce_code, sce_zh, mod_id)
                    sql_execute.append(sql_sce)

                    # 用例数据
                    for case_index, case_code in enumerate(data_list[pro_code][iter_code][mod_code]['value'][sce_code]['value'], 1):
                        try:
                            # 添加用例描述
                            case_zh = data_list[pro_code][iter_code][mod_code]['value'][sce_code]['value'][case_code]['title'].replace("\\", "\\\\").replace('\"', '').replace("\'", "\\'")
                            case_desc = data_list[pro_code][iter_code][mod_code]['value'][sce_code]['value'][case_code]['description'].replace("\\", "\\\\").replace('\"', '').replace("\'", "\\'")

                            # 设置用例等级
                            severity_level = data_list[pro_code][iter_code][mod_code]['value'][sce_code]['value'][case_code]['severity'].replace('\"', '')
                            case_level_id = case_level[severity_level]

                            # 设置用例等级
                            case_status = data_list[pro_code][iter_code][mod_code]['value'][sce_code]['value'][case_code]['status']

                            # 添加用例数据
                            sql_case = "INSERT INTO ts_case(case_code,case_name,case_des,case_status,s_id,case_level,manager_id,created_by,updated_by,enabled_flag,meta_status) VALUES('{}','{}','{}',{},{},{},1,'自动化平台','自动化平台',1,'unexecuted')".format(case_code, case_zh, case_desc, case_status, sce_id, case_level_id)
                            # print(sql_case)
                            sql_execute.append(sql_case)

                            # 添加用例等级
                            severity_level = data_list[pro_code][iter_code][mod_code]['value'][sce_code]['value'][case_code]['mark']
                            for i in severity_level:
                                case_level_id = case_mark[i]
                                sql_severity = "INSERT INTO ts_casemark_detail(case_id,case_mark_id,created_by,updated_by,enabled_flag) VALUES({},{},1,1,1)".format(case_id, case_level_id)
                                sql_execute.append(sql_severity)

                        except IOError as e:
                            print("项目：{}, 迭代：{}, 模块：{},场景/story：{}，用例：{},异常：{}".format(pro_code, iter_code, mod_code, sce_code, case_code, e))

                        case_id = case_id + 1
                    sce_id = sce_id + 1
                mod_id = mod_id + 1
            iter_id = iter_id + 1

    for p_env_id, pro_code in enumerate(env_list.keys(), 1):
        for env_index, env_name in enumerate(env_list[pro_code], 1):
            env_url = env_list[pro_code][env_name]
            sql_env = "INSERT INTO ts_env(env_name,env_url,p_id,is_enable,created_by,updated_by,enabled_flag) VALUES('{}','{}',{},1,1,1,1)".format(env_name, env_url, p_env_id)
            sql_execute.append(sql_env)

    change_db(sql_execute)

def format_data(type, place, data):
    list = {}
    if type == 'pro':
        if place == 'id':
            for i in data:
                list[i['id']] = i['project_name']
        else:
            for i in data:
                list[i['project_name']] = i['id']
        return list
    if type == 'iter':
        if place == 'id':
            for i in data:
                list[i['id']] = i['iter_code']
        else:
            for i in data:
                list[i['iter_code']] = i['id']
        return list
    elif type == 'mod':
        if place == 'id':
            for i in data:
                list[i['id']] = i['module_code']
        else:
            for i in data:
                list[i['module_code']] = i['id']
        return list
    elif type == 'sce':
        if place == 'id':
            for i in data:
                list[i['scene_id']] = i['scene_code']
        else:
            for i in data:
                list[i['scene_code']] = i['scene_id']
        return list
    elif type == 'case':
        if place == 'id':
            for i in data:
                list[i['id']] = i['case_code']
        else:
            for i in data:
                list[i['case_code']] = i['id']
        return list

def algo_data(type, sql_data, data_list, parm=None):
    sql_execute = []
    list_sq = []
    list_py = []
    module_list_py = {}
    module_list_sq = {}

    if type == 'pro':

        for pro_id, pro_code in enumerate(data_list.keys(), 1):
            list_py.append(pro_code)

        for i in sql_data:
            list_sq.append(i['project_name'])

        del_data = list(set(list_sq).difference(set(list_py)))
        inp_data = list(set(list_py).difference(set(list_sq)))

        for project in del_data:
            print('更新后删除 [项目编码] {} '.format(project))
            sql_pro = "DELETE FROM ts_project WHERE project_name='{}'".format(project)
            sql_execute.append(sql_pro)

        change_db(sql_execute)

        sql_execute = []

        for project_name in inp_data:
            print('更新后增加 [项目编码] {} '.format(project_name))
            project_name = project_name.replace('\"', '').replace('\'', '')
            sql_pro = "INSERT INTO ts_project(project_name,created_by,updated_by,manager_id,project_team,enabled_flag) VALUES ('{}',1,1,1,1,1)".format(project_name)
            sql_execute.append(sql_pro)
        change_db(sql_execute)
    if type == 'iter':

        for iter_id, iter_code, in enumerate(data_list.keys(), 1):
            list_py.append(iter_code)

        for i in sql_data:
            list_sq.append(i['iter_code'])

        del_data = list(set(list_sq).difference(set(list_py)))
        inp_data = list(set(list_py).difference(set(list_sq)))

        for iter in del_data:
            print('更新后删除 [迭代编码] {} '.format(iter))
            sql_pro = "DELETE FROM ts_iteration WHERE iter_code ='{}' AND p_id={}".format(iter, parm)
            sql_execute.append(sql_pro)

        change_db(sql_execute)

        sql_execute = []

        for iter_code in inp_data:
            iter_name = iter_code.replace('\"','').replace('\'','')
            print('更新后增加 [迭代编码] {} [迭代名称] {}'.format(iter_code, iter_name))
            sql_pro = "INSERT INTO ts_iteration(iter_code,iter_name,p_id,enabled_flag) VALUES ('{}','{}',{},1)".format(iter_code, iter_name, parm)
            sql_execute.append(sql_pro)

        change_db(sql_execute)

    elif type == 'mod':

        for mod_id, mod_code, in enumerate(data_list.keys(), 1):
            list_py.append(mod_code)

        for i in sql_data:
            list_sq.append(i['module_code'])

        del_data = list(set(list_sq).difference(set(list_py)))
        inp_data = list(set(list_py).difference(set(list_sq)))

        for module in del_data:
            print('更新后删除 [模块编码] {} '.format(module))
            sql_pro = "DELETE FROM ts_module WHERE module_code ='{}' AND i_id={}".format(module, parm)
            sql_execute.append(sql_pro)

        change_db(sql_execute)

        sql_execute = []

        for module_code in inp_data:
            module_zh = data_list[module_code]['att'].replace('\"','').replace('\'','')
            print('更新后增加 [模块编码] {} [模块名称] {} '.format(module_code, module_zh))
            sql_pro = "INSERT INTO ts_module(module_code,module_name,i_id,created_by,updated_by,enabled_flag) VALUES ('{}','{}',{},'自动化平台','自动化平台',1)".format(module_code, module_zh, parm)
            sql_execute.append(sql_pro)

        change_db(sql_execute)

        # 初始化执行列表
        sql_execute = []

        # 模块查询sql,为了获取mod_id
        module_sql = "SELECT id,module_code from ts_module where i_id={}".format(parm)

        # 获取最新列表
        get_mod_id = format_data('mod', 'name', query_db(module_sql))

        for module_code in inp_data:
            mod_id = get_mod_id[module_code]

            print('更新后增加 [FT,ST,UT测试场景] {}'.format(module_code))
            # 添加模块分类
            sql_type_FT = "INSERT INTO ts_testtype(testtype_name,testtype_des,m_id,created_by,updated_by,enabled_flag) VALUES ('接口测试','FT',{},'自动化平台','自动化平台',1)".format(mod_id)
            sql_execute.append(sql_type_FT)
            sql_type_ST = "INSERT INTO ts_testtype(testtype_name,testtype_des,m_id,created_by,updated_by,enabled_flag) VALUES ('场景测试','ST',{},'自动化平台','自动化平台',1)".format(mod_id)
            sql_execute.append(sql_type_ST)
            sql_type_UT = "INSERT INTO ts_testtype(testtype_name,testtype_des,m_id,created_by,updated_by,enabled_flag) VALUES ('单元测试','UT',{},'自动化平台','自动化平台',1)".format(mod_id)
            sql_execute.append(sql_type_UT)
        change_db(sql_execute)

    elif type == 'yaml':

        for mod_id, mod_code, in enumerate(data_list.keys(), 1):
            list_py.append(mod_code)

        for i in sql_data:
            list_sq.append(i['m_code'])

        del_data = list(set(list_sq).difference(set(list_py)))
        inp_data = list(set(list_py).difference(set(list_sq)))


        for module in del_data:
            print('更新后删除 [模块编码] {} 中的yaml文件内容 '.format(module))
            sql_pro_yaml = "DELETE FROM ts_yaml WHERE m_code ='{}' AND p_id={}".format(module, parm)
            sql_execute.append(sql_pro_yaml)
        change_db(sql_execute)

        # 初始化执行列表
        sql_execute = []

        parm_name_sql = "SELECT * from ts_iteration LEFT JOIN ts_project ON ts_iteration.p_id=ts_project.id WHERE ts_iteration.id={}".format(parm)
        parm_name = query_db(parm_name_sql)

        pro_id,pro_name,iter_id,iter_code = parm_name[0]['ts_project.id'],parm_name[0]['project_name'],parm_name[0]['id'],parm_name[0]['iter_code']

        # 模块查询sql,为了获取mod_id
        module_sql = "SELECT id,module_code from ts_module where i_id={}".format(parm)
        get_mod_id = format_data('mod', 'name', query_db(module_sql))

        for module_code in inp_data:
            mod_id = get_mod_id[module_code]
            yaml_text = data_list[module_code]['yaml']
            print('更新后增加 [yaml文件] {}'.format(module_code))
            sql_pro_yaml = "INSERT INTO ts_yaml(p_id,p_code,i_id,i_code,m_id,m_code,yaml_text,enabled_flag) VALUES ({},'{}',{},'{}',{},'{}','{}',1)".format(pro_id, pro_name, iter_id, iter_code, mod_id, module_code, yaml_text)
            sql_execute.append(sql_pro_yaml)
        change_db(sql_execute)

    elif type == 'sce':

        for sce_id, sce_code in enumerate(data_list.keys(), 1):
            list_py.append(sce_code)

        for i in sql_data:
            list_sq.append(i['scene_code'])

        del_data = list(set(list_sq).difference(set(list_py)))
        inp_data = list(set(list_py).difference(set(list_sq)))

        for scene in del_data:
            print('更新后删除 [场景编码] {} '.format(scene))
            sql_pro = "DELETE FROM scene WHERE scene_code='{}'".format(scene)
            sql_execute.append(sql_pro)
        change_db(sql_execute)

        sql_execute = []

        for scene_code in inp_data:
            scene_zh = data_list[scene_code]['att'].replace('\"','').replace('\'','')
            print('更新后增加 [场景编码] {} [场景名称] {} '.format(scene_code, scene_zh))
            sql_pro = "INSERT INTO scene(scene_code,scene_name,m_id,scene_level,created_by,updated_by,enabled_flag,scene_type) VALUES('{}','{}',{},1,'自动化平台','自动化平台',1,2)".format(scene_code, scene_zh, parm)
            sql_execute.append(sql_pro)
        change_db(sql_execute)

    elif type == 'case':

        case_level = {
            'blocker': 1,
            'critical': 2,
            'normal': 3,
            'minor': 4,
            'trivial': 5,
        }

        case_mark = {
            'smoke': 1,
            'RT': 2,
            'UT': 3,
        }

        for case_id, case_code in enumerate(data_list.keys(), 1):
            list_py.append(case_code)

        for i in sql_data:
            list_sq.append(i['case_code'])

        del_data = list(set(list_sq).difference(set(list_py)))
        inp_data = list(set(list_py).difference(set(list_sq)))

        for case in del_data:
            print('更新后删除 [用例编码] {} '.format(case))
            sql_pro = "DELETE FROM ts_case WHERE case_code ='{}'".format(case)
            sql_execute.append(sql_pro)
        change_db(sql_execute)

        sql_execute = []

        for case_code in inp_data:

            case_zh = data_list[case_code]['title'].replace("\\", "\\\\").replace('\"','').replace('\'','')
            case_desc = data_list[case_code]['description'].replace("\\", "\\\\").replace('\"','').replace('\'','')
            severity_level = data_list[case_code]['severity'].replace('\"','').replace('\'','')
            case_level_id = case_level[severity_level]
            case_status = data_list[case_code]['status']
            print('更新后增加 [用例编码] {} [用例名称] {} [用例描述] {} [用例等级] {} [执行状态] {} '.format(case_code, case_zh, case_desc, case_level_id, case_status))
            sql_pro = "INSERT INTO ts_case(case_code,case_name,case_des,case_status,s_id,case_level,manager_id,created_by,updated_by,enabled_flag,meta_status) VALUES('{}','{}','{}',{},{},{},1,'自动化平台','自动化平台',1,'unexecuted')".format(case_code, case_zh, case_desc, case_status, parm, case_level_id)
            sql_execute.append(sql_pro)
        change_db(sql_execute)

        # 初始化执行列表
        sql_execute = []

        # 模块查询sql,为了获取mod_id
        case_sql = "SELECT id,case_code from ts_case where s_id = {}".format(parm)

        # 获取最新列表
        get_case_id = format_data('case', 'name', query_db(case_sql))

        for case_code in inp_data:
            case_id = get_case_id[case_code]
        # 添加用例等级
            mark_level = data_list[case_code]['mark']
            print('更新后增加 [用例标记] {} '.format(mark_level))
            for i in mark_level:
                case_mark_id = case_mark[i]
                sql_mark_level = "INSERT INTO ts_casemark_detail(case_id,case_mark_id,created_by,updated_by,enabled_flag) VALUES({},{},1,1,1)".format(case_id, case_mark_id)
                sql_execute.append(sql_mark_level)
        change_db(sql_execute)

    elif type == 'env':

        for env_id, env_code in enumerate(data_list.keys(), 1):
            list_py.append(env_code)

        for i in sql_data:
            list_sq.append(i['env_name'])

        del_data = list(set(list_sq).difference(set(list_py)))
        inp_data = list(set(list_py).difference(set(list_sq)))

        for env in del_data:
            print('更新后删除 [项目环境] {} '.format(env))
            sql_pro = "DELETE FROM ts_env WHERE env_name='{}'".format(env)
            sql_execute.append(sql_pro)
        change_db(sql_execute)

        sql_execute = []

        for env_name in inp_data:
            env_url = data_list[env_name]
            print('更新后增加 [项目环境] {} [环境地址] {} '.format(env_name, env_url))
            sql_pro = "INSERT INTO ts_env(env_name,env_url,p_id,is_enable,created_by,updated_by,enabled_flag) VALUES('{}','{}',{},1,1,1,1)".format(env_name, env_url, parm)
            sql_execute.append(sql_pro)
        change_db(sql_execute)

def del_data(type, data_list):
    if len(data_list) == 0:
        sql_execute = []

        if type == 'env':
            sql_pro = "TRUNCATE ts_env"

        elif type == 'iter':
            sql_pro = "TRUNCATE ts_iteration"

        elif type == 'mod':
            sql_pro = "TRUNCATE ts_module"

        elif type == 'yaml':
            sql_pro = "TRUNCATE ts_yaml"

        elif type == 'test_type':
            sql_pro = "TRUNCATE ts_testtype"

        elif type == 'sce':
            sql_pro = "TRUNCATE scene"

        elif type == 'case':
            sql_pro = "TRUNCATE ts_case"

        elif type == 'mark':
            sql_pro = "TRUNCATE ts_casemark_detail"

        sql_execute.append(sql_pro)
        change_db(sql_execute)
    elif len(data_list) == 1:
        data_list = data_list[0]

        sql_execute = []

        if type == 'env':
            sql_pro = "DELETE FROM ts_env WHERE p_id NOT IN ({})".format(data_list)

        elif type == 'iter':
            sql_pro = "DELETE FROM ts_iteration WHERE p_id NOT IN ({})".format(data_list)

        elif type == 'mod':
            sql_pro = "DELETE FROM ts_module WHERE i_id NOT IN ({})".format(data_list)

        elif type == 'yaml':
            sql_pro = "DELETE FROM ts_yaml WHERE m_id NOT IN ({})".format(data_list)

        elif type == 'test_type':
            sql_pro = "DELETE FROM ts_testtype WHERE m_id NOT IN ({})".format(data_list)

        elif type == 'sce':
            sql_pro = "DELETE FROM scene WHERE m_id NOT IN ({})".format(data_list)

        elif type == 'case':
            sql_pro = "DELETE FROM ts_case WHERE s_id NOT IN ({})".format(data_list)

        elif type == 'mark':
            sql_pro = "DELETE FROM ts_casemark_detail WHERE case_id NOT IN ({})".format(data_list)

        sql_execute.append(sql_pro)
        change_db(sql_execute)
    else:
        sql_execute = []

        if type == 'env':
            sql_pro = "DELETE FROM ts_env WHERE p_id NOT IN {}".format(data_list)

        elif type == 'iter':
            sql_pro = "DELETE FROM ts_iteration WHERE p_id NOT IN {}".format(data_list)

        elif type == 'mod':
            sql_pro = "DELETE FROM ts_module WHERE i_id NOT IN {}".format(data_list)

        elif type == 'yaml':
            sql_pro = "DELETE FROM ts_yaml WHERE m_id NOT IN {}".format(data_list)

        elif type == 'test_type':
            sql_pro = "DELETE FROM ts_testtype WHERE m_id NOT IN {}".format(data_list)

        elif type == 'sce':
            sql_pro = "DELETE FROM scene WHERE m_id NOT IN {}".format(data_list)

        elif type == 'case':
            sql_pro = "DELETE FROM ts_case WHERE s_id NOT IN {}".format(data_list)

        elif type == 'mark':
            sql_pro = "DELETE FROM ts_casemark_detail WHERE case_id NOT IN {};".format(data_list)

        sql_execute.append(sql_pro)
        change_db(sql_execute)

def update_data(type, sql_data, data_list, parm=None):
    sql_execute = []
    list_sq = []
    list_py = []
    iter_list_py = {}
    iter_list_sq = {}
    module_list_py = {}
    module_list_sq = {}
    yaml_list_py = {}
    yaml_list_sq = {}
    env_list_py = {}
    env_list_sq = {}
    scene_list_py = {}
    scene_list_sq = {}
    case_list_py = {}
    case_list_sq = {}

    case_level = {
        'blocker': 1,
        'critical': 2,
        'normal': 3,
        'minor': 4,
        'trivial': 5,
    }

    case_mark = {
        'smoke': 1,
        'RT': 2,
        'UT': 3
    }

    if type == 'mod':
        for mod_id, mod_code, in enumerate(data_list.keys(), 1):
            list_py.append(mod_code)
            module_list_py[mod_code] = data_list[mod_code]['att'].replace('\"','').replace('\'','')
        module_list_py = sorted(module_list_py.items())
        # 格式化字典
        module_list_py_json = {k: v for k, v in module_list_py}
        # print(module_list_py_json)

        for i in sql_data:
            list_sq.append(i['module_code'])
            module_list_sq[i['module_code']] = i['module_name']
        module_list_sq = sorted(module_list_sq.items())
        # 格式化字典
        module_list_sq_json = {k: v for k, v in module_list_sq}
        # print(module_list_sq_json)

        for module_key in module_list_py_json:
            if module_list_sq_json[module_key] != module_list_py_json[module_key]:
                print('同步内容 [模块描述] {} '.format(module_key))
                sql_pro = 'UPDATE ts_module SET module_name="{}" WHERE module_code="{}" AND i_id={}'.format(module_list_py_json[module_key], module_key, parm)
                sql_execute.append(sql_pro)
        change_db(sql_execute)

    if type == 'yaml':
        for mod_id, mod_code, in enumerate(data_list.keys(), 1):
            list_py.append(mod_code)
            yaml_list_py[mod_code] = data_list[mod_code]['yaml'].replace('\\"', '\"').replace( "\\'", "\'")
        yaml_list_py = sorted(yaml_list_py.items())
        # 格式化字典
        yaml_list_py_json = {k: v for k, v in yaml_list_py}
        # print(yaml_list_py_json)

        for i in sql_data:
            list_sq.append(i['m_code'])
            yaml_list_sq[i['m_code']] = i['yaml_text']
        yaml_list_sq = sorted(yaml_list_sq.items())
        # 格式化字典
        yaml_list_sq_json = {k: v for k, v in yaml_list_sq}
        # print(yaml_list_sq_json)

        for module_key in yaml_list_py_json:
            if yaml_list_sq_json[module_key] != yaml_list_py_json[module_key]:
                print('同步内容 [yaml内容] {} '.format(module_key))
                yaml_content = yaml_list_py_json[module_key].replace('\"', '\\"').replace("\'", "\\'")
                sql_pro = "UPDATE ts_yaml SET yaml_text='{}' WHERE m_code='{}' AND i_id={}".format(yaml_content, module_key, parm)
                sql_execute.append(sql_pro)
        change_db(sql_execute)

    if type == 'env':
        env_list_py = data_list
        env_list_py = sorted(env_list_py.items())
        # 格式化字典
        env_list_py_json = {k: v for k, v in env_list_py}
        # print(env_list_py_json)

        for i in sql_data:
            list_sq.append(i['env_name'])
            env_list_sq[i['env_name']] = i['env_url']
        env_list_sq = sorted(env_list_sq.items())
        # 格式化字典
        env_list_sq_json = {k: v for k, v in env_list_sq}
        # print(env_list_sq_json)

        for env_key in env_list_py_json:
            if env_list_sq_json[env_key] != env_list_py_json[env_key]:
                print('同步内容 [环境地址] {} '.format(env_key))
                sql_pro = 'UPDATE ts_env SET env_url="{}" WHERE env_url="{}" AND p_id={}'.format(env_list_py_json[env_key],env_list_sq_json[env_key], parm)
                sql_execute.append(sql_pro)
        change_db(sql_execute)

    if type == 'sce':
        for sce_id, sce_code, in enumerate(data_list.keys(), 1):
            list_py.append(sce_code)
            scene_list_py[sce_code] = data_list[sce_code]['att'].replace('\\"', '\"').replace( "\\'", "\'")
        scene_list_py = sorted(scene_list_py.items())
        # 格式化字典
        scene_list_py_json = {k: v for k, v in scene_list_py}
        # print(scene_list_py_json)

        for i in sql_data:
            list_sq.append(i['scene_code'])
            scene_list_sq[i['scene_code']] = i['scene_name']
        scene_list_sq = sorted(scene_list_sq.items())
        # 格式化字典
        scene_list_sq_json = {k: v for k, v in scene_list_sq}
        # print(scene_list_sq_json)

        for scene_key in scene_list_py_json:
            if scene_list_sq_json[scene_key] != scene_list_py_json[scene_key]:
                sce_content = scene_list_py_json[scene_key].replace('\"', '\\"').replace("\'", "\\'")
                print('同步内容 [场景编码] {} [场景描述] {} '.format(scene_key, sce_content))
                sql_pro = 'UPDATE scene SET scene_name="{}" WHERE scene_code="{}" AND m_id={}'.format(sce_content, scene_key, parm)
                sql_execute.append(sql_pro)
        change_db(sql_execute)

    if type == 'case':
        for case_id, case_code, in enumerate(data_list.keys(), 1):
            list_py.append(case_code)
            python_list = []
            # python_list.append(data_list[case_code]['title'].replace("\\", "\\\\").replace('\"', '').replace("\'", "\\'"))
            python_list.append(data_list[case_code]['title'].replace('\\"', '\"').replace("\\'", "\'"))
            # python_list.append(data_list[case_code]['description'].replace("\\", "\\\\").replace('\"', '').replace("\'", "\\'"))
            python_list.append(data_list[case_code]['description'].replace('\\"', '\"').replace("\\'", "\'"))
            python_list.append(data_list[case_code]['status'])
            python_list.append(str(case_level[data_list[case_code]['severity']]))
            case_list_py[case_code] = python_list

        case_list_py = sorted(case_list_py.items())
        # 格式化字典
        case_list_py_json = {k: v for k, v in case_list_py}
        # print(case_list_py_json)

        for i in sql_data:
            list_sq.append(i['case_code'])
            sqldata_list = []
            sqldata_list.append(i['case_name'])
            sqldata_list.append(i['case_des'])
            sqldata_list.append(i['case_status'])
            sqldata_list.append(i['case_level'])
            case_list_sq[i['case_code']] = sqldata_list

        case_list_sq = sorted(case_list_sq.items())
        # 格式化字典
        case_list_sq_json = {k: v for k, v in case_list_sq}
        # print(case_list_sq_json)

        for case_key in case_list_py_json:
            # print('case_list_py_json----', case_list_py_json)
            # print('case_list_sq_json----', case_list_sq_json)
            if case_list_sq_json[case_key] != case_list_py_json[case_key]:
                case_name_content = case_list_py_json[case_key][0].replace('\"', '\\"').replace("\'", "\\'")
                case_des_content = case_list_py_json[case_key][1].replace('\"', '\\"').replace("\'", "\\'")
                case_status_content = case_list_py_json[case_key][2]
                case_level_content = case_list_py_json[case_key][3]
                print('同步内容 [用例编码] {} [用例名称] {} [用例步骤] {} [用例等级] {} [用例状态] {}'.format(case_key, case_name_content, case_des_content, case_level_content, case_status_content))
                sql_pro = 'UPDATE ts_case SET case_name="{}",case_des="{}",case_status={},case_level={} WHERE case_code="{}" AND s_id={}'.format(case_name_content, case_des_content, case_status_content, case_level_content, case_key, parm)

                sql_execute.append(sql_pro)
        change_db(sql_execute)

    if type == 'mark':
        case_tag_list_py = []
        case_tag_list_sq = []
        if len(data_list) != 0:
            if len(sql_data) != 0:
                for i in sql_data:
                    case_tag_list_sq.append(i['case_mark_id'])

                for k in data_list:
                    case_tag_list_py.append(case_mark[k])

                ins_mark = list(set(case_tag_list_py).difference(set(case_tag_list_sq)))
                del_mark = list(set(case_tag_list_sq).difference(set(case_tag_list_py)))

                if len(del_mark) != 0:
                    print('同步内容 [删除用例标记] {} '.format(del_mark))
                    for mark_id in del_mark:
                        sql_pro = "DELETE FROM ts_casemark_detail WHERE case_id={} AND case_mark_id={}".format(parm, mark_id)
                        sql_execute.append(sql_pro)

                if len(ins_mark) != 0:
                    print('同步内容 [增加用例标记] {} '.format(ins_mark))
                    for mark_id in ins_mark:
                        sql_pro = "INSERT INTO ts_casemark_detail(case_id,case_mark_id,created_by,updated_by,enabled_flag) VALUES({},{},1,1,1)".format(parm, mark_id)
                        sql_execute.append(sql_pro)

        change_db(sql_execute)

def music(music_name,a):
    print('正在下载{}{}'.format(music_name,a))
    sleep(2)
    print('{}下载成功'.format(music_name))
def sync_Data(data_list, env_list=None):

    # 项目查询sql
    project_sql = "SELECT id,project_name from ts_project"
    # 查找出py文件和数据库项目数据的差异并进行操作
    algo_data('pro', query_db(project_sql), data_list)
    # 查找最新数据ts_project表的数据并格式化
    pro_list = format_data('pro', 'name', query_db(project_sql))

    n = len(pro_list.keys())

    with ThreadPoolExecutor(max_workers=6) as executor:
        executor.map(thread_task, [data_list] * n,[env_list] * n, pro_list.keys())

def thread_task(data_list, env_list=None, pro_code=None):

    # 项目查询sql
    project_sql = "SELECT id,project_name from ts_project"

    # 查找最新数据ts_project表的数据并格式化
    pro_list = format_data('pro', 'name', query_db(project_sql))

    # 获取最新项目对应id
    pro_id = pro_list[pro_code]

    # 存储每个项目数据
    pro_data_list = data_list[pro_code]
    env_data_list = env_list[pro_code]

    # 环境查询sql
    env_sql = "SELECT id,env_name,env_url from ts_env where p_id={}".format(pro_id)

    # 查找出py文件和数据库项目数据的差异并进行操作
    algo_data('env', query_db(env_sql), env_data_list, pro_id)

    # 查找出py文件和数据库环境数据的差异并进行輸入操作
    update_data('env', query_db(env_sql), env_data_list, pro_id)

    # 模块查询sql
    iter_sql = "SELECT id,iter_code,iter_name from ts_iteration where p_id = {}".format(pro_id)

    # 查找出py文件和数据库项目数据的差异并进行輸入操作
    algo_data('iter', query_db(iter_sql), pro_data_list, pro_id)

    # 项目查询sql
    iter_sql = "SELECT id,iter_code from ts_iteration where p_id = {}".format(pro_id)

    # 查找最新数据ts_project表的数据并格式化
    iter_list = format_data('iter', 'name', query_db(iter_sql))

    # 遍历出每个模块数据
    for iter_code in pro_data_list:

        # 获取最新项目对应id
        iter_id = iter_list[iter_code]

        # 存储每个项目数据
        iter_data_list = pro_data_list[iter_code]

        # 模块查询sql
        module_sql = "select ts_module.id,ts_module.module_code,ts_module.module_name,ts_yaml.yaml_text from ts_module LEFT JOIN ts_yaml ON ts_module.id = ts_yaml.m_id WHERE ts_module.i_id = {}".format(iter_id)

        # 查找出py文件和数据库项目数据的差异并进行輸入操作
        algo_data('mod', query_db(module_sql), iter_data_list, iter_id)

        # 查找出py文件和数据库项目数据的差异并进行輸入操作
        update_data('mod', query_db(module_sql), iter_data_list, iter_id)

        # 模块yaml查询sql
        yaml_sql = "SELECT id,p_id,p_code,i_id,i_code,m_id,m_code,yaml_text from ts_yaml where p_id={} and i_id={}".format(pro_id, iter_id)

        # 查找出py文件和数据库项目数据的差异并进行操作
        algo_data('yaml', query_db(yaml_sql), iter_data_list, iter_id)

        # 查找出py文件和数据库环境数据的差异并进行輸入操作
        update_data('yaml', query_db(yaml_sql), iter_data_list, iter_id)

        # 查找最新数据ts_module表的数据并格式化
        mod_list = format_data('mod', 'name', query_db(module_sql))

        # 遍历出每个模块数据
        for mod_code in iter_data_list:

            # # 获取最新模块对应id
            mod_id = mod_list[mod_code]
            # 存储每个模块数据
            mod_data_list = iter_data_list[mod_code]['value']

            # 场景查询sql
            scene_sql = "SELECT scene_id,scene_code,scene_name from scene where m_id = {}".format(mod_id)

            # 查找出py文件和数据库项目数据的差异并进行操作
            algo_data('sce', query_db(scene_sql), mod_data_list, mod_id)

            # 查找出py文件和数据库项目数据的差异并进行操作
            update_data('sce', query_db(scene_sql), mod_data_list, mod_id)

            # 查找最新数据ts_module表的数据并格式化
            sce_list = format_data('sce', 'name', query_db(scene_sql))

            # 遍历出每个场景数据
            for sce_code in mod_data_list:

                # 获取最新场景对应id
                sce_id = sce_list[sce_code]

                # 存储每个场景数据
                sce_data_list = mod_data_list[sce_code]['value']

                # 用例查询sql
                case_sql = "SELECT id,case_code,case_name,case_des,case_status,case_level from ts_case where s_id = {}".format(sce_id)

                # 查找出py文件和数据库项目数据的差异并进行操作
                algo_data('case', query_db(case_sql), sce_data_list, sce_id)

                # 查找出py文件和数据库项目数据的差异并进行操作
                update_data('case', query_db(case_sql), sce_data_list, sce_id)

                # 查找最新数据ts_module表的数据并格式化
                case_list = format_data('case', 'name', query_db(case_sql))

                for case_code in sce_data_list:
                    # 获取最新场景对应id
                    case_id = case_list[case_code]
                    # 存储每个场景数据
                    case_data_list = sce_data_list[case_code]['mark']

                    # 用例查询sql
                    case_sql = "SELECT id,case_id,case_mark_id from ts_casemark_detail where case_id={}".format(case_id)

                    # 查找出py文件和数据库项目数据mark的差异并进行操作
                    update_data('mark', query_db(case_sql), case_data_list, case_id)

def clear_data():
    # 项目查询sql
    project_sql = "SELECT id,project_name from ts_project"

    # 模块查询sql
    iter_sql = "SELECT id,iter_code from ts_iteration"

    # 模块查询sql
    module_sql = "SELECT id,module_code from ts_module"

    # 场景查询sql
    scene_sql = "SELECT scene_id,scene_code from scene"

    # 用例查询sql
    case_sql = "SELECT id,case_code from ts_case"

    # 查找最新数据ts_project表的数据并格式化
    pro_list = format_data('pro', 'id', query_db(project_sql))

    # 获取最新project_id list
    pro_id_list = tuple(pro_list.keys())

    # 清除环境多余数据
    del_data('env', pro_id_list)

    # 清除模块多余数据
    del_data('iter', pro_id_list)

    # 查找最新数据ts_project表的数据并格式化
    iter_list = format_data('iter', 'id', query_db(iter_sql))

    # 获取最新iter_id_list
    iter_id_list = tuple(iter_list.keys())

    # 清除模块多余数据
    del_data('mod', iter_id_list)

    # 查找最新数据ts_module表的数据并格式化
    mod_list = format_data('mod', 'id', query_db(module_sql))

    # 获取最新mod_id list
    mod_id_list = tuple(mod_list.keys())

    # 清除元素定位多余数据
    del_data('yaml', mod_id_list)

    # 清除场景多余数据
    del_data('sce', mod_id_list)

    # 清除测试类型多余数据
    del_data('test_type', mod_id_list)

    # 查找最新数据ts_module表的数据并格式化
    sce_list = format_data('sce', 'id', query_db(scene_sql))

    # 获取最新sce_id list
    sce_id_list = tuple(sce_list.keys())

    # 清除用例多余数据
    del_data('case', sce_id_list)

    # 查找最新数据ts_module表的数据并格式化
    case_list = format_data('case', 'id', query_db(case_sql))

    # 获取最新case_id list
    case_id_list = tuple(case_list.keys())

    # 清除标记多余数据
    del_data('mark', case_id_list)

if __name__ == '__main__':
    # 区分环境选择配置
    run_env(sys.argv[1])

    # print(get_env())
    # print(get_Data())

    # 同步所有数据（覆盖）
    # sync_AllData(get_Data(),get_env())

    # 同步所有数据（增量）
    sync_Data(get_Data(), get_env())
    clear_data()

