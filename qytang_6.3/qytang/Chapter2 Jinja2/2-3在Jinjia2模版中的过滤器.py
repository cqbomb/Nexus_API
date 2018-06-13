from flask import Flask,render_template

application = Flask(__name__)

#模板文件(添加过滤器)放入templates目录
@application.route("/")
def index():
	return render_template('filter.txt',name='qinke',value='welcome to qytang!')#转载模板文件
"""
Jinja2支持的过滤器

safe:渲染值时不转移
capitalize:首字母大写，其他为小写
lower:全部变成小写
upper:全部变成大写
title:把每个单词的首字母都换成大写
trim:把值的首尾空格去掉
striptags:渲染之前把值中所有的HTML标签都去掉
"""

if __name__ == "__main__":
    application.run(host = '0.0.0.0',port = '8888')
