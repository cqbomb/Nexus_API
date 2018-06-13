from flask import Flask,render_template

application = Flask(__name__)

"""
1.如何写条件控制语句
2.条件什么情况下为True，什么情况下为False

Python为假的情况:
1.False
2.None
3.空列表
4.空字典
5.空字符串

Jinjia2为假的情况:
1.变量不存在
2.字符串为空（长度为0）
3.数值为0或者0.0
4.空列表
5.空字典
6.None
"""
@application.route("/")
def index():#Jinja2当变量不存在时也为假！
	return render_template('if.txt')

@application.route("/user/")
def user():
	return render_template('if.txt',user = '', \
									intValue = 15, \
									list = [1,2,3],\
									dict = {1:1},\
									value = None)
	#return render_template('if.txt',user = 'qinke')

if __name__ == "__main__":
    application.run(host = '0.0.0.0',port = '8888')
