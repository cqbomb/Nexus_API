from flask import Flask
from flask import request
from flask import redirect
from flask import make_response
from datetime import *

application = Flask(__name__)

@application.route("/")
def index():
	#此处使用make_response与正常return没有区别
    response = make_response('<h1>This document is response text</h1>')
    return response

@application.route("/writecookie/<cv>")
def writeCookie(cv):
	#写入Cookie值与过期时间
    response = make_response('<h1>Cookie已写入</h1>')
    #严重注意过期时间使用了utc,因为游览器总是认为服务器回送的是utc 0的格林威治时间
    outdate = datetime.utcnow() + timedelta(seconds = 20)
    print(outdate)
    response.set_cookie('cv',cv,expires = outdate)
    return response

@application.route("/readcookie")
def readCookie():
	#读取Cookie，并且判断Cookie超时！
    value = request.cookies.get('cv')
    print(value)
    if value == None:
    	value = 'Cookie失效'
    return value

@application.route('/redirect_cookie')
def cookie_insertion():
    redirect_to_index = redirect('/')
    response = make_response(redirect_to_index)  
    response.set_cookie('cookie_name',value='values')
    return response

if __name__ == "__main__":
    application.run(host = '0.0.0.0')
