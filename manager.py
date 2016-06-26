# -*- coding: utf-8 -*-
#让脚本和系统分开来
from flask_script import Manager
from falsk_test02 import app

manger = Manager(app)

# @manger.command
# def hello(name):
#     print 'hello',name

@manger.command
def initialize_database():
    #一些数据库的管理
    'initialize database'
    print 'databsae...'

@manger.option('-n','--name',dest='name',default='nowcoder')
def hello(name):
    print 'hello',name

if __name__ == '__main__':
    manger.run()