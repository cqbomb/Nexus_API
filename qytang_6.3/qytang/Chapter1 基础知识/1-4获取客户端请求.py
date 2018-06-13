from flask import Flask
from flask import request

application = Flask(__name__)

#获取头部信息
@application.route("/get_headers")
def get_headers():
    user_agent = request.headers.get('User-Agent')
    return "<h1>Your browser is {}".format(user_agent)

#获取参数信息，request不是全局的，它获取每一个进程的请求
@application.route("/get_args")
def get_args():
    value1 = request.args.get('arg1')
    value2 = request.args.get('arg2')
    return "<h1>arg1 = {},arg2 = {}".format(value1,value2)

if __name__ == "__main__":
    application.run(host = '0.0.0.0')
