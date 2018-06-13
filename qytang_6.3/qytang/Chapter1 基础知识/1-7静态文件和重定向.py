from flask import *

application = Flask(__name__)


@application.route("/test")
def test():
	#隐视访问最终客户看到http://nginx.qytang.com:5000/test
    return application.send_static_file('test.txt')#直接就可以访问static目录下的test.txt文件

@application.route("/abc")
def abc():
	#显视重定向最终客户看到http://nginx.qytang.com:5000/static/test.txt
    return redirect('/static/test.txt')

if __name__ == "__main__":
    application.run(host = '0.0.0.0')