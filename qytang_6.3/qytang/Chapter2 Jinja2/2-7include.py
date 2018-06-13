from flask import Flask,render_template

application = Flask(__name__)

class MyItem:
	def __init__(self,id,name):
		self.id = id
		self.name = name

@application.route("/")
#使用macro.txt内部的宏
def index():
	return render_template('include.txt',\
							items1 = [{'id':11,'name':'Ender11'},\
									 {'id':12,'name':'Collinsctk12'},\
									 {'id':13,'name':'Tina13'},\
									 MyItem(14,'qytang14')],\
							items2 = [{'id':21,'name':'Ender21'},\
									 {'id':22,'name':'Collinsctk22'},\
									 {'id':23,'name':'Tina23'},\
									 MyItem(24,'qytang24')],\
							items3 = ({'id':31,'name':'Ender31'},\
									 {'id':32,'name':'Collinsctk32'},\
									 {'id':33,'name':'Tina33'},\
									 MyItem(34,'qytang34')),\
									 )


if __name__ == "__main__":
    application.run(host = '0.0.0.0',port = '8888')
