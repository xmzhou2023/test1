# coding:utf-8

import os
import configparser

configpath  = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + r"/data/DRP/config.ini")

conf = configparser.ConfigParser()
conf.read(configpath,encoding="utf-8")

env = conf.get('Environ','env')
environ = '/env/' + env + '/envConfig.yaml'


if __name__ == '__main__':
    print(env,environ)
