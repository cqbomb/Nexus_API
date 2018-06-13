from flask import Flask,render_template

application = Flask(__name__)

#模板文件放入templates目录
@application.route("/")
def index():
    return render_template('index.html')#转载模板文件

@application.route("/user/<name>")
def user(name):
    return render_template('user.html',template_name1=name)#替换模板文件内的参数

if __name__ == "__main__":
    application.run(host = '0.0.0.0',port = '8888')
