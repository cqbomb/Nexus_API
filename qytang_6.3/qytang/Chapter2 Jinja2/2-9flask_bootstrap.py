from flask import Flask,render_template
from flask_bootstrap import Bootstrap

application = Flask(__name__)
bootstrap = Bootstrap(application)

@application.route("/")
def index():
	return render_template('bs.txt',name='qytang')

if __name__ == "__main__":
    application.run(host = '0.0.0.0',port = '8888')
