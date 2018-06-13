# -*- coding: utf-8 -*-  
from flask import Flask, jsonify, render_template, request  
app = Flask(__name__)  

test_list = []

def qytangtest(i):
	finish = 0
	global test_list
	for x in range(i):
		test_list.append((i,finish))
	else:
		test_list.append((0,1))

@app.route("/")  
def index():  
# 主页面  
    return render_template("ajax_test_3.html")  
     
@app.route('/add')  
def add_numbers(): 
    input_int = request.args.get('input_int',type=int)
    print(input_int)
    for i in range(input_int):
        return jsonify(result = i)  
     
if __name__=="__main__":  
    app.run(host = "0.0.0.0", debug = True) 