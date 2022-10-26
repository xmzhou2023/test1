#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import ast
import os
import configparser
from libs.config.conf import PEROJECT_PATH

class ReadConfig:
    """配置文件"""
    def __init__(self, name, env, ini_name=None, values=None):
        INI_PATH = os.path.join(PEROJECT_PATH, name, 'env', env, 'config.ini')
        if not os.path.exists(INI_PATH):
            raise FileNotFoundError("配置文件%s不存在！" % INI_PATH)
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(INI_PATH, encoding='utf-8')
        self.ini_name = ini_name
        self.values = values

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(INI_PATH, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get('HOST', 'url')

    @property
    def db(self):
        return self._get('SQL', 'db')

    @property
    def IPM_db(self):
        return self._get(self.ini_name, self.values)

    @property
    def MIP_db(self):
        return self._get(self.ini_name, self.values)

if __name__ == '__main__':
    ini = ReadConfig('DRP','test')
    sql = ast.literal_eval(ini.db)
    inis = ReadConfig('IPM', 'test','database','db_ipm_config_uat')
    sql_IPM = ast.literal_eval(inis.IPM_db)
    inim = ReadConfig('MIP', 'test','database','ms_platform_test')
    sql_MIP = ast.literal_eval(inis.MIP_db)
    print(ini.url)
    print(sql)
    print(sql_IPM)
