from flask import Flask,render_template
from flask_bootstrap import Bootstrap

application = Flask(__name__)
bootstrap = Bootstrap(application)

@application.route("/")
def index():
	return render_template('error.txt',name='qytang')

@application.route("/500")
def error_500():
	raise Exception('服务器内部错误，请检查代码')
	return render_template('error.txt',name='qytang')

@application.errorhandler(404)
def page_not_found(e):
	print(e)
	return render_template('404.txt'),404

@application.errorhandler(500)
def internal_server_error(e):
	print(e)
	return render_template('500.txt',error=e),500


if __name__ == "__main__":
    application.run(host = '0.0.0.0',port = '8888')
