# -*- coding: utf-8 -*-
'''
HTTP Method
1、GET:获取接口信息；
2、HEAD:紧急查看接口HTTP的头
3、POST:提交数据到服务器
4、PUT:支持幂等性的POST，幂等性（方法调用两次结果相同，防止服务器出错）
5、DELETE:删除服务器上的资源
6、OPITIONS:查看支持的方法
一般网站只用GET和POST，代表获取和更新，html的form仅支持GET和POST
'''

from flask import Flask

app = Flask(__name__)  # 定义一个应用


@app.route('/index/')
@app.route('/')  # 装饰器
def index():
    return 'hello'


@app.route('/profile/<uid>/')  # <>可以理解为正则匹配
def profile(uid):
    return 'profile:' + uid


#  '/' 结尾会自动补齐
@app.route('/profilex/<int:uid>/')  # 这里指定是int，uid必须为数字
def profilex(uid):
    return 'profile:' + str(uid)


@app.route('/profile_method/<int:uid>/', methods=['GET', 'POST'])
def profile_method(uid):
    return 'profile:' + str(uid)


if __name__ == '__main__':
    app.run(debug=True)
