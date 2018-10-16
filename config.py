# -*- coding: utf-8 -*-
# @Time    :2018/6/14
# @Author  :songtao

import os
import pymysql.cursors

BASEPATH = os.path.dirname(__file__)

SESSION_EXPIRES_SECONDS = 72000 #session失效时间
#Appliaction 配置
settings = {
    'static_path':os.path.join(os.path.dirname(__file__), 'static'),
    'template_path':os.path.join(os.path.dirname(__file__), 'template'),
    'cookie_secret':'ssdsdfdsiwaeijsdcnjiucdsfjkk',
    'xsrf_cookies':False,
    'debug':False,
}

#mysql配置
# mysql_options = {
#     'host':'192.168.1.64',
#     'database':'trade_data',
#     'user':'root',
#     'password':'123456',
#     'charset':'utf8',
#     'port': 3306,
#     'cursorclass': pymysql.cursors.DictCursor
# }

mysql_options = {
    'host':'54.95.38.134',
    'database':'bitup_sys',
    'user':'bitup',
    'password':'Up=8u5e3W4Rjhfy8U4',
    'charset':'utf8',
    'port': 4423,
    'cursorclass': pymysql.cursors.DictCursor
}

#redis配置
redis_options = {
    'host':'172.20.10.11',
    'port':6379,
    'socket_timeout':10
}

log_level = 'info'
