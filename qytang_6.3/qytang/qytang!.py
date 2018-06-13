from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

application = Flask(__name__, instance_relative_config=True)#获取instance目录内config.py的配置

application.config.from_object('config')#读取config.py内的配置
application.config.from_pyfile('config.py')#读取instance/config.py内的配置，后加载优先

application.debug = application.config['DEBUG']#激活debug

toolbar = DebugToolbarExtension(application)

#静态路由
@application.route("/")
def hello():
    return "<body><h1 style='color:blue'>Welcome to qytang!</h1><h1>"+application.config['USERNAME']+"</h1></body>"
    #要插入toolbar一定要有body
    
@application.route("/greet")
def greet():
	return "<body><h1>Hello everyone</h1></body>"

#动态路由
@application.route("/greet/<name>")
def greetName(name):
	return "<h1>Hello my {}</h1>".format(name)

@application.route("/greet/<a1>/<a2>/<a3>")
def args1(a1,a2,a3):
	return "<h1>{},{},{}</h1>".format(a1,a2,a3)

@application.route("/greet/<a1>-<a2>-<a3>")
def args2(a1,a2,a3):
	return "<h1>{}*{}*{}</h1>".format(a1,a2,a3)

#测试静态路由优先
@application.route("/greet/qinke")
def greetqinke():
	return "<h1>Hello qinke</h1>"

if __name__ == "__main__":
    application.run()
