# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, make_response, redirect,flash,get_flashed_messages
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)  # 定义一个应用

app.jinja_env.line_statement_prefix = '/'

app.secret_key = 'nowcoder'

@app.route('/profile/<int:uid>/', methods=['GET', 'POST'])
def profile_method(uid):
    colors = ('red', 'green')  # tumple
    infos = {'nowcoder': 'abc', 'google': 'def'}
    return render_template('profile.html', uid=uid, colors=colors, infos=infos)


# import make_response,request
@app.route('/request')
def request_demo():
    key = request.args.get('key', 'defaultkey')
    res = request.args.get('key', 'defaultkey') + '<br>'
    res = res + request.url + '++' + request.path + '<br>'
    for property in dir(request):
        res = res + str(property) + '|==|<br>' + str(eval('request.' + property)) + '<br>'
    response = make_response(res)
    response.set_cookie('nowcoderid', key)
    response.status = '404'
    response.headers['nowcoder'] = 'hello~'
    return response


# 重定向 import redirect
# 301：永久转移
# 302: 临时转移
@app.route('/newpath')
def newpath():
    return 'newpath'


@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('newpath', code=code)

# error
# @app.errorhandler(404)
# def page_not_found(error):
#     print error
#     return render_template('not_found.html', url=request.url),404

#Flash message,import flash,get_flashed_messages
# 要设置一个app.secret_key，保证session_id能够产生，保证服务器能够识别是否是同一个人
@app.route('/')
def index():
    res = ''
    for msg,category in get_flashed_messages(with_categories=True):
        res = res + category + msg + '<br>'
    res += 'hello'
    return res

@app.route('/login')
def login():
    app.logger.info('log success')
    flash('登录成功','info')
    return 'ok'
    # return redirect('/')#跳转到首页上去

@app.route('/log/<level>/<msg>/')
def log(level,msg):
    dict = {'warn':logging.WARN,'error':logging.ERROR,'info':logging.INFO}
    if dict.has_key(level):
        app.logger.log(dict[level],msg)
    return 'logged:'+ msg

#Log 形成报表，查漏问题，INFO>WARN>ERROR
# import logging
# from logging.handlers import RotatingFileHandler
#@app.logger.log(level, msg)
def set_logger():
    info_file_handler= RotatingFileHandler('C:\\Users\\Administrator\\Desktop\\info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)

    warn_file_handler= RotatingFileHandler('C:\\Users\\Administrator\\Desktop\\warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)

    error_file_handler= RotatingFileHandler('C:\\Users\\Administrator\\Desktop\\error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)

if __name__ == '__main__':
    set_logger()
    app.run(debug=True)


# html 调用模版
# ｛% macro render_color(color) %｝
#     <div>This is color {{color}} <br>{{ caller() }}</div>
# {% endmacro %}
#
# ｛% for color in colors: %｝
#     ｛% call render_color(color) %｝
#         render_color_demo
#     ｛% endcall %｝
# ｛% endfor %｝








