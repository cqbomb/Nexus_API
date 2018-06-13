from flask import Flask,render_template

application = Flask(__name__)

class MyItem:
	def __init__(self,id,name):
		self.id = id
		self.name = name

@application.route("/")
def index():
	return render_template('for.txt',products = ['secie','dcie','rsie','wirelessie','ispie'],\
									 items = [{'id':1,'name':'Ender'},\
									 		  {'id':2,'name':'Collinsctk'},\
									 		  {'id':3,'name':'Tina'},\
									 		  MyItem(4,'qytang')])

if __name__ == "__main__":
    application.run(host = '0.0.0.0',port = '8888')
