from flask import Flask
from flask import request
from flask import session
from datetime import *

application = Flask(__name__)

@application.route("/")
def index():
	#http://nginx.qytang.com:5000/
    if 'username' in session:#判断用户是否登录，session为字典
        return '已经登录 {}'.format(session['username'])
    return "未登录"

@application.route("/login")
def login():
    #http://nginx.qytang.com:5000/login?username=qinke
    session.permanent = True
    session['username'] = request.args.get('username')#设置用户名到字典
    return "登录成功"

@application.route("/logout")
def logout():
    #http://nginx.qytang.com:5000/logout
    session.pop('username',None)#如果有就删除，如果没有就返回None
    return "注销成功"

application.secret_key = 'qytangccies'
application.permanent_session_lifetime = timedelta(seconds = 20)

if __name__ == "__main__":
    application.run(host = '0.0.0.0')