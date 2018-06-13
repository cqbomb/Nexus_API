from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

application = Flask(__name__)

#静态路由
@application.route("/")
def hello():
    return "<h1 style='color:blue'>Welcome to qytang!</h1>"

@application.route("/greet")
def greet():
	return "<h1>Hello everyone</h1>"

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
    application.run(host = '0.0.0.0')
