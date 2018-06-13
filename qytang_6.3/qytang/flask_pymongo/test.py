from flask import Flask
from flask_pymongo import PyMongo

application = Flask(__name__)

application.config['QYTANG_HOST'] = 'mongodb.qytang.com'
application.config['QYTANG_PORT'] = 27017
application.config['QYTANG_DBNAME'] = 'qytang'
application.config['QYTANG_USERNAME'] = 'qytangadmin'
application.config['QYTANG_PASSWORD'] = 'Cisc0123'
qytangdb = PyMongo(application, config_prefix='QYTANG')

@application.route("/pymongo/<name>")
def pymongotest(name):
	user = qytangdb.db.users.find_one_or_404({'user':name})#返回的为整行的字典
	return "<h1>Hello my {}</h1>".format(user['user'])#提取字典的键

if __name__ == "__main__":
    application.run(host = '0.0.0.0')
